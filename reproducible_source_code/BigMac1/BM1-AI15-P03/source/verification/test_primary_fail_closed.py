#!/usr/bin/env python3
"""Adversarial fail-closed regression for ``primary_verify.py``.

The harness never imports the verifier under test.  It launches a fresh
interpreter for every (certificate, interpreter-mode) pair, records raw
stdout/stderr and exact hashes, and requires:

* the unmodified certificate to exit zero and emit JSON status ``PASS``;
* every tampered certificate to exit nonzero and not emit ``PASS``.

No Python language assertions are used, so optimization cannot remove the
harness's own checks.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import platform
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_VERIFIER = PROJECT_ROOT / "verification" / "primary_verify.py"
DEFAULT_CERTIFICATE = PROJECT_ROOT / "certificates" / "zero_set_certificate.json"
DEFAULT_OUTPUT = PROJECT_ROOT / "verification" / "primary_fail_closed_results.json"


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def read_json_object(path: Path) -> tuple[bytes, dict[str, Any]]:
    raw = path.read_bytes()
    parsed = json.loads(raw)
    if not isinstance(parsed, dict):
        raise ValueError(f"expected a top-level JSON object in {path}")
    return raw, parsed


def parse_pass_status(stdout: str) -> bool:
    """Return true only when the final nonempty stdout line is PASS JSON."""
    lines = [line for line in stdout.splitlines() if line.strip()]
    if not lines:
        return False
    try:
        value = json.loads(lines[-1])
    except json.JSONDecodeError:
        return False
    return isinstance(value, dict) and value.get("status") == "PASS"


def bad_extension_block(data: dict[str, Any]) -> None:
    data["even_one_flip"]["extension_block"] = "+++++++++"


def bad_claimed_zeros(data: dict[str, Any]) -> None:
    data["claimed_zeros"] = [7, 8, 12]


def remove_schema_version(data: dict[str, Any]) -> None:
    removed = data.pop("schema_version", None)
    if removed is None:
        raise ValueError("source certificate had no schema_version to remove")


def execute_case(
    python: Path,
    interpreter_flags: list[str],
    verifier: Path,
    certificate: Path,
    normalized_certificate_name: str,
    timeout_seconds: int,
) -> dict[str, Any]:
    command = [str(python), *interpreter_flags, str(verifier), str(certificate)]
    environment = os.environ.copy()
    environment.pop("PYTHONOPTIMIZE", None)
    environment.pop("PYTHONPATH", None)
    environment["PYTHONHASHSEED"] = "0"
    try:
        completed = subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            env=environment,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
        returncode = completed.returncode
        stdout = completed.stdout
        stderr = completed.stderr
        timed_out = False
    except subprocess.TimeoutExpired as exc:
        returncode = 124
        stdout = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or "")
        stderr = exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or "")
        stderr += f"\nHARNESS TIMEOUT after {timeout_seconds} seconds"
        timed_out = True
    return {
        "command": [str(python), *interpreter_flags, str(verifier), normalized_certificate_name],
        "returncode": returncode,
        "timed_out": timed_out,
        "emitted_pass_status": parse_pass_status(stdout),
        "stdout": stdout,
        "stderr": stderr,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verifier", type=Path, default=DEFAULT_VERIFIER)
    parser.add_argument("--certificate", type=Path, default=DEFAULT_CERTIFICATE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()

    verifier = args.verifier.resolve()
    certificate = args.certificate.resolve()
    output = args.output.resolve()
    python = Path(sys.executable).resolve()
    if args.timeout <= 0:
        print("FAIL: timeout must be positive", file=sys.stderr)
        return 2
    if not verifier.is_file() or not certificate.is_file():
        print("FAIL: verifier or certificate path is not a regular file", file=sys.stderr)
        return 2

    source_certificate_raw, source_data = read_json_object(certificate)
    verifier_raw = verifier.read_bytes()
    harness_raw = Path(__file__).read_bytes()

    mutations: list[tuple[str, str, Callable[[dict[str, Any]], None] | None]] = [
        ("valid", "unmodified source certificate", None),
        (
            "bad_extension_block",
            "even_one_flip.extension_block changed to '+++++++++'",
            bad_extension_block,
        ),
        (
            "bad_claimed_zeros",
            "claimed_zeros (exceptional-order/zero list) changed to [7,8,12]",
            bad_claimed_zeros,
        ),
        (
            "missing_schema_version",
            "required top-level key schema_version removed",
            remove_schema_version,
        ),
    ]
    modes = [
        ("normal", []),
        ("optimized", ["-O"]),
        ("optimized_isolated", ["-O", "-I"]),
    ]

    results: list[dict[str, Any]] = []
    vulnerabilities: list[str] = []
    with tempfile.TemporaryDirectory(prefix="a383733-primary-fail-closed-") as temporary:
        temporary_path = Path(temporary)
        for case_name, description, mutation in mutations:
            if mutation is None:
                case_path = certificate
                case_raw = source_certificate_raw
            else:
                case_data = copy.deepcopy(source_data)
                mutation(case_data)
                case_raw = (json.dumps(case_data, indent=2, sort_keys=True) + "\n").encode("utf-8")
                case_path = temporary_path / f"{case_name}.json"
                case_path.write_bytes(case_raw)
            expected_exit = "zero_with_pass" if mutation is None else "nonzero_without_pass"
            for mode_name, flags in modes:
                raw_run = execute_case(
                    python,
                    flags,
                    verifier,
                    case_path,
                    f"<{case_name}.json>",
                    args.timeout,
                )
                if mutation is None:
                    expectation_met = (
                        raw_run["returncode"] == 0
                        and raw_run["emitted_pass_status"]
                        and not raw_run["timed_out"]
                    )
                else:
                    expectation_met = (
                        raw_run["returncode"] != 0
                        and not raw_run["emitted_pass_status"]
                        and not raw_run["timed_out"]
                    )
                record = {
                    "case": case_name,
                    "description": description,
                    "mode": mode_name,
                    "interpreter_flags": flags,
                    "certificate_sha256": sha256_bytes(case_raw),
                    "expected_exit": expected_exit,
                    "expectation_met": expectation_met,
                    **raw_run,
                }
                results.append(record)
                if mutation is not None and not expectation_met:
                    vulnerabilities.append(
                        f"tampered case {case_name} was not rejected in mode {mode_name}: "
                        f"returncode={raw_run['returncode']}, "
                        f"emitted_pass_status={raw_run['emitted_pass_status']}, "
                        f"timed_out={raw_run['timed_out']}"
                    )

    unmet = [
        f"{record['case']}::{record['mode']}"
        for record in results
        if not record["expectation_met"]
    ]
    report = {
        "schema": "a383733-primary-fail-closed-regression-v1",
        "status": "PASS" if not unmet else "FAIL",
        "meaning": (
            "PASS means valid inputs were accepted and every listed tampering was rejected "
            "by nonzero exit in every interpreter mode."
        ),
        "environment": {
            "python_executable": str(python),
            "python_version": sys.version,
            "platform": platform.platform(),
        },
        "inputs": {
            "verifier": str(verifier),
            "verifier_sha256": sha256_bytes(verifier_raw),
            "certificate": str(certificate),
            "certificate_sha256": sha256_bytes(source_certificate_raw),
            "harness": str(Path(__file__).resolve()),
            "harness_sha256": sha256_bytes(harness_raw),
        },
        "mode_matrix": {name: flags for name, flags in modes},
        "unmet_expectations": unmet,
        "remaining_vulnerabilities": vulnerabilities,
        "results": results,
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    summary = {
        "status": report["status"],
        "output": str(output),
        "output_sha256": sha256_bytes(output.read_bytes()),
        "verifier_sha256": report["inputs"]["verifier_sha256"],
        "certificate_sha256": report["inputs"]["certificate_sha256"],
        "harness_sha256": report["inputs"]["harness_sha256"],
        "unmet_expectations": unmet,
        "remaining_vulnerabilities": vulnerabilities,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if not unmet else 1


if __name__ == "__main__":
    raise SystemExit(main())
