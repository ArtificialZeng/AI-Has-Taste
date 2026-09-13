#!/usr/bin/env python3
"""Generate the canonical CNF for a (4,3)-degree EKR counterexample.

This is discovery/certificate-generation code.  The independent verifier in
verification/verify_instance.py does not import it.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path


def canonical_instance(n: int):
    if n < 5:
        raise ValueError("n must be at least 5")
    edges = list(itertools.combinations(range(1, n + 1), 4))
    var_of = {edge: index + 1 for index, edge in enumerate(edges)}
    clauses: list[tuple[int, ...]] = []
    disjoint_count = 0
    for left_index, left in enumerate(edges):
        left_set = frozenset(left)
        for right_index in range(left_index + 1, len(edges)):
            right = edges[right_index]
            if left_set.isdisjoint(right):
                clauses.append((-(left_index + 1), -(right_index + 1)))
                disjoint_count += 1
    degree_count = 0
    for triple in itertools.combinations(range(1, n + 1), 3):
        extensions = [
            var_of[tuple(sorted((*triple, vertex)))]
            for vertex in range(1, n + 1)
            if vertex not in triple
        ]
        for omitted in extensions:
            clauses.append(tuple(var for var in extensions if var != omitted))
            degree_count += 1
    return edges, clauses, disjoint_count, degree_count


def render_dimacs(n: int) -> tuple[str, dict[str, object]]:
    edges, clauses, disjoint_count, degree_count = canonical_instance(n)
    lines = [
        "c canonical (k,d)=(4,3) d-degree EKR counterexample instance",
        f"c n {n}",
        "c variables are lexicographically ordered 4-subsets of [n]",
        f"p cnf {len(edges)} {len(clauses)}",
    ]
    lines.extend(" ".join(map(str, clause)) + " 0" for clause in clauses)
    dimacs = "\n".join(lines) + "\n"
    metadata: dict[str, object] = {
        "schema_version": 1,
        "n": n,
        "k": 4,
        "d": 3,
        "variable_count": len(edges),
        "clause_count": len(clauses),
        "disjointness_clause_count": disjoint_count,
        "minimum_degree_clause_count": degree_count,
        "encoding": {
            "disjointness": "for every disjoint pair E,E': (-x_E or -x_E')",
            "minimum_degree": (
                "for each triple S and each one of its extensions e, the clause "
                "containing all other extensions; their conjunction is degree(S)>=2"
            ),
            "auxiliary_variables": 0,
        },
        "variable_map": [
            {"variable": index + 1, "edge": list(edge)}
            for index, edge in enumerate(edges)
        ],
        "dimacs_sha256": hashlib.sha256(dimacs.encode("ascii")).hexdigest(),
    }
    return dimacs, metadata


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("cnf", type=Path)
    parser.add_argument("metadata", type=Path)
    args = parser.parse_args()
    dimacs, metadata = render_dimacs(args.n)
    args.cnf.write_text(dimacs, encoding="ascii", newline="\n")
    args.metadata.write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({key: metadata[key] for key in (
        "n", "variable_count", "clause_count", "disjointness_clause_count",
        "minimum_degree_clause_count", "dimacs_sha256"
    )}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
