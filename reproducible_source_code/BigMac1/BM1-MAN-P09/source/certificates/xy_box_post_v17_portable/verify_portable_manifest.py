#!/usr/bin/env python3
"""Fail-closed verifier for the parallel post-v17 portable certificate layer.

Manifest paths are package-root relative.  Historical source/referee manifests
may occur as opaque provenance records, but this verifier never treats them as
transitively replayable.  The new portable manifests list every proof input,
fresh run log, exit record, and verifier used by the portable layer itself.
"""

from __future__ import annotations

import argparse
import hashlib
import re
from pathlib import Path, PurePosixPath


PACKAGE_ROOT = Path(__file__).resolve().parents[2]
ABS_TMP = re.compile(
    rb"(?<![A-Za-z0-9_.-])" + b"/" + b"tmp" + b"/"
)
FORBIDDEN = (
    b"/" + b"Users/" + b"mac",
    b"Documents/" + b"ChatGPT/" + b"math",
)


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_manifest(path: Path) -> dict[str, str]:
    records: dict[str, str] = {}
    for line_number, line in enumerate(
            path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            expected, relative = line.split("  ", 1)
        except ValueError as exc:
            raise AssertionError(
                f"malformed manifest line {line_number}") from exc
        pure = PurePosixPath(relative)
        if pure.is_absolute() or ".." in pure.parts or "" in pure.parts:
            raise AssertionError(f"unsafe manifest path: {relative}")
        if relative in records:
            raise AssertionError(f"duplicate manifest path: {relative}")
        if not re.fullmatch(r"[0-9a-f]{64}", expected):
            raise AssertionError(f"invalid SHA-256: {relative}")
        records[relative] = expected
    if not records:
        raise AssertionError("empty manifest")
    return records


def verify(manifest: Path, kind: str, expected_count: int,
           attack: str = "none") -> None:
    records = parse_manifest(manifest)
    if attack == "bad-manifest":
        records.pop(next(iter(records)))
    if len(records) != expected_count:
        raise AssertionError(
            f"manifest record count: {len(records)} != {expected_count}")
    if attack == "bad-member":
        first = next(iter(records))
        records[first] = "0" * 64
    normal_logs = 0
    normal_exits = 0
    attack_exits = 0
    for relative, expected in sorted(records.items()):
        path = PACKAGE_ROOT / relative
        if not path.is_file():
            raise AssertionError(f"missing manifest member: {relative}")
        data = path.read_bytes()
        if digest(path) != expected:
            raise AssertionError(f"manifest hash mismatch: {relative}")
        if any(marker in data for marker in FORBIDDEN) or ABS_TMP.search(data):
            raise AssertionError(f"machine path leaked: {relative}")
        name = path.name
        if name in {"normal.log", "verifier_normal.log"}:
            normal_logs += 1
            if b"PASS" not in data:
                raise AssertionError(f"normal log lacks PASS: {relative}")
        if name.endswith("normal.exit"):
            normal_exits += 1
            if data.strip() != b"0":
                raise AssertionError(f"normal exit is not zero: {relative}")
        if name.endswith(".exit") and (
                "attack" in name or "bad_" in name or
                "optimized" in name or "attempt" in name):
            attack_exits += 1
            if data.strip() == b"0":
                raise AssertionError(f"fail-closed attack exited zero: {relative}")
    if kind in {"source", "referee"}:
        if normal_logs < 1 or normal_exits < 1 or attack_exits < 1:
            raise AssertionError(
                f"insufficient {kind} gates: normal_logs={normal_logs}, "
                f"normal_exits={normal_exits}, attacks={attack_exits}")
    print(
        f"PASS portable {kind} manifest: {len(records)}/{len(records)}; "
        f"normal_logs={normal_logs}; normal_exits={normal_exits}; "
        f"attacks={attack_exits}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--kind", choices=("source", "referee", "cell", "top"),
                        required=True)
    parser.add_argument("--expected-count", type=int, required=True)
    parser.add_argument("--attack", choices=("none", "bad-manifest", "bad-member"),
                        default="none")
    args = parser.parse_args()
    manifest = args.manifest
    if not manifest.is_absolute():
        manifest = PACKAGE_ROOT / manifest
    verify(manifest, args.kind, args.expected_count, args.attack)


if __name__ == "__main__":
    main()
