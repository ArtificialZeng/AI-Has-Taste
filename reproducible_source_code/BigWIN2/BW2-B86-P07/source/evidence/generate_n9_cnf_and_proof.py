#!/usr/bin/env python3
"""Generate the canonical nine-vertex CNF and a Glucose DRUP refutation.

The graph variables are the 36 pairs of vertices in lexicographic order.  For
every five-set and every forbidden local graph, one ten-literal clause excludes
that exact induced pattern.  No symmetry-breaking clauses are used.
"""

from __future__ import annotations

import argparse
import hashlib
from itertools import combinations, permutations
from pathlib import Path

import pysat
from pysat.solvers import Glucose3


EXPECTED_CNF_SHA256 = "70b78d1ae0f25858dd024eda62addf5f7d623a410725026e7a37200bb79f8cc4"
EXPECTED_DRUP_SHA256 = "cdfb10845b6fc6c282095187e9f1af6ec2f02456bbfb32d04cacadfaaeadb760"
LOCAL_VERTICES = tuple(range(5))
LOCAL_PAIRS = tuple(combinations(LOCAL_VERTICES, 2))
LOCAL_PAIR_INDEX = {pair: index for index, pair in enumerate(LOCAL_PAIRS)}
TSTAR_EDGES = ((0, 1), (0, 2), (0, 3), (3, 4))
GLOBAL_PAIRS = tuple(combinations(range(9), 2))
VARIABLE = {pair: index + 1 for index, pair in enumerate(GLOBAL_PAIRS)}


def edge_mask(edges):
    result = 0
    for u, v in edges:
        pair = (u, v) if u < v else (v, u)
        result |= 1 << LOCAL_PAIR_INDEX[pair]
    return result


def tstar_copies():
    return {
        edge_mask((permutation[u], permutation[v]) for u, v in TSTAR_EDGES)
        for permutation in permutations(LOCAL_VERTICES)
    }


def forbidden_masks(copies):
    return tuple(
        pattern
        for pattern in range(1 << len(LOCAL_PAIRS))
        if pattern not in copies
        and any(
            (pattern & copy) == pattern or (pattern & copy) == copy
            for copy in copies
        )
    )


def canonical_clauses():
    copies = tstar_copies()
    forbidden = forbidden_masks(copies)
    clauses = []
    for vertices in combinations(range(9), 5):
        for pattern in forbidden:
            clause = []
            for index, (i, j) in enumerate(LOCAL_PAIRS):
                variable = VARIABLE[(vertices[i], vertices[j])]
                clause.append(-variable if pattern >> index & 1 else variable)
            clauses.append(tuple(clause))
    assert len(copies) == 60
    assert len(forbidden) == 757
    assert len(clauses) == 95_382
    return clauses


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def write_cnf(path, clauses):
    with path.open("w", encoding="ascii", newline="\n") as stream:
        stream.write(f"p cnf {len(GLOBAL_PAIRS)} {len(clauses)}\n")
        for clause in clauses:
            stream.write(" ".join(map(str, clause)))
            stream.write(" 0\n")


def write_proof(path, proof):
    with path.open("w", encoding="ascii", newline="\n") as stream:
        for line in proof:
            stream.write(line.rstrip("\r\n"))
            stream.write("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cnf", type=Path, default=Path("evidence/n9_tstar_exact.cnf"))
    parser.add_argument("--proof", type=Path, default=Path("evidence/n9_tstar_exact.drup"))
    parser.add_argument("--log", type=Path, default=Path("evidence/n9_generation.log"))
    args = parser.parse_args()

    clauses = canonical_clauses()
    write_cnf(args.cnf, clauses)
    cnf_digest = sha256(args.cnf)
    if cnf_digest != EXPECTED_CNF_SHA256:
        raise SystemExit(f"unexpected CNF SHA-256: {cnf_digest}")

    with Glucose3(bootstrap_with=clauses, with_proof=True) as solver:
        satisfiable = solver.solve()
        if satisfiable:
            raise SystemExit("CNF is SAT; no refutation exists")
        proof = solver.get_proof()
        stats = solver.accum_stats()

    if not proof or proof[-1].strip() != "0":
        raise SystemExit("proof does not end with the empty clause")
    write_proof(args.proof, proof)
    proof_digest = sha256(args.proof)
    if proof_digest != EXPECTED_DRUP_SHA256:
        raise SystemExit(f"unexpected DRUP SHA-256: {proof_digest}")

    lines = [
        f"python_sat_version={pysat.__version__}",
        "solver=PySAT Glucose3 with_proof=True",
        "proof_format=textual DRUP/RUP; one clause per line; deletions prefixed by d",
        f"variables={len(GLOBAL_PAIRS)}",
        f"clauses={len(clauses)}",
        f"cnf_sha256={cnf_digest}",
        "satisfiable=false",
        f"proof_lines={len(proof)}",
        f"proof_sha256={proof_digest}",
        f"solver_stats={stats}",
    ]
    args.log.write_text("\n".join(lines) + "\n", encoding="ascii")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
