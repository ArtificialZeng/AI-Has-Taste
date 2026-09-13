#!/usr/bin/env python3
"""Independent exact checks for the referee's n=3 reduction.

This script deliberately does not import discovery or proof-builder code.  It
uses two evaluators: direct permutation enumeration and the binary-form
coefficient formula.  All arithmetic in the tests is over Python integers or
SymPy polynomials.
"""

from itertools import permutations
from math import comb, factorial, prod
from random import Random

import sympy as sp


def permanent_direct(matrix):
    n = len(matrix)
    return sum(prod(matrix[i][sigma[i]] for i in range(n))
               for sigma in permutations(range(n)))


def block_double(matrix):
    return [row + row for row in matrix] + [row + row for row in matrix]


def binary_coefficients(vectors):
    """Coefficients of product_i (x_i + u_i z), in ascending order."""
    coefficients = [1]
    for x_i, u_i in vectors:
        updated = [0] * (len(coefficients) + 1)
        for k, value in enumerate(coefficients):
            updated[k] += x_i * value
            updated[k + 1] += u_i * value
        coefficients = updated
    return coefficients


def convolution(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, x_i in enumerate(left):
        for j, y_j in enumerate(right):
            result[i + j] += x_i * y_j
    return result


def permanent_rank_two(row_vectors, column_vectors):
    n = len(row_vectors)
    a = binary_coefficients(row_vectors)
    b = binary_coefficients(column_vectors)
    return sum(factorial(k) * factorial(n - k) * a[k] * b[k]
               for k in range(n + 1))


def permanent_doubled_rank_two(row_vectors, column_vectors):
    n = len(row_vectors)
    a2 = convolution(binary_coefficients(row_vectors),
                     binary_coefficients(row_vectors))
    b2 = convolution(binary_coefficients(column_vectors),
                     binary_coefficients(column_vectors))
    return sum(factorial(k) * factorial(2 * n - k) * a2[k] * b2[k]
               for k in range(2 * n + 1))


def symbolic_checks():
    # Start from coefficient definitions rather than a stored expansion.
    a = sp.symbols("a0:4")
    b = sp.symbols("b0:4")
    a2 = convolution(a, a)
    b2 = convolution(b, b)
    per_t = sum(factorial(k) * factorial(3 - k) * a[k] * b[k]
                for k in range(4))
    per_block = sum(factorial(k) * factorial(6 - k) * a2[k] * b2[k]
                    for k in range(7))
    gap = sp.expand(comb(6, 3) * per_t**2 - per_block)

    # Three distinct row directions can be gauged to factors 1, z, 1+z,
    # hence a=(0,1,1,0).  Finite column directions have coefficients given
    # by product_j(1+r_j z).
    t, p, q = sp.symbols("t p q", real=True)
    roots = (t + p, t + q, t - p - q)
    s1 = sum(roots)
    s2 = sum(roots[i] * roots[j] for i in range(3) for j in range(i + 1, 3))
    s3 = prod(roots)
    canonical_gap = sp.expand(gap.subs(dict(zip(a, (0, 1, 1, 0)))).subs(
        dict(zip(b, (1, s1, s2, s3)))))
    S = p**2 + p * q + q**2
    h = p * q * (p + q)
    E = 6 * S * t**2 + 6 * (S + 3 * h) * t + 2 * S**2 + 9 * h + 6 * S
    assert sp.expand(canonical_gap - 16 * E) == 0

    A = 6 * S
    B = 6 * (S + 3 * h)
    C = 2 * S**2 + 9 * h + 6 * S
    discriminant_certificate = (p - q)**2 * (2 * p + q)**2 * (p + 2 * q)**2
    assert sp.expand(4 * S**3 - 27 * h**2 - discriminant_certificate) == 0
    assert sp.expand(4 * A * C - B**2
                     - 12 * (discriminant_certificate + 9 * S**2)) == 0

    # Repeated row direction: factors 1,1,z, hence a=(0,1,0,0).
    repeated_gap = sp.factor(gap.subs(dict(zip(a, (0, 1, 0, 0)))))
    assert sp.expand(repeated_gap - 32 * (b[1]**2 - 3 * b[0] * b[2])) == 0
    return sp.factor(gap)


def evaluator_cross_checks():
    rng = Random(20260829)
    for n, trials in ((3, 40), (4, 12)):
        for _ in range(trials):
            rows = [(rng.randint(-3, 3), rng.randint(-3, 3)) for _ in range(n)]
            columns = [(rng.randint(-3, 3), rng.randint(-3, 3)) for _ in range(n)]
            matrix = [[x_i * y_j + u_i * v_j for y_j, v_j in columns]
                      for x_i, u_i in rows]
            assert permanent_direct(matrix) == permanent_rank_two(rows, columns)
            assert permanent_direct(block_double(matrix)) == \
                permanent_doubled_rank_two(rows, columns)

    # A rank-two equality case that a proof must not lose by dividing by per(T).
    sparse = [[0, 0, 1], [0, 0, 1], [1, 1, 0]]
    assert permanent_direct(sparse) == 0
    assert permanent_direct(block_double(sparse)) == 0


if __name__ == "__main__":
    factorized_gap = symbolic_checks()
    evaluator_cross_checks()
    print("PASS: exact symbolic identities and independent direct evaluators")
    print("n=3 coefficient gap:", factorized_gap)
