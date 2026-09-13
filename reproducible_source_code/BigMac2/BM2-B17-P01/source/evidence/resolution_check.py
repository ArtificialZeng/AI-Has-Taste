#!/usr/bin/env python3
"""Exact finite scan and rational checks for the uniform tail proof.

The finite part uses only Python integers/Fraction.  The tail section checks
the rational cross-products appearing in uniform_tail_proof.md; the analytic
Stirling and calculus inequalities themselves are documented there.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
import sys

from exact_scan import advance, direct_r, transition_and_peak


START = 496
END = 100000
N = 100001
SOURCE_SHA256 = "ce462b0aacd55a07bf7a64e52e96110e6e6f953d4bf779163753c7cb2ce876b9"
DIRECT_CHECKS = {496, 497, 2000, 2001, 4096, 10000, 50000, 100000}


def finite_scan() -> dict[str, object]:
    _, a, tie = transition_and_peak(START)
    value = direct_r(START, a)
    largest = (value, START, a)
    violations: list[dict[str, object]] = []
    checks: list[dict[str, object]] = []
    transition_counts: dict[int, int] = {0: 0, 1: 0}
    tie_rows = int(tie)
    signature = hashlib.sha256()

    for n in range(START, END + 1):
        if n > START:
            _, next_a, tie = transition_and_peak(n)
            jump = next_a - a
            assert jump in transition_counts
            transition_counts[jump] += 1
            value = advance(value, n - 1, a, next_a)
            a = next_a
            tie_rows += int(tie)

        if n in DIRECT_CHECKS:
            agrees = value == direct_r(n, a)
            assert agrees
            checks.append({"n": n, "a": a, "recurrence_equals_direct_formula": agrees})

        below = value.numerator < value.denominator
        signature.update(f"{n},{a},{below}\n".encode("ascii"))
        if not below:
            violations.append(
                {
                    "n": n,
                    "a": a,
                    "numerator": str(value.numerator),
                    "denominator": str(value.denominator),
                }
            )
        if value > largest[0]:
            largest = (value, n, a)

    maximum, max_n, max_a = largest
    assert not violations
    return {
        "arithmetic": "exact Python integers and fractions; no floating point",
        "range": {"first_n": START, "last_n": END, "row_count": END - START + 1},
        "violation_count": len(violations),
        "violations": violations,
        "maximizer_tie_rows": tie_rows,
        "transition_counts": {str(k): v for k, v in transition_counts.items()},
        "direct_formula_cross_checks": checks,
        "row_signature_sha256": signature.hexdigest(),
        "global_maximum_in_scanned_range": {
            "n": max_n,
            "a": max_a,
            "t": max_n - 2 * max_a + 1,
            "numerator": str(maximum.numerator),
            "denominator": str(maximum.denominator),
            "denominator_minus_numerator": str(maximum.denominator - maximum.numerator),
            "strictly_below_one": maximum < 1,
        },
    }


def tail_rational_checks() -> dict[str, object]:
    # e > sum_{j=0}^6 1/j! = 1957/720 > 2718/1000.
    e_partial = sum(Fraction(1, math.factorial(j)) for j in range(7))
    assert e_partial == Fraction(1957, 720)
    assert e_partial > Fraction(2718, 1000)

    # 4/sqrt(pi) < 231/100 follows from pi > 3 and this square comparison.
    pi_square_margin = Fraction(231, 100) ** 2 * 3 - 16
    assert pi_square_margin > 0

    # 1/sqrt(2e) < 429/1000, using e > 2718/1000.
    e_square_margin = 2 * Fraction(2718, 1000) * Fraction(429, 1000) ** 2 - 1
    assert e_square_margin > 0

    A = Fraction(N - 1, N * (N - 2))
    sqrt_A_margin = Fraction(3163, 10**6) ** 2 - A
    assert sqrt_A_margin > 0

    denominator_product = (1 - Fraction(1, N)) * (1 - Fraction(N, (N - 2) ** 2))
    C_margin = denominator_product - Fraction(10**6, 1000011) ** 2
    assert C_margin > 0

    E = Fraction(1, 12 * N) + Fraction(1, 12 * (N - 2)) + Fraction(1, 6 * (N - 1))
    exponential_input_margin = Fraction(4, 1000004) - E
    assert exponential_input_margin > 0
    # exp(E) <= 1/(1-E) < 1000004/1000000.
    assert Fraction(1, 1) / (1 - E) < Fraction(1000004, 10**6)

    uniform_bound = (
        Fraction(231, 100)
        * (Fraction(429, 1000) + Fraction(3163, 10**6))
        * Fraction(1000011, 10**6)
        * Fraction(1000004, 10**6)
    )
    assert uniform_bound == Fraction(24957787612296876183, 25000000000000000000)
    assert uniform_bound < 1

    def record(x: Fraction) -> dict[str, str]:
        return {"numerator": str(x.numerator), "denominator": str(x.denominator)}

    return {
        "endpoint_n": N,
        "all_checks_passed": True,
        "e_partial_sum": record(e_partial),
        "pi_square_margin": record(pi_square_margin),
        "e_square_margin": record(e_square_margin),
        "sqrt_A_square_margin": record(sqrt_A_margin),
        "C_inverse_square_margin": record(C_margin),
        "exponential_input_margin": record(exponential_input_margin),
        "uniform_upper_bound": record(uniform_bound),
        "strict_margin_below_one": record(1 - uniform_bound),
    }


def main() -> None:
    sys.set_int_max_str_digits(0)
    with open("source.md", "rb") as source_file:
        source_hash = hashlib.sha256(source_file.read()).hexdigest()
    assert source_hash == SOURCE_SHA256
    result = {
        "source_sha256": source_hash,
        "finite_scan": finite_scan(),
        "tail_rational_certificate": tail_rational_checks(),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
