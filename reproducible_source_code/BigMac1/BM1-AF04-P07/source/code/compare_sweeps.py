#!/usr/bin/env python3
"""Bind Builder and independent Certifier sweeps to identical input streams."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or value.get("status") != "PASS":
        raise ValueError(f"non-PASS sweep certificate: {path}")
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("builder", type=Path)
    parser.add_argument("certifier", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        builder = load(args.builder)
        certifier = load(args.certifier)
        if builder.get("role") != "builder" or certifier.get("role") != "certifier":
            raise ValueError("role mismatch")
        keys = ("n", "target", "modulus", "expected_total", "verified_total", "generator_sha256")
        for key in keys:
            if builder.get(key) != certifier.get(key):
                raise ValueError(f"top-level mismatch in {key}")
        if builder.get("scanner_sha256") == certifier.get("scanner_sha256"):
            raise ValueError("Builder and Certifier executable hashes are identical")
        left = builder.get("slices")
        right = certifier.get("slices")
        if not isinstance(left, list) or not isinstance(right, list) or len(left) != builder["modulus"] or len(right) != builder["modulus"]:
            raise ValueError("malformed slice arrays")
        checked = 0
        for a, b in zip(left, right, strict=True):
            if a.get("residue") != b.get("residue"):
                raise ValueError("residue mismatch")
            if a.get("count") != b.get("count"):
                raise ValueError(f"slice count mismatch at residue {a.get('residue')}")
            if a.get("stream_sha256") != b.get("stream_sha256"):
                raise ValueError(f"stream hash mismatch at residue {a.get('residue')}")
            checked += 1
        record = {
            "schema_version": 1,
            "status": "PASS",
            "n": builder["n"],
            "target": builder["target"],
            "verified_total": builder["verified_total"],
            "matching_slices": checked,
            "generator_sha256": builder["generator_sha256"],
            "builder_certificate_sha256": digest(args.builder),
            "certifier_certificate_sha256": digest(args.certifier),
            "builder_scanner_sha256": builder["scanner_sha256"],
            "certifier_scanner_sha256": certifier["scanner_sha256"],
        }
        args.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
        print(
            f"SWEEPS_MATCH_OK n={record['n']} target={record['target']} "
            f"slices={checked} total={record['verified_total']} output={args.output}"
        )
    except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError) as error:
        print(f"SWEEPS_MATCH_FAIL: {error}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
