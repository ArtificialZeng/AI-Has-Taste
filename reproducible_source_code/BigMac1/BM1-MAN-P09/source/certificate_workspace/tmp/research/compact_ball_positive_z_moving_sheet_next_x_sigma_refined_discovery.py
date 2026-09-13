#!/usr/bin/env python3
"""Exact sigma-sensitive discovery test on 1/31 <= X <= 1/30.

This script rebuilds the fully conjugated Hermitian ``Q,Q^2`` gate, performs
the rational moving-sheet substitution sparsely, and keeps the exact power of
``sigma=S/X`` in every remainder term.  It is discovery code; a theorem
verifier must freeze every decisive rational value.
"""

if not __debug__:
    raise RuntimeError("do not run this discovery script with python -O")

from itertools import product

import sympy as sp

from compact_ball_adjacent_z_layers_discovery import reconstruct_quartic


def sparse_add(left, right):
    out = dict(left)
    for key, value in right.items():
        out[key] = out.get(key, 0) + value
    return {key: value for key, value in out.items() if value != 0}


def sparse_mul(left, right):
    out = {}
    for (si, xi), lv in left.items():
        for (sj, xj), rv in right.items():
            key = (si + sj, xi + xj)
            out[key] = out.get(key, 0) + lv * rv
    return {key: value for key, value in out.items() if value != 0}


def sparse_pow(base, exponent):
    out = {(0, 0): sp.Integer(1)}
    for _ in range(exponent):
        out = sparse_mul(out, base)
    return out


def centered_box_abs(poly, variables, radii):
    expanded = sp.Poly(sp.expand(poly), *variables, domain=sp.QQ)
    bound = sp.Integer(0)
    for powers, coefficient in expanded.terms():
        bound += abs(coefficient) * sp.prod(
            radius**power for radius, power in zip(radii, powers)
        )
    return sp.factor(bound), len(expanded.terms())


