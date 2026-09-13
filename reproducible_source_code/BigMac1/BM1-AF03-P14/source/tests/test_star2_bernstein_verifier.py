#!/usr/bin/env python3
"""Mutation tests for the fail-closed star2 verifier."""

from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "results" / "star2_bernstein_no_go_certificate.json"
VERIFY = ROOT / "src" / "verify_star2_bernstein.py"


def run(payload: dict) -> int:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "certificate.json"
        path.write_text(json.dumps(payload), encoding="utf-8")
        return subprocess.run(
            [sys.executable, str(VERIFY), str(path)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        ).returncode


def main() -> int:
    original = json.loads(CERT.read_text(encoding="utf-8"))
    if run(original) != 0:
        print("valid certificate was rejected", file=sys.stderr)
        return 1
    mutations = []
    p = copy.deepcopy(original); p["high_pairs"] = [[0, 1]]; mutations.append(p)
    p = copy.deepcopy(original); p["direction_coefficients_xyzw"][0] = -1; mutations.append(p)
    p = copy.deepcopy(original); del p["domain"]; mutations.append(p)
    p = copy.deepcopy(original); p["bernstein"]["H_degree"] = 7; mutations.append(p)
    p = copy.deepcopy(original); p["bernstein"]["H_coefficients"][0]["terms"][0][-2] = "0"; mutations.append(p)
    p = copy.deepcopy(original); p["chamber_margin_identities"]["low_12"] = "wrong"; mutations.append(p)
    p = copy.deepcopy(original); p["claim"] = "false claim"; mutations.append(p)
    p = copy.deepcopy(original); p["critical_numerators"] = "wrong"; mutations.append(p)
    for index, payload in enumerate(mutations, 1):
        if run(payload) == 0:
            print(f"mutation {index} was accepted", file=sys.stderr)
            return 1
    print(f"PASS: valid certificate accepted; {len(mutations)} corruptions rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
