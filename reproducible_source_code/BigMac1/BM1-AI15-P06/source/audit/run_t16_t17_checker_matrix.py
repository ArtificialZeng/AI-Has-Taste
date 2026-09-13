#!/usr/bin/env python3
"""External execution and tamper matrix for the frozen t=16 and t=17 checks.

Each checker is copied with its bound proof into a temporary directory outside
the project.  The genuine copy and a one-byte proof mutation are then run in
normal, optimized, isolated, and optimized-isolated Python modes.  Every
decisive runner check uses an explicit exception path.
"""

from __future__ import annotations

import ast
import datetime as dt
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import NoReturn


ROOT = Path(__file__).resolve().parents[1]
CASES = {
    "t16": (
        ROOT / "audit" / "referee_t16_check_postfix.py",
        ROOT / "proof" / "t16_branch.md",
    ),
    "t17": (
        ROOT / "audit" / "referee_t17_check.py",
        ROOT / "proof" / "t17_branch.md",
    ),
}
MODES = {
    "normal": [],
    "optimized": ["-O"],
    "isolated": ["-I"],
    "optimized_isolated": ["-O", "-I"],
}


class MatrixFailure(Exception):
    """The expected fail-closed execution semantics were violated."""


def fail(message: str) -> NoReturn:
    raise MatrixFailure(message)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def digest_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def digest_path(path: Path) -> str:
    return digest_bytes(path.read_bytes())


def ast_assert_count(path: Path) -> int:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    return sum(isinstance(node, ast.Assert) for node in ast.walk(tree))


def execute(
    *, name: str, checker: Path, cwd: Path, expected_pass: bool
) -> dict[str, object]:
    modes: dict[str, object] = {}
    for mode, flags in MODES.items():
        command = [sys.executable, *flags, str(checker)]
        completed = subprocess.run(
            command,
            cwd=cwd,
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
            require(completed.returncode == 0, f"{name}/{mode}: genuine input failed")
            require(pass_marker, f"{name}/{mode}: genuine input omitted PASS")
            require(not fail_marker, f"{name}/{mode}: genuine input printed FAIL")
        else:
            require(completed.returncode != 0, f"{name}/{mode}: mutation exited zero")
            require(not pass_marker, f"{name}/{mode}: mutation printed PASS")
            require(fail_marker, f"{name}/{mode}: mutation omitted FAIL")
        modes[mode] = {
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
        "checker_sha256": digest_path(checker),
        "modes": modes,
    }


def main() -> int:
    try:
        for checker, proof in CASES.values():
            require(checker.is_file(), f"missing checker: {checker}")
            require(proof.is_file(), f"missing proof: {proof}")
            require(ast_assert_count(checker) == 0, f"assert found in checker: {checker}")

        records: list[dict[str, object]] = []
        proof_hashes: dict[str, str] = {}
        checker_hashes: dict[str, str] = {}
        assert_counts: dict[str, int] = {}
        with tempfile.TemporaryDirectory(prefix="kusner_t16_t17_", dir="/tmp") as raw_temp:
            outside = Path(raw_temp).resolve()
            require(outside != ROOT and ROOT not in outside.parents, "workdir is inside project")
            for label, (source_checker, source_proof) in CASES.items():
                checker_hashes[label] = digest_path(source_checker)
                proof_hashes[label] = digest_path(source_proof)
                assert_counts[label] = ast_assert_count(source_checker)

                genuine = outside / f"{label}_genuine"
                (genuine / "audit").mkdir(parents=True)
                (genuine / "proof").mkdir()
                checker = genuine / "audit" / source_checker.name
                proof = genuine / "proof" / source_proof.name
                shutil.copyfile(source_checker, checker)
                shutil.copyfile(source_proof, proof)
                records.append(
                    execute(
                        name=f"{label}_genuine",
                        checker=checker,
                        cwd=outside,
                        expected_pass=True,
                    )
                )

                tampered = outside / f"{label}_tampered"
                shutil.copytree(genuine, tampered)
                tampered_proof = tampered / "proof" / source_proof.name
                original = tampered_proof.read_bytes()
                tampered_proof.write_bytes(original + b"\n")
                require(digest_path(tampered_proof) != proof_hashes[label], "mutation did not change hash")
                records.append(
                    execute(
                        name=f"{label}_tampered_proof",
                        checker=tampered / "audit" / source_checker.name,
                        cwd=outside,
                        expected_pass=False,
                    )
                )

            result = {
                "status": "PASS",
                "audit": "external fail-closed t16/t17 checker matrix",
                "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                "python": sys.version,
                "project_root": str(ROOT),
                "external_workdir": str(outside),
                "external_workdir_inside_project": False,
                "runner_sha256": digest_path(Path(__file__).resolve()),
                "checker_sha256": checker_hashes,
                "proof_sha256": proof_hashes,
                "ast_assert_counts": assert_counts,
                "modes": list(MODES),
                "case_count": len(records),
                "process_count": len(records) * len(MODES),
                "cases": records,
            }
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0
    except Exception as exc:
        print(
            json.dumps({"status": "FAIL", "error": f"{type(exc).__name__}: {exc}"}, sort_keys=True),
            file=sys.stderr,
        )
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
