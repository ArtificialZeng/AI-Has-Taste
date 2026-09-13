#!/usr/bin/env python3
"""Deterministically rerun the independent breaker route and write its log."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys


HERE = Path(__file__).resolve().parent
PROJECT = HERE.parent.parent
GENERATED = HERE / "generated"


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(command: list[str], expected_codes: set[int]) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        command,
        cwd=PROJECT,
        check=False,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode not in expected_codes:
        raise SystemExit(
            f"unexpected exit {result.returncode} from {command!r}:\n"
            f"stdout={result.stdout}\nstderr={result.stderr}"
        )
    return result


def relative_command(command: list[str]) -> list[str]:
    rendered: list[str] = []
    for token in command:
        try:
            rendered.append(str(Path(token).resolve().relative_to(PROJECT)))
        except (ValueError, OSError):
            rendered.append(token)
    return rendered


def main() -> int:
    solver_string = shutil.which("cadical")
    if solver_string is None:
        raise SystemExit("cadical is required")
    solver = Path(solver_string).resolve()
    GENERATED.mkdir(parents=True, exist_ok=True)
    commands: list[dict[str, object]] = []
    instances: dict[str, object] = {}

    version_result = run([str(solver), "--version"], {0})
    solver_version = version_result.stdout.strip()
    for n in (8, 9, 10):
        generation_command = [
            sys.executable,
            str(HERE / "generate_pb_witness.py"),
            str(n),
            str(GENERATED),
        ]
        generated = run(generation_command, {0})
        commands.append(
            {
                "argv": relative_command(generation_command),
                "exit_code": generated.returncode,
                "stdout": generated.stdout.strip(),
                "stderr": generated.stderr.strip(),
            }
        )
        metadata_path = GENERATED / f"n{n}_witness_pair.metadata.json"
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        status_path = GENERATED / (
            "n8.solver_witness" if n == 8 else f"n{n}.solver_status"
        )
        solve_command = [
            str(solver),
            "-q",
            "--seed=0",
            "-w",
            str(status_path),
            str(GENERATED / f"n{n}_witness_pair.cnf"),
        ]
        solved = run(solve_command, {10, 20})
        commands.append(
            {
                "argv": relative_command(solve_command),
                "exit_code": solved.returncode,
                "stdout": solved.stdout.strip(),
                "stderr": solved.stderr.strip(),
            }
        )
        status_lines = status_path.read_text(encoding="ascii").splitlines()
        status = status_lines[0] if status_lines else ""
        expected_status = "s SATISFIABLE" if n == 8 else "s UNSATISFIABLE"
        if status != expected_status:
            raise SystemExit(f"n={n}: expected {expected_status!r}, got {status!r}")
        instance_record: dict[str, object] = {
            key: metadata[key]
            for key in (
                "primary_variable_count",
                "auxiliary_variable_count",
                "total_variable_count",
                "opb_constraint_count",
                "disjoint_pair_count",
                "triple_count",
                "cnf_clause_count",
                "opb_sha256",
                "cnf_sha256",
            )
        }
        instance_record.update(
            {
                "solver_exit_code": solved.returncode,
                "solver_status": status.removeprefix("s "),
                "solver_output_sha256": digest(status_path),
                "certification_scope": (
                    "literal exact model independently checked"
                    if n == 8
                    else "discovery-only UNSAT status; no proof certificate"
                ),
            }
        )
        instances[str(n)] = instance_record

    family_path = HERE / "n8_literal_family.json"
    extract_command = [
        sys.executable,
        str(HERE / "extract_primary_family.py"),
        "8",
        str(GENERATED / "n8.solver_witness"),
        str(family_path),
    ]
    extracted = run(extract_command, {0})
    commands.append(
        {
            "argv": relative_command(extract_command),
            "exit_code": extracted.returncode,
            "stdout": extracted.stdout.strip(),
            "stderr": extracted.stderr.strip(),
        }
    )
    verify_command = [
        sys.executable,
        str(HERE / "verify_family.py"),
        str(family_path),
    ]
    verified = run(verify_command, {0})
    commands.append(
        {
            "argv": relative_command(verify_command),
            "exit_code": verified.returncode,
            "stdout": verified.stdout.strip(),
            "stderr": verified.stderr.strip(),
        }
    )

    log = {
        "schema_version": 1,
        "route": "breaker exact PB plus witness-pair CNF",
        "determinism": {
            "solver_seed": 0,
            "timings_omitted": True,
            "instances_and_variable_order": "lexicographic",
        },
        "environment": {
            "python": platform.python_version(),
            "solver": "cadical",
            "solver_version": solver_version,
            "solver_binary_sha256": digest(solver),
        },
        "source_sha256": {
            path.name: digest(path)
            for path in (
                HERE / "generate_pb_witness.py",
                HERE / "extract_primary_family.py",
                HERE / "verify_family.py",
                HERE / "rerun.py",
            )
        },
        "instances": instances,
        "n8_literal_verification": json.loads(verified.stdout),
        "commands": commands,
    }
    (HERE / "run_log.json").write_text(
        json.dumps(log, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(log["instances"], sort_keys=True))
    print(verified.stdout.strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
