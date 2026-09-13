#!/usr/bin/env python3
"""Exact reciprocal-endpoint envelope discovery beyond X=1/30.

The script rebuilds the fully conjugated raw quartic, retains every power of
sigma=S/X, and classifies each requested reciprocal endpoint by the exact
remainder, Z cap, danger, and rank-two legality tests.  Negative sufficient
bounds are never reported as negative gates.
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
    h1 = quotient.pop((1, 0))
    expected_h1 = R(152587890625) * M**2 * A**8 * (
        5 * M**2 + 14 * M + 14
    )
    if sp.expand(h1 - expected_h1) != 0:
        raise AssertionError("H1 mismatch")

    variables = (M, omega, nu)
    mradius = R(1, 1000)
    tradius = R(1, 100)
    radii = (mradius, tradius, tradius)
    h2_lowers = {
        key: centered_box_lower(quotient[key], variables, radii)
        for key in ((2, 0), (1, 1), (0, 2))
    }
    if any(value <= 0 for value in h2_lowers.values()):
        raise AssertionError(("H2", h2_lowers))
    closure_reserve = h2_lowers[(0, 2)]

    higher = []
    parameter_monomials = 0
    for (si, xi), coefficient in sorted(quotient.items()):
        total = si + xi
        if total <= 2:
            continue
        bound, count = centered_box_abs(coefficient, variables, radii)
        higher.append((si, xi, bound))
        parameter_monomials += count
    if len(higher) != 16 or parameter_monomials != 947:
        raise AssertionError((len(higher), parameter_monomials))

    smax = R(1, 10000)
    xmin = R(1, 30)
    sigmamax = sp.factor(smax / xmin)
    if sigmamax != R(3, 1000):
        raise AssertionError(sigmamax)

    amin = 1 - mradius
    amax = 1 + mradius
    y0max = R(12, 25) / amin + tradius
    w0min = (18 - 45 * mradius) / (25 * amin) - tradius
    w0max = (18 + 45 * mradius) / (25 * amax) + tradius
    yupper = smax * y0max

    print("SIGMA_MAX", sigmamax)
    print("H2_CLOSURE_RESERVE", closure_reserve)
    print("HIGHER_SX_TERMS", len(higher))
    print("PARAMETER_MONOMIALS", parameter_monomials)
    for denominator_endpoint in (29, 28, 27, 26, 25, 24, 23):
        xmax = R(1, denominator_endpoint)
        remainder = sp.factor(sum(
            bound * sigmamax**si * xmax**(si + xi - 2)
            for si, xi, bound in higher
        ))
        margin = sp.factor(closure_reserve - remainder)

        wbarmin = w0min - R(3, 5) * xmax
        zslope = sp.factor(wbarmin - smax * y0max**2)
        # Keep the exact negative -X^2 at the monotone upper X endpoint.
        zupper = sp.factor(3 * xmax - xmax**2 + smax * w0max)
        danger = sp.factor(
            R(3, 5) - R(13, 5) * xmax
            - R(6, 5) * yupper - smax * w0max
        )
        tests = {
            "remainder": margin > 0,
            "positive_Z": zslope > 0,
            "Z_cap": zupper < R(1, 8),
            "danger": danger > 0,
            "lambda_rank": amin > 0,
        }
        print("ENDPOINT", f"1/{denominator_endpoint}")
        print("  REMAINDER", remainder)
        print("  MARGIN", margin)
        print("  Z_SLOPE", zslope)
        print("  Z_UPPER", zupper)
        print("  DANGER_RESERVE", danger)
        print("  TESTS", tests)
        print("  STATUS", "PASS" if all(tests.values()) else "METHOD_OR_LEGALITY_FAILURE")

    # The next reciprocal endpoint fails the requested lower-Z cap by an
    # actual exact parameter point, not merely by a loose upper bound.
    xfail = R(1, 23)
    mfail = mradius
    ofail = tradius
    nfail = -tradius
    afail = 1 + mfail
    y0fail = R(12, 25) / afail + nfail
    w0fail = (45 * mfail + 18 + 25 * afail * ofail) / (25 * afail)
    zfail = sp.factor(
        3 * xfail - xfail**2
        + smax * (w0fail - R(3, 5) * xfail)
        - smax**2 * y0fail**2
    )
    xraw = -R(1, 5) + xfail
    yraw = R(3, 5) + smax * y0fail
    lfail = afail / smax
    danger_fail = sp.factor(1 - xraw**2 - yraw**2 - zfail)
    det_fail = sp.factor(R(5, 9) * smax * zfail)
    gate_fail = sp.factor(quartic.as_expr().subs({
        S: smax, Z: zfail, x: xraw, y: yraw, lam: lfail,
    }))
    if not (
        zfail > R(1, 8) and lfail > 0 and danger_fail > 0
        and det_fail > 0
    ):
        raise AssertionError("next reciprocal Z-cap witness")
    print("NEXT_RECIPROCAL_X", xfail)
    print("NEXT_RECIPROCAL_EXACT_Z", zfail)
    print("NEXT_RECIPROCAL_Z_MINUS_1/8", sp.factor(zfail - R(1, 8)))
    print("NEXT_RECIPROCAL_DANGER", danger_fail)
    print("NEXT_RECIPROCAL_DET", det_fail)
    print("NEXT_RECIPROCAL_RAW_GATE", gate_fail)
    print("NEXT_RECIPROCAL_STATUS", "Z_CAP_FAILURE_NOT_GATE_COUNTEREXAMPLE")

    # Finite exact falsification audit at the last passing reciprocal and the
    # first scope-failing reciprocal.  It is not used as continuum proof.
    direct_records = []
    for sv, xv, mv, ov, nv in product(
        (R(1, 1000000), smax),
        (R(1, 24), R(1, 23)),
        (-mradius, mradius),
        (-tradius, tradius),
        (-tradius, tradius),
    ):
        av = 1 + mv
        y0v = R(12, 25) / av + nv
        w0v = (45 * mv + 18 + 25 * av * ov) / (25 * av)
        zv = sp.factor(
            3 * xv - xv**2 + sv * (w0v - R(3, 5) * xv)
            - sv**2 * y0v**2
        )
        xrv = -R(1, 5) + xv
        yrv = R(3, 5) + sv * y0v
        lv = av / sv
        dv = sp.factor(1 - xrv**2 - yrv**2 - zv)
        detv = sp.factor(R(5, 9) * sv * zv)
        if not (lv > 0 and zv > 0 and dv > 0 and detv > 0):
            raise AssertionError(("illegal exact falsification node", sv, xv, mv, ov, nv))
        gv = sp.factor(quartic.as_expr().subs({
            S: sv, Z: zv, x: xrv, y: yrv, lam: lv,
        }))
        direct_records.append(((sv, xv, mv, ov, nv), gv))
    negatives = [item for item in direct_records if item[1] < 0]
    print("DIRECT_EXACT_LEGAL_NODES", len(direct_records))
    print("DIRECT_EXACT_NEGATIVE_NODES", len(negatives))
    print("DIRECT_EXACT_MINIMUM", min(direct_records, key=lambda item: item[1]))
    print("DIRECT_SCOPE", "finite falsification audit only")
    if negatives:
        raise AssertionError(("exact legal gate negative", negatives[0]))


if __name__ == "__main__":
    main()
