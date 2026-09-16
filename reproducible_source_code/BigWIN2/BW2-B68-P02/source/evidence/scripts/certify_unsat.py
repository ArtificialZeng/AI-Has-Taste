#!/usr/bin/env python3
"""Emit and replay DRAT certificates for every needed UNSAT classification."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

from pysat.solvers import Solver

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sweep_colorings import ROOT, build_cnf  # noqa: E402

import networkx as nx  # noqa: E402


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save_report(path: Path, records: list[dict], started: float, status: str) -> None:
    report = {
        "script": str(Path(__file__).relative_to(ROOT)),
        "solver": "PySAT glucose3 with_proof=True",
        "checker": "tools/drat-trim (April 21, 2024 source)",
        "checker_source_sha256": sha256(ROOT / "tools" / "drat-trim.c"),
        "checker_binary_sha256": sha256(ROOT / "tools" / "drat-trim"),
        "records": records,
        "record_count": len(records),
        "seconds": round(time.monotonic() - started, 6),
        "status": status,
    }
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")


def main() -> None:
    started = time.monotonic()
    input_path = ROOT / "evidence" / "coloring_witnesses.jsonl"
    report_path = ROOT / "evidence" / "unsat_certification.json"
    base = ROOT / "evidence" / "unsat"
    records: list[dict] = []
    targets = []
    for line in input_path.read_text().splitlines():
        row = json.loads(line)
        if row["classification"] == "A_unsat_observed":
            targets.append((row, "A", False))
        elif row["classification"] == "A_sat_E_unsat_observed":
            targets.append((row, "E", True))

    for target_number, (row, predicate, equitable) in enumerate(targets, 1):
        n, index = row["n"], row["index"]
        directory = base / predicate
        directory.mkdir(parents=True, exist_ok=True)
        stem = f"n{n:02d}_i{index:04d}"
        cnf_path = directory / f"{stem}.cnf"
        proof_path = directory / f"{stem}.drat"
        graph = nx.from_graph6_bytes(row["graph6"].encode("ascii"))
        cnf, _ = build_cnf(graph, equitable=equitable)
        cnf.to_file(str(cnf_path))
        # Formula addition after proof logging is enabled avoids losing a proof
        # when UNSAT is detected while clauses are being imported.
        with Solver(name="glucose3", with_proof=True) as solver:
            solver.append_formula(cnf.clauses)
            sat = solver.solve()
            assert not sat, (predicate, n, index, row["graph6"])
            proof = solver.get_proof()
            assert proof is not None
            proof_path.write_text("\n".join(proof) + "\n", encoding="ascii")

        checked = subprocess.run(
            [str(ROOT / "tools" / "drat-trim"), str(cnf_path), str(proof_path)],
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
        )
        assert checked.returncode == 0, (predicate, n, index, checked.stdout[-2000:])
        assert "s VERIFIED" in checked.stdout, (predicate, n, index, checked.stdout[-2000:])
        records.append(
            {
                "predicate": predicate,
                "n": n,
                "index": index,
                "graph6": row["graph6"],
                "variables": cnf.nv,
                "clauses": len(cnf.clauses),
                "cnf": str(cnf_path.relative_to(ROOT)),
                "cnf_sha256": sha256(cnf_path),
                "proof": str(proof_path.relative_to(ROOT)),
                "proof_sha256": sha256(proof_path),
                "proof_lines": len(proof),
                "checker_last_lines": checked.stdout.strip().splitlines()[-4:],
                "status": "VERIFIED",
            }
        )
        if target_number % 25 == 0:
            save_report(report_path, records, started, f"in progress: {target_number}/{len(targets)}")
            print(f"verified {target_number}/{len(targets)}", flush=True)

    save_report(report_path, records, started, "all DRAT proofs VERIFIED")
    print(json.dumps({"targets": len(targets), "seconds": time.monotonic() - started}, sort_keys=True))


if __name__ == "__main__":
    main()
