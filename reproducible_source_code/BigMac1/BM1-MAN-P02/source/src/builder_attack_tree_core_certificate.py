#!/usr/bin/env python3
"""Fail-closed attacks for the frozen ten-vertex tree-core certificate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def run_verifier(
    verifier: Path,
    certificate: Path,
    expected_sha256: str | None,
) -> dict[str, object]:
    command = [sys.executable, str(verifier), str(certificate)]
    if expected_sha256 is not None:
        command.extend(["--expected-sha256", expected_sha256])
    completed = subprocess.run(command, text=True, capture_output=True, check=False)
    combined = (completed.stdout + completed.stderr).strip()
    return {
        "returncode": completed.returncode,
        "rejected": completed.returncode != 0,
        "diagnostic_tail": combined[-1200:],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--verifier", type=Path, required=True)
    parser.add_argument("--expected-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    raw = args.certificate.read_bytes()
    actual_sha256 = hashlib.sha256(raw).hexdigest()
    if actual_sha256 != args.expected_sha256:
        raise ValueError("attack harness was given the wrong source hash")
    source = json.loads(raw)
    results: dict[str, dict[str, object]] = {}
    with tempfile.TemporaryDirectory(prefix="tree-core-attacks-") as directory:
        temporary = Path(directory)

        results["bad_source_hash"] = run_verifier(
            args.verifier,
            args.certificate,
            "0" * 64,
        )

        dropped = copy.deepcopy(source)
        dropped["records"].pop()
        drop_path = temporary / "drop_tree.json"
        drop_path.write_text(json.dumps(dropped, indent=2) + "\n", encoding="utf-8")
        results["drop_tree"] = run_verifier(args.verifier, drop_path, None)

        altered = copy.deepcopy(source)
        edges = altered["records"][0]["canonical_edge_list"]
        if not edges:
            raise AssertionError("first serialized tree unexpectedly has no edge")
        edges[0] = [0, 2] if edges[0] != [0, 2] else [0, 3]
        edge_path = temporary / "alter_edge_list.json"
        edge_path.write_text(json.dumps(altered, indent=2) + "\n", encoding="utf-8")
        results["alter_edge_list"] = run_verifier(args.verifier, edge_path, None)

        flipped = copy.deepcopy(source)
        nonsingular = next(record for record in flipped["records"] if not record["singular"])
        nonsingular["target_clique_found"] = True
        flip_path = temporary / "flip_target_result.json"
        flip_path.write_text(json.dumps(flipped, indent=2) + "\n", encoding="utf-8")
        results["flip_target_result"] = run_verifier(args.verifier, flip_path, None)

    if not all(result["rejected"] for result in results.values()):
        raise AssertionError("at least one fail-closed attack was accepted")
    payload = {
        "schema_version": 1,
        "frozen_source_sha256": actual_sha256,
        "all_attacks_rejected": True,
        "attacks": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
