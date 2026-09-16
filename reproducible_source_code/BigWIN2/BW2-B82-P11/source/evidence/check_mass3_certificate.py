#!/usr/bin/env python3
"""Independent exact checker for ``mass3_certificates.json``.

Unlike the producer's coefficient-box enumeration, this checker derives short
relations from differences of unordered multisets and derives mass-three
directions from disjoint weak compositions.  It then repeats the complete
integer-alphabet census through the certified cutoff.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from itertools import combinations, combinations_with_replacement
from math import gcd
from pathlib import Path
from typing import Iterator, Sequence


def vector_gcd(row: Sequence[int]) -> int:
    value = 0
    for x in row:
        value = gcd(value, abs(x))
    return value


def positive_mass(row: Sequence[int]) -> int:
    return sum(x for x in row if x > 0)


def canonical(row: Sequence[int]) -> tuple[int, ...]:
    result = tuple(row)
    first = next(x for x in result if x)
    return result if first > 0 else tuple(-x for x in result)


def count_vector(multiset: Sequence[int], width: int) -> tuple[int, ...]:
    result = [0] * width
    for index in multiset:
        result[index] += 1
    return tuple(result)


def relations_from_multisets(width: int, max_mass: int) -> list[tuple[int, ...]]:
    """Generate every nonzero balanced row up to sign from sum collisions."""

    rows: set[tuple[int, ...]] = set()
    for length in range(1, max_mass + 1):
        multisets = list(combinations_with_replacement(range(width), length))
        vectors = [count_vector(item, width) for item in multisets]
        for left in vectors:
            for right in vectors:
                row = tuple(a - b for a, b in zip(left, right))
                if not any(row):
                    continue
                if positive_mass(row) <= max_mass:
                    rows.add(canonical(row))
    return sorted(rows)


def weak_compositions(total: int, width: int) -> Iterator[tuple[int, ...]]:
    if width == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, width - 1):
            yield (first,) + rest


def primitive_mass_three_directions() -> list[tuple[int, ...]]:
    """Derive directions from their unique positive and negative parts."""

    parts = list(weak_compositions(3, 5))
    rows: set[tuple[int, ...]] = set()
    for positive in parts:
        for negative in parts:
            if any(a and b for a, b in zip(positive, negative)):
                continue
            row = tuple(a - b for a, b in zip(positive, negative))
            if vector_gcd(row) == 1:
                rows.add(canonical(row))
    return sorted(rows)


def tails(row: Sequence[int]) -> tuple[int, ...]:
    return tuple(sum(row[j:]) for j in range(1, 5))


def is_feasible(row: Sequence[int]) -> bool:
    values = tails(row)
    return min(values) < 0 < max(values)


def integer_alphabets(cutoff: int) -> Iterator[tuple[int, ...]]:
    for diameter in range(4, cutoff + 1):
        for middle in combinations(range(1, diameter), 3):
            yield (0,) + middle + (diameter,)


def vanishing_rows(
    alphabet: Sequence[int], rows: Sequence[tuple[int, ...]], stop_after: int | None = None
) -> list[tuple[int, ...]]:
    result = []
    for row in rows:
        if sum(a * s for a, s in zip(row, alphabet)) == 0:
            result.append(row)
            if stop_after is not None and len(result) >= stop_after:
                break
    return result


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check(certificate_path: Path) -> dict[str, object]:
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    assert certificate["schema"] == "win-00082-p11.mass3-classification.v1"
    cutoff = certificate["cutoff"]
    assert cutoff == 33

    relation_rows = relations_from_multisets(5, 3)
    directions = primitive_mass_three_directions()
    feasible = sorted(row for row in directions if is_feasible(row))
    feasible_set = set(feasible)

    entries = certificate["directions"]
    certified_set = {tuple(entry["delta"]) for entry in entries}
    assert len(certified_set) == len(entries)
    assert certified_set == feasible_set
    assert certificate["uncovered_directions"] == []

    for entry in entries:
        direction = tuple(entry["delta"])
        computed_tails = tails(direction)
        gaps = tuple(entry["positive_gap_witness"])
        assert tuple(entry["tail_sums"]) == computed_tails
        assert len(gaps) == 4 and all(gap > 0 for gap in gaps)
        assert sum(a * b for a, b in zip(computed_tails, gaps)) == 0
        model = tuple(entry["minimum_model"])
        assert model[0] == 0 and all(a < b for a, b in zip(model, model[1:]))
        assert model[-1] <= cutoff
        assert vanishing_rows(model, relation_rows) == [direction]

    computed_minimum: dict[tuple[int, ...], tuple[int, ...]] = {}
    computed_occurrences = {row: 0 for row in feasible}
    alphabet_count = 0
    for alphabet in integer_alphabets(cutoff):
        alphabet_count += 1
        zeros = vanishing_rows(alphabet, relation_rows, stop_after=2)
        if len(zeros) == 1 and zeros[0] in feasible_set:
            direction = zeros[0]
            computed_occurrences[direction] += 1
            computed_minimum.setdefault(direction, alphabet)

    assert set(computed_minimum) == feasible_set
    for entry in entries:
        direction = tuple(entry["delta"])
        assert tuple(entry["minimum_model"]) == computed_minimum[direction]
        assert entry["minimum_diameter"] == computed_minimum[direction][-1]
        assert entry["model_count_through_cutoff"] == computed_occurrences[direction]

    maximum_minimum = max(model[-1] for model in computed_minimum.values())
    extremal = sorted(
        row for row, model in computed_minimum.items() if model[-1] == maximum_minimum
    )
    assert certificate["maximum_minimum_diameter"] == maximum_minimum
    assert [list(row) for row in extremal] == certificate[
        "extremal_directions_modulo_sign"
    ]

    core_rows = relations_from_multisets(4, 3)
    core_counts: dict[str, int] = {}
    minimum_cores: list[tuple[int, ...]] = []
    core_count = 0
    for diameter in range(3, 12):
        good = []
        for middle in combinations(range(1, diameter), 2):
            core_count += 1
            core = (0,) + middle + (diameter,)
            if not vanishing_rows(core, core_rows, stop_after=1):
                good.append(core)
        core_counts[str(diameter)] = len(good)
        if good and not minimum_cores:
            minimum_cores = good

    core_certificate = certificate["relation_free_core_census"]
    assert core_counts == core_certificate["counts_by_exact_diameter"]
    assert core_count == core_certificate["integer_core_count_through_diameter_11"]
    assert [list(core) for core in minimum_cores] == core_certificate["minimum_cores"]
    assert minimum_cores[0][-1] == core_certificate["minimum_diameter"]

    cluster_direction = (1, -3, 0, 0, 2)
    for core in minimum_cores:
        _, a, b, c = core
        cluster_model = (0, 2 * c, 2 * c + a, 2 * c + b, 3 * c)
        assert vanishing_rows(cluster_model, relation_rows) == [cluster_direction]

    reported_counts = certificate["counts"]
    computed_counts = {
        "balanced_nonzero_rows_oriented": 2 * len(relation_rows),
        "balanced_nonzero_rows_modulo_sign": len(relation_rows),
        "primitive_mass_three_directions_modulo_sign": len(directions),
        "tail_feasible_directions_modulo_sign": len(feasible),
        "tail_infeasible_directions_modulo_sign": len(directions) - len(feasible),
        "integer_alphabets_through_cutoff": alphabet_count,
        "covered_feasible_directions": len(computed_minimum),
        "uncovered_feasible_directions": len(feasible_set - set(computed_minimum)),
    }
    assert reported_counts == computed_counts

    return {
        "schema": "win-00082-p11.mass3-independent-audit.v1",
        "all_checks_passed": True,
        "arithmetic": "exact integers only",
        "certificate_file": str(certificate_path),
        "certificate_sha256": sha256(certificate_path),
        "checker_sha256": sha256(Path(__file__)),
        "independent_generation": {
            "short_relations": "differences of unordered multisets of lengths 1, 2, 3",
            "mass_three_directions": "disjoint weak compositions of 3",
            "core_test": "direct evaluation of independently generated four-coordinate rows",
        },
        "verified_counts": computed_counts,
        "maximum_minimum_diameter": maximum_minimum,
        "extremal_directions_modulo_sign": [list(row) for row in extremal],
        "minimum_relation_free_core_diameter": minimum_cores[0][-1],
        "minimum_relation_free_cores": [list(core) for core in minimum_cores],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate", type=Path, default=Path("evidence/mass3_certificates.json")
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = check(args.certificate)
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(rendered, end="")
    else:
        args.output.write_text(rendered, encoding="utf-8")


if __name__ == "__main__":
    main()
