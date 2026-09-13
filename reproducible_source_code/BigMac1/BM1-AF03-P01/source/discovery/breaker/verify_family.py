#!/usr/bin/env python3
"""Fail-closed checker for a literal family, reconstructed from definitions.

This verifier deliberately does not import the PB/CNF generator or solver
output parser.  Its only trusted input is a strict JSON object containing n
and a literal list of 4-subsets.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import sys


class Rejection(Exception):
    pass


def load_strict(path: Path) -> tuple[int, list[tuple[int, ...]]]:
    try:
        raw = path.read_bytes()
        document = json.loads(raw.decode("utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise Rejection(f"unreadable JSON: {exc}") from exc
    if not isinstance(document, dict) or set(document) != {"n", "family"}:
        raise Rejection("top level must contain exactly n and family")
    n = document["n"]
    family_raw = document["family"]
    if type(n) is not int or n not in (8, 9, 10):
        raise Rejection("n must be an integer in {8,9,10}")
    if not isinstance(family_raw, list):
        raise Rejection("family must be a list")
    family: list[tuple[int, ...]] = []
    for index, edge_raw in enumerate(family_raw):
        if not isinstance(edge_raw, list) or len(edge_raw) != 4:
            raise Rejection(f"family[{index}] is not a four-element list")
        if any(type(vertex) is not int for vertex in edge_raw):
            raise Rejection(f"family[{index}] contains a noninteger")
        edge = tuple(edge_raw)
        if edge != tuple(sorted(edge)) or len(set(edge)) != 4:
            raise Rejection(f"family[{index}] is not a strictly increasing 4-set")
        if edge[0] < 1 or edge[-1] > n:
            raise Rejection(f"family[{index}] has a vertex outside [n]")
        family.append(edge)
    if family != sorted(family):
        raise Rejection("family must be lexicographically sorted")
    if len(set(family)) != len(family):
        raise Rejection("family contains a duplicate")
    return n, family


def verify(path: Path) -> dict[str, object]:
    n, family = load_strict(path)
    family_sets = [frozenset(edge) for edge in family]
    for left_index, right_index in itertools.combinations(range(len(family)), 2):
        if family_sets[left_index].isdisjoint(family_sets[right_index]):
            raise Rejection(
                f"disjoint members at indices {left_index},{right_index}: "
                f"{family[left_index]} and {family[right_index]}"
            )

    minimum_degree = n - 3
    degree_histogram: dict[int, int] = {}
    minimizers: list[list[int]] = []
    for triple in itertools.combinations(range(1, n + 1), 3):
        triple_set = frozenset(triple)
        degree = sum(triple_set.issubset(edge) for edge in family_sets)
        degree_histogram[degree] = degree_histogram.get(degree, 0) + 1
        if degree < minimum_degree:
            minimum_degree = degree
            minimizers = [list(triple)]
        elif degree == minimum_degree:
            minimizers.append(list(triple))
    if minimum_degree < 2:
        raise Rejection(f"minimum triple degree is {minimum_degree}, not at least 2")

    return {
        "status": "VERIFIED_LITERAL_COUNTEREXAMPLE",
        "n": n,
        "family_size": len(family),
        "minimum_triple_degree": minimum_degree,
        "degree_histogram": {
            str(key): degree_histogram[key] for key in sorted(degree_histogram)
        },
        "number_of_minimizers": len(minimizers),
        "first_minimizer": minimizers[0],
        "input_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("family", type=Path)
    args = parser.parse_args()
    try:
        result = verify(args.family)
    except Rejection as exc:
        print(f"REJECTED: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
