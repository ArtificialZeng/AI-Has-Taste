#!/usr/bin/env python3
"""Exact small obstructions to tempting constructive proof routes.

These examples do not refute the Latin Tableau Conjecture.  They refute only
specific stronger lemmas/algorithms that might otherwise be used to prove it.
"""

from __future__ import annotations

import itertools
import json
import sys
from collections import Counter

from cds_search import cds, partitions_in_box, solve_shape, verify_coloring


def profile(coloring: list[list[int]]) -> tuple[int, ...]:
    return tuple(sorted(Counter(color for row in coloring for color in row).values(), reverse=True))


def first_fit(shape: tuple[int, ...]) -> list[list[int]]:
    coloring: list[list[int]] = []
    columns = [set() for _ in range(shape[0])]
    for row_length in shape:
        row: list[int] = []
        used: set[int] = set()
        for j in range(row_length):
            color = 0
            while color in used or color in columns[j]:
                color += 1
            row.append(color)
            used.add(color)
            columns[j].add(color)
        coloring.append(row)
    return coloring


def fixed_cyclic(shape: tuple[int, ...]) -> list[list[int]]:
    modulus = max(len(shape), shape[0])
    return [[(i + j) % modulus for j in range(row_length)] for i, row_length in enumerate(shape)]


def shifted_cyclic_profile_exists(shape: tuple[int, ...]) -> tuple[bool, int]:
    """Test all distinct cyclic row shifts; intended only for the small witness."""
    if len(shape) > shape[0]:
        raise ValueError("transpose the shape before using this checker")
    modulus = shape[0]
    tested = 0
    target = cds(shape)
    for shifts in itertools.permutations(range(modulus), len(shape)):
        tested += 1
        counts = [0] * modulus
        for row_length, shift in zip(shape, shifts):
            for j in range(row_length):
                counts[(j + shift) % modulus] += 1
        if tuple(sorted(counts, reverse=True)) == target:
            return True, tested
    return False, tested


def main() -> int:
    records: list[dict[str, object]] = []
    for name, algorithm in (("row-major-first-fit", first_fit), ("fixed-cyclic", fixed_cyclic)):
        failures: list[tuple[int, ...]] = []
        for shape in partitions_in_box(6, 6):
            if profile(algorithm(shape)) != cds(shape):
                failures.append(shape)
        witness = min(failures, key=lambda s: (sum(s), max(len(s), s[0]), s))
        coloring = algorithm(witness)
        records.append(
            {
                "route": name,
                "claim_refuted": f"The {name} coloring always has the CDS profile.",
                "shape": list(witness),
                "cds": list(cds(witness)),
                "algorithm_profile": list(profile(coloring)),
                "coloring_zero_based": coloring,
                "proper": all(
                    len(set(row)) == len(row) for row in coloring
                ) and all(
                    len({coloring[i][j] for i in range(len(witness)) if j < witness[i]})
                    == sum(j < row_length for row_length in witness)
                    for j in range(witness[0])
                ),
                "minimality_scope": "minimum area among every shape in the 6x6 box",
            }
        )

    cyclic_shape = (4, 2, 2)
    cyclic_exists, cyclic_tests = shifted_cyclic_profile_exists(cyclic_shape)
    records.append(
        {
            "route": "distinct-cyclic-row-shifts",
            "claim_refuted": "Some assignment of distinct cyclic row shifts always has the CDS profile.",
            "shape": list(cyclic_shape),
            "cds": list(cds(cyclic_shape)),
            "shift_assignments_tested": cyclic_tests,
            "exists": cyclic_exists,
            "exhaustive_scope": "all injections of 3 row shifts into Z/4Z (4P3 = 24)",
        }
    )
    if cyclic_exists or cyclic_tests != 24:
        raise AssertionError("cyclic obstruction was not reproduced")

    greedy_shape = (5, 4, 3, 3)
    bad_matching = ((0, 4), (1, 3), (2, 0), (3, 1))
    forced = solve_shape(greedy_shape, time_limit=30, forced_first_matching=bad_matching)
    if forced.status != "infeasible":
        raise AssertionError(f"forced-matching obstruction did not reproduce: {forced.status}")
    unrestricted = solve_shape(greedy_shape, time_limit=30)
    if unrestricted.coloring is None:
        raise AssertionError("the obstruction shape itself must be CDS-colorable")
    okay, reason = verify_coloring(greedy_shape, unrestricted.delta, unrestricted.coloring)
    if not okay:
        raise AssertionError(reason)
    records.append(
        {
            "route": "arbitrary-maximum-matching-first",
            "claim_refuted": "Every maximum matching can be the largest color class of a CDS coloring.",
            "shape": list(greedy_shape),
            "cds": list(unrestricted.delta),
            "bad_maximum_matching": [list(edge) for edge in bad_matching],
            "forced_solver_status": forced.status,
            "human_certificate": (
                "After deleting the forced matching, the residual board has four columns 0,1,2,3; "
                "column 3 has the unique residual edge (0,3). Each residual matching of size 4 "
                "must use all four columns and hence (0,3), so two disjoint residual size-4 "
                "matchings cannot exist, while the remaining CDS demands sizes 4,4,2,1."
            ),
            "unrestricted_cds_coloring_zero_based": [list(row) for row in unrestricted.coloring],
        }
    )

    json.dump({"schema_version": 1, "obstructions": records}, sys.stdout, indent=2, sort_keys=True)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
