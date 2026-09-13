#!/usr/bin/env python3
"""Positive and corruption tests for the independent D_9 verifier."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
VERIFIER = ROOT / "certificates" / "verify_d9_flow.py"
CERTIFICATE = ROOT / "certificates" / "d9_normalized_flow.json"
D4_CERTIFICATE = ROOT / "certificates" / "d4_baseline_flow.json"


def run(path: Path, expected_n: int = 9) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(VERIFIER), "--expected-n", str(expected_n), str(path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
    )


def main() -> int:
    valid = run(CERTIFICATE)
    if valid.returncode != 0 or '"result": "VERIFIED"' not in valid.stdout:
        raise AssertionError(f"valid certificate failed: {valid.stdout} {valid.stderr}")
    valid_d4 = run(D4_CERTIFICATE, expected_n=4)
    if valid_d4.returncode != 0 or '"endpoint": "Abs(D_4) normalized flow"' not in valid_d4.stdout:
        raise AssertionError(f"valid D4 baseline failed: {valid_d4.stdout} {valid_d4.stderr}")
    wrong_endpoint = run(D4_CERTIFICATE, expected_n=9)
    if wrong_endpoint.returncode == 0 or "REJECTED:" not in wrong_endpoint.stderr:
        raise AssertionError("D4 certificate was accepted as a D9 endpoint")
    original = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    mutations = []

    changed = copy.deepcopy(original)
    changed["rank_sizes"][4] += 1
    mutations.append(("rank size", changed))

    changed = copy.deepcopy(original)
    changed["layers"].pop()
    mutations.append(("missing layer", changed))

    changed = copy.deepcopy(original)
    changed["unexpected"] = 1
    mutations.append(("extra root field", changed))

    changed = copy.deepcopy(original)
    changed["layers"][0]["flows"][0]["degree_from"] += 1
    mutations.append(("wrong degree", changed))

    changed = copy.deepcopy(original)
    changed["layers"][0]["flows"][0]["numerator"] = -1
    mutations.append(("negative flow", changed))

    changed = copy.deepcopy(original)
    changed["layers"][0]["flows"][0]["denominator"] *= 2
    changed["layers"][0]["flows"][0]["numerator"] *= 2
    mutations.append(("noncanonical fraction", changed))

    changed = copy.deepcopy(original)
    changed["layers"][1]["flows"][0]["to"] = changed["layers"][1]["flows"][0]["from"]
    mutations.append(("wrong-rank endpoint", changed))

    d4_original = json.loads(D4_CERTIFICATE.read_text(encoding="utf-8"))
    changed = copy.deepcopy(d4_original)
    changed["layers"][1]["flows"][0]["edge_count"] += 1
    mutations.append(("D4 wrong cover multiplicity", changed, 4))

    changed = copy.deepcopy(d4_original)
    changed["layers"][2]["flows"].pop()
    mutations.append(("D4 missing positive flow", changed, 4))

    with tempfile.TemporaryDirectory(prefix="d9-flow-corruption-") as temporary:
        temporary_path = Path(temporary)
        for index, mutation in enumerate(mutations):
            name, document, *endpoint = mutation
            path = temporary_path / f"bad-{index}.json"
            path.write_text(json.dumps(document), encoding="utf-8")
            outcome = run(path, expected_n=endpoint[0] if endpoint else 9)
            if outcome.returncode == 0 or "REJECTED:" not in outcome.stderr:
                raise AssertionError(f"corruption was accepted ({name}): {outcome.stdout} {outcome.stderr}")

    print(
        "PASS: D4 and D9 certificates accepted; endpoint mismatch and "
        f"{len(mutations)} corruptions rejected"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
