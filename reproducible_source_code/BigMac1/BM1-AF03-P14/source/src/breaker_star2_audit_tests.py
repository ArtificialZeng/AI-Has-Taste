#!/usr/bin/env python3
"""Mutation tests for the independent standard-library star2 audit."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import platform
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def duplicate_top(raw: str, key: str) -> str:
    return re.sub(r"\{", '{"' + key + '":"__bad_first_value__",', raw, count=1)


def duplicate_nested(raw: str, object_key: str, nested_key: str) -> str:
    pattern = r'("' + re.escape(object_key) + r'"\s*:\s*\{)'
    changed, count = re.subn(
        pattern,
        r'\1"' + nested_key + r'":"__bad_first_value__",',
        raw,
        count=1,
    )
    if count != 1:
        raise RuntimeError(f"nested object not found: {object_key}")
    return changed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    certificate_path = root / "results/star2_bernstein_no_go_certificate.json"
    audit = root / "src/breaker_star2_audit.py"
    source = json.loads(certificate_path.read_text(encoding="utf-8"))
    cases = [("valid", source, True)]
    changed = copy.deepcopy(source); changed["claim"] = "false claim"; cases.append(("changed_claim", changed, False))
    changed = copy.deepcopy(source); changed["critical_numerators"] = "wrong"; cases.append(("changed_critical_declaration", changed, False))
    changed = copy.deepcopy(source); changed["high_pairs"] = [[0, 1]]; cases.append(("changed_graph", changed, False))
    changed = copy.deepcopy(source); changed["direction_coefficients_xyzw"][0] = -1; cases.append(("changed_direction", changed, False))
    changed = copy.deepcopy(source); changed["bernstein"]["H_coefficients"][4]["terms"][20][-2] = "0"; cases.append(("changed_coefficient", changed, False))
    changed = copy.deepcopy(source); del changed["domain"]; cases.append(("missing_domain", changed, False))
    raw = certificate_path.read_text(encoding="utf-8")
    cases.append(("duplicate_top_key", duplicate_top(raw, "schema"), False))
    cases.append(("duplicate_nested_key", duplicate_nested(raw, "normalization", "a4"), False))
    changed = copy.deepcopy(source); changed["normalization"]["a4"] = True; cases.append(("boolean_normalization", changed, False))
    results = []
    with tempfile.TemporaryDirectory(prefix="star2-audit-tests-") as directory:
        for index, (name, payload, should_accept) in enumerate(cases):
            certificate = Path(directory) / f"{name}.json"
            artifact = Path(directory) / f"{name}-result.json"
            certificate.write_text(payload if isinstance(payload, str) else json.dumps(payload), encoding="utf-8")
            process = subprocess.run(
                [
                    sys.executable,
                    str(audit),
                    str(certificate),
                    "--output",
                    str(artifact),
                    "--random-checks",
                    "4",
                    "--seed",
                    str(220260829 + index),
                ],
                check=False,
                capture_output=True,
                text=True,
            )
            results.append(
                {
                    "name": name,
                    "expected": "accept" if should_accept else "reject",
                    "returncode": process.returncode,
                    "message": (process.stderr or process.stdout).strip()[:220],
                }
            )
    passed = all(
        row["returncode"] == 0 if row["expected"] == "accept" else row["returncode"] != 0
        for row in results
    )
    output = {
        "status": "PASS" if passed else "FAIL",
        "python": platform.python_version(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "tests": results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))
    if not passed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
