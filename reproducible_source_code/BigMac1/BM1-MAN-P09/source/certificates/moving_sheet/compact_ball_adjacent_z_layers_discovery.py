#!/usr/bin/env python3
"""Exact exploratory Bernstein data for the adjacent compact-ball Z layers.

This is discovery code only.  A theorem verifier must hard-code every claimed
minimum and reconstruct the Hermitian gate independently.
"""

if not __debug__:
    raise RuntimeError("do not run this discovery script with python -O")

from itertools import product
from math import comb

import sympy as sp


def zero(expression, label):
    if isinstance(expression, sp.MatrixBase):
        for entry in expression:
            zero(entry, label)
        return
    value = sp.factor(sp.cancel(sp.together(sp.expand_complex(expression))))
    if value != 0:
        raise AssertionError(f"{label}: {value}")


def bernstein_controls(polynomial, variables, degrees=None):
    poly = sp.Poly(sp.expand(polynomial), *variables, domain=sp.QQ)
    natural = [poly.degree(variable) for variable in variables]
    if degrees is None:
        degrees = natural
    if any(target < source for source, target in zip(natural, degrees)):
        raise ValueError((natural, degrees))
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


def elevate_one_axis(controls, degrees, axis):
    """Raise one tensor Bernstein degree by one using the exact recurrence."""
    old_degree = degrees[axis]
    new_degrees = list(degrees)
    new_degrees[axis] += 1
    elevated = {}
    for index in product(*(range(degree + 1) for degree in new_degrees)):
        position = index[axis]
        value = sp.Rational(0)
        if position > 0:
            old_index = list(index)
            old_index[axis] = position - 1
            value += sp.Rational(position, old_degree + 1) * controls[tuple(old_index)]
        if position <= old_degree:
            old_index = list(index)
            old_index[axis] = position
            value += sp.Rational(old_degree + 1 - position, old_degree + 1) * controls[tuple(old_index)]
        elevated[index] = sp.factor(value)
    return new_degrees, elevated


def elevate_tensor(controls, degrees, target_degrees):
    degrees = list(degrees)
    while degrees != list(target_degrees):
        axis = next(
            index for index, (degree, target) in enumerate(zip(degrees, target_degrees))
            if degree < target
        )
        degrees, controls = elevate_one_axis(controls, degrees, axis)
    return controls


def elevate_univariate(values):
    old_degree = len(values) - 1
    elevated = []
    for position in range(old_degree + 2):
        value = sp.Rational(0)
        if position > 0:
            value += sp.Rational(position, old_degree + 1) * values[position - 1]
        if position <= old_degree:
            value += sp.Rational(old_degree + 1 - position, old_degree + 1) * values[position]
        elevated.append(sp.factor(value))
    return elevated


def reconstruct_quartic():
    I = sp.I
    R = sp.Rational
    h, q, lam = sp.symbols("h q lambda", real=True)
    S, Z, x, y = sp.symbols("S Z x y", real=True)
    a = 1 / sp.sqrt(6)
    c = sp.sqrt(R(5, 6))
    zeta = R(4, 5) + I * R(3, 5)
    p = sp.Matrix([a, 0, c])
    rvec = sp.Matrix([-a, 0, c * zeta])
    fvec = sp.Matrix([-c * h, q, -a * h * zeta])
    basis = sp.Matrix.hstack(rvec, fvec)
    relation = sp.Poly(q**2 - (1 - h**2), q)
    j = (1 + 5 * x) / (3 * sp.sqrt(5))
    k = (-3 + 5 * y) / (3 * sp.sqrt(5))
    W = j**2 + k**2 + R(5, 9) * Z
    compression = sp.Matrix([[h**2, h * (j + I * k)],
                             [h * (j - I * k), W]])
    H = sp.expand(basis * compression * basis.conjugate().T)
    Q = sp.expand(lam * H)
    image = sp.expand(Q * p)
    Q2 = sp.expand(Q * Q)
    first = c * sp.conjugate(image[0]) + a * image[2] + I * (a * c - Q2[2, 0])
    leakage = c * sp.conjugate(image[1]) - I * Q2[2, 1]
    raw_gate = sp.expand_complex(
        4 * a**2 * image[1] * sp.conjugate(image[1])
        + first * sp.conjugate(first)
        + leakage * sp.conjugate(leakage)
        - 32 * a**2 * sp.re(image[0])**2
    )
    raw_gate = sp.expand(sp.rem(sp.Poly(raw_gate, q), relation).as_expr())
    transformed = sp.expand(
        (36 * raw_gate).subs(h**8, S**4).subs(h**6, S**3)
        .subs(h**4, S**2).subs(h**2, S)
    )
    if transformed.has(h) or transformed.has(q):
        raise AssertionError("unresolved radical")
    quartic = sp.Poly(transformed, lam)
    zero(quartic.nth(0) - 5, "constant coefficient")
    return quartic, (S, Z, x, y), lam


