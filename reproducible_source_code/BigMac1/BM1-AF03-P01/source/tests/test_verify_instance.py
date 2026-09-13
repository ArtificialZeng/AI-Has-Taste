#!/usr/bin/env python3
"""Acceptance and rejection tests for the no-import CNF verifier."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VERIFIER = ROOT / "verification" / "verify_instance.py"
VALID = ROOT / "instances" / "ekr_k4d3_n9.cnf"


def run(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VERIFIER), str(path), "--n", "9"],
        text=True,
        capture_output=True,
        check=False,
    )


def expect_rejection(directory: Path, name: str, content: str | bytes) -> None:
    path = directory / name
    if isinstance(content, bytes):
        path.write_bytes(content)
    else:
        path.write_text(content, encoding="ascii")
    result = run(path)
    if result.returncode == 0 or "REJECTED:" not in result.stderr:
        raise AssertionError(f"mutation {name} was not fail-closed: {result}")


def main() -> int:
    original = VALID.read_text(encoding="ascii")
    accepted = run(VALID)
    if accepted.returncode != 0 or "VERIFIED_CANONICAL_INSTANCE" not in accepted.stdout:
        raise AssertionError(f"valid instance rejected: {accepted}")
    lines = original.splitlines()
    header_index = next(i for i, line in enumerate(lines) if line.startswith("p cnf"))
    first_clause = header_index + 1
    with tempfile.TemporaryDirectory(prefix="ekr-verifier-mutations-") as tmp:
        directory = Path(tmp)
        changed = list(lines)
        parts = changed[header_index].split()
        parts[3] = str(int(parts[3]) + 1)
        changed[header_index] = " ".join(parts)
        expect_rejection(directory, "bad_header.cnf", "\n".join(changed) + "\n")

        changed = list(lines)
        changed.pop(first_clause)
        parts = changed[header_index].split()
        parts[3] = str(int(parts[3]) - 1)
        changed[header_index] = " ".join(parts)
        expect_rejection(directory, "missing_clause.cnf", "\n".join(changed) + "\n")

        changed = list(lines)
        literals = changed[first_clause].split()
        literals[0] = str(-int(literals[0]))
        changed[first_clause] = " ".join(literals)
        expect_rejection(directory, "flipped_literal.cnf", "\n".join(changed) + "\n")

        changed = list(lines)
        literals = changed[first_clause].split()
        changed[first_clause] = " ".join([literals[0], literals[0], *literals[1:]])
        expect_rejection(directory, "duplicate_literal.cnf", "\n".join(changed) + "\n")

        expect_rejection(
            directory,
            "non_ascii.cnf",
            original.replace("canonical", "canónical").encode("utf-8"),
        )
    print("PASS: valid instance accepted; 5 malformed/mutated instances rejected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
