#!/usr/bin/env python3
"""Exact finite search for a restricted nine-pair construction.

Enumerate normalized primitive Pythagorean pairs with hypotenuse at most 2000
and test whether nine squared products, using at most three distinct pair types,
can sum to 9/8. This restriction is not the original problem.
"""

from fractions import Fraction
from math import gcd


MAX_HYPOTENUSE = 2000
MAX_M = 100  # safely exceeds sqrt(MAX_HYPOTENUSE)

products = {Fraction(0): (0, 1, 1)}
for m in range(2, MAX_M):
    for n in range(1, m):
        if gcd(m, n) != 1 or (m - n) % 2 == 0:
            continue
        a, b, c = m * m - n * n, 2 * m * n, m * m + n * n
        if c > MAX_HYPOTENUSE:
            continue
        q = Fraction(a * a * b * b, c**4)
        products.setdefault(q, (a, b, c))

values = tuple(products)
target = Fraction(9, 8)
for count_1 in range(10):
    for count_2 in range(10 - count_1):
        count_3 = 9 - count_1 - count_2
        if count_3 == 0:
            continue
        for q_1 in values:
            remainder = target - count_1 * q_1
            for q_2 in values:
                q_3 = (remainder - count_2 * q_2) / count_3
                if q_3 in products:
                    print("solution", count_1, q_1, products[q_1])
                    print("solution", count_2, q_2, products[q_2])
                    print("solution", count_3, q_3, products[q_3])
                    raise SystemExit(0)

print(f"pair-product values: {len(values)}")
print("no representation with at most three types in the stated finite search")
