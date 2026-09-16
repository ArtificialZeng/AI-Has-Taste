#!/usr/bin/env python3
"""Independent literal checker for the explicit starlike construction.

This certificate does not import either discovery implementation.  It checks
all ordered arm-length tuples in a user-specified box that satisfy the proved
short-arm capacity inequalities.
"""

from __future__ import annotations

import argparse
import itertools
import json
from datetime import datetime, timezone
from pathlib import Path


def build(lengths: tuple[int, ...]) -> tuple[list[list[int]], list[list[int]]]:
    adjacency: list[list[int]] = [[]]
    arms: list[list[int]] = []
    for length in lengths:
        arm: list[int] = []
        previous = 0
        for _ in range(length):
            vertex = len(adjacency)
            adjacency.append([previous])
            adjacency[previous].append(vertex)
            arm.append(vertex)
            previous = vertex
        arms.append(arm)
    return adjacency, arms


def distances(adjacency: list[list[int]]) -> list[list[int]]:
    matrix: list[list[int]] = []
    for source in range(len(adjacency)):
        row = [-1] * len(adjacency)
        row[source] = 0
        queue = [source]
        for vertex in queue:
            for neighbor in adjacency[vertex]:
                if row[neighbor] < 0:
                    row[neighbor] = row[vertex] + 1
                    queue.append(neighbor)
        matrix.append(row)
    return matrix


def resolves(matrix: list[list[int]], chosen: list[int]) -> bool:
    codes = [tuple(sorted(row[v] for v in chosen)) for row in matrix]
    return len(codes) == len(set(codes))


def capacity_ok(lengths: tuple[int, ...]) -> bool:
    for radius in range(1, max(lengths) + 1):
        if sum(length <= radius for length in lengths) > 2**radius:
            return False
    return True


def construction(lengths: tuple[int, ...], arms: list[list[int]]) -> list[int]:
    m = len(lengths)
    if m == 4:
        if lengths[3] >= 3:
            return [arms[0][0], arms[2][1], arms[3][2]]
        if lengths == (1, 1, 2, 2):
            return [arms[0][0], arms[2][0], arms[2][1], arms[3][1]]
        if lengths == (1, 2, 2, 2):
            return [arms[0][0], arms[1][0], arms[1][1], arms[2][1]]
        if lengths == (2, 2, 2, 2):
            return [arms[0][0], arms[0][1], arms[1][0], arms[2][1]]
        raise AssertionError("capacity-valid four-arm tuple was not classified")

    chosen: list[int] = []
    bit_count = 0
    for q, arm in enumerate(arms):
        for bit in range(q.bit_length()):
            if q & (1 << bit):
                if bit >= len(arm):
                    raise AssertionError("binary pattern exceeds its arm")
                chosen.append(arm[bit])
                bit_count += 1
    if bit_count % 2 == 0:
        chosen.append(0)
    return chosen


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-arms", type=int, default=12)
    parser.add_argument("--max-length", type=int, default=8)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    rows: list[dict[str, int]] = []
    failures: list[dict[str, object]] = []
    for m in range(3, args.max_arms + 1):
        tested = 0
        for lengths in itertools.combinations_with_replacement(
            range(1, args.max_length + 1), m
        ):
            if not capacity_ok(lengths):
                continue
            adjacency, arms = build(lengths)
            matrix = distances(adjacency)
            chosen = construction(lengths, arms)
            diameter = lengths[-1] + lengths[-2]
            bound = len(adjacency) - diameter + 1
            tested += 1
            if len(chosen) > bound or not resolves(matrix, chosen):
                failures.append(
                    {
                        "lengths": list(lengths),
                        "chosen": chosen,
                        "bound": bound,
                        "resolves": resolves(matrix, chosen),
                    }
                )
                break
        rows.append({"arms": m, "tuples_checked": tested})
        print(f"arms={m} tuples={tested} failures={len(failures)}", flush=True)
        if failures:
            break

    report = {
        "schema_version": 1,
        "kind": "independent_starlike_construction_check",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "max_arms": args.max_arms,
            "max_length": args.max_length,
        },
        "rows": rows,
        "failures": failures,
        "status": "PASS" if not failures else "FAIL",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(report["status"])
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
