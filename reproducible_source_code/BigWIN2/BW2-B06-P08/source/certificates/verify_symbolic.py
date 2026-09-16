#!/usr/bin/env python3
"""Independent symbolic/Sturm verifier for nonparry_d4.json.

Trust path: SymPy polynomial remainders and exact Sturm root counts.  It does
not import the interval verifier, discovery code, or Breaker implementation.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import sympy as sp


def fail(message: str) -> None:
    raise AssertionError(message)


def rational(text: str) -> sp.Rational:
    return sp.Rational(text)


def sign_at_isolated_root(
    expression: sp.Expr,
    variable: sp.Symbol,
    interval_lo: sp.Rational,
    interval_hi: sp.Rational,
) -> int:
    polynomial = sp.Poly(expression, variable, domain=sp.QQ)
    if polynomial.is_zero:
        return 0
    if polynomial.count_roots(interval_lo, interval_hi) != 0:
        fail(f"sign polynomial has a root in the isolating interval: {polynomial.as_expr()}")
    value = polynomial.eval((interval_lo + interval_hi) / 2)
    return 1 if value > 0 else -1


def verify(certificate_path: Path) -> None:
    raw = certificate_path.read_bytes()
    data = json.loads(raw)
    x, s = sp.symbols("x s")
    f = x**4 - x - 1
    h = s**6 + s**4 - s**3 - s**2 - 1
    beta_lo, beta_hi = map(rational, data["beta_interval"])
    s_lo, s_hi = map(rational, data["s_interval"])

    f_poly = sp.Poly(f, x, domain=sp.QQ)
    h_poly = sp.Poly(h, s, domain=sp.QQ)
    if f_poly.count_roots(beta_lo, beta_hi) != 1 or f_poly.count_roots(0, sp.oo) != 1:
        fail("Sturm isolation/uniqueness failed for beta")
    if h_poly.count_roots(s_lo, s_hi) != 1 or h_poly.count_roots(0, sp.oo) != 1:
        fail("Sturm isolation/uniqueness failed for s")
    if not sp.Poly(f, x, modulus=2).is_irreducible:
        fail("defining polynomial is not irreducible modulo 2")

    # Clean-room check of the quadratic factorization over Q(s)/(h).
    u = -s / (s**2 + 1)
    p = -1 / s
    factor_difference = sp.Poly(
        sp.together((x**2 - u * x + s) * (x**2 + u * x + p) - f),
        x,
    )
    for coefficient in factor_difference.all_coeffs():
        numerator, _ = sp.fraction(sp.cancel(coefficient))
        if sp.rem(numerator, h, s) != 0:
            fail("quadratic factorization does not follow from h(s)=0")

    discriminant_numerator, discriminant_denominator = sp.fraction(
        sp.factor(u**2 - 4 * s)
    )
    if sign_at_isolated_root(discriminant_numerator, s, s_lo, s_hi) >= 0:
        fail("complex-pair discriminant is not negative")
    if sign_at_isolated_root(discriminant_denominator, s, s_lo, s_hi) <= 0:
        fail("complex-pair discriminant denominator is not positive")
    if not (s_hi < beta_lo**2 and s_lo * beta_lo > 1):
        fail("Perron separation failed")

    rho = rational(data["rho_lower"])
    if not rho**2 < s_lo:
        fail("rho lower bound failed")

    seen_exponents = []
    for row in data["witnesses"]:
        k = int(row["k"])
        seen_exponents.append(k)
        floor_q = int(row["floor_q"])
        q_expression = sp.rem(x**k, f, x)
        if sign_at_isolated_root(q_expression - floor_q, x, beta_lo, beta_hi) <= 0:
            fail(f"lower floor sign failed for k={k}")
        if sign_at_isolated_root(floor_q + 1 - q_expression, x, beta_lo, beta_hi) <= 0:
            fail(f"upper floor sign failed for k={k}")

        state = sp.Integer(1)
        state_vectors = set()
        for character in row["digits"]:
            digit = int(character)
            state = sp.rem(sp.expand(q_expression * state - digit), f, x)
            if sign_at_isolated_root(state, x, beta_lo, beta_hi) <= 0:
                fail(f"state is not positive for k={k}")
            if sign_at_isolated_root(1 - state, x, beta_lo, beta_hi) <= 0:
                fail(f"state is not below one for k={k}")
            vector = tuple(int(sp.Poly(state, x).nth(i)) for i in range(4))
            if vector in state_vectors:
                fail(f"unexpected repeated state inside witness for k={k}")
            state_vectors.add(vector)

        final_vector = [int(sp.Poly(state, x).nth(i)) for i in range(4)]
        if final_vector != row["final_state_low_to_high"]:
            fail(f"final state mismatch for k={k}")

        a0, a1, a2, a3 = final_vector
        A = a0 - a2 * s - a3 * u * s
        B = a1 + a2 * u + a3 * (u**2 - s)
        norm_squared = sp.factor(A**2 + A * B * u + B**2 * s)
        lower = rational(row["norm_lower"])
        gap_numerator, gap_denominator = sp.fraction(
            sp.factor(norm_squared - lower**2)
        )
        gap_remainder = sp.rem(gap_numerator, h, s)
        serialized_remainder = sum(
            coefficient * s**degree
            for degree, coefficient in enumerate(row["norm_gap_remainder_low_to_high"])
        )
        if sp.expand(gap_remainder - serialized_remainder) != 0:
            fail(f"serialized norm identity mismatch for k={k}")
        if sign_at_isolated_root(gap_remainder, s, s_lo, s_hi) <= 0:
            fail(f"Sturm norm gap failed for k={k}")
        if sign_at_isolated_root(gap_denominator, s, s_lo, s_hi) <= 0:
            fail(f"norm denominator sign failed for k={k}")
        if not lower * (rho**k - 1) > floor_q:
            fail(f"escape product failed for k={k}")

    if seen_exponents != list(range(1, 8)):
        fail("wrong exponent coverage")

    separator = rational(data["golden_ratio_separator"])
    if not s_lo**4 > separator:
        fail("eighth-power cutoff failed")
    if not (separator > sp.Rational(1, 2) and (2 * separator - 1) ** 2 > 5):
        fail("golden-ratio strictness failed")

    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_hash = hashlib.sha256(raw).hexdigest()
    print(
        "SYMBOLIC_STURM_CERTIFICATE_OK",
        "witnesses=7",
        "cutoff=8",
        f"sympy={sp.__version__}",
        f"input_sha256={input_hash}",
        f"code_sha256={code_hash}",
    )


if __name__ == "__main__":
    default = Path(__file__).with_name("nonparry_d4.json")
    verify(Path(sys.argv[1]) if len(sys.argv) == 2 else default)
