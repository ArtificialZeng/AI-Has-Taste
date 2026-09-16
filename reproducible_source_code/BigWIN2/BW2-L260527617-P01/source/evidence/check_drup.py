#!/usr/bin/env python3
"""Replay a textual DRUP proof using an independent unit-propagation engine.

The certificates in this directory were emitted through PySAT with solver
name ``glucose3``; see ``provenance-correction.md`` and the byte-identical
reproduction in ``glucose_reproduction_audit.json``.  This checker uses
PySAT's MiniSat 2.2 (or another solver selected on the command line) only as a
watched-literal unit-propagation engine.  For every added clause C it propagates
the assumptions negating all literals of C and demands a conflict before
adding C.

Deletion records are intentionally ignored.  This is sound: retaining an
already checked clause only strengthens the working formula, and induction
shows that every retained learned clause follows from the original CNF.
Acceptance additionally requires a RUP-checked empty-clause addition.
"""

import argparse
import hashlib
import platform
import time

import pysat
from pysat.formula import CNF
from pysat.solvers import Solver


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def proof_steps(path, variables):
    with open(path, "r", encoding="ascii") as handle:
        for line_number, line in enumerate(handle, 1):
            fields = line.split()
            if not fields:
                continue
            deletion = fields[0] == "d"
            number_fields = fields[1:] if deletion else fields
            try:
                numbers = [int(field) for field in number_fields]
            except ValueError as error:
                raise ValueError(f"noninteger on proof line {line_number}") from error
            if not numbers or numbers[-1] != 0 or 0 in numbers[:-1]:
                raise ValueError(f"malformed proof line {line_number}")
            clause = numbers[:-1]
            if any(abs(literal) > variables for literal in clause):
                raise ValueError(f"out-of-range literal on proof line {line_number}")
            yield line_number, deletion, clause


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("cnf")
    parser.add_argument("proof")
    parser.add_argument("--solver", default="minisat22")
    args = parser.parse_args()

    started = time.monotonic()
    formula = CNF(from_file=args.cnf)
    additions = 0
    deletions = 0
    saw_checked_empty = False
    with Solver(name=args.solver, bootstrap_with=formula.clauses) as solver:
        for line_number, deletion, clause in proof_steps(args.proof, formula.nv):
            if deletion:
                deletions += 1
                continue
            additions += 1
            status, _ = solver.propagate(assumptions=[-literal for literal in clause])
            if status is not False:
                raise SystemExit(
                    f"REJECT line={line_number} addition={additions} "
                    f"clause_size={len(clause)} is_not_RUP"
                )
            if not clause:
                saw_checked_empty = True
            solver.add_clause(clause)

    if not saw_checked_empty:
        raise SystemExit("REJECT no RUP-checked empty clause")
    elapsed = time.monotonic() - started
    print(
        "VERIFIED_DRUP",
        f"cnf={args.cnf}",
        f"proof={args.proof}",
        f"cnf_sha256={sha256(args.cnf)}",
        f"proof_sha256={sha256(args.proof)}",
        f"variables={formula.nv}",
        f"base_clauses={len(formula.clauses)}",
        f"additions={additions}",
        f"deletions_ignored={deletions}",
        f"solver={args.solver}",
        f"python={platform.python_version()}",
        f"pysat={pysat.__version__}",
        f"seconds={elapsed:.6f}",
    )


if __name__ == "__main__":
    main()
