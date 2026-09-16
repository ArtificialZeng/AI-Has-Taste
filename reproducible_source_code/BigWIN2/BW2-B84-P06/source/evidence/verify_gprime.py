#!/usr/bin/env python3
"""Exact exhaustive recovery-set verifier for Equation (3)'s 11-column G'.

All arithmetic is integer arithmetic modulo 3.  For each target column the
script enumerates all 2^11-1 nonempty coordinate subsets, keeps the
inclusion-minimal recovery sets, and performs exhaustive dynamic programming
over their union masks to find a maximum pairwise-disjoint packing.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

P = 3

# Independently transcribed from arXiv:2601.04041v2, Equation (3), deleting
# the last (duplicate) all-one parity column.  -1 is represented by 2 in F_3.
ROWS = [
    [1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 2, 0, 2, 0, 1],
    [0, 0, 1, 0, 0, 0, 2, 0, 0, 2, 1],
    [0, 0, 0, 1, 0, 0, 0, 2, 2, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 2, 0, 2, 1],
    [0, 0, 0, 0, 0, 1, 0, 0, 2, 2, 1],
]


def inv(a: int) -> int:
    if a % P == 1:
        return 1
    if a % P == 2:
        return 2
    raise ZeroDivisionError


def rref_rank(matrix: list[list[int]]) -> int:
    a = [[x % P for x in row] for row in matrix]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    pivot_row = 0
    for col in range(n):
        pivot = next((r for r in range(pivot_row, m) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = inv(a[pivot_row][col])
        a[pivot_row] = [(scale * x) % P for x in a[pivot_row]]
        for r in range(m):
            if r != pivot_row and a[r][col]:
                scale = a[r][col]
                a[r] = [(x - scale * y) % P for x, y in zip(a[r], a[pivot_row])]
        pivot_row += 1
        if pivot_row == m:
            break
    return pivot_row


def solve(columns: list[int], target: int) -> list[int] | None:
    """Return coefficients expressing column target using columns, or None."""
    # Six equations, len(columns) unknowns, final entry is augmented target.
    a = [[ROWS[r][c] % P for c in columns] + [ROWS[r][target] % P]
         for r in range(6)]
    m, n = 6, len(columns)
    pivot_row = 0
    pivot_cols: list[int] = []
    for col in range(n):
        pivot = next((r for r in range(pivot_row, m) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = inv(a[pivot_row][col])
        a[pivot_row] = [(scale * x) % P for x in a[pivot_row]]
        for r in range(m):
            if r != pivot_row and a[r][col]:
                scale = a[r][col]
                a[r] = [(x - scale * y) % P for x, y in zip(a[r], a[pivot_row])]
        pivot_cols.append(col)
        pivot_row += 1
        if pivot_row == m:
            break
    if any(all(a[r][c] == 0 for c in range(n)) and a[r][n] != 0
           for r in range(m)):
        return None
    ans = [0] * n
    for r, col in enumerate(pivot_cols):
        ans[col] = a[r][n]
    assert all(sum(ROWS[r][c] * x for c, x in zip(columns, ans)) % P
               == ROWS[r][target] % P for r in range(6))
    return ans


def members(mask: int, n: int = 11) -> list[int]:
    return [j for j in range(n) if mask & (1 << j)]


def minimal_recovery_masks(target: int) -> list[int]:
    minimal: list[int] = []
    masks = sorted(range(1, 1 << 11), key=lambda x: (x.bit_count(), x))
    for mask in masks:
        if any((prev & mask) == prev for prev in minimal):
            continue
        if solve(members(mask), target) is not None:
            minimal.append(mask)
    return minimal


def maximum_disjoint_packing(masks: list[int]) -> list[int]:
    # dp maps an occupied-coordinate mask to one packing producing it.
    dp: dict[int, tuple[int, ...]] = {0: ()}
    for recovery in masks:
        additions: dict[int, tuple[int, ...]] = {}
        for used, packing in list(dp.items()):
            if used & recovery:
                continue
            union = used | recovery
            candidate = packing + (recovery,)
            incumbent = dp.get(union) or additions.get(union)
            if incumbent is None or len(candidate) > len(incumbent):
                additions[union] = candidate
        for union, packing in additions.items():
            if union not in dp or len(packing) > len(dp[union]):
                dp[union] = packing
    return list(max(dp.values(), key=lambda x: (len(x), tuple(-m for m in x))))


def describe_set(mask: int, target: int) -> dict[str, object]:
    cols = members(mask)
    coeffs = solve(cols, target)
    assert coeffs is not None
    return {
        "indices_1_based": [c + 1 for c in cols],
        "coefficients_mod_3": coeffs,
    }


def build_report() -> dict[str, object]:
    columns = [[ROWS[r][c] for r in range(6)] for c in range(11)]
    results = []
    for target in range(11):
        recovery_masks = minimal_recovery_masks(target)
        packing = maximum_disjoint_packing(recovery_masks)
        results.append({
            "target_index_1_based": target + 1,
            "target_column": columns[target],
            "minimal_recovery_set_count": len(recovery_masks),
            "minimal_recovery_sets": [describe_set(m, target) for m in recovery_masks],
            "maximum_pairwise_disjoint_packing_size": len(packing),
            "maximum_packing_witness": [describe_set(m, target) for m in packing],
            "has_four_disjoint_recovery_sets": len(packing) >= 4,
        })
    matrix_encoding = json.dumps(ROWS, separators=(",", ":")).encode()
    return {
        "provenance": "win-00084-p06-triage-2c247bef6e50",
        "arithmetic": "exact integers modulo 3",
        "source": "arXiv:2601.04041v2 Equation (3), final duplicate parity column deleted",
        "matrix_rows_mod_3": ROWS,
        "matrix_encoding_sha256": hashlib.sha256(matrix_encoding).hexdigest(),
        "rank_mod_3": rref_rank(ROWS),
        "enumeration": {
            "coordinate_subsets_per_target": (1 << 11) - 1,
            "method": "all nonempty subsets; inclusion-minimal span sets; exact union-mask packing DP",
        },
        "targets": results,
        "matrix_has_four_all_symbol_pir_property": all(
            item["has_four_disjoint_recovery_sets"] for item in results
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = build_report()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
