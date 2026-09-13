#!/usr/bin/env python3
"""Exact seam-preserving x-shear cap cell on 497/500 <= X <= 1.

The independently audited predecessor ends at X=497/500 with

    Z_constant = Z_old + 2 (Xstar-Xanchor),
    Xstar = 1019767/1040000,

The old transverse coordinates admit an exact Z-only no-go at X=1.  This
source instead uses the seam-preserving cap chart

    x_cap = x_old - (3/2)(X-497/500),
    y_cap = y_old,
    Z_cap = Z_constant + 2(X-497/500),

on the single adjacent cell 497/500 <= X <= 1.  It binds the independently
audited predecessor and exact legality preflight, rebuilds the original fully
conjugated Hermitian Q,Q^2 gate, checks the parameter/cleared-gate/core seam
and full endpoint legality before constructing the 40-control certificate.
It is a source candidate, not an independent referee result.
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run with python -O")

from hashlib import sha256
from pathlib import Path
import os
import sys


if len(sys.argv) != 1:
    raise SystemExit("usage: cap x-shear X=1 exact gate accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
BUILDER = "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_exact_gate.py"
PREDECESSOR = "tmp/research/compact_ball_inward_z_constant_lift_x497_500_exact_gate.py"
DEPENDENCIES = {
    BUILDER:
        "33bad020143d4e4143b0742526b4fb0ba4d0089d1e12e8365ceca878577e0d2e",
    PREDECESSOR:
        "d38dba1bf18b5906765f217bd764edc974cad2821ee8630fc292cffa77994653",
    "tmp/research/compact_ball_inward_z_constant_lift_x497_500_source_freeze_manifest.sha256":
        "e7220043d9ac01c91e72ebf4029a8c248bff77bb2225b2884b5c372c60df108d",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_constant_lift_x497_500_independent_referee.py":
        "15b996eb17581b8627e2a02686fd30d677d02ac8679e9947b1d93e4e47cf0f2e",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_CONSTANT_LIFT_X497_500_INDEPENDENT_REFEREE_AUDIT.md":
        "ed2cb48240fa5a17eef9e9e76c4e547942642de1cc3997f2c23ae95818b61c45",
    "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_constant_lift_x497_500_independent_referee_manifest.sha256":
        "50c451f84eabfdb7832e3610c37bd347dc1419c109f64b7c7cece41e8e60eb06",
    "tmp/research/compact_ball_cap_x_shear_legality_preflight.py":
        "838758106ab04ec129666f9a81c62cc53139136fceb29b88073dc51d6a89e387",
    "tmp/research/compact_ball_cap_x_shear_legality_preflight.txt":
        "380a3626dd674caa8d5215c4fa2b31ddc78c28bc9836bef20d355a7d9ba1ab20",
    "tmp/research/compact_ball_cap_x_shear_legality_preflight.exit":
        "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
}
if os.environ.get("CAP_X_SHEAR_X1_BAD_SOURCE") == "1":
    DEPENDENCIES[BUILDER] = "0" * 64
if os.environ.get("CAP_X_SHEAR_X1_BAD_PREDECESSOR") == "1":
    DEPENDENCIES[PREDECESSOR] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    if not path.is_file():
        raise RuntimeError(f"cap x-shear X=1 failed: missing {relative}")
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(f"cap x-shear X=1 failed: hash mismatch {relative}")
print("PASS frozen X497/500 source/referee and cap preflight hashes", flush=True)


def replace_exact(source, old, new, count):
    actual = source.count(old)
    if actual != count:
        raise RuntimeError(
            "cap x-shear X=1 failed: specialization multiplicity "
            f"{old!r}: expected {count}, got {actual}"
        )
    return source.replace(old, new)


source = (ROOT / BUILDER).read_text(encoding="utf-8")
replacements = (
    ("to X=7/8", "to the X=1 x-shear cap", 1),
    ("17/20 <= X <= 7/8", "497/500 <= X <= 1", 1),
    ("X7/8", "CAP-X-SHEAR-X1", 1),
    ("INWARD_Z_X7_8", "CAP_X_SHEAR_X1", 3),
    ("Xleft = R(17, 20)", "Xleft = R(497, 500)", 1),
    ("Xright = R(7, 8)", "Xright = R(1)", 1),
    ("at X=17/20", "at X=497/500", 2),
    (
        "xsheet = -R(1, 5) + X",
        "xsheet = -R(1, 5) + X - R(3, 2)*(X-Xleft)",
        1,
    ),
    (
        "    x: -R(1, 5)+X,",
        "    x: -R(1, 5)+X-R(3, 2)*(X-Xleft),",
        1,
    ),
    (
        "Znew = sp.expand(Zold + K*(X-Xanchor))",
        "Xstar = R(1019767, 1040000)\n"
        "Znew = sp.expand(\n"
        "    Zold + K*(Xstar-Xanchor) + K*(X-Xleft)\n"
        ")",
        1,
    ),
    (
        "    (0, 0): R(9, 13)-K*Xanchor,\n"
        "    (0, 1): K,",
        "    (0, 0): (R(9, 13)+K*(Xstar-Xanchor)\n"
        "             -K*Xleft),\n"
        "    (0, 1): K,",
        1,
    ),
    (
        "require(len(premap_poly.terms()) == 134, \"134-term sparse pre-map\")",
        "require(len(premap_poly.terms()) == 177, \"177-term cap sparse pre-map\")",
        1,
    ),
)
for old, new, count in replacements:
    source = replace_exact(source, old, new, count)

# Explicit predecessor/new seam checks before legality and controls.
splice_print = 'print("PASS exact old/new chart and raw-gate splice", flush=True)'
splice_extension = splice_print + r'''
Z_previous_seam = sp.factor(
    (Zold + K*(Xstar-Xanchor)).subs(X, Xleft)
)
Z_cap_seam = sp.factor(Znew.subs(X, Xleft))
x_previous_seam = (-R(1, 5)+X).subs(X, Xleft)
x_cap_seam = xsheet.subs(X, Xleft)
y_previous_seam = ysheet.subs(X, Xleft)
y_cap_seam = ysheet.subs(X, Xleft)
lambda_previous_seam = A/S
lambda_cap_seam = A/S
require(sp.factor(Z_previous_seam-Z_cap_seam) == 0
        and sp.factor(x_previous_seam-x_cap_seam) == 0
        and sp.factor(y_previous_seam-y_cap_seam) == 0
        and sp.factor(lambda_previous_seam-lambda_cap_seam) == 0,
        "full (x,y,Z,lambda) parameter seam")
old_gate_seam = sp.factor((36*Gamma).subs({
    lam: lambda_previous_seam,
    x: x_previous_seam,
    y: y_previous_seam,
    Z: Z_previous_seam,
}))
new_gate_seam = sp.factor((36*Gamma).subs({
    lam: lambda_cap_seam,
    x: x_cap_seam,
    y: y_cap_seam,
    Z: Z_cap_seam,
}))
positive_clear = 25**8*A**8*S**3
require(sp.factor(sp.cancel(
    positive_clear*(old_gate_seam-new_gate_seam)
)) == 0, "cleared raw-gate seam")
require(sp.factor(sp.cancel(
    (positive_clear*old_gate_seam-first_layer)
    -(positive_clear*new_gate_seam-first_layer)
)) == 0, "cleared core seam")
print("PASS exact X=497/500 (x,y,Z,lambda)/cleared-gate/cleared-core seam",
      flush=True)
'''
source = replace_exact(source, splice_print, splice_extension, 1)

# Legality is checked before the continuum certificate, so a chart failure
# cannot spend or contaminate the positivity gate.
control_marker = "# One exact Bernstein cell only."
legality_marker = "# Full-cell legality."
diagnostic_marker = "# Definition-level diagnostic nodes."
prefix, after_control = source.split(control_marker, 1)
control_body, after_legality = after_control.split(legality_marker, 1)
legality_body, diagnostic_body = after_legality.split(diagnostic_marker, 1)
cap_legality = r'''
# Exact Z-only obstruction for the old transverse coordinates at X=1.
y0min = sp.factor(y0.subs({M: Mrad, nu: -nu_rad}))
y0max = sp.factor(y0.subs({M: -Mrad, nu: nu_rad}))
require(y0min == R(46999, 100100) > 0
        and y0max == R(16333, 33300) >= y0min,
        "strict y0 interval")
Zonly_excess = sp.factor(
    (((-R(1, 5)+X)**2+ysheet**2-1).subs(X, 1))
)
require(sp.factor(Zonly_excess-S*y0*(R(6, 5)+S*y0)) == 0,
        "exact Z-only no-go identity at X=1")
print("PASS exact Z-only chart-family obstruction at X=1", flush=True)

# Full cap-chart legality.  Parameter monotonicities identify the worst Z
# corner, and concavity in X reduces its lower bound to the two endpoints.
bmax = sp.factor(b.subs({X: Xleft, M: Mrad, omega: omega_rad}))
bmin = sp.factor(b.subs({X: Xright, M: -Mrad,
                         omega: -omega_rad}))
require(bmin <= bmax < 0, "uniform negative b")
require(sp.factor(sp.diff(b, M)-R(27, 25)/A**2) == 0
        and sp.diff(b, omega) == 1
        and sp.diff(b, X) == -R(10801, 275),
        "exact b monotonicity")
require(sp.factor(sp.diff(y0, M)+R(12, 25)/A**2) == 0
        and sp.diff(y0, nu) == 1,
        "exact y0 monotonicity")

Zworst = sp.factor(Znew.subs({S: Smax, M: -Mrad,
                              omega: -omega_rad, nu: nu_rad}))
require(sp.diff(Zworst, X, 2) == -2,
        "worst-corner Z is concave in X")
Zleft = sp.factor(Zworst.subs(X, Xleft))
Zright = sp.factor(Zworst.subs(X, Xright))
require(Zleft == R(17798406223702873, 15857127000000000000) > 0,
        "strict seam Z reserve")
require(Zright == R(17995576623934873, 15857127000000000000)
        > Zleft,
        "strict X=1 Z reserve")
Zmin = Zleft
Zupper = sp.factor(Znew.subs({X: Xright, S: 0}))
require(Zupper == R(10967, 2600000) < 1,
        "uniform Z upper bound")
Zderivative = sp.factor(sp.diff(Znew, X))
require(sp.factor(Zderivative-(K-2*X-R(10801, 275)*S)) == 0,
        "exact cap Z derivative")
Zderivative_lower = sp.factor(
    Zderivative.subs({X: Xright, S: Smax})
)
Zderivative_upper = sp.factor(
    Zderivative.subs({X: Xleft, S: 0})
)
require(Zderivative_lower == -R(10801, 2750000)
        and Zderivative_upper == R(3, 250),
        "exact cap Z derivative interval")

T = sp.factor(R(6, 5)*y0+b)
Tmax = sp.factor(T.subs({X: Xleft, M: Mrad,
                         omega: omega_rad, nu: nu_rad}))
require(Tmax == -R(1218219, 40625) < 0,
        "uniform negative danger correction")
require(sp.factor(sp.cancel(sp.diff(T, M)-R(63, 125)/A**2)) == 0
        and sp.factor(sp.cancel(sp.diff(T, omega)-1)) == 0
        and sp.factor(sp.cancel(sp.diff(T, nu)-R(6, 5))) == 0
        and sp.factor(sp.cancel(sp.diff(T, X)+R(10801, 275))) == 0,
        "exact T monotonicity")

danger_new = sp.factor(1-xsheet**2-ysheet**2-Znew)
danger_direct = sp.factor(1-xsheet**2-ysheet**2-Znew)
require(sp.factor(danger_new-danger_direct) == 0,
        "exact cap danger identity")
danger_base_poly = sp.factor(danger_direct.subs(S, 0))
require(sp.factor(danger_direct-danger_base_poly+S*T) == 0,
        "danger base plus negative-T correction")
Dderivative = sp.factor(sp.diff(danger_direct, X))
require(sp.factor(Dderivative-(432040*S+16500*X-7799)/11000) == 0,
        "exact cap danger derivative")
Dderivative_inf = sp.factor(Dderivative.subs({X: Xleft, S: 0}))
require(Dderivative_inf == R(391, 500) > 0,
        "danger increases across the full cell")
danger_base = sp.factor(danger_base_poly.subs(X, Xleft))
danger_right_base = sp.factor(danger_base_poly.subs(X, Xright))
require(danger_base == R(13993, 2600000) > 0
        and danger_right_base == R(8207, 812500) > danger_base,
        "strict full-cell and X=1 danger")

det_coefficient = sp.factor(R(5, 9)*Zmin)
require(det_coefficient
        == R(17798406223702873, 28542828600000000000) > 0,
        "strict both-z rank-two determinant lower bound")
print("PASS full-cell and X=1 lambda/Z/danger/rank-two legality for both z signs",
      flush=True)
'''
source = (prefix + legality_marker + cap_legality
          + control_marker + control_body
          + diagnostic_marker + diagnostic_body)

# Fail-closed source mutations strike independent proof layers.
if os.environ.get("CAP_X_SHEAR_X1_DROP_Q2") == "1":
    source = replace_exact(source, "Q2 = sp.expand(Q*Q)",
                           "Q2 = sp.zeros(3, 3)", 1)
if os.environ.get("CAP_X_SHEAR_X1_FLIP_DANGER") == "1":
    source = replace_exact(
        source,
        "danger_new = sp.factor(1-xsheet**2-ysheet**2-Znew)",
        "danger_new = sp.factor(-(1-xsheet**2-ysheet**2-Znew))",
        1,
    )
if os.environ.get("CAP_X_SHEAR_X1_DROP_CORE") == "1":
    source = replace_exact(
        source,
        "if os.environ.get(\"CAP_X_SHEAR_X1_DROP_TERM\") == \"1\":",
        "if True:",
        1,
    )

namespace = {
    "__name__": "__main__",
    "__file__": str(Path(__file__).resolve()),
    "__builtins__": __builtins__,
}
exec(compile(source, str(Path(__file__).resolve()), "exec"), namespace)

lower_table = namespace["lowers"]
minimum_index = namespace["minimum_index"]
reserve = namespace["reserve"]
ties = [key for key, value in lower_table.items() if value == reserve]
if ties != [minimum_index]:
    raise RuntimeError(
        "cap x-shear X=1 failed: weakest control is not unique: "
        f"{ties}"
    )
print("PASS unique weakest centered control", minimum_index, flush=True)
print("CHART x=x_old-(3/2)(X-497/500), y=y_old, "
      "Z=Z_constant+2(X-497/500)",
      flush=True)
print("Z_ONLY_NO_GO X=1 old transverse x,y exclude every Z>=0", flush=True)
print("RESULT exact source candidate on one seam-preserving cap cell to X=1",
      flush=True)
print("CLASSIFICATION proof candidate; no chart illegality and no raw-gate negative",
      flush=True)
print("SCOPE one local cap cell only; full compact ball/common metric/arbitrary-node/fixed-lens open",
      flush=True)
