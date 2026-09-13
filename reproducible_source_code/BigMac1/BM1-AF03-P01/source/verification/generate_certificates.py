#!/usr/bin/env python3
"""Deterministically regenerate and independently check both endpoint LRATs."""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    version = subprocess.run(
        ["cadical", "--version"], text=True, capture_output=True, check=True
    ).stdout.strip()
    records = []
    for n in (9, 10):
        cnf = ROOT / "instances" / f"ekr_k4d3_n{n}.cnf"
        proof = ROOT / "certificates" / f"ekr_k4d3_n{n}.lrat"
        log = ROOT / "logs" / "run" / f"cadical_n{n}.log"
        command = [
            "cadical", "--seed=0", "--lrat", "--no-binary", "--checkproof=3",
            str(cnf.relative_to(ROOT)), str(proof.relative_to(ROOT)),
        ]
        solved = subprocess.run(
            command, cwd=ROOT, text=True, capture_output=True, check=False
        )
        combined = solved.stdout + solved.stderr
        log.write_text(combined, encoding="utf-8")
        if solved.returncode != 20 or "s UNSATISFIABLE" not in combined:
            raise RuntimeError(f"CaDiCaL did not prove UNSAT for n={n}")
        verify_command = [
            sys.executable,
            str(ROOT / "verification" / "verify_lrat.py"),
            str(cnf), str(proof), "--n", str(n),
        ]
        checked = subprocess.run(
            verify_command, cwd=ROOT, text=True, capture_output=True, check=False
        )
        if checked.returncode != 0:
            raise RuntimeError(f"external verification failed for n={n}: {checked.stderr}")
        verification_record = json.loads(checked.stdout)
        verification_output = ROOT / "certificates" / f"verification_n{n}.json"
        verification_output.write_text(
            json.dumps(verification_record, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        records.append({
            "n": n,
            "solver": "CaDiCaL",
            "solver_version": version,
            "seed": 0,
            "command": command,
            "solver_exit_code": solved.returncode,
            "solver_status": "UNSATISFIABLE",
            "cnf_sha256": digest(cnf),
            "proof_sha256": digest(proof),
            "solver_log_sha256": digest(log),
            "independent_verification": verification_record,
        })
    manifest = {
        "schema_version": 1,
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "objective_convention": (
            "SAT means an intersecting 4-family with every triple degree >=2; "
            "UNSAT means no counterexample exists"
        ),
        "encoding": "canonical no-auxiliary long-clause CNF",
        "runs": records,
    }
    output = ROOT / "logs" / "run" / "certification_run.json"
    output.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
