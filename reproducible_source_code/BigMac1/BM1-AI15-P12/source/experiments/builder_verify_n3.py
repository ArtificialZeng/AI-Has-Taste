#!/usr/bin/env python3
"""Exact symbolic cross-checks for the Gate-5 n=3 proof-builder audit.

This script is a verifier of displayed polynomial identities, not a numerical
proof.  All arithmetic used in the assertions is exact SymPy arithmetic.
"""

from itertools import permutations

import sympy as sp


def permanent(matrix):
    n = len(matrix)
    return sp.expand(
        sum(
            sp.prod(matrix[i][sigma[i]] for i in range(n))
            for sigma in permutations(range(n))
        )
    )


def pairing(left, right, degree):
    return sp.expand(
        sum(left[k] * right[k] / sp.binomial(degree, k)
            for k in range(degree + 1))
    )


def convolution(left, right):
    result = [sp.Integer(0)] * (len(left) + len(right) - 1)
    for i, x in enumerate(left):
        for j, y in enumerate(right):
            result[i + j] += x * y
    return [sp.expand(x) for x in result]


def verify_canonical_identity():
    g0, g1, g2, g3 = sp.symbols("g0 g1 g2 g3", real=True)
    f = [0, 1, 1, 0]  # XY(X+Y), indexed by the exponent of Y.
    g = [g0, g1, g2, g3]
    delta = sp.factor(pairing(f, g, 3) ** 2
                      - pairing(convolution(f, f), convolution(g, g), 6))
    expected = (
        2 * g1**2 + g1 * g2 + 2 * g2**2
        - 6 * g0 * g2 - 9 * g0 * g3 - 6 * g1 * g3
    ) / 45
    assert sp.factor(delta - expected) == 0
    return delta


def verify_ordered_root_identity():
    t, p, q = sp.symbols("t p q", real=True)
    roots = [t, t + p, t + p + q]
    z = sp.symbols("z")
    poly = sp.Poly(sp.prod(z - root for root in roots), z)
    g3, g2, g1, g0 = poly.all_coeffs()
    numerator = sp.expand(
        2 * g1**2 + g1 * g2 + 2 * g2**2
        - 6 * g0 * g2 - 9 * g0 * g3 - 6 * g1 * g3
    )
    expected = sp.expand(
        2 * (p**2 + p*q + q**2) * t**2
        + (4*p**3 + 6*p**2*q - 2*p**2 + 2*p*q**2
           - 2*p*q - 2*q**2) * t
        + 2*p**4 + 4*p**3*q - 2*p**3 + 2*p**2*q**2
        - 3*p**2*q + 2*p**2 - p*q**2 + 2*p*q + 2*q**2
    )
    assert sp.expand(numerator - expected) == 0
    discriminant = sp.factor(sp.discriminant(numerator, t))
    positive_sum = (
        p**4*q**2 + p**4 + 2*p**3*q**3 + 2*p**3*q
        + p**2*q**4 + 3*p**2*q**2 + 2*p*q**3 + q**4
    )
    assert sp.expand(discriminant + 12 * positive_sum) == 0
    return numerator, discriminant


def verify_double_root_stratum():
    g0, g1, g2, g3 = sp.symbols("g0 g1 g2 g3", real=True)
    f = [0, 1, 0, 0]  # X^2 Y.
    g = [g0, g1, g2, g3]
    delta = sp.factor(pairing(f, g, 3) ** 2
                      - pairing(convolution(f, f), convolution(g, g), 6))
    assert sp.factor(delta - sp.Rational(2, 45)*(g1**2 - 3*g0*g2)) == 0
    return delta


def verify_against_permanent_enumeration():
    # A deterministic exact example with rank exactly two and mixed signs.
    rows = [(-1, 0), (0, -2), (-1, -2)]
    cols = [(2, 1), (-2, 0), (0, 2)]
    matrix = [[sp.Integer(a*c + b*d) for c, d in cols] for a, b in rows]
    block = [matrix[i % 3] + matrix[i % 3] for i in range(6)]

    x, y = sp.symbols("x y")
    fpoly = sp.Poly(sp.prod(a*x + b*y for a, b in rows), x, y)
    gpoly = sp.Poly(sp.prod(c*x + d*y for c, d in cols), x, y)
    f = [fpoly.coeff_monomial(x**(3-k)*y**k) for k in range(4)]
    g = [gpoly.coeff_monomial(x**(3-k)*y**k) for k in range(4)]

    per3 = permanent(matrix)
    per6 = permanent(block)
    assert per3 == sp.factorial(3) * pairing(f, g, 3)
    assert per6 == sp.factorial(6) * pairing(convolution(f, f),
                                             convolution(g, g), 6)
    assert per6 > 0
    assert per6 <= sp.binomial(6, 3) * per3**2
    return matrix, per3, per6


def main():
    delta = verify_canonical_identity()
    numerator, discriminant = verify_ordered_root_identity()
    double_delta = verify_double_root_stratum()
    matrix, per3, per6 = verify_against_permanent_enumeration()
    print("canonical_delta =", delta)
    print("ordered_root_numerator =", numerator)
    print("ordered_root_discriminant =", discriminant)
    print("double_root_delta =", double_delta)
    print("exact_test_matrix =", matrix)
    print("per(T) =", per3)
    print("per([[T,T],[T,T]]) =", per6)
    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
