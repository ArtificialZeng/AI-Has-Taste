#!/usr/bin/env python3
"""Exact adjacent-cell gate for the recentered inward-Z lift to X=9/10.

This fail-closed source binds the independently audited X<=7/8 source and
referee artifacts, then performs a deterministic source-to-source
specialization to the one and only new cell 7/8 <= X <= 9/10.  Executing the
specialized source rebuilds the original Hermitian Q, every entry of Q^2,
and the fully conjugated raw gate before testing splice, legality, centered
Bernstein controls, and exact rational diagnostic nodes.  It is a source
candidate, not an independent referee.
"""

if not __debug__:
    raise RuntimeError("fail closed: do not run with python -O")

from hashlib import sha256
from pathlib import Path
import os
import sys


if len(sys.argv) != 1:
    raise SystemExit("usage: recentered-lift X9/10 exact gate accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_exact_gate.py"
DEPENDENCIES = {
    PREDECESSOR:
        "33bad020143d4e4143b0742526b4fb0ba4d0089d1e12e8365ceca878577e0d2e",
    "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_source_freeze_manifest.sha256":
        "bf68bd1522118abb2d04fff5aeb70443b766250ade53702a9259eaeb88aa384b",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x7_8_independent_referee.py":
        "270a24bd0a3eaa2e68f4b831966b5e646c2cee7cdeca1ca917d2fb6ebd1b1f4c",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_RECENTERED_LIFT_X7_8_INDEPENDENT_REFEREE_AUDIT.md":
        "9405feb3acbc6512cc168f636563af627bd5ef9f9f4196c08a0fe2128de10430",
    "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x7_8_independent_referee_manifest.sha256":
        "bd6624479621d948b298f3f7243a1091dab0043bd744b9c425e5127007a5bc8f",
}
if os.environ.get("INWARD_Z_X9_10_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[PREDECESSOR] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    if not path.is_file():
        raise RuntimeError(f"recentered-lift X9/10 failed: missing {relative}")
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(
            f"recentered-lift X9/10 failed: hash mismatch {relative}"
        )
print("PASS frozen X<=7/8 source/referee dependency hashes", flush=True)


def replace_exact(source, old, new, count):
    """Replace an audited token only when its multiplicity is exact."""
    actual = source.count(old)
    if actual != count:
        raise RuntimeError(
            "recentered-lift X9/10 failed: specialization multiplicity "
            f"{old!r}: expected {count}, got {actual}"
        )
    return source.replace(old, new)


source = (ROOT / PREDECESSOR).read_text(encoding="utf-8")
replacements = (
    ("to X=7/8", "to X=9/10", 1),
    ("17/20 <= X <= 7/8", "7/8 <= X <= 9/10", 1),
    ("X7/8", "X9/10", 1),
    ("INWARD_Z_X7_8", "INWARD_Z_X9_10", 3),
    ("Xleft = R(17, 20)", "Xleft = R(7, 8)", 1),
    ("Xright = R(7, 8)", "Xright = R(9, 10)", 1),
    ("at X=17/20", "at X=7/8", 2),
    ("R(676699, 2750000)", "R(539199, 2750000)", 1),
    ("R(97261562093134873, 15857127000000000000)",
     "R(204722284502434873, 15857127000000000000)", 1),
    ("R(40307, 2600000)", "R(13733, 650000)", 1),
    ("-R(434919, 17875)", "-R(723953, 28600)", 1),
    ("R(109767, 650000)", "R(83767, 650000)", 1),
)
for old, new, count in replacements:
    source = replace_exact(source, old, new, count)

# The executed audited body sees this x9_10 file as __file__, so its printed
# SCRIPT_SHA256 byte-binds the present source rather than its predecessor.
namespace = {
    "__name__": "__main__",
    "__file__": str(Path(__file__).resolve()),
    "__builtins__": __builtins__,
}
exec(compile(source, str(Path(__file__).resolve()), "exec"), namespace)
