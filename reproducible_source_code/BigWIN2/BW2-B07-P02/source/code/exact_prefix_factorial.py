#!/usr/bin/env python3
"""Exact coefficient scan using one global factorial denominator."""

from argparse import ArgumentParser
from math import factorial
from time import perf_counter


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--limit", type=int, default=5000)
    args = parser.parse_args()
    limit = args.limit
    if limit < 1:
        raise SystemExit("limit must be positive")

    started = perf_counter()
    denominator = factorial(limit)
    coeff = [0] * (limit + 1)
    coeff[0] = denominator
    for part in range(1, limit + 1):
        for degree in range(limit, part - 1, -1):
            quotient, remainder = divmod(coeff[degree - part], part)
            if remainder:
                raise AssertionError((part, degree, remainder))
            coeff[degree] += quotient

    nondecrease = [
        degree
        for degree in range(1, limit + 1)
        if coeff[degree] >= coeff[degree - 1]
    ]
    if limit >= 30 and nondecrease[-1] != 30:
        raise AssertionError(nondecrease[-10:])
    if limit >= 31 and not all(
        coeff[degree] < coeff[degree - 1]
        for degree in range(31, limit + 1)
    ):
        raise AssertionError("strict-decrease check failed")

    elapsed = perf_counter() - started
    print("method=factorial_common_denominator")
    print(f"exact_checked_through={limit}")
    print(f"last_nondecrease_n={nondecrease[-1]}")
    print(f"elapsed_seconds={elapsed:.6f}")


if __name__ == "__main__":
    main()
