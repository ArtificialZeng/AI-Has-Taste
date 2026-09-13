#!/usr/bin/env python3
"""Exact matrix-level cross-check of the n=3 equality classification.

The human iff proof is in audit/agents/builder.md.  This script verifies the
two GL2 translations, the equality polynomials in both homogeneous normal
forms, and the generic 2-by-2 zero-block family using permanent definitions.
"""

from itertools import permutations

import sympy as sp


def permanent(matrix):
    n = len(matrix)
    return sp.expand(sum(
        sp.prod(matrix[i][sigma[i]] for i in range(n))
        for sigma in permutations(range(n))
    ))


def duplicate(matrix):
    n = len(matrix)
    return [[matrix[i % n][j % n] for j in range(2*n)]
            for i in range(2*n)]


def product_coefficients(first, second):
    result = [sp.Integer(1)]
    for a, b in zip(first, second):
        new = [sp.Integer(0)] * (len(result) + 1)
        for k, value in enumerate(result):
            new[k] += value * a
            new[k + 1] += value * b
        result = [sp.expand(value) for value in new]
    return result


def bracket(c, d, i, j):
    return d[i] * c[j] - c[i] * d[j]


def main():
    c = sp.symbols("c0:3", real=True)
    d = sp.symbols("d0:3", real=True)

    # Distinct-row normal form: f=X(X-Y)(X+Y).  The variable change
    # A=[[1,1],[-1,1]] sends it to 4*X*Y*(X+Y), while a column covector
    # (c,d) is sent to ((c-d)/2,(c+d)/2).
    cp = [(c[i] - d[i]) / 2 for i in range(3)]
    dp = [(c[i] + d[i]) / 2 for i in range(3)]
    g = product_coefficients(cp, dp)
    g0, g1, g2, g3 = g
    discriminant_numerator = sp.expand(
        2*g1**2 + g1*g2 + 2*g2**2
        - 6*g0*g2 - 9*g0*g3 - 6*g1*g3
    )
    distinct_sos = sp.expand(
        bracket(c, d, 1, 2)**2 * (d[0]**2 + 3*c[0]**2)
        + bracket(c, d, 0, 2)**2 * (d[1]**2 + 3*c[1]**2)
        + bracket(c, d, 0, 1)**2 * (d[2]**2 + 3*c[2]**2)
    )
    assert sp.Poly(distinct_sos - 16*discriminant_numerator,
                   *c, *d).is_zero

    # Repeated-row normal form: f=X^2(X+Y).  The variable change
    # A=[[1,0],[-1,1]] sends it to X^2Y; columns become (c,c+d).
    repeated_g = product_coefficients(c, [c[i] + d[i] for i in range(3)])
    h = sp.expand(repeated_g[1]**2 - 3*repeated_g[0]*repeated_g[2])
    repeated_sos = sp.expand(
        bracket(c, d, 0, 1)**2 * c[2]**2
        + bracket(c, d, 0, 2)**2 * c[1]**2
        + bracket(c, d, 1, 2)**2 * c[0]**2
    )
    assert sp.Poly(repeated_sos - 2*h, *c, *d).is_zero

    # A generic 2-by-2 zero block.  The two top rows can only use the
    # third original column (or its two duplicates), so both permanents
    # vanish identically.
    a, b, u, v, w = sp.symbols("a b u v w", real=True)
    zero_block_matrix = [[0, 0, a], [0, 0, b], [u, v, w]]
    assert permanent(zero_block_matrix) == 0
    assert permanent(duplicate(zero_block_matrix)) == 0

    # Rank-one equality as a polynomial factorial identity.
    x = sp.symbols("x0:3", real=True)
    y = sp.symbols("y0:3", real=True)
    rank_one = [[x[i]*y[j] for j in range(3)] for i in range(3)]
    p3 = permanent(rank_one)
    p6 = permanent(duplicate(rank_one))
    assert sp.Poly(20*p3**2 - p6, *x, *y).is_zero

    print("PASS: distinct GL2/SOS identity")
    print("PASS: repeated GL2/SOS identity")
    print("PASS: symbolic 2x2 zero-block family")
    print("PASS: symbolic rank-one family")
    print("ALL EQUALITY CROSS-CHECKS PASSED")


if __name__ == "__main__":
    main()
