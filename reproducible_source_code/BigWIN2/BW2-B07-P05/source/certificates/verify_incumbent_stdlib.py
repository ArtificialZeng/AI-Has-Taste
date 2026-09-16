#!/usr/bin/env python3
"""Independent standard-library verifier for the algebraic incumbent.

The checker uses vector cross products, rational polynomial arithmetic modulo
the cubic, and exact rational interval refinement.  It does not import SymPy
or trust precomputed triangle areas.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path
import sys


def frac(value: str | int) -> Fraction:
    return Fraction(value)


def trim(poly: list[Fraction]) -> list[Fraction]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def add(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    n = max(len(a), len(b))
    out = [Fraction(0) for _ in range(n)]
    for i in range(n):
        out[i] = (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
    return trim(out)


def neg(a: list[Fraction]) -> list[Fraction]:
    return [-c for c in a]


def sub(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    return add(a, neg(b))


def scale(a: list[Fraction], c: Fraction) -> list[Fraction]:
    return trim([c * q for q in a])


def reduce_mod_cubic(a: list[Fraction]) -> list[Fraction]:
    # 12 z^3 - 27 z^2 + 20 z - 4 = 0.
    out = a[:]
    while len(out) > 3:
        degree = len(out) - 1
        lead = out.pop()
        if lead == 0:
            continue
        shift = degree - 3
        while len(out) < shift + 3:
            out.append(Fraction(0))
        out[shift] += lead * Fraction(1, 3)
        out[shift + 1] -= lead * Fraction(5, 3)
        out[shift + 2] += lead * Fraction(9, 4)
    return trim(out)


def mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(a) + len(b) - 1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return reduce_mod_cubic(out)


def eval_poly(poly: list[Fraction], x: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(poly):
        value = value * x + coefficient
    return value


def interval_poly(poly: list[Fraction], lo: Fraction, hi: Fraction) -> tuple[Fraction, Fraction]:
    # The isolating interval is positive, so powers are monotone.
    lower = Fraction(0)
    upper = Fraction(0)
    for degree, coefficient in enumerate(poly):
        a = lo**degree
        b = hi**degree
        if coefficient >= 0:
            lower += coefficient * a
            upper += coefficient * b
        else:
            lower += coefficient * b
            upper += coefficient * a
    return lower, upper


class RootOracle:
    def __init__(self, lo: Fraction, hi: Fraction) -> None:
        self.f = [Fraction(-4), Fraction(20), Fraction(-27), Fraction(12)]
        assert eval_poly(self.f, lo) < 0 < eval_poly(self.f, hi)
        derivative = [Fraction(20), Fraction(-54), Fraction(36)]
        dlo, _ = interval_poly(derivative, lo, hi)
        assert dlo > 0, "cubic must be strictly increasing on the isolating interval"
        self.initial = (lo, hi)

    def sign(self, poly: list[Fraction]) -> int:
        poly = trim(poly[:])
        if poly == [0]:
            return 0
        lo, hi = self.initial
        for _ in range(300):
            lower, upper = interval_poly(poly, lo, hi)
            if lower > 0:
                return 1
            if upper < 0:
                return -1
            mid = (lo + hi) / 2
            value = eval_poly(self.f, mid)
            if value < 0:
                lo = mid
            elif value > 0:
                hi = mid
            else:
                raise AssertionError("the cubic unexpectedly has a rational root")
        raise AssertionError(f"could not determine sign of {poly}")


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("incumbent.json")
    raw = path.read_bytes()
    data = json.loads(raw)
    assert data["schema"] == "heilbronn-square-ten-incumbent-v1"
    assert [frac(c) for c in data["minimal_polynomial_coefficients_ascending"]] == [
        Fraction(-4), Fraction(20), Fraction(-27), Fraction(12)
    ]
    lo, hi = map(frac, data["isolating_interval"])
    oracle = RootOracle(lo, hi)
    points = [
        ([frac(c) for c in px], [frac(c) for c in py])
        for px, py in data["coordinates_coefficients_ascending"]
    ]
    assert len(points) == 10
    one = [Fraction(1)]
    zero = [Fraction(0)]

    for px, py in points:
        assert oracle.sign(px) >= 0 and oracle.sign(sub(one, px)) >= 0
        assert oracle.sign(py) >= 0 and oracle.sign(sub(one, py)) >= 0
    for i, j in itertools.combinations(range(10), 2):
        dx = sub(points[i][0], points[j][0])
        dy = sub(points[i][1], points[j][1])
        assert oracle.sign(dx) != 0 or oracle.sign(dy) != 0

    target = [frac(c) for c in data["minimum_area_coefficients_ascending_reduced"]]
    equality = []
    area_forms = set()
    strict = 0
    for i, j, k in itertools.combinations(range(10), 3):
        # Vector-cross-product decomposition, independent of the SymPy checker.
        qx = sub(points[j][0], points[i][0])
        qy = sub(points[j][1], points[i][1])
        rx = sub(points[k][0], points[i][0])
        ry = sub(points[k][1], points[i][1])
        determinant = sub(mul(qx, ry), mul(qy, rx))
        determinant_sign = oracle.sign(determinant)
        assert determinant_sign != 0
        area = scale(determinant, Fraction(determinant_sign, 2))
        difference = sub(area, target)
        difference_sign = oracle.sign(difference)
        assert difference_sign >= 0
        canonical = tuple(area)
        area_forms.add(canonical)
        if difference_sign == 0:
            equality.append([i, j, k])
        else:
            strict += 1

    expected = data["expected"]
    assert len(equality) + strict == expected["triangle_count"] == 120
    assert equality == expected["equality_triples_zero_based"]
    assert len(equality) == expected["equality_triangle_count"] == 16
    assert strict == expected["strict_triangle_count"] == 104
    assert len(area_forms) == expected["distinct_area_form_count"] == 23
    # This exact separator is also needed by the full-family cover theorem.
    assert oracle.sign(sub(scale(target, Fraction(2)), [Fraction(9, 100)])) > 0

    code_digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_digest = hashlib.sha256(raw).hexdigest()
    print(json.dumps({
        "status": "PASS",
        "implementation": "stdlib-vector-cross-rational-root-interval",
        "triangle_count": 120,
        "equality_triangle_count": 16,
        "strict_triangle_count": 104,
        "distinct_area_form_count": 23,
        "input_sha256": input_digest,
        "code_sha256": code_digest
    }, sort_keys=True))


if __name__ == "__main__":
    main()
