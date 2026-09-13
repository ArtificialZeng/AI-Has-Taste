#!/usr/bin/env python3
"""Mutation tests demonstrating that verify_orbit_flow.py fails closed."""

from __future__ import annotations

import argparse
import copy
import json
import subprocess
import sys
import tempfile
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    args = parser.parse_args()
    original = json.loads(args.certificate.read_text())
    mutations = {}

    changed_amount = copy.deepcopy(original)
    changed_amount["rank_pairs"][0]["flows"][0]["numerator"] += 1
    mutations["changed_amount"] = changed_amount

    unknown_endpoint = copy.deepcopy(original)
    unknown_endpoint["rank_pairs"][0]["flows"][0]["upper"] = "P[bogus]N[-]"
    mutations["unknown_endpoint"] = unknown_endpoint

    zero_denominator = copy.deepcopy(original)
    zero_denominator["rank_pairs"][0]["flows"][0]["denominator"] = 0
    mutations["zero_denominator"] = zero_denominator

    missing_flow = copy.deepcopy(original)
    missing_flow["rank_pairs"][-1]["flows"].pop()
    missing_flow["rank_pairs"][-1]["nonzero_flow_count"] -= 1
    mutations["missing_flow"] = missing_flow

    duplicate_type = copy.deepcopy(original)
    duplicate_type["types"][-1] = copy.deepcopy(duplicate_type["types"][0])
    mutations["duplicate_type"] = duplicate_type

    verifier = Path(__file__).with_name("verify_orbit_flow.py")
    with tempfile.TemporaryDirectory(prefix="abs_dn_rejections_") as directory:
        root = Path(directory)
        for name, data in mutations.items():
            path = root / f"{name}.json"
            path.write_text(json.dumps(data, sort_keys=True) + "\n")
            result = subprocess.run(
                [sys.executable, str(verifier), str(path)],
                check=False,
                capture_output=True,
                text=True,
            )
            if result.returncode == 0 or '"status": "REJECTED"' not in result.stdout:
                raise AssertionError(f"verifier accepted mutation {name}: {result.stdout} {result.stderr}")
            print(f"REJECTED {name}")
    print(f"all {len(mutations)} corruptions rejected")


if __name__ == "__main__":
    main()
