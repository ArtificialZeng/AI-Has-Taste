#!/usr/bin/env python3
"""Fail-closed verifier for canonical endpoint CNFs.

This program reconstructs the formula directly from the mathematical
definition and deliberately imports no discovery/generator module.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import sys


class VerificationError(Exception):
    pass


def parse_dimacs(path: Path) -> tuple[int, list[tuple[int, ...]]]:
    try:
        raw = path.read_text(encoding="ascii")
    except (OSError, UnicodeError) as exc:
        raise VerificationError(f"cannot read strict ASCII DIMACS: {exc}") from exc
    variables = None
    declared_clauses = None
    clauses: list[tuple[int, ...]] = []
    saw_clause = False
    for line_number, raw_line in enumerate(raw.splitlines(), 1):
        line = raw_line.strip()
        if not line:
            continue
        if line.startswith("c"):
            if saw_clause:
                raise VerificationError(f"comment after clauses at line {line_number}")
            continue
        if line.startswith("p"):
            if variables is not None or saw_clause:
                raise VerificationError(f"misplaced/duplicate header at line {line_number}")
            fields = line.split()
            if len(fields) != 4 or fields[:2] != ["p", "cnf"]:
                raise VerificationError(f"malformed header at line {line_number}")
            try:
                variables, declared_clauses = map(int, fields[2:])
            except ValueError as exc:
                raise VerificationError("noninteger header") from exc
            if variables <= 0 or declared_clauses < 0:
                raise VerificationError("invalid header counts")
            continue
        if variables is None:
            raise VerificationError(f"clause before header at line {line_number}")
        saw_clause = True
        try:
            values = [int(token) for token in line.split()]
        except ValueError as exc:
            raise VerificationError(f"noninteger token at line {line_number}") from exc
        if len(values) < 2 or values[-1] != 0 or 0 in values[:-1]:
            raise VerificationError(f"clause must have one final zero at line {line_number}")
        clause = tuple(values[:-1])
        if any(abs(literal) > variables for literal in clause):
            raise VerificationError(f"literal out of range at line {line_number}")
        if len(set(clause)) != len(clause):
            raise VerificationError(f"duplicate literal at line {line_number}")
        if any(-literal in clause for literal in clause):
            raise VerificationError(f"tautological clause at line {line_number}")
        clauses.append(clause)
    if variables is None or declared_clauses is None:
        raise VerificationError("missing header")
    if len(clauses) != declared_clauses:
        raise VerificationError(
            f"clause count mismatch: declared {declared_clauses}, parsed {len(clauses)}"
        )
    return variables, clauses


def reconstruct(n: int) -> tuple[int, list[tuple[int, ...]]]:
    if n not in (8, 9, 10):
        raise VerificationError("n must be one of the audited instances 8, 9, 10")
    edges = list(itertools.combinations(range(1, n + 1), 4))
    lookup = {edge: index + 1 for index, edge in enumerate(edges)}
    clauses: list[tuple[int, ...]] = []
    for left_index in range(len(edges)):
        for right_index in range(left_index + 1, len(edges)):
            if set(edges[left_index]).isdisjoint(edges[right_index]):
                clauses.append((-(left_index + 1), -(right_index + 1)))
    for triple in itertools.combinations(range(1, n + 1), 3):
        extension_variables = []
        for vertex in range(1, n + 1):
            if vertex not in triple:
                edge = tuple(sorted(triple + (vertex,)))
                extension_variables.append(lookup[edge])
        for position in range(len(extension_variables)):
            clauses.append(tuple(
                extension_variables[index]
                for index in range(len(extension_variables))
                if index != position
            ))
    return len(edges), clauses


def verify(path: Path, n: int) -> dict[str, object]:
    parsed_variables, parsed_clauses = parse_dimacs(path)
    expected_variables, expected_clauses = reconstruct(n)
    if parsed_variables != expected_variables:
        raise VerificationError(
            f"variable count mismatch: {parsed_variables} != {expected_variables}"
        )
    if parsed_clauses != expected_clauses:
        mismatch = next(
            (index for index, pair in enumerate(zip(parsed_clauses, expected_clauses))
             if pair[0] != pair[1]),
            min(len(parsed_clauses), len(expected_clauses)),
        )
        raise VerificationError(f"canonical clause mismatch at zero-based index {mismatch}")
    input_bytes = path.read_bytes()
    code_bytes = Path(__file__).read_bytes()
    return {
        "status": "VERIFIED_CANONICAL_INSTANCE",
        "n": n,
        "variables": parsed_variables,
        "clauses": len(parsed_clauses),
        "cnf_sha256": hashlib.sha256(input_bytes).hexdigest(),
        "verifier_sha256": hashlib.sha256(code_bytes).hexdigest(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("cnf", type=Path)
    parser.add_argument("--n", required=True, type=int)
    args = parser.parse_args()
    try:
        record = verify(args.cnf, args.n)
    except VerificationError as exc:
        print(f"REJECTED: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(record, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
