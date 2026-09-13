#!/usr/bin/env python3
"""Exact reconstruction checks for proof/agent_builder_report.md.

This is a builder-side checker, not the independent release verifier.  It uses
only SymPy exact arithmetic and raises AssertionError on every mismatch.
"""

from math import comb

import sympy as sp


def exact_zero(expr):
    assert sp.cancel(sp.together(expr)) == 0


def section_polynomial(coords, negative_pairs=()):
    """Balanced Q_5 numerator P_N from report equation (4.2)."""
    t = sum(coords) / 2
    p = t**4 - sum((t - x) ** 4 for x in coords)
    p += sum(
        (t - coords[i] - coords[j]) ** 4
        for i in range(5)
        for j in range(i + 1, 5)
    )
    p -= 2 * sum((t - coords[i] - coords[j]) ** 4 for i, j in negative_pairs)
    return sp.expand(p)


def verify_n4_hessian():
    a = sp.symbols("a0:4", positive=True)
    t = sum(a) / 2
    # At (1,1,2,2), pair 01 is strictly below half and the other two
    # representative pair forms vanish; their second Hessians vanish too.
    p = sp.expand(t**3 - sum((t - x) ** 3 for x in a) + (t - a[0] - a[1]) ** 3)
    norm = sp.sqrt(sum(x * x for x in a))
    f = norm * p / (6 * sp.prod(a))
    root10 = sp.sqrt(10)
    point = {a[0]: 1 / root10, a[1]: 1 / root10,
             a[2]: 2 / root10, a[3]: 2 / root10}
    assert all(sp.simplify(sp.diff(f, x).subs(point)) == 0 for x in a)
    h = sp.simplify(sp.hessian(f, a).subs(point))
    expected = root10 * sp.Matrix([
        [-sp.Rational(1, 8), sp.Rational(7, 24), -sp.Rational(1, 24), -sp.Rational(1, 24)],
        [sp.Rational(7, 24), -sp.Rational(1, 8), -sp.Rational(1, 24), -sp.Rational(1, 24)],
        [-sp.Rational(1, 24), -sp.Rational(1, 24), -sp.Rational(1, 2), sp.Rational(13, 24)],
        [-sp.Rational(1, 24), -sp.Rational(1, 24), sp.Rational(13, 24), -sp.Rational(1, 2)],
    ])
    assert h == expected
    vectors = [
        (sp.Matrix([1, -1, 0, 0]), -5 * root10 / 12),
        (sp.Matrix([0, 0, 1, -1]), -25 * root10 / 24),
        (sp.Matrix([2, 2, -1, -1]), 5 * root10 / 24),
    ]
    for vector, eigenvalue in vectors:
        exact_zero((vector.T * h * vector)[0] / vector.dot(vector) - eigenvalue)


def two_value_expected():
    r = sp.symbols("r", real=True)
    h1 = r**6 - 12*r**5 + 51*r**4 - 96*r**3 + 96*r**2 - 64
    h2 = 16*r**5 - 48*r**4 + 40*r**3 - 8*r**2 - 9*r + 3
    h3 = 3*r**5 - 9*r**4 - 8*r**3 + 40*r**2 - 48*r + 16
    return r, {
        (1, 1): (
            r * (3*r**3 - 16*r**2 + 128) / 8,
            sp.Rational(3, 2) * r**4 * (r - 3) * (r - 1),
        ),
        (1, -1): (
            -(r**4 - 16*r**3 + 96*r**2 - 256*r + 64) / 8,
            -h1 / 2,
        ),
        (2, 1): (
            (16*r**4 - 96*r**3 + 216*r**2 - 24*r + 3) / 8,
            sp.Rational(3, 4) * (r - 1) * h2,
        ),
        (2, -1): (
            3 * (32*r - 13) / 4,
            sp.Rational(3, 2) * (13*r**2 - 48*r + 39),
        ),
        (3, 1): (
            (3*r**4 - 24*r**3 + 216*r**2 - 96*r + 16) / 8,
            sp.Rational(3, 4) * (r - 1) * h3,
        ),
        (3, -1): (2 * (9*r**2 - 2), -12 * (r**2 - 2)),
        (4, 1): (
            (128*r**3 - 16*r + 3) / 8,
            -sp.Rational(3, 2) * (r - 1) * (3*r - 1),
        ),
    }, (h1, h2, h3)


