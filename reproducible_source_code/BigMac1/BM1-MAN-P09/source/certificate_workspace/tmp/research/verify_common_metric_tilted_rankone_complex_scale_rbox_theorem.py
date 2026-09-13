#!/usr/bin/env python3
"""Fail-closed exact source verifier for either audited rational r layer."""

if not __debug__:
    raise RuntimeError("fail closed: run without python -O")

import argparse
from math import comb
import sympy as sp


def modulus_square(value):
    return sp.expand_complex(value * sp.conjugate(value))


def original_gate(matrix, a, c):
    vector = sp.Matrix([a, 0, c])
    image = matrix * vector
    square = matrix**2
    return sp.factor(
        a**2 * modulus_square(image[1])
        + sp.Rational(1, 4) * modulus_square(
            c * sp.conjugate(image[0]) + a * image[2]
            + sp.I * (a * c - square[2, 0])
        )
        + sp.Rational(1, 4) * modulus_square(
            c * sp.conjugate(image[1]) - sp.I * square[2, 1]
        )
        - 8 * a**2 * sp.re(image[0]) ** 2
    )


def interval_bernstein_controls(polynomial, variables, bounds):
    poly = sp.Poly(polynomial, *variables, domain=sp.QQ)
    degrees = tuple(poly.degree(variable) for variable in variables)
    coefficients = dict(poly.terms())
    dimension = len(variables)
    for axis, (degree, (left, right)) in enumerate(zip(degrees, bounds)):
        width = right - left
        other_axes = [index for index in range(dimension) if index != axis]
        groups = {
            tuple(monomial[index] for index in other_axes)
            for monomial in coefficients
        }
        transform = {}
        for target in range(degree + 1):
            for source in range(degree + 1):
                transform[target, source] = sum(
                    sp.Rational(comb(source, affine_power), 1)
                    * left ** (source - affine_power)
                    * width**affine_power
                    * sp.Rational(
                        comb(target, affine_power),
                        comb(degree, affine_power),
                    )
                    for affine_power in range(min(target, source) + 1)
                )
        converted = {}
        for group in groups:
            source_values = []
            for source in range(degree + 1):
                monomial = [0] * dimension
                monomial[axis] = source
                for index, exponent in zip(other_axes, group):
                    monomial[index] = exponent
                source_values.append(coefficients.get(tuple(monomial), 0))
            for target in range(degree + 1):
                output = [0] * dimension
                output[axis] = target
                for index, exponent in zip(other_axes, group):
                    output[index] = exponent
                converted[tuple(output)] = sum(
                    transform[target, source] * source_values[source]
                    for source in range(degree + 1)
                )
        coefficients = converted
    return degrees, coefficients


ell, w, k, z, r, T, s = sp.symbols("ell w k z r T s", real=True)
variables = (ell, w, k, z, r)
a = sp.Rational(3, 5)
c = sp.Rational(4, 5)
t = sp.Integer(4)
Delta = sp.factor(r * t - z**2 - w**2)
n = sp.factor(t * (k**2 + ell**2) + r - 2 * (k * z + ell * w))
g = sp.factor(a * c * ell - z * k - w * ell - t)
qmin = s**2 * n / Delta
Q = sp.Matrix([
    [r, s * (k + sp.I * ell), z + sp.I * w],
    [s * (k - sp.I * ell), qmin, s],
    [z - sp.I * w, s, t],
])

active = Q.extract([0, 2], [0, 2])
coupling = Q.extract([0, 2], [1])
assert sp.factor(active.det() - Delta) == 0
assert sp.factor(
    (sp.conjugate(coupling).T * active.inv() * coupling)[0] - qmin
) == 0
assert sp.factor(Q.det()) == 0
danger = sp.factor(sp.re((Q * sp.Matrix([a, 0, c]))[0]))
assert sp.factor(danger - (a * r + c * z)) == 0

