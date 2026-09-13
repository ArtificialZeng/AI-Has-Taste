#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Exact order-eight regular distance-magic classification.

This script has no third-party Python dependencies.  It asks nauty's ``geng``
for every unlabeled 8-vertex k-regular graph in the only degree-feasible cases,
tests all 8! ordinary labelings of each graph, and row-reduces the induced
7-dimensional adjacency operator over F_2.  The JSON output contains enough
data to replay every successful labeling and every row-reduction certificate.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import shutil
import subprocess


N = 8
DEGREES = (0, 2, 4, 6)
EXPECTED_COUNTS = {0: 1, 2: 3, 4: 6, 6: 1}
EXPECTED_SOURCE_SHA256 = (
    "59a054758e876b4f40c2ad469819dc925ef8f259f2d23eeafa4a82b8d2f04053"
)
ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "evidence" / "order8_classification.json"
G6_OUTPUT = ROOT / "evidence" / "regular_order8.g6"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def bits(mask: int, width: int) -> str:
    """Bit j is printed in position j, so strings use matrix column order."""
    return "".join("1" if (mask >> j) & 1 else "0" for j in range(width))


def decode_graph6(line: str) -> list[list[int]]:
    text = line.strip()
    if text.startswith(">>graph6<<"):
        text = text[len(">>graph6<<") :]
    vals = [ord(ch) - 63 for ch in text]
    if not vals or vals[0] != N:
        raise ValueError(f"expected short graph6 record of order {N}: {line!r}")
    stream: list[int] = []
    for val in vals[1:]:
        if not 0 <= val < 64:
            raise ValueError(f"invalid graph6 byte in {line!r}")
        stream.extend((val >> shift) & 1 for shift in range(5, -1, -1))
    needed = N * (N - 1) // 2
    if len(stream) < needed or any(stream[needed:]):
        raise ValueError(f"bad graph6 padding in {line!r}")
    adj = [[0] * N for _ in range(N)]
    pos = 0
    for j in range(1, N):
        for i in range(j):
            adj[i][j] = adj[j][i] = stream[pos]
            pos += 1
    return adj


def encode_graph6(adj: list[list[int]]) -> str:
    stream = [adj[i][j] for j in range(1, N) for i in range(j)]
    stream.extend([0] * ((-len(stream)) % 6))
    chars = [chr(N + 63)]
    for start in range(0, len(stream), 6):
        val = 0
        for bit in stream[start : start + 6]:
            val = 2 * val + bit
        chars.append(chr(val + 63))
    return "".join(chars)


def neighbors(adj: list[list[int]]) -> list[tuple[int, ...]]:
    return [tuple(j for j, entry in enumerate(row) if entry) for row in adj]


def ordinary_magic_search(adj: list[list[int]], degree: int) -> dict[str, object]:
    nbrs = neighbors(adj)
    target = 9 * degree // 2
    count = 0
    first: tuple[int, ...] | None = None
    first_sums: tuple[int, ...] | None = None
    tested = 0
    for labeling in itertools.permutations(range(1, N + 1)):
        tested += 1
        sums = tuple(sum(labeling[u] for u in nbrs[v]) for v in range(N))
        if all(value == target for value in sums):
            count += 1
            if first is None:
                first = labeling
                first_sums = sums
    if tested != math.factorial(N):
        raise AssertionError("permutation enumeration was incomplete")
    return {
        "permutations_tested": tested,
        "magic_constant": target,
        "ordinary_magic_labeling_count": count,
        "is_ordinary_distance_magic": count > 0,
        "first_labeling_by_vertex": list(first) if first is not None else None,
        "first_neighborhood_sums": list(first_sums) if first_sums is not None else None,
    }


def reduced_adjacency_rows(adj: list[list[int]]) -> list[int]:
    """Matrix on F_2^8/<1>, in bases [e_0],...,[e_6].

    A basis-column image is normalized by adding its coordinate at vertex 7
    times the all-one vector, thereby making its last coordinate zero.
    """
    rows = [0] * (N - 1)
    for col in range(N - 1):
        last = adj[N - 1][col]
        for row in range(N - 1):
            if adj[row][col] ^ last:
                rows[row] |= 1 << col
    return rows


