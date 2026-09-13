#!/usr/bin/env python3
"""Exact product enumeration of all 3^12 balanced arc selections.

For each orbit (tail modulo 4, step), one of its three possible tails is
chosen.  This is exactly the domain specified in problem.md.  All arithmetic
is integer arithmetic modulo 12.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import sys


N = 12
LAYERS = range(4)
STEPS = (1, 2, 3)
ORBITS = tuple((j, s) for j in LAYERS for s in STEPS)
PATH_ARCS = ((0, 2), (2, 4), (4, 6))
ALL_VERTICES_MASK = (1 << N) - 1


def file_hash(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def development_colour(successor: tuple[int, ...], arc: tuple[int, int]) -> int:
    """Return the unique k for which arc belongs to H+4k."""
    x, z = arc
    colours = []
    for k in range(3):
        y = (x - 4 * k) % N
        w = (z - 4 * k) % N
        if successor[y] == w:
            colours.append(k)
    if len(colours) != 1:
        raise AssertionError((arc, colours, successor))
    return colours[0]


def normalized_cycle(successor: tuple[int, ...]) -> list[int]:
    cycle = [0]
    for _ in range(N - 1):
        cycle.append(successor[cycle[-1]])
    if len(set(cycle)) != N or successor[cycle[-1]] != 0:
        raise AssertionError(successor)
    return cycle


def cycle_decomposition(successor: tuple[int, ...]) -> list[list[int]]:
    """Canonical cycle listing: least unseen vertex starts each cycle."""
    unseen = set(range(N))
    cycles: list[list[int]] = []
    while unseen:
        start = min(unseen)
        cycle = [start]
        unseen.remove(start)
        vertex = successor[start]
        while vertex != start:
            if vertex not in unseen:
                raise AssertionError(successor)
            cycle.append(vertex)
            unseen.remove(vertex)
            vertex = successor[vertex]
        cycles.append(cycle)
    return cycles


def main() -> None:
    total = 0
    outdegree_one = 0
    indegree_one = 0
    hamilton = 0
    target = 0
    colour_histogram: Counter[str] = Counter()
    cycle_type_histogram: Counter[str] = Counter()
    permutation_survivors: list[dict[str, object]] = []
    minimum_successor: tuple[int, ...] | None = None

    # digits[(j,s)] = t selects tail j+4t from orbit O_(j,s).
    for digits in product(range(3), repeat=len(ORBITS)):
        total += 1
        successor = [-1] * N
        tails_mask = 0
        heads_mask = 0
        repeated_tail = False
        for (j, step), t in zip(ORBITS, digits):
            tail = j + 4 * t
            head = (tail + step) % N
            bit = 1 << tail
            if tails_mask & bit:
                repeated_tail = True
            tails_mask |= bit
            heads_mask |= 1 << head
            successor[tail] = head

        if repeated_tail or tails_mask != ALL_VERTICES_MASK:
            continue
        outdegree_one += 1
        if heads_mask != ALL_VERTICES_MASK:
            continue
        indegree_one += 1

        successor_tuple = tuple(successor)
        cycles = cycle_decomposition(successor_tuple)
        cycle_type = "+".join(str(len(cycle)) for cycle in sorted(cycles, key=len))
        cycle_type_histogram[cycle_type] += 1
        permutation_survivors.append(
            {
                "successor": list(successor_tuple),
                "cycles": cycles,
            }
        )
        vertex = 0
        visited_mask = 0
        for _ in range(N):
            visited_mask |= 1 << vertex
            vertex = successor_tuple[vertex]
        if vertex != 0 or visited_mask != ALL_VERTICES_MASK:
            continue
        hamilton += 1

        colours = tuple(
            development_colour(successor_tuple, arc) for arc in PATH_ARCS
        )
        colour_histogram["".join(map(str, colours))] += 1
        if len(set(colours)) != 3:
            continue
        target += 1
        if minimum_successor is None or successor_tuple < minimum_successor:
            minimum_successor = successor_tuple

    assert total == 3**12
    assert outdegree_one == 6**4

    root = Path(__file__).resolve().parent.parent
    result = {
        "algorithm": "itertools.product over layer-major orbit choices",
        "domain_argument": (
            "For each of 12 pairs (j,s), independently choose t in {0,1,2}; "
            "the selected arc is j+4t -> j+4t+s (mod 12)."
        ),
        "exact_arithmetic": True,
        "python_executable": sys.executable,
        "source_sha256": file_hash(root / "source.md"),
        "problem_sha256": file_hash(root / "problem.md"),
        "counts": {
            "balanced_selections": total,
            "outdegree_one": outdegree_one,
            "indegree_and_outdegree_one": indegree_one,
            "hamilton_cycles": hamilton,
            "target_cycles": target,
        },
        "cycle_type_histogram_for_degree_survivors": dict(
            sorted(cycle_type_histogram.items())
        ),
        "all_degree_survivors": permutation_survivors,
        "hamilton_colour_histogram": dict(sorted(colour_histogram.items())),
        "lexicographically_minimal_target_successor": (
            list(minimum_successor) if minimum_successor is not None else None
        ),
        "lexicographically_minimal_target_cycle_from_zero": (
            normalized_cycle(minimum_successor)
            if minimum_successor is not None
            else None
        ),
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
