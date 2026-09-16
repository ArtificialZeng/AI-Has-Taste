#!/usr/bin/env python3
"""Build and proof-solve the exact non-star equality classification CNF."""

from __future__ import annotations

import hashlib
import json
import shutil
import time
from pathlib import Path

from pysat.formula import CNF
from pysat.solvers import Solver


ROOT = Path(__file__).resolve().parent
SUMMARY_PATH = ROOT / "rref_hypergraph_summary.json"
EDGE_PATH = ROOT / "forbidden_triples_u8.bin"
CNF_PATH = ROOT / "nonstar_equality.cnf"
PROOF_PATH = ROOT / "nonstar_equality.bdrat"
RESULT_PATH = ROOT / "equality_drat_solver_result.json"
TARGET = 35 ** 3


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as input_file:
        for block in iter(lambda: input_file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def span_mask(basis: list[int]) -> int:
    vectors = [0]
    for row in basis:
        vectors += [vector ^ row for vector in vectors]
    return sum(1 << vector for vector in vectors)


class Encoder:
    def __init__(self, top_id: int):
        self.cnf = CNF()
        self.top_id = top_id
        self.comparators = 0

    def new_var(self) -> int:
        self.top_id += 1
        return self.top_id

    def comparator(self, first: int, second: int) -> tuple[int, int]:
        """Return fresh variables exactly equal to OR and AND."""
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
    assert len(edge_data) == 3 * summary["edge_count"]
    assert hashlib.sha256(edge_data).hexdigest() == summary["edge_file_sha256"]
    masks = [span_mask(basis) for basis in summary["rref_bases"]]
    assert len(masks) == len(set(masks)) == 155

    families = [
        list(range(part * 155 + 1, (part + 1) * 155 + 1))
        for part in range(3)
    ]
    encoder = Encoder(top_id=465)
    outputs = [
        encoder.insertion_sort_descending(variables)
        for variables in families
    ]

    # Losslessly order family sizes.
    for threshold in range(155):
        encoder.cnf.append([-outputs[1][threshold], outputs[0][threshold]])
        encoder.cnf.append([-outputs[2][threshold], outputs[1][threshold]])

    # Lossless GL(5,2) and stabilizer normalizations, independently audited by
    # verify_reductions.py.
    encoder.cnf.append([families[0][0]])
    representatives: dict[int, int] = {}
    for index, mask in enumerate(masks):
        dimension = (masks[0] & mask).bit_count().bit_length() - 1
        representatives.setdefault(dimension, index)
    assert representatives == {3: 0, 2: 1, 1: 13}
    encoder.cnf.append([
        families[1][representatives[dimension]]
        for dimension in (1, 2, 3)
    ])

    view = memoryview(edge_data)
    for position in range(0, len(view), 3):
        encoder.cnf.append([
            -families[0][view[position]],
            -families[1][view[position + 1]],
            -families[2][view[position + 2]],
        ])

    equality_size_triples = [
        (first, second, third)
        for first in range(1, 156)
        for second in range(1, first + 1)
        for third in range(1, second + 1)
        if first * second * third == TARGET
    ]
    assert equality_size_triples == [
        (35, 35, 35), (49, 35, 25), (125, 49, 7)
    ]
    equality_terms = []
    for sizes in equality_size_triples:
        literals = []
        for part, size in enumerate(sizes):
            literals.append(outputs[part][size - 1])
            if size < 155:
                literals.append(-outputs[part][size])
        term = encoder.new_var()
        equality_terms.append(term)
        for literal in literals:
            encoder.cnf.append([-term, literal])
        encoder.cnf.append([term, *(-literal for literal in literals)])
    encoder.cnf.append(equality_terms)

    # Each clause is false on exactly one complete 465-bit assignment: all
    # three families equal the full star through the specified nonzero vector.
    excluded_stars = []
    for vector in range(1, 32):
        star = frozenset(
            index for index, mask in enumerate(masks)
            if mask & (1 << vector)
        )
        assert len(star) == 35
        encoder.cnf.append([
            -variable if index in star else variable
            for variables in families
            for index, variable in enumerate(variables)
        ])
        excluded_stars.append(star)
    assert len(set(excluded_stars)) == 31

    build_seconds = time.monotonic() - start
    encoder.cnf.to_file(CNF_PATH)
    cnf_hash = file_sha256(CNF_PATH)
    write_seconds = time.monotonic() - start - build_seconds

    solver_start = time.monotonic()
    with Solver(
        name="cadical195",
        bootstrap_with=encoder.cnf.clauses,
        with_proof=True,
    ) as solver:
        satisfiable = solver.solve()
        model = solver.get_model() if satisfiable else None
        if not satisfiable:
            solver.solver.prfile.flush()
            solver.solver.prfile.seek(0)
            with PROOF_PATH.open("wb") as proof_file:
                shutil.copyfileobj(
                    solver.solver.prfile, proof_file, length=1024 * 1024
                )
    solve_seconds = time.monotonic() - solver_start

    result = {
        "solver": "CaDiCaL 1.9.5 via PySAT 1.8.dev24",
        "status": "SATISFIABLE" if satisfiable else "UNSATISFIABLE",
        "encoding": "pure CNF; exact Boolean sorting networks",
        "required_product": TARGET,
        "sorted_equality_size_triples": equality_size_triples,
        "excluded_exact_common_stars": len(excluded_stars),
        "edge_file_sha256": summary["edge_file_sha256"],
        "variables": encoder.top_id,
        "clauses": len(encoder.cnf.clauses),
        "comparators": encoder.comparators,
        "cnf_file": CNF_PATH.name,
        "cnf_bytes": CNF_PATH.stat().st_size,
        "cnf_sha256": cnf_hash,
        "proof_file": PROOF_PATH.name if not satisfiable else None,
        "proof_format": "binary DRAT" if not satisfiable else None,
        "proof_bytes": PROOF_PATH.stat().st_size if not satisfiable else None,
        "proof_sha256": file_sha256(PROOF_PATH) if not satisfiable else None,
        "build_seconds": build_seconds,
        "write_seconds": write_seconds,
        "solve_seconds": solve_seconds,
        "wall_seconds": time.monotonic() - start,
        "proof_verified": False,
    }
    if model is not None:
        positive = {literal for literal in model if literal > 0}
        selected = [
            [index for index, variable in enumerate(variables)
             if variable in positive]
            for variables in families
        ]
        counts = [len(part) for part in selected]
        assert counts[0] * counts[1] * counts[2] == TARGET
        forbidden = next((
            (first, second, third)
            for first in selected[0]
            for second in selected[1]
            for third in selected[2]
            if (masks[first] & masks[second] & masks[third]).bit_count() == 1
        ), None)
        assert forbidden is None
        assert not any(all(set(part) == star for part in selected)
                       for star in excluded_stars)
        result.update({
            "counts": counts,
            "selected_vertex_indices": selected,
            "independent_primal_replay_passed": True,
        })

    RESULT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
