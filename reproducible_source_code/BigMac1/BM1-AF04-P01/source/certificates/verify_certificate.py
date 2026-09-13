#!/usr/bin/env python3
"""Independent exact verifier for the A278992 EGF-to-recurrence certificate.

This file imports no discovery module and uses only Python's standard library.
All polynomial and rational-function operations are rebuilt with Fraction.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path


ZERO = (Fraction(0),)
ONE = (Fraction(1),)


def fail(message: str) -> "NoReturn":
    raise ValueError(message)


def strict_keys(obj: object, keys: set[str], where: str) -> dict:
    if not isinstance(obj, dict):
        fail(f"{where}: expected object")
    actual = set(obj)
    if actual != keys:
        fail(f"{where}: keys {sorted(actual)} != {sorted(keys)}")
    return obj


def trim(poly: tuple[Fraction, ...]) -> tuple[Fraction, ...]:
    values = list(poly)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values)


def parse_poly(value: object, where: str) -> tuple[Fraction, ...]:
    if not isinstance(value, list) or not value:
        fail(f"{where}: expected nonempty coefficient list")
    out: list[Fraction] = []
    for item in value:
        if isinstance(item, bool) or not isinstance(item, int):
            fail(f"{where}: coefficients must be JSON integers")
        out.append(Fraction(item))
    return trim(tuple(out))


def padd(a, b):
    size = max(len(a), len(b))
    return trim(tuple((a[i] if i < len(a) else 0) +
                      (b[i] if i < len(b) else 0) for i in range(size)))


def pneg(a):
    return trim(tuple(-x for x in a))


def psub(a, b):
    return padd(a, pneg(b))


def pscale(a, scalar):
    return trim(tuple(Fraction(scalar) * x for x in a))


def pmul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return trim(tuple(out))


def pder(a):
    if len(a) == 1:
        return ZERO
    return trim(tuple(Fraction(i) * a[i] for i in range(1, len(a))))


def ppow(a, power: int):
    result = ONE
    for _ in range(power):
        result = pmul(result, a)
    return result


def ptranslate(a, shift):
    """Return a(x+shift), with coefficients in ascending powers of x."""
    result = ZERO
    linear = (Fraction(shift), Fraction(1))
    for degree, coefficient in enumerate(a):
        result = padd(result, pscale(ppow(linear, degree), coefficient))
    return result


class Rat:
    __slots__ = ("num", "den")

    def __init__(self, num=ZERO, den=ONE):
        self.num = trim(tuple(Fraction(x) for x in num))
        self.den = trim(tuple(Fraction(x) for x in den))
        if self.den == ZERO:
            fail("zero rational-function denominator")

    @classmethod
    def poly(cls, poly):
        return cls(poly, ONE)

    def __add__(self, other):
        other = as_rat(other)
        return Rat(padd(pmul(self.num, other.den), pmul(other.num, self.den)),
                   pmul(self.den, other.den))

    def __neg__(self):
        return Rat(pneg(self.num), self.den)

    def __sub__(self, other):
        return self + (-as_rat(other))

    def __mul__(self, other):
        other = as_rat(other)
        return Rat(pmul(self.num, other.num), pmul(self.den, other.den))

    def derivative(self):
        return Rat(psub(pmul(pder(self.num), self.den),
                        pmul(self.num, pder(self.den))),
                   pmul(self.den, self.den))

    def is_zero(self):
        return self.num == ZERO

    def equals(self, other):
        other = as_rat(other)
        return psub(pmul(self.num, other.den),
                    pmul(other.num, self.den)) == ZERO


def as_rat(value):
    return value if isinstance(value, Rat) else Rat.poly(value)


def parse_rat(value: object, where: str) -> Rat:
    obj = strict_keys(value, {"num", "den"}, where)
    return Rat(parse_poly(obj["num"], where + ".num"),
               parse_poly(obj["den"], where + ".den"))


def row_derivative(row):
    return [entry.derivative() for entry in row]


def row_times_matrix(row, matrix):
    return [sum((row[i] * matrix[i][j] for i in range(len(row))), Rat())
            for j in range(len(matrix[0]))]


def row_add(left, right):
    return [left[i] + right[i] for i in range(len(left))]


def row_scale(poly, row):
    factor = Rat.poly(poly)
    return [factor * entry for entry in row]


def derivative_n(value: Rat, count: int) -> Rat:
    for _ in range(count):
        value = value.derivative()
    return value


def compose_operators(left: dict[int, Rat], right: dict[int, Rat]):
    """Return left o right in right-normal form sum c_k(t) D^k."""
    out: dict[int, Rat] = {}
    for i, ai in left.items():
        for j, bj in right.items():
            for r in range(i + 1):
                order = i - r + j
                term = ai * Rat.poly((Fraction(math.comb(i, r)),)) * derivative_n(bj, r)
                out[order] = out.get(order, Rat()) + term
    return out


def parse_operator(obj: object, orders: range, where: str, rational=False):
    expected = {str(i) for i in orders}
    data = strict_keys(obj, expected, where)
    if rational:
        return {i: parse_rat(data[str(i)], f"{where}.{i}") for i in orders}
    return {i: Rat.poly(parse_poly(data[str(i)], f"{where}.{i}")) for i in orders}


def falling_poly(power: int):
    result = ONE
    for h in range(power):
        result = pmul(result, (Fraction(-h), Fraction(1)))
    return result


def derive_recurrence(l5: dict[int, Rat]):
    by_lag = {lag: ZERO for lag in range(5)}
    for derivative_order, rational in l5.items():
        if rational.den != ONE:
            fail("L5 must have polynomial coefficients")
        for t_power, coefficient in enumerate(rational.num):
            if coefficient == 0:
                continue
            lag = 4 + t_power - derivative_order
            if lag not in by_lag:
                fail(f"coefficient extraction produced unexpected lag {lag}")
            contribution_m = pscale(falling_poly(t_power), coefficient)
            contribution_n = ptranslate(contribution_m, -4)
            by_lag[lag] = padd(by_lag[lag], contribution_n)
    return by_lag


def series_mul(a, b, size):
    out = [Fraction(0)] * size
    for i, x in enumerate(a[:size]):
        for j, y in enumerate(b[:size - i]):
            out[i + j] += x * y
    return out


def series_inv(a, size):
    if not a or a[0] == 0:
        fail("series inverse with zero constant term")
    out = [Fraction(0)] * size
    out[0] = 1 / a[0]
    for n in range(1, size):
        out[n] = -sum(a[k] * out[n - k] for k in range(1, n + 1)) / a[0]
    return out


def series_exp(h, size):
    if h[0] != 0:
        fail("verifier only supports exponential series with constant zero")
    out = [Fraction(0)] * size
    out[0] = Fraction(1)
    for n in range(1, size):
        out[n] = sum(Fraction(k) * h[k] * out[n - k]
                     for k in range(1, n + 1)) / n
    return out


def reconstruct_initials(q, exponent_constant, g_prefactor, count):
    # Unique s with s(0)=1 and s^2=q.
    s = [Fraction(0)] * count
    s[0] = Fraction(1)
    for n in range(1, count):
        qn = q[n] if n < len(q) else Fraction(0)
        s[n] = (qn - sum(s[k] * s[n - k] for k in range(1, n))) / 2

    # E=exp(-1-t+s); the constant cancels because s(0)=1.
    h = s[:]
    h[0] += Fraction(-1)
    if count > 1:
        h[1] += Fraction(exponent_constant)
    e = series_exp(h, count)
    inv_s = series_inv(s, count)
    one_plus_inv_s = inv_s[:]
    one_plus_inv_s[0] += 1
    first = series_mul(one_plus_inv_s, e, count)

    minus_t = [Fraction(0)] * count
    if count > 1:
        minus_t[1] = Fraction(-1)
    exp_minus_t = series_exp(minus_t, count)
    g = series_mul(list(g_prefactor) + [Fraction(0)] * max(0, count-len(g_prefactor)),
                   exp_minus_t, count)
    f = [first[i] - g[i] for i in range(count)]
    return [int(f[i] * math.factorial(i)) for i in range(count)]


def eval_poly(poly, value: int):
    total = Fraction(0)
    for coefficient in reversed(poly):
        total = total * value + coefficient
    return total


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: verify_certificate.py CERTIFICATE.json", file=sys.stderr)
        return 2
    input_path = Path(sys.argv[1])
    raw = input_path.read_bytes()
    data = json.loads(raw)
    top = strict_keys(data, {
        "schema_version", "theorem_id", "definitions", "expected_l3",
        "multiplier", "expected_l5", "expected_recurrence",
        "initial_coefficients"
    }, "root")
    if top["schema_version"] != 1 or top["theorem_id"] != "A278992_EGF_TO_RECURRENCE":
        fail("unsupported schema or theorem id")

    defs = strict_keys(top["definitions"], {
        "q", "s_at_zero", "exponent_derivative_constant", "g_prefactor",
        "output_row"
    }, "definitions")
    q = parse_poly(defs["q"], "definitions.q")
    g_prefactor = parse_poly(defs["g_prefactor"], "definitions.g_prefactor")
    if defs["s_at_zero"] != 1 or defs["exponent_derivative_constant"] != -1:
        fail("unexpected branch or exponent derivative")
    output_raw = defs["output_row"]
    if not isinstance(output_raw, list) or len(output_raw) != 3 or any(
            isinstance(x, bool) or not isinstance(x, int) for x in output_raw):
        fail("definitions.output_row: expected three integers")

    # Rebuild X' = A X for X=(E,E/s,G) from q=s^2, E=exp(-1-t+s),
    # and G=P exp(-t).  This does not trust a serialized state matrix.
    q_rat = Rat.poly(q)
    qprime_half = Rat.poly(pscale(pder(q), Fraction(1, 2)))
    exponent_constant = Rat.poly((Fraction(defs["exponent_derivative_constant"]),))
    qprime_over_2q = Rat(qprime_half.num, pmul(qprime_half.den, q))
    p_rat = Rat.poly(g_prefactor)
    g_log_derivative = Rat(psub(pder(g_prefactor), g_prefactor), g_prefactor)
    z = Rat()
    matrix = [
        [exponent_constant, qprime_half, z],
        [qprime_over_2q, exponent_constant - qprime_over_2q, z],
        [z, z, g_log_derivative],
    ]
    rows = [[Rat.poly((Fraction(x),)) for x in output_raw]]
    for _ in range(3):
        rows.append(row_add(row_derivative(rows[-1]),
                            row_times_matrix(rows[-1], matrix)))

    l3 = parse_operator(top["expected_l3"], range(4), "expected_l3")
    relation = [Rat(), Rat(), Rat()]
    for order in range(4):
        relation = row_add(relation, row_scale(l3[order].num, rows[order]))
    if not all(entry.is_zero() for entry in relation):
        fail("expected_l3 does not annihilate the reconstructed state output")

    multiplier = parse_operator(top["multiplier"], range(3), "multiplier", rational=True)
    composed = compose_operators(multiplier, l3)
    l5 = parse_operator(top["expected_l5"], range(6), "expected_l5")
    if set(composed) != set(l5) or any(not composed[k].equals(l5[k]) for k in l5):
        fail("multiplier o L3 is not expected_l5")

    derived_recurrence = derive_recurrence(l5)
    recurrence_obj = strict_keys(top["expected_recurrence"],
                                 {str(i) for i in range(5)},
                                 "expected_recurrence")
    expected_recurrence = {
        i: parse_poly(recurrence_obj[str(i)], f"expected_recurrence.{i}")
        for i in range(5)
    }
    if derived_recurrence != expected_recurrence:
        fail("ODE coefficient extraction does not match expected recurrence")

    initials_raw = top["initial_coefficients"]
    if not isinstance(initials_raw, list) or not initials_raw or any(
            isinstance(x, bool) or not isinstance(x, int) for x in initials_raw):
        fail("initial_coefficients: expected nonempty integer list")
    rebuilt = reconstruct_initials(q, defs["exponent_derivative_constant"],
                                   g_prefactor, len(initials_raw))
    if rebuilt != initials_raw:
        fail(f"initial coefficients mismatch: rebuilt {rebuilt}")
    for n in range(4, len(rebuilt)):
        residual = sum(eval_poly(expected_recurrence[lag], n) * rebuilt[n-lag]
                       for lag in range(5))
        if residual != 0:
            fail(f"nonzero exact recurrence residual at n={n}: {residual}")

    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_hash = hashlib.sha256(raw).hexdigest()
    print(json.dumps({
        "status": "VERIFIED",
        "checks": [
            "state_system_to_L3",
            "ore_left_product_to_L5",
            "L5_to_recurrence",
            "formal_series_initials",
            "boundary_residuals_n4_to_n8"
        ],
        "input_sha256": input_hash,
        "verifier_sha256": code_hash
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"VERIFICATION_FAILED: {exc}", file=sys.stderr)
        raise SystemExit(1)
