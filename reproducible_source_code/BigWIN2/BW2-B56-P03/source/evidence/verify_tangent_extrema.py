#!/usr/bin/env python3
"""Independent EK/component replay of the five decisive colength-15 ideals.

This verifier intentionally imports no code from tangent_borel15.py.  The four
global maximizers and the unique best m1<=2 competitor are selected from the
primary summary, but their dimensions are recomputed from atlas monomials.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

Exponent = tuple[int, int, int]

ROOT = Path(__file__).resolve().parent
ATLAS = ROOT / "borel-atlas-15.jsonl"
SUMMARY = ROOT / "borel-tangent-summary-15.json"
OUTPUT = ROOT / "tangent-extrema-independent.json"


class Components:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n
        self.zero = [False] * n

    def root(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.root(self.parent[x])
        return self.parent[x]

    def join(self, x: int, y: int) -> None:
        x, y = self.root(x), self.root(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            x, y = y, x
        self.parent[y] = x
        self.zero[x] = self.zero[x] or self.zero[y]
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1

    def force_zero(self, x: int) -> None:
        self.zero[self.root(x)] = True

    def free_components(self) -> int:
        roots = {self.root(x) for x in range(len(self.parent))}
        return sum(1 for x in roots if not self.zero[x])


def minus(a: Exponent, b: Exponent) -> Exponent:
    return tuple(a[k] - b[k] for k in range(3))  # type: ignore[return-value]


def plus(a: Exponent, b: Exponent) -> Exponent:
    return tuple(a[k] + b[k] for k in range(3))  # type: ignore[return-value]


def divides(a: Exponent, b: Exponent) -> bool:
    return all(a[k] <= b[k] for k in range(3))


def last_variable(a: Exponent) -> int:
    return next(k for k in (2, 1, 0) if a[k])


def first_variable(a: Exponent) -> int:
    return next(k for k in (0, 1, 2) if a[k])


def canonical_factorization(
    monomial: Exponent, generators: list[Exponent]
) -> tuple[int, Exponent]:
    """Stable factorization monomial=g*q with max(g)<=min(q)."""
    candidates: list[tuple[int, Exponent]] = []
    for number, generator in enumerate(generators):
        if divides(generator, monomial):
            quotient = minus(monomial, generator)
            if quotient == (0, 0, 0) or last_variable(generator) <= first_variable(quotient):
                candidates.append((number, quotient))
    assert len(candidates) == 1, (monomial, candidates)
    return candidates[0]


def independently_compute(record: dict[str, object]) -> dict[str, object]:
    generators = [tuple(x) for x in record["minimal_generators"]]  # type: ignore[index]
    standards = [tuple(x) for x in record["standard_monomials"]]  # type: ignore[index]
    standard_number = {x: i for i, x in enumerate(standards)}
    block = len(standards)
    graph = Components(block * len(generators))
    syzygy_count = 0
    equation_count = 0
    units: tuple[Exponent, ...] = ((1, 0, 0), (0, 1, 0), (0, 0, 1))

    # Eliahou--Kervaire: one relation for every i<max(g).
    for source_number, generator in enumerate(generators):
        for variable in range(last_variable(generator)):
            target_number, quotient = canonical_factorization(
                plus(generator, units[variable]), generators
            )
            syzygy_count += 1
            for output in standards:
                left_input = minus(output, units[variable])
                right_input = minus(output, quotient)
                left = standard_number.get(left_input)
                right = standard_number.get(right_input)
                if left is None and right is None:
                    continue
                equation_count += 1
                if left is not None and right is not None:
                    graph.join(source_number * block + left, target_number * block + right)
                elif left is not None:
                    graph.force_zero(source_number * block + left)
                else:
                    assert right is not None
                    graph.force_zero(target_number * block + right)

    return {
        "id": record["id"],
        "m": record["m"],
        "generator_count": len(generators),
        "variables": block * len(generators),
        "ek_syzygies": syzygy_count,
        "nonzero_component_equations": equation_count,
        "independent_tangent_dimension": graph.free_components(),
    }


def main() -> int:
    summary = json.loads(SUMMARY.read_text(encoding="ascii"))
    selected_ids = summary["maximizer_ids"] + summary["m1_at_m1_le_2_maximizer_ids"]
    expected = {x: summary["maximum"] for x in summary["maximizer_ids"]}
    expected.update(
        {x: summary["m1_at_m1_le_2_maximum"] for x in summary["m1_at_m1_le_2_maximizer_ids"]}
    )
    atlas = {
        record["id"]: record
        for record in (
            json.loads(line) for line in ATLAS.read_text(encoding="ascii").splitlines()
        )
    }
    assert len(selected_ids) == 5 and len(set(selected_ids)) == 5
    checks = [independently_compute(atlas[identifier]) for identifier in selected_ids]
    for check in checks:
        assert check["independent_tangent_dimension"] == expected[check["id"]], check

    result = {
        "method": "independent Eliahou-Kervaire presentation and pinned-component count",
        "imports_primary_implementation": False,
        "atlas_sha256": hashlib.sha256(ATLAS.read_bytes()).hexdigest(),
        "primary_summary_sha256": hashlib.sha256(SUMMARY.read_bytes()).hexdigest(),
        "selected_global_maximizers": summary["maximizer_ids"],
        "selected_best_m1_le_2": summary["m1_at_m1_le_2_maximizer_ids"],
        "checks": checks,
        "all_five_match_primary": True,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="ascii")
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
