#!/usr/bin/env python3
"""Fail-closed aggregation for an exact chunked gentreeg sweep."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re


SUMMARY = re.compile(
    r"^RESEARCH_CHECK trees=(\d+) generated=(\d+) nonunimodal=(\d+) "
    r"nonlogconcave=(\d+) sequence_hash=([0-9a-f]{16}) "
    r"parent_hash=([0-9a-f]{16}) cpu=([0-9]+(?:\.[0-9]+)?)$"
)
MASK64 = (1 << 64) - 1


def sha256(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, required=True)
    parser.add_argument("--modulus", type=int, required=True)
    parser.add_argument("--expected", type=int, required=True)
    parser.add_argument("--results-dir", type=pathlib.Path, required=True)
    parser.add_argument("--project-dir", type=pathlib.Path, default=pathlib.Path("."))
    args = parser.parse_args()
    if args.order < 1 or args.modulus < 1 or args.expected < 1:
        raise SystemExit("order, modulus, and expected count must be positive")

    total_trees = total_generated = 0
    total_nonunimodal = total_nonlogconcave = 0
    sequence_hash = parent_hash = 0
    total_cpu = 0.0
    exception_lines = 0
    combined_summary = hashlib.sha256()

    for residue in range(args.modulus):
        stem = f"order{args.order:02d}_chunk{residue:03d}_of_{args.modulus:03d}"
        summary_path = args.results_dir / f"{stem}.summary.done"
        exceptions_path = args.results_dir / f"{stem}.exceptions.done"
        if not summary_path.is_file() or not exceptions_path.is_file():
            raise SystemExit(f"missing completed chunk files for {stem}")
        raw_summary = summary_path.read_text(encoding="utf-8")
        lines = [line for line in raw_summary.splitlines() if line]
        if len(lines) != 1:
            raise SystemExit(f"expected exactly one summary line in {summary_path}")
        match = SUMMARY.fullmatch(lines[0])
        if match is None:
            raise SystemExit(f"malformed summary line in {summary_path}")
        trees, generated, nonuni, nonlc = map(int, match.group(1, 2, 3, 4))
        if trees != generated or trees == 0:
            raise SystemExit(f"invalid generator/checker count in {summary_path}")
        total_trees += trees
        total_generated += generated
        total_nonunimodal += nonuni
        total_nonlogconcave += nonlc
        sequence_hash = (sequence_hash + int(match.group(5), 16)) & MASK64
        parent_hash = (parent_hash + int(match.group(6), 16)) & MASK64
        total_cpu += float(match.group(7))
        combined_summary.update(f"{residue}:".encode())
        combined_summary.update(raw_summary.encode())

        for line in exceptions_path.read_text(encoding="utf-8").splitlines():
            if not line.startswith(("NONLOGCONCAVE ", "NONUNIMODAL ")):
                raise SystemExit(f"malformed exception line in {exceptions_path}")
            if line.startswith("NONUNIMODAL "):
                raise SystemExit(f"counterexample present in {exceptions_path}")
            exception_lines += 1

    if total_trees != args.expected or total_generated != args.expected:
        raise SystemExit(
            f"coverage failure: got {total_trees}, expected {args.expected}"
        )
    if total_nonunimodal != 0:
        raise SystemExit(f"found {total_nonunimodal} non-unimodal trees")

    project = args.project_dir.resolve()
    artifact_paths = {
        "checker_binary": project / "experiments/gentreeg_order31_checker",
        "checker_source": project / "experiments/order31_checker.c",
        "aggregator_source": pathlib.Path(__file__).resolve(),
        "nauty_tarball": project / "literature/external/nauty2_9_3.tar.gz",
    }
    for label, path in artifact_paths.items():
        if not path.is_file():
            raise SystemExit(f"missing bound artifact {label}: {path}")

    print(json.dumps({
        "status": "PASS",
        "order": args.order,
        "modulus": args.modulus,
        "trees": total_trees,
        "expected": args.expected,
        "nonunimodal": total_nonunimodal,
        "nonlogconcave": total_nonlogconcave,
        "saved_nonlogconcave_lines": exception_lines,
        "sequence_hash_sum_mod_2^64": f"{sequence_hash:016x}",
        "parent_hash_sum_mod_2^64": f"{parent_hash:016x}",
        "checker_cpu_seconds": round(total_cpu, 2),
        "ordered_summary_sha256": combined_summary.hexdigest(),
        "artifact_sha256": {
            label: sha256(path) for label, path in artifact_paths.items()
        },
    }, sort_keys=True))


if __name__ == "__main__":
    main()
