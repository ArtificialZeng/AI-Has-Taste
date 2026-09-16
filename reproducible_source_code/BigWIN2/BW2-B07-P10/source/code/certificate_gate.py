#!/usr/bin/env python3
"""Fail-closed release gate; prints input and verifier-code fingerprints."""

import hashlib
import pathlib
import subprocess
import sys


ROOT = pathlib.Path(__file__).resolve().parent.parent
CHECKS = [
    ["python3", "code/verify_disconnected_euler.py", "certificates/disconnected17_inputs.json"],
    ["python3", "code/verify_disconnected_partitions.py", "certificates/disconnected17_inputs.json"],
    ["python3", "code/verify_disconnected_from_totals.py", "certificates/disconnected17_inputs.json"],
    ["python3", "code/verify_lower_burnside.py", "certificates/bounds17_inputs.json"],
    ["python3", "code/verify_lower_burnside_independent.py", "certificates/bounds17_inputs.json"],
    ["python3", "code/verify_upper_extensions.py", "certificates/bounds17_inputs.json"],
    ["python3", "code/verify_upper_extensions_bruteforce.py", "certificates/bounds17_inputs.json"],
    ["python3", "code/verify_table59_pdf.py", "literature/sources/brinkmann_mckay_2002_posets.pdf", "certificates/bounds17_inputs.json"],
    ["python3", "code/test_small_exhaustive.py"],
]
EXPECTED_FAILURES = [
    ["python3", "code/verify_disconnected_euler.py", "tests/fixtures/malformed_disconnected.json"],
    ["python3", "code/verify_disconnected_partitions.py", "tests/fixtures/malformed_disconnected.json"],
    ["python3", "code/verify_lower_burnside.py", "tests/fixtures/malformed_bounds.json"],
    ["python3", "code/verify_upper_extensions.py", "tests/fixtures/malformed_bounds.json"],
]


def sha256(path: pathlib.Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    for command in CHECKS:
        subprocess.run(command, cwd=ROOT, check=True)
    for command in EXPECTED_FAILURES:
        result = subprocess.run(command, cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            raise SystemExit(f"CERTIFICATE GATE FAILED: malformed input accepted by {command[1]}")

    inputs = [
        ROOT / "certificates/disconnected17_inputs.json",
        ROOT / "certificates/bounds17_inputs.json",
        ROOT / "literature/sources/brinkmann_mckay_2002_posets.pdf",
    ]
    codes = sorted((ROOT / "code").glob("*.py"))
    for path in inputs:
        print(f"INPUT_SHA256 {path.relative_to(ROOT)} {sha256(path)}")
    aggregate = hashlib.sha256()
    for path in codes:
        aggregate.update(str(path.relative_to(ROOT)).encode("utf-8") + b"\0")
        aggregate.update(bytes.fromhex(sha256(path)))
    print(f"CODESET_SHA256 {aggregate.hexdigest()}")
    print("CERTIFICATE GATE: PASSED")


if __name__ == "__main__":
    if len(sys.argv) != 1:
        raise SystemExit("usage: certificate_gate.py")
    main()
