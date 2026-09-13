#!/usr/bin/env python3
"""Fail-closed aggregation of canonical tournament sweep summaries.

No packing-search code is imported.  The aggregator checks that every residue
slice occurs exactly once, every process exited successfully, every summary
matches the requested endpoint, and the exact total number of isomorphism
classes is present.  It then serializes all slice counts, tournament-stream
SHA-256 digests, and log hashes into one JSON certificate index.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import re
import shutil
import sys
from pathlib import Path


SUMMARY = re.compile(
    r"^(BUILDER_OK|CERTIFIER_OK) n=(\d+) target=(\d+) count=(\d+) "
    r"sha256=([0-9a-f]{64}) nodes=(\d+) max_nodes=(\d+)$"
)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        while block := handle.read(1 << 20):
            h.update(block)
    return h.hexdigest()


def fail(message: str) -> None:
    print(f"AGGREGATE_FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", type=Path, required=True)
    parser.add_argument("--role", choices=("builder", "certifier"), required=True)
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--target", type=int, required=True)
    parser.add_argument("--modulus", type=int, required=True)
    parser.add_argument("--expect-total", type=int, required=True)
    parser.add_argument("--scanner", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    if args.modulus <= 0 or args.expect_total <= 0:
        fail("modulus and expected total must be positive")
    if not args.scanner.is_file():
        fail(f"missing scanner executable {args.scanner}")

    wanted_prefix = "BUILDER_OK" if args.role == "builder" else "CERTIFIER_OK"
    slices: list[dict[str, object]] = []
    grand_count = grand_nodes = 0
    largest_search = 0
    for residue in range(args.modulus):
        stem = f"slice_{residue:04d}_of_{args.modulus:04d}"
        log = args.run_dir / f"{stem}.log"
        status = args.run_dir / f"{stem}.status"
        if not log.is_file() or not status.is_file():
            fail(f"missing log or status for residue {residue}")
        status_text = status.read_text(encoding="ascii").strip()
        if status_text != "0":
            fail(f"nonzero or malformed status for residue {residue}: {status_text!r}")
        raw = log.read_text(encoding="utf-8")
        lines = raw.splitlines()
        if len(lines) != 1:
            fail(f"residue {residue} log must contain exactly one line, found {len(lines)}")
        matches = [SUMMARY.fullmatch(line) for line in lines]
        matches = [match for match in matches if match is not None]
        if len(matches) != 1:
            fail(f"residue {residue} has {len(matches)} valid summary lines")
        match = matches[0]
        prefix, n_text, target_text, count_text, stream_hash, nodes_text, max_text = match.groups()
        if prefix != wanted_prefix:
            fail(f"residue {residue} role mismatch: {prefix}")
        if int(n_text) != args.n or int(target_text) != args.target:
            fail(f"residue {residue} endpoint mismatch")
        count = int(count_text)
        nodes = int(nodes_text)
        max_nodes = int(max_text)
        if count <= 0 or nodes <= 0 or max_nodes <= 0:
            fail(f"residue {residue} has nonpositive counters")
        grand_count += count
        grand_nodes += nodes
        largest_search = max(largest_search, max_nodes)
        slices.append(
            {
                "residue": residue,
                "count": count,
                "stream_sha256": stream_hash,
                "nodes": nodes,
                "max_nodes": max_nodes,
                "log_sha256": sha256(log),
            }
        )

    if grand_count != args.expect_total:
        fail(f"class total {grand_count} != expected {args.expect_total}")

    generator = shutil.which("gentourng")
    if generator is None:
        fail("gentourng is not on PATH during aggregation")
    generator_path = Path(generator).resolve()
    record = {
        "schema_version": 1,
        "status": "PASS",
        "role": args.role,
        "n": args.n,
        "target": args.target,
        "generator_command": "gentourng -q N RES/MOD",
        "generator_path": str(generator_path),
        "generator_sha256": sha256(generator_path),
        "modulus": args.modulus,
        "expected_total": args.expect_total,
        "verified_total": grand_count,
        "total_search_nodes": grand_nodes,
        "largest_single_instance_nodes": largest_search,
        "scanner": str(args.scanner),
        "scanner_sha256": sha256(args.scanner),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "slices": slices,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(
        f"AGGREGATE_OK role={args.role} n={args.n} target={args.target} "
        f"slices={args.modulus} total={grand_count} nodes={grand_nodes} "
        f"max_nodes={largest_search} output={args.output}"
    )


if __name__ == "__main__":
    main()
