#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Independent replay checks for order8_classification.json.

Unlike the producer, this verifier obtains adjacency matrices from nauty
``showg`` rather than decoding graph6 in Python.  It independently repeats all
label permutations, recomputes binary ranks, and replays the stored elementary
row operations.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
EVIDENCE = ROOT / "evidence"
CLASSIFICATION = EVIDENCE / "order8_classification.json"
G6 = EVIDENCE / "regular_order8.g6"
REPORT = EVIDENCE / "verification_report.json"
REQUIRED_PYTHON = Path(
    "/Users/mac/4prove-or-disprove-math/.research-venv/bin/python"
).resolve()


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def showg_matrices() -> list[list[list[int]]]:
    proc = subprocess.run(
        ["/opt/homebrew/bin/showg", "-q", "-a", str(G6)],
        check=True,
        capture_output=True,
        text=True,
    )
    if proc.stderr:
        raise AssertionError(f"showg emitted stderr: {proc.stderr!r}")
    lines = proc.stdout.splitlines()
    matrices: list[list[list[int]]] = []
    pos = 0
    while pos < len(lines):
        n = int(lines[pos])
        pos += 1
        if n != 8:
            raise AssertionError(f"unexpected order from showg: {n}")
        block = lines[pos : pos + n]
        pos += n
        if len(block) != n or any(len(row) != n for row in block):
            raise AssertionError("truncated showg adjacency block")
        matrices.append([[int(x) for x in row] for row in block])
    return matrices


def brute_force_magic(adj: list[list[int]], degree: int) -> tuple[int, list[int] | None]:
    target = 9 * degree // 2
    count = 0
    witness: list[int] | None = None
    for labels in itertools.permutations(range(1, 9)):
        if all(sum(entry * label for entry, label in zip(row, labels)) == target for row in adj):
            count += 1
            if witness is None:
                witness = list(labels)
    return count, witness


def quotient_matrix(adj: list[list[int]]) -> list[list[int]]:
    # Normalize A e_j by subtracting its last coordinate times 1 (same as XOR).
    return [
        [adj[row][col] ^ adj[7][col] for col in range(7)]
        for row in range(7)
    ]


