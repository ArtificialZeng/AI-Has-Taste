#!/usr/bin/env python3
"""Exact first right-hand cell for a seam-preserving constant-Z lift.

The independently audited recentered chart ends at

    Xstar = 1019767/1040000.

This source changes charts by

    Z_constant = Z_recentered - 2 (X-Xstar)
               = Z_old + 2 (Xstar-Xanchor)

and treats exactly Xstar <= X <= 99/100.  It binds the audited predecessor,
rebuilds the original fully conjugated Hermitian Q,Q^2 gate, verifies the
three seam layers and full legality before constructing the 40-control
certificate.  It is a source candidate, not an independent referee result.
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run with python -O")

from hashlib import sha256
from pathlib import Path
import os
import sys


if len(sys.argv) != 1:
    raise SystemExit("usage: constant-lift X99/100 exact gate accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
BUILDER = "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_exact_gate.py"
PREDECESSOR = "tmp/research/compact_ball_inward_z_recentered_lift_danger_root_exact_gate.py"
DEPENDENCIES = {
    BUILDER:
        "33bad020143d4e4143b0742526b4fb0ba4d0089d1e12e8365ceca878577e0d2e",
    PREDECESSOR:
        "ff17446a58de45a1ca095b98e6414e6c66c7e26ea4a4c772bc79f94bc8cb4ebb",
    "tmp/research/compact_ball_inward_z_recentered_lift_danger_root_source_freeze_manifest.sha256":
        "9ade4c2d4f293940f8c801eda0716ffc79428ba6e3280cb2241f347a43d5fa8e",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_danger_root_independent_referee.py":
        "c05ec572c5deac77b2e527f0cbe967b494767e975eb7a2ac74901dcf86aac9cb",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_RECENTERED_LIFT_DANGER_ROOT_INDEPENDENT_REFEREE_AUDIT.md":
        "0788871230d0c0f57eb6fd88a16fbefdbccad2682f7b3f28eaf37228d1ac9916",
    "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_danger_root_independent_referee_manifest.sha256":
        "8fd7cea471d2f00508fd27faa387333b648f9e9425f3d07d07ed5b4b24be810f",
}
if os.environ.get("INWARD_Z_CONSTANT_X99_100_BAD_SOURCE") == "1":
    DEPENDENCIES[BUILDER] = "0" * 64
if os.environ.get("INWARD_Z_CONSTANT_X99_100_BAD_PREDECESSOR") == "1":
    DEPENDENCIES[PREDECESSOR] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    if not path.is_file():
        raise RuntimeError(f"constant-lift X99/100 failed: missing {relative}")
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(f"constant-lift X99/100 failed: hash mismatch {relative}")
print("PASS frozen danger-root source/referee dependency hashes", flush=True)


def replace_exact(source, old, new, count):
    actual = source.count(old)
    if actual != count:
        raise RuntimeError(
            "constant-lift X99/100 failed: specialization multiplicity "
            f"{old!r}: expected {count}, got {actual}"
        )
    return source.replace(old, new)


source = (ROOT / BUILDER).read_text(encoding="utf-8")
replacements = (
    ("to X=7/8", "to X=99/100 on the constant lift", 1),
    ("17/20 <= X <= 7/8",
     "1019767/1040000 <= X <= 99/100", 1),
    ("X7/8", "X99/100-CONSTANT", 1),
    ("INWARD_Z_X7_8", "INWARD_Z_CONSTANT_X99_100", 3),
    ("Xleft = R(17, 20)", "Xleft = R(1019767, 1040000)", 1),
    ("Xright = R(7, 8)", "Xright = R(99, 100)", 1),
    ("at X=17/20", "at X=1019767/1040000", 2),
    ("Znew = sp.expand(Zold + K*(X-Xanchor))",
     "Znew = sp.expand(Zold + K*(Xleft-Xanchor))", 1),
    (
        "    (0, 0): R(9, 13)-K*Xanchor,\n"
        "    (0, 1): K,",
        "    (0, 0): R(9, 13)+K*(Xleft-Xanchor),\n"
        "    (0, 1): R(0),",
        1,
    ),
    ("Znew.subs(X, X_previous),",
     "(Zold + K*(X-Xanchor)).subs(X, X_previous),", 1),
    (
        "require(sp.factor(Zderivative-(K-2*X-R(10801, 275)*S)) == 0,\n"
        "        \"exact Z derivative\")\n"
        "Zderivative_lower = sp.factor(K-2*Xright-R(10801, 275)*Smax)\n"
        "require(Zderivative_lower == R(676699, 2750000) > 0,\n"
        "        \"Z increases on the full cell\")",
        "require(sp.factor(Zderivative-(-2*X-R(10801, 275)*S)) == 0,\n"
        "        \"exact constant-lift Z derivative\")\n"
        "Zderivative_lower = sp.factor(-2*Xright-R(10801, 275)*Smax)\n"
        "Zderivative_upper = sp.factor(-2*Xleft)\n"
        "require(Zderivative_lower == -R(5455801, 2750000)\n"
        "        and Zderivative_upper == -R(1019767, 520000) < 0,\n"
        "        \"Z decreases on the full cell\")",
        1,
    ),
    ("bmin_left = sp.factor(b.subs({X: Xleft, M: -Mrad,",
     "bmin_right = sp.factor(b.subs({X: Xright, M: -Mrad,", 1),
    ("bmin_left <= bmax < 0", "bmin_right <= bmax < 0", 1),
    ("Znew.subs({X: Xleft, S: Smax, M: -Mrad,",
     "Znew.subs({X: Xright, S: Smax, M: -Mrad,", 1),
    ("R(97261562093134873, 15857127000000000000)",
     "R(143889690210214873, 15857127000000000000)", 1),
    ("R(9, 13)-Xright**2+K*(Xright-Xanchor)",
     "R(9, 13)-Xleft**2+K*(Xleft-Xanchor)", 1),
    ("R(40307, 2600000)", "R(33258337711, 1081600000000)", 1),
    ("-R(434919, 17875)", "-R(8425123367, 286000000)", 1),
    ("R(2, 5)*(X-R(3, 13))-K*(X-Xanchor)-S*T",
     "R(2, 5)*(X-R(3, 13))-K*(Xleft-Xanchor)-S*T", 1),
    ("R(2, 5)*(Xright-R(3, 13))-K*(Xright-Xanchor)",
     "R(2, 5)*(Xleft-R(3, 13))-K*(Xleft-Xanchor)", 1),
    (
        "require(danger_base == R(109767, 650000) > 0,\n"
        "        \"strict full-cell danger lower bound\")",
        "require(danger_base == 0,\n"
        "        \"exact zero danger base at the seam\")\n"
        "danger_slope = sp.factor(-Tmax)\n"
        "require(danger_slope == R(8425123367, 286000000) > 0,\n"
        "        \"strict S-dependent danger at the seam\")\n"
        "danger_right_base = sp.factor(\n"
        "    R(2, 5)*(Xright-Xleft)\n"
        ")\n"
        "require(danger_right_base == R(9833, 2600000) > 0,\n"
        "        \"positive right-end danger base\")",
        1,
    ),
    ("print(\"DANGER_LOWER\", danger_base)",
     "print(\"DANGER_LOWER\", S*danger_slope)", 1),
)
for old, new, count in replacements:
    source = replace_exact(source, old, new, count)

# Add explicit definition-level seam checks before legality and controls.
splice_print = 'print("PASS exact old/new chart and raw-gate splice", flush=True)'
splice_extension = splice_print + r'''
Z_previous_seam = sp.factor(
    (Zold + K*(X-Xanchor)).subs(X, Xleft)
)
Z_constant_seam = sp.factor(Znew.subs(X, Xleft))
require(sp.factor(Z_previous_seam-Z_constant_seam) == 0,
        "old/new Z seam")
seam_common = {
    lam: A/S,
    x: xsheet.subs(X, Xleft),
    y: ysheet.subs(X, Xleft),
}
old_gate_seam = sp.factor((36*Gamma).subs({
    **seam_common, Z: Z_previous_seam,
}))
new_gate_seam = sp.factor((36*Gamma).subs({
    **seam_common, Z: Z_constant_seam,
}))
positive_clear = 25**8*A**8*S**3
require(sp.factor(sp.cancel(
    positive_clear*(old_gate_seam-new_gate_seam)
)) == 0, "cleared raw-gate seam")
require(sp.factor(sp.cancel(
    (positive_clear*old_gate_seam-first_layer)
    -(positive_clear*new_gate_seam-first_layer)
)) == 0, "cleared core seam")
print("PASS exact parameter/cleared-gate/cleared-core seam", flush=True)
'''
source = replace_exact(source, splice_print, splice_extension, 1)

# The frozen builder originally tests controls before legality.  This source
# moves the unchanged exact legality block ahead of the unchanged control
# block, so a chart failure cannot spend or contaminate the positivity gate.
control_marker = "# One exact Bernstein cell only."
legality_marker = "# Full-cell legality."
diagnostic_marker = "# Definition-level diagnostic nodes."
prefix, after_control = source.split(control_marker, 1)
control_body, after_legality = after_control.split(legality_marker, 1)
legality_body, diagnostic_body = after_legality.split(diagnostic_marker, 1)
source = (prefix + legality_marker + legality_body
          + control_marker + control_body
          + diagnostic_marker + diagnostic_body)

# Fail-closed source mutations strike independent proof layers.
if os.environ.get("INWARD_Z_CONSTANT_X99_100_DROP_Q2") == "1":
    source = replace_exact(source, "Q2 = sp.expand(Q*Q)",
                           "Q2 = sp.zeros(3, 3)", 1)
if os.environ.get("INWARD_Z_CONSTANT_X99_100_FLIP_DANGER") == "1":
    source = replace_exact(
        source,
        "danger_new = sp.factor(1-xsheet**2-ysheet**2-Znew)",
        "danger_new = sp.factor(-(1-xsheet**2-ysheet**2-Znew))",
        1,
    )
if os.environ.get("INWARD_Z_CONSTANT_X99_100_DROP_CORE") == "1":
    source = replace_exact(
        source,
        "if os.environ.get(\"INWARD_Z_CONSTANT_X99_100_DROP_TERM\") == \"1\":",
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
        "constant-lift X99/100 failed: weakest control is not unique: "
        f"{ties}"
    )
print("PASS unique weakest centered control", minimum_index, flush=True)
print("CHART Z_recentered - 2*(X-Xstar); exact seam-preserving constant lift",
      flush=True)
