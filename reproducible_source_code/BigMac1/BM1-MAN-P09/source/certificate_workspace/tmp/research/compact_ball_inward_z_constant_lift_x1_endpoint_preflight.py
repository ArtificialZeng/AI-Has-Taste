#!/usr/bin/env python3
"""Exact endpoint preflight for the constant-Z chart on 99/100 <= X <= 1.

This script deliberately stops before any Bernstein-control construction.  It
rebuilds the original fully conjugated Hermitian Q,Q^2 gate from the frozen
sparse builder, checks the three seam layers at X=99/100, and then classifies
the full-cell chart legality exactly.  The result is a chart obstruction, not
a negative raw-gate counterexample and not a maximality assertion.
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run with python -O")

from hashlib import sha256
from pathlib import Path
import os
import sys


if len(sys.argv) != 1:
    raise SystemExit("usage: constant-lift X=1 endpoint preflight accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
BUILDER = "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_exact_gate.py"
DEPENDENCIES = {
    BUILDER:
        "33bad020143d4e4143b0742526b4fb0ba4d0089d1e12e8365ceca878577e0d2e",
    "tmp/research/compact_ball_inward_z_constant_lift_x99_100_exact_gate.py":
        "a99072346ca9d92e3a5e45600d1de371b2609185bef60b2c069d2a400e1d9322",
    "tmp/research/compact_ball_inward_z_constant_lift_x99_100_source_freeze_manifest.sha256":
        "e573ff4ab4ab1f2065ff6c40289aacd19e8629e3bbe53b177cd996c7624d7840",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_constant_lift_x99_100_independent_referee.py":
        "4958ec0eaca83cb06b8a368b94767dd32b826094e8e99fac3b34118aa19083e3",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_CONSTANT_LIFT_X99_100_INDEPENDENT_REFEREE_AUDIT.md":
        "cdf21533b5b1e921d28b4ed3d7c70ea0664356b99380469bfb7fa9609df8c12f",
    "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_constant_lift_x99_100_independent_referee_manifest.sha256":
        "378f98ff3d854f6d013d1578c8657cfa6a27502a631f1dd052f2207fd62266b3",
}
if os.environ.get("INWARD_Z_CONSTANT_X1_BAD_SOURCE") == "1":
    DEPENDENCIES[BUILDER] = "0" * 64
if os.environ.get("INWARD_Z_CONSTANT_X1_BAD_PREDECESSOR") == "1":
    DEPENDENCIES[
        "tmp/research/compact_ball_inward_z_constant_lift_x99_100_exact_gate.py"
    ] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    if not path.is_file():
        raise RuntimeError(f"constant-lift X=1 preflight failed: missing {relative}")
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(
            f"constant-lift X=1 preflight failed: hash mismatch {relative}"
        )
print("PASS frozen X99/100 source/referee dependency hashes", flush=True)


def replace_exact(source, old, new, count):
    actual = source.count(old)
    if actual != count:
        raise RuntimeError(
            "constant-lift X=1 preflight failed: specialization multiplicity "
            f"{old!r}: expected {count}, got {actual}"
        )
    return source.replace(old, new)


source = (ROOT / BUILDER).read_text(encoding="utf-8")
replacements = (
    ("to X=7/8", "to X=1 endpoint preflight on the constant lift", 1),
    ("17/20 <= X <= 7/8", "99/100 <= X <= 1 endpoint preflight", 1),
    ("X7/8", "X1-ENDPOINT-PREFLIGHT", 1),
    ("INWARD_Z_X7_8", "INWARD_Z_CONSTANT_X1_PREFLIGHT", 3),
    ("Xleft = R(17, 20)", "Xleft = R(99, 100)", 1),
    ("Xright = R(7, 8)", "Xright = R(1)", 1),
    ("at X=17/20", "at X=99/100", 2),
    (
        "Znew = sp.expand(Zold + K*(X-Xanchor))",
        "Xstar = R(1019767, 1040000)\n"
        "Znew = sp.expand(Zold + K*(Xstar-Xanchor))",
        1,
    ),
    (
        "    (0, 0): R(9, 13)-K*Xanchor,\n"
        "    (0, 1): K,",
        "    (0, 0): R(9, 13)+K*(Xstar-Xanchor),\n"
        "    (0, 1): R(0),",
        1,
    ),
)
for old, new, count in replacements:
    source = replace_exact(source, old, new, count)

# Reconstruct through the original raw gate, sparse composition, positive
# clearing, core extraction, and the builder's parameter-level splice.  The
# control and old legality blocks are intentionally excluded.
control_marker = "# One exact Bernstein cell only."
legality_marker = "# Full-cell legality."
diagnostic_marker = "# Definition-level diagnostic nodes."
prefix, after_control = source.split(control_marker, 1)
_control_body, after_legality = after_control.split(legality_marker, 1)
_old_legality, _diagnostic = after_legality.split(diagnostic_marker, 1)

seam_and_legality = r'''
# Bind the new cell directly to the independently audited predecessor chart at
# X=99/100.  Both cells use the same constant-Z formula.
Z_previous = sp.expand(Zold + K*(Xstar-Xanchor))
Z_current = Znew
require(sp.factor((Z_previous-Z_current).subs(X, Xleft)) == 0,
        "constant chart parameter seam")
seam_common = {
    lam: A/S,
    x: xsheet.subs(X, Xleft),
    y: ysheet.subs(X, Xleft),
}
old_gate_seam = sp.factor((36*Gamma).subs({
    **seam_common, Z: Z_previous.subs(X, Xleft),
}))
new_gate_seam = sp.factor((36*Gamma).subs({
    **seam_common, Z: Z_current.subs(X, Xleft),
}))
positive_clear = 25**8*A**8*S**3
require(sp.factor(sp.cancel(
    positive_clear*(old_gate_seam-new_gate_seam)
)) == 0, "cleared raw-gate seam")
require(sp.factor(sp.cancel(
    (positive_clear*old_gate_seam-first_layer)
    -(positive_clear*new_gate_seam-first_layer)
)) == 0, "cleared core seam")
print("PASS exact X=99/100 parameter/cleared-gate/cleared-core seam", flush=True)

# Exact full-cell legality classification.  The constant chart has
# dZ/dX=-2X-(10801/275)S<0.  Its exact worst corner is therefore the right
# endpoint, S=Smax, M=-Mrad, omega=-omega_rad, nu=nu_rad.
Zderivative = sp.factor(sp.diff(Znew, X))
require(sp.factor(Zderivative-(-2*X-R(10801, 275)*S)) == 0,
        "exact constant-lift Z derivative")
Zderivative_lower = sp.factor(-2*Xright-R(10801, 275)*Smax)
Zderivative_upper = sp.factor(-2*Xleft)
require(Zderivative_lower == -R(5510801, 2750000)
        and Zderivative_upper == -R(99, 50) < 0,
        "Z strictly decreases on the full cell")

y0min = sp.factor(y0.subs({M: Mrad, nu: -nu_rad}))
y0max = sp.factor(y0.subs({M: -Mrad, nu: nu_rad}))
bmax = sp.factor(b.subs({X: Xleft, M: Mrad, omega: omega_rad}))
bmin_right = sp.factor(b.subs({X: Xright, M: -Mrad,
                               omega: -omega_rad}))
require(0 < y0min <= y0max and bmin_right <= bmax < 0,
        "uniform y0/b signs")
require(sp.factor(sp.diff(b, M)-R(27, 25)/A**2) == 0
        and sp.diff(b, omega) == 1
        and sp.diff(b, X) == -R(10801, 275),
        "exact b monotonicity")
require(sp.factor(sp.diff(y0, M)+R(12, 25)/A**2) == 0
        and sp.diff(y0, nu) == 1,
        "exact y0 monotonicity")

Zright_base = sp.factor(Znew.subs({X: Xright, S: 0}))
Zmin = sp.factor(Znew.subs({X: Xright, S: Smax, M: -Mrad,
                            omega: -omega_rad, nu: nu_rad}))
Zupper = sp.factor(Znew.subs({X: Xleft, S: 0}))
require(Zright_base == -R(20233, 2600000) < 0,
        "exact S=0 endpoint Z obstruction")
require(Zmin == -R(172289947376065127, 15857127000000000000) < 0,
        "exact full-box Z obstruction")
require(Zupper == R(31507, 2600000) < 1,
        "uniform Z upper bound")

T = sp.factor(R(6, 5)*y0+b)
Tmax = sp.factor(T.subs({X: Xleft, M: Mrad,
                         omega: omega_rad, nu: nu_rad}))
require(Tmax == -R(5332081, 178750) < 0,
        "uniform negative danger correction")
require(sp.factor(sp.cancel(sp.diff(T, M)-R(63, 125)/A**2)) == 0
        and sp.factor(sp.cancel(sp.diff(T, omega)-1)) == 0
        and sp.factor(sp.cancel(sp.diff(T, nu)-R(6, 5))) == 0
        and sp.factor(sp.cancel(sp.diff(T, X)+R(10801, 275))) == 0,
        "exact T monotonicity")
danger_new = sp.factor(1-xsheet**2-ysheet**2-Znew)
danger_identity = sp.factor(
    R(2, 5)*(X-R(3, 13))-K*(Xstar-Xanchor)-S*T
)
require(sp.factor(danger_new-danger_identity) == 0,
        "exact constant-chart danger identity")
danger_left_base = sp.factor(danger_identity.subs({X: Xleft, S: 0}))
danger_right_base = sp.factor(danger_identity.subs({X: Xright, S: 0}))
require(danger_left_base == R(9833, 2600000) > 0
        and danger_right_base == R(20233, 2600000) > danger_left_base,
        "strict full-cell danger lower bound")

# For both z signs, the rank-two determinant identity is (5/9)SZ.  Its
# algebraic identity remains valid, but the negative endpoint Z means the
# real-chart/rank-two legality condition fails before the raw gate is tested.
det_coefficient = sp.factor(R(5, 9)*Zmin)
require(det_coefficient == -R(172289947376065127,
                              28542828600000000000) < 0,
        "exact rank-two determinant obstruction induced by negative Z")

print("PASS original-gate endpoint preflight completed", flush=True)
print("CELL", Xleft, Xright)
print("Z_RIGHT_BASE", Zright_base)
print("Z_MIN", Zmin)
print("Z_UPPER", Zupper)
print("Z_DERIVATIVE_INTERVAL", Zderivative_lower, Zderivative_upper)
print("T_MAX", Tmax)
print("DANGER_BASE_INTERVAL", danger_left_base, danger_right_base)
print("DET_C_WITNESS_COEFFICIENT", det_coefficient)
print("SCRIPT_SHA256", sha256(Path(__file__).read_bytes()).hexdigest())
print("RESULT exact endpoint chart obstruction; controls intentionally not run")
print("CLASSIFICATION chart illegality (Z<0), not Bernstein insufficiency, "
      "not resource failure, not legal raw-gate negative")
print("SCOPE X=1 obstruction only; no maximality and no CE number")
'''

source = prefix + seam_and_legality
namespace = {
    "__name__": "__main__",
    "__file__": str(Path(__file__).resolve()),
    "__builtins__": __builtins__,
}
exec(compile(source, str(Path(__file__).resolve()), "exec"), namespace)
