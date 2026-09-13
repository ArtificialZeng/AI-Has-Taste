#!/usr/bin/env python3
"""Fresh small-range check by direct induced-subset enumeration.

This deliberately does not use translation symmetry or the census DFS.  A
vertex subset induces a chordless cycle exactly when its induced graph is
connected and every induced degree is two.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
MANIFEST = PROJECT / "evidence" / "n32_manifest.json"
OUTPUT = PROJECT / "audit" / "referee_subset_check.json"


def adjacency(n: int, selected: set[int]) -> list[int]:
    return [
        sum(
            1 << y
            for y in range(n)
            if x != y and math.gcd(abs(x - y), n) in selected
        )
        for x in range(n)
    ]


def complement(rows: list[int]) -> list[int]:
    universe = (1 << len(rows)) - 1
    return [universe ^ (1 << vertex) ^ row for vertex, row in enumerate(rows)]


def connected(rows: list[int], subset: int) -> bool:
    reached = subset & -subset
    frontier = reached
    while frontier:
        neighbors = 0
        work = frontier
        while work:
            bit = work & -work
            work ^= bit
            neighbors |= rows[bit.bit_length() - 1]
        frontier = neighbors & subset & ~reached
        reached |= frontier
    return reached == subset


def has_odd_hole(rows: list[int]) -> bool:
    n = len(rows)
    for size in range(5, n + 1, 2):
        for vertices in itertools.combinations(range(n), size):
            subset = sum(1 << vertex for vertex in vertices)
            if all((rows[vertex] & subset).bit_count() == 2 for vertex in vertices):
                if connected(rows, subset):
                    return True
    return False


def main() -> None:
    raw = MANIFEST.read_bytes()
    records = json.loads(raw)["records"]
    checked = 0
    graph_holes = 0
    complement_holes = 0
    mismatches = []
    for record in records:
        if record["n"] > 16:
            break
        rows = adjacency(record["n"], set(record["D"]))
        in_graph = has_odd_hole(rows)
        in_complement = False if in_graph else has_odd_hole(complement(rows))
        observed = "imperfect" if in_graph or in_complement else "perfect"
        if in_graph:
            graph_holes += 1
        elif in_complement:
            complement_holes += 1
        if observed != record["status"]:
            mismatches.append(
                {
                    "n": record["n"],
                    "dmask": record["dmask"],
                    "manifest": record["status"],
                    "subset_check": observed,
                }
            )
        checked += 1
    result = {
        "algorithm": "direct odd-cardinality induced-subset enumeration",
        "complement_odd_holes_found": complement_holes,
        "graph_odd_holes_found": graph_holes,
        "manifest_sha256": hashlib.sha256(raw).hexdigest(),
        "mismatches": mismatches,
        "n_max": 16,
        "records_checked": checked,
        "status": "pass" if not mismatches else "fail",
    }
    OUTPUT.write_text(
        json.dumps(result, sort_keys=True, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
