#!/usr/bin/env python3
"""Exact coverage audit for the stitched five-parameter X-sheet.

This script does not test gate positivity.  It binds the audited chart
descriptions, verifies their exact seams, and supplies one exact legal
compact-ball direction outside the stitched sheet and the principal audited
shape boxes recorded in CLAIM_LEDGER.md.
"""

from __future__ import annotations

import hashlib
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[2]


BOUND = {
    "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md":
        "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_positive_z_moving_sheet_x5_extension.md":
        "a86dbe3eea4d9bfaf2772383407e65a5960e6941344713377068ff048ffc5f4d",
    "tmp/research/audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_POSITIVE_Z_MOVING_SHEET_X5_EXTENSION_INDEPENDENT_AUDIT.md":
        "d2283df6f7414580764f2572167441bc8ff3026fae8ad1882a0960312764d078",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_affine_omega_tilt_extension.md":
        "bd127112e0cd59e9f0ed8c565480a612c2c75ba83edd979c3552896b18395067",
    "tmp/research/audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_AFFINE_OMEGA_TILT_EXTENSION_INDEPENDENT_AUDIT.md":
        "33452bd574d47968fbbc599d6017806c47e672ef9e9ab86a5a2473e1a223a1b2",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_tilt_source_candidate.md":
        "7b78d77ef418de755f41d8fcbd7b8aaa15eae1b1052276fe1a90274c1989e563",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_TILT_INDEPENDENT_REFEREE_AUDIT.md":
        "bde3d29e63f8e9672494a824da34f9081ca0349b37f1cdcaa317d5b7c874c2d5",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_legality_frontier_extension_source_candidate.md":
        "5e4109a188f3301412dd49f78039f2a0d4e107948f8e23c1bdc79cbcd4029aa0",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_LEGALITY_FRONTIER_EXTENSION_INDEPENDENT_REFEREE_AUDIT.md":
        "44ac690f65bf7b6ce7a4be8320ed8406e4e4dae167673117435d5f95b8865591",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_danger_root_source_candidate.md":
        "9a92b5f4c819643dacb7ad5e40bad2e5a73d4b6d301a4f895738e61d785b9120",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_RECENTERED_LIFT_DANGER_ROOT_INDEPENDENT_REFEREE_AUDIT.md":
        "0788871230d0c0f57eb6fd88a16fbefdbccad2682f7b3f28eaf37228d1ac9916",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_constant_lift_x497_500_source_candidate.md":
        "34d9f85a9c242ec4245aa583ef82295fb2a16502dcd49aa909df880bace69b2d",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_CONSTANT_LIFT_X497_500_INDEPENDENT_REFEREE_AUDIT.md":
        "ed2cb48240fa5a17eef9e9e76c4e547942642de1cc3997f2c23ae95818b61c45",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_cap_x_shear_x1_source_candidate.md":
        "9d6a18986fcd6ddefdae87c1cdaeb51ae0e24f97316cecbe91f0536b0295bea5",
    "audit/COMPACT_BALL_CAP_X_SHEAR_X1_INDEPENDENT_REFEREE_AUDIT.md":
        "b8db0fa9bf450312c8921ca9ace147c09b451060647a9b90cb1267992144e71d",
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def zero(expr: sp.Expr, label: str) -> None:
    if sp.cancel(expr) != 0:
        raise AssertionError(f"{label}: {sp.factor(expr)}")


def main() -> None:
    for rel, expected in BOUND.items():
        got = sha256(ROOT / rel)
        if got != expected:
            raise AssertionError(f"dependency hash mismatch: {rel}: {got}")
    print(f"DEPENDENCY_HASHES={len(BOUND)}/{len(BOUND)}")

    S, X, M, omega, nu = sp.symbols("S X M omega nu", real=True)
    A = 1 + M
    y0 = sp.Rational(12, 25) / A + nu
    b0 = (45 * M + 18) / (25 * A) - sp.Rational(3, 5) * X + omega
    tilt = sp.Rational(10636, 275) * (X - sp.Rational(1, 5))
    b1 = b0 - tilt
    xold = -sp.Rational(1, 5) + X
    y = sp.Rational(3, 5) + S * y0
    Z0 = 3 * X - X**2 + S * b0 - S**2 * y0**2
    Z1 = 3 * X - X**2 + S * b1 - S**2 * y0**2
    Zin = sp.Rational(9, 13) - X**2 + S * b1 - S**2 * y0**2
    X0 = sp.Rational(83059, 100000)
    Xstar = sp.Rational(1019767, 1040000)
    Xcap = sp.Rational(497, 500)
    Zrec = Zin + 2 * (X - X0)
    Zconst = Zin + 2 * (Xstar - X0)
    xcap = xold - sp.Rational(3, 2) * (X - Xcap)
    Zcap = Zconst + 2 * (X - Xcap)

    zero((b1 - b0).subs(X, sp.Rational(1, 5)), "center/affine b seam")
    zero((Z1 - Z0).subs(X, sp.Rational(1, 5)), "center/affine Z seam")
    zero((Zin - Z1).subs(X, sp.Rational(3, 13)), "affine/inward Z seam")
    zero((Zrec - Zin).subs(X, X0), "inward/recentered Z seam")
    zero((Zconst - Zrec).subs(X, Xstar), "recentered/constant Z seam")
    zero((xcap - xold).subs(X, Xcap), "constant/cap x seam")
    zero((Zcap - Zconst).subs(X, Xcap), "constant/cap Z seam")
    print("SEAMS=7/7")

    intervals = [
        (sp.Rational(0), sp.Rational(1, 5)),
        (sp.Rational(1, 5), sp.Rational(3, 13)),
        (sp.Rational(3, 13), X0),
        (X0, Xstar),
        (Xstar, Xcap),
        (Xcap, sp.Rational(1)),
    ]
    if intervals[0][0] != 0 or intervals[-1][1] != 1:
        raise AssertionError("wrong outer X endpoints")
    for (_, right), (left, _) in zip(intervals, intervals[1:]):
        if right != left:
            raise AssertionError("X interval gap")
    print("X_PROJECTION=[0,1]")

    y0_min = sp.cancel(y0.subs({M: sp.Rational(1, 1000), nu: -sp.Rational(1, 100)}))
    if y0_min != sp.Rational(46999, 100100) or y0_min <= 0:
        raise AssertionError(f"unexpected y0 lower bound: {y0_min}")
    print(f"Y0_MIN={y0_min}")
    print("SHEET_Y_STRICTLY_GREATER_THAN=3/5")

    # One exact full-cone direction outside the stitched X-sheet.
    xw = sp.Rational(5, 8)
    yw = sp.Rational(0)
    Zw = sp.Rational(1, 8)
    Sw = sp.Rational(1, 2)
    lambdaw = sp.Rational(1)
    danger = sp.cancel(1 - xw**2 - yw**2 - Zw)
    detC = sp.cancel(sp.Rational(5, 9) * Sw * Zw)
    if danger != sp.Rational(31, 64) or detC != sp.Rational(5, 144):
        raise AssertionError("witness legality arithmetic changed")
    if not (danger > 0 and detC > 0 and Sw > 0 and lambdaw > 0):
        raise AssertionError("witness is not strict legal rank two")
    if yw > sp.Rational(3, 5):
        raise AssertionError("witness unexpectedly meets X-sheet y bound")
    if not xw > sp.Rational(1, 2):
        raise AssertionError("witness does not leave the stitched rational box")
    print(f"UNCOVERED_WITNESS=(S,lambda,x,y,Z)=({Sw},{lambdaw},{xw},{yw},{Zw})")
    print(f"UNCOVERED_WITNESS_DANGER={danger}")
    print(f"UNCOVERED_WITNESS_DETC={detC}")
    print("CLASSIFICATION=COVERAGE_GAP_NOT_COUNTEREXAMPLE")
    print("PASS exact stitched-X-sheet coverage audit")


if __name__ == "__main__":
    main()
