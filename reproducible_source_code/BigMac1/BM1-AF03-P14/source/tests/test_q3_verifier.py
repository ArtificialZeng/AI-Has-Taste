#!/usr/bin/env python3
"""Mutation tests for the Q3 exact classification certificate."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERTIFICATE = ROOT / "results" / "q3_classification_certificate.json"
VERIFIER = ROOT / "src" / "verify_q3_classification.py"


def main() -> int:
    original = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    valid = subprocess.run(
        [sys.executable, str(VERIFIER), str(CERTIFICATE)], capture_output=True, text=True
    )
    if valid.returncode != 0:
        print("FAIL: valid Q3 certificate rejected", file=sys.stderr)
        return 1
    mutations = []
    for path, value in [
        (("claim",), "a non-diagonal orbit may survive"),
        (("positive_saturation",), ["a"]),
        (("primitive_resultant",), "-64*b^2*(b-1)^4*(b^2+b+1)^3"),
        (("surviving_positive_branch",), "b=1"),
    ]:
        changed = copy.deepcopy(original)
        changed[path[0]] = value
        mutations.append(changed)
    extra = copy.deepcopy(original)
    extra["unknown"] = True
    mutations.append(extra)

    with tempfile.TemporaryDirectory(prefix="q3_mutations_") as directory:
        for index, mutation in enumerate(mutations):
            path = Path(directory) / f"mutation-{index}.json"
            path.write_text(json.dumps(mutation), encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(VERIFIER), str(path)], capture_output=True, text=True
            )
            if result.returncode == 0 or "REJECT:" not in result.stderr:
                print(f"FAIL: accepted Q3 mutation {index}", file=sys.stderr)
                return 1
    print(f"PASS: valid Q3 certificate accepted; {len(mutations)} corruptions rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
