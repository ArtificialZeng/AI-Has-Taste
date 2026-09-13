#!/usr/bin/env python3
"""Run both exhaustive enumerators and compare their decisive exact data."""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys


HERE = Path(__file__).resolve().parent
SCRIPTS = (HERE / "enumerate_balanced.py", HERE / "enumerate_replay.py")


def digest_bytes(data: bytes) -> str:
    return sha256(data).hexdigest()


def canonical_survivors(result: dict[str, object]) -> bytes:
    records = result["all_degree_survivors"]
    assert isinstance(records, list)
    records = sorted(records, key=lambda item: item["successor"])
    return json.dumps(records, sort_keys=True, separators=(",", ":")).encode()


def run(path: Path) -> tuple[dict[str, object], bytes]:
    completed = subprocess.run(
        [sys.executable, str(path)],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.stderr:
        raise RuntimeError(completed.stderr.decode())
    return json.loads(completed.stdout), completed.stdout


def main() -> None:
    first, first_raw = run(SCRIPTS[0])
    second, second_raw = run(SCRIPTS[1])
    keys = (
        "counts",
        "cycle_type_histogram_for_degree_survivors",
        "hamilton_colour_histogram",
        "lexicographically_minimal_target_successor",
        "lexicographically_minimal_target_cycle_from_zero",
        "source_sha256",
        "problem_sha256",
    )
    for key in keys:
        if first[key] != second[key]:
            raise AssertionError((key, first[key], second[key]))
    first_survivors = canonical_survivors(first)
    second_survivors = canonical_survivors(second)
    if first_survivors != second_survivors:
        raise AssertionError("the degree-survivor sets differ")

    result = {
        "crosscheck": "pass",
        "python_executable": sys.executable,
        "enumerator_sha256": {
            path.name: digest_bytes(path.read_bytes()) for path in SCRIPTS
        },
        "raw_output_sha256": {
            SCRIPTS[0].name: digest_bytes(first_raw),
            SCRIPTS[1].name: digest_bytes(second_raw),
        },
        "agreed_counts": first["counts"],
        "agreed_cycle_type_histogram": first[
            "cycle_type_histogram_for_degree_survivors"
        ],
        "canonical_degree_survivors_sha256": digest_bytes(first_survivors),
        "degree_survivor_count": len(first["all_degree_survivors"]),
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
