#!/usr/bin/env python3
"""Exact finite replay for the all-odd colored-cycle obstruction.

The general determinant and continuity arguments are proved in the companion
Markdown file.  This script checks their algebra in boundary, odd, and even
dimensions using exact integers and rationals only.
"""

from fractions import Fraction
from itertools import permutations

import sympy as sp


def supported_permutations(m):
    """Return determinant permutations supported by columns i-1 and i."""
    return [
        p
        for p in permutations(range(m))
        if all(p[i] in ((i - 1) % m, i) for i in range(m))
    ]


def coefficient_matrix(x):
    m = len(x)
    B = sp.zeros(m)
    for i in range(m):
        B[i, (i - 1) % m] = x[(i - 1) % m]
        B[i, i] = x[(i + 1) % m]
    return B


def concentration_matrix(b):
    m = len(b)
    K = 2 * sp.eye(m)
    for i in range(m):
        K[i, (i + 1) % m] = b[i]
        K[(i + 1) % m, i] = b[i]
    return K


def weighted_laplacian(w):
    m = len(w)
    L = sp.zeros(m)
    for i in range(m):
        j = (i + 1) % m
        L[i, i] += w[i]
        L[j, j] += w[i]
        L[i, j] -= w[i]
        L[j, i] -= w[i]
    return L


# The combinatorial determinant support has exactly the two terms used in the
# proof.  The smallest case m=3 and both parities are included.
for m in range(3, 9):
    supported = supported_permutations(m)
    identity = tuple(range(m))
    shift = tuple((i - 1) % m for i in range(m))
    assert set(supported) == {identity, shift}

# Symbolic determinant replay in several dimensions, including even dimensions
# where it vanishes identically.
for m in range(3, 9):
    x_symbols = sp.symbols(f"x0:{m}", nonzero=True)
    determinant = sp.factor(coefficient_matrix(x_symbols).det())
    expected = (1 + (-1) ** (m - 1)) * sp.prod(x_symbols)
    assert determinant == expected

# At the all-ones point, every odd system has the unique solution b=-1, and the
# resulting concentration matrix is the ordinary cycle Laplacian of rank m-1.
for m in (3, 5, 7, 9, 15):
    x = sp.ones(m, 1)
    B = coefficient_matrix(list(x))
    assert B.det() == 2
    b = B.inv() * (-2 * x)
    assert b == -sp.ones(m, 1)
    K = concentration_matrix(list(b))
    assert K * x == sp.zeros(m, 1)
    assert K.rank() == m - 1
    assert K == weighted_laplacian([sp.Integer(1)] * m)

# Held-out rational points close to one replay the open sign condition and the
# weighted-Laplacian congruence without floating point arithmetic.
for m in (3, 5, 7, 9, 11):
    x_values = [
        sp.Rational(Fraction(1, 1) + Fraction((i % 3) - 1, 100 * m))
        for i in range(m)
    ]
    x = sp.Matrix(x_values)
    B = coefficient_matrix(x_values)
    assert B.det() == 2 * sp.prod(x_values)
    b = B.inv() * (-2 * x)
    assert all(value < 0 for value in b)
    K = concentration_matrix(list(b))
    D = sp.diag(*x_values)
    w = [-b[i] * x_values[i] * x_values[(i + 1) % m] for i in range(m)]
    assert all(value > 0 for value in w)
    assert K * x == sp.zeros(m, 1)
    assert D * K * D == weighted_laplacian(w)
    assert K.rank() == m - 1

print("supported determinant permutations checked for m=3,...,8")
print("symbolic determinant and parity checked for m=3,...,8")
print("all-ones PSD/rank certificates checked through odd m=15")
print("held-out exact rational congruences checked for odd m=3,5,7,9,11")
