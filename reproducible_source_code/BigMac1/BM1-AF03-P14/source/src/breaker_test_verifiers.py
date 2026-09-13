#!/usr/bin/env python3
"""Positive and destructive-input tests for the two breaker verifiers."""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import re
import subprocess
import sys
import tempfile
from pathlib import Path


def run(verifier: Path, certificate: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(verifier), str(certificate)],
        check=False,
        capture_output=True,
        text=True,
    )


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


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    saddle_cert = root / "results/breaker_saddle_certificate.json"
    saddle_verifier = root / "src/breaker_verify_saddle.py"
    q4_cert = root / "results/breaker_q4_baseline_certificate.json"
    q4_verifier = root / "src/breaker_verify_q4_baseline.py"
    tests: list[dict] = []

    for name, verifier, certificate in (
        ("valid_q5_saddle", saddle_verifier, saddle_cert),
        ("valid_q4_baseline", q4_verifier, q4_cert),
    ):
        result = run(verifier, certificate)
        tests.append({"name": name, "expected": "accept", "returncode": result.returncode})

    mutations = []
    q5 = json.loads(saddle_cert.read_text(encoding="utf-8"))
    changed = json.loads(json.dumps(q5))
    changed["minimal_polynomial_constant_first"][0] = 12
    mutations.append(("q5_changed_polynomial", saddle_verifier, changed))
    changed = json.loads(json.dumps(q5))
    del changed["expected_active_sign_vectors"]
    mutations.append(("q5_missing_field", saddle_verifier, changed))
    changed = json.loads(json.dumps(q5))
    changed["root_interval"]["left"] = "1/2"
    mutations.append(("q5_wrong_root_interval", saddle_verifier, changed))
    changed = json.loads(json.dumps(q5))
    changed["expected_tangent_signature"]["positive"] = 2
    mutations.append(("q5_changed_signature", saddle_verifier, changed))
    q5_raw = saddle_cert.read_text(encoding="utf-8")
    mutations.append(("q5_duplicate_top_key", saddle_verifier, duplicate_top(q5_raw, "schema")))
    mutations.append(("q5_duplicate_nested_key", saddle_verifier, duplicate_nested(q5_raw, "root_interval", "left")))
    changed = json.loads(json.dumps(q5))
    changed["expected_tangent_signature"]["positive"] = True
    mutations.append(("q5_boolean_signature", saddle_verifier, changed))
    q4 = json.loads(q4_cert.read_text(encoding="utf-8"))
    changed = json.loads(json.dumps(q4))
    changed["unnormalized_vector"][2] = "2/3"
    mutations.append(("q4_changed_vector", q4_verifier, changed))
    q4_raw = q4_cert.read_text(encoding="utf-8")
    mutations.append(("q4_duplicate_top_key", q4_verifier, duplicate_top(q4_raw, "schema")))
    mutations.append(("q4_duplicate_nested_key", q4_verifier, duplicate_nested(q4_raw, "expected_tangent_signature", "positive")))
    changed = json.loads(json.dumps(q4))
    changed["expected_tangent_signature"]["positive"] = True
    mutations.append(("q4_boolean_signature", q4_verifier, changed))

    with tempfile.TemporaryDirectory(prefix="breaker-verifier-tests-") as temp_dir:
        for name, verifier, data in mutations:
            certificate = Path(temp_dir) / f"{name}.json"
            certificate.write_text(data if isinstance(data, str) else json.dumps(data), encoding="utf-8")
            result = run(verifier, certificate)
            tests.append(
                {
                    "name": name,
                    "expected": "reject",
                    "returncode": result.returncode,
                    "stderr_or_stdout_prefix": (result.stderr or result.stdout).strip()[:160],
                }
            )
    passed = all(
        (row["returncode"] == 0 if row["expected"] == "accept" else row["returncode"] != 0)
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
