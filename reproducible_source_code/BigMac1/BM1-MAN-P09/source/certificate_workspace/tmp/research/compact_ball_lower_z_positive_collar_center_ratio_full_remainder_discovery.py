#!/usr/bin/env python3
"""Exact coefficientwise full-remainder test on the two center ratio charts.

This is a low-memory discovery certificate.  It reconstructs the raw gate,
performs the full moving-sheet substitution sparsely, clears one known
strictly positive denominator, removes the exact nonnegative H1 layer, and
bounds every higher homogeneous layer coefficientwise.  No sampled values or
large Bernstein tensor are used.
"""

if not __debug__:
    raise RuntimeError("do not run this discovery script with python -O")

import sympy as sp

from compact_ball_adjacent_z_layers_discovery import reconstruct_quartic


def sparse_add(left, right):
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, 0) + value
    return {key: value for key, value in out.items() if value != 0}


def sparse_mul(left, right):
    out = {}
    for (si, xi), left_value in left.items():
        for (sj, xj), right_value in right.items():
            key = (si + sj, xi + xj)
            out[key] = out.get(key, 0) + left_value * right_value
    return {key: value for key, value in out.items() if value != 0}


def sparse_pow(base, exponent):
    out = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        out = sparse_mul(out, base)
    return out


def parameter_poly(poly, variables):
    return sp.Poly(sp.expand(poly), *variables, domain=sp.QQ)


def centered_box_abs(poly, variables, radii):
    expanded = parameter_poly(poly, variables)
    bound = sp.Integer(0)
    for powers, coefficient in expanded.terms():
        bound += abs(coefficient) * sp.prod(
            radius**power for radius, power in zip(radii, powers)
        )
    return sp.factor(bound), len(expanded.terms())


def centered_box_lower(poly, variables, radii):
    expanded = parameter_poly(poly, variables)
    constant = expanded.coeff_monomial((0,) * len(variables))
    variation = sp.Integer(0)
    for powers, coefficient in expanded.terms():
        if not any(powers):
            continue
        variation += abs(coefficient) * sp.prod(
            radius**power for radius, power in zip(radii, powers)
        )
    return sp.factor(constant - variation)


