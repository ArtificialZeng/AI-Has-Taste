#!/usr/bin/env python3
"""Generate an exact PB instance and an independent witness-pair CNF encoding.

The semantic OPB formulation uses one Boolean variable x_E per 4-set E.
The CNF is not the canonical long-clause encoding used elsewhere in this
project.  For each triple S it introduces a Boolean witness for every pair of
extensions of S, requires at least one witness, and makes a true witness imply
that both extensions are selected.

This is discovery code, not a certificate checker.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build(n: int) -> tuple[str, str, dict[str, object]]:
    if n not in (8, 9, 10):
        raise ValueError("the breaker audit is restricted to n in {8,9,10}")

    vertices = range(1, n + 1)
    edges = list(itertools.combinations(vertices, 4))
    triples = list(itertools.combinations(vertices, 3))
    variable_of = {edge: index + 1 for index, edge in enumerate(edges)}

    disjoint_pairs: list[tuple[int, int]] = []
    for left_index, left in enumerate(edges):
        left_set = frozenset(left)
        for right_index in range(left_index + 1, len(edges)):
            if left_set.isdisjoint(edges[right_index]):
                disjoint_pairs.append((left_index + 1, right_index + 1))

    opb_lines = [
        f"* #variable= {len(edges)} #constraint= {len(disjoint_pairs) + len(triples)}",
        "* x1,... are lexicographically ordered 4-subsets of [n]",
    ]
    for left, right in disjoint_pairs:
        opb_lines.append(f"+1 ~x{left} +1 ~x{right} >= 1 ;")
    extensions_by_triple: list[list[int]] = []
    for triple in triples:
        extensions = [
            variable_of[tuple(sorted((*triple, vertex)))]
            for vertex in vertices
            if vertex not in triple
        ]
        extensions_by_triple.append(extensions)
        terms = " ".join(f"+1 x{variable}" for variable in extensions)
        opb_lines.append(f"{terms} >= 2 ;")
    opb = "\n".join(opb_lines) + "\n"

    # Equisatisfiable witness-pair CNF.  Primary variables retain the OPB IDs.
    clauses: list[tuple[int, ...]] = [
        (-left, -right) for left, right in disjoint_pairs
    ]
    next_variable = len(edges) + 1
    witness_blocks: list[dict[str, object]] = []
    for triple, extensions in zip(triples, extensions_by_triple):
        witnesses: list[int] = []
        witness_pairs: list[list[int]] = []
        for left_position, right_position in itertools.combinations(
            range(len(extensions)), 2
        ):
            witness = next_variable
            next_variable += 1
            left = extensions[left_position]
            right = extensions[right_position]
            witnesses.append(witness)
            witness_pairs.append([left, right])
            clauses.append((-witness, left))
            clauses.append((-witness, right))
        clauses.append(tuple(witnesses))
        witness_blocks.append(
            {
                "triple": list(triple),
                "extensions": extensions,
                "first_witness_variable": witnesses[0],
                "witness_pairs": witness_pairs,
            }
        )

    cnf_lines = [
        "c independent witness-pair encoding of the exact PB feasibility problem",
        f"c n {n}",
        f"c primary variables 1 through {len(edges)} are lexicographic 4-subsets",
        f"p cnf {next_variable - 1} {len(clauses)}",
    ]
    cnf_lines.extend(" ".join(map(str, clause)) + " 0" for clause in clauses)
    cnf = "\n".join(cnf_lines) + "\n"

    metadata: dict[str, object] = {
        "schema_version": 1,
        "n": n,
        "primary_variable_count": len(edges),
        "auxiliary_variable_count": next_variable - 1 - len(edges),
        "total_variable_count": next_variable - 1,
        "opb_constraint_count": len(disjoint_pairs) + len(triples),
        "disjoint_pair_count": len(disjoint_pairs),
        "triple_count": len(triples),
        "cnf_clause_count": len(clauses),
        "primary_variable_map": [
            {"variable": index + 1, "edge": list(edge)}
            for index, edge in enumerate(edges)
        ],
        "witness_blocks": witness_blocks,
        "equivalence_argument": {
            "forward": (
                "a true witness implies its two extension variables, so the "
                "cover clause supplies two selected extensions"
            ),
            "reverse": (
                "if at least two extensions are selected, set the witness for "
                "any selected pair true and all other witnesses false"
            ),
        },
        "opb_sha256": sha256(opb.encode("ascii")),
        "cnf_sha256": sha256(cnf.encode("ascii")),
    }
    return opb, cnf, metadata


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("output_directory", type=Path)
    args = parser.parse_args()
    opb, cnf, metadata = build(args.n)
    args.output_directory.mkdir(parents=True, exist_ok=True)
    stem = f"n{args.n}_witness_pair"
    (args.output_directory / f"{stem}.opb").write_text(
        opb, encoding="ascii", newline="\n"
    )
    (args.output_directory / f"{stem}.cnf").write_text(
        cnf, encoding="ascii", newline="\n"
    )
    (args.output_directory / f"{stem}.metadata.json").write_text(
        json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    summary_keys = (
        "n",
        "primary_variable_count",
        "auxiliary_variable_count",
        "total_variable_count",
        "opb_constraint_count",
        "disjoint_pair_count",
        "triple_count",
        "cnf_clause_count",
        "opb_sha256",
        "cnf_sha256",
    )
    print(json.dumps({key: metadata[key] for key in summary_keys}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
