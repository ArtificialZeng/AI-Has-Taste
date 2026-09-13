#!/usr/bin/env python3
"""First exact centered chart around the moving S=0 equality sheet.

This is a bounded local discovery certificate, not a full collar proof.  It
first checks exact divisibility by S^2 X^2 before mapping X away from zero.
"""

if not __debug__:
    raise RuntimeError("do not run this discovery script with python -O")

from itertools import product
from math import prod

import sympy as sp

from compact_ball_adjacent_z_layers_discovery import (
    bernstein_controls,
    reconstruct_quartic,
)


def main():
    R = sp.Rational
    quartic, (S, Z, x, y), lam = reconstruct_quartic()
    mu, X, Y, M = sp.symbols("mu X Y M", real=True)
    omega, nu = sp.symbols("omega nu", real=True)
    s, xi, m, o, n = sp.symbols("s xi m o n", real=True)

    gate = sp.cancel(quartic.as_expr().subs(lam, mu / S))
    N = sp.expand((S**3 * gate).subs({
        x: -R(1, 5) + X,
        y: R(3, 5) + Y,
        mu: 1 + M,
    }))

    wc = -3 * (5 * M * X - 15 * M + 5 * X - 6) / (25 * (1 + M))
    vc = R(12, 25) / (1 + M)
    Y_map = S * (vc + nu)
    W_map = S * (wc + omega)
    Z_map = 3 * X - X**2 - Y_map**2 + W_map
    centered = sp.factor(N.subs({Y: Y_map, Z: Z_map}))
    numerator, denominator = sp.fraction(sp.cancel(centered))
    print("CLEARING_DENOMINATOR", sp.factor(denominator))
    cleared = sp.expand(numerator)

    scale_quotient = sp.cancel(cleared / S**2)
    scale_numerator, scale_denominator = sp.fraction(scale_quotient)
    if scale_denominator.free_symbols:
        raise AssertionError(("not divisible by S^2", scale_denominator))
    print("S2_DIVISIBILITY", "PASS", sp.factor(scale_denominator))
    # X^2 is not a global polynomial factor.  On this main chart X>0, so the
    # rational division is lossless; its mapped denominator is audited
    # separately and no conclusion is extended to X=0.
    quotient = sp.cancel(scale_quotient / X**2)

    mapping = {
        S: s / 10000,
        X: R(1, 4000) + R(1, 20000) * xi,
        M: -R(1, 1000) + R(1, 500) * m,
        omega: -R(1, 100) + R(1, 50) * o,
        nu: -R(1, 100) + R(1, 50) * n,
    }
    mapped_rational = sp.cancel(quotient.subs(mapping))
    mapped_numerator, mapped_denominator = sp.fraction(mapped_rational)
    mapped = sp.expand(mapped_numerator)
    _, _, denominator_controls = bernstein_controls(
        sp.expand(mapped_denominator), (xi,)
    )
    if any(value <= 0 for value in denominator_controls.values()):
        raise AssertionError(("mapped X denominator", mapped_denominator))
    print("MAPPED_POSITIVE_DENOMINATOR", sp.factor(mapped_denominator))
    polynomial = sp.Poly(mapped, s, xi, m, o, n, domain=sp.QQ)
    degrees = [polynomial.degree(variable) for variable in (s, xi, m, o, n)]
    predicted = prod(degree + 1 for degree in degrees)
    print("PREDICTED_DEGREES", degrees)
    print("PREDICTED_CONTROLS", predicted)
    if predicted > 100000:
        print("STATUS", "RESOURCE_LIMIT_BEFORE_TENSOR")
        return

    natural, actual_degrees, controls = bernstein_controls(
        mapped, (s, xi, m, o, n)
    )
    if natural != degrees or actual_degrees != degrees or len(controls) != predicted:
        raise AssertionError("control accounting mismatch")
    negative = [item for item in controls.items() if item[1] < 0]
    zeros = [item for item in controls.items() if item[1] == 0]
    positive = [item for item in controls.items() if item[1] > 0]
    print("NEGATIVE", len(negative))
    print("ZEROS", len(zeros))
    print("FIRST_NEGATIVE", negative[0] if negative else None)
    print("MINIMUM", min(controls.items(), key=lambda item: item[1]))
    print("MINIMUM_POSITIVE", min(positive, key=lambda item: item[1]))
    print("MAIN_STATUS", "PASS" if not negative else "CERTIFICATE_FAILURE_ONLY")

    # Separate center overlap: X may vanish, so divide only by S^2 and never
    # by X^2.  The other local coordinates and scale range are unchanged.
    center_mapping = dict(mapping)
    center_mapping[X] = R(1, 4000) * xi
    center_rational = sp.cancel(scale_quotient.subs(center_mapping))
    center_numerator, center_denominator = sp.fraction(center_rational)
    _, _, center_denominator_controls = bernstein_controls(
        sp.expand(center_denominator), (xi,)
    )
    if any(value <= 0 for value in center_denominator_controls.values()):
        raise AssertionError(("center denominator", center_denominator))
    center_expression = sp.expand(center_numerator)
    center_poly = sp.Poly(center_expression, s, xi, m, o, n, domain=sp.QQ)
    center_degrees = [
        center_poly.degree(variable) for variable in (s, xi, m, o, n)
    ]
    center_predicted = prod(degree + 1 for degree in center_degrees)
    print("CENTER_POSITIVE_DENOMINATOR", sp.factor(center_denominator))
    print("CENTER_PREDICTED_DEGREES", center_degrees)
    print("CENTER_PREDICTED_CONTROLS", center_predicted)
    if center_predicted > 100000:
        print("CENTER_STATUS", "RESOURCE_LIMIT_BEFORE_TENSOR")
        return
    _, verified_degrees, center_controls = bernstein_controls(
        center_expression, (s, xi, m, o, n)
    )
    if verified_degrees != center_degrees or len(center_controls) != center_predicted:
        raise AssertionError("center control accounting mismatch")
    center_negative = [item for item in center_controls.items() if item[1] < 0]
    center_zeros = [item for item in center_controls.items() if item[1] == 0]
    center_positive = [item for item in center_controls.items() if item[1] > 0]
    print("CENTER_NEGATIVE", len(center_negative))
    print("CENTER_ZEROS", len(center_zeros))
    print("CENTER_FIRST_NEGATIVE", center_negative[0] if center_negative else None)
    print("CENTER_MINIMUM", min(center_controls.items(), key=lambda item: item[1]))
    print("CENTER_MINIMUM_POSITIVE", min(center_positive, key=lambda item: item[1]))
    print("CENTER_STATUS", "PASS" if not center_negative else "CERTIFICATE_FAILURE_ONLY")
    center_x0 = sp.factor(scale_quotient.subs(X, 0))
    print("CENTER_X0_FACTORED", center_x0)
    center_x0_poly = sp.Poly(sp.expand(center_x0), S)
    center_coefficients = []
    for degree in range(center_x0_poly.degree() + 1):
        coefficient = sp.factor(center_x0_poly.nth(degree))
        center_coefficients.append(coefficient)
        print(
            "CENTER_X0_S_COEFFICIENT", degree,
            coefficient,
        )

    node_values = []
    for S_value, M_value, omega_value, nu_value in product(
        (R(0), R(1, 20000), R(1, 10000)),
        (-R(1, 1000), R(0), R(1, 1000)),
        (-R(1, 100), R(0), R(1, 100)),
        (-R(1, 100), R(0), R(1, 100)),
    ):
        value = sp.factor(center_x0.subs({
            S: S_value,
            M: M_value,
            omega: omega_value,
            nu: nu_value,
        }))
        node_values.append(((S_value, M_value, omega_value, nu_value), value))
    node_negative = [item for item in node_values if item[1] < 0]
    print("CENTER_X0_EXACT_NODES", len(node_values))
    print("CENTER_X0_NODE_NEGATIVE", len(node_negative))
    print("CENTER_X0_NODE_MINIMUM", min(node_values, key=lambda item: item[1]))

    coefficient_mapping = {
        M: -R(1, 1000) + R(1, 500) * m,
        omega: -R(1, 100) + R(1, 50) * o,
        nu: -R(1, 100) + R(1, 50) * n,
    }
    coefficient_minima = {}
    coefficient_counts = 0
    for degree in range(2, 6):
        mapped_coefficient = sp.expand(center_coefficients[degree].subs(
            coefficient_mapping
        ))
        _, coefficient_degrees, coefficient_controls = bernstein_controls(
            mapped_coefficient, (m, o, n)
        )
        minimum = min(coefficient_controls.items(), key=lambda item: item[1])
        coefficient_minima[degree] = minimum[1]
        coefficient_counts += len(coefficient_controls)
        print(
            "CENTER_COEFFICIENT", degree,
            "degrees", coefficient_degrees,
            "controls", len(coefficient_controls),
            "minimum", minimum,
        )
    scale_max = R(1, 10000)
    bracket_lower = coefficient_minima[2]
    for degree in range(3, 6):
        bracket_lower += scale_max**(degree - 2) * min(
            R(0), coefficient_minima[degree]
        )
    print("CENTER_COEFFICIENT_CONTROLS", coefficient_counts)
    print("CENTER_BRACKET_LOWER", sp.factor(bracket_lower))
    print(
        "CENTER_ANALYTIC_STATUS",
        "PASS" if bracket_lower > 0 and not node_negative else "FAIL",
    )


if __name__ == "__main__":
    main()
