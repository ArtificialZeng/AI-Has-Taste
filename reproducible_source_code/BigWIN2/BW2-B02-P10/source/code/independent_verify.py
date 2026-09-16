#!/usr/bin/env python3
"""Independent exact P/N verifier for a finite CRIM size range.

Unlike discovery_dp.py, this program constructs column moves by literal
conjugation and never computes mex or nonzero Grundy values.  It can compare
its independently recomputed losing-set digest and counts with a discovery
summary, failing closed on malformed or inconsistent input.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import time
from pathlib import Path
from typing import Dict, Iterator, Sequence, Set, Tuple

Partition = Tuple[int, ...]


def generate_partitions(total: int) -> Iterator[Partition]:
    work: list[int] = []

    def extend(remaining: int, ceiling: int) -> Iterator[Partition]:
        if remaining == 0:
            yield tuple(work)
            return
        candidate = min(remaining, ceiling)
        while candidate:
            work.append(candidate)
            yield from extend(remaining - candidate, candidate)
            work.pop()
            candidate -= 1

    yield from extend(total, total)


def transpose(shape: Partition) -> Partition:
    if not shape:
        return ()
    return tuple(sum(row >= column for row in shape) for column in range(1, shape[0] + 1))


def delete_distinct_rows(shape: Partition) -> Set[Partition]:
    followers: Set[Partition] = set()
    for position in range(len(shape)):
        followers.add(shape[:position] + shape[position + 1 :])
    return followers


def conjugation_options(shape: Partition) -> Set[Partition]:
    row_followers = delete_distinct_rows(shape)
    transposed = transpose(shape)
    column_followers = {transpose(child) for child in delete_distinct_rows(transposed)}
    return row_followers | column_followers


def add_losing_hash(hasher: "hashlib._Hash", shape: Partition) -> None:
    hasher.update((",".join(map(str, shape)) + ":0\n").encode("ascii"))


def validate_expected(data: object, max_size: int) -> dict:
    if not isinstance(data, dict):
        raise ValueError("expected summary must be a JSON object")
    required = {
        "max_size": int,
        "partition_count_including_empty": int,
        "losing_count_including_empty": int,
        "odd_rank_losing_count": int,
        "losing_set_sha256": str,
        "by_size": list,
    }
    for key, kind in required.items():
        if key not in data or not isinstance(data[key], kind):
            raise ValueError(f"missing or invalid field: {key}")
    if data["max_size"] != max_size:
        raise ValueError("expected summary max_size does not match command line")
    return data


def run(max_size: int) -> dict:
    started = time.time()
    losing: Dict[Partition, bool] = {(): True}
    digest = hashlib.sha256()
    add_losing_hash(digest, ())
    total = 1
    total_losing = 1
    total_odd_losing = 0
    rows = []

    for size in range(1, max_size + 1):
        count = 0
        p_count = 0
        odd_p_count = 0
        for shape in generate_partitions(size):
            is_losing = all(not losing[child] for child in conjugation_options(shape))
            losing[shape] = is_losing
            count += 1
            if is_losing:
                p_count += 1
                add_losing_hash(digest, shape)
                if (len(shape) + shape[0]) & 1:
                    odd_p_count += 1
        total += count
        total_losing += p_count
        total_odd_losing += odd_p_count
        rows.append(
            {
                "size": size,
                "partitions": count,
                "losing": p_count,
                "odd_rank_losing": odd_p_count,
            }
        )

    return {
        "schema_version": 1,
        "engine": "independent_verify_conjugation_boolean_pn",
        "exact_arithmetic": True,
        "max_size": max_size,
        "partition_count_including_empty": total,
        "losing_count_including_empty": total_losing,
        "odd_rank_losing_count": total_odd_losing,
        "losing_set_sha256": digest.hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "elapsed_seconds": round(time.time() - started, 6),
        "by_size": rows,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-size", required=True, type=int)
    parser.add_argument("--expected", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    if args.max_size < 0:
        parser.error("--max-size must be nonnegative")

    result = run(args.max_size)
    if args.expected:
        try:
            expected = validate_expected(
                json.loads(args.expected.read_text(encoding="utf-8")), args.max_size
            )
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
            sys.stderr.write(f"FAIL: cannot validate expected summary: {exc}\n")
            return 3
        comparable = (
            "partition_count_including_empty",
            "losing_count_including_empty",
            "odd_rank_losing_count",
            "losing_set_sha256",
            "by_size",
        )
        mismatches = [key for key in comparable if result[key] != expected[key]]
        if mismatches:
            sys.stderr.write("FAIL: independent mismatch in " + ", ".join(mismatches) + "\n")
            return 4
        result["comparison"] = "PASS"
        result["expected_file_sha256"] = hashlib.sha256(args.expected.read_bytes()).hexdigest()

    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return 0 if result["odd_rank_losing_count"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