def rref_certificate(input_rows: list[int], ncols: int) -> dict[str, object]:
    rows = input_rows.copy()
    transform = [1 << i for i in range(len(rows))]
    operations: list[list[object]] = []
    pivots: list[int] = []
    rank = 0
    for col in range(ncols):
        pivot = next((r for r in range(rank, len(rows)) if (rows[r] >> col) & 1), None)
        if pivot is None:
            continue
        if pivot != rank:
            rows[rank], rows[pivot] = rows[pivot], rows[rank]
            transform[rank], transform[pivot] = transform[pivot], transform[rank]
            operations.append(["swap", rank, pivot])
        for r in range(len(rows)):
            if r != rank and ((rows[r] >> col) & 1):
                rows[r] ^= rows[rank]
                transform[r] ^= transform[rank]
                operations.append(["xor", r, rank])
        pivots.append(col)
        rank += 1
        if rank == len(rows):
            break

    # Replay the elementary (hence invertible) row operations as a local check.
    replay = input_rows.copy()
    replay_transform = [1 << i for i in range(len(rows))]
    for op, a, b in operations:
        a = int(a)
        b = int(b)
        if op == "swap":
            replay[a], replay[b] = replay[b], replay[a]
            replay_transform[a], replay_transform[b] = (
                replay_transform[b],
                replay_transform[a],
            )
        elif op == "xor":
            replay[a] ^= replay[b]
            replay_transform[a] ^= replay_transform[b]
        else:
            raise AssertionError(f"unknown row operation: {op}")
    if replay != rows or replay_transform != transform:
        raise AssertionError("row-operation replay failed")

    free = [col for col in range(ncols) if col not in pivots]
    kernel: list[int] = []
    for free_col in free:
        vector = 1 << free_col
        for pivot_row, pivot_col in enumerate(pivots):
            if (rows[pivot_row] >> free_col) & 1:
                vector |= 1 << pivot_col
        if any((row & vector).bit_count() % 2 for row in input_rows):
            raise AssertionError("computed kernel vector is not in the kernel")
        kernel.append(vector)
    if len(kernel) != ncols - rank:
        raise AssertionError("rank-nullity check failed")

    return {
        "rank": rank,
        "nullity": ncols - rank,
        "pivot_columns_zero_based": pivots,
        "input_rows": [bits(row, ncols) for row in input_rows],
        "elementary_row_operations": operations,
        "rref_rows": [bits(row, ncols) for row in rows],
        "left_transform_rows": [bits(row, len(rows)) for row in transform],
        "kernel_basis_quotient_coordinates": [bits(v, ncols) for v in kernel],
    }


