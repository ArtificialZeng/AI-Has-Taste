#!/usr/bin/env python3
"""Exact sampled-subgraph bounds for the (r,n)=(25,48) frontier.

This is discovery/accounting code, not a certificate for Albertson's conjecture.
It compares both the unrounded Cranston bound and the stronger bound obtained
by applying integrality before summing over induced k-vertex subgraphs.
"""
from fractions import Fraction
from math import comb, ceil
import platform

N = 48
TARGET = 4356


def unrounded(m: int, k: int) -> Fraction:
    return (Fraction(5 * m * (N - 2) * (N - 3), (k - 2) * (k - 3))
            - Fraction(203 * N * (N - 1) * (N - 2) * (N - 3),
                       9 * k * (k - 1) * (k - 3)))


def locally_rounded(m: int, k: int) -> Fraction:
    # For every induced k-vertex H, Theorem A(i) and integrality give
    # cr(H) >= 5e(H) - floor(203(k-2)/9).
    penalty = (203 * (k - 2)) // 9
    num = 5 * m * comb(N - 2, k - 2) - penalty * comb(N, k)
    den = comb(N - 4, k - 4)
    return Fraction(num, den)


print(f"python={platform.python_version()} implementation={platform.python_implementation()}")
print(f"n={N} target={TARGET} k_range=4..{N}")
for m in (598, 599, 600):
    for label, fn in (("unrounded", unrounded), ("locally_rounded", locally_rounded)):
        vals = [(fn(m, k), k) for k in range(4, N + 1)]
        best, k = max(vals)
        print(f"m={m} method={label} best_k={k} bound={best.numerator}/{best.denominator} "
              f"ceil={ceil(best)} resolves={ceil(best) >= TARGET}")
