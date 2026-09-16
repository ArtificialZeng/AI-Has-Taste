#!/usr/bin/env python3
"""Exact tangent dimensions for the colength-15 Borel atlas.

Method A presents a monomial ideal by all pairwise Taylor syzygies and takes
the exact rational rank of the resulting generator-image matrix with SymPy.

Method B is deliberately separate: for these stable ideals it constructs the
Eliahou--Kervaire first syzygies from the canonical stable decomposition, then
counts the unpinned connected components of the coefficient graph.  Every
equation has the form v=0 or v=w, so that count is its exact nullity over any
field.  The two methods are compared record by record.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path
from typing import Sequence

from sympy import SparseMatrix

Point = tuple[int, int, int]
Relation = tuple[int, Point, int, Point]


def add(a: Point, b: Point) -> Point:
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def sub(a: Point, b: Point) -> Point:
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def divides(a: Point, b: Point) -> bool:
    return all(a[i] <= b[i] for i in range(3))


def maximum_variable(a: Point) -> int:
    return max(i for i, exponent in enumerate(a) if exponent)


def minimum_variable(a: Point) -> int:
    return min(i for i, exponent in enumerate(a) if exponent)


def taylor_relations(generators: Sequence[Point]) -> list[Relation]:
    """All Taylor pair relations (L/g_i)e_i-(L/g_j)e_j."""
    relations: list[Relation] = []
    for i, a in enumerate(generators):
        for j in range(i + 1, len(generators)):
            b = generators[j]
            lcm = tuple(max(a[k], b[k]) for k in range(3))
            relations.append((i, sub(lcm, a), j, sub(lcm, b)))
    return relations


def stable_decomposition(v: Point, generators: Sequence[Point]) -> tuple[int, Point]:
    """Return the unique v=g*c with max(g)<=min(c) for a stable ideal."""
    answers: list[tuple[int, Point]] = []
    for i, g in enumerate(generators):
        if not divides(g, v):
            continue
        c = sub(v, g)
        if c == (0, 0, 0) or maximum_variable(g) <= minimum_variable(c):
            answers.append((i, c))
    if len(answers) != 1:
        raise AssertionError(f"stable decomposition of {v}: {answers}")
    return answers[0]


def eliahou_kervaire_relations(generators: Sequence[Point]) -> list[Relation]:
    """First EK syzygies x_i e_g-c e_{g(x_i g)}, i<max(g)."""
    relations: list[Relation] = []
    units: tuple[Point, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    for source, g in enumerate(generators):
        for variable in range(maximum_variable(g)):
            v = add(g, units[variable])
            target, cofactor = stable_decomposition(v, generators)
            relations.append((source, units[variable], target, cofactor))
    return relations


def relation_rows(
    standards: Sequence[Point], generators: Sequence[Point], relations: Sequence[Relation]
) -> tuple[list[dict[int, int]], int]:
    """Version of coefficient_rows with an explicit, reliable width."""
    standard_index = {monomial: i for i, monomial in enumerate(standards)}
    block = len(standards)
    rows: list[dict[int, int]] = []
    for left_generator, left_shift, right_generator, right_shift in relations:
        for target in standards:
            row: dict[int, int] = {}
            left_source = sub(target, left_shift)
            if left_source in standard_index:
                column = left_generator * block + standard_index[left_source]
                row[column] = row.get(column, 0) + 1
            right_source = sub(target, right_shift)
            if right_source in standard_index:
                column = right_generator * block + standard_index[right_source]
                row[column] = row.get(column, 0) - 1
            row = {column: value for column, value in row.items() if value}
            if row:
                rows.append(row)
    return rows, len(generators) * block


def rational_nullity(rows: Sequence[dict[int, int]], columns: int) -> tuple[int, int]:
    entries = {
        (row_index, column): value
        for row_index, row in enumerate(rows)
        for column, value in row.items()
    }
    rank = int(SparseMatrix(len(rows), columns, entries).rank())
    return columns - rank, rank


class PinnedComponents:
    """Union-find for equations v=w and v=0."""

    def __init__(self, size: int) -> None:
        self.parent = list(range(size))
        self.weight = [1] * size
        self.pinned = [False] * size

    def find(self, a: int) -> int:
        while self.parent[a] != a:
            self.parent[a] = self.parent[self.parent[a]]
            a = self.parent[a]
        return a

    def union(self, a: int, b: int) -> None:
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.weight[a] < self.weight[b]:
            a, b = b, a
        self.parent[b] = a
        self.weight[a] += self.weight[b]
        self.pinned[a] = self.pinned[a] or self.pinned[b]

    def pin(self, a: int) -> None:
        self.pinned[self.find(a)] = True

    def nullity(self) -> int:
        roots = {self.find(a) for a in range(len(self.parent))}
        return sum(not self.pinned[root] for root in roots)


def component_nullity(rows: Sequence[dict[int, int]], columns: int) -> int:
    components = PinnedComponents(columns)
    for row in rows:
        if len(row) == 1:
            (variable, coefficient), = row.items()
            if coefficient not in (-1, 1):
                raise AssertionError(row)
            components.pin(variable)
        elif len(row) == 2:
            items = list(row.items())
            if {items[0][1], items[1][1]} != {-1, 1}:
                raise AssertionError(row)
            components.union(items[0][0], items[1][0])
        else:
            raise AssertionError(row)
    return components.nullity()


def read_atlas(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="ascii").splitlines()]


def analyze(record: dict[str, object]) -> dict[str, object]:
    standards = [tuple(p) for p in record["standard_monomials"]]  # type: ignore[index]
    generators = [tuple(p) for p in record["minimal_generators"]]  # type: ignore[index]

    taylor = taylor_relations(generators)
    taylor_rows, columns = relation_rows(standards, generators, taylor)
    nullity, rank = rational_nullity(taylor_rows, columns)

    ek = eliahou_kervaire_relations(generators)
    ek_rows, ek_columns = relation_rows(standards, generators, ek)
    if ek_columns != columns:
        raise AssertionError((columns, ek_columns))
    independent_nullity = component_nullity(ek_rows, columns)
    if independent_nullity != nullity:
        raise AssertionError(
            f"method mismatch for {record['id']}: Taylor={nullity}, EK={independent_nullity}"
        )

    return {
        "id": record["id"],
        "m": record["m"],
        "generator_count": len(generators),
        "variables": columns,
        "taylor_syzygies": len(taylor),
        "taylor_nonzero_rows": len(taylor_rows),
        "taylor_rank_Q": rank,
        "tangent_dimension": nullity,
        "ek_syzygies": len(ek),
        "ek_nonzero_rows": len(ek_rows),
        "ek_component_nullity": independent_nullity,
        "methods_agree": True,
        "minimal_generators": record["minimal_generators"],
        "standard_monomials": record["standard_monomials"],
    }


def canonical_line(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def run(atlas_path: Path, output_dir: Path) -> dict[str, object]:
    atlas_bytes = atlas_path.read_bytes()
    records = read_atlas(atlas_path)
    results = [analyze(record) for record in records]
    if len(results) != 107 or len({r["id"] for r in results}) != 107:
        raise AssertionError("expected 107 distinct atlas records")

    maximum = max(int(r["tangent_dimension"]) for r in results)
    maximizers = [r for r in results if r["tangent_dimension"] == maximum]
    lower_m1 = [r for r in results if int(r["m"][0]) <= 2]  # type: ignore[index]
    lower_maximum = max(int(r["tangent_dimension"]) for r in lower_m1)
    lower_maximizers = [r for r in lower_m1 if r["tangent_dimension"] == lower_maximum]

    output = ("\n".join(canonical_line(r) for r in results) + "\n").encode("ascii")
    table_path = output_dir / "borel-tangents-15.jsonl"
    table_path.write_bytes(output)

    dimensions_by_m1: dict[str, dict[str, int]] = {}
    for m1 in (1, 2, 3):
        subset = [r for r in results if int(r["m"][0]) == m1]  # type: ignore[index]
        dimensions_by_m1[str(m1)] = {
            "count": len(subset),
            "maximum": max(int(r["tangent_dimension"]) for r in subset),
            "minimum": min(int(r["tangent_dimension"]) for r in subset),
        }

    histogram = Counter(int(r["tangent_dimension"]) for r in results)
    summary: dict[str, object] = {
        "colength": 15,
        "atlas_file": atlas_path.name,
        "atlas_sha256": hashlib.sha256(atlas_bytes).hexdigest(),
        "records": len(results),
        "arithmetic": "exact integer matrix entries and rank over Q",
        "primary_method": "all Taylor pair syzygies; SymPy SparseMatrix.rank over Q",
        "independent_method": "Eliahou-Kervaire first syzygies; pinned-component nullity",
        "independent_checks": len(results),
        "all_methods_agree": True,
        "tangent_table_file": table_path.name,
        "tangent_table_sha256": hashlib.sha256(output).hexdigest(),
        "tangent_table_bytes": len(output),
        "maximum": maximum,
        "maximizer_count": len(maximizers),
        "maximizer_ids": [r["id"] for r in maximizers],
        "maximizers": maximizers,
        "m1_at_m1_le_2_maximum": lower_maximum,
        "m1_at_m1_le_2_maximizer_count": len(lower_maximizers),
        "m1_at_m1_le_2_maximizer_ids": [r["id"] for r in lower_maximizers],
        "m1_at_m1_le_2_maximizers": lower_maximizers,
        "dimensions_by_m1": dimensions_by_m1,
        "dimension_histogram": {str(k): histogram[k] for k in sorted(histogram)},
    }
    summary_path = output_dir / "borel-tangent-summary-15.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="ascii")
    return summary


def main(argv: Sequence[str] | None = None) -> int:
    default_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser()
    parser.add_argument("--atlas", type=Path, default=default_dir / "borel-atlas-15.jsonl")
    parser.add_argument("--output-dir", type=Path, default=default_dir)
    args = parser.parse_args(argv)
    args.output_dir.mkdir(parents=True, exist_ok=True)
    summary = run(args.atlas, args.output_dir)
    compact = {
        key: summary[key]
        for key in (
            "records", "all_methods_agree", "maximum", "maximizer_ids",
            "m1_at_m1_le_2_maximum", "m1_at_m1_le_2_maximizer_ids",
            "dimensions_by_m1", "tangent_table_sha256",
        )
    }
    print(json.dumps(compact, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