def main() -> None:
    source_bytes = (ROOT / "source.md").read_bytes()
    source_sha = sha256_bytes(source_bytes)
    if source_sha != EXPECTED_SOURCE_SHA256:
        raise RuntimeError("source.md changed; refusing to classify a moving target")

    python_executable = str(Path(os.environ.get("MATH_RESEARCH_PYTHON", "")).resolve())
    required_python = "/Users/mac/4prove-or-disprove-math/.research-venv/bin/python"
    if str(Path(os.sys.executable).resolve()) != str(Path(required_python).resolve()):
        raise RuntimeError(f"wrong Python interpreter: {os.sys.executable}")
    if python_executable and python_executable != str(Path(required_python).resolve()):
        raise RuntimeError(f"MATH_RESEARCH_PYTHON points elsewhere: {python_executable}")

    geng = shutil.which("geng")
    if geng is None:
        raise RuntimeError("nauty geng is unavailable")
    geng_path = str(Path(geng).resolve())
    generator: dict[str, object] = {
        "resolved_executable": geng_path,
        "executable_sha256": sha256_bytes(Path(geng_path).read_bytes()),
        "commands": [],
    }

    all_lines: list[str] = []
    degree_lines: dict[int, list[str]] = {}
    for degree in DEGREES:
        argv = [geng, "-q", f"-d{degree}", f"-D{degree}", str(N)]
        proc = subprocess.run(argv, check=True, capture_output=True)
        if proc.stderr:
            raise RuntimeError(f"unexpected geng stderr for degree {degree}: {proc.stderr!r}")
        lines = proc.stdout.decode("ascii").splitlines()
        if len(lines) != EXPECTED_COUNTS[degree]:
            raise AssertionError(
                f"geng count mismatch at degree {degree}: {len(lines)}"
            )
        degree_lines[degree] = lines
        all_lines.extend(lines)
        generator["commands"].append(
            {
                "argv": argv,
                "degree": degree,
                "record_count": len(lines),
                "stdout_sha256": sha256_bytes(proc.stdout),
            }
        )
    if len(all_lines) != 11 or len(set(all_lines)) != 11:
        raise AssertionError("expected eleven distinct graph6 representatives")

    records: list[dict[str, object]] = []
    for degree in DEGREES:
        for index, graph6 in enumerate(degree_lines[degree], start=1):
            adj = decode_graph6(graph6)
            if encode_graph6(adj) != graph6:
                raise AssertionError(f"graph6 round trip failed for {graph6}")
            if any(adj[i][i] for i in range(N)):
                raise AssertionError("loop found")
            if any(adj[i][j] != adj[j][i] for i in range(N) for j in range(N)):
                raise AssertionError("asymmetric adjacency matrix")
            degrees = [sum(row) for row in adj]
            if degrees != [degree] * N:
                raise AssertionError(f"degree mismatch for {graph6}: {degrees}")
            edge_list = [[i, j] for i in range(N) for j in range(i + 1, N) if adj[i][j]]
            ordinary = ordinary_magic_search(adj, degree)
            reduced_rows = reduced_adjacency_rows(adj)
            rank = rref_certificate(reduced_rows, N - 1)
            record: dict[str, object] = {
                "class_id": f"d{degree}-{index}",
                "graph6": graph6,
                "degree": degree,
                "edges_zero_based": edge_list,
                "adjacency_rows": ["".join(map(str, row)) for row in adj],
                **ordinary,
                "reduced_adjacency_certificate": rank,
                "generating_F2_cubed_magic_by_source_criterion": rank["nullity"] >= 2,
            }
            records.append(record)

    magic_records = [r for r in records if r["is_ordinary_distance_magic"]]
    failures = [
        r for r in magic_records
        if not r["generating_F2_cubed_magic_by_source_criterion"]
    ]
    output = {
        "schema": "order8-regular-distance-magic-classification-v1",
        "arithmetic": "exact integers and F_2 bit operations only",
        "source_md_sha256": source_sha,
        "python_executable": str(Path(os.sys.executable).resolve()),
        "domain_argument": {
            "ordinary_magic_constant_formula": "c=9k/2",
            "maximum_simple_graph_degree": 7,
            "degree_cases": list(DEGREES),
            "geng_semantics": (
                "one graph6 representative of each unlabeled simple graph on 8 "
                "vertices; -dK -DK imposes minimum degree = maximum degree = K"
            ),
            "representative_counts_by_degree": {
                str(k): len(degree_lines[k]) for k in DEGREES
            },
            "total_representatives": len(records),
        },
        "generator": generator,
        "search": {
            "label_permutations_per_representative": math.factorial(N),
            "total_label_permutations_tested": math.factorial(N) * len(records),
            "ordinary_distance_magic_class_count": len(magic_records),
            "ordinary_distance_magic_class_ids": [r["class_id"] for r in magic_records],
            "criterion_failure_class_ids": [r["class_id"] for r in failures],
            "universal_assertion_holds": not failures,
        },
        "records": records,
    }

    # Generated artifacts; rerunning this file deterministically replaces them.
    G6_OUTPUT.write_text("\n".join(all_lines) + "\n", encoding="ascii")
    OUTPUT.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(output["search"], sort_keys=True))


if __name__ == "__main__":
    main()
