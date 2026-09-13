#!/usr/bin/env python3
"""Independent five-axis nodal referee for either rational r layer.

No discovery or source verifier is imported.  The cubic is extracted from
the original fully conjugated gate.  Every control is recovered from exact
rational nodes and every node is reconstructed from the recovered controls.
"""

if not __debug__:
    raise RuntimeError("fail closed: run without python -O")

import argparse
from functools import lru_cache
import gc
import sympy as sp


def square_modulus(value):
    return sp.expand_complex(value * sp.conjugate(value))


def original_gate(matrix):
    a = sp.Rational(3, 5)
    c = sp.Rational(4, 5)
    vector = sp.Matrix([a, 0, c])
    image = matrix * vector
    square = matrix**2
    return sp.expand(
        a**2 * square_modulus(image[1])
        + sp.Rational(1, 4) * square_modulus(
            c * sp.conjugate(image[0]) + a * image[2]
            + sp.I * (a * c - square[2, 0])
        )
        + sp.Rational(1, 4) * square_modulus(
            c * sp.conjugate(image[1]) - sp.I * square[2, 1]
        )
        - 8 * a**2 * sp.re(image[0]) ** 2
    )


@lru_cache(maxsize=None)
def bernstein_collocation(degree):
    if degree == 0:
        matrix = sp.eye(1)
    else:
        matrix = sp.Matrix([
            [
                sp.binomial(degree, column)
                * sp.Rational(row, degree) ** column
                * (1 - sp.Rational(row, degree)) ** (degree - column)
                for column in range(degree + 1)
            ]
            for row in range(degree + 1)
        ])
    return matrix, matrix.inv()


def apply_axis_transform(coefficients, degrees, axis, transform):
    dimension = len(degrees)
    degree = degrees[axis]
    other_axes = [index for index in range(dimension) if index != axis]
    groups = {
        tuple(index[index_other] for index_other in other_axes)
        for index in coefficients
    }
    converted = {}
    for group in groups:
        source_values = []
        for source in range(degree + 1):
            index = [0] * dimension
            index[axis] = source
            for index_other, exponent in zip(other_axes, group):
                index[index_other] = exponent
            source_values.append(coefficients.get(tuple(index), 0))
        for target in range(degree + 1):
            index = [0] * dimension
            index[axis] = target
            for index_other, exponent in zip(other_axes, group):
                index[index_other] = exponent
            converted[tuple(index)] = sum(
                transform[target, source] * source_values[source]
                for source in range(degree + 1)
            )
    return converted


def nodal_bernstein_statistics(polynomial, variables, bounds):
    poly = sp.Poly(polynomial, *variables, domain=sp.QQ)
    degrees = tuple(poly.degree(variable) for variable in variables)
    coefficients = dict(poly.terms())
    collocations = []

    # Original power coefficients -> complete exact rational node tensor.
    for axis, (degree, (left, right)) in enumerate(zip(degrees, bounds)):
        points = [
            left + (right - left) * sp.Rational(index, degree)
            if degree else left
            for index in range(degree + 1)
        ]
        power_to_nodes = sp.Matrix([
            [point**source for source in range(degree + 1)]
            for point in points
        ])
        coefficients = apply_axis_transform(
            coefficients, degrees, axis, power_to_nodes
        )
        collocations.append(bernstein_collocation(degree))
    nodal_values = coefficients

    # Five independent exact collocation inversions.
    for axis, (_, inverse) in enumerate(collocations):
        coefficients = apply_axis_transform(
            coefficients, degrees, axis, inverse
        )
    count = len(coefficients)
    minimum = min(coefficients.values())
    positive = all(value > 0 for value in coefficients.values())

    # Reconstruct every node.  Drop the extra controls reference so the large
    # discriminant tensor keeps only the node tensor and current transform.
    reconstruction = coefficients
    del coefficients
    gc.collect()
    for axis, (matrix, _) in enumerate(collocations):
        reconstruction = apply_axis_transform(
            reconstruction, degrees, axis, matrix
        )
        gc.collect()
    assert reconstruction == nodal_values
    return degrees, count, minimum, positive


ell, w, k, z, r, tau, T, qfree = sp.symbols(
    "ell w k z r tau T qfree", real=True
)
variables = (ell, w, k, z, r)
I = sp.I
a = sp.Rational(3, 5)
c = sp.Rational(4, 5)
t = sp.Integer(4)
Delta = r * t - z**2 - w**2
n = t * (k**2 + ell**2) + r - 2 * (k * z + ell * w)
qmin = tau**2 * n / Delta
matrix = sp.Matrix([
    [r, tau * (k + I * ell), z + I * w],
    [tau * (k - I * ell), qmin, tau],
    [z - I * w, tau, t],
])

active = matrix.extract([0, 2], [0, 2])
coupling = matrix.extract([0, 2], [1])
assert sp.factor(active.det() - Delta) == 0
assert sp.factor(
    (sp.conjugate(coupling).T * active.inv() * coupling)[0] - qmin
) == 0
assert sp.factor(matrix.det()) == 0
danger = sp.factor(sp.re((matrix * sp.Matrix([a, 0, c]))[0]))
assert sp.factor(danger - (a * r + c * z)) == 0

