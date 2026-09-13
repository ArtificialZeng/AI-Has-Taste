#!/usr/bin/env python3
"""Exact discovery for a moving-sheet stitch across Z=1/8.

The script first certifies non-inclusion in the existing outer box, then
rebuilds the raw compact-ball quartic and tests the recentered
``Y=y-3/5``, ``sigma=S/X`` chart on 1/24 <= X <= 1/23.  Finite exact raw-gate
nodes are a falsification audit only.
"""

if not __debug__:
    raise RuntimeError("do not run this discovery script with python -O")

from itertools import product

import sympy as sp

from compact_ball_adjacent_z_layers_discovery import reconstruct_quartic
from compact_ball_positive_z_moving_sheet_reciprocal_endpoint_envelope_discovery import (
    centered_box_abs,
    centered_box_lower,
    sparse_add,
    sparse_mul,
    sparse_pow,
)


def main():
    R = sp.Rational
    quartic, (S, Z, x, y), lam = reconstruct_quartic()
    mu, X, Y, M = sp.symbols("mu X Y M", real=True)
    omega, nu = sp.symbols("omega nu", real=True)
    A = 1 + M
    denominator = 25 * A
    y0 = (12 + 25 * A * nu) / denominator
    w0 = (45 * M + 18 + 25 * A * omega) / denominator

    smax = R(1, 10000)
    xmin = R(1, 24)
    xmax = R(1, 23)
    mradius = R(1, 1000)
    tradius = R(1, 100)
    amin = 1 - mradius
    amax = 1 + mradius
    y0min = R(12, 25) / amax - tradius
    y0max = R(12, 25) / amin + tradius
    w0min = (18 - 45 * mradius) / (25 * amin) - tradius
    w0max = (18 + 45 * mradius) / (25 * amax) + tradius

    # Exact inclusion certificate against the previously proved outer box.
    xraw_min = -R(1, 5) + xmin
    xraw_max = -R(1, 5) + xmax
    y_gap_inf = R(1, 10)
    y_gap_upper = R(1, 10) + smax * y0max
    if not (
        -R(1, 4) < xraw_min < xraw_max < R(1, 2)
        and y0min > 0 and y_gap_inf > 0
    ):
        raise AssertionError("outer-box inclusion classification")
    print("OUTER_X_RANGE", xraw_min, xraw_max)
    print("OUTER_Y_GAP_INFIMUM", y_gap_inf)
    print("OUTER_Y_GAP_UPPER", y_gap_upper)
    print("OUTER_INCLUSION", "NO: every actual y>3/5>1/2")

    # Rebuild the exact sparse quotient of the original raw gate.
    gate = sp.cancel(quartic.as_expr().subs(lam, mu / S))
    N = sp.expand((S**3 * gate).subs({
        x: -R(1, 5) + X,
        y: R(3, 5) + Y,
        mu: A,
    }))
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
    radii = (mradius, tradius, tradius)
    h2_lowers = {
        key: centered_box_lower(quotient[key], variables, radii)
        for key in ((2, 0), (1, 1), (0, 2))
    }
    if any(value <= 0 for value in h2_lowers.values()):
        raise AssertionError(("H2", h2_lowers))
    closure_reserve = h2_lowers[(0, 2)]
    sigmamax = sp.factor(smax / xmin)
    if sigmamax != R(3, 1250):
        raise AssertionError(sigmamax)

    remainder = sp.Integer(0)
    sx_terms = 0
    parameter_monomials = 0
    for (si, xi), coefficient in quotient.items():
        total = si + xi
        if total <= 2:
            continue
        bound, terms = centered_box_abs(coefficient, variables, radii)
        remainder += bound * sigmamax**si * xmax**(total - 2)
        sx_terms += 1
        parameter_monomials += terms
    remainder = sp.factor(remainder)
    margin = sp.factor(closure_reserve - remainder)
    print("SIGMA_MAX", sigmamax)
    print("REMAINDER_SX_TERMS", sx_terms)
    print("PARAMETER_MONOMIALS", parameter_monomials)
    print("CROSS_CAP_REMAINDER", remainder)
    print("CROSS_CAP_MARGIN", margin)
    print("CROSS_CAP_SIGN_STATUS", "PASS" if margin > 0 else "BOUND_FAILURE_ONLY")

    # Uniform legality without imposing either side of Z=1/8.
    wbarmin = w0min - R(3, 5) * xmax
    zslope = sp.factor(wbarmin - smax * y0max**2)
    zupper = sp.factor(3 * xmax - xmax**2 + smax * w0max)
    danger = sp.factor(
        R(3, 5) - R(13, 5) * xmax
        - R(6, 5) * smax * y0max - smax * w0max
    )
    print("Z_SLOPE", zslope)
    print("Z_UPPER", zupper)
    print("DANGER_RESERVE", danger)
    if not (zslope > 0 and zupper < R(1, 7) and danger > 0 and amin > 0):
        raise AssertionError("cross-cap legality")

    # Exact witnesses on both sides of Z=1/8.
    witness_specs = (
        ("BELOW", xmin, -mradius, -tradius, tradius),
        ("ABOVE", xmax, mradius, tradius, -tradius),
    )
    witness_values = {}
    for label, xv, mv, ov, nv in witness_specs:
        av = 1 + mv
        y0v = R(12, 25) / av + nv
        w0v = (45 * mv + 18 + 25 * av * ov) / (25 * av)
        zv = sp.factor(
            3 * xv - xv**2 + smax * (w0v - R(3, 5) * xv)
            - smax**2 * y0v**2
        )
        xrv = -R(1, 5) + xv
        yrv = R(3, 5) + smax * y0v
        lv = av / smax
        dv = sp.factor(1 - xrv**2 - yrv**2 - zv)
        detv = sp.factor(R(5, 9) * smax * zv)
        gv = sp.factor(quartic.as_expr().subs({
            S: smax, Z: zv, x: xrv, y: yrv, lam: lv,
        }))
        if not (lv > 0 and zv > 0 and dv > 0 and detv > 0 and gv > 0):
            raise AssertionError(("illegal witness", label))
        witness_values[label] = zv
        print(label + "_Z", zv)
        print(label + "_Z_MINUS_1/8", sp.factor(zv - R(1, 8)))
        print(label + "_RAW_GATE", gv)
    if not (witness_values["BELOW"] < R(1, 8) < witness_values["ABOVE"]):
        raise AssertionError("no exact cross-cap witnesses")

    # Finite exact falsification audit, separate from the proof.
    records = []
    xmid = sp.factor((xmin + xmax) / 2)
    for sv, xv, mv, ov, nv in product(
        (R(1, 1000000), R(1, 20000), smax),
        (xmin, xmid, xmax),
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
            raise AssertionError(("illegal exact node", sv, xv, mv, ov, nv))
        gv = sp.factor(quartic.as_expr().subs({
            S: sv, Z: zv, x: xrv, y: yrv, lam: lv,
        }))
        records.append(((sv, xv, mv, ov, nv), gv))
    negatives = [item for item in records if item[1] < 0]
    print("DIRECT_EXACT_LEGAL_NODES", len(records))
    print("DIRECT_EXACT_NEGATIVE_NODES", len(negatives))
    print("DIRECT_EXACT_MINIMUM", min(records, key=lambda item: item[1]))
    print("DIRECT_SCOPE", "finite falsification audit only")
    if negatives:
        raise AssertionError(("exact legal negative", negatives[0]))


if __name__ == "__main__":
    main()