qfree = sp.symbols("qfree", real=True)
free_matrix = Q.copy()
free_matrix[1, 1] = qfree
free_image = free_matrix * sp.Matrix([a, 0, c])
last_leak = sp.expand(
    c * sp.conjugate(free_image[1])
    - sp.I * (free_matrix**2)[2, 1]
)
assert sp.factor(sp.im(last_leak) + s * (qfree - g)) == 0
assert sp.factor(qmin - g - (s**2 * n - Delta * g) / Delta) == 0

x = a * r + c * z
L = a * k + c
A = a * c * (r + t) + z - w * (r + t)
B = a * c - w - z * (r + t)
C = c * L + z * ell - w * k
P = sp.expand(
    Delta**2 * (
        (A - T * ell) ** 2 + (B - T * k) ** 2 - 32 * a**2 * x**2
        + T * (4 * a**2 * (L**2 + a**2 * ell**2) + C**2)
    )
    + T * (T * n - Delta * g) ** 2
)
assert sp.factor(4 * Delta**2 * original_gate(Q, a, c) - P.subs(T, s**2)) == 0
scale_poly = sp.Poly(P, T)
C0 = sp.factor(scale_poly.coeff_monomial(1))
C1 = sp.factor(scale_poly.coeff_monomial(T))
C2 = sp.factor(scale_poly.coeff_monomial(T**2))
assert sp.factor(scale_poly.coeff_monomial(T**3) - n**2) == 0
assert sp.factor(C2 - (
    Delta**2 * (k**2 + ell**2) - 2 * Delta * g * n
)) == 0
TL = sp.factor(Delta * g / n)
g0_num, g0_den = sp.cancel(P.subs(T, TL)).as_numer_denom()
g1_num, g1_den = sp.cancel(sp.diff(P, T).subs(T, TL)).as_numer_denom()
assert sp.factor(g0_den - 15625 * n**2) == 0
assert sp.factor(g1_den + 625 * n) == 0
g2 = sp.factor(C2 + 3 * n**2 * TL)
assert sp.factor(g2 - (
    Delta**2 * (k**2 + ell**2) + Delta * g * n
)) == 0

pn = sp.Poly(n, *variables, domain=sp.QQ)
p0 = sp.Poly(C0, *variables, domain=sp.QQ)
p1 = sp.Poly(C1, *variables, domain=sp.QQ)
p2 = sp.Poly(C2, *variables, domain=sp.QQ)
negative_disc = -(
    18 * pn**2 * p2 * p1 * p0
    - 4 * p2**3 * p0
    + p2**2 * p1**2
    - 4 * pn**2 * p1**3
    - 27 * pn**4 * p0**2
)
negative_disc_den, negative_disc_integer = negative_disc.clear_denoms(
    convert=True
)
assert negative_disc_den == 244140625
negative_disc_num = negative_disc_integer.as_expr()

parser = argparse.ArgumentParser()
parser.add_argument(
    "--adjacent-r", action="store_true",
    help="verify r in [101/100,103/100] rather than [99/100,101/100]",
)
arguments = parser.parse_args()

r_bounds = (
    (sp.Rational(101, 100), sp.Rational(103, 100))
    if arguments.adjacent_r
    else (sp.Rational(99, 100), sp.Rational(101, 100))
)
bounds = (
    (sp.Integer(8), sp.Integer(10)),
    (-sp.Rational(31, 100), -sp.Rational(29, 100)),
    (-sp.Rational(301, 100), -sp.Rational(299, 100)),
    (-sp.Rational(101, 100), -sp.Rational(99, 100)),
    r_bounds,
)
if arguments.adjacent_r:
    expected_minima = {
        "danger": sp.Rational(87, 500),
        "Delta": sp.Rational(14619, 5000),
        "n": sp.Rational(1456853, 5000),
        "C0": sp.Rational(448500662246821401, 1250000000000000),
        "C1": sp.Rational(1261378431909517593, 1250000000000000),
        "N0": sp.Rational(
            4642466069575661682742742534193063,
            10000000000000000000000,
        ),
        "N1": sp.Rational(
            3637314850248595682332957, 20000000000000000
        ),
        "ND": sp.Rational(
            18942501765434648654554516142706963646914690725542726020966050250291,
            3200000000000000000000000000000000000000000,
        ),
    }
