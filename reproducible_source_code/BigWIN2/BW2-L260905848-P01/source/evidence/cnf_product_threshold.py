#!/usr/bin/env python3
"""Independent bit-level SAT encoding of product >= 42876.

Unlike ``cpsat_product_search.py``, this script contains no integer or product
primitive.  It sorts each family's 155 membership bits with Boolean comparator
gates.  The final unary outputs say exactly which cardinality thresholds hold.
The product threshold is then a disjunction over its componentwise-minimal
sorted integer triples.

The generated DIMACS file plus an UNSAT proof (when requested from a
proof-logging solver) are intended to make the finite claim independently
checkable by a standard DRAT checker.
"""

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path

from pysat.formula import CNF
from pysat.solvers import Solver


ROOT = Path(__file__).resolve().parent
SUMMARY_PATH = ROOT / "rref_hypergraph_summary.json"
EDGE_PATH = ROOT / "forbidden_triples_u8.bin"
CNF_PATH = ROOT / "product_above_bound.cnf"
PROOF_PATH = ROOT / "product_above_bound.drat"
RESULT_PATH = ROOT / "cnf_product_threshold_result.json"
TARGET = 42_876


def span_mask(basis: list[int]) -> int:
    vectors = [0]
    for row in basis:
        vectors += [vector ^ row for vector in vectors]
    return sum(1 << vector for vector in vectors)


def minimal_sorted_product_boundary() -> list[tuple[int, int, int]]:
    boundary = []
    for first in range(1, 156):
        for second in range(1, first + 1):
            for third in range(1, second + 1):
                if first * second * third < TARGET:
                    continue
                if (
                    (first - 1) * second * third < TARGET
                    and first * (second - 1) * third < TARGET
                    and first * second * (third - 1) < TARGET
                ):
                    boundary.append((first, second, third))
    # Exhaustively validate the boundary representation over the complete
    # cardinality cube after sorting.
    for first in range(1, 156):
        for second in range(1, first + 1):
            for third in range(1, second + 1):
                represented = any(
                    first >= a and second >= b and third >= c
                    for a, b, c in boundary
                )
                assert represented == (first * second * third >= TARGET)
    return boundary


class Encoder:
    def __init__(self, top_id: int):
        self.cnf = CNF()
        self.top_id = top_id
        self.comparators = 0

    def new_var(self) -> int:
        self.top_id += 1
        return self.top_id

    def comparator(self, first: int, second: int) -> tuple[int, int]:
        """Return exact Boolean (first OR second, first AND second)."""
        high, low = self.new_var(), self.new_var()
        self.cnf.extend([
            [-first, high],
            [-second, high],
            [first, second, -high],
            [first, -low],
            [second, -low],
            [-first, -second, low],
        ])
        self.comparators += 1
        return high, low

    def insertion_sort_descending(self, inputs: list[int]) -> list[int]:
        wires = inputs[:]
        for right in range(1, len(wires)):
            for position in range(right, 0, -1):
                wires[position - 1], wires[position] = self.comparator(
                    wires[position - 1], wires[position]
                )
        return wires


