#!/usr/bin/env python3
"""Exact producer for the five-letter primitive-mass-three classification.

The program uses only exhaustive integer enumeration.  It produces one exact
integer model for each order-feasible primitive balanced direction of mass
three and, because alphabets are visited by increasing diameter, the model is
also minimum-diameter (with lexicographic tie-breaking).
"""

from __future__ import annotations

import argparse
import json
from itertools import combinations, combinations_with_replacement, product
from math import gcd
from pathlib import Path
from typing import Iterable, Iterator, Sequence


JOB_ID = "win-00082-p11-research-c81fb15b21eb"


def mass(row: Sequence[int]) -> int:
    return sum(x for x in row if x > 0)


def row_gcd(row: Sequence[int]) -> int:
    value = 0
    for x in row:
        value = gcd(value, abs(x))
    return value


def canonical(row: Sequence[int]) -> tuple[int, ...]:
    result = tuple(row)
    first = next(x for x in result if x)
    return result if first > 0 else tuple(-x for x in result)


def balanced_rows(max_mass: int = 3) -> list[tuple[int, ...]]:
    """All nonzero balanced rows of mass at most ``max_mass``.

    Every coefficient has absolute value at most the mass, so the displayed
    coefficient box is a complete finite domain, not a heuristic cutoff.
    """

    rows: list[tuple[int, ...]] = []
    for row in product(range(-max_mass, max_mass + 1), repeat=5):
        if sum(row) != 0:
            continue
        row_mass = mass(row)
        if 1 <= row_mass <= max_mass:
            rows.append(tuple(row))
    return rows


def tail_sums(row: Sequence[int]) -> tuple[int, int, int, int]:
    return tuple(sum(row[j:]) for j in range(1, 5))  # type: ignore[return-value]


def feasible_tail(tails: Sequence[int]) -> bool:
    return min(tails) < 0 < max(tails)


def positive_gap_witness(tails: Sequence[int]) -> tuple[int, int, int, int]:
    """Construct positive gaps annihilated by a mixed-sign tail row."""

    positive_sum = sum(x for x in tails if x > 0)
    negative_size = -sum(x for x in tails if x < 0)
    assert positive_sum > 0 and negative_size > 0
    gaps = tuple(
        negative_size if x > 0 else positive_sum if x < 0 else 1 for x in tails
    )
    assert all(x > 0 for x in gaps)
    assert sum(a * g for a, g in zip(tails, gaps)) == 0
    return gaps  # type: ignore[return-value]


def integer_alphabets(max_diameter: int) -> Iterator[tuple[int, int, int, int, int]]:
    """Every translated increasing integer five-tuple through the cutoff."""

    for diameter in range(4, max_diameter + 1):
        for middle in combinations(range(1, diameter), 3):
            yield (0, middle[0], middle[1], middle[2], diameter)


def zero_rows(
    alphabet: Sequence[int], canonical_rows: Iterable[tuple[int, ...]]
) -> list[tuple[int, ...]]:
    return [
        row
        for row in canonical_rows
        if sum(a * s for a, s in zip(row, alphabet)) == 0
    ]


def relation_free_core(core: Sequence[int]) -> bool:
    """Test absence of balanced relations of mass at most three.

    Because the core begins at zero, padding with zeros identifies such a
    relation with a collision between two unordered three-term sums.
    """

    sums = [
        sum(core[i] for i in multiset)
        for multiset in combinations_with_replacement(range(4), 3)
    ]
    return len(sums) == len(set(sums))


def produce(max_diameter: int = 33) -> dict[str, object]:
    oriented_rows = balanced_rows(3)
    canonical_rows = sorted(row for row in oriented_rows if canonical(row) == row)

    primitive_mass_three = sorted(
        row
        for row in canonical_rows
        if mass(row) == 3 and row_gcd(row) == 1
    )
    feasible = sorted(
        row for row in primitive_mass_three if feasible_tail(tail_sums(row))
    )
    target = set(feasible)

    minimum_models: dict[tuple[int, ...], tuple[int, ...]] = {}
    occurrence_count = {row: 0 for row in feasible}
    tuple_count = 0
    for alphabet in integer_alphabets(max_diameter):
        tuple_count += 1
        zeros = zero_rows(alphabet, canonical_rows)
        if len(zeros) == 1 and zeros[0] in target:
            direction = zeros[0]
            occurrence_count[direction] += 1
            minimum_models.setdefault(direction, alphabet)

    uncovered = sorted(target.difference(minimum_models))

    core_counts: dict[str, int] = {}
    minimum_cores: list[tuple[int, int, int, int]] = []
    core_tuple_count = 0
    for diameter in range(3, 12):
        good: list[tuple[int, int, int, int]] = []
        for a, b in combinations(range(1, diameter), 2):
            core_tuple_count += 1
            core = (0, a, b, diameter)
            if relation_free_core(core):
                good.append(core)
        core_counts[str(diameter)] = len(good)
        if good and not minimum_cores:
            minimum_cores = good

    directions = []
    for direction in feasible:
        tails = tail_sums(direction)
        model = minimum_models.get(direction)
        directions.append(
            {
                "delta": list(direction),
                "tail_sums": list(tails),
                "positive_gap_witness": list(positive_gap_witness(tails)),
                "minimum_model": list(model) if model is not None else None,
                "minimum_diameter": model[-1] if model is not None else None,
                "model_count_through_cutoff": occurrence_count[direction],
            }
        )

    maximum_minimum = (
        max(model[-1] for model in minimum_models.values())
        if minimum_models
        else None
    )
    extremal = sorted(
        direction
        for direction, model in minimum_models.items()
        if model[-1] == maximum_minimum
    )

    return {
        "schema": "win-00082-p11.mass3-classification.v1",
        "provenance_job_id": JOB_ID,
        "arithmetic": "exact integers only",
        "cutoff": max_diameter,
        "counts": {
            "balanced_nonzero_rows_oriented": len(oriented_rows),
            "balanced_nonzero_rows_modulo_sign": len(canonical_rows),
            "primitive_mass_three_directions_modulo_sign": len(
                primitive_mass_three
            ),
            "tail_feasible_directions_modulo_sign": len(feasible),
            "tail_infeasible_directions_modulo_sign": len(primitive_mass_three)
            - len(feasible),
            "integer_alphabets_through_cutoff": tuple_count,
            "covered_feasible_directions": len(minimum_models),
            "uncovered_feasible_directions": len(uncovered),
        },
        "uncovered_directions": [list(row) for row in uncovered],
        "maximum_minimum_diameter": maximum_minimum,
        "extremal_directions_modulo_sign": [list(row) for row in extremal],
        "directions": directions,
        "relation_free_core_census": {
            "criterion": "all 20 unordered three-term sums are distinct",
            "integer_core_count_through_diameter_11": core_tuple_count,
            "counts_by_exact_diameter": core_counts,
            "minimum_diameter": minimum_cores[0][-1] if minimum_cores else None,
            "minimum_cores": [list(core) for core in minimum_cores],
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--max-diameter", type=int, default=33)
    args = parser.parse_args()
    result = produce(args.max_diameter)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(rendered, end="")
    else:
        args.output.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
