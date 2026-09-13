#!/usr/bin/env python3
"""Exact low-order (S,X) structure for the unresolved center overlap.

Discovery only.  This script reconstructs the raw compact-ball quartic, uses
the audited moving-sheet recentering, clears denominators, divides only by
the already verified factor S^2, and prints the joint homogeneous layers of
total degree at most three in (S,X).  It deliberately avoids a global
``cancel``/``expand`` after the rational moving-sheet substitution.
"""

if not __debug__:
    raise RuntimeError("do not run this discovery script with python -O")

import sympy as sp
from itertools import product

from compact_ball_adjacent_z_layers_discovery import reconstruct_quartic


MAX_RAW_TOTAL = 5  # after the exact S^2 factor: quotient total degree <= 3


def truncated_add(left, right):
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, 0) + value
    return {key: value for key, value in out.items() if value != 0}


def truncated_mul(left, right):
    out = {}
    for (si, xi), left_value in left.items():
        for (sj, xj), right_value in right.items():
            key = (si + sj, xi + xj)
            if sum(key) <= MAX_RAW_TOTAL:
                out[key] = out.get(key, 0) + left_value * right_value
    return {key: value for key, value in out.items() if value != 0}


def truncated_pow(base, exponent):
    out = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        out = truncated_mul(out, base)
    return out


def centered_box_lower(poly, variables, radii):
    """Constant term minus the exact absolute monomial variation bound."""
    expanded = sp.Poly(sp.expand(poly), *variables, domain=sp.QQ)
    constant = expanded.coeff_monomial((0,) * len(variables))
    variation = sp.Integer(0)
    for powers, coefficient in expanded.terms():
        if not any(powers):
            continue
        variation += abs(coefficient) * sp.prod(
            radius**power for radius, power in zip(radii, powers)
        )
    return sp.factor(constant - variation), sp.factor(constant), sp.factor(variation)


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
    # Y=S*y0 and Z=3X-X^2+S*(w0-3X/5)-S^2*y0^2.
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
        if s_degree + x_degree + y_degree > MAX_RAW_TOTAL:
            continue
        term = {(s_degree, x_degree): coefficient}
        term = truncated_mul(term, truncated_pow(z_map, z_degree))
        term = truncated_mul(term, truncated_pow(y_map, y_degree))
        mapped = truncated_add(mapped, term)

    # A power eight clears every possible denominator in the degree-five
    # truncation (Z has degree at most four and y0 can enter quadratically).
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
        raise AssertionError(("positive denominator clearing failed", symbolic_denominators))
    below = {key: value for key, value in cleared.items() if sum(key) < 2}
    if any(value != 0 for value in below.values()):
        raise AssertionError(("missing exact S^2-scale vanishing", below))
    quotient = {
        (s_degree - 2, x_degree): value
        for (s_degree, x_degree), value in cleared.items()
        if value != 0
        for _ in (None,)
        if s_degree >= 2
    }
    lost = {
        key: value for key, value in cleared.items()
        if value != 0 and key[0] < 2
    }
    if lost:
        # N is divisible by S^2 only after the moving equality substitution;
        # any surviving S-degree <2 is a genuine implementation error.
        raise AssertionError(("not divisible by S^2", lost))
    print("POSITIVE_CLEARING_FACTOR", sp.factor(clearing))
    layers = {}
    for total in range(4):
        layer = sum(
            value * S**s_degree * X**x_degree
            for (s_degree, x_degree), value in quotient.items()
            if s_degree + x_degree == total
        )
        layers[total] = sp.expand(layer)
        print("QUOTIENT_HOMOGENEOUS_LAYER", total, sp.factor(layer))

    h1 = sp.factor(layers[1] / S)
    print("H1_S_COEFFICIENT", h1)
    if sp.simplify(h1.subs(M, 0)) != 0:
        raise AssertionError("expected sharp M=0 degeneration")

    h2 = sp.Poly(layers[2], S, X)
    coefficients = {
        "SS": sp.factor(h2.coeff_monomial(S**2)),
        "SX": sp.factor(h2.coeff_monomial(S * X)),
        "XX": sp.factor(h2.coeff_monomial(X**2)),
    }
    if sp.expand(layers[2] - sum((
        coefficients["SS"] * S**2,
        coefficients["SX"] * S * X,
        coefficients["XX"] * X**2,
    ))) != 0:
        raise AssertionError("H2 is not quadratic in S,X")
    variables = (M, omega, nu)
    radii = (R(1, 1000), R(1, 100), R(1, 100))
    for name, coefficient in coefficients.items():
        lower, constant, variation = centered_box_lower(
            coefficient, variables, radii
        )
        print("H2_COEFFICIENT", name, coefficient)
        print("H2_INTERVAL", name, "constant", constant,
              "variation", variation, "lower", lower)
        if lower <= 0:
            raise AssertionError(("nonpositive exact coefficient bound", name, lower))

    node_values = []
    for values in product(*[(-radius, R(0), radius) for radius in radii]):
        substitution = dict(zip(variables, values))
        for name, coefficient in coefficients.items():
            node_values.append((name, values, sp.factor(coefficient.subs(substitution))))
    negative = [item for item in node_values if item[2] < 0]
    print("H2_EXACT_NODE_COUNT", len(node_values))
    print("H2_EXACT_NODE_NEGATIVE", len(negative))
    print("H2_EXACT_NODE_MINIMUM", min(node_values, key=lambda item: item[2]))
    print("PROJECTIVE_SCALE", "X=S*rho on X<=S; S=X*sigma on S<=X")
    print("PROJECTIVE_OVERLAP", "rho=sigma=1")


if __name__ == "__main__":
    main()
