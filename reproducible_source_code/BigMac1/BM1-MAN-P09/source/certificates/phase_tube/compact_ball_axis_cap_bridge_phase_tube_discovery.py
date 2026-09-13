#!/usr/bin/env python3
"""Exact discovery for a complex-phase tube around the high-Z bridge arc.

This is discovery code only.  It rebuilds the fully conjugated Hermitian
Q,Q^2 gate and reports exact tensor Bernstein data for candidate rational
half-widths in y.  It imports no frozen bridge coefficient table.
"""

if not __debug__:
    raise RuntimeError("fail closed: optimized Python disables discovery")

from itertools import product
from math import comb

import sympy as sp


def require(condition, label):
    if not bool(condition):
        raise RuntimeError(label)


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
    natural = tuple(poly.degree(variable) for variable in variables)
    degrees = natural if declared_degrees is None else declared_degrees
    require(all(a <= b for a, b in zip(natural, degrees)),
            f"bad declared degrees {natural} versus {degrees}")
    power = dict(poly.terms())
    controls = {}
    for index in product(*(range(degree + 1) for degree in degrees)):
        value = sp.Rational(0)
        for monomial in product(*(range(entry + 1) for entry in index)):
            term = power.get(monomial, sp.Rational(0))
            for control, exponent, degree in zip(index, monomial, degrees):
                term *= sp.Rational(comb(control, exponent), comb(degree, exponent))
            value += term
        controls[index] = sp.factor(value)
    return natural, degrees, controls


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
relation = sp.Poly(q**2 - (1 - h**2), q)

j = (1 + 5 * x) / (3 * sp.sqrt(5))
kappa = (-3 + 5 * y) / (3 * sp.sqrt(5))
C = sp.Matrix([
    [h**2, h * (j + I * kappa)],
    [h * (j - I * kappa), j**2 + kappa**2 + R(5, 9) * Z],
])
H = sp.expand(basis * C * basis.conjugate().T)
Q = sp.expand(lam * H)
image = sp.expand(Q * p)
Q2 = sp.expand(Q * Q)
first = c * sp.conjugate(image[0]) + a * image[2] + I * (a * c - Q2[2, 0])
leakage = c * sp.conjugate(image[1]) - I * Q2[2, 1]
raw = reduce_q(sp.expand_complex(
    4 * a**2 * image[1] * sp.conjugate(image[1])
    + first * sp.conjugate(first)
    + leakage * sp.conjugate(leakage)
    - 32 * a**2 * sp.re(image[0])**2
), q, relation)
gate36 = even_h_to_S(36 * raw, h, S)
quartic = sp.Poly(gate36, lam)
require(quartic.degree() == 4 and quartic.nth(0) == 5, "quartic reconstruction")
coefficients = [sp.factor(quartic.nth(power)) for power in range(5)]
for power in range(1, 5):
    quotient, remainder = sp.div(
        sp.Poly(coefficients[power], S, Z, x, y),
        sp.Poly(S, S, Z, x, y),
    )
    require(remainder.is_zero and quotient.domain == sp.QQ, f"C{power}/S")


def test_epsilon(epsilon):
    shape_map = {
        x: u / 8,
        y: epsilon * (2 * v - 1),
        Z: R(63, 64) - u**2 / 64,
    }
    reserve = sp.factor(1 - shape_map[x]**2 - shape_map[y]**2 - shape_map[Z])
    print(f"epsilon={epsilon}; reserve={reserve}; reserve_min={R(1,64)-epsilon**2}")
    quotients = {}
    coefficient_data = []
    for power in range(1, 5):
        quotient = sp.cancel(coefficients[power] / S).subs(shape_map)
        natural, degrees, controls = bernstein_controls(quotient, (S, u, v))
        negative = [(index, value) for index, value in controls.items() if value < 0]
        zero = [(index, value) for index, value in controls.items() if value == 0]
        minimum = min(controls.items(), key=lambda item: item[1])
        print(
            f"C{power}/S natural={natural} controls={len(controls)} "
            f"negative={len(negative)} zero={len(zero)} min={minimum}"
        )
        quotients[power] = quotient
        coefficient_data.append((power, natural, controls, minimum))

    compactified = sp.expand(sum(
        coefficients[power].subs(shape_map)
        * tau**power * (1 - tau)**(4-power)
        for power in range(5)
    ))
    natural, degrees, controls = bernstein_controls(compactified, (S, u, v, tau))
    negative = [(index, value) for index, value in controls.items() if value < 0]
    zero = [(index, value) for index, value in controls.items() if value == 0]
    minimum = min(controls.items(), key=lambda item: item[1])
    print(
        f"tau natural={natural} controls={len(controls)} "
        f"negative={len(negative)} zero={len(zero)} min={minimum}"
    )
    if negative:
        print("tau first_negative", negative[0])
    positive = [(index, value) for index, value in controls.items() if value > 0]
    print(
        f"tau positive={len(positive)} zeros={len(zero)} "
        f"least_positive={min(positive, key=lambda item: item[1])}"
    )
    for label, variable, endpoint, remaining, declared in (
        ("tau=0", tau, 0, (S, u, v), (0, 0, 0)),
        ("x=0", u, 0, (S, v, tau), (4, 8, 4)),
        ("x=1/8", u, 1, (S, v, tau), (4, 8, 4)),
        ("y=-epsilon", v, 0, (S, u, tau), (4, 4, 4)),
        ("y=+epsilon", v, 1, (S, u, tau), (4, 4, 4)),
    ):
        _, _, face = bernstein_controls(
            compactified.subs(variable, endpoint), remaining, declared
        )
        face_positive = [(index, value) for index, value in face.items()
                         if value > 0]
        face_zeros = [(index, value) for index, value in face.items()
                      if value == 0]
        face_negative = [(index, value) for index, value in face.items()
                         if value < 0]
        print(
            f"{label} controls={len(face)} negative={len(face_negative)} "
            f"zero={len(face_zeros)} "
            f"min_positive={min(face_positive, key=lambda item: item[1])}"
        )
    tau_one = sp.cancel(compactified.subs(tau, 1) / S)
    _, _, tau_one_controls = bernstein_controls(tau_one, (S, u, v))
    print(
        f"tau=1/S controls={len(tau_one_controls)} "
        f"min={min(tau_one_controls.items(), key=lambda item: item[1])}"
    )
    return coefficient_data, (natural, controls, minimum)


if __name__ == "__main__":
    raw_point = {
        h: R(3, 5), q: R(4, 5), lam: R(7, 5),
        x: R(1, 16), y: R(1, 128), Z: R(251, 256),
    }
    reduced_point = {
        S: R(9, 25), lam: R(7, 5),
        x: R(1, 16), y: R(1, 128), Z: R(251, 256),
    }
    raw_value = sp.factor(36 * raw.subs(raw_point))
    reduced_value = sp.factor(gate36.subs(reduced_point))
    require(raw_value == reduced_value, "nonzero-y raw/reduced calibration")
    print(f"nonzero-y calibration={raw_value}")
    for epsilon in (R(1, 64), R(1, 128), R(1, 256)):
        test_epsilon(epsilon)