else:
    expected_minima = {
        "danger": sp.Rational(93, 500),
        "Delta": sp.Rational(14219, 5000),
        "n": sp.Rational(1456753, 5000),
        "C0": sp.Rational(420515573041543529, 1250000000000000),
        "C1": sp.Rational(1195599356262447793, 1250000000000000),
        "N0": sp.Rational(
            544257743489740893611366179477411,
            1250000000000000000000,
        ),
        "N1": sp.Rational(
            3448220588099013077412457, 20000000000000000
        ),
        "ND": sp.Rational(
            16659627721252625696244381239255705449827376815068142600603001925331,
            3200000000000000000000000000000000000000000,
        ),
    }
certificate = [
    ("danger", -danger, (0, 0, 0, 1, 1), expected_minima["danger"]),
    ("Delta", Delta, (0, 2, 0, 2, 1), expected_minima["Delta"]),
    ("n", n, (2, 1, 2, 1, 1), expected_minima["n"]),
    ("C0", C0, (0, 6, 0, 6, 4), expected_minima["C0"]),
    ("C1", C1, (2, 6, 2, 6, 3), expected_minima["C1"]),
    ("N0", g0_num, (5, 10, 5, 10, 6), expected_minima["N0"]),
    ("N1", -g1_num, (4, 7, 4, 7, 4), expected_minima["N1"]),
    ("ND", negative_disc_num, (10, 20, 10, 20, 12), expected_minima["ND"]),
]
control_count = 0
for name, polynomial, expected_degree, expected_minimum in certificate:
    degree, controls = interval_bernstein_controls(polynomial, variables, bounds)
    assert degree == expected_degree, (name, degree)
    assert all(value > 0 for value in controls.values()), name
    assert min(controls.values()) == expected_minimum, name
    control_count += len(controls)
assert control_count == 734288

values = {
    ell: 9,
    w: -sp.Rational(31, 100),
    k: -sp.Rational(301, 100),
    z: -sp.Rational(101, 100),
    r: sp.Rational(103, 100) if arguments.adjacent_r else sp.Rational(99, 100),
    s: 1,
}
Q_exact = sp.simplify(Q.subs(values))
assert Delta.subs(values) == (
    sp.Rational(15019, 5000) if arguments.adjacent_r
    else sp.Rational(14219, 5000)
)
assert n.subs(values) == (
    sp.Rational(1803851, 5000) if arguments.adjacent_r
    else sp.Rational(1803651, 5000)
)
assert g.subs(values) == sp.Rational(699, 10000)
assert Q_exact[1, 1] == (
    sp.Rational(1803851, 15019) if arguments.adjacent_r
    else sp.Rational(1803651, 14219)
)
assert sp.factor(Q_exact.det()) == 0
assert danger.subs(values) == (
    -sp.Rational(19, 100) if arguments.adjacent_r
    else -sp.Rational(107, 500)
)
gate_exact = original_gate(Q_exact, a, c)
expected_gate = (
    sp.Rational(82806323094723125611, 22557036100000000)
    if arguments.adjacent_r
    else sp.Rational(82629943031775348959, 20217996100000000)
)
assert gate_exact == expected_gate > 0
real_exact = Q_exact.applyfunc(sp.re)
expected_phase_increment = (
    -sp.Rational(234143982116037, 150190000000)
    if arguments.adjacent_r
    else -sp.Rational(1176241596854997, 710950000000)
)
assert sp.factor(4 * (
    gate_exact - original_gate(real_exact, a, c)
)) == expected_phase_increment < 0
assert sp.im(Q_exact[0, 1]) * sp.im(Q_exact[0, 2]) < 0

print("PASS original Hermitian gate, danger, and complete legal scale half-line")
print("PASS 734288 strictly positive exact five-axis Bernstein controls")
print("PASS endpoint/derivative/curvature/discriminant partition")
print("PASS exact phase-retaining r-boundary witness")
print("r_bounds=", r_bounds)
print("scope=six-real-parameter partial theorem; general complex gate open")
