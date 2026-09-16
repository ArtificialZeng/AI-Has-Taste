#!/usr/bin/env python3
"""Pure-standard-library exact verifier for nonparry_d4.json.

Trust path: integer quotient-ring recurrences plus outward rational interval
arithmetic.  No floating point, numerical root finder, SymPy, or discovery
output is used.
"""

from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable


def fail(message: str) -> None:
    raise AssertionError(message)


def q(text: str) -> Fraction:
    return Fraction(text)


def polynomial_value(coefficients: Iterable[int], x: Fraction) -> Fraction:
    value = Fraction(0)
    for coefficient in reversed(tuple(coefficients)):
        value = value * x + coefficient
    return value


def sign_changes(coefficients_low_to_high: Iterable[int]) -> int:
    signs = [1 if c > 0 else -1 for c in reversed(tuple(coefficients_low_to_high)) if c]
    return sum(a != b for a, b in zip(signs, signs[1:]))


def polynomial_add(a: list[int], b: list[int]) -> list[int]:
    result = [0] * max(len(a), len(b))
    for i, coefficient in enumerate(a):
        result[i] += coefficient
    for i, coefficient in enumerate(b):
        result[i] += coefficient
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def polynomial_multiply(a: list[int], b: list[int]) -> list[int]:
    result = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            result[i + j] += ai * bj
    return result


@dataclass(frozen=True)
class Interval:
    lo: Fraction
    hi: Fraction

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            fail("reversed interval")

    @staticmethod
    def point(value: int | Fraction) -> "Interval":
        value = Fraction(value)
        return Interval(value, value)

    def __add__(self, other: "Interval") -> "Interval":
        return Interval(self.lo + other.lo, self.hi + other.hi)

    def __neg__(self) -> "Interval":
        return Interval(-self.hi, -self.lo)

    def __sub__(self, other: "Interval") -> "Interval":
        return self + (-other)

    def __mul__(self, other: "Interval") -> "Interval":
        products = (
            self.lo * other.lo,
            self.lo * other.hi,
            self.hi * other.lo,
            self.hi * other.hi,
        )
        return Interval(min(products), max(products))

    def reciprocal(self) -> "Interval":
        if self.lo <= 0 <= self.hi:
            fail("interval division by a possible zero")
        return Interval(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other: "Interval") -> "Interval":
        return self * other.reciprocal()

    def square(self) -> "Interval":
        if self.lo <= 0 <= self.hi:
            return Interval(Fraction(0), max(self.lo**2, self.hi**2))
        return Interval(min(self.lo**2, self.hi**2), max(self.lo**2, self.hi**2))

    def pow(self, exponent: int) -> "Interval":
        if exponent < 0:
            return self.pow(-exponent).reciprocal()
        result = Interval.point(1)
        base = self
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent //= 2
        return result


def interval_polynomial(coefficients: Iterable[int], x: Interval) -> Interval:
    result = Interval.point(0)
    power = Interval.point(1)
    for coefficient in coefficients:
        result = result + Interval.point(coefficient) * power
        power = power * x
    return result


Vector = tuple[int, int, int, int]


def multiply_by_x(vector: Vector) -> Vector:
    a, b, c, d = vector
    return d, a + d, b, c


def multiply_by_x_power(vector: Vector, exponent: int) -> Vector:
    for _ in range(exponent):
        vector = multiply_by_x(vector)
    return vector


def vector_interval(vector: Vector, beta: Interval) -> Interval:
    return interval_polynomial(vector, beta)


def gf2_remainder(dividend_bits: int, divisor_bits: int) -> int:
    while dividend_bits.bit_length() >= divisor_bits.bit_length():
        shift = dividend_bits.bit_length() - divisor_bits.bit_length()
        dividend_bits ^= divisor_bits << shift
    return dividend_bits


