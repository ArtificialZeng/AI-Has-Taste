#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Fresh exact referee check of the frozen order-eight classification.

This verifier does not call nauty and does not use the producer's labeling
search.  It enumerates every labeled regular graph by completing one vertex at
a time, independently forms the relabeling orbits of the frozen
representatives, and tests the fixed labeling 1,...,8.  Fixing the labeling is
without loss: every ordinary distance-magic labeling transports its graph to
one for which vertex i has label i+1.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parent.parent
INPUT = ROOT / "evidence" / "order8_classification.json"
OUTPUT = ROOT / "audit" / "referee_recheck.json"
REQUIRED_PYTHON = Path(
    "/Users/mac/4prove-or-disprove-math/.research-venv/bin/python"
).resolve()
N = 8
PAIRS = tuple((i, j) for i in range(N) for j in range(i + 1, N))
PAIR_BIT = {pair: bit for bit, pair in enumerate(PAIRS)}


def edge_bit(i: int, j: int) -> int:
    if i > j:
        i, j = j, i
    return 1 << PAIR_BIT[(i, j)]


def enumerate_regular_masks(degree: int) -> set[int]:
    """Enumerate every labeled simple degree-``degree`` graph exactly once."""

    result: set[int] = set()

    def recurse(vertex: int, remaining: tuple[int, ...], mask: int) -> None:
        while vertex < N and remaining[vertex] == 0:
            vertex += 1
        if vertex == N:
            if all(value == 0 for value in remaining):
                result.add(mask)
            return
        need = remaining[vertex]
        available = tuple(
            j for j in range(vertex + 1, N) if remaining[j] > 0
        )
        if need < 0 or need > len(available):
            return
        for chosen in itertools.combinations(available, need):
            new = list(remaining)
            new[vertex] = 0
            new_mask = mask
            for j in chosen:
                new[j] -= 1
                new_mask |= edge_bit(vertex, j)
            if any(value < 0 for value in new):
                continue
            if sum(new[vertex + 1 :]) % 2:
                continue
            recurse(vertex + 1, tuple(new), new_mask)

    recurse(0, (degree,) * N, 0)
    return result


def mask_from_rows(rows: list[str], permutation: tuple[int, ...]) -> int:
    mask = 0
    for bit, (i, j) in enumerate(PAIRS):
        if rows[permutation[i]][permutation[j]] == "1":
            mask |= 1 << bit
    return mask


def orbit(rows: list[str]) -> set[int]:
    return {
        mask_from_rows(rows, permutation)
        for permutation in itertools.permutations(range(N))
    }


def fixed_labels_are_magic(mask: int, degree: int) -> bool:
    target = 9 * degree // 2
    for i in range(N):
        total = 0
        for j in range(N):
            if i != j and mask & edge_bit(i, j):
                total += j + 1
        if total != target:
            return False
    return True


def quotient_rank(rows: list[str]) -> int:
    matrix = [
        [int(rows[row][col]) ^ int(rows[7][col]) for col in range(7)]
        for row in range(7)
    ]
    rank = 0
    for col in range(7):
        pivot = next(
            (row for row in range(rank, 7) if matrix[row][col]), None
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        for row in range(7):
            if row != rank and matrix[row][col]:
                matrix[row] = [
                    a ^ b for a, b in zip(matrix[row], matrix[rank])
                ]
        rank += 1
    return rank


def main() -> None:
    if Path(sys.executable).resolve() != REQUIRED_PYTHON:
        raise RuntimeError(f"wrong interpreter: {sys.executable}")
    records = json.loads(INPUT.read_text(encoding="utf-8"))["records"]
    expected_positive_ids = {"d0-1", "d2-1", "d4-1", "d6-1"}
    report: dict[str, object] = {
        "status": "pass",
        "method": (
            "fresh exhaustive labeled-graph generation; full permutation "
            "orbits of frozen representatives; fixed-label magic test"
        ),
        "degrees": {},
    }
    for degree in (0, 2, 4, 6):
        universe = enumerate_regular_masks(degree)
        degree_records = [r for r in records if r["degree"] == degree]
        record_orbits = {
            r["class_id"]: orbit(r["adjacency_rows"]) for r in degree_records
        }
        orbit_ids = list(record_orbits)
        for index, left in enumerate(orbit_ids):
            for right in orbit_ids[index + 1 :]:
                if record_orbits[left] & record_orbits[right]:
                    raise AssertionError(f"overlapping orbits {left}, {right}")
        covered = set().union(*record_orbits.values())
        if universe != covered:
            raise AssertionError(f"coverage mismatch in degree {degree}")

        magic_masks = {
            mask for mask in universe if fixed_labels_are_magic(mask, degree)
        }
        magic_class_ids = {
            class_id
            for class_id, masks in record_orbits.items()
            if magic_masks & masks
        }
        expected_here = {
            class_id for class_id in expected_positive_ids
            if class_id.startswith(f"d{degree}-")
        }
        if magic_class_ids != expected_here:
            raise AssertionError(
                f"ordinary-magic class mismatch at degree {degree}"
            )
        if any(
            mask not in set().union(
                *(record_orbits[class_id] for class_id in magic_class_ids)
            )
            for mask in magic_masks
        ):
            raise AssertionError("magic graph lies outside positive orbits")

        ranks = {
            r["class_id"]: quotient_rank(r["adjacency_rows"])
            for r in degree_records
        }
        for r in degree_records:
            certificate_rank = r["reduced_adjacency_certificate"]["rank"]
            if ranks[r["class_id"]] != certificate_rank:
                raise AssertionError(f"rank mismatch at {r['class_id']}")
        report["degrees"][str(degree)] = {
            "all_labeled_regular_graphs": len(universe),
            "covered_by_disjoint_frozen_orbits": len(covered),
            "fixed_identity_label_magic_graphs": len(magic_masks),
            "ordinary_magic_class_ids": sorted(magic_class_ids),
            "quotient_ranks_by_class": ranks,
        }

    positive_nullities = {
        r["class_id"]: 7 - quotient_rank(r["adjacency_rows"])
        for r in records if r["class_id"] in expected_positive_ids
    }
    if positive_nullities != {
        "d0-1": 7,
        "d2-1": 4,
        "d4-1": 6,
        "d6-1": 4,
    }:
        raise AssertionError("positive nullities do not match frozen claim")
    report["positive_reduced_nullities"] = positive_nullities
    report["universal_assertion_verified"] = True
    OUTPUT.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
