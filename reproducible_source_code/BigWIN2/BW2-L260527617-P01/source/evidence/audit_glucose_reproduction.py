#!/usr/bin/env python3
"""Reproduce all archived CNF/DRUP files with PySAT solver ``glucose3``.

This is a provenance audit, not an UNSAT checker.  It makes fresh temporary
artifacts and requires byte-for-byte equality with every archived pair.  Proof
validity is checked separately by ``audit_drat_trim.py``.
"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import tempfile

import pysat


CASES = (
    ("L10_22222", 10, "2,2,2,2,2"),
    ("L12_22224", 12, "2,2,2,2,4"),
    ("L14_22226", 14, "2,2,2,2,6"),
    ("L14_22244", 14, "2,2,2,4,4"),
    ("L16_22228", 16, "2,2,2,2,8"),
    ("L16_22246", 16, "2,2,2,4,6"),
    ("L16_22444", 16, "2,2,4,4,4"),
    ("L18_222210", 18, "2,2,2,2,10"),
    ("L18_22248", 18, "2,2,2,4,8"),
    ("L18_22266", 18, "2,2,2,6,6"),
    ("L18_22446", 18, "2,2,4,4,6"),
    ("L18_24444", 18, "2,4,4,4,4"),
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def atomic_json(path: Path, value: object) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    os.replace(temporary, path)


def main() -> int:
    project = Path(__file__).resolve().parent.parent
    evidence = project / "evidence"
    generator = evidence / "search_exact_sat.py"
    records = []
    all_identical = True

    with tempfile.TemporaryDirectory(
        prefix="lit260527617-glucose-reproduction-", dir="/tmp"
    ) as directory:
        temporary_dir = Path(directory)
        for case, length, pattern in CASES:
            fresh_cnf = temporary_dir / f"{case}.cnf"
            fresh_proof = temporary_dir / f"{case}.drup"
            command = [
                sys.executable,
                str(generator),
                "--length",
                str(length),
                "--count-pattern",
                pattern,
                "--solver",
                "glucose3",
                "--cnf",
                str(fresh_cnf),
                "--proof",
                str(fresh_proof),
            ]
            process = subprocess.run(
                command,
                cwd=project,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                check=False,
            )
            archived_cnf = evidence / f"{case}.cnf"
            archived_proof = evidence / f"{case}.drup"
            solver_marker = "solver = glucose3" in process.stdout.splitlines()
            unsat_marker = "result = unsat" in process.stdout.splitlines()
            proof_lines = [
                line for line in process.stdout.splitlines()
                if line.startswith("proof_lines = ")
            ]
            positive_proof_lines = (
                len(proof_lines) == 1
                and int(proof_lines[0].split("=", 1)[1]) > 0
            )
            cnf_identical = (
                process.returncode == 0
                and fresh_cnf.is_file()
                and fresh_cnf.read_bytes() == archived_cnf.read_bytes()
            )
            proof_identical = (
                process.returncode == 0
                and fresh_proof.is_file()
                and fresh_proof.read_bytes() == archived_proof.read_bytes()
            )
            reproduced = all(
                (
                    process.returncode == 0,
                    solver_marker,
                    unsat_marker,
                    positive_proof_lines,
                    cnf_identical,
                    proof_identical,
                )
            )
            all_identical = all_identical and reproduced
            record = {
                "case": case,
                "length": length,
                "count_pattern": [int(value) for value in pattern.split(",")],
                "solver": "glucose3",
                "exit_code": process.returncode,
                "solver_marker": solver_marker,
                "unsat_marker": unsat_marker,
                "positive_proof_lines": positive_proof_lines,
                "cnf": f"evidence/{case}.cnf",
                "cnf_sha256": sha256(archived_cnf),
                "cnf_byte_identical": cnf_identical,
                "proof": f"evidence/{case}.drup",
                "proof_sha256": sha256(archived_proof),
                "proof_byte_identical": proof_identical,
                "result": "reproduced" if reproduced else "mismatch",
            }
            records.append(record)
            print(
                case,
                f"exit={process.returncode}",
                f"cnf_identical={str(cnf_identical).lower()}",
                f"proof_identical={str(proof_identical).lower()}",
                f"result={record['result']}",
                flush=True,
            )

    report = {
        "schema_version": 1,
        "audit": "byte-identical Glucose3 reproduction of archived CNF/DRUP pairs",
        "checked_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "python": platform.python_version(),
        "pysat": pysat.__version__,
        "platform": platform.platform(),
        "generator": "evidence/search_exact_sat.py",
        "generator_sha256": sha256(generator),
        "solver_argument": "glucose3",
        "case_count": len(records),
        "all_byte_identical": all_identical,
        "cases": records,
    }
    atomic_json(evidence / "glucose_reproduction_audit.json", report)
    print(f"ALL_BYTE_IDENTICAL={str(all_identical).lower()} cases={len(records)}")
    return 0 if all_identical else 1


if __name__ == "__main__":
    sys.exit(main())
