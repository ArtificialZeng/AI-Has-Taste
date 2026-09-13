#!/usr/bin/env python3
"""Independent constant-Z X=1 endpoint addendum.

The frozen endpoint-preflight source and its manifest are opaque inputs used
only for SHA-256 binding.  This script does not import, execute, or parse
either file.  It rebuilds the constant-Z sheet and the determinant identity
from the original compact-ball parameter definitions.
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "tmp/research/compact_ball_inward_z_constant_lift_x1_endpoint_preflight.py"
SOURCE_MANIFEST = ROOT / "tmp/research/compact_ball_inward_z_constant_lift_x1_endpoint_preflight_manifest.sha256"
PREDECESSOR_REFEREE = ROOT / "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_constant_lift_x99_100_independent_referee.py"
PREDECESSOR_REPORT = ROOT / "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_CONSTANT_LIFT_X99_100_INDEPENDENT_REFEREE_AUDIT.md"
PREDECESSOR_MANIFEST = ROOT / "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_constant_lift_x99_100_independent_referee_manifest.sha256"
REDUCTION_NOTE = ROOT / "tmp/research/common_metric_ranktwo_transverse_full_cone_compact_ball_reduction.md"
REDUCTION_AUDIT = ROOT / "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_FULL_CONE_COMPACT_BALL_REDUCTION_REFEREE_AUDIT.md"

EXPECTED = {
    SOURCE: "18fbd9ab9937b9700db7ad87e3c1edefaec76f8657c750606452f9a9f7e393bb",
    SOURCE_MANIFEST: "128cbea09b378a24e4a60997695bad51c66118f63da5b645857e270f878c5533",
    PREDECESSOR_REFEREE: "4958ec0eaca83cb06b8a368b94767dd32b826094e8e99fac3b34118aa19083e3",
    PREDECESSOR_REPORT: "cdf21533b5b1e921d28b4ed3d7c70ea0664356b99380469bfb7fa9609df8c12f",
    PREDECESSOR_MANIFEST: "378f98ff3d854f6d013d1578c8657cfa6a27502a631f1dd052f2207fd62266b3",
    REDUCTION_NOTE: "4ad2db93ed2a14fc6d0d54b723fb55943f15e0ad85e0a130f1c568c473e5aaa3",
    REDUCTION_AUDIT: "0a13cb475d667b5ff281f798628571756403e95fbb1eff118fa5cfcba8758f20",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, label: str) -> None:
    if not condition:
        raise AssertionError(f"FAIL CLOSED: {label}")


def zero(expr: sp.Expr) -> bool:
    return sp.cancel(sp.together(expr)) == 0


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-path", type=Path, default=SOURCE)
    parser.add_argument("--manifest-path", type=Path, default=SOURCE_MANIFEST)
    args = parser.parse_args()

    require(__debug__, "optimized Python is forbidden")
    require(sha(args.source_path) == EXPECTED[SOURCE],
            "opaque endpoint-preflight source SHA-256")
    require(sha(args.manifest_path) == EXPECTED[SOURCE_MANIFEST],
            "opaque endpoint-preflight manifest SHA-256")
    for path, expected in EXPECTED.items():
        if path not in (SOURCE, SOURCE_MANIFEST):
            require(sha(path) == expected, f"frozen dependency SHA-256: {path.name}")
    print("PASS opaque source/manifest and frozen predecessor/reduction hashes")
    print("INDEPENDENCE preflight source/manifest used only for SHA-256")

    R = sp.Rational
    S, X, M, omega, nu = sp.symbols("S X M omega nu", real=True)
    A = 1 + M
    Xstar = R(1019767, 1040000)
    anchor = R(83059, 100000)
    Smax = R(1, 10000)
    Mlo, Mhi = -R(1, 1000), R(1, 1000)
    wlo, whi = -R(1, 100), R(1, 100)
    nlo, nhi = -R(1, 100), R(1, 100)

    y0 = R(12, 25) / A + nu
    b = ((45 * M + 18) / (25 * A) - R(3, 5) * X + omega
         - R(10636, 275) * (X - R(1, 5)))
    Zold = R(9, 13) - X**2 + S * b - S**2 * y0**2
    shift = sp.factor(2 * (Xstar - anchor))
    Zconst = sp.factor(Zold + shift)
    require(shift == R(779767, 2600000), "independent constant-Z shift")

    # Endpoint Z obstruction from the original sheet definition.
    Zbase = sp.factor(Zconst.subs({X: 1, S: 0}))
    require(Zbase == -R(20233, 2600000), "constant-Z X=1 S=0 value")
    require(y0.subs({M: Mhi, nu: nlo}) > 0, "uniform y0 positivity")
    require(zero(sp.diff(b, M) - R(27, 25) / A**2),
            "b monotonicity M")
    require(sp.diff(b, omega) == 1, "b monotonicity omega")
    bmax_x1 = sp.factor(b.subs({X: 1, M: Mhi, omega: whi}))
    require(bmax_x1 == -R(15420411, 500500) and bmax_x1 < 0,
            "uniform negative b at X=1")
    # Therefore every 0<S<=Smax has Zconst<Zbase<0.
    require(zero(sp.diff(Zconst, omega) - S), "Z monotonicity omega")
    require(zero(sp.diff(Zconst, nu) + 2 * S**2 * y0),
            "Z monotonicity nu")
    require(zero(sp.diff(Zconst, M)
                 - S * R(27, 25) / A**2
                 - S**2 * R(24, 25) * y0 / A**2),
            "Z monotonicity M")
    require(zero(sp.diff(Zconst, S) - b + 2 * S * y0**2),
            "Z monotonicity S")
    worst_data = {X: 1, S: Smax, M: Mlo, omega: wlo, nu: nhi}
    Zworst = sp.factor(Zconst.subs(worst_data))
    require(Zworst == -R(172289947376065127, 15857127000000000000),
            "exact X=1 lower corner")
    print(f"X1_Z_BASE {Zbase}")
    print(f"X1_Z_WORST {Zworst}")
    print("PASS Zconst<0 for every 0<S<=1/10000 and the frozen box at X=1")

    # Rebuild the original two-by-two compression determinant algebraically.
    h, j, k, ell, Z = sp.symbols("h j k ell Z", real=True)
    C = sp.Matrix([[h**2, h * (j + sp.I * k)],
                   [h * (j - sp.I * k), j**2 + k**2 + ell**2]])
    detC = sp.expand(C.det())
    require(zero(detC - h**2 * ell**2), "original det(C)=h^2 ell^2")
    det_ratio = sp.factor(detC.subs({h**2: S, ell**2: R(5, 9) * Z}) / S)
    require(zero(det_ratio - R(5, 9) * Z), "det(C)/S=(5/9)Z")
    det_worst = sp.factor(R(5, 9) * Zworst)
    require(det_worst == -R(172289947376065127, 28542828600000000000),
            "negative determinant coefficient at lower corner")
    print(f"X1_DETC_OVER_S_WORST {det_worst}")
    print("PASS det(C)/S=(5/9)Zconst<0: constant-Z chart is illegal at X=1")

    # Danger is nevertheless strictly positive, so it is not the obstruction.
    x_sheet = -R(1, 5) + X
    y_sheet = R(3, 5) + S * y0
    danger = sp.factor(1 - x_sheet**2 - y_sheet**2 - Zconst)
    danger_base = sp.factor(R(2, 5) * (X - R(3, 13)) - shift)
    T = sp.factor(R(6, 5) * y0 + b)
    require(zero(sp.diff(T, M) - R(63, 125) / A**2),
            "T monotonicity M")
    require(zero(sp.diff(T, omega) - 1)
            and zero(sp.diff(T, nu) - R(6, 5)),
            "T monotonicity omega and nu")
    require(zero(danger - (danger_base - S * T)),
            "constant-Z danger identity")
    Dbase_x1 = sp.factor(danger_base.subs(X, 1))
    Tmax_x1 = sp.factor(T.subs({X: 1, M: Mhi, omega: whi, nu: nhi}))
    require(Dbase_x1 == R(20233, 2600000) and Dbase_x1 > 0,
            "positive X=1 danger base")
    require(Tmax_x1 == -R(432183, 14300) and Tmax_x1 < 0,
            "uniform negative T at X=1")
    print(f"X1_DANGER_BASE {Dbase_x1}")
    print(f"X1_TMAX {Tmax_x1}")
    print("PASS danger=Dbase-S*T>Dbase>0 at X=1")

    # The lower-corner Z function crosses strictly between the two rationals.
    lower = sp.factor(Zconst.subs({S: Smax, M: Mlo,
                                   omega: wlo, nu: nhi}))
    left, right = R(497, 500), R(199, 200)
    lower_left = sp.factor(lower.subs(X, left))
    lower_right = sp.factor(lower.subs(X, right))
    require(lower_left == R(17798406223702873, 15857127000000000000)
            and lower_left > 0, "lower-corner Z positive at 497/500")
    require(lower_right == -R(13803700407925127, 15857127000000000000)
            and lower_right < 0, "lower-corner Z negative at 199/200")
    require(zero(sp.diff(lower, X) + 2 * X + R(10801, 275) * Smax),
            "lower-corner Z derivative")
    require(sp.diff(lower, X).subs(X, left) < 0
            and sp.diff(lower, X).subs(X, right) < 0,
            "lower-corner Z strictly decreasing on bracket")
    print(f"ROOT_BRACKET_LEFT {left} value={lower_left}")
    print(f"ROOT_BRACKET_RIGHT {right} value={lower_right}")
    print("PASS unique lower-corner Z root satisfies 497/500<root<199/200")

    # Internal fail-closed sentinels: neither a changed shift nor a flipped
    # determinant sign can satisfy the exact defining identities.
    bad_shift = Zold + R(2001, 1000) * (Xstar - anchor)
    require(not zero(bad_shift - Zconst), "internal bad-shift attack rejected")
    require(not zero(-R(5, 9) * Z - det_ratio),
            "internal flipped-det(C) attack rejected")

    print("SCOPE chart illegality only; no raw-gate sign or Bernstein claim")
    print("SCOPE no maximality, CE-046/048/059/060, full-ball or common-metric inference")
    print("VERDICT PASS independent constant-Z X=1 endpoint addendum")


if __name__ == "__main__":
    main()
