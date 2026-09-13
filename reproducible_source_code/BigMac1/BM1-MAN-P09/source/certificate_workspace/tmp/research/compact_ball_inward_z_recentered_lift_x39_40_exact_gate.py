#!/usr/bin/env python3
"""Exact adjacent-cell gate for the recentered inward-Z lift to X=39/40.

This fail-closed source binds the independently audited X<=19/20 source and
referee artifacts, plus the frozen self-contained exact builder.  It applies
a deterministic multiplicity-checked specialization to the one and only new
cell 19/20 <= X <= 39/40.  The specialized body rebuilds the original
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
    raise SystemExit("usage: recentered-lift X39/40 exact gate accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
BUILDER = "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_exact_gate.py"
PREDECESSOR = "tmp/research/compact_ball_inward_z_recentered_lift_x19_20_exact_gate.py"
DEPENDENCIES = {
    BUILDER:
        "33bad020143d4e4143b0742526b4fb0ba4d0089d1e12e8365ceca878577e0d2e",
    PREDECESSOR:
        "a3097867b0e8a6644c13306e6b3c146839af2f1f0599f326294fee2b0aff355e",
    "tmp/research/compact_ball_inward_z_recentered_lift_x19_20_source_freeze_manifest.sha256":
        "32d9b3639ceddc0c5c76cf985df9a8d4e1ffae4c968d967c354408f23bbca34d",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x19_20_independent_referee.py":
        "6be12ce4210e72ad321774674b577bbdd133638cee9664824da698e274a6f82a",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_RECENTERED_LIFT_X19_20_INDEPENDENT_REFEREE_AUDIT.md":
        "829b5386955b1c620d793480ee780b537c579c5547bd2518347c27d7fc62005d",
    "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x19_20_independent_referee_manifest.sha256":
        "a375007f0f0bd110cd11c524f7aa74ff6892cc0127a21a032b2b0fa7a7855265",
}
if os.environ.get("INWARD_Z_X39_40_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[PREDECESSOR] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    if not path.is_file():
        raise RuntimeError(f"recentered-lift X39/40 failed: missing {relative}")
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(
            f"recentered-lift X39/40 failed: hash mismatch {relative}"
        )
print("PASS frozen X<=19/20 source/referee dependency hashes", flush=True)


def replace_exact(source, old, new, count):
    """Replace an audited token only when its multiplicity is exact."""
    actual = source.count(old)
    if actual != count:
        raise RuntimeError(
            "recentered-lift X39/40 failed: specialization multiplicity "
            f"{old!r}: expected {count}, got {actual}"
        )
    return source.replace(old, new)


source = (ROOT / BUILDER).read_text(encoding="utf-8")
replacements = (
    ("to X=7/8", "to X=39/40", 1),
    ("17/20 <= X <= 7/8", "19/20 <= X <= 39/40", 1),
    ("X7/8", "X39/40", 1),
    ("INWARD_Z_X7_8", "INWARD_Z_X39_40", 3),
    ("Xleft = R(17, 20)", "Xleft = R(19, 20)", 1),
    ("Xright = R(7, 8)", "Xright = R(39, 40)", 1),
    ("at X=17/20", "at X=19/20", 2),
    ("R(676699, 2750000)", "R(126699, 2750000)", 1),
    ("R(97261562093134873, 15857127000000000000)",
     "R(408175999230334873, 15857127000000000000)", 1),
    ("R(40307, 2600000)", "R(79307, 2600000)", 1),
    ("-R(434919, 17875)", "-R(91841, 3250)", 1),
    ("R(109767, 650000)", "R(5767, 650000)", 1),
)
for old, new, count in replacements:
    source = replace_exact(source, old, new, count)

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
        "recentered-lift X39/40 failed: weakest control is not unique: "
        f"{ties}"
    )
print("PASS unique weakest centered control", minimum_index, flush=True)