def verify(certificate_path: Path) -> None:
    raw = certificate_path.read_bytes()
    data = json.loads(raw)
    required_keys = {
        "schema_version",
        "task_id",
        "polynomial_coefficients_low_to_high",
        "modulus_polynomial_coefficients_low_to_high",
        "beta_interval",
        "s_interval",
        "rho_lower",
        "golden_ratio_separator",
        "witnesses",
    }
    if set(data) != required_keys:
        fail("unexpected or missing top-level certificate fields")
    if data["schema_version"] != 1 or data["task_id"] != "08_nonparry_d4":
        fail("wrong schema or task")

    f = data["polynomial_coefficients_low_to_high"]
    h = data["modulus_polynomial_coefficients_low_to_high"]
    if f != [-1, -1, 0, 0, 1]:
        fail("wrong defining polynomial")
    if h != [-1, 0, -1, -1, 1, 0, 1]:
        fail("wrong modulus polynomial")

    beta_lo, beta_hi = map(q, data["beta_interval"])
    s_lo, s_hi = map(q, data["s_interval"])
    if not (Fraction(1) < beta_lo < beta_hi and polynomial_value(f, beta_lo) < 0 < polynomial_value(f, beta_hi)):
        fail("beta interval does not isolate a positive root")
    if sign_changes(f) != 1:
        fail("Descartes uniqueness check failed for beta")
    if not (Fraction(1) < s_lo < s_hi and polynomial_value(h, s_lo) < 0 < polynomial_value(h, s_hi)):
        fail("s interval does not isolate a root above one")
    if sign_changes(h) != 1:
        fail("Descartes uniqueness check failed for s")

    # X^4+X+1 has neither an F_2 root nor the irreducible quadratic factor.
    f_mod2_bits = (1 << 4) | (1 << 1) | 1
    if gf2_remainder(f_mod2_bits, 0b10) == 0 or gf2_remainder(f_mod2_bits, 0b11) == 0:
        fail("unexpected linear factor modulo 2")
    if gf2_remainder(f_mod2_bits, 0b111) == 0:
        fail("unexpected quadratic factor modulo 2")

    # Verify the symbolic numerator of p+s-u^2 for
    # p=-1/s and u=-s/(s^2+1). It must be h(s).
    numerator = polynomial_add(
        polynomial_multiply([-1, 0, 1], [1, 0, 2, 0, 1]),
        [0, 0, 0, -1],
    )
    if numerator != h:
        fail("quadratic factorization identity failed")

    beta_interval = Interval(beta_lo, beta_hi)
    s_interval = Interval(s_lo, s_hi)
    one = Interval.point(1)
    u_interval = -(s_interval / (s_interval.square() + one))
    if not (u_interval.square() - Interval.point(4) * s_interval).hi < 0:
        fail("the selected quadratic is not certified nonreal")
    if not (s_hi < beta_lo**2 and s_lo * beta_lo > 1):
        fail("Perron modulus separation failed")

    rho = q(data["rho_lower"])
    if not (rho > 1 and rho**2 < s_lo):
        fail("rho is not a strict lower bound for |gamma|")

    witnesses = data["witnesses"]
    if [row.get("k") for row in witnesses] != list(range(1, 8)):
        fail("witness exponent list is not exactly 1,...,7")
    expected_row_keys = {
        "k",
        "floor_q",
        "digits",
        "final_state_low_to_high",
        "norm_lower",
        "norm_gap_remainder_low_to_high",
    }

    for row in witnesses:
        if set(row) != expected_row_keys:
            fail("malformed witness row")
        k = row["k"]
        floor_q = row["floor_q"]
        digits = row["digits"]
        if not digits or any(character not in "0123456789" for character in digits):
            fail("malformed digit word")

        q_vector = multiply_by_x_power((1, 0, 0, 0), k)
        q_interval = vector_interval(q_vector, beta_interval)
        if not (floor_q < q_interval.lo and q_interval.hi < floor_q + 1):
            fail(f"floor(beta^{k}) failed")

        state: Vector = (1, 0, 0, 0)
        for character in digits:
            digit = int(character)
            if digit > floor_q:
                fail(f"digit outside alphabet for k={k}")
            state = multiply_by_x_power(state, k)
            state = (state[0] - digit, state[1], state[2], state[3])
            state_value = vector_interval(state, beta_interval)
            if not (state_value.lo > 0 and state_value.hi < 1):
                fail(f"uncertified greedy state for k={k}")
        if list(state) != row["final_state_low_to_high"]:
            fail(f"wrong serialized final state for k={k}")

        a0, a1, a2, a3 = state
        A = (
            Interval.point(a0)
            - Interval.point(a2) * s_interval
            - Interval.point(a3) * u_interval * s_interval
        )
        B = (
            Interval.point(a1)
            + Interval.point(a2) * u_interval
            + Interval.point(a3) * (u_interval.square() - s_interval)
        )
        norm_squared = A.square() + A * B * u_interval + B.square() * s_interval
        lower = q(row["norm_lower"])
        if not norm_squared.lo > lower**2:
            fail(f"embedded norm lower bound failed for k={k}")

        gap_check = interval_polynomial(row["norm_gap_remainder_low_to_high"], s_interval)
        if not gap_check.lo > 0:
            fail(f"serialized symbolic norm gap is not positive for k={k}")
        if not lower * (rho**k - 1) > floor_q:
            fail(f"strict escape product failed for k={k}")

    separator = q(data["golden_ratio_separator"])
    if not (s_lo**4 > separator and separator > Fraction(1, 2)):
        fail("large-exponent rational separator failed")
    if not (2 * separator - 1) ** 2 > 5:
        fail("separator is not strictly above the golden ratio")

    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_hash = hashlib.sha256(raw).hexdigest()
    print(
        "EXACT_INTERVAL_CERTIFICATE_OK",
        "witnesses=7",
        "cutoff=8",
        f"input_sha256={input_hash}",
        f"code_sha256={code_hash}",
    )


if __name__ == "__main__":
    default = Path(__file__).with_name("nonparry_d4.json")
    verify(Path(sys.argv[1]) if len(sys.argv) == 2 else default)
