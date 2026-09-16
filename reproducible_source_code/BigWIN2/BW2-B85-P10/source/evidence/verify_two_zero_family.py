#!/usr/bin/env python3
"""Exact audit for the length-two zero-run family T(p,0,0,q).

The symbolic part reconstructs every low-degree minor used in the proof from
the displayed polynomial decompositions.  The finite part checks the closed
form against the independently brute-force-validated tree DP, and searches a
large exact parameter rectangle.  No floating-point arithmetic is used.
"""

from __future__ import annotations

import json
from math import comb

import sympy as sp

from caterpillar_small_search import brute_polynomial, dp_polynomial


def choose_int(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def formula_polynomial(p: int, q: int) -> list[int]:
    """Coefficients of D_{T(p,0,0,q)} from the endpoint-state identity."""
    r = p + q
    h = []
    for t in range(r + 3):
        value = (
            choose_int(r + 2, t)
            + 2 * choose_int(q, t - p)
            + choose_int(q, t - p - 1)
            + 2 * choose_int(p, t - q)
            + choose_int(p, t - q - 1)
            + 2 * (t == r - 1)
            + (t == r)
        )
        h.append(value)
    return [0, 0] + h


def exact_identity_checks() -> dict[str, int]:
    dp_checks = 0
    brute_checks = 0
    for p in range(1, 21):
        for q in range(1, 21):
            expected = formula_polynomial(p, q)
            assert expected == dp_polynomial((p, 0, 0, q))
            dp_checks += 1
            if p + q + 4 <= 13:
                assert expected == brute_polynomial((p, 0, 0, q))
                brute_checks += 1
    return {
        "ordered_pairs_formula_vs_tree_dp_p_q_at_most_20": dp_checks,
        "ordered_pairs_formula_vs_direct_subsets_total_order_at_most_13": brute_checks,
    }


p, u, a = sp.symbols("p u a")


def choose_poly(z: sp.Expr, k: int) -> sp.Expr:
    """The falling-factorial polynomial binomial(z,k), for fixed k."""
    if k < 0:
        return sp.Integer(0)
    out = sp.Integer(1)
    for i in range(k):
        out *= z - i
    return sp.expand(out / sp.factorial(k))


def nonnegative_shifted_coefficients(expr: sp.Expr) -> int:
    """Certify coefficientwise nonnegativity after p=a+1, a,u>=0."""
    poly = sp.Poly(sp.expand(expr.subs(p, a + 1)), a, u)
    coefficients = poly.coeffs()
    assert coefficients
    assert all(coefficient >= 0 for coefficient in coefficients)
    assert any(coefficient > 0 for coefficient in coefficients)
    return len(coefficients)


def symbolic_certificate() -> dict[str, object]:
    # K_p=(1+x)^(p+2)+x+2x^2.  Only centers 1,2,3 differ
    # from the binomial row.
    def k_coefficient(h: int) -> sp.Expr:
        return sp.expand(
            choose_poly(p + 2, h)
            + (1 if h == 1 else 0)
            + (2 if h == 2 else 0)
        )

    k_minors = []
    for h in range(1, 4):
        delta = sp.expand(
            k_coefficient(h) ** 2
            - k_coefficient(h - 1) * k_coefficient(h + 1)
        )
        k_minors.append(nonnegative_shifted_coefficients(delta))

    # R=(1+x)^u K_p+x+2x^2.  Multiplication by (1+x)^u
    # preserves log-concavity, and only centers 1,2,3 are altered.
    def pk_coefficient(h: int) -> sp.Expr:
        return sp.expand(
            sum(choose_poly(u, j) * k_coefficient(h - j) for j in range(h + 1))
        )

    def r_coefficient(h: int) -> sp.Expr:
        return sp.expand(
            pk_coefficient(h)
            + (1 if h == 1 else 0)
            + (2 if h == 2 else 0)
        )

    r_minors = []
    for h in range(1, 4):
        delta = sp.expand(
            r_coefficient(h) ** 2
            - r_coefficient(h - 1) * r_coefficient(h + 1)
        )
        r_minors.append(nonnegative_shifted_coefficients(delta))

    # H*=(1+x)^p R+x^2+2x^3.  Again convolution preserves
    # log-concavity; the last summand alters exactly centers 1,...,4.
    def s_coefficient(h: int) -> sp.Expr:
        return sp.expand(
            sum(choose_poly(p, j) * r_coefficient(h - j) for j in range(h + 1))
        )

    def hstar_coefficient(h: int) -> sp.Expr:
        return sp.expand(
            s_coefficient(h)
            + (1 if h == 2 else 0)
            + (2 if h == 3 else 0)
        )

    hstar_minors = []
    hstar_deltas = []
    for h in range(1, 5):
        delta = sp.expand(
            hstar_coefficient(h) ** 2
            - hstar_coefficient(h - 1) * hstar_coefficient(h + 1)
        )
        hstar_deltas.append(delta)
        hstar_minors.append(nonnegative_shifted_coefficients(delta))

    # Bind the most complicated certificate to the compact nine-block
    # expansion displayed in the proof note.
    delta4_numerator = sp.expand(2880 * hstar_deltas[3]).subs(p, a + 1)
    delta4_blocks = sp.Poly(sp.expand(delta4_numerator), a)
    expected_blocks = {
        8: 256,
        7: 64 * (16 * u + 51),
        6: 16 * (112 * u**2 + 714 * u + 1179),
        5: 16 * (112 * u**3 + 1089 * u**2 + 3537 * u + 3825),
        4: 8 * (140 * u**4 + 1875 * u**3 + 9120 * u**2 + 19125 * u + 14988),
        3: 16 * (28 * u**5 + 490 * u**4 + 3225 * u**3 + 10025 * u**2 + 14988 * u + 8901),
        2: 8 * (14 * u**6 + 309 * u**5 + 2625 * u**4 + 10950 * u**3 + 23967 * u**2 + 26703 * u + 12682),
        1: 8 * (2 * u**7 + 54 * u**6 + 579 * u**5 + 3115 * u**4 + 8979 * u**3 + 14393 * u**2 + 12682 * u + 4560),
        0: (u + 1)
        * (
            u**7
            + 31 * u**6
            + 395 * u**5
            + 2565 * u**4
            + 8484 * u**3
            + 13484 * u**2
            + 15360 * u
            + 2880
        ),
    }
    # The expected blocks above are deliberately checked rather than trusted.
    # (They are scaled groupings of the coefficientwise-positive expansion.)
    actual = {degree[0]: sp.expand(coefficient) for degree, coefficient in delta4_blocks.terms()}
    assert actual == {degree: sp.expand(value) for degree, value in expected_blocks.items()}

    return {
        "arithmetic": "exact rational symbolic",
        "substitution_for_positive_orthant": "a=p-1, with a>=0 and u=q-p>=0",
        "K_changed_minor_centers": [1, 2, 3],
        "K_positive_monomial_counts": k_minors,
        "R_changed_minor_centers": [1, 2, 3],
        "R_positive_monomial_counts": r_minors,
        "H_reversal_changed_minor_centers": [1, 2, 3, 4],
        "H_reversal_positive_monomial_counts": hstar_minors,
        "status": "all reconstructed minor polynomials coefficientwise nonnegative and nonzero",
    }


def finite_search(limit: int = 150) -> dict[str, object]:
    pairs = 0
    minors = 0
    smallest = None
    for p_value in range(1, limit + 1):
        for q_value in range(p_value, limit + 1):
            coefficients = formula_polynomial(p_value, q_value)
            pairs += 1
            for j in range(1, len(coefficients) - 1):
                slack = (
                    coefficients[j] ** 2
                    - coefficients[j - 1] * coefficients[j + 1]
                )
                assert slack >= 0
                minors += 1
                if coefficients[j - 1] * coefficients[j + 1] > 0:
                    record = {
                        "slack": slack,
                        "p": p_value,
                        "q": q_value,
                        "index_in_D": j,
                        "coefficient_triple": coefficients[j - 1 : j + 2],
                    }
                    key = (slack, p_value + q_value, p_value, q_value, j)
                    if smallest is None or key < smallest[0]:
                        smallest = (key, record)
    assert smallest is not None
    return {
        "parameter_scope": f"1<=p<=q<={limit}",
        "parameter_pairs": pairs,
        "log_concavity_minors": minors,
        "smallest_positive_support_slack": smallest[1],
        "status": "no counterexample (supplementary finite check; theorem uses symbolic proof)",
    }


def main() -> None:
    result = {
        "identity_validation": exact_identity_checks(),
        "symbolic_certificate": symbolic_certificate(),
        "finite_search": finite_search(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
