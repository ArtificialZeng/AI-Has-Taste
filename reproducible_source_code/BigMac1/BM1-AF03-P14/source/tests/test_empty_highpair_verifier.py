#!/usr/bin/env python3
"""Mutation tests for the fail-closed empty-chamber verifier."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = ROOT / "results" / "empty_highpair_classification_certificate.json"
VERIFIER = ROOT / "src" / "verify_empty_highpair_classification.py"


def run(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VERIFIER), str(path)],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=150,
        check=False,
    )


def main() -> int:
    original = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    valid = run(CERTIFICATE)
    if valid.returncode != 0:
        print("FAIL: valid certificate was rejected", file=sys.stderr)
        print(valid.stdout, valid.stderr, file=sys.stderr)
        return 1

    mutations: list[tuple[str, dict]] = []

    item = copy.deepcopy(original)
    item["empty_chamber"]["high_pairs"] = [[0, 1]]
    mutations.append(("nonempty high-pair set", item))

    item = copy.deepcopy(original)
    item["three_value_cases"][1]["resultant_constant"] += 1
    mutations.append(("changed resultant", item))

    item = copy.deepcopy(original)
    item["factor_polynomials"]["B4"][2] += 1
    mutations.append(("changed factor coefficient", item))

    item = copy.deepcopy(original)
    item["three_value_cases"][4]["multiplicities"] = [2, 1, 2]
    mutations.append(("changed multiplicity", item))

    item = copy.deepcopy(original)
    item["empty_chamber"]["low_pair_closure"] = "ai+aj<1 for every 0<=i<j<=4"
    mutations.append(("dropped wall endpoints", item))

    item = copy.deepcopy(original)
    del item["branch_groebner_bases"]["122_B4"]
    mutations.append(("missing branch basis", item))

    item = copy.deepcopy(original)
    item["sturm_checks"][2][3] = 0
    mutations.append(("false Sturm count", item))

    item = copy.deepcopy(original)
    item["factor_polynomials"]["A4"][0] = "54;system(\"touch /tmp/unsafe\")"
    mutations.append(("expression injection", item))

    with tempfile.TemporaryDirectory(prefix="empty-cert-mutations-") as tmp:
        directory = Path(tmp)
        for index, (name, mutation) in enumerate(mutations):
            path = directory / f"mutation-{index}.json"
            path.write_text(json.dumps(mutation), encoding="utf-8")
            result = run(path)
            if result.returncode == 0:
                print(f"FAIL: accepted mutation: {name}", file=sys.stderr)
                return 1

    print(f"PASS: valid certificate accepted; {len(mutations)} corruptions rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
