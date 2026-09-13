#!/usr/bin/env python3
"""Negative parser tests; every damaged certificate must be rejected."""

import copy
import json
import tempfile
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from verify_exact import load_config


GOOD = json.loads((Path(__file__).resolve().parents[1] / "certificate" / "certificate.json").read_text())


def rejected(value):
    with tempfile.NamedTemporaryFile("w", suffix=".json") as handle:
        json.dump(value, handle)
        handle.flush()
        try:
            load_config(Path(handle.name))
        except ValueError:
            return True
    return False


bad = []
case = copy.deepcopy(GOOD); del case["schema"]; bad.append(case)
case = copy.deepcopy(GOOD); case["schema"] = "unknown"; bad.append(case)
case = copy.deepcopy(GOOD); case["source_sha256"] = "00"; bad.append(case)
case = copy.deepcopy(GOOD); case["pivot_prime"] = 15; bad.append(case)
case = copy.deepcopy(GOOD); case["cases"][0]["expected_candidate_count"] += 1; bad.append(case)
case = copy.deepcopy(GOOD); case["cases"][0]["n"] = 6; bad.append(case)
case = copy.deepcopy(GOOD); case["extra"] = True; bad.append(case)

assert all(rejected(case) for case in bad), "a malformed certificate was accepted"
print(f"PASS malformed_rejected={len(bad)}")
