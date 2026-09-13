#!/usr/bin/env python3
"""Exact recentered inward-Z gate to the rational danger-base root.

The single cell is

    39/40 <= X <= 1019767/1040000.

This fail-closed source binds the independently audited X<=39/40 result and
the exact X=1 endpoint preflight.  It specializes the frozen self-contained
definition-level builder, so the original fully conjugated Hermitian Q,Q^2
gate is rebuilt before splice, legality, controls, and diagnostics are tested.
It is a source candidate, not an independent referee result.
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run with python -O")

from hashlib import sha256
from pathlib import Path
import os
import sys


if len(sys.argv) != 1:
    raise SystemExit("usage: danger-root exact gate accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
BUILDER = "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_exact_gate.py"
PREDECESSOR = "tmp/research/compact_ball_inward_z_recentered_lift_x39_40_exact_gate.py"
PREFLIGHT = "tmp/research/compact_ball_inward_z_recentered_lift_x1_endpoint_preflight.py"
DEPENDENCIES = {
    BUILDER:
        "33bad020143d4e4143b0742526b4fb0ba4d0089d1e12e8365ceca878577e0d2e",
    PREDECESSOR:
        "fd2478e01760b932f1e331022b9719720e0a228170314920288fac433d307087",
    "tmp/research/compact_ball_inward_z_recentered_lift_x39_40_source_freeze_manifest.sha256":
        "517866298fbb674efbfc90c0b93cd6494a2bb4b26c5037f638ecafd63eb8852d",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x39_40_independent_referee.py":
        "b7b84114d358e65b8bc6f16419cfa3ffde1b0b32c1b58399712ac44d44ae58ba",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_RECENTERED_LIFT_X39_40_INDEPENDENT_REFEREE_AUDIT.md":
        "61536f6e9a4155ce456495eb6132ef244996b79dda0ef070dc0cb245ee82dbad",
    "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x39_40_independent_referee_manifest.sha256":
        "a5af10c556602ba6ad49ced87718805fbb1e5af0123f4191ce6266b3a460fd8d",
    PREFLIGHT:
        "b46081f52bf4af38c77a1da7ded7a8c1734169be85ca1eab84d221826fd8ba50",
    "tmp/research/compact_ball_inward_z_recentered_lift_x1_endpoint_preflight.log":
        "b1ee7b4b1b10970208224f0e68516fa8cd6aa430a9f4ae1a716c32ffd54635e7",
    "tmp/research/compact_ball_inward_z_recentered_lift_x1_endpoint_preflight.exit":
        "9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa",
}
if os.environ.get("INWARD_Z_DANGER_ROOT_BAD_SOURCE") == "1":
    DEPENDENCIES[BUILDER] = "0" * 64
if (os.environ.get("INWARD_Z_DANGER_ROOT_BAD_PREDECESSOR") == "1"
        or os.environ.get("INWARD_Z_DANGER_ROOT_BAD_DEPENDENCY") == "1"):
    DEPENDENCIES[PREDECESSOR] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    if not path.is_file():
        raise RuntimeError(f"danger-root gate failed: missing {relative}")
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(f"danger-root gate failed: hash mismatch {relative}")
print("PASS frozen X<=39/40 referee and X=1 preflight dependency hashes",
      flush=True)


def replace_exact(source, old, new, count):
    """Replace an audited token only when its multiplicity is exact."""
    actual = source.count(old)
    if actual != count:
        raise RuntimeError(
            "danger-root gate failed: specialization multiplicity "
            f"{old!r}: expected {count}, got {actual}"
        )
    return source.replace(old, new)


source = (ROOT / BUILDER).read_text(encoding="utf-8")
replacements = (
    ("to X=7/8", "to X=1019767/1040000", 1),
    ("17/20 <= X <= 7/8",
     "39/40 <= X <= 1019767/1040000", 1),
    ("X7/8", "XDANGERROOT", 1),
    ("INWARD_Z_X7_8", "INWARD_Z_DANGER_ROOT", 3),
    ("Xleft = R(17, 20)", "Xleft = R(39, 40)", 1),
    ("Xright = R(7, 8)", "Xright = R(1019767, 1040000)", 1),
    ("at X=17/20", "at X=39/40", 2),
    ("R(676699, 2750000)", "R(5002423, 143000000)", 1),
    ("R(97261562093134873, 15857127000000000000)",
     "R(436351086639634873, 15857127000000000000)", 1),
    ("R(40307, 2600000)", "R(33258337711, 1081600000000)", 1),
    ("-R(434919, 17875)", "-R(4181417, 143000)", 1),
    (
        "require(danger_base == R(109767, 650000) > 0,\n"
        "        \"strict full-cell danger lower bound\")",
        "require(danger_base == 0,\n"
        "        \"exact rational danger-base endpoint\")\n"
        "danger_slope = sp.factor(-Tmax)\n"
        "require(danger_slope > 0,\n"
        "        \"strict S-dependent full-cell danger lower bound\")",
        1,
    ),
    ("print(\"DANGER_LOWER\", danger_base)",
     "print(\"DANGER_LOWER\", S*danger_slope)", 1),
)
for old, new, count in replacements:
    source = replace_exact(source, old, new, count)

# Source-level mutation hooks used only by the frozen fail-closed attack
# matrix.  Each mutation strikes a different proof layer and must be rejected
# by a substantive identity/check in the specialized builder.
if os.environ.get("INWARD_Z_DANGER_ROOT_DROP_Q2") == "1":
    source = replace_exact(source, "Q2 = sp.expand(Q*Q)",
                           "Q2 = sp.zeros(3, 3)", 1)
if os.environ.get("INWARD_Z_DANGER_ROOT_FLIP_DANGER") == "1":
    source = replace_exact(
        source,
        "danger_new = sp.factor(1-xsheet**2-ysheet**2-Znew)",
        "danger_new = sp.factor(-(1-xsheet**2-ysheet**2-Znew))",
        1,
    )
if os.environ.get("INWARD_Z_DANGER_ROOT_DROP_CORE") == "1":
    source = replace_exact(
        source,
        "if os.environ.get(\"INWARD_Z_DANGER_ROOT_DROP_TERM\") == \"1\":",
        "if True:",
        1,
    )

namespace = {
    "__name__": "__main__",
    "__file__": str(Path(__file__).resolve()),
    "__builtins__": __builtins__,
}
exec(compile(source, str(Path(__file__).resolve()), "exec"), namespace)

# Make uniqueness part of the final source bytes, not an inference from log
# ordering.  Preserve the entire weakest polynomial printed by the builder.
lower_table = namespace["lowers"]
minimum_index = namespace["minimum_index"]
reserve = namespace["reserve"]
ties = [key for key, value in lower_table.items() if value == reserve]
if ties != [minimum_index]:
    raise RuntimeError(
        "danger-root gate failed: weakest control is not unique: "
        f"{ties}"
    )
print("PASS unique weakest centered control", minimum_index, flush=True)

# Bind the X=1 chart obstruction as provenance and verify its exact witness
# again from the reconstructed chart.  This is not a raw-gate negative and
# receives no counterexample identifier.
sp, R = namespace["sp"], namespace["R"]
S, X = namespace["S"], namespace["X"]
M, omega, nu = namespace["M"], namespace["omega"], namespace["nu"]
danger_new, Znew = namespace["danger_new"], namespace["Znew"]
witness = {X: R(1), S: R(1, 1000000), M: R(0),
           omega: R(0), nu: R(0)}
witness_danger = sp.factor(danger_new.subs(witness))
witness_Z = sp.factor(Znew.subs(witness))
if witness_danger != -R(555866869, 17875000000):
    raise RuntimeError("danger-root gate failed: X=1 obstruction drift")
if witness_Z != R(173705179061213, 5585937500000000):
    raise RuntimeError("danger-root gate failed: X=1 witness Z drift")
print("PASS exact X=1 chart-obstruction provenance; no raw-gate claim",
      flush=True)
