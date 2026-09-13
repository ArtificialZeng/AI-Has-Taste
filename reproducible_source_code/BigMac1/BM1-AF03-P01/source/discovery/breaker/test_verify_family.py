#!/usr/bin/env python3
"""Adversarial rejection tests for the standalone literal-family checker."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile


HERE = Path(__file__).resolve().parent


def invoke(document: object) -> subprocess.CompletedProcess[str]:
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "input.json"
        path.write_text(json.dumps(document) + "\n", encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(HERE / "verify_family.py"), str(path)],
            check=False,
            text=True,
            encoding="utf-8",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )


def main() -> int:
    valid_path = HERE / "n8_literal_family.json"
    valid = subprocess.run(
        [sys.executable, str(HERE / "verify_family.py"), str(valid_path)],
        check=False,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if valid.returncode != 0 or "VERIFIED_LITERAL_COUNTEREXAMPLE" not in valid.stdout:
        raise SystemExit("valid positive-control family was rejected")

    rejected = {
        "missing_key": {"n": 8},
        "unordered_edge": {"n": 8, "family": [[2, 1, 3, 4]]},
        "duplicate_edge": {
            "n": 8,
            "family": [[1, 2, 3, 4], [1, 2, 3, 4]],
        },
        "disjoint_pair": {
            "n": 8,
            "family": [[1, 2, 3, 4], [5, 6, 7, 8]],
        },
        "degree_failure": {"n": 8, "family": [[1, 2, 3, 4]]},
    }
    for name, document in rejected.items():
        result = invoke(document)
        if result.returncode == 0 or not result.stderr.startswith("REJECTED:"):
            raise SystemExit(f"mutation {name} was not rejected fail-closed")
    print(
        json.dumps(
            {
                "status": "PASS",
                "accepted": 1,
                "rejected_mutations": sorted(rejected),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
