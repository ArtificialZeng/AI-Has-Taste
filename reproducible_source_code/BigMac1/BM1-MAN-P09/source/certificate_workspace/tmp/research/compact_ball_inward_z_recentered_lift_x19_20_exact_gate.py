#!/usr/bin/env python3
"""Exact adjacent-cell gate for the recentered inward-Z lift to X=19/20.

This fail-closed source binds the independently audited X<=15/16 source and
referee artifacts, plus the frozen self-contained exact builder.  It applies
a deterministic multiplicity-checked specialization to the one and only new
cell 15/16 <= X <= 19/20.  The specialized body rebuilds the original
Hermitian Q, every entry of Q^2, and the fully conjugated raw gate before
testing splice, legality, exact controls, and rational diagnostic nodes.
It is a source candidate, not an independent referee.
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run with python -O")

from hashlib import sha256
from pathlib import Path
import os
import sys


if len(sys.argv) != 1:
    raise SystemExit("usage: recentered-lift X19/20 exact gate accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
BUILDER = "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_exact_gate.py"
PREDECESSOR = "tmp/research/compact_ball_inward_z_recentered_lift_x15_16_exact_gate.py"
DEPENDENCIES = {
    BUILDER:
        "33bad020143d4e4143b0742526b4fb0ba4d0089d1e12e8365ceca878577e0d2e",
    PREDECESSOR:
        "73b3fbbb5c4497fbb20cd0745478a736b17d36fb8d68294fb4eef0e7f1c1437a",
    "tmp/research/compact_ball_inward_z_recentered_lift_x15_16_source_freeze_manifest.sha256":
        "15861a8df55c795bd30e9b0bf43e50a36f7bd5819a06a47fa78a26b8541ad64a",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x15_16_independent_referee.py":
        "6c8168342d1a330e2566a86f458889bd59cc1315623a55977adc72b0f7daf934",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_RECENTERED_LIFT_X15_16_INDEPENDENT_REFEREE_AUDIT.md":
        "194a1c1e82b556b3c016da7244d4efd93297ec348ed479d4073b289d2541beed",
    "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x15_16_independent_referee_manifest.sha256":
        "1035e61afa5346eba9f4f2bae4b04807002730c92857e0103d9ab83d2fd6dfae",
}
if os.environ.get("INWARD_Z_X19_20_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[PREDECESSOR] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    if not path.is_file():
        raise RuntimeError(f"recentered-lift X19/20 failed: missing {relative}")
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(
            f"recentered-lift X19/20 failed: hash mismatch {relative}"
        )
print("PASS frozen X<=15/16 source/referee dependency hashes", flush=True)


def replace_exact(source, old, new, count):
    """Replace an audited token only when its multiplicity is exact."""
    actual = source.count(old)
    if actual != count:
        raise RuntimeError(
            "recentered-lift X19/20 failed: specialization multiplicity "
            f"{old!r}: expected {count}, got {actual}"
        )
    return source.replace(old, new)


source = (ROOT / BUILDER).read_text(encoding="utf-8")
replacements = (
    ("to X=7/8", "to X=19/20", 1),
    ("17/20 <= X <= 7/8", "15/16 <= X <= 19/20", 1),
    ("X7/8", "X19/20", 1),
    ("INWARD_Z_X7_8", "INWARD_Z_X19_20", 3),
    ("Xleft = R(17, 20)", "Xleft = R(15, 16)", 1),
    ("Xright = R(7, 8)", "Xright = R(19, 20)", 1),
    ("at X=17/20", "at X=15/16", 2),
    ("R(676699, 2750000)", "R(264199, 2750000)", 1),
    ("R(97261562093134873, 15857127000000000000)",
     "R(386655427244434873, 15857127000000000000)", 1),
    ("R(40307, 2600000)", "R(1163, 40625)", 1),
    ("-R(434919, 17875)", "-R(1588319, 57200)", 1),
    ("R(109767, 650000)", "R(31767, 650000)", 1),
)
for old, new, count in replacements:
    source = replace_exact(source, old, new, count)

namespace = {
    "__name__": "__main__",
    "__file__": str(Path(__file__).resolve()),
    "__builtins__": __builtins__,
}
exec(compile(source, str(Path(__file__).resolve()), "exec"), namespace)

# The source-side candidate additionally fails closed unless the weakest
# centered lower is unique.  The independent referee must reconstruct this
# fact without importing the candidate.
lower_table = namespace["lowers"]
minimum_index = namespace["minimum_index"]
reserve = namespace["reserve"]
ties = [key for key, value in lower_table.items() if value == reserve]
if ties != [minimum_index]:
    raise RuntimeError(
        "recentered-lift X19/20 failed: weakest control is not unique: "
        f"{ties}"
    )
print("PASS unique weakest centered control", minimum_index, flush=True)
