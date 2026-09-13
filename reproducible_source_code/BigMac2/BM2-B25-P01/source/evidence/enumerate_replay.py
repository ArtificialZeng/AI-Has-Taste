#!/usr/bin/env python3
"""Independent exact replay of the 3^12 balanced-selection enumeration.

This implementation uses an integer base-three counter, step-major orbit
order, bit-mask degree tests, and a successor-orbit length test.  It shares no
enumeration routine with enumerate_balanced.py.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path
import sys


N = 12
FULL = (1 << N) - 1
LIMIT = 3**12
# Deliberately different from the primary script's layer-major ordering.
ORBITS = tuple((layer, step) for step in (1, 2, 3) for layer in range(4))
PATH_TAILS = (0, 2, 4)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def colour(successor: list[int], path_tail: int) -> int:
    hits = []
    for k in range(3):
        representative_tail = (path_tail - 4 * k) % N
        if successor[representative_tail] == (representative_tail + 2) % N:
            hits.append(k)
    if len(hits) != 1:
        raise RuntimeError((path_tail, hits))
    return hits[0]


def cycle_from_zero(successor: tuple[int, ...]) -> list[int]:
    answer = []
    v = 0
    for _ in range(N):
        answer.append(v)
        v = successor[v]
    if v != 0 or len(set(answer)) != N:
        raise RuntimeError(successor)
    return answer


def decompose(successor: tuple[int, ...]) -> list[list[int]]:
    unseen = set(range(N))
    cycles = []
    while unseen:
        start = min(unseen)
        current = start
        cycle = []
        while True:
            if current not in unseen:
                if current != start:
                    raise RuntimeError(successor)
                break
            unseen.remove(current)
            cycle.append(current)
            current = successor[current]
        cycles.append(cycle)
    return cycles


def main() -> None:
    counts = defaultdict(int)
    histogram = defaultdict(int)
    cycle_types = defaultdict(int)
    survivors = []
    best: tuple[int, ...] | None = None

    for code in range(LIMIT):
        counts["balanced_selections"] += 1
        residue = code
        successor = [-1] * N
        tail_mask = 0
        head_mask = 0
        duplicate_tail = False

        for layer, step in ORBITS:
            t = residue % 3
            residue //= 3
            tail = layer + 4 * t
            head = (tail + step) % N
            tail_bit = 1 << tail
            duplicate_tail |= bool(tail_mask & tail_bit)
            tail_mask |= tail_bit
            head_mask |= 1 << head
            successor[tail] = head

        if duplicate_tail or tail_mask != FULL:
            continue
        counts["outdegree_one"] += 1
        if head_mask != FULL:
            continue
        counts["indegree_and_outdegree_one"] += 1

        successor_tuple = tuple(successor)
        cycles = decompose(successor_tuple)
        cycle_type = "+".join(str(x) for x in sorted(map(len, cycles)))
        cycle_types[cycle_type] += 1
        survivors.append({"successor": list(successor_tuple), "cycles": cycles})

        v = 0
        orbit_mask = 0
        for _ in range(N):
            orbit_mask |= 1 << v
            v = successor[v]
        if v != 0 or orbit_mask != FULL:
            continue
        counts["hamilton_cycles"] += 1

        colours = tuple(colour(successor, x) for x in PATH_TAILS)
        histogram["".join(str(x) for x in colours)] += 1
        if len(frozenset(colours)) != 3:
            continue
        counts["target_cycles"] += 1
        candidate = successor_tuple
        if best is None or candidate < best:
            best = candidate

    if counts["balanced_selections"] != LIMIT:
        raise RuntimeError(counts)
    if counts["outdegree_one"] != 6**4:
        raise RuntimeError(counts)

    root = Path(__file__).resolve().parent.parent
    ordered_counts = {
        key: counts[key]
        for key in (
            "balanced_selections",
            "outdegree_one",
            "indegree_and_outdegree_one",
            "hamilton_cycles",
            "target_cycles",
        )
    }
    output = {
        "algorithm": "integer base-three counter over step-major orbit choices",
        "domain_argument": (
            "Codes 0 through 3^12-1 give all twelve-digit ternary strings "
            "exactly once; digit t at (s,j) selects tail j+4t."
        ),
        "exact_arithmetic": True,
        "python_executable": sys.executable,
        "source_sha256": digest(root / "source.md"),
        "problem_sha256": digest(root / "problem.md"),
        "counts": ordered_counts,
        "cycle_type_histogram_for_degree_survivors": dict(sorted(cycle_types.items())),
        "all_degree_survivors": sorted(survivors, key=lambda item: item["successor"]),
        "hamilton_colour_histogram": dict(sorted(histogram.items())),
        "lexicographically_minimal_target_successor": list(best) if best else None,
        "lexicographically_minimal_target_cycle_from_zero": (
            cycle_from_zero(best) if best else None
        ),
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
