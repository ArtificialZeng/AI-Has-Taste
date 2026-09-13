#!/usr/bin/env python3
"""Positive and mutation-rejection tests for breaker_star4_verify.py."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import subprocess
import sys
import tempfile
from pathlib import Path


def invoke(verifier: Path, certificate: Path):
    return subprocess.run(
        [sys.executable, str(verifier), str(certificate)],
        check=False,
        capture_output=True,
        text=True,
        stdin=subprocess.DEVNULL,
        timeout=360,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    verifier = root / "src/breaker_star4_verify.py"
    certificate = root / "results/breaker_star4_certificate.json"
    source = json.loads(certificate.read_text(encoding="utf-8"))
    tests = []
    valid = invoke(verifier, certificate)
    tests.append(
        {
            "name": "valid_certificate",
            "expected": "accept",
            "returncode": valid.returncode,
            "output": valid.stdout.strip()[:1200],
        }
    )
    mutations = []
    changed = json.loads(json.dumps(source))
    changed["high_pairs"][3] = [1, 4]
    mutations.append(("changed_chamber_edge", changed))
    changed = json.loads(json.dumps(source))
    changed["expected_saturated_vector_dimension"] = 47
    mutations.append(("changed_vector_dimension", changed))
    changed = json.loads(json.dumps(source))
    changed["ideal_consequences"]["h23"] = "(a2-1)*(a2-a3)"
    mutations.append(("weakened_ideal_consequence", changed))
    changed = json.loads(json.dumps(source))
    changed["sturm_sequence_primitive_degree_descending"][3][0] = -4
    mutations.append(("changed_sturm_entry", changed))
    changed = json.loads(json.dumps(source))
    del changed["conclusion"]
    mutations.append(("missing_conclusion", changed))
    with tempfile.TemporaryDirectory(prefix="star4-mutations-") as directory:
        for name, data in mutations:
            path = Path(directory) / f"{name}.json"
            path.write_text(json.dumps(data), encoding="utf-8")
            result = invoke(verifier, path)
            tests.append(
                {
                    "name": name,
                    "expected": "reject",
                    "returncode": result.returncode,
                    "message": (result.stderr or result.stdout).strip()[:180],
                }
            )
    passed = all(
        row["returncode"] == 0 if row["expected"] == "accept" else row["returncode"] != 0
        for row in tests
    )
    payload = {
        "status": "PASS" if passed else "FAIL",
        "python": platform.python_version(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "tests": tests,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
