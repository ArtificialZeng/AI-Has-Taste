#!/usr/bin/env python3
"""Fail-closed verifier for the adjacent-x source-freeze manifest."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PREFIX = "tmp/research/compact_ball_uncovered_box_x5_8_xy_adjacent_x627_1000"
MANIFEST = ROOT / f"{PREFIX}_source_freeze_manifest.sha256"
SOURCE_REL = f"{PREFIX}_exact_gate.py"
REQUIRED = {
    SOURCE_REL,
    f"{PREFIX}_normal.log",
    f"{PREFIX}_normal.exit",
    f"{PREFIX}_pycompile.log",
    f"{PREFIX}_pycompile.exit",
    f"{PREFIX}_fail_closed_test_record.md",
    "tmp/research/common_metric_ranktwo_transverse_compact_ball_"
    "uncovered_box_x5_8_xy_adjacent_x627_1000_source_candidate.md",
    "tmp/research/verify_compact_ball_uncovered_box_x5_8_xy_"
    "adjacent_x627_1000_source_freeze.py",
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    records: dict[str, str] = {}
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        expected, relative = line.split("  ", 1)
        if relative.startswith("/") or ".." in Path(relative).parts:
            raise AssertionError(f"unsafe manifest path: {relative}")
        if relative in records:
            raise AssertionError(f"duplicate manifest path: {relative}")
        records[relative] = expected

    if os.environ.get("XADJ_FREEZE_BAD_MANIFEST") == "1":
        records.pop(SOURCE_REL)
    if not REQUIRED.issubset(records):
        raise AssertionError(f"required manifest records missing: {REQUIRED - records.keys()}")

    for relative, expected in sorted(records.items()):
        if os.environ.get("XADJ_FREEZE_BAD_SOURCE_HASH") == "1" and relative == SOURCE_REL:
            expected = "0" * 64
        actual = digest(ROOT / relative)
        if actual != expected:
            raise AssertionError(f"manifest hash mismatch: {relative}")

    print(f"PASS adjacent-x source freeze manifest: {len(records)}/{len(records)}")


if __name__ == "__main__":
    main()
