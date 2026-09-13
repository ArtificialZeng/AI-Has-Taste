#!/usr/bin/env python3
"""Exact independent Burnside/Davis counts of unlabeled tournaments.

For a partition of n into odd cycle lengths with multiplicities j_k, Davis's
formula contributes

    2^t / product(k^j_k j_k!),

where 2t = sum_{r,s} j_r j_s gcd(r,s) - sum_r j_r.
All arithmetic is rational and the final denominator must be one.
"""

from fractions import Fraction
from math import factorial, gcd


def odd_partitions(n: int, largest: int | None = None):
    if n == 0:
        yield ()
        return
    if largest is None or largest > n:
        largest = n
    if largest % 2 == 0:
        largest -= 1
    for part in range(largest, 0, -2):
        for rest in odd_partitions(n - part, part):
            yield (part,) + rest


def tournament_count(n: int) -> int:
    total = Fraction(0)
    for partition in odd_partitions(n):
        multiplicity: dict[int, int] = {}
        for part in partition:
            multiplicity[part] = multiplicity.get(part, 0) + 1
        twice_exponent = sum(
            jr * js * gcd(r, s)
            for r, jr in multiplicity.items()
            for s, js in multiplicity.items()
        ) - sum(multiplicity.values())
        assert twice_exponent % 2 == 0
        denominator = 1
        for length, number in multiplicity.items():
            denominator *= length**number * factorial(number)
        total += Fraction(1 << (twice_exponent // 2), denominator)
    assert total.denominator == 1
    return total.numerator


def main() -> None:
    expected = [1, 1, 1, 2, 4, 12, 56, 456, 6880, 191536, 9733056, 903753248]
    actual = [tournament_count(n) for n in range(12)]
    assert actual == expected, (actual, expected)
    for n, value in enumerate(actual):
        print(f"n={n} unlabeled_tournaments={value}")
    print("BURNSIDE_OK n=11 count=903753248 arithmetic=fractions.Fraction")


if __name__ == "__main__":
    main()
