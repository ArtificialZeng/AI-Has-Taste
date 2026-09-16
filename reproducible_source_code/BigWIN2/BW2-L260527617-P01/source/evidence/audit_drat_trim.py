#!/usr/bin/env python3
"""Replay every archived CNF/DRUP pair with drat-trim.

The audit is deliberately independent of ``check_drup.py``.  Acceptance of a
case requires both process exit code zero and an exact ``s VERIFIED`` output
line.  The JSON report binds that verdict to SHA-256 digests of the CNF, proof,
checker executable, and raw checker output.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys


CASES = (
    "L10_22222",
    "L12_22224",
    "L14_22226",
    "L14_22244",
    "L16_22228",
    "L16_22246",
    "L16_22444",
    "L18_222210",
    "L18_22248",
    "L18_22266",
    "L18_22446",
    "L18_24444",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def atomic_write(path: Path, data: bytes) -> None:
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(data)
    os.replace(temporary, path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--drat-trim", default="/home/ailab/.local/bin/drat-trim"
    )
    parser.add_argument("--evidence-dir", default="evidence")
    parser.add_argument(
        "--json", default="evidence/drat_trim_audit.json"
    )
    parser.add_argument(
        "--log", default="evidence/drat_trim_replay.log"
    )
    args = parser.parse_args()

    evidence_dir = Path(args.evidence_dir)
    checker = Path(args.drat_trim).resolve()
    if not checker.is_file():
        parser.error(f"drat-trim executable not found: {checker}")

    records = []
    log_parts = []
    all_verified = True
    for case in CASES:
        cnf = evidence_dir / f"{case}.cnf"
        proof = evidence_dir / f"{case}.drup"
        if not cnf.is_file() or not proof.is_file():
            parser.error(f"missing certificate pair for {case}")
        command = [str(checker), str(cnf), str(proof), "-w"]
        process = subprocess.run(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        output = process.stdout
        lines = output.decode("ascii", errors="replace").splitlines()
        marker_count = sum(line.strip() == "s VERIFIED" for line in lines)
        verified = process.returncode == 0 and marker_count == 1
        all_verified = all_verified and verified
        record = {
            "case": case,
            "cnf": cnf.as_posix(),
            "cnf_sha256": sha256(cnf),
            "proof": proof.as_posix(),
            "proof_sha256": sha256(proof),
            "exit_code": process.returncode,
            "verified_marker": marker_count == 1,
            "verified_marker_count": marker_count,
            "result": "verified" if verified else "rejected",
            "raw_output_sha256": sha256_bytes(output),
        }
        records.append(record)
        log_parts.append(
            f"===== {case} =====\n"
            f"command={' '.join(command)}\n"
            f"cnf_sha256={record['cnf_sha256']}\n"
            f"proof_sha256={record['proof_sha256']}\n"
            f"exit_code={process.returncode}\n"
            f"verified_marker_count={marker_count}\n"
            f"raw_output_sha256={record['raw_output_sha256']}\n"
            + output.decode("ascii", errors="replace").replace("\r", "\n")
            + "\n"
        )
        print(
            case,
            f"exit={process.returncode}",
            f"marker_count={marker_count}",
            f"result={record['result']}",
            flush=True,
        )

    report = {
        "schema_version": 1,
        "audit": "independent drat-trim replay of archived CNF/DRUP pairs",
        "checked_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "python": platform.python_version(),
        "platform": platform.platform(),
        "drat_trim": str(checker),
        "drat_trim_sha256": sha256(checker),
        "required_conditions": {
            "exit_code": 0,
            "exact_output_line": "s VERIFIED",
            "exact_output_line_count": 1,
        },
        "case_count": len(records),
        "all_verified": all_verified,
        "cases": records,
    }
    atomic_write(Path(args.json), (json.dumps(report, indent=2) + "\n").encode())
    atomic_write(Path(args.log), "".join(log_parts).encode())
    print(f"ALL_VERIFIED={str(all_verified).lower()} cases={len(records)}")
    return 0 if all_verified else 1


if __name__ == "__main__":
    sys.exit(main())
