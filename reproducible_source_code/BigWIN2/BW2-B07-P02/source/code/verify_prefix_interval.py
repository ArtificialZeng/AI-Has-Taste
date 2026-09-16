#!/usr/bin/env python3
"""Independent fixed-point interval checker for the finite prefix.

All interval endpoints are integers representing multiples of 1/SCALE.
Every division is rounded outwards.  Thus this checker does not use the
5000! denominator or any intermediate divisibility assumption made by
``exact_prefix_factorial.py``.
"""

from argparse import ArgumentParser
from time import perf_counter


def ceil_div(nonnegative: int, divisor: int) -> int:
    return (nonnegative + divisor - 1) // divisor


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--limit", type=int, default=5000)
    parser.add_argument("--decimal-digits", type=int, default=30)
    args = parser.parse_args()
    limit = args.limit
    digits = args.decimal_digits
    if limit < 31:
        raise SystemExit("limit must be at least 31")
    if digits < 10:
        raise SystemExit("decimal-digits must be at least 10")

    started = perf_counter()
    scale = 10**digits
    lower = [0] * (limit + 1)
    upper = [0] * (limit + 1)
    lower[0] = upper[0] = scale

    for cycle_length in range(1, limit + 1):
        for degree in range(limit, cycle_length - 1, -1):
            lower[degree] += lower[degree - cycle_length] // cycle_length
            upper[degree] += ceil_div(
                upper[degree - cycle_length], cycle_length
            )

    if not lower[30] > upper[29]:
        raise AssertionError("q_30 > q_29 was not certified")
    for degree in range(31, limit + 1):
        if not upper[degree] < lower[degree - 1]:
            raise AssertionError(
                ("comparison not separated", degree,
                 upper[degree], lower[degree - 1])
            )

    minimum_gap, minimum_gap_degree = min(
        (lower[degree - 1] - upper[degree], degree)
        for degree in range(31, limit + 1)
    )
    maximum_width = max(
        upper[degree] - lower[degree]
        for degree in range(limit + 1)
    )
    elapsed = perf_counter() - started
    print("method=outward_rounded_fixed_point_intervals")
    print(f"scale=10^{digits}")
    print(f"exact_checked_through={limit}")
    print("last_nondecrease_n=30")
    print(f"minimum_separating_gap_units={minimum_gap}")
    print(f"minimum_gap_degree={minimum_gap_degree}")
    print(f"maximum_interval_width_units={maximum_width}")
    print(f"elapsed_seconds={elapsed:.6f}")


if __name__ == "__main__":
    main()
