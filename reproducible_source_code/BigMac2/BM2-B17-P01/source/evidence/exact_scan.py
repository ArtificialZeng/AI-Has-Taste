#!/usr/bin/env python3
"""Exact scan of row maxima for 2001 <= n <= 100000.

No floating-point quantity is used.  The adjacent-ratio threshold localizes a
row maximum, and consecutive row maxima are propagated as ``Fraction`` values.
Every decision R_n(a) < 1 is the integer comparison numerator < denominator.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
import sys


START = 2001
END = 100000
DIRECT_CHECKS = {2001, 2002, 4096, 10000, 50000, 100000}


def threshold(n: int, t: int) -> int:
    """Sign-equivalent numerator of R_n(a-1)/R_n(a) - 1.

    Here t = n - 2*a + 1.  Direct expansion gives

      sign(q_n(a)-1) = sign(n^2 - n(2t^2+3t) - t - 1).
    """

    return n * n - n * (2 * t * t + 3 * t) - t - 1


def transition_and_peak(n: int) -> tuple[int, int, bool]:
    """Return (first nonincreasing step, a peak, whether the step is a tie)."""

    lo, hi = 2, (n - 1) // 2
    # For n >= START the threshold is negative at a=2 and positive at hi.
    assert threshold(n, n - 2 * lo + 1) < 0
    assert threshold(n, n - 2 * hi + 1) > 0
    while lo < hi:
        mid = (lo + hi) // 2
        if threshold(n, n - 2 * mid + 1) >= 0:
            hi = mid
        else:
            lo = mid + 1
    first_down = lo
    value = threshold(n, n - 2 * first_down + 1)
    assert value >= 0
    assert threshold(n, n - 2 * (first_down - 1) + 1) < 0
    # If value is zero then first_down-1 and first_down are tied maxima.
    return first_down, first_down - 1, value == 0


def direct_r(n: int, a: int) -> Fraction:
    """The defining binomial expression, evaluated exactly."""

    numerator = (
        n
        * (n - 2 * a + 1)
        * math.comb(n, a)
        * math.comb(n - 2, a - 1)
    )
    denominator = (n - a) * math.comb(2 * n - 2, n - 1)
    return Fraction(numerator, denominator)


def advance(r: Fraction, n: int, a: int, next_a: int) -> Fraction:
    """Advance R_n(a) to R_{n+1}(next_a), exactly."""

    if next_a == a:
        factor = Fraction(
            (n + 1) ** 2 * (n - 1) * (n - 2 * a + 2),
            2 * (2 * n - 1) * (n - a + 1) ** 2 * (n - 2 * a + 1),
        )
    elif next_a == a + 1:
        factor = Fraction(
            (n + 1) ** 2 * (n - 1) * (n - 2 * a),
            2 * (2 * n - 1) * a * (a + 1) * (n - 2 * a + 1),
        )
    else:
        raise AssertionError(f"unexpected maximizing-index jump at n={n}: {a}->{next_a}")
    return r * factor


def main() -> None:
    # Python 3.11 guards decimal conversion of large integers by default.
    sys.set_int_max_str_digits(0)

    _, a, tie = transition_and_peak(START)
    r = direct_r(START, a)
    global_max = (r, START, a)
    violations: list[dict[str, str | int]] = []
    direct_checks: list[dict[str, int | bool]] = []
    transition_counts = {0: 0, 1: 0}
    tie_rows = int(tie)
    row_signature = hashlib.sha256()

    for n in range(START, END + 1):
        if n > START:
            _, next_a, tie = transition_and_peak(n)
            jump = next_a - a
            if jump not in transition_counts:
                raise AssertionError(f"unexpected jump {jump} at n={n}")
            transition_counts[jump] += 1
            r = advance(r, n - 1, a, next_a)
            a = next_a
            tie_rows += int(tie)

        if n in DIRECT_CHECKS:
            direct_checks.append(
                {"n": n, "a": a, "recurrence_equals_direct_formula": r == direct_r(n, a)}
            )
            assert direct_checks[-1]["recurrence_equals_direct_formula"]

        # This is the decisive exact comparison for the row maximum.
        is_strictly_below_one = r.numerator < r.denominator
        row_signature.update(f"{n},{a},{is_strictly_below_one}\n".encode("ascii"))
        if not is_strictly_below_one:
            violations.append(
                {
                    "n": n,
                    "a": a,
                    "numerator": str(r.numerator),
                    "denominator": str(r.denominator),
                }
            )
        if r > global_max[0]:
            global_max = (r, n, a)

    max_r, max_n, max_a = global_max
    result = {
        "arithmetic": "exact Python integers and fractions; no floating point",
        "direct_formula_cross_checks": direct_checks,
        "global_maximum_in_scanned_range": {
            "a": max_a,
            "denominator": str(max_r.denominator),
            "denominator_minus_numerator": str(max_r.denominator - max_r.numerator),
            "n": max_n,
            "numerator": str(max_r.numerator),
            "strictly_below_one": max_r.numerator < max_r.denominator,
            "t": max_n - 2 * max_a + 1,
        },
        "maximizer_tie_rows": tie_rows,
        "range": {"first_n": START, "last_n": END, "row_count": END - START + 1},
        "row_signature_sha256": row_signature.hexdigest(),
        "transition_counts": {str(k): v for k, v in transition_counts.items()},
        "violation_count": len(violations),
        "violations": violations,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
