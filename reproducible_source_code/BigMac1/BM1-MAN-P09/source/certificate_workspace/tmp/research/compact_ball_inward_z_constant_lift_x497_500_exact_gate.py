#!/usr/bin/env python3
"""Exact constant-Z lift cell on 99/100 <= X <= 497/500.

The independently audited predecessor uses

    Z_constant = Z_old + 2 (Xstar-Xanchor),
    Xstar = 1019767/1040000,

through X=99/100.  This source keeps exactly the same chart and treats the
single adjacent strict rational cell 99/100 <= X <= 497/500.  It binds the
predecessor and the exact X=1 chart-obstruction preflight, rebuilds the
original fully conjugated Hermitian Q,Q^2 gate, checks the three seam layers
and full legality before constructing the 40-control certificate.  It is a
source candidate, not an independent referee result.
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run with python -O")

from hashlib import sha256
from pathlib import Path
import os
import sys


if len(sys.argv) != 1:
    raise SystemExit("usage: constant-lift X497/500 exact gate accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
BUILDER = "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_exact_gate.py"
PREDECESSOR = "tmp/research/compact_ball_inward_z_constant_lift_x99_100_exact_gate.py"
DEPENDENCIES = {
    BUILDER:
        "33bad020143d4e4143b0742526b4fb0ba4d0089d1e12e8365ceca878577e0d2e",
    PREDECESSOR:
        "a99072346ca9d92e3a5e45600d1de371b2609185bef60b2c069d2a400e1d9322",
    "tmp/research/compact_ball_inward_z_constant_lift_x99_100_source_freeze_manifest.sha256":
        "e573ff4ab4ab1f2065ff6c40289aacd19e8629e3bbe53b177cd996c7624d7840",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_constant_lift_x99_100_independent_referee.py":
        "4958ec0eaca83cb06b8a368b94767dd32b826094e8e99fac3b34118aa19083e3",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_CONSTANT_LIFT_X99_100_INDEPENDENT_REFEREE_AUDIT.md":
        "cdf21533b5b1e921d28b4ed3d7c70ea0664356b99380469bfb7fa9609df8c12f",
    "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_constant_lift_x99_100_independent_referee_manifest.sha256":
        "378f98ff3d854f6d013d1578c8657cfa6a27502a631f1dd052f2207fd62266b3",
    "tmp/research/compact_ball_inward_z_constant_lift_x1_endpoint_preflight.py":
        "18fbd9ab9937b9700db7ad87e3c1edefaec76f8657c750606452f9a9f7e393bb",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_inward_z_constant_lift_x1_endpoint_preflight.md":
        "65e3f94346aa9898d0dcafb00eb178a332e4dba1451ac7f5c4f3301c0b5ff738",
    "tmp/research/compact_ball_inward_z_constant_lift_x1_endpoint_preflight.txt":
        "2e5d3cda52bf28388ce89b229705bd2bd3b657811146f4c059060759b353c13e",
    "tmp/research/compact_ball_inward_z_constant_lift_x1_endpoint_preflight.exit":
        "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
    "tmp/research/compact_ball_inward_z_constant_lift_x1_endpoint_preflight_manifest.sha256":
        "128cbea09b378a24e4a60997695bad51c66118f63da5b645857e270f878c5533",
}
if os.environ.get("INWARD_Z_CONSTANT_X497_500_BAD_SOURCE") == "1":
    DEPENDENCIES[BUILDER] = "0" * 64
if os.environ.get("INWARD_Z_CONSTANT_X497_500_BAD_PREDECESSOR") == "1":
    DEPENDENCIES[PREDECESSOR] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    if not path.is_file():
        raise RuntimeError(f"constant-lift X497/500 failed: missing {relative}")
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(f"constant-lift X497/500 failed: hash mismatch {relative}")
print("PASS frozen X99/100 source/referee and X=1 preflight hashes", flush=True)


def replace_exact(source, old, new, count):
    actual = source.count(old)
    if actual != count:
        raise RuntimeError(
            "constant-lift X497/500 failed: specialization multiplicity "
            f"{old!r}: expected {count}, got {actual}"
        )
    return source.replace(old, new)


source = (ROOT / BUILDER).read_text(encoding="utf-8")
replacements = (
    ("to X=7/8", "to X=497/500 on the constant lift", 1),
    ("17/20 <= X <= 7/8", "99/100 <= X <= 497/500", 1),
    ("X7/8", "X497/500-CONSTANT", 1),
    ("INWARD_Z_X7_8", "INWARD_Z_CONSTANT_X497_500", 3),
    ("Xleft = R(17, 20)", "Xleft = R(99, 100)", 1),
    ("Xright = R(7, 8)", "Xright = R(497, 500)", 1),
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
        "require(Zderivative_lower == -R(5477801, 2750000)\n"
        "        and Zderivative_upper == -R(99, 50) < 0,\n"
        "        \"Z decreases on the full cell\")",
        1,
    ),
    ("bmin_left = sp.factor(b.subs({X: Xleft, M: -Mrad,",
     "bmin_right = sp.factor(b.subs({X: Xright, M: -Mrad,", 1),
    ("bmin_left <= bmax < 0", "bmin_right <= bmax < 0", 1),
    ("Znew.subs({X: Xleft, S: Smax, M: -Mrad,",
     "Znew.subs({X: Xright, S: Smax, M: -Mrad,", 1),
    ("R(97261562093134873, 15857127000000000000)",
     "R(17798406223702873, 15857127000000000000)", 1),
    ("R(9, 13)-Xright**2+K*(Xright-Xanchor)",
     "R(9, 13)-Xleft**2+K*(Xstar-Xanchor)", 1),
    ("R(40307, 2600000)", "R(31507, 2600000)", 1),
    ("-R(434919, 17875)", "-R(5332081, 178750)", 1),
    ("R(2, 5)*(X-R(3, 13))-K*(X-Xanchor)-S*T",
     "R(2, 5)*(X-R(3, 13))-K*(Xstar-Xanchor)-S*T", 1),
    ("R(2, 5)*(Xright-R(3, 13))-K*(Xright-Xanchor)",
     "R(2, 5)*(Xleft-R(3, 13))-K*(Xstar-Xanchor)", 1),
    (
        "require(danger_base == R(109767, 650000) > 0,\n"
        "        \"strict full-cell danger lower bound\")",
        "require(danger_base == R(9833, 2600000) > 0,\n"
        "        \"strict full-cell danger lower bound\")\n"
        "danger_right_base = sp.factor(\n"
        "    R(2, 5)*(Xright-R(3, 13))-K*(Xstar-Xanchor)\n"
        ")\n"
        "require(danger_right_base == R(13993, 2600000) > danger_base,\n"
        "        \"positive right-end danger base\")",
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
Z_constant_seam = sp.factor(Znew.subs(X, Xleft))
require(sp.factor(Z_previous_seam-Z_constant_seam) == 0,
        "constant chart seam")
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
print("PASS exact X=99/100 parameter/cleared-gate/cleared-core seam", flush=True)
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
source = (prefix + legality_marker + legality_body
          + control_marker + control_body
          + diagnostic_marker + diagnostic_body)

# Fail-closed source mutations strike independent proof layers.
if os.environ.get("INWARD_Z_CONSTANT_X497_500_DROP_Q2") == "1":
    source = replace_exact(source, "Q2 = sp.expand(Q*Q)",
                           "Q2 = sp.zeros(3, 3)", 1)
if os.environ.get("INWARD_Z_CONSTANT_X497_500_FLIP_DANGER") == "1":
    source = replace_exact(
        source,
        "danger_new = sp.factor(1-xsheet**2-ysheet**2-Znew)",
        "danger_new = sp.factor(-(1-xsheet**2-ysheet**2-Znew))",
        1,
    )
if os.environ.get("INWARD_Z_CONSTANT_X497_500_DROP_CORE") == "1":
    source = replace_exact(
        source,
        "if os.environ.get(\"INWARD_Z_CONSTANT_X497_500_DROP_TERM\") == \"1\":",
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
        "constant-lift X497/500 failed: weakest control is not unique: "
        f"{ties}"
    )
print("PASS unique weakest centered control", minimum_index, flush=True)
print("CHART Z_old + 2*(Xstar-Xanchor); constant seam-preserving lift",
      flush=True)
print("ROOT_BRACKET 497/500 < positive chart root < 199/200", flush=True)
print("RESULT exact source candidate on one strict rational constant-lift cell",
      flush=True)
print("CLASSIFICATION proof candidate; no chart illegality and no raw-gate negative",
      flush=True)
print("SCOPE one adjacent local cell only; no endpoint maximality; full compact ball/common metric/arbitrary-node/fixed-lens open",
      flush=True)
