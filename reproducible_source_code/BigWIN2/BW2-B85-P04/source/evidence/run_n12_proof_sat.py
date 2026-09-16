#!/usr/bin/env python3
"""Run a PySAT solver with DRUP/DRAT tracing on the frozen n=12 CNF."""

import argparse
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import shutil
from time import monotonic

import pysat
from pysat.formula import CNF
from pysat.solvers import Glucose4, Lingeling, MapleChrono, MapleCM, Maplesat


HERE = Path(__file__).resolve().parent
CNF_PATH = HERE / "n12.cnf"
SOLVERS = {
    "glucose4": Glucose4,
    "lingeling": Lingeling,
    "maplechrono": MapleChrono,
    "maplecm": MapleCM,
    "maplesat": Maplesat,
}


def write_coloring(model):
    assignment = {abs(x): x > 0 for x in model}
    vertices = list(combinations(range(1, 13), 3))
    edges = []
    for i, a in enumerate(vertices):
        for j in range(i + 1, len(vertices)):
            if set(a).isdisjoint(vertices[j]):
                edges.append((a, vertices[j]))
    assert len(edges) == 9240 and all(i in assignment for i in range(1, 9241))
    lines = [
        "# Complete edge coloring of KG(12,3)",
        "# Format: endpoint_A endpoint_B color; endpoints are sorted triples",
        "# Variable order is the canonical order in generate_n12_cnf.py",
    ]
    for variable, (a, b) in enumerate(edges, 1):
        aa = ",".join(map(str, a))
        bb = ",".join(map(str, b))
        lines.append(f"{aa} {bb} {'R' if assignment[variable] else 'B'}")
    target = HERE / "n12_coloring.txt"
    target.write_text("\n".join(lines) + "\n", encoding="ascii")
    return target


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--solver", choices=sorted(SOLVERS), default="maplechrono")
    parser.add_argument("--conf-budget", type=int)
    args = parser.parse_args()
    formula = CNF(from_file=str(CNF_PATH))
    started = monotonic()
    SolverClass = SOLVERS[args.solver]
    with SolverClass(bootstrap_with=formula.clauses, with_proof=True, use_timer=True) as solver:
        if args.conf_budget is not None:
            solver.conf_budget(args.conf_budget)
            result = solver.solve_limited()
        else:
            result = solver.solve()
        elapsed = monotonic() - started
        record = {
            "solver": args.solver,
            "pysat_version": pysat.__version__,
            "conflict_budget": args.conf_budget,
            "result": "SAT" if result is True else "UNSAT" if result is False else "UNKNOWN",
            "solver_cpu_seconds": solver.time(),
            "wall_seconds": elapsed,
            "stats": solver.accum_stats(),
            "cnf_sha256": sha256(CNF_PATH.read_bytes()).hexdigest(),
        }
        if result is True:
            target = write_coloring(solver.get_model())
            record["coloring_file"] = "evidence/n12_coloring.txt"
            record["coloring_sha256"] = sha256(target.read_bytes()).hexdigest()
        elif result is False:
            solver.prfile.flush()
            solver.prfile.seek(0)
            target = HERE / "n12.drat"
            with target.open("wb") as stream:
                shutil.copyfileobj(solver.prfile, stream)
            record["proof_file"] = "evidence/n12.drat"
            record["proof_bytes"] = target.stat().st_size
            record["proof_sha256"] = sha256(target.read_bytes()).hexdigest()
    output = HERE / "n12_solver_run.json"
    output.write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="ascii")
    print(json.dumps(record, sort_keys=True))


if __name__ == "__main__":
    main()
