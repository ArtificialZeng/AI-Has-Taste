#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import subprocess
import tempfile


ROOT = pathlib.Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates/n8_certificate.json"
DRIVER = ROOT / "src/verify_certificate.py"
CORE = ROOT / "experiments/verifier_core"
CORE_SOURCE = ROOT / "src/verifier.cpp"


def run(path: pathlib.Path, only_n: int | None = None) -> subprocess.CompletedProcess[str]:
    command = [
        "python3",
        str(DRIVER),
        "--certificate",
        str(path),
        "--core",
        str(CORE),
        "--core-source",
        str(CORE_SOURCE),
    ]
    if only_n is not None:
        command.extend(["--only-n", str(only_n)])
    return subprocess.run(command, text=True, capture_output=True, cwd=ROOT)


def must_reject(payload: str, label: str, only_n: int | None = None) -> None:
    with tempfile.TemporaryDirectory() as directory:
        path = pathlib.Path(directory) / "tampered.json"
        path.write_text(payload, encoding="utf-8")
        result = run(path, only_n)
        if result.returncode == 0 or "VERIFIER_REJECT" not in result.stderr:
            raise AssertionError(f"{label} was not rejected: {result.stdout} {result.stderr}")


def main() -> None:
    original = json.loads(CERT.read_text(encoding="utf-8"))

    missing = dict(original)
    del missing["algorithm"]
    must_reject(json.dumps(missing), "missing required key")

    extra = dict(original)
    extra["trusted_discovery_output"] = True
    must_reject(json.dumps(extra), "extra trusted field")

    wrong_type = dict(original)
    wrong_type["max_n"] = True
    must_reject(json.dumps(wrong_type), "boolean substituted for integer")

    duplicate = CERT.read_text(encoding="utf-8").replace(
        '"schema_version": 1,', '"schema_version": 1, "schema_version": 1,', 1
    )
    must_reject(duplicate, "duplicate JSON key")

    altered = json.loads(CERT.read_text(encoding="utf-8"))
    altered["baselines"][4]["initial_classes"] += 1
    must_reject(json.dumps(altered), "altered exact count", only_n=4)

    accepted = run(CERT, only_n=4)
    if accepted.returncode != 0 or "CERTIFIED_FINITE_RESULT" not in accepted.stdout:
        raise AssertionError(f"valid certificate rejected: {accepted.stdout} {accepted.stderr}")
    print("FAIL_CLOSED_TESTS_PASS cases=6")


if __name__ == "__main__":
    main()
