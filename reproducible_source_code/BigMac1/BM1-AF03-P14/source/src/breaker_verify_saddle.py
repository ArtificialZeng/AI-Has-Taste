#!/usr/bin/env python3
"""Fail-closed exact verifier for the Q5 quadratic saddle certificate.

The verifier uses only the Python standard library.  It reconstructs the
active box-spline chamber from all 32 sign vectors, differentiates the
positive-part numerator through degree two, checks exact stationarity in
Q[t]/(39t^2-48t+13), and certifies the tangent Hessian signature by the
S_2 x S_3 invariant decomposition.  It does not import discovery code or
trust stored gradient/Hessian values.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


def fail(message: str) -> "None":
    raise SystemExit("REJECT: " + message)


def reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            fail(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def reject_booleans(value: object, path: str = "$") -> None:
    if type(value) is bool:
        fail(f"boolean forbidden in certificate at {path}")
    if type(value) is dict:
        for key, child in value.items():
            reject_booleans(child, f"{path}.{key}")
    elif type(value) is list:
        for index, child in enumerate(value):
            reject_booleans(child, f"{path}[{index}]")


@dataclass(frozen=True)
class Quad:
    """Element c0+c1*t of Q[t]/(39*t^2-48*t+13)."""

    c0: Fraction
    c1: Fraction = Fraction(0)

    def __add__(self, other: object) -> "Quad":
        other = as_quad(other)
        return Quad(self.c0 + other.c0, self.c1 + other.c1)

    __radd__ = __add__

    def __neg__(self) -> "Quad":
        return Quad(-self.c0, -self.c1)

    def __sub__(self, other: object) -> "Quad":
        return self + (-as_quad(other))

    def __rsub__(self, other: object) -> "Quad":
        return as_quad(other) - self

    def __mul__(self, other: object) -> "Quad":
        other = as_quad(other)
        # t^2=(48t-13)/39.
        return Quad(
            self.c0 * other.c0 - Fraction(13, 39) * self.c1 * other.c1,
            self.c0 * other.c1
            + self.c1 * other.c0
            + Fraction(48, 39) * self.c1 * other.c1,
        )

    __rmul__ = __mul__

    def inverse(self) -> "Quad":
        # Solve [[a,-13b/39],[b,a+48b/39]] [c,d]^T=[1,0]^T.
        a, b = self.c0, self.c1
        A, B, C, D = a, -Fraction(13, 39) * b, b, a + Fraction(48, 39) * b
        determinant = A * D - B * C
        if determinant == 0:
            fail("division by zero in quadratic field")
        return Quad(D / determinant, -C / determinant)

    def __truediv__(self, other: object) -> "Quad":
        return self * as_quad(other).inverse()

    def __rtruediv__(self, other: object) -> "Quad":
        return as_quad(other) / self

    def __pow__(self, exponent: int) -> "Quad":
        if not isinstance(exponent, int) or exponent < 0:
            fail("unsupported quadratic-field exponent")
        result = Quad(Fraction(1))
        base = self
        power = exponent
        while power:
            if power & 1:
                result = result * base
            base = base * base
            power //= 2
        return result

    def is_zero(self) -> bool:
        return self.c0 == 0 and self.c1 == 0


def as_quad(value: object) -> Quad:
    if isinstance(value, Quad):
        return value
    if isinstance(value, (int, Fraction)):
        return Quad(Fraction(value))
    fail("non-exact scalar encountered")


def parse_fraction(value: object) -> Fraction:
    if not isinstance(value, str):
        fail("rational endpoints must be strings")
    try:
        answer = Fraction(value)
    except (ValueError, ZeroDivisionError):
        fail("invalid rational endpoint")
    return answer


def sign_at_isolated_root(value: Quad, left: Fraction, right: Fraction) -> int:
    if value.is_zero():
        return 0
    endpoint = left if value.c1 >= 0 else right
    lower = value.c0 + value.c1 * endpoint
    endpoint2 = right if value.c1 >= 0 else left
    upper = value.c0 + value.c1 * endpoint2
    if lower > 0:
        return 1
    if upper < 0:
        return -1
    fail("isolating interval cannot decide an algebraic sign")


def dot(vector1: list[Quad], vector2: list[Quad]) -> Quad:
    if len(vector1) != len(vector2):
        fail("dimension mismatch")
    return sum((x * y for x, y in zip(vector1, vector2)), Quad(Fraction(0)))


def mat_vec(matrix: list[list[Quad]], vector: list[Quad]) -> list[Quad]:
    return [dot(row, vector) for row in matrix]


def quadratic(matrix: list[list[Quad]], vector: list[Quad]) -> Quad:
    return dot(vector, mat_vec(matrix, vector)) / dot(vector, vector)


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: breaker_verify_saddle.py CERTIFICATE.json")
    certificate_path = Path(sys.argv[1])
    try:
        raw = certificate_path.read_bytes()
        data = json.loads(raw, object_pairs_hook=reject_duplicate_keys)
    except (OSError, json.JSONDecodeError):
        fail("unreadable certificate")
    reject_booleans(data)
    expected_keys = {
        "schema",
        "minimal_polynomial_constant_first",
        "root_interval",
        "unnormalized_vector",
        "expected_active_sign_vectors",
        "expected_tangent_signature",
    }
    if not isinstance(data, dict) or set(data) != expected_keys:
        fail("wrong or incomplete top-level schema")
    if data["schema"] != "q5-quadratic-saddle-v1":
        fail("unsupported schema")
    if data["minimal_polynomial_constant_first"] != [13, -48, 39]:
        fail("unexpected minimal polynomial")
    interval = data["root_interval"]
    if not isinstance(interval, dict) or set(interval) != {"left", "right"}:
        fail("invalid interval object")
    left, right = parse_fraction(interval["left"]), parse_fraction(interval["right"])
    if not (0 < left < right < Fraction(2, 3)):
        fail("interval is not contained in the claimed open chamber")
    polynomial = lambda x: 39 * x * x - 48 * x + 13
    # The derivative is negative throughout this short interval.  Endpoint
    # signs then isolate exactly one (the smaller) real root.
    if not (78 * right - 48 < 0 and polynomial(left) > 0 > polynomial(right)):
        fail("interval does not isolate the intended root")
    if data["unnormalized_vector"] != ["1", "1", "t", "t", "t"]:
        fail("unexpected vector encoding")
    if data["expected_active_sign_vectors"] != 16:
        fail("unexpected active-sign count")
    if data["expected_tangent_signature"] != {"positive": 1, "negative": 3, "zero": 0}:
        fail("unexpected claimed signature")

    zero, one, t = Quad(Fraction(0)), Quad(Fraction(1)), Quad(Fraction(0), Fraction(1))
    a = [one, one, t, t, t]
    G = zero
    grad_G = [zero for _ in range(5)]
    hess_G = [[zero for _ in range(5)] for _ in range(5)]
    active_count = 0
    for eps in itertools.product((-1, 1), repeat=5):
        linear = sum((Fraction(eps[i], 2) * a[i] for i in range(5)), zero)
        linear_sign = sign_at_isolated_root(linear, left, right)
        if linear_sign == 0:
            fail("candidate lies on a subset-sum wall")
        if linear_sign < 0:
            continue
        active_count += 1
        coeff = -1 if sum(e == -1 for e in eps) % 2 else 1
        G += coeff * linear**4
        for i in range(5):
            li = Fraction(eps[i], 2)
            grad_G[i] += coeff * 4 * linear**3 * li
            for j in range(5):
                lj = Fraction(eps[j], 2)
                hess_G[i][j] += coeff * 12 * linear**2 * li * lj
    if active_count != data["expected_active_sign_vectors"]:
        fail("active chamber reconstruction disagrees")
    if sign_at_isolated_root(G, left, right) <= 0:
        fail("box-spline numerator is not positive")

    r2 = dot(a, a)
    grad_log: list[Quad] = []
    hess_log = [[zero for _ in range(5)] for _ in range(5)]
    for i in range(5):
        grad_log.append(a[i] / r2 + grad_G[i] / G - one / a[i])
        for j in range(5):
            delta = one if i == j else zero
            hess_log[i][j] = (
                delta / r2
                - 2 * a[i] * a[j] / r2**2
                + hess_G[i][j] / G
                - grad_G[i] * grad_G[j] / G**2
                + (delta / a[i] ** 2)
            )
    if not all(entry.is_zero() for entry in grad_log):
        fail("candidate is not exactly stationary")

    # Orthogonal S_2 x S_3 decomposition of the four-dimensional tangent
    # space: X-antisymmetric (1D), Y-standard (2D), and group contrast (1D).
    ux = [one, -one, zero, zero, zero]
    uy1 = [zero, zero, one, -one, zero]
    uy2 = [zero, zero, one, one, -2 * one]
    contrast = [3 * t, 3 * t, -2 * one, -2 * one, -2 * one]
    vectors = [ux, uy1, uy2, contrast]
    if not all(dot(a, vector).is_zero() for vector in vectors):
        fail("purported signature basis is not tangent")
    for i in range(4):
        for j in range(i):
            if not dot(vectors[i], vectors[j]).is_zero():
                fail("signature decomposition is not orthogonal")
            if not dot(vectors[i], mat_vec(hess_log, vectors[j])).is_zero():
                fail("Hessian mixes claimed invariant subspaces")
    signs = [sign_at_isolated_root(quadratic(hess_log, v), left, right) for v in vectors]
    if signs != [-1, -1, -1, 1]:
        fail("tangent Hessian signature check failed")

    output = {
        "status": "ACCEPT",
        "claim": "exact non-diagonal full-support critical point is a saddle",
        "active_sign_vectors": active_count,
        "tangent_signs": signs,
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
