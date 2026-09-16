#!/usr/bin/env python3
"""Exact triage check for J(4r+2,2r,r); standard-library only."""

from fractions import Fraction
from math import comb


def binom(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def eberlein(r: int, j: int) -> int:
    return sum(
        (-1) ** ell
        * binom(j, ell)
        * binom(2 * r - j, r - ell)
        * binom(2 * r + 2 - j, r - ell)
        for ell in range(r + 1)
    )


def trace_ratio(r: int) -> Fraction:
    """R/(m_4*|theta_2|^2); <1 makes the trace bound decisive."""
    n = 4 * r + 2
    degree = comb(2 * r, r) * comb(2 * r + 2, r)
    vertices = comb(n, 2 * r)
    m4 = comb(n, 4) - comb(n, 3)
    theta2_abs = Fraction(
        2 * r * r + 1, (2 * r - 1) * (2 * r + 2) * (2 * r + 1)
    )
    return Fraction(vertices, degree) / (m4 * theta2_abs**2)


if __name__ == "__main__":
    print("r minimizing_indices E_r(2) trace_ratio(<1 decisive)")
    for r in range(2, 61):
        values = [eberlein(r, j) for j in range(2 * r + 1)]
        minimum = min(values)
        minimizers = [j for j, value in enumerate(values) if value == minimum]
        q = trace_ratio(r)
        print(r, minimizers, values[2], f"{q.numerator}/{q.denominator}", q < 1)