def binary_rank(matrix: list[list[int]]) -> int:
    work = [row[:] for row in matrix]
    rank = 0
    for col in range(len(work[0])):
        pivot = next((i for i in range(rank, len(work)) if work[i][col]), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        for i in range(rank + 1, len(work)):
            if work[i][col]:
                work[i] = [a ^ b for a, b in zip(work[i], work[rank])]
        rank += 1
    return rank


def replay_operations(matrix: list[list[int]], certificate: dict[str, object]) -> None:
    work = [row[:] for row in matrix]
    for operation in certificate["elementary_row_operations"]:
        op, a, b = operation
        if op == "swap":
            work[a], work[b] = work[b], work[a]
        elif op == "xor":
            work[a] = [x ^ y for x, y in zip(work[a], work[b])]
        else:
            raise AssertionError(f"unknown operation {op!r}")
    encoded = ["".join(map(str, row)) for row in work]
    if encoded != certificate["rref_rows"]:
        raise AssertionError("stored row-operation transcript does not reach stored RREF")


def components(adj: list[list[int]]) -> list[list[int]]:
    unseen = set(range(8))
    result: list[list[int]] = []
    while unseen:
        start = min(unseen)
        stack = [start]
        unseen.remove(start)
        component: list[int] = []
        while stack:
            v = stack.pop()
            component.append(v)
            for u, edge in enumerate(adj[v]):
                if edge and u in unseen:
                    unseen.remove(u)
                    stack.append(u)
        result.append(sorted(component))
    return result


def identify_positive(adj: list[list[int]], degree: int) -> str:
    if degree == 0:
        return "8K1"
    if degree == 2:
        comps = sorted(len(c) for c in components(adj))
        if comps != [4, 4]:
            raise AssertionError(f"unexpected positive degree-2 structure: {comps}")
        return "2C4"
    if degree == 4:
        left = set(range(4))
        right = set(range(4, 8))
        if any(adj[i][j] != int((i in left) != (j in left)) for i in range(8) for j in range(8)):
            raise AssertionError("positive degree-4 record is not displayed as K4,4")
        return "K4,4"
    if degree == 6:
        nonedges = [
            (i, j) for i in range(8) for j in range(i + 1, 8) if not adj[i][j]
        ]
        if len(nonedges) != 4 or sorted(v for e in nonedges for v in e) != list(range(8)):
            raise AssertionError("degree-6 complement is not a perfect matching")
        return "K2,2,2,2"
    raise AssertionError(f"unexpected positive degree {degree}")


def main() -> None:
    if Path(sys.executable).resolve() != REQUIRED_PYTHON:
        raise RuntimeError(f"wrong interpreter: {sys.executable}")
    payload = json.loads(CLASSIFICATION.read_text(encoding="utf-8"))
    records = payload["records"]
    matrices = showg_matrices()
    if len(records) != 11 or len(matrices) != 11:
        raise AssertionError("certificate does not have all eleven representatives")
    if G6.read_text(encoding="ascii").splitlines() != [r["graph6"] for r in records]:
        raise AssertionError("graph6 stream and JSON record order differ")

    checked: list[dict[str, object]] = []
    positives: list[str] = []
    total_permutations = 0
    for record, adj in zip(records, matrices):
        adjacency_rows = ["".join(map(str, row)) for row in adj]
        if adjacency_rows != record["adjacency_rows"]:
            raise AssertionError(f"showg/parser disagreement at {record['class_id']}")
        degree = record["degree"]
        if [sum(row) for row in adj] != [degree] * 8:
            raise AssertionError(f"nonregular record {record['class_id']}")

        count, witness = brute_force_magic(adj, degree)
        total_permutations += math.factorial(8)
        if count != record["ordinary_magic_labeling_count"]:
            raise AssertionError(f"ordinary-label count disagreement at {record['class_id']}")
        if witness != record["first_labeling_by_vertex"]:
            raise AssertionError(f"first witness disagreement at {record['class_id']}")

        quotient = quotient_matrix(adj)
        rank = binary_rank(quotient)
        cert = record["reduced_adjacency_certificate"]
        if rank != cert["rank"] or 7 - rank != cert["nullity"]:
            raise AssertionError(f"binary rank disagreement at {record['class_id']}")
        replay_operations(quotient, cert)
        for vector_text in cert["kernel_basis_quotient_coordinates"]:
            vector = [int(x) for x in vector_text]
            if any(sum(a * b for a, b in zip(row, vector)) % 2 for row in quotient):
                raise AssertionError(f"bad kernel vector at {record['class_id']}")

        structural_name = None
        if count:
            structural_name = identify_positive(adj, degree)
            positives.append(structural_name)
            if 7 - rank < 2:
                raise AssertionError(f"universal assertion fails at {record['class_id']}")
        checked.append(
            {
                "class_id": record["class_id"],
                "ordinary_labeling_count": count,
                "reduced_rank": rank,
                "reduced_nullity": 7 - rank,
                "structural_name_if_ordinary_magic": structural_name,
            }
        )

    expected_positive_names = ["8K1", "2C4", "K4,4", "K2,2,2,2"]
    if positives != expected_positive_names:
        raise AssertionError(f"unexpected positive classification: {positives}")
    report = {
        "status": "pass",
        "verification_method": (
            "showg adjacency extraction; independent 8! permutation loops; "
            "independent F_2 elimination; replay of stored elementary row operations"
        ),
        "classification_sha256": digest(CLASSIFICATION),
        "graph6_stream_sha256": digest(G6),
        "source_md_sha256": digest(ROOT / "source.md"),
        "representatives_checked": len(records),
        "total_label_permutations_rechecked": total_permutations,
        "ordinary_distance_magic_classes": expected_positive_names,
        "universal_assertion_verified": True,
        "records": checked,
    }
    REPORT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("status", "representatives_checked", "total_label_permutations_rechecked", "ordinary_distance_magic_classes", "universal_assertion_verified")}, sort_keys=True))


if __name__ == "__main__":
    main()
