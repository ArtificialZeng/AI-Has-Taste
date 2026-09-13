#!/usr/bin/env python3
"""Fail-closed binder for the frozen Erdős--Szekeres #699 finite result.

This program does not repeat the exhaustive enumeration.  It binds the exact
certificate, the already-run verifier source, and its strict output; it then
checks that the canonical certificate count and the verifier's recomputed
anchor count are the same fixed integer.  Runtime is parsed only to reject
malformed output and is never trusted as mathematical evidence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


EXPECTED_BINDING: dict[str, Any] = {
    "schema": "erdos699-i3-release-binding-v1",
    "n_min": 8,
    "n_max": 100_000_000,
    "i": 3,
    "candidate_indices_tested": 43_631_335_536,
    "certificate_path": "certificates/i3_scan_100m.json",
    "certificate_sha256": (
        "23c45255e41877ccde381d86564e991ced9b7e08b8559f48405f4a759b51f0ba"
    ),
    "verifier_source_path": "code/verify_i3.cpp",
    "verifier_source_sha256": (
        "5365f052cd14ae35efa5e7efed5008584fb4ab523f8f1a6c51058a14a2d9bcd5"
    ),
    "strict_output_path": "certificates/i3_verify_100m_strict.txt",
    "strict_output_sha256": (
        "9a1a430068f5813195a90b0f22937095008b50f84c66fb311ca64ff3dc2904ab"
    ),
    "binary_build_command": (
        "c++ -O3 -std=c++17 -Wall -Wextra -pedantic "
        "code/verify_i3.cpp -o code/verify_i3"
    ),
}

CERTIFICATE_KEYS = {
    "schema",
    "n_min",
    "n_max",
    "i",
    "candidate_indices_tested",
    "weak_counterexample",
    "elapsed_ms_diagnostic_only",
}

STRICT_OUTPUT = re.compile(
    r"VERIFIED erdos699 i=([0-9]+) n=\[([0-9]+),([0-9]+)\] "
    r"anchor_candidates=([0-9]+) elapsed_ms_diagnostic_only=([0-9]+)\n?\Z"
)


class BindingError(RuntimeError):
    pass


def reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise BindingError(f"duplicate JSON field: {key}")
        result[key] = value
    return result


def reject_nonstandard_constant(token: str) -> Any:
    raise BindingError(f"nonstandard JSON constant: {token}")


def load_unique_json(path: Path) -> dict[str, Any]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise BindingError(f"cannot read JSON {path}: {exc}") from exc
    try:
        value = json.loads(
            text,
            object_pairs_hook=reject_duplicate_pairs,
            parse_constant=reject_nonstandard_constant,
        )
    except (json.JSONDecodeError, BindingError) as exc:
        raise BindingError(f"invalid or non-unique JSON {path}: {exc}") from exc
    if type(value) is not dict:
        raise BindingError(f"top-level JSON object required: {path}")
    return value


def exact_nonnegative_int(value: Any, field: str) -> int:
    if type(value) is not int or value < 0:
        raise BindingError(f"{field} must be a nonnegative JSON integer")
    return value


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as stream:
            for block in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(block)
    except OSError as exc:
        raise BindingError(f"cannot hash {path}: {exc}") from exc
    return digest.hexdigest()


def artifact(root: Path, relative: str) -> Path:
    path = (root / relative).resolve()
    if not path.is_relative_to(root) or not path.is_file():
        raise BindingError(f"missing or escaping artifact path: {relative}")
    return path


def require_hash(path: Path, expected: str, label: str) -> None:
    actual = sha256(path)
    if actual != expected:
        raise BindingError(f"{label} SHA-256 mismatch: expected {expected}, got {actual}")


def verify(root: Path, binding_path: Path) -> str:
    root = root.resolve()
    if not root.is_dir():
        raise BindingError(f"project root is not a directory: {root}")

    binding = load_unique_json(binding_path.resolve())
    if binding != EXPECTED_BINDING:
        raise BindingError("binding manifest does not match compiled release pins")

    certificate_path = artifact(root, EXPECTED_BINDING["certificate_path"])
    source_path = artifact(root, EXPECTED_BINDING["verifier_source_path"])
    output_path = artifact(root, EXPECTED_BINDING["strict_output_path"])

    certificate = load_unique_json(certificate_path)
    if set(certificate) != CERTIFICATE_KEYS:
        missing = sorted(CERTIFICATE_KEYS - set(certificate))
        extra = sorted(set(certificate) - CERTIFICATE_KEYS)
        raise BindingError(f"certificate fields differ: missing={missing}, extra={extra}")

    for field in ("n_min", "n_max", "i", "candidate_indices_tested"):
        exact_nonnegative_int(certificate[field], f"certificate.{field}")
    exact_nonnegative_int(
        certificate["elapsed_ms_diagnostic_only"],
        "certificate.elapsed_ms_diagnostic_only",
    )
    if certificate["schema"] != "erdos699-i3-scan-v1":
        raise BindingError("certificate schema mismatch")
    if certificate["weak_counterexample"] is not None:
        raise BindingError("certificate is not a null-result certificate")

    for field in ("n_min", "n_max", "i", "candidate_indices_tested"):
        if certificate[field] != EXPECTED_BINDING[field]:
            raise BindingError(
                f"certificate {field} mismatch: expected "
                f"{EXPECTED_BINDING[field]}, got {certificate[field]}"
            )

    try:
        strict_text = output_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise BindingError(f"cannot read strict output: {exc}") from exc
    match = STRICT_OUTPUT.fullmatch(strict_text)
    if match is None:
        raise BindingError("strict output is malformed, duplicated, or truncated")
    output_i, output_n_min, output_n_max, output_candidates, output_runtime = (
        int(group) for group in match.groups()
    )
    if (output_n_min, output_n_max, output_i) != (
        EXPECTED_BINDING["n_min"],
        EXPECTED_BINDING["n_max"],
        EXPECTED_BINDING["i"],
    ):
        raise BindingError("strict output endpoint/stratum mismatch")
    if output_candidates != EXPECTED_BINDING["candidate_indices_tested"]:
        raise BindingError("strict output anchor-candidate count mismatch")
    if output_candidates != certificate["candidate_indices_tested"]:
        raise BindingError("certificate and strict-output candidate counts differ")
    if output_runtime < 0:
        raise BindingError("strict output runtime must be syntactically nonnegative")

    require_hash(
        certificate_path, EXPECTED_BINDING["certificate_sha256"], "certificate"
    )
    require_hash(source_path, EXPECTED_BINDING["verifier_source_sha256"], "source")
    require_hash(output_path, EXPECTED_BINDING["strict_output_sha256"], "output")

    return (
        "BOUND VERIFIED erdos699 i=3 n=[8,100000000] "
        "candidate_indices_tested=43631335536 "
        "anchor_candidates=43631335536 runtime_ignored=true"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--binding", required=True, type=Path)
    args = parser.parse_args()
    try:
        print(verify(args.root, args.binding))
        return 0
    except (BindingError, OSError, ValueError) as exc:
        print(f"binding verification failed closed: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
