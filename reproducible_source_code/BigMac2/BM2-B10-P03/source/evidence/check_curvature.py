#!/usr/bin/env python3
"""Dependency-free exact sanity checks for curvature_fixed_points.md.

The Markdown proof is decisive.  This script supplies reproducible finite
Fraction checks of every chamber formula, all sampled walls, and the stated
fixed-point classification on a bounded integer grid.
"""

from fractions import Fraction as Q
from itertools import product


def edge_kappa(e, yz, xz, D, Y, X):
    """Equation (2), with xz at x and yz at y."""
    p = Q(xz, e + xz)
    q = Q(yz, e + yz)
    A = q - p
    if A >= 0:
        return 1 + q - A * Q(Y, D)
    return 1 + p + A * Q(X, D)


def certified_vector(a, b, c):
    da, db, dc = min(a, b + c), min(b, a + c), min(c, a + b)
    return (
        edge_kappa(a, b, c, da, db, dc),
        edge_kappa(b, c, a, db, dc, da),
        edge_kappa(c, a, b, dc, da, db),
    )


def central(e, u, v):
    M, m = max(u, v), min(u, v)
    return Q(e * e + 2 * e * M + e * m + 3 * M * m - M * M,
             (e + M) * (e + m))


def long_vector(L, u, v):
    S = L + u + v
    return (
        Q(S * (L * (u + v) + 2 * u * v),
          (L + u) * (L + v) * (u + v)),
        Q(S, L + u),
        Q(S, L + v),
    )


checked = 0
fixed = 0
for a, b, c in product(range(1, 25), repeat=3):
    got = certified_vector(a, b, c)

    if a <= b + c and b <= a + c and c <= a + b:
        assert got == (central(a, b, c), central(b, a, c), central(c, a, b))

    if a >= b + c:
        assert got == long_vector(a, b, c)
    if b >= a + c:
        kb, ka, kc = long_vector(b, a, c)
        assert got == (ka, kb, kc)
    if c >= a + b:
        kc, ka, kb = long_vector(c, a, b)
        assert got == (ka, kb, kc)

    equal = got[0] == got[1] == got[2]
    L, M, m = sorted((a, b, c), reverse=True)
    classified = (L == M == m) or (M == m and L >= 2 * M)
    assert equal == classified
    fixed += int(equal)
    checked += 1

assert certified_vector(4, 1, 1) == (Q(6, 5),) * 3
print(f"exact checks passed: {checked} positive integer triples; {fixed} fixed triples")
