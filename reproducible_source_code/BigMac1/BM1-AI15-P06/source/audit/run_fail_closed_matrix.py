#!/usr/bin/env python3
"""Adversarial execution matrix for the three exact audit programs.

The runner creates all tampered inputs in an external temporary directory and
executes every positive and negative case under normal, -O, -I, and -O -I.
It writes nothing to the project and emits one JSON record on standard output.
"""

from __future__ import annotations

import ast
import copy
import datetime as dt
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import NoReturn


ROOT = Path(__file__).resolve().parents[1]
SPARSE_SCRIPT = ROOT / "certificate" / "verify_sparse_gap.py"
SPARSE_INPUT = ROOT / "certificate" / "sparse_gap_claim.json"
WITNESS_SCRIPT = ROOT / "certificate" / "verify_equilateral_witnesses.py"
WITNESS_INPUT = ROOT / "certificate" / "equilateral_witnesses.json"
FRAME_SCRIPT = ROOT / "experiments" / "proof_cut_frame_audit.py"

MODES = {
    "normal": [],
    "optimized": ["-O"],
    "isolated": ["-I"],
    "optimized_isolated": ["-O", "-I"],
}


class MatrixError(Exception):
    """An expected pass/failure semantic was violated."""


def fail(message: str) -> NoReturn:
    raise MatrixError(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def digest_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def digest_path(path: Path) -> str:
    return digest_bytes(path.read_bytes())


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def ast_assert_count(path: Path) -> int:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return sum(isinstance(node, ast.Assert) for node in ast.walk(tree))


def execute_case(
    *,
    name: str,
    script: Path,
    arguments: list[Path],
    expected_pass: bool,
    outside_cwd: Path,
) -> dict[str, object]:
    mode_records = {}
    for mode, flags in MODES.items():
        command = [sys.executable, *flags, str(script), *(str(path) for path in arguments)]
        completed = subprocess.run(
            command,
            cwd=outside_cwd,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=120,
            check=False,
        )
        stdout = completed.stdout.decode("utf-8", errors="replace").strip()
        stderr = completed.stderr.decode("utf-8", errors="replace").strip()
        pass_marker = '"status": "PASS"' in stdout or '"status": "PASS"' in stderr
        fail_marker = '"status": "FAIL"' in stdout or '"status": "FAIL"' in stderr
        if expected_pass:
            require(completed.returncode == 0, f"{name}/{mode}: valid input exited {completed.returncode}")
            require(pass_marker, f"{name}/{mode}: valid input omitted PASS marker")
            require(not fail_marker, f"{name}/{mode}: valid input printed FAIL")
        else:
            require(completed.returncode != 0, f"{name}/{mode}: tampered input exited zero")
            require(not pass_marker, f"{name}/{mode}: tampered input printed PASS")
            require(fail_marker, f"{name}/{mode}: tampered input omitted FAIL marker")
        mode_records[mode] = {
            "command": command,
            "exit_code": completed.returncode,
            "stdout": stdout,
            "stderr": stderr,
            "stdout_sha256": digest_bytes(completed.stdout),
            "stderr_sha256": digest_bytes(completed.stderr),
        }
    return {
        "name": name,
        "expected": "PASS" if expected_pass else "FAIL",
        "script_sha256": digest_path(script),
        "argument_sha256": [digest_path(path) for path in arguments],
        "modes": mode_records,
    }


def main() -> int:
    scripts = [SPARSE_SCRIPT, WITNESS_SCRIPT, FRAME_SCRIPT]
    try:
        for path in [*scripts, SPARSE_INPUT, WITNESS_INPUT]:
            require(path.is_file(), f"missing project artifact: {path}")
        assert_counts = {str(path.relative_to(ROOT)): ast_assert_count(path) for path in scripts}
        require(all(count == 0 for count in assert_counts.values()), f"residual assert statements: {assert_counts}")

        sparse = json.loads(SPARSE_INPUT.read_text(encoding="utf-8"))
        witness = json.loads(WITNESS_INPUT.read_text(encoding="utf-8"))
        cases: list[dict[str, object]] = []
        with tempfile.TemporaryDirectory(prefix="kusner_fail_closed_", dir="/tmp") as temporary:
            outside = Path(temporary).resolve()
            require(ROOT not in outside.parents and outside != ROOT, "temporary directory is inside project")

            def sparse_mutant(name: str, mutate: object) -> Path:
                value = copy.deepcopy(sparse)
                if not callable(mutate):
                    fail("internal sparse mutation is not callable")
                mutate(value)
                path = outside / f"{name}.json"
                write_json(path, value)
                return path

            def witness_mutant(name: str, mutate: object) -> Path:
                value = copy.deepcopy(witness)
                if not callable(mutate):
                    fail("internal witness mutation is not callable")
                mutate(value)
                path = outside / f"{name}.json"
                write_json(path, value)
                return path

            test_specs: list[tuple[str, Path, list[Path], bool]] = [
                ("valid_sparse", SPARSE_SCRIPT, [SPARSE_INPUT], True),
                ("valid_witnesses", WITNESS_SCRIPT, [WITNESS_INPUT], True),
                ("valid_frame_audit", FRAME_SCRIPT, [], True),
                ("sparse_missing_m", SPARSE_SCRIPT, [sparse_mutant("sparse_missing_m", lambda value: value.pop("m"))], False),
                ("sparse_changed_m", SPARSE_SCRIPT, [sparse_mutant("sparse_changed_m", lambda value: value.__setitem__("m", 10))], False),
                ("sparse_changed_d", SPARSE_SCRIPT, [sparse_mutant("sparse_changed_d", lambda value: value.__setitem__("d", 6))], False),
                ("sparse_changed_gap_count", SPARSE_SCRIPT, [sparse_mutant("sparse_changed_gap_count", lambda value: value.__setitem__("excluded_positive_gap_counts", [10, 12]))], False),
                ("witness_missing_points", WITNESS_SCRIPT, [witness_mutant("witness_missing_points", lambda value: value["witnesses"][0].pop("points"))], False),
                ("witness_changed_dimension", WITNESS_SCRIPT, [witness_mutant("witness_changed_dimension", lambda value: value["witnesses"][0].__setitem__("dimension", 4))], False),
                ("witness_changed_distance", WITNESS_SCRIPT, [witness_mutant("witness_changed_distance", lambda value: value["witnesses"][0].__setitem__("common_distance", 3))], False),
                ("witness_changed_coordinate", WITNESS_SCRIPT, [witness_mutant("witness_changed_coordinate", lambda value: value["witnesses"][0]["points"][0].__setitem__(0, 2))], False),
            ]

            frame_text = FRAME_SCRIPT.read_text(encoding="utf-8")
            require(frame_text.count("M = 11\n") == 1, "cannot make unambiguous frame-script mutant")
            frame_mutant = outside / "proof_cut_frame_audit_m12.py"
            frame_mutant.write_text(frame_text.replace("M = 11\n", "M = 12\n", 1), encoding="utf-8")
            test_specs.append(("frame_changed_m", frame_mutant, [], False))

            for name, script, arguments, expected_pass in test_specs:
                cases.append(
                    execute_case(
                        name=name,
                        script=script,
                        arguments=arguments,
                        expected_pass=expected_pass,
                        outside_cwd=outside,
                    )
                )

            record = {
                "status": "PASS",
                "audit": "fail-closed verifier execution matrix",
                "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                "python": sys.version,
                "runner_sha256": digest_path(Path(__file__).resolve()),
                "project_root": str(ROOT),
                "external_workdir": str(outside),
                "external_workdir_inside_project": False,
                "ast_assert_counts": assert_counts,
                "modes": list(MODES),
                "case_count": len(cases),
                "process_count": len(cases) * len(MODES),
                "cases": cases,
            }
        print(json.dumps(record, indent=2, sort_keys=True))
        return 0
    except Exception as exc:
        print(
            json.dumps({"status": "FAIL", "error": f"{type(exc).__name__}: {exc}"}, sort_keys=True),
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
