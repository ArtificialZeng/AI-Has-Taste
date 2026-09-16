#!/usr/bin/env python3
"""Independent exact referee check of the four frozen witnesses.

This implementation does not import or call verify_small_primes.py.  It uses
multinomial coefficient extraction and square-fibre counts, rather than that
file's polynomial-convolution and pair-enumeration routines.
"""

from collections import Counter
from math import factorial


WITNESSES = (
    (5, 1, 1, 8, 2, 3),
    (7, 0, 1, 11, 3, 4),
    (11, 1, 3, 17, 5, 6),
    (13, 0, 4, 20, 6, 7),
)


def dotminus(u, v):
    return u - v if u >= v else 0


def printed_equation_4(p, a, b):
    """Evaluate equation (4) literally over nonnegative integers."""
    w = p * p
    radix = 1 << w
    numerator = (radix**3 + a * radix + b) ** ((p - 1) // 2)
    quotient = numerator // (radix ** (p - 1))
    digit = quotient % radix
    return digit, digit % p


def multinomial_coefficient(p, a, b):
    """Extract [x^(p-1)](x^3+a*x+b)^((p-1)/2) combinatorially."""
    e = (p - 1) // 2
    total = 0
    terms = []
    for i in range(e + 1):
        for j in range(e - i + 1):
            k = e - i - j
            if 3 * i + j != p - 1:
                continue
            value = (
                factorial(e)
                // (factorial(i) * factorial(j) * factorial(k))
                * a**j
                * b**k
            )
            total += value
            terms.append((i, j, k, value))
    return total, terms


def point_count_by_square_fibres(p, a, b):
    fibres = Counter((y * y) % p for y in range(p))
    values = [((x**3 + a * x + b) % p) for x in range(p)]
    return sum(fibres[t] for t in values), values


def equation_5(p, r):
    lift_indicator = dotminus(1, dotminus(4 * p + 1, r * r))
    return dotminus(p, r) + p * lift_indicator, lift_indicator


def main():
    print("Independent exact referee replay")
    print("p A B digit coefficient terms r N Nhat indicator discriminant")
    for p, a, b, expected_n, expected_r, expected_nhat in WITNESSES:
        digit, r = printed_equation_4(p, a, b)
        coefficient, terms = multinomial_coefficient(p, a, b)
        count, values = point_count_by_square_fibres(p, a, b)
        nhat, indicator = equation_5(p, r)
        discriminant = (4 * a**3 + 27 * b**2) % p
        assert digit == coefficient
        assert (count, r, nhat) == (expected_n, expected_r, expected_nhat)
        assert count != nhat and discriminant != 0
        print(
            p,
            a,
            b,
            digit,
            coefficient,
            terms,
            r,
            count,
            nhat,
            indicator,
            discriminant,
        )
        print("  f(x):", values)

    # Quantifier check: these are all primes strictly between 3 and 17.
    lower_primes = [n for n in range(4, 17) if n > 1 and all(n % d for d in range(2, int(n**0.5) + 1))]
    assert lower_primes == [row[0] for row in WITNESSES]
    print("lower_primes:", lower_primes)
    print("all_checks_passed=true")


if __name__ == "__main__":
    main()