def centered_box_lower(poly, variables, radii):
    expanded = sp.Poly(sp.expand(poly), *variables, domain=sp.QQ)
    constant = expanded.coeff_monomial((0,) * len(variables))
    variation = sp.Integer(0)
    for powers, coefficient in expanded.terms():
        if any(powers):
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
    denominator = 25 * A
    y0 = (12 + 25 * A * nu) / denominator
    w0 = (45 * M + 18 + 25 * A * omega) / denominator
    ymap = {(1, 0): y0}
    zmap = {
        (0, 1): R(3),
        (0, 2): -R(1),
        (1, 0): w0,
        (1, 1): -R(3, 5),
        (2, 0): -y0**2,
    }

    mapped = {}
    for (si, zi, xi, yi), coefficient in sp.Poly(N, S, Z, X, Y).terms():
        term = {(si, xi): coefficient}
        term = sparse_mul(term, sparse_pow(zmap, zi))
        term = sparse_mul(term, sparse_pow(ymap, yi))
        mapped = sparse_add(mapped, term)
    cleared = {
        key: sp.factor(sp.cancel(value * denominator**8))
        for key, value in mapped.items()
    }
    if any(value != 0 and key[0] < 2 for key, value in cleared.items()):
        raise AssertionError("missing exact S^2 factor")
    quotient = {
        (si - 2, xi): value
        for (si, xi), value in cleared.items() if value != 0
    }
    if len(quotient) != 20:
        raise AssertionError(("quotient support", len(quotient)))

    h1 = quotient.pop((1, 0))
    expected_h1 = R(152587890625) * M**2 * A**8 * (
        5 * M**2 + 14 * M + 14
    )
    if sp.expand(h1 - expected_h1) != 0:
        raise AssertionError("H1 mismatch")

    variables = (M, omega, nu)
    radii = (R(1, 1000), R(1, 100), R(1, 100))
    h2_lowers = {
        key: centered_box_lower(quotient[key], variables, radii)
        for key in ((2, 0), (1, 1), (0, 2))
    }
    if any(value <= 0 for value in h2_lowers.values()):
        raise AssertionError(("H2", h2_lowers))

    xmin = R(1, 31)
    xmax = R(1, 30)
    smax = R(1, 10000)
    sigmamax = sp.factor(smax / xmin)
    if sigmamax != R(31, 10000):
        raise AssertionError(sigmamax)

    # After S=sigma*X and division by X^2, the positive H2 lower bound can
    # retain all three positive terms.  Each higher term retains sigma^si.
    h2_reserve = sp.factor(
        h2_lowers[(0, 2)]
        + h2_lowers[(1, 1)] * sigmamax
        + h2_lowers[(2, 0)] * sigmamax**2
    )
    # For a uniform lower bound the positive sigma terms are optional; the
    # certifier will use the smaller c-only reserve, which remains valid at
    # the S->0 closure.
    closure_reserve = h2_lowers[(0, 2)]

    remainder = sp.Integer(0)
    term_count = 0
    parameter_monomials = 0
    detailed = []
    for (si, xi), coefficient in sorted(quotient.items()):
        total = si + xi
        if total <= 2:
            continue
        bound, count = centered_box_abs(coefficient, variables, radii)
        contribution = sp.factor(
            bound * sigmamax**si * xmax**(total - 2)
        )
        remainder += contribution
        term_count += 1
        parameter_monomials += count
        detailed.append(((si, xi), bound, contribution))
    remainder = sp.factor(remainder)
    margin = sp.factor(closure_reserve - remainder)

    print("RAW_QUARTIC_DEGREE", quartic.degree())
    print("QUOTIENT_SUPPORT", len(quotient) + 1)
    print("SIGMA_MAX", sigmamax)
    print("H2_LOWERS", h2_lowers)
    print("H2_FULL_ENDPOINT_RESERVE", h2_reserve)
    print("H2_CLOSURE_RESERVE", closure_reserve)
    print("REMAINDER_SX_TERMS", term_count)
    print("PARAMETER_MONOMIALS", parameter_monomials)
    print("SIGMA_SENSITIVE_REMAINDER", remainder)
    print("SIGMA_SENSITIVE_MARGIN", margin)
    print("MIN_CONTRIBUTION", min(detailed, key=lambda item: item[2]))
    print("MAX_CONTRIBUTION", max(detailed, key=lambda item: item[2]))
    print("STATUS", "PASS" if margin > 0 else "BOUND_FAILURE_ONLY")

    # Symmetric falsification route: exact rational nodes of the original
    # quartic, including both X endpoints and a midpoint.  This is not used
    # in the continuum proof and is not promoted beyond a finite search.
    xmid = sp.factor((xmin + xmax) / 2)
    direct_records = []
    for sv, xv, mv, ov, nv in product(
        (R(1, 1000000), R(1, 20000), smax),
        (xmin, xmid, xmax),
        (-R(1, 1000), R(1, 1000)),
        (-R(1, 100), R(1, 100)),
        (-R(1, 100), R(1, 100)),
    ):
        substitutions = {S: sv, X: xv, M: mv, omega: ov, nu: nv}
        yv = sp.factor((S * y0).subs(substitutions))
        zv = sp.factor((
            3 * X - X**2 + S * w0 - S**2 * y0**2
        ).subs(substitutions))
        xv_raw = -R(1, 5) + xv
        yv_raw = R(3, 5) + yv
        lv = sp.factor((1 + mv) / sv)
        danger = sp.factor(1 - xv_raw**2 - yv_raw**2 - zv)
        determinant = sp.factor(R(5, 9) * sv * zv)
        if not (lv > 0 and 0 < zv < R(1, 8) and danger > 0 and determinant > 0):
            raise AssertionError(("illegal direct node", substitutions))
        value = sp.factor(quartic.as_expr().subs({
            S: sv, Z: zv, x: xv_raw, y: yv_raw, lam: lv,
        }))
        direct_records.append(((sv, xv, mv, ov, nv), value))
    direct_negatives = [item for item in direct_records if item[1] < 0]
    print("DIRECT_EXACT_LEGAL_NODES", len(direct_records))
    print("DIRECT_EXACT_NEGATIVE_NODES", len(direct_negatives))
    print("DIRECT_EXACT_MINIMUM", min(direct_records, key=lambda item: item[1]))
    print("DIRECT_SCOPE", "finite falsification audit only")
    if direct_negatives:
        raise AssertionError(("exact legal negative candidate", direct_negatives[0]))


if __name__ == "__main__":
    main()
