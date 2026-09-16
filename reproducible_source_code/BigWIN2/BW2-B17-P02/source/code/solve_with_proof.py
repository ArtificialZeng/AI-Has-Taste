#!/usr/bin/env python3
"""Solve a DIMACS CNF with CaDiCaL 1.9.5 through PySAT and save DRAT."""
from __future__ import annotations

import argparse
import json
import time
from pathlib import Path
from pysat.formula import CNF
from pysat.solvers import Solver


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cnf", type=Path)
    ap.add_argument("proof", type=Path)
    ap.add_argument("log", type=Path)
    args = ap.parse_args()
    formula = CNF(from_file=str(args.cnf))
    started = time.time()
    with Solver(name="cadical195", bootstrap_with=formula.clauses,
                with_proof=True) as solver:
        sat = solver.solve()
        stats = solver.accum_stats()
        proof = None if sat else solver.get_proof()
    elapsed = time.time() - started
    record = {"solver": "CaDiCaL 1.9.5 via python-sat", "sat": sat,
              "elapsed_seconds": elapsed, "stats": stats,
              "proof_lines": None if proof is None else len(proof)}
    args.log.parent.mkdir(parents=True, exist_ok=True)
    args.log.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    if proof is not None:
        args.proof.parent.mkdir(parents=True, exist_ok=True)
        args.proof.write_text("\n".join(proof) + "\n", encoding="ascii")
    print(json.dumps(record, sort_keys=True))
    raise SystemExit(10 if sat else 20)


if __name__ == "__main__":
    main()
