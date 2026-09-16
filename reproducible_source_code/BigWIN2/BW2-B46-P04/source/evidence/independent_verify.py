#!/usr/bin/env python3
"""Independent exact witness verification via Frobenius/Jacobi--Trudi.

This code does not enumerate rim hooks or use beta numbers.  It specializes
the Jacobi--Trudi determinant s_lambda=det(h_{lambda_i-i+j}) at
p_1=1, p_2=y, and p_k=0 for k>2.  Since

    sum h_k t^k = exp(t + y*t^2/2),

the coefficient of y^b in s_lambda, multiplied by
z_(2^b,1^a)=a! 2^b b!, is chi^lambda(2^b,1^a).
"""

from fractions import Fraction
from functools import lru_cache
from math import factorial


def poly_add(left, right):
    return tuple(x + y for x, y in zip(left, right))


def poly_scale(poly, scalar):
    return tuple(scalar * x for x in poly)


def poly_multiply(left, right, degree):
    out = [Fraction(0) for _ in range(degree + 1)]
    for i, x in enumerate(left):
        if not x:
            continue
        for j, y in enumerate(right[: degree - i + 1]):
            if y:
                out[i + j] += x * y
    return tuple(out)


@lru_cache(maxsize=None)
def complete_h(k, degree):
    if k < 0:
        return tuple(Fraction(0) for _ in range(degree + 1))
    out = []
    for b in range(degree + 1):
        if 2 * b <= k:
            out.append(Fraction(1, factorial(k - 2 * b) * (2 ** b) * factorial(b)))
        else:
            out.append(Fraction(0))
    return tuple(out)


def determinant_coefficient(partition, degree):
    """Coefficient of y^degree in the specialized JT determinant."""
    r = len(partition)
    zero = tuple(Fraction(0) for _ in range(degree + 1))
    one = (Fraction(1),) + zero[1:]
    dp = {0: one}
    for i in range(r):
        next_dp = {}
        for mask, accumulator in dp.items():
            for j in range(r):
                if mask & (1 << j):
                    continue
                # Previous chosen columns greater than j create inversions.
                inversions = (mask >> (j + 1)).bit_count()
                entry = complete_h(partition[i] - i + j, degree)
                term = poly_multiply(accumulator, entry, degree)
                if inversions % 2:
                    term = poly_scale(term, -1)
                new_mask = mask | (1 << j)
                next_dp[new_mask] = poly_add(next_dp.get(new_mask, zero), term)
        dp = next_dp
    return dp[(1 << r) - 1][degree]


def character(partition, transpositions):
    n = sum(partition)
    fixed_points = n - 2 * transpositions
    assert fixed_points >= 0
    coefficient = determinant_coefficient(partition, transpositions)
    value = coefficient * factorial(fixed_points) * (2 ** transpositions) * factorial(transpositions)
    assert value.denominator == 1
    return value.numerator, coefficient


def self_test():
    columns = {
        3: {(3,): 1, (2, 1): 0, (1, 1, 1): -1},
        4: {(4,): 1, (3, 1): -1, (2, 2): 2,
            (2, 1, 1): -1, (1, 1, 1, 1): 1},
    }
    for n, rows in columns.items():
        b = 1 if n == 3 else 2
        for partition, expected in rows.items():
            assert character(partition, b)[0] == expected


def main():
    self_test()
    print("self_test=independent S3/S4 Jacobi-Trudi columns passed")
    witnesses = [
        ((14, 7, 6, 5, 3, 3, 2, 2, 2), 2),
        ((14, 11, 4, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1), 4),
    ]
    for partition, b in witnesses:
        value, coefficient = character(partition, b)
        print(f"lambda={partition}")
        print(f"mu=(2^{b},1^{44-2*b})")
        print(f"jacobi_trudi_coefficient={coefficient}")
        print(f"character={value}")
        assert value == 0


if __name__ == "__main__":
    main()