def main():
    R = sp.Rational
    quartic, (S, Z, x, y), lam = reconstruct_quartic()
    mu, X, Y, M = sp.symbols("mu X Y M", real=True)
    omega, nu = sp.symbols("omega nu", real=True)

    gate = sp.cancel(quartic.as_expr().subs(lam, mu / S))
    N = sp.expand((S**3 * gate).subs({
        x: -R(1, 5) + X,
        y: R(3, 5) + Y,
        mu: 1 + M,
    }))
    A = 1 + M
    positive_denominator = 25 * A
    y0 = (12 + 25 * A * nu) / positive_denominator
    w0 = (45 * M + 18 + 25 * A * omega) / positive_denominator
    y_map = {(1, 0): y0}
    z_map = {
        (0, 1): R(3),
        (0, 2): -R(1),
        (1, 0): w0,
        (1, 1): -R(3, 5),
        (2, 0): -y0**2,
    }

    raw_poly = sp.Poly(N, S, Z, X, Y)
    print("RAW_MONOMIALS", len(raw_poly.terms()))
    mapped = {}
    for (s_degree, z_degree, x_degree, y_degree), coefficient in raw_poly.terms():
        term = {(s_degree, x_degree): coefficient}
        term = sparse_mul(term, sparse_pow(z_map, z_degree))
        term = sparse_mul(term, sparse_pow(y_map, y_degree))
        mapped = sparse_add(mapped, term)

    clearing = positive_denominator**8
    cleared = {
        key: sp.factor(sp.cancel(value * clearing))
        for key, value in mapped.items()
    }
    symbolic_denominators = {
        sp.factor(sp.denom(value)) for value in cleared.values()
        if sp.denom(value).free_symbols
    }
    if symbolic_denominators:
        raise AssertionError(("positive clearing failed", symbolic_denominators))
    lost = {
        key: value for key, value in cleared.items()
        if value != 0 and key[0] < 2
    }
    if lost:
        raise AssertionError(("moving chart is not divisible by S^2", lost))
    quotient = {
        (s_degree - 2, x_degree): value
        for (s_degree, x_degree), value in cleared.items()
        if value != 0
    }
    print("POSITIVE_CLEARING_FACTOR", sp.factor(clearing))
    print("QUOTIENT_SX_MONOMIALS", len(quotient))
    print("QUOTIENT_BIDEGREE", max(i for i, _ in quotient),
          max(j for _, j in quotient))

    h1 = quotient.get((1, 0), 0)
    expected_h1 = (
        R(152587890625) * M**2 * A**8 * (5 * M**2 + 14 * M + 14)
    )
    if sp.expand(h1 - expected_h1) != 0:
        raise AssertionError("H1 mismatch")
    rest = dict(quotient)
    del rest[(1, 0)]
    if any(i + j < 2 for i, j in rest):
        raise AssertionError("unexpected lower layer after H1 removal")
    print("H1_NONNEGATIVE", sp.factor(h1))

    variables = (M, omega, nu)
    radii = (R(1, 1000), R(1, 100), R(1, 100))
    h2_coefficients = {
        "SS": rest[(2, 0)],
        "SX": rest[(1, 1)],
        "XX": rest[(0, 2)],
    }
    h2_lowers = {
        name: centered_box_lower(value, variables, radii)
        for name, value in h2_coefficients.items()
    }
    if any(value <= 0 for value in h2_lowers.values()):
        raise AssertionError(("H2 reserve failed", h2_lowers))
    reserve = min(h2_lowers.values())
    print("H2_LOWERS", h2_lowers)
    print("H2_COMMON_RESERVE", reserve)

    layer_bounds = {}
    parameter_term_count = 0
    layer_sx_counts = {}
    for (s_degree, x_degree), coefficient in rest.items():
        total = s_degree + x_degree
        if total <= 2:
            continue
        bound, terms = centered_box_abs(coefficient, variables, radii)
        layer_bounds[total - 2] = layer_bounds.get(total - 2, 0) + bound
        layer_sx_counts[total - 2] = layer_sx_counts.get(total - 2, 0) + 1
        parameter_term_count += terms
    if parameter_term_count > 2000:
        print("STATUS", "RESOURCE_CAP_BEFORE_REMAINDER")
        print("PARAMETER_MONOMIAL_COUNT", parameter_term_count)
        return
    print("PARAMETER_MONOMIAL_COUNT", parameter_term_count)
    for degree in sorted(layer_bounds):
        print("REMAINDER_LAYER", degree,
              "SX_TERMS", layer_sx_counts[degree],
              "ABS_BOUND", sp.factor(layer_bounds[degree]))

    for chart, radius in (
        ("C0", R(1, 10000)),
        ("C1", R(1, 4000)),
        ("C1_EXTENDED", R(3, 10000)),
    ):
        remainder = sum(
            bound * radius**degree
            for degree, bound in layer_bounds.items()
        )
        margin = sp.factor(reserve - remainder)
        print(chart, "RADIUS", radius)
        print(chart, "REMAINDER_BOUND", sp.factor(remainder))
        print(chart, "MARGIN", margin)
        print(chart, "STATUS", "PASS" if margin > 0 else "BOUND_FAILURE_ONLY")

    print("COVER_C0", "X=S*rho, 0<=rho<=1, includes X=0")
    print("COVER_C1", "S=X*sigma, 0<=sigma<=1")
    print("COVER_PROJECTIVE_OVERLAP", "X=S, rho=sigma=1")
    print("COVER_MAIN_OVERLAP", "X=1/4000")


if __name__ == "__main__":
    main()
