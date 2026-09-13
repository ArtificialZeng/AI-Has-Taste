#!/usr/bin/env python3
"""Fail-closed attacks for the ten-vertex unicyclic-core certificate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run_verifier(verifier: Path, source: Path, expected_hash: str, output: Path) -> dict[str, object]:
    command = [
        sys.executable,
        str(verifier),
        "--source",
        str(source),
        "--expected-source-sha256",
        expected_hash,
        "--output",
        str(output),
    ]
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    combined = (completed.stdout + completed.stderr).strip()
    return {
        "returncode": completed.returncode,
        "rejected": completed.returncode != 0,
        "diagnostic_tail": combined[-1200:],
    }


def write_case(directory: Path, name: str, payload: object) -> Path:
    path = directory / f"{name}.json"
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    return path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--verifier", type=Path, required=True)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    actual = digest(args.certificate)
    if actual != args.expected_sha256:
        raise ValueError("attack harness received the wrong frozen source hash")
    source = json.loads(args.certificate.read_text(encoding="utf-8"))
    results = {}
    with tempfile.TemporaryDirectory(prefix="unicyclic-core-attacks-") as raw_directory:
        directory = Path(raw_directory)
        results["bad_source_hash"] = run_verifier(
            args.verifier,
            args.certificate,
            "0" * 64,
            directory / "bad_hash_output.json",
        )

        dropped = copy.deepcopy(source)
        dropped["records"].pop()
        path = write_case(directory, "drop_record", dropped)
        results["drop_record"] = run_verifier(
            args.verifier, path, digest(path), directory / "drop_output.json"
        )

        altered = copy.deepcopy(source)
        edges = altered["records"][0]["canonical_edge_list"]
        edges[0] = [0, 2] if edges[0] != [0, 2] else [0, 3]
        path = write_case(directory, "alter_edge", altered)
        results["alter_edge_list"] = run_verifier(
            args.verifier, path, digest(path), directory / "edge_output.json"
        )

        incomplete = copy.deepcopy(source)
        incomplete["exact_search_enabled"] = False
        path = write_case(directory, "disable_exact", incomplete)
        results["disable_exact_search"] = run_verifier(
            args.verifier, path, digest(path), directory / "exact_output.json"
        )

        flipped = copy.deepcopy(source)
        flipped["counterexample_candidate_found"] = True
        path = write_case(directory, "flip_conclusion", flipped)
        results["flip_top_level_conclusion"] = run_verifier(
            args.verifier, path, digest(path), directory / "flip_output.json"
        )

    if not all(result["rejected"] for result in results.values()):
        raise AssertionError("at least one corrupted certificate was accepted")
    payload = {
        "schema_version": 1,
        "frozen_source_sha256": actual,
        "all_attacks_rejected": True,
        "attacks": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