def two_value_polynomial(m, upper_piece, r):
    """Construct P_m directly by complement-paired linear forms."""
    q = 5 - m
    t = (m * r + q) / 2
    lx, ly = t - r, t - 1
    p = t**4 - m * lx**4 - q * ly**4
    pair_types = []
    if m >= 2:
        pair_types.append((t - 2*r, comb(m, 2), -1 if upper_piece else 1))
    # Only these cross-pair forms change sign in the m=1 upper piece.
    cross_sign = -1 if m == 1 and upper_piece else 1
    pair_types.append((t - r - 1, m*q, cross_sign))
    if q >= 2:
        pair_types.append((t - 2, comb(q, 2), 1))
    for linear_form, multiplicity, sign in pair_types:
        p += multiplicity * sign * linear_form**4
    return sp.expand(p)


def verify_two_value_table_and_sturm():
    r, expected, hs = two_value_expected()
    for (m, piece), (wanted_p, wanted_e) in expected.items():
        upper = piece == -1
        p = two_value_polynomial(m, upper, r)
        q = 5 - m
        s = m*r*r + q
        e = sp.expand(r*s*sp.diff(p, r) - m*((m - 1)*r*r + q)*p)
        exact_zero(p - wanted_p)
        exact_zero(e - wanted_e)

    h1, h2, h3 = hs
    assert sp.Poly(h1, r).count_roots(2, 4) == 0
    assert sp.Poly(h2, r).count_roots(1, sp.Rational(3, 2)) == 0
    assert sp.Poly(h3, r).count_roots(1, 2) == 0


def verify_q5_hessians():
    a = sp.symbols("a0:5", positive=True)
    r = sp.symbols("r", positive=True)
    s = 2*r*r + 3
    p = section_polynomial(a, negative_pairs=((0, 1),))
    norm = sp.sqrt(sum(x*x for x in a))
    f = norm * p / (24 * sp.prod(a))
    point = {a[0]: r, a[1]: r, a[2]: 1, a[3]: 1, a[4]: 1}
    gradients = [sp.factor(sp.diff(f, x).subs(point)) for x in a]
    exact_zero(gradients[0] - (13*r*r - 48*r + 39) / (32*r**3*sp.sqrt(s)))
    exact_zero(gradients[2] + (13*r*r - 48*r + 39) / (48*r**2*sp.sqrt(s)))
    h = sp.hessian(f, a).subs(point)
    vectors = {
        "large": sp.Matrix([1, -1, 0, 0, 0]),
        "small": sp.Matrix([0, 0, 1, -1, 0]),
        "block": sp.Matrix([3, 3, -2*r, -2*r, -2*r]),
    }
    # Multiplication by s converts the Hessian at (r,r,1,1,1) to the
    # Hessian at its unit normalization.
    eigenvalues = {
        "large": -3*sp.sqrt(s)*(16*r**4 - 32*r**3 + 37*r**2 - 32*r + 13)/(32*r**4),
        "small": -sp.sqrt(s)*(5*r**2 - 16*r + 14)/(16*r**2),
        "block": sp.sqrt(s)*(32*r**3 - 65*r**2 + 96*r - 117)/(32*r**4),
    }
    modulus = 13*r*r - 48*r + 39
    for name, vector in vectors.items():
        rayleigh = s * (vector.T * h * vector)[0] / vector.dot(vector)
        numerator = sp.together(rayleigh - eigenvalues[name]).as_numer_denom()[0]
        assert sp.rem(numerator, modulus, r) == 0

    alpha = (24 + sp.sqrt(69)) / 13
    positive_factors = [
        16*r**4 - 32*r**3 + 37*r**2 - 32*r + 13,
        5*r**2 - 16*r + 14,
        32*r**3 - 65*r**2 + 96*r - 117,
    ]
    assert all(sp.simplify(expr.subs(r, alpha)) > 0 for expr in positive_factors)

    # The diagonal Q_5 Hessian.
    all_positive_p = section_polynomial(a)
    diagonal_f = norm * all_positive_p / (24 * sp.prod(a))
    root5 = sp.sqrt(5)
    diagonal = {x: 1/root5 for x in a}
    diagonal_h = sp.simplify(sp.hessian(diagonal_f, a).subs(diagonal))
    wanted = sp.Matrix(5, 5, lambda i, j: -root5/8 if i == j else root5/32)
    assert diagonal_h == wanted


def verify_transverse_d4_series():
    t = sp.symbols("t", positive=True)
    coords = [sp.Integer(1)] * 4 + [t]
    p = section_polynomial(coords)
    f = sp.sqrt(t*t + 4) * p / (24*t)
    target = sp.sqrt(t*t + 4) * (3*t**3 - 16*t**2 + 128) / 192
    exact_zero(f - target)
    assert sp.series(f, t, 0, 4) == sp.Rational(4, 3) + t**3/32 + sp.Order(t**4)


def main():
    verify_n4_hessian()
    verify_two_value_table_and_sturm()
    verify_q5_hessians()
    verify_transverse_d4_series()
    print("builder exact checks: PASS")


if __name__ == "__main__":
    main()