def main() -> None:
    start = time.monotonic()
    summary = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
    edge_data = EDGE_PATH.read_bytes()
    assert hashlib.sha256(edge_data).hexdigest() == summary["edge_file_sha256"]
    assert len(edge_data) == 3 * summary["edge_count"]
    masks = [span_mask(basis) for basis in summary["rref_bases"]]
    assert len(masks) == 155

    # Variables 1..465 are family membership bits.
    families = [
        list(range(part * 155 + 1, (part + 1) * 155 + 1))
        for part in range(3)
    ]
    encoder = Encoder(top_id=465)
    outputs = [
        encoder.insertion_sort_descending(variables)
        for variables in families
    ]

    # The exact unary outputs allow lossless ordering of the three sizes.
    for threshold in range(155):
        encoder.cnf.append([-outputs[1][threshold], outputs[0][threshold]])
        encoder.cnf.append([-outputs[2][threshold], outputs[1][threshold]])

    # Normalize one selected member of part 0, and one stabilizer orbit in
    # part 1, exactly as in the independent CP-SAT model.
    encoder.cnf.append([families[0][0]])
    representatives = {}
    for index, mask in enumerate(masks):
        dimension = (masks[0] & mask).bit_count().bit_length() - 1
        representatives.setdefault(dimension, index)
    assert set(representatives) == {1, 2, 3}
    encoder.cnf.append([
        families[1][representatives[dimension]] for dimension in (1, 2, 3)
    ])

    # Exact forbidden-triple clauses, decoded from the separately generated
    # and dual/primal-cross-checked hypergraph.
    view = memoryview(edge_data)
    for position in range(0, len(view), 3):
        encoder.cnf.append([
            -families[0][view[position]],
            -families[1][view[position + 1]],
            -families[2][view[position + 2]],
        ])

    boundary = minimal_sorted_product_boundary()
    assert len(boundary) == 829
    term_variables = []
    for first, second, third in boundary:
        literals = (
            outputs[0][first - 1],
            outputs[1][second - 1],
            outputs[2][third - 1],
        )
        term = encoder.new_var()
        term_variables.append(term)
        for literal in literals:
            encoder.cnf.append([-term, literal])
        encoder.cnf.append([term, *(-literal for literal in literals)])
    encoder.cnf.append(term_variables)

    build_seconds = time.monotonic() - start
    encoder.cnf.to_file(CNF_PATH)
    cnf_hash = hashlib.sha256(CNF_PATH.read_bytes()).hexdigest()
    write_seconds = time.monotonic() - start - build_seconds

    solver_name = os.environ.get("SAT_SOLVER", "cadical195")
    with_proof = os.environ.get("SAT_PROOF", "0") == "1"
    solver_start = time.monotonic()
    with Solver(
        name=solver_name,
        bootstrap_with=encoder.cnf.clauses,
        with_proof=with_proof,
    ) as solver:
        satisfiable = solver.solve()
        model = solver.get_model() if satisfiable else None
        proof = solver.get_proof() if with_proof and not satisfiable else None
    solve_seconds = time.monotonic() - solver_start

    proof_hash = None
    proof_lines = None
    if proof is not None:
        PROOF_PATH.write_text("\n".join(proof) + "\n", encoding="ascii")
        proof_hash = hashlib.sha256(PROOF_PATH.read_bytes()).hexdigest()
        proof_lines = len(proof)

    result = {
        "solver": solver_name,
        "status": "SATISFIABLE" if satisfiable else "UNSATISFIABLE",
        "encoding": "pure CNF with exact Boolean sorting networks",
        "target_product_at_least": TARGET,
        "edge_file_sha256": summary["edge_file_sha256"],
        "variables": encoder.top_id,
        "clauses": len(encoder.cnf.clauses),
        "comparators": encoder.comparators,
        "minimal_product_boundary_triples": len(boundary),
        "cnf_file": CNF_PATH.name,
        "cnf_sha256": cnf_hash,
        "proof_requested": with_proof,
        "proof_file": PROOF_PATH.name if proof is not None else None,
        "proof_sha256": proof_hash,
        "proof_lines": proof_lines,
        "build_seconds": build_seconds,
        "write_seconds": write_seconds,
        "solve_seconds": solve_seconds,
        "wall_seconds": time.monotonic() - start,
    }
    if model is not None:
        positive = set(literal for literal in model if literal > 0)
        selected = [
            [index for index, variable in enumerate(variables)
             if variable in positive]
            for variables in families
        ]
        counts = [len(part) for part in selected]
        result.update({
            "counts": counts,
            "product": counts[0] * counts[1] * counts[2],
            "selected_vertex_indices": selected,
        })
    RESULT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
