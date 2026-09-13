#!/usr/bin/env python3
"""Negative tests for both n=3 certificate verifiers.

The canonical certificate is read-only.  Every adversarial input is written to
an isolated temporary directory.  The tests exercise both the in-process
schema validator and each verifier's command-line hash gate.
"""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import pathlib
import subprocess
import sys
import tempfile


HERE = pathlib.Path(__file__).resolve().parent
CERT_PATH = HERE / "n3_sos_certificate.json"
VERIFIER_PATHS = (
    HERE / "verify_n3_sos_stdlib.py",
    HERE / "verify_n3_sos.py",
)
EXPECTED_CERT_SHA256 = "b239bd925f6daac67ab3b2f914fb39e67387d4351af1fc23baa9265c832e74f0"


def load_module(path: pathlib.Path):
    module_name = f"fail_closed_{path.stem}"
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise AssertionError(f"cannot import verifier: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def expect_value_error(action, label: str):
    try:
        action()
    except (ValueError, json.JSONDecodeError):
        return
    raise AssertionError(f"{label}: malformed input was accepted")


def serialize(value) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def main() -> int:
    canonical_raw = CERT_PATH.read_bytes()
    canonical_hash = hashlib.sha256(canonical_raw).hexdigest()
    if canonical_hash != EXPECTED_CERT_SHA256:
        raise AssertionError(
            f"canonical input hash mismatch before tests: {canonical_hash}"
        )
    canonical_object = json.loads(canonical_raw)
    modules = tuple(load_module(path) for path in VERIFIER_PATHS)

    # A byte-distinct but semantically identical input isolates the hash gate.
    badhash = canonical_raw + b" "

    extra_object = copy.deepcopy(canonical_object)
    extra_object["unexpected_top_level_key"] = "must be rejected"

    drop_object = copy.deepcopy(canonical_object)
    del drop_object["normal_forms"][0]["claimed_gap"]

    tamper_object = copy.deepcopy(canonical_object)
    tamper_object["normal_forms"][1]["row_projective_parameters"][2] = 2

    cases = {
        "badhash": badhash,
        "extra": serialize(extra_object),
        "drop": serialize(drop_object),
        "tamper": serialize(tamper_object),
    }
    results = []

    # Exercise the strict decoder against inputs Python's default JSON decoder
    # would otherwise normalize or accept.
    for module in modules:
        expect_value_error(
            lambda module=module: module.decode_certificate(b'{"x":1,"x":2}'),
            f"{module.__name__}/malformed-duplicate-key",
        )
        expect_value_error(
            lambda module=module: module.decode_certificate(b'{"x":NaN}'),
            f"{module.__name__}/malformed-nonfinite",
        )

    with tempfile.TemporaryDirectory(prefix="n3-cert-negative-") as tmp:
        tmp_path = pathlib.Path(tmp)
        for case_name, payload in cases.items():
            case_path = tmp_path / f"{case_name}.json"
            case_path.write_bytes(payload)

            for module, verifier_path in zip(modules, VERIFIER_PATHS):
                decoded = module.decode_certificate(payload)
                if case_name == "badhash":
                    # Schema is valid: only the byte hash is wrong.
                    module.validate_certificate(decoded)
                else:
                    expect_value_error(
                        lambda module=module, decoded=decoded:
                            module.validate_certificate(decoded),
                        f"{verifier_path.name}/{case_name}/schema",
                    )

                completed = subprocess.run(
                    [sys.executable, str(verifier_path), str(case_path)],
                    cwd=HERE,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    check=False,
                )
                combined = completed.stdout + completed.stderr
                if completed.returncode == 0 or '"status": "PASS"' in combined:
                    raise AssertionError(
                        f"{verifier_path.name}/{case_name}: CLI accepted bad input"
                    )
                if "certificate sha256 mismatch" not in combined:
                    raise AssertionError(
                        f"{verifier_path.name}/{case_name}: hash gate did not fail first"
                    )
                results.append({
                    "case": case_name,
                    "verifier": verifier_path.name,
                    "status": "REJECTED",
                })

    final_hash = hashlib.sha256(CERT_PATH.read_bytes()).hexdigest()
    if final_hash != canonical_hash:
        raise AssertionError("canonical certificate changed during negative tests")

    print(json.dumps({
        "status": "PASS",
        "canonical_certificate_sha256": canonical_hash,
        "negative_cases": results,
        "parser_cases": ["malformed-duplicate-key", "malformed-nonfinite"],
        "canonical_input_unchanged": True,
        "python": sys.version.split()[0],
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
