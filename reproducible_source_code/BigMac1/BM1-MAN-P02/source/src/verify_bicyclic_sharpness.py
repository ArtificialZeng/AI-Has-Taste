#!/usr/bin/env python3
"""Exact verifier for the bicyclic principal core in the order-62 graph."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Sequence


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def determinant(matrix: Sequence[Sequence[int]]) -> int:
    work = [list(map(int, row)) for row in matrix]
    n = len(work)
    sign = 1
    previous = 1
    for column in range(n - 1):
        pivot_row = next((row for row in range(column, n) if work[row][column]), None)
        if pivot_row is None:
            return 0
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            sign *= -1
        pivot = work[column][column]
        for row in range(column + 1, n):
            for other in range(column + 1, n):
                numerator = work[row][other] * pivot - work[row][column] * work[column][other]
                if column and numerator % previous:
                    raise ArithmeticError("inexact Bareiss division")
                work[row][other] = numerator // previous
            work[row][column] = 0
        previous = pivot
    return sign * work[-1][-1]


def connected(adjacency: Sequence[Sequence[int]]) -> bool:
    reached = {0}
    stack = [0]
    while stack:
        vertex = stack.pop()
        for neighbour, value in enumerate(adjacency[vertex]):
            if value and neighbour not in reached:
                reached.add(neighbour)
                stack.append(neighbour)
    return len(reached) == len(adjacency)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("witness", type=Path)
    parser.add_argument("--expected-witness-sha256", required=True)
    parser.add_argument("--ambient", type=Path, required=True)
    parser.add_argument("--expected-ambient-sha256", required=True)
    parser.add_argument("--ambient-verification", type=Path, required=True)
    parser.add_argument("--expected-ambient-verification-sha256", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    witness_hash = sha256(args.witness)
    ambient_hash = sha256(args.ambient)
    verification_hash = sha256(args.ambient_verification)
    if witness_hash != args.expected_witness_sha256:
        raise ValueError("witness SHA-256 mismatch")
    if ambient_hash != args.expected_ambient_sha256:
        raise ValueError("ambient certificate SHA-256 mismatch")
    if verification_hash != args.expected_ambient_verification_sha256:
        raise ValueError("ambient verification SHA-256 mismatch")

    witness = json.loads(args.witness.read_text(encoding="utf-8"))
    ambient = json.loads(args.ambient.read_text(encoding="utf-8"))
    prior = json.loads(args.ambient_verification.read_text(encoding="utf-8"))
    if witness.get("ambient_certificate_sha256") != ambient_hash:
        raise ValueError("witness does not bind the ambient graph")
    if prior.get("status") != "PASS" or prior.get("certificate_sha256") != ambient_hash:
        raise ValueError("ambient graph verification is not a bound PASS")
    checks = prior.get("graph_checks", {})
    if prior.get("rank_exact") != 10 or checks.get("n") != 62:
        raise ValueError("ambient graph has wrong order or exact rank")
    if not all(checks.get(key) for key in (
        "binary", "no_isolates", "pairwise_distinct_open_neighbourhoods",
        "symmetric", "zero_diagonal",
    )):
        raise ValueError("ambient graph verification lacks a required graph check")

    adjacency = ambient.get("adjacency_matrix")
    indices = witness.get("core_indices")
    if not isinstance(adjacency, list) or len(adjacency) != 62:
        raise ValueError("expected a 62-vertex ambient adjacency matrix")
    if not isinstance(indices, list) or len(indices) != 10 or len(set(indices)) != 10:
        raise ValueError("expected ten distinct core indices")
    if any(not isinstance(index, int) or not 0 <= index < 62 for index in indices):
        raise ValueError("core index outside the ambient graph")

    core = [[int(adjacency[left][right]) for right in indices] for left in indices]
    if any(core[i][i] for i in range(10)):
        raise AssertionError("core has a loop")
    if any(
        core[i][j] != core[j][i] or core[i][j] not in (0, 1)
        for i in range(10) for j in range(10)
    ):
        raise AssertionError("core is not a simple adjacency matrix")
    edges = [[i, j] for i in range(10) for j in range(i + 1, 10) if core[i][j]]
    if edges != witness.get("core_edges"):
        raise AssertionError("listed core edges do not match the ambient graph")
    if len(edges) != 11 or not connected(core):
        raise AssertionError("core is not connected bicyclic")
    det = determinant(core)
    if det != -1 or det != witness.get("core_determinant"):
        raise AssertionError("core determinant mismatch")

    payload = {
        "status": "PASS",
        "arithmetic": "integers only",
        "witness": str(args.witness),
        "witness_sha256": witness_hash,
        "ambient_certificate": str(args.ambient),
        "ambient_certificate_sha256": ambient_hash,
        "ambient_verification": str(args.ambient_verification),
        "ambient_verification_sha256": verification_hash,
        "ambient_order": 62,
        "ambient_rank": 10,
        "ambient_reduced": True,
        "core_indices": indices,
        "core_order": 10,
        "core_edge_count": len(edges),
        "core_edges": edges,
        "core_connected": True,
        "core_cyclomatic_number": len(edges) - len(indices) + 1,
        "core_bicyclic": True,
        "core_determinant": det,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
