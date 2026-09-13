#!/usr/bin/env python3
"""Exact adjacent-cell gate for the recentered inward-Z lift to X=15/16.

This fail-closed source binds the independently audited X<=11/12 source and
referee artifacts, plus the frozen self-contained exact builder.  It applies
a deterministic multiplicity-checked specialization to the one and only new
cell 11/12 <= X <= 15/16.  The specialized body rebuilds the original
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
    raise SystemExit("usage: recentered-lift X15/16 exact gate accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
BUILDER = "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_exact_gate.py"
PREDECESSOR = "tmp/research/compact_ball_inward_z_recentered_lift_x11_12_exact_gate.py"
DEPENDENCIES = {
    BUILDER:
        "33bad020143d4e4143b0742526b4fb0ba4d0089d1e12e8365ceca878577e0d2e",
    PREDECESSOR:
        "fdbf6e078e7d6beb20a5243ddcf80c4a5534027aa9f82283d327cb2361593dfe",
    "tmp/research/compact_ball_inward_z_recentered_lift_x11_12_source_freeze_manifest.sha256":
        "60e1bc22a58ac6ddd8023a0c5e325b6856adf39935c1b6ec526c2b02c602c404",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x11_12_independent_referee.py":
        "2e48c1e37a6ee2063b4b497a998fbf77e13bc44db7c02980f357028d13634f40",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_RECENTERED_LIFT_X11_12_INDEPENDENT_REFEREE_AUDIT.md":
        "10df94f15a7709e90cdb254be1e7c57d4fff5ea53eb0d0b2439d730816e2d9ee",
    "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x11_12_independent_referee_manifest.sha256":
        "c8e96e96d1ce5da8aa91f1852383d04e78597f38086843387db4e9767c152f7e",
}
if os.environ.get("INWARD_Z_X15_16_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[PREDECESSOR] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    if not path.is_file():
        raise RuntimeError(f"recentered-lift X15/16 failed: missing {relative}")
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(
            f"recentered-lift X15/16 failed: hash mismatch {relative}"
        )
print("PASS frozen X<=11/12 source/referee dependency hashes", flush=True)


def replace_exact(source, old, new, count):
    """Replace an audited token only when its multiplicity is exact."""
    actual = source.count(old)
    if actual != count:
        raise RuntimeError(
            "recentered-lift X15/16 failed: specialization multiplicity "
            f"{old!r}: expected {count}, got {actual}"
        )
    return source.replace(old, new)


source = (ROOT / BUILDER).read_text(encoding="utf-8")
replacements = (
    ("to X=7/8", "to X=15/16", 1),
    ("17/20 <= X <= 7/8", "11/12 <= X <= 15/16", 1),
    ("X7/8", "X15/16", 1),
    ("INWARD_Z_X7_8", "INWARD_Z_X15_16", 3),
    ("Xleft = R(17, 20)", "Xleft = R(11, 12)", 1),
    ("Xright = R(7, 8)", "Xright = R(15, 16)", 1),
    ("at X=17/20", "at X=11/12", 2),
    ("R(676699, 2750000)", "R(332949, 2750000)", 1),
    ("R(97261562093134873, 15857127000000000000)",
     "R(339775913517934873, 15857127000000000000)", 1),
    ("R(40307, 2600000)", "R(283103, 10400000)", 1),
    ("-R(434919, 17875)", "-R(289034, 10725)", 1),
    ("R(109767, 650000)", "R(44767, 650000)", 1),
)
for old, new, count in replacements:
    source = replace_exact(source, old, new, count)

namespace = {
    "__name__": "__main__",
    "__file__": str(Path(__file__).resolve()),
    "__builtins__": __builtins__,
}
exec(compile(source, str(Path(__file__).resolve()), "exec"), namespace)