def main():
    R = sp.Rational
    quartic, (S, Z, x, y), lam = reconstruct_quartic()
    u, v, w, t, tau = sp.symbols("u v w t tau", real=True)

    def mapped_coefficient(power, left, right):
        return sp.expand(sp.cancel(quartic.nth(power) / S).subs({
            S: u,
            Z: left + (right - left) * v,
            x: R(1, 8) + w / 8,
            y: (2 * t - 1) / 8,
        }))

    intervals = [
        ("lower", R(1, 8), R(3, 16)),
        ("upper", R(5, 16), R(3, 8)),
        ("central-plus-upper", R(3, 16), R(3, 8)),
    ]
    for name, left, right in intervals:
        print(name, left, right)
        for power in range(1, 5):
            natural, degrees, controls = bernstein_controls(
                mapped_coefficient(power, left, right), (u, v, w, t)
            )
            nonpositive = [item for item in controls.items() if item[1] <= 0]
            print(
                power, natural, len(controls),
                "first_nonpositive=", nonpositive[0] if nonpositive else None,
                "minimum=", min(controls.items(), key=lambda item: item[1]),
            )

    corner = {S: u, Z: R(1, 8), x: R(1, 4), y: R(1, 8)}
    compactified_corner = sp.expand(
        sum(quartic.nth(power).subs(corner) * tau**power
            * (1 - tau)**(4 - power) for power in range(5))
    )
    print("lower_bad_corner_compactified=", sp.factor(compactified_corner))
    for tau_degree in [4, 5, 6, 8, 12, 16, 24, 32, 48, 64]:
        natural, degrees, controls = bernstein_controls(
            compactified_corner, (u, tau), (4, tau_degree)
        )
        nonpositive = [item for item in controls.items() if item[1] <= 0]
        print(
            "corner", degrees, "first_nonpositive=",
            nonpositive[0] if nonpositive else None,
            "minimum=", min(controls.items(), key=lambda item: item[1]),
        )

    # Lossless all-scale test on the entire lower shape layer.  First put
    # every lambda coefficient into a common four-shape Bernstein degree,
    # then use the exact compactification lambda=tau/(1-tau).
    target_shape_degrees = [4, 4, 8, 8]
    shape_controls = []
    for power in range(5):
        mapped = sp.Integer(5) if power == 0 else u * mapped_coefficient(
            power, R(1, 8), R(3, 16)
        )
        natural, degrees, controls = bernstein_controls(mapped, (u, v, w, t))
        shape_controls.append(
            elevate_tensor(controls, degrees, target_shape_degrees)
        )
        print("lower full coefficient", power, natural, "to", target_shape_degrees)

    tau_controls = {
        index: [shape_controls[power][index] / comb(4, power)
                for power in range(5)]
        for index in product(*(range(degree + 1) for degree in target_shape_degrees))
    }
    for tau_degree in [4, 5]:
        while len(next(iter(tau_controls.values()))) - 1 < tau_degree:
            for index in tau_controls:
                tau_controls[index] = elevate_univariate(tau_controls[index])
        all_controls = [
            (shape_index + (tau_index,), value)
            for shape_index, values in tau_controls.items()
            for tau_index, value in enumerate(values)
        ]
        nonpositive = [item for item in all_controls if item[1] <= 0]
        positive = [item for item in all_controls if item[1] > 0]
        zeros = [item for item in all_controls if item[1] == 0]
        print(
            "lower full tau degree", len(next(iter(tau_controls.values()))) - 1,
            "first_nonpositive=", nonpositive[0] if nonpositive else None,
            "minimum=", min(all_controls, key=lambda item: item[1]),
            "negative_count=", len([value for _, value in all_controls if value < 0]),
            "zero_count=", len(zeros),
            "minimum_positive=", min(positive, key=lambda item: item[1]),
        )
        if tau_degree == 5:
            expected_zeros = {
                (0, z_index, x_index, y_index, tau_index)
                for z_index in range(5)
                for x_index in range(9)
                for y_index in range(9)
                for tau_index in range(2, 6)
            }
            actual_zeros = {index for index, _ in zeros}
            print("degree5_zero_pattern_exact=", actual_zeros == expected_zeros)


if __name__ == "__main__":
    main()
