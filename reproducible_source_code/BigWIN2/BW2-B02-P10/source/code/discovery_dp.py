#!/usr/bin/env python3
"""Exact bottom-up Sprague--Grundy discovery for CRIM.

This implementation represents a column deletion directly: choose the height
of an actual column and subtract one from all rows meeting that column.  It is
deliberately independent of code/independent_verify.py's conjugation-based
option generator and Boolean P/N recurrence.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import time
from pathlib import Path
from typing import Dict, Iterable, Iterator, Sequence, Set, Tuple

Partition = Tuple[int, ...]


def partitions_of(n: int, cap: int | None = None) -> Iterator[Partition]:
    """Yield all partitions of n in reverse lexicographic order."""
    if n == 0:
        yield ()
        return
    if cap is None or cap > n:
        cap = n
    for first in range(cap, 0, -1):
        for tail in partitions_of(n - first, first):
            yield (first,) + tail


def direct_options(partition: Partition) -> Set[Partition]:
    """Return the exact CRIM follower set without forming a conjugate."""
    options: Set[Partition] = set()

    # Equal indexed rows give the same follower, so one representative of
    # each row length is enough.
    previous = None
    for index, length in enumerate(partition):
        if length != previous:
            options.add(partition[:index] + partition[index + 1 :])
            previous = length

    # At column j, height is the number of row lengths at least j.  Columns
    # of equal height give the same follower.  Iterate over all j to keep the
    # definition transparent, and deduplicate via the set.
    for column in range(1, partition[0] + 1) if partition else ():
        height = 0
        while height < len(partition) and partition[height] >= column:
            height += 1
        child = tuple(x - 1 for x in partition[:height] if x > 1) + partition[height:]
        options.add(child)

    return options


def mex(values: Iterable[int]) -> int:
    present = set(values)
    result = 0
    while result in present:
        result += 1
    return result


def record_hash(hasher: "hashlib._Hash", partition: Partition, value: int) -> None:
    encoded = ",".join(map(str, partition))
    hasher.update(f"{encoded}:{value}\n".encode("ascii"))


def run(max_size: int) -> tuple[dict, Dict[Partition, int]]:
    started = time.time()
    grundy: Dict[Partition, int] = {(): 0}
    all_digest = hashlib.sha256()
    losing_digest = hashlib.sha256()
    record_hash(all_digest, (), 0)
    record_hash(losing_digest, (), 0)
    rows = []
    total = 1
    total_losing = 1
    total_odd_losing = 0
    max_grundy = 0

    for size in range(1, max_size + 1):
        count = 0
        losing = 0
        odd_losing = 0
        for partition in partitions_of(size):
            follower_values = (grundy[child] for child in direct_options(partition))
            value = mex(follower_values)
            grundy[partition] = value
            count += 1
            max_grundy = max(max_grundy, value)
            record_hash(all_digest, partition, value)
            if value == 0:
                losing += 1
                record_hash(losing_digest, partition, 0)
                if (len(partition) + partition[0]) % 2:
                    odd_losing += 1
        total += count
        total_losing += losing
        total_odd_losing += odd_losing
        rows.append(
            {
                "size": size,
                "partitions": count,
                "losing": losing,
                "odd_rank_losing": odd_losing,
            }
        )

    script_bytes = Path(__file__).read_bytes()
    summary = {
        "schema_version": 1,
        "engine": "discovery_dp_direct_columns_full_sg",
        "exact_arithmetic": True,
        "max_size": max_size,
        "partition_count_including_empty": total,
        "losing_count_including_empty": total_losing,
        "odd_rank_losing_count": total_odd_losing,
        "max_grundy": max_grundy,
        "all_values_sha256": all_digest.hexdigest(),
        "losing_set_sha256": losing_digest.hexdigest(),
        "script_sha256": hashlib.sha256(script_bytes).hexdigest(),
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "elapsed_seconds": round(time.time() - started, 6),
        "by_size": rows,
    }
    return summary, grundy


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-size", type=int, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args(argv)
    if args.max_size < 0:
        parser.error("--max-size must be nonnegative")

    summary, _ = run(args.max_size)
    rendered = json.dumps(summary, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    sys.stdout.write(rendered)
    return 0 if summary["odd_rank_losing_count"] == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
