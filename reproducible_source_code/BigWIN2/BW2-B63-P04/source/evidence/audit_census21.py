#!/usr/bin/env python3
"""Deterministic integrity/uniqueness audit for the order-21 census."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


EXPECTED = 2_144_505


def sha256(path: Path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main():
    root = Path(__file__).resolve().parent / "census21"
    state_path = root / "state.json"
    chunks_path = root / "chunks.jsonl"
    codes_path = root / "canonical.u64"
    state = json.loads(state_path.read_text())
    chunks = [json.loads(line) for line in chunks_path.read_text().splitlines()]

    assert state["order"] == 21
    assert state["complete"] is True and state["next_layout"] is None
    assert state["count"] == EXPECTED
    assert state["chunks"] == len(chunks)
    cursor = 1
    strict_stable = regular_unstable = singular = 0
    for expected_chunk, chunk in enumerate(chunks):
        assert chunk["chunk"] == expected_chunk
        assert chunk["first_index"] == cursor
        assert chunk["last_index"] == cursor + chunk["count"] - 1
        cursor = chunk["last_index"] + 1
        strict_stable += chunk["strict_stable"]
        regular_unstable += chunk["regular_unstable"]
        singular += chunk["singular"]
    assert cursor - 1 == EXPECTED
    assert strict_stable == EXPECTED and regular_unstable == singular == 0
    assert not (root / "suspects.jsonl").exists()

    codes = np.fromfile(codes_path, dtype="<u8")
    assert len(codes) == EXPECTED
    codes.sort()
    duplicate_positions = np.flatnonzero(codes[1:] == codes[:-1])
    assert len(duplicate_positions) == 0
    sorted_digest = hashlib.sha256(codes.astype("<u8", copy=False).tobytes()).hexdigest()

    report = {
        "audit": "order-21 census integrity and exact canonical-code uniqueness",
        "complete": True,
        "expected_and_observed_count": EXPECTED,
        "chunk_count": len(chunks),
        "contiguous_indices": True,
        "strict_stable_regular_routh": strict_stable,
        "regular_unstable": regular_unstable,
        "singular_routh": singular,
        "canonical_codes": len(codes),
        "distinct_canonical_codes": len(codes),
        "duplicate_canonical_codes": 0,
        "canonical_u64_sha256": sha256(codes_path),
        "canonical_sorted_u64_sha256": sorted_digest,
        "chunks_jsonl_sha256": sha256(chunks_path),
        "state_json_sha256": sha256(state_path),
        "census_program_sha256": sha256(Path(__file__).resolve().parent / "census21.py"),
    }
    output = root / "audit.json"
    output.write_text(json.dumps(report, sort_keys=True, indent=2) + "\n")
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
