#!/usr/bin/env python3
"""Exact comparison of affine omega/nu tilted moving-sheet discoveries.

All candidates retain

    |M|<=1/1000, |omega|<=1/100, |nu|<=1/100, 0<S<=1/10000,

use the exact old-sheet seam X=1/5, and end at X=3/13.  The physical centers
are omega+alpha*(X-1/5) and nu+beta*(X-1/5), constrained by
alpha+(6/5)beta=-10636/275.  This is discovery/falsification only.
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run discovery with python -O")

from hashlib import sha256
from itertools import product
from pathlib import Path

import sympy as sp

from compact_ball_adjacent_z_layers_discovery import reconstruct_quartic
from compact_ball_positive_z_moving_sheet_reciprocal_endpoint_envelope_discovery import (
    centered_box_abs,
    centered_box_lower,
    sparse_add,
    sparse_mul,
    sparse_pow,
)


R = sp.Rational


def evaluate(name, alpha, beta, quartic, symbols):
    S, Z, x, y, lam, X, M, omega, nu = symbols
    A = 1 + M
    denominator = 25 * A
    xmin, xmax = R(1, 5), R(3, 13)
    smax = R(1, 10000)
    mrad, wrad, nrad = R(1, 1000), R(1, 100), R(1, 100)
    amin, amax = 1 - mrad, 1 + mrad

    mu, Yaux = sp.symbols("mu Yaux", real=True)
    rescaled = sp.cancel(quartic.as_expr().subs(lam, mu / S))
    numerator = sp.expand((S**3 * rescaled).subs({
        x: -R(1, 5) + X,
        y: R(3, 5) + Yaux,
        mu: A,
    }))
    raw_terms = sp.Poly(numerator, S, Z, X, Yaux).terms()
    ybase = (12 + 25 * A * (nu - beta * xmin)) / denominator
    wbase = (45 * M + 18 + 25 * A * (omega - alpha * xmin)) / denominator
    sparse_y = {(1, 0): ybase}
    if beta != 0:
        sparse_y[(1, 1)] = beta
    sparse_z = {
        (0, 1): R(3),
        (0, 2): -R(1),
        (1, 0): wbase,
        (1, 1): alpha - R(3, 5),
        (2, 0): -ybase**2,
    }
    if beta != 0:
        sparse_z[(2, 1)] = -2 * beta * ybase
        sparse_z[(2, 2)] = -beta**2

    mapped = {}
    for (si, zi, xi, yi), coefficient in raw_terms:
        term = {(si, xi): coefficient}
        term = sparse_mul(term, sparse_pow(sparse_z, zi))
        term = sparse_mul(term, sparse_pow(sparse_y, yi))
        mapped = sparse_add(mapped, term)
    cleared = {
        key: sp.factor(sp.cancel(value * denominator**8))
        for key, value in mapped.items() if value != 0
    }
    if any(key[0] < 2 for key, value in cleared.items() if value != 0):
        raise AssertionError((name, "missing S^2"))
    quotient = {
        (si - 2, xi): sp.expand(value)
        for (si, xi), value in cleared.items() if value != 0
    }
    qcount = len(quotient)
    h1 = quotient.pop((1, 0))
    expected_h1 = R(152587890625) * M**2 * A**8 * (
        5 * M**2 + 14 * M + 14
    )
    if sp.expand(h1 - expected_h1) != 0:
        raise AssertionError((name, "H1"))

    variables = (M, omega, nu)
    radii = (mrad, wrad, nrad)
    h2 = {
        key: centered_box_lower(quotient[key], variables, radii)
        for key in ((2, 0), (1, 1), (0, 2))
    }
    sigmamax = sp.factor(smax / xmin)
    higher = {
        key: coefficient for key, coefficient in quotient.items()
        if sum(key) > 2
    }
    remainder = 0
    monomials = 0
    for (si, xi), coefficient in higher.items():
        bound, terms = centered_box_abs(coefficient, variables, radii)
        remainder += bound * sigmamax**si * xmax**(si + xi - 2)
        monomials += terms
    remainder = sp.factor(remainder)
    margin = sp.factor(h2[(0, 2)] - remainder)
    ratio = sp.factor(remainder / h2[(0, 2)])

    # Exact legality.  The total danger tilt is identical in all candidates.
    y_pos = sp.factor(R(12, 25) / amin + nrad)
    y_neg_right = sp.factor(
        R(12, 25) / amax - nrad + beta * (xmax - xmin)
    )
    y_abs = max(y_pos, abs(y_neg_right))
    wbar_min = sp.factor(
        (18 - 45 * mrad) / (25 * amin) - wrad
        + alpha * (xmax - xmin) - R(3, 5) * xmax
    )
    wbar_max = sp.factor(
        (18 + 45 * mrad) / (25 * amax) + wrad
        - R(3, 5) * xmin
    )
    zlower = sp.factor(
        3 * xmin - xmin**2
        + smax * min(wbar_min, 0) - smax**2 * y_abs**2
    )
    zupper = sp.factor(
        3 * xmax - xmax**2 + smax * max(wbar_max, 0)
    )
    total_tilt = sp.factor(alpha + R(6, 5) * beta)
    Tmax = sp.factor(
        R(9, 5) + wrad + R(6, 5) * nrad
        - R(63, 125) / amax - R(3, 5) * X
        + total_tilt * (X - xmin)
    )
    Tmax_right = sp.factor(Tmax.subs(X, xmax))
    danger_smax = sp.factor(
        R(3, 5) - R(13, 5) * X - smax * Tmax
    )
    danger_smax_right = sp.factor(danger_smax.subs(X, xmax))
    legal_envelope = (
        total_tilt == -R(10636, 275)
        and zlower > 0 and zupper < 1
        and Tmax_right == -R(1, 100)
        and danger_smax_right == R(1, 1000000)
        and sp.diff(danger_smax, X) < 0
    )

    # Exact raw-gate nodes.
    records = []
    xmid = sp.factor((xmin + xmax) / 2)
    for sv, xv, mv, ov, nv in product(
        (R(1, 1000000), R(1, 20000), smax),
        (xmin, xmid, xmax),
        (-mrad, mrad),
        (-wrad, wrad),
        (-nrad, nrad),
    ):
        av = 1 + mv
        omega_v = ov + alpha * (xv - xmin)
        nu_v = nv + beta * (xv - xmin)
        y0v = R(12, 25) / av + nu_v
        w0v = (45 * mv + 18 + 25 * av * omega_v) / (25 * av)
        zv = sp.factor(
            3 * xv - xv**2
            + sv * (w0v - R(3, 5) * xv) - sv**2 * y0v**2
        )
        xrv = -R(1, 5) + xv
        yrv = R(3, 5) + sv * y0v
        lv = av / sv
        danger = sp.factor(1 - xrv**2 - yrv**2 - zv)
        det = sp.factor(R(5, 9) * sv * zv)
        gate = sp.factor(quartic.as_expr().subs({
            S: sv, Z: zv, x: xrv, y: yrv, lam: lv,
        }))
        if not (lv > 0 and zv > 0 and danger > 0 and det > 0):
            raise AssertionError((name, "illegal", sv, xv, mv, ov, nv))
        records.append(((sv, xv, mv, ov, nv), gate, zv, danger, det))
    negatives = [record for record in records if record[1] < 0]
    minimum = min(records, key=lambda record: record[1])
    right_worst = next(
        record for record in records
        if record[0] == (smax, xmax, mrad, wrad, nrad)
    )

    print("CANDIDATE", name)
    print("ALPHA", alpha)
    print("BETA", beta)
    print("OMEGA_CENTER_RIGHT", sp.factor(alpha * (xmax - xmin)))
    print("NU_CENTER_RIGHT", sp.factor(beta * (xmax - xmin)))
    print("RAW_PREMAP_TERMS", len(raw_terms))
    print("QUOTIENT_TERMS", qcount)
    print("HIGHER_TERMS", len(higher))
    print("PARAMETER_MONOMIALS", monomials)
    print("H2_S2", h2[(2, 0)])
    print("H2_SX", h2[(1, 1)])
    print("H2_X2", h2[(0, 2)])
    print("REMAINDER_ABS", remainder)
    print("REMAINDER_CORE_RATIO", ratio)
    print("STRICT_MARGIN", margin)
    print("ABS_CERTIFICATE_STATUS", "PASS" if margin > 0 else "FAILURE_ONLY")
    print("Z_LOWER", zlower)
    print("Z_UPPER", zupper)
    print("TMAX_RIGHT", Tmax_right)
    print("DANGER_SMAX_RIGHT", danger_smax_right)
    print("LEGALITY_STATUS", "PASS" if legal_envelope else "FAIL")
    print("EXACT_NODES", len(records))
    print("EXACT_NEGATIVES", len(negatives))
    print("EXACT_MIN_ARG", minimum[0])
    print("EXACT_MIN_GATE", minimum[1])
    print("RIGHT_WORST_GATE", right_worst[1])
    print("RIGHT_WORST_Z", right_worst[2])
    print("RIGHT_WORST_DANGER", right_worst[3])
    print("RIGHT_WORST_DET", right_worst[4])
    if negatives:
        print("FIRST_EXACT_LEGAL_NEGATIVE", negatives[0])
    print("END_CANDIDATE", name)
    return {
        "name": name,
        "margin": margin,
        "ratio": ratio,
        "negative": negatives[0] if negatives else None,
    }


def main():
    quartic, (S, Z, x, y), lam = reconstruct_quartic()
    X, M, omega, nu = sp.symbols("X M omega nu", real=True)
    total = -R(10636, 275)
    candidates = (
        ("omega_only", total, R(0)),
        ("equal_danger_split", total / 2, R(5, 12) * total),
        ("nu_only", R(0), R(5, 6) * total),
    )
    results = [
        evaluate(
            name, alpha, beta, quartic,
            (S, Z, x, y, lam, X, M, omega, nu),
        )
        for name, alpha, beta in candidates
    ]
    best = min(results, key=lambda result: result["ratio"])
    print("BEST_ABS_RATIO_CANDIDATE", best["name"])
    print("BEST_ABS_RATIO", best["ratio"])
    print("ANY_EXACT_LEGAL_NEGATIVE", any(result["negative"] for result in results))
    print("SCRIPT_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
    print("SCOPE exact discovery only; certificate failure is not gate failure")


if __name__ == "__main__":
    main()

