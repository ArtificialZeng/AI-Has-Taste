#!/usr/bin/env python3
"""Fail-closed exact source verifier for the high-Z bridge phase tube.

The program imports no discovery output or frozen coefficient table.  It
rebuilds the fully conjugated Hermitian Q,Q^2 gate, maps the rational phase
tube to a unit cube, and certifies all signs by exact tensor Bernstein data.
"""

if not __debug__:
    raise RuntimeError("fail closed: optimized Python disables verification")

from hashlib import sha256
from itertools import product
from math import comb
import os
from pathlib import Path
import sys

import sympy as sp


if len(sys.argv) != 1:
    raise SystemExit("usage: source verifier accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
DEPENDENCIES = {
    "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md":
        "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_axis_cap_bridge_arc_theorem.md":
        "fd3610ec3c5d3e4f8f804c03f4210e316bfbe13ff13a6fa60b512617f95011d9",
}
if os.environ.get("AXIS_CAP_PHASE_TUBE_TEST_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[next(iter(DEPENDENCIES))] = "0" * 64


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(f"verification failed: {label}")


for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    require(path.is_file(), f"missing dependency {relative}")
    require(sha256(path.read_bytes()).hexdigest() == expected,
            f"dependency hash mismatch {relative}")


def exact_zero(expression, label):
    if isinstance(expression, sp.MatrixBase):
        for row in range(expression.rows):
            for column in range(expression.cols):
                exact_zero(expression[row, column], f"{label}[{row},{column}]")
        return
    value = sp.factor(sp.cancel(sp.together(sp.expand_complex(expression))))
    require(value == 0, f"{label}: {value}")


def reduce_q(expression, q, relation):
    if isinstance(expression, sp.MatrixBase):
        return expression.applyfunc(lambda entry: reduce_q(entry, q, relation))
    numerator, denominator = sp.cancel(sp.together(expression)).as_numer_denom()
    remainder = sp.Poly(sp.expand(numerator), q).rem(relation).as_expr()
    return sp.factor(remainder / denominator)


def even_h_to_S(expression, h, S):
    result = 0
    for (degree,), coefficient in sp.Poly(sp.expand(expression), h).terms():
        require(degree % 2 == 0, f"odd h power {degree}")
        result += coefficient * S ** (degree // 2)
    return sp.expand(result)


def bernstein_controls(polynomial, variables, declared_degrees=None):
    poly = sp.Poly(sp.expand(polynomial), *variables, domain=sp.QQ)
    natural_degrees = tuple(poly.degree(variable) for variable in variables)
    degrees = natural_degrees if declared_degrees is None else declared_degrees
    require(len(degrees) == len(variables), "Bernstein arity")
    require(all(natural <= declared
                for natural, declared in zip(natural_degrees, degrees)),
            f"declared degree too small {natural_degrees} versus {degrees}")
    power = dict(poly.terms())
    controls = {}
    for index in product(*(range(degree + 1) for degree in degrees)):
        value = sp.Rational(0)
        for monomial in product(*(range(entry + 1) for entry in index)):
            term = power.get(monomial, sp.Rational(0))
            for control, exponent, degree in zip(index, monomial, degrees):
                term *= sp.Rational(comb(control, exponent),
                                    comb(degree, exponent))
            value += term
        controls[index] = sp.factor(value)
    return natural_degrees, degrees, controls


def certify_strict(polynomial, variables, expected_degrees, expected_count,
                   expected_minimum, label):
    natural, degrees, controls = bernstein_controls(polynomial, variables)
    require(natural == expected_degrees, f"{label} degrees {natural}")
    require(degrees == expected_degrees, f"{label} declared degrees")
    require(len(controls) == expected_count, f"{label} control count")
    require(all(value > 0 for value in controls.values()),
            f"{label} strict controls")
    minimum = min(controls.items(), key=lambda item: item[1])
    require(minimum == expected_minimum, f"{label} minimum {minimum}")
    return controls


R, I = sp.Rational, sp.I
h, q, lam = sp.symbols("h q lambda", real=True)
S, Z, x, y = sp.symbols("S Z x y", real=True)
u, v, tau = sp.symbols("u v tau", real=True)
a, c = 1 / sp.sqrt(6), sp.sqrt(R(5, 6))
zeta = R(4, 5) + I * R(3, 5)
p = sp.Matrix([a, 0, c])
rvec = sp.Matrix([-a, 0, c * zeta])
fvec = sp.Matrix([-c * h, q, -a * h * zeta])
basis = sp.Matrix.hstack(rvec, fvec)
q_relation = sp.Poly(q**2 - (1 - h**2), q)
exact_zero(reduce_q(basis.conjugate().T * basis - sp.eye(2), q, q_relation),
           "compression frame Gram")

j = (1 + 5 * x) / (3 * sp.sqrt(5))
kappa = (-3 + 5 * y) / (3 * sp.sqrt(5))
compression = sp.Matrix([
    [h**2, h * (j + I * kappa)],
    [h * (j - I * kappa), j**2 + kappa**2 + R(5, 9) * Z],
])
exact_zero(compression - compression.conjugate().T, "compression Hermitian")
exact_zero(compression.det() - R(5, 9) * h**2 * Z,
           "compression determinant")

H = sp.expand(basis * compression * basis.conjugate().T)
Q = sp.expand(lam * H)
exact_zero(Q - Q.conjugate().T, "Q Hermitian")
image = sp.expand(Q * p)
Q2 = sp.expand(Q * Q)
first = c * sp.conjugate(image[0]) + a * image[2] \
    + I * (a * c - Q2[2, 0])
leakage = c * sp.conjugate(image[1]) - I * Q2[2, 1]
raw_full = sp.expand_complex(
    4 * a**2 * image[1] * sp.conjugate(image[1])
    + first * sp.conjugate(first)
    + leakage * sp.conjugate(leakage)
    - 32 * a**2 * sp.re(image[0])**2
)
raw_gate = reduce_q(raw_full, q, q_relation)

danger_formula = R(5, 36) * sp.sqrt(6) * lam * h**2 \
    * (x**2 + y**2 + Z - 1)
exact_zero(reduce_q(sp.re(image[0]) - danger_formula, q, q_relation),
           "unit-ball danger identity")

gate36 = even_h_to_S(36 * raw_gate, h, S)
require(not gate36.has(h, q), "frame variables survived")
quartic = sp.Poly(gate36, lam)
require(quartic.degree() == 4, "positive-scale quartic degree")
require(quartic.nth(0) == 5, "constant coefficient five")
coefficients = [sp.factor(quartic.nth(power)) for power in range(5)]

# A raw/reduced calibration strictly inside the new tube and with y!=0.
raw_point = {
    h: R(3, 5), q: R(4, 5), lam: R(7, 5),
    x: R(1, 16), y: R(1, 128), Z: R(251, 256),
}
reduced_point = {
    S: R(9, 25), lam: R(7, 5),
    x: R(1, 16), y: R(1, 128), Z: R(251, 256),
}
raw_value = sp.factor(36 * raw_full.subs(raw_point))
reduced_value = sp.factor(gate36.subs(reduced_point))
expected_raw = R(
    2190361703821949821239444799,
    52776558133248000000000000,
)
require(raw_value == expected_raw, "nonzero-y raw calibration value")
exact_zero(raw_value - reduced_value, "nonzero-y raw/reduced calibration")

for power in range(1, 5):
    quotient, remainder = sp.div(
        sp.Poly(coefficients[power], S, Z, x, y),
        sp.Poly(S, S, Z, x, y),
    )
    require(remainder.is_zero, f"C{power} exact S factor")
    require(quotient.domain == sp.QQ, f"C{power}/S rational")

if os.environ.get("AXIS_CAP_PHASE_TUBE_TEST_DROP_TERM") == "1":
    polynomial = sp.Poly(coefficients[4], S, Z, x, y)
    monomial, coefficient = polynomial.terms()[0]
    deleted = coefficient
    for variable, degree in zip((S, Z, x, y), monomial):
        deleted *= variable**degree
    coefficients[4] = sp.expand(coefficients[4] - deleted)

exact_zero(
    sum(coefficients[power] * lam**power for power in range(5)) - gate36,
    "raw coefficient reconstruction",
)

# Unit-cube tube coordinates: u=8x and y=(2v-1)/64.
tube_map = {
    x: u / 8,
    y: (2 * v - 1) / 64,
    Z: R(63, 64) - u**2 / 64,
}
reserve = sp.factor(1 - tube_map[x]**2 - tube_map[y]**2 - tube_map[Z])
exact_zero(reserve - (R(1, 64) - tube_map[y]**2),
           "tube danger reserve identity")
require(sp.factor(reserve.subs(v, 0)) == R(63, 4096),
        "negative-phase reserve endpoint")
require(sp.factor(reserve.subs(v, 1)) == R(63, 4096),
        "positive-phase reserve endpoint")
require(tube_map[Z].subs(u, 0) == R(63, 64), "Z upper endpoint")
require(tube_map[Z].subs(u, 1) == R(31, 32), "Z lower endpoint")
require(R(31, 32) > 0, "positive Z")

expected_coefficient_data = {
    1: ((0, 1, 2), 6, ((0, 1, 2), R(33605, 6144))),
    2: ((1, 2, 4), 30,
        ((0, 2, 4), R(15241448155, 1358954496))),
    3: ((2, 3, 6), 84,
        ((0, 3, 6), R(49463834927165, 8349416423424))),
    4: ((3, 4, 8), 180,
        ((0, 4, 8), R(1152452992382662513, 307792887033102336))),
}
coefficient_control_count = 0
for power, (degrees, count, minimum) in expected_coefficient_data.items():
    mapped = sp.cancel(coefficients[power] / S).subs(tube_map)
    controls = certify_strict(mapped, (S, u, v), degrees, count, minimum,
                              f"C{power}/S")
    coefficient_control_count += len(controls)
require(coefficient_control_count == 300, "300 coefficient controls")

# Lossless positive-scale compactification tau=lambda/(1+lambda).
compactified = sp.expand(sum(
    coefficients[power].subs(tube_map)
    * tau**power * (1 - tau)**(4 - power)
    for power in range(5)
))
natural_degrees, degrees, full_controls = bernstein_controls(
    compactified, (S, u, v, tau)
)
require(natural_degrees == (4, 4, 8, 4), "compactified natural degrees")
require(degrees == (4, 4, 8, 4), "compactified degrees")
require(len(full_controls) == 1125, "1125 compactified controls")
require(all(value >= 0 for value in full_controls.values()),
        "compactified nonnegative controls")
expected_zeros = {
    (0, u_index, v_index, tau_index)
    for u_index in range(5)
    for v_index in range(9)
    for tau_index in range(1, 5)
}
actual_zeros = {
    index for index, value in full_controls.items() if value == 0
}
require(actual_zeros == expected_zeros,
        "only 180 S=0 closure zeros")
positive_full = [(index, value) for index, value in full_controls.items()
                 if value > 0]
require(len(positive_full) == 945, "945 positive compactified controls")
require(min(positive_full, key=lambda item: item[1])
        == ((1, 4, 8, 1), R(33605, 98304)),
        "least positive compactified control")

# The finite-scale origin and projective infinity.
certify_strict(compactified.subs(tau, 0), (S, u, v), (0, 0, 0), 1,
               ((0, 0, 0), R(5)), "tau=0 face")
tau_one = sp.cancel(compactified.subs(tau, 1) / S)
certify_strict(
    tau_one, (S, u, v), (3, 4, 8), 180,
    ((0, 4, 8), R(1152452992382662513, 307792887033102336)),
    "tau=1 face / S",
)

# The two x endpoints and two signed phase endpoints.  Their only zeros are
# the same artificial S=0 closure, never an original S>0 datum.
face_data = (
    ("x=0", u, 0, (S, v, tau), (4, 8, 4), 225, 36,
     ((1, 8, 3), R(51090800938045, 133590662774784))),
    ("x=1/8", u, 1, (S, v, tau), (4, 8, 4), 225, 36,
     ((1, 8, 1), R(33605, 98304))),
    ("y=-1/64", v, 0, (S, u, tau), (4, 4, 4), 125, 20,
     ((1, 4, 1), R(37445, 98304))),
    ("y=+1/64", v, 1, (S, u, tau), (4, 4, 4), 125, 20,
     ((1, 4, 1), R(33605, 98304))),
)
for label, variable, endpoint, remaining, declared, count, zero_count, minimum in face_data:
    _, face_degrees, face_controls = bernstein_controls(
        compactified.subs(variable, endpoint), remaining, declared
    )
    require(face_degrees == declared, f"{label} declared degrees")
    require(len(face_controls) == count, f"{label} control count")
    require(all(value >= 0 for value in face_controls.values()),
            f"{label} nonnegative controls")
    zeros = {index for index, value in face_controls.items() if value == 0}
    require(len(zeros) == zero_count, f"{label} closure zero count")
    require(all(index[0] == 0 and index[-1] >= 1 for index in zeros),
            f"{label} zeros only at S=0 and positive tau degree")
    positive = [(index, value) for index, value in face_controls.items()
                if value > 0]
    require(min(positive, key=lambda item: item[1]) == minimum,
            f"{label} least positive control")

print(f"PASS nonzero-y raw calibration {raw_value}")
print("PASS reserve >=63/4096, 31/32<=Z<=63/64, det C=(5/9)SZ>0")
print("PASS fully conjugated Hermitian Q,Q^2 quartic and both z signs via Z=z^2")
print("PASS 300/300 strictly positive coefficient tensor controls")
print("PASS 1125 tau controls: 945 positive and 180 S=0 closure zeros")
print("PASS tau=0, tau=1, x endpoints, and y=+-1/64 faces")
print("PASS strict original gate for 0<S<=1 and finite lambda>0 on the tube")
print("scope=source-certified candidate; independent referee pending")

