#!/usr/bin/env python3
"""Exact adjacent-cell gate for the recentered inward-Z lift to X=11/12.

This fail-closed source binds the independently audited X<=9/10 source and
referee artifacts, plus the frozen self-contained exact builder.  It applies
a deterministic multiplicity-checked specialization to the one and only new
cell 9/10 <= X <= 11/12.  The specialized body rebuilds the original
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
    raise SystemExit("usage: recentered-lift X11/12 exact gate accepts no arguments")

ROOT = Path(__file__).resolve().parents[2]
BUILDER = "tmp/research/compact_ball_inward_z_recentered_lift_x7_8_exact_gate.py"
PREDECESSOR = "tmp/research/compact_ball_inward_z_recentered_lift_x9_10_exact_gate.py"
DEPENDENCIES = {
    BUILDER:
        "33bad020143d4e4143b0742526b4fb0ba4d0089d1e12e8365ceca878577e0d2e",
    PREDECESSOR:
        "dd4eb36ae2fa6852beb9892bfacb342b34e74e34d7ccc0b0b9d8f841a97c968f",
    "tmp/research/compact_ball_inward_z_recentered_lift_x9_10_source_freeze_manifest.sha256":
        "f581e2de74db2e6f34a7a2a9e7682572f93a24ef87e4534886362be5ad2fc7ff",
    "tmp/research/audit/verify_common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x9_10_independent_referee.py":
        "042367f84df57db758088dde4526320ab598c016c1dc6f2c3bf75bf5a6d629ab",
    "audit/COMMON_METRIC_RANKTWO_TRANSVERSE_COMPACT_BALL_INWARD_Z_RECENTERED_LIFT_X9_10_INDEPENDENT_REFEREE_AUDIT.md":
        "9e0b17cb62a6332fb39acc0984855481e3131c3d16ec0dd116342007baf316ac",
    "tmp/research/audit/common_metric_ranktwo_transverse_compact_ball_inward_z_recentered_lift_x9_10_independent_referee_manifest.sha256":
        "e0bcd3d53f4b84fafe3322d33e4b3c8e4cbeb43890b33d6b4bace5fa054aa1e0",
}
if os.environ.get("INWARD_Z_X11_12_BAD_DEPENDENCY") == "1":
    DEPENDENCIES[PREDECESSOR] = "0" * 64

for relative, expected in DEPENDENCIES.items():
    path = ROOT / relative
    if not path.is_file():
        raise RuntimeError(f"recentered-lift X11/12 failed: missing {relative}")
    actual = sha256(path.read_bytes()).hexdigest()
    if actual != expected:
        raise RuntimeError(
            f"recentered-lift X11/12 failed: hash mismatch {relative}"
        )
print("PASS frozen X<=9/10 source/referee dependency hashes", flush=True)


def replace_exact(source, old, new, count):
    """Replace an audited token only when its multiplicity is exact."""
    actual = source.count(old)
    if actual != count:
        raise RuntimeError(
            "recentered-lift X11/12 failed: specialization multiplicity "
            f"{old!r}: expected {count}, got {actual}"
        )
    return source.replace(old, new)


source = (ROOT / BUILDER).read_text(encoding="utf-8")
replacements = (
    ("to X=7/8", "to X=11/12", 1),
    ("17/20 <= X <= 7/8", "9/10 <= X <= 11/12", 1),
    ("X7/8", "X11/12", 1),
    ("INWARD_Z_X7_8", "INWARD_Z_X11_12", 3),
    ("Xleft = R(17, 20)", "Xleft = R(9, 10)", 1),
    ("Xright = R(7, 8)", "Xright = R(11, 12)", 1),
    ("at X=17/20", "at X=9/10", 2),
    ("R(676699, 2750000)", "R(1342597, 8250000)", 1),
    ("R(97261562093134873, 15857127000000000000)",
     "R(292361598161734873, 15857127000000000000)", 1),
    ("R(40307, 2600000)", "R(8842, 365625)", 1),
    ("-R(434919, 17875)", "-R(1880089, 71500)", 1),
    ("R(109767, 650000)", "R(199301, 1950000)", 1),
)
for old, new, count in replacements:
    source = replace_exact(source, old, new, count)

namespace = {
    "__name__": "__main__",
    "__file__": str(Path(__file__).resolve()),
    "__builtins__": __builtins__,
}
exec(compile(source, str(Path(__file__).resolve()), "exec"), namespace)
