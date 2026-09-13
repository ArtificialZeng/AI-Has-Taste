#!/usr/bin/env python3
"""Fail-closed wrapper around a pinned independent LRAT checker."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
INSTANCE_VERIFIER = ROOT / "verification" / "verify_instance.py"
CHECKER_DIR = ROOT / "verification" / "third_party" / "drat-trim"
EXPECTED_SOURCES = {
    "LICENSE": "71ab2a9dc5a294ad8fba4ccb8c45aaa8a439596d314a2a046ac9b62266872a18",
    "Makefile": "1f3c7128b1dd739723257edd95cc28a2ee747779ca01ae80ed9252f02ec5149d",
    "README.md": "fa0b7c5b81b332aad990a1980c5d7a5fda41b153159cf331982bf36d87483054",
    "lrat-check.c": "bf07c2ac96b9035da1ebcc578cb95e956a2b795629d613154cdb307f8a8f4a95",
}
PINNED_COMMIT = "2e3b2dc0ecf938addbd779d42877b6ed69d9a985"
C_INT_MAX = 2_147_483_647


class VerificationError(Exception):
    pass


def sha256(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError as exc:
        raise VerificationError(f"cannot hash {path}: {exc}") from exc


def check_pinned_checker_sources() -> tuple[dict[str, str], bytes]:
    checker_source = b""
    for filename, expected in EXPECTED_SOURCES.items():
        path = CHECKER_DIR / filename
        try:
            raw = path.read_bytes()
        except OSError as exc:
            raise VerificationError(f"cannot read pinned checker source {path}: {exc}") from exc
        actual = hashlib.sha256(raw).hexdigest()
        if actual != expected:
            raise VerificationError(
                f"pinned checker source hash mismatch for {filename}: {actual}"
            )
        if filename == "lrat-check.c":
            checker_source = raw
    return (
        {
            "checker_commit": PINNED_COMMIT,
            "checker_source_sha256": EXPECTED_SOURCES["lrat-check.c"],
        },
        checker_source,
    )


def compile_pinned_checker(source_bytes: bytes, destination: Path) -> dict[str, object]:
    source_snapshot = destination.with_suffix(".c")
    source_snapshot.write_bytes(source_bytes)
    command = [
        "cc",
        str(source_snapshot),
        "-std=c99",
        "-DLONGTYPE",
        "-O2",
        "-o",
        str(destination),
    ]
    compiled = subprocess.run(
        command,
        text=True,
        capture_output=True,
        check=False,
        timeout=60,
    )
    if compiled.returncode != 0 or not destination.is_file():
        diagnostic = (compiled.stdout + compiled.stderr).strip().replace("\n", " | ")
        raise VerificationError(f"failed to compile pinned LRAT checker source: {diagnostic}")
    return {
        "checker_build_command": [
            "cc", "<verified-source-snapshot>", "-std=c99", "-DLONGTYPE",
            "-O2", "-o", "<fresh-temporary-executable>",
        ],
        "checker_binary_sha256": sha256(destination),
    }


def check_strict_lrat_syntax(
    proof: Path, variable_count: int, original_clause_count: int
) -> tuple[int, int]:
    try:
        raw = proof.read_bytes()
        text = raw.decode("ascii")
    except (OSError, UnicodeError) as exc:
        raise VerificationError(f"proof is not readable strict ASCII: {exc}") from exc
    if not raw or not text.endswith("\n"):
        raise VerificationError("proof must be nonempty and newline-terminated")
    lines = text.splitlines()
    if not lines or any(not line.strip() for line in lines):
        raise VerificationError("blank LRAT lines are forbidden")
    final_empty = False
    addition_count = 0
    deletion_count = 0
    last_addition_id = original_clause_count
    active_clause_ids = set(range(1, original_clause_count + 1))
    for line_number, line in enumerate(lines, 1):
        tokens = line.split()
        try:
            step_id = int(tokens[0])
        except (IndexError, ValueError) as exc:
            raise VerificationError(f"invalid step id at line {line_number}") from exc
        if step_id <= 0:
            raise VerificationError(f"nonpositive step id at line {line_number}")
        if step_id > C_INT_MAX:
            raise VerificationError(f"step id exceeds checker integer range at line {line_number}")
        if len(tokens) >= 2 and tokens[1] == "d":
            deletion_count += 1
            if len(tokens) < 4 or tokens[-1] != "0" or tokens[2:-1].count("0"):
                raise VerificationError(f"malformed deletion at line {line_number}")
            try:
                deleted = [int(token) for token in tokens[2:-1]]
            except ValueError as exc:
                raise VerificationError(f"noninteger deletion hint at line {line_number}") from exc
            if any(index <= 0 for index in deleted):
                raise VerificationError(f"nonpositive deletion target at line {line_number}")
            if any(index > C_INT_MAX for index in deleted):
                raise VerificationError(f"deletion target exceeds checker integer range at line {line_number}")
            if step_id != last_addition_id:
                raise VerificationError(
                    f"deletion id does not equal the latest addition id at line {line_number}"
                )
            if len(set(deleted)) != len(deleted):
                raise VerificationError(f"duplicate deletion target at line {line_number}")
            missing = [index for index in deleted if index not in active_clause_ids]
            if missing:
                raise VerificationError(
                    f"deletion targets inactive/nonexistent clause {missing[0]} at line {line_number}"
                )
            active_clause_ids.difference_update(deleted)
            final_empty = False
            continue
        try:
            values = [int(token) for token in tokens[1:]]
        except ValueError as exc:
            raise VerificationError(f"noninteger addition data at line {line_number}") from exc
        if values.count(0) != 2 or values[-1] != 0:
            raise VerificationError(f"addition needs exactly two zero delimiters at line {line_number}")
        delimiter = values.index(0)
        literals = values[:delimiter]
        hints = values[delimiter + 1 : -1]
        if any(literal == 0 for literal in literals) or any(hint == 0 for hint in hints):
            raise VerificationError(f"embedded zero at line {line_number}")
        if any(abs(hint) > C_INT_MAX for hint in hints):
            raise VerificationError(f"hint exceeds checker integer range at line {line_number}")
        if step_id <= last_addition_id:
            raise VerificationError(f"addition ids are not strictly increasing at line {line_number}")
        if any(abs(literal) > variable_count for literal in literals):
            raise VerificationError(f"literal out of range at line {line_number}")
        if len(set(literals)) != len(literals):
            raise VerificationError(f"duplicate literal at line {line_number}")
        if any(-literal in literals for literal in literals):
            raise VerificationError(f"tautological addition at line {line_number}")
        missing_hints = [hint for hint in hints if abs(hint) not in active_clause_ids]
        if missing_hints:
            raise VerificationError(
                f"hint references inactive/nonexistent clause {missing_hints[0]} at line {line_number}"
            )
        last_addition_id = step_id
        active_clause_ids.add(step_id)
        addition_count += 1
        final_empty = len(literals) == 0
    if not final_empty:
        raise VerificationError("last LRAT line is not an empty-clause addition")
    return addition_count, deletion_count


def verify(cnf: Path, proof: Path, n: int) -> dict[str, object]:
    if n not in (9, 10):
        raise VerificationError("UNSAT endpoint verification is restricted to n=9 or n=10")
    checker_record, checker_source = check_pinned_checker_sources()
    with tempfile.TemporaryDirectory(prefix="ekr-fresh-lrat-checker-") as directory:
        temporary = Path(directory)
        cnf_snapshot = temporary / "instance.cnf"
        proof_snapshot = temporary / "proof.lrat"
        cnf_snapshot.write_bytes(cnf.read_bytes())
        proof_snapshot.write_bytes(proof.read_bytes())
        instance = subprocess.run(
            [sys.executable, str(INSTANCE_VERIFIER), str(cnf_snapshot), "--n", str(n)],
            text=True,
            capture_output=True,
            check=False,
            timeout=60,
        )
        if instance.returncode != 0:
            raise VerificationError(
                f"canonical instance verification failed: {instance.stderr.strip()}"
            )
        try:
            instance_record = json.loads(instance.stdout)
        except json.JSONDecodeError as exc:
            raise VerificationError("canonical instance verifier emitted non-JSON output") from exc
        expected_instance_hash = sha256(cnf_snapshot)
        expected_proof_hash = sha256(proof_snapshot)
        expected_verifier_hash = sha256(INSTANCE_VERIFIER)
        required_instance_record = {
            "status": "VERIFIED_CANONICAL_INSTANCE",
            "n": n,
            "cnf_sha256": expected_instance_hash,
            "verifier_sha256": expected_verifier_hash,
        }
        if not isinstance(instance_record, dict) or any(
            instance_record.get(key) != value for key, value in required_instance_record.items()
        ):
            raise VerificationError("canonical instance verifier returned an inconsistent record")
        variables = instance_record.get("variables")
        clauses = instance_record.get("clauses")
        if (
            not isinstance(variables, int) or variables <= 0
            or not isinstance(clauses, int) or clauses <= 0
        ):
            raise VerificationError("canonical instance verifier returned invalid counts")
        additions, deletions = check_strict_lrat_syntax(
            proof_snapshot, variables, clauses
        )
        fresh_checker = temporary / "lrat-check"
        checker_record.update(compile_pinned_checker(checker_source, fresh_checker))
        checked = subprocess.run(
            [str(fresh_checker), str(cnf_snapshot), str(proof_snapshot)],
            text=True,
            capture_output=True,
            check=False,
            timeout=60,
        )
    if (
        checked.returncode != 0
        or "c VERIFIED" not in checked.stdout.splitlines()
        or any("NOT VERIFIED" in line for line in checked.stdout.splitlines())
    ):
        diagnostic = (checked.stdout + checked.stderr).strip().replace("\n", " | ")
        raise VerificationError(f"independent LRAT checker rejected proof: {diagnostic}")
    record: dict[str, object] = {
        "status": "VERIFIED_UNSAT_LRAT",
        "n": n,
        "cnf_sha256": expected_instance_hash,
        "proof_sha256": expected_proof_hash,
        "wrapper_sha256": sha256(Path(__file__)),
        "instance_verifier_sha256": expected_verifier_hash,
        "proof_addition_lines": additions,
        "proof_deletion_lines": deletions,
    }
    record.update(checker_record)
    return record


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("cnf", type=Path)
    parser.add_argument("proof", type=Path)
    parser.add_argument("--n", required=True, type=int)
    args = parser.parse_args()
    try:
        record = verify(args.cnf, args.proof, args.n)
    except (OSError, VerificationError, subprocess.TimeoutExpired) as exc:
        print(f"REJECTED: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(record, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