free_matrix = matrix.copy()
free_matrix[1, 1] = qfree
free_image = free_matrix * sp.Matrix([a, 0, c])
last_leak = sp.expand(
    c * sp.conjugate(free_image[1])
    - I * (free_matrix**2)[2, 1]
)
g = a * c * ell - z * k - w * ell - t
assert sp.factor(sp.im(last_leak) + tau * (qfree - g)) == 0
assert sp.factor(qmin - g - (tau**2 * n - Delta * g) / Delta) == 0

raw_tau = sp.Poly(sp.expand(4 * Delta**2 * original_gate(matrix)), tau)
assert all(monomial[0] % 2 == 0 for monomial, _ in raw_tau.terms())
scale_poly = sp.Poly(sum(
    coefficient * T ** (monomial[0] // 2)
    for monomial, coefficient in raw_tau.terms()
), T)
assert scale_poly.degree() == 3
P = scale_poly.as_expr()
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

bb, d2, d1, d0, X = sp.symbols("bb d2 d1 d0 X", real=True)
universal = bb * X**3 + d2 * X**2 + d1 * X + d0
formula = (
    18 * bb * d2 * d1 * d0 - 4 * d2**3 * d0 + d2**2 * d1**2
    - 4 * bb * d1**3 - 27 * bb**2 * d0**2
)
assert sp.factor(sp.discriminant(universal, X) - formula) == 0
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
    help="audit r in [101/100,103/100] rather than [99/100,101/100]",
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
expected = [
    ("danger", -danger, (0, 0, 0, 1, 1), 4, expected_minima["danger"]),
    ("Delta", Delta, (0, 2, 0, 2, 1), 18, expected_minima["Delta"]),
    ("n", n, (2, 1, 2, 1, 1), 72, expected_minima["n"]),
    ("C0", C0, (0, 6, 0, 6, 4), 245, expected_minima["C0"]),
    ("C1", C1, (2, 6, 2, 6, 3), 1764, expected_minima["C1"]),
    ("N0", g0_num, (5, 10, 5, 10, 6), 30492, expected_minima["N0"]),
    ("N1", -g1_num, (4, 7, 4, 7, 4), 8000, expected_minima["N1"]),
    ("ND", negative_disc_num, (10, 20, 10, 20, 12), 693693, expected_minima["ND"]),
]
control_count = 0
for name, polynomial, claimed_degree, claimed_count, claimed_minimum in expected:
    degree, count, minimum, positive = nodal_bernstein_statistics(
        polynomial, variables, bounds
    )
    assert degree == claimed_degree, (name, degree)
    assert count == claimed_count, (name, count)
    assert positive, name
    assert minimum == claimed_minimum, name
    control_count += count
assert control_count == 734288

witness_values = {
    ell: 9,
    w: -sp.Rational(31, 100),
    k: -sp.Rational(301, 100),
    z: -sp.Rational(101, 100),
    r: sp.Rational(103, 100) if arguments.adjacent_r else sp.Rational(99, 100),
    tau: 1,
}
witness = matrix.subs(witness_values)
assert sp.factor(witness.det()) == 0
assert Delta.subs(witness_values) == (
    sp.Rational(15019, 5000) if arguments.adjacent_r
    else sp.Rational(14219, 5000)
)
assert n.subs(witness_values) == (
    sp.Rational(1803851, 5000) if arguments.adjacent_r
    else sp.Rational(1803651, 5000)
)
assert g.subs(witness_values) == sp.Rational(699, 10000)
assert witness[1, 1] == (
    sp.Rational(1803851, 15019) if arguments.adjacent_r
    else sp.Rational(1803651, 14219)
)
assert danger.subs(witness_values) == (
    -sp.Rational(19, 100) if arguments.adjacent_r
    else -sp.Rational(107, 500)
)
witness_gate = sp.factor(original_gate(witness))
expected_witness_gate = (
    sp.Rational(82806323094723125611, 22557036100000000)
    if arguments.adjacent_r
    else sp.Rational(82629943031775348959, 20217996100000000)
)
assert witness_gate == expected_witness_gate > 0
real_witness = witness.applyfunc(sp.re)
expected_phase_increment = (
    -sp.Rational(234143982116037, 150190000000)
    if arguments.adjacent_r
    else -sp.Rational(1176241596854997, 710950000000)
)
assert sp.factor(4 * (
    witness_gate - original_gate(real_witness)
)) == expected_phase_increment < 0
assert sp.im(witness[0, 1]) * sp.im(witness[0, 2]) < 0

print("PASS independent original-gate, danger, and legal-half-line reconstruction")
print("PASS independent nodal reconstruction of 734288 Bernstein controls")
print("PASS independent endpoint/derivative/discriminant sign audit")
print("PASS independent exact phase-integrity r-boundary witness")
print("r_bounds=", r_bounds)
print("scope=six-real-parameter partial theorem; unrestricted gate remains open")
