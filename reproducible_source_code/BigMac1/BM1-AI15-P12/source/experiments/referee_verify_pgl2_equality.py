#!/usr/bin/env python3
"""Independent exact verification of the homogeneous n=3 normal forms.

The script starts with the permutation definition of the permanent.  It does
not import the builder, certificate, or discovery evaluators.
"""

from itertools import permutations

import sympy as sp


def permanent(matrix):
    n = len(matrix)
    return sp.expand(sum(
        sp.prod(matrix[i][sigma[i]] for i in range(n))
        for sigma in permutations(range(n))
    ))


def doubled(matrix):
    n = len(matrix)
    return [[matrix[i % n][j % n] for j in range(2 * n)]
            for i in range(2 * n)]


def determinant_pair(c, d, i, j):
    return d[i] * c[j] - c[i] * d[j]


def gap_for_row_parameters(parameters, c, d):
    matrix = [[c[j] + parameters[i] * d[j] for j in range(3)]
              for i in range(3)]
    return sp.expand(20 * permanent(matrix)**2 - permanent(doubled(matrix)))


def main():
    c = sp.symbols("c0:3", real=True)
    d = sp.symbols("d0:3", real=True)

    distinct_gap = gap_for_row_parameters((-1, 0, 1), c, d)
    distinct_sos = 16 * (
        determinant_pair(c, d, 1, 2)**2 * (d[0]**2 + 3 * c[0]**2)
        + determinant_pair(c, d, 0, 2)**2 * (d[1]**2 + 3 * c[1]**2)
        + determinant_pair(c, d, 0, 1)**2 * (d[2]**2 + 3 * c[2]**2)
    )
    assert sp.Poly(sp.expand(distinct_gap - distinct_sos), *c, *d,
                   domain=sp.ZZ).is_zero

    repeated_gap = gap_for_row_parameters((0, 0, 1), c, d)
    repeated_sos = 16 * (
        determinant_pair(c, d, 0, 1)**2 * c[2]**2
        + determinant_pair(c, d, 0, 2)**2 * c[1]**2
        + determinant_pair(c, d, 1, 2)**2 * c[0]**2
    )
    assert sp.Poly(sp.expand(repeated_gap - repeated_sos), *c, *d,
                   domain=sp.ZZ).is_zero

    # Sufficiency families, again from the permanent definition.
    a, b, u, v, w = sp.symbols("a b u v w", real=True)
    zero_block = [[0, 0, a], [0, 0, b], [u, v, w]]
    assert permanent(zero_block) == 0
    assert permanent(doubled(zero_block)) == 0

    x = sp.symbols("x0:3", real=True)
    y = sp.symbols("y0:3", real=True)
    rank_one = [[x[i] * y[j] for j in range(3)] for i in range(3)]
    assert sp.Poly(
        sp.expand(20 * permanent(rank_one)**2 - permanent(doubled(rank_one))),
        *x, *y, domain=sp.ZZ,
    ).is_zero

    print("PASS: distinct homogeneous SOS from 3! and 6! definitions")
    print("PASS: repeated homogeneous SOS from 3! and 6! definitions")
    print("PASS: rank-one and 2x2-zero-block sufficiency families")


if __name__ == "__main__":
    main()
