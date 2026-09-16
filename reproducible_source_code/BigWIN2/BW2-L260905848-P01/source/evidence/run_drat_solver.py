#!/usr/bin/env python3
"""Run a proof-logging SAT solver on the frozen product-threshold CNF.

The proof is kept in binary DRAT form and streamed out of PySAT's temporary
trace file; this avoids materializing a multi-gigabyte textual trace in RAM.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import time
from pathlib import Path

from pysat.formula import CNF
from pysat.solvers import Solver


ROOT = Path(__file__).resolve().parent
CNF_PATH = ROOT / "product_above_bound.cnf"
PROOF_PATH = ROOT / "product_above_bound.bdrat"
RESULT_PATH = ROOT / "drat_solver_result.json"
EXPECTED_CNF_SHA256 = "5a04264cfb4b6deaa3ea5b280eab1ba83a483e4ecba86455b4c0475cc0257760"


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as input_file:
        for block in iter(lambda: input_file.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    start = time.monotonic()
    cnf_hash = file_sha256(CNF_PATH)
    assert cnf_hash == EXPECTED_CNF_SHA256
    cnf = CNF(from_file=CNF_PATH)
    parse_seconds = time.monotonic() - start
    solver_start = time.monotonic()
    with Solver(name="cadical195", bootstrap_with=cnf.clauses, with_proof=True) as solver:
        satisfiable = solver.solve()
        # PySAT's get_proof() materializes and decodes the whole trace in RAM.
        # Copy CaDiCaL's binary DRAT stream to durable evidence in bounded RAM.
        if not satisfiable:
            solver.solver.prfile.flush()
            solver.solver.prfile.seek(0)
            with PROOF_PATH.open("wb") as proof_file:
                shutil.copyfileobj(
                    solver.solver.prfile, proof_file, length=1024 * 1024
                )
    solve_seconds = time.monotonic() - solver_start
    assert not satisfiable
    assert PROOF_PATH.is_file() and PROOF_PATH.stat().st_size > 0
    result = {
        "solver": "CaDiCaL 1.9.5 via PySAT 1.8.dev24",
        "status": "UNSATISFIABLE",
        "cnf_file": CNF_PATH.name,
        "cnf_sha256": cnf_hash,
        "variables": cnf.nv,
        "clauses": len(cnf.clauses),
        "proof_file": PROOF_PATH.name,
        "proof_format": "binary DRAT",
        "proof_bytes": PROOF_PATH.stat().st_size,
        "proof_sha256": file_sha256(PROOF_PATH),
        "parse_seconds": parse_seconds,
        "solve_seconds": solve_seconds,
        "wall_seconds": time.monotonic() - start,
        "proof_verified": False,
        "proof_verification_note": "Run drat-trim -i separately; solver output alone is not verification.",
    }
    RESULT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
