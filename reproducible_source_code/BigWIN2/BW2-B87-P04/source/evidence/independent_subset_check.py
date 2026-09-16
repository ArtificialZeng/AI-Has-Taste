#!/usr/bin/env python3
"""Independent exact checker for the frozen five-vertex classification.

This implementation deliberately does not import or reproduce the supplied
partition-based verifier.  It

* enumerates every labeled simple graph on at most five vertices and forms
  isomorphism orbits by an integer edge-mask canonicalization;
* finds flats by testing cycle-matroid closure for every edge subset;
* tests the flat-cover relation explicitly;
* applies the frozen L_e and D formulas over fractions.Fraction; and
* compares every Hilbert vector with a separately supplied census JSON.

The JSON output contains the exact sparse echelon bases, so the rational rank
calculations are inspectable rather than being only a list of dimensions.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations
import json
from math import factorial
from pathlib import Path
from typing import Iterable, Sequence


EXPECTED_REFERENCE_SHA256 = (
    "151aad4a7e4ec0d3f7a2582e7ca604078b65b8cddb8375d7e5891f78328f14d0"
)


def pairs(n: int) -> tuple[tuple[int, int], ...]:
    return tuple(combinations(range(n), 2))


def mask_edges(n: int, mask: int) -> tuple[tuple[int, int], ...]:
    return tuple(edge for i, edge in enumerate(pairs(n)) if mask >> i & 1)


def edges_mask(n: int, edges: Iterable[Sequence[int]]) -> int:
    position = {edge: i for i, edge in enumerate(pairs(n))}
    answer = 0
    for a, b in edges:
        edge = (a, b) if a < b else (b, a)
        answer |= 1 << position[edge]
    return answer


def permute_mask(n: int, mask: int, permutation: Sequence[int]) -> int:
    return edges_mask(
        n,
        ((permutation[a], permutation[b]) for a, b in mask_edges(n, mask)),
    )


def canonical_mask(n: int, mask: int) -> int:
    return min(permute_mask(n, mask, p) for p in permutations(range(n)))


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> None:
        a, b = self.find(a), self.find(b)
        if a != b:
            self.parent[b] = a


def component_roots(n: int, edges: Sequence[tuple[int, int]], mask: int) -> tuple[int, ...]:
    uf = UnionFind(n)
    for i, (a, b) in enumerate(edges):
        if mask >> i & 1:
            uf.union(a, b)
    return tuple(uf.find(v) for v in range(n))


def connected(n: int, mask: int) -> bool:
    if n == 1:
        return True
    roots = component_roots(n, pairs(n), mask)
    return len(set(roots)) == 1


def enumerate_graph_classes() -> tuple[list[tuple[int, int]], dict[int, dict[str, int]]]:
    representatives: list[tuple[int, int]] = []
    audit: dict[int, dict[str, int]] = {}
    for n in range(1, 6):
        total_masks = 1 << len(pairs(n))
        labeled_connected = [mask for mask in range(total_masks) if connected(n, mask)]
        keys = sorted({canonical_mask(n, mask) for mask in labeled_connected})
        representatives.extend((n, key) for key in keys)

        orbit_sum = 0
        for key in keys:
            aut = sum(
                permute_mask(n, key, p) == key for p in permutations(range(n))
            )
            assert factorial(n) % aut == 0
            orbit_sum += factorial(n) // aut
        assert orbit_sum == len(labeled_connected)
        audit[n] = {
            "all_labeled": total_masks,
            "connected_labeled": len(labeled_connected),
            "isomorphism_classes": len(keys),
            "sum_orbit_sizes": orbit_sum,
        }
    assert [audit[n]["isomorphism_classes"] for n in range(1, 6)] == [1, 1, 2, 6, 21]
    assert len(representatives) == 31
    return representatives, audit


def subset_closure(n: int, graph_edges: Sequence[tuple[int, int]], subset: int) -> int:
    roots = component_roots(n, graph_edges, subset)
    closure = 0
    for i, (a, b) in enumerate(graph_edges):
        if roots[a] == roots[b]:
            closure |= 1 << i
    return closure


def subset_rank(n: int, graph_edges: Sequence[tuple[int, int]], subset: int) -> int:
    return n - len(set(component_roots(n, graph_edges, subset)))


def flat_layers(n: int, graph_edges: Sequence[tuple[int, int]]) -> list[list[int]]:
    m = len(graph_edges)
    top_rank = subset_rank(n, graph_edges, (1 << m) - 1)
    layers: list[list[int]] = [[] for _ in range(top_rank + 1)]
    for subset in range(1 << m):
        closure = subset_closure(n, graph_edges, subset)
        assert subset & ~closure == 0
        assert subset_closure(n, graph_edges, closure) == closure
        assert subset_rank(n, graph_edges, subset) == subset_rank(n, graph_edges, closure)
        if closure == subset:
            layers[subset_rank(n, graph_edges, subset)].append(subset)
    for layer in layers:
        layer.sort()
        assert len(layer) == len(set(layer))
    assert layers[0] == [0]
    assert layers[-1] == [(1 << m) - 1]
    return layers


def proper_subset(a: int, b: int) -> bool:
    return a != b and a & ~b == 0


def is_cover(x: int, y: int, all_flats: Sequence[int]) -> bool:
    if not proper_subset(x, y):
        return False
    return not any(proper_subset(x, z) and proper_subset(z, y) for z in all_flats)


def echelon(vectors: Iterable[Sequence[Fraction]], width: int) -> list[list[Fraction]]:
    """Return a deterministic reduced row basis over Q."""
    basis: dict[int, list[Fraction]] = {}
    for raw in vectors:
        vector = list(raw)
        assert len(vector) == width
        for pivot in sorted(basis):
            if vector[pivot]:
                coefficient = vector[pivot]
                vector = [a - coefficient * b for a, b in zip(vector, basis[pivot])]
        pivot = next((i for i, value in enumerate(vector) if value), None)
        if pivot is None:
            continue
        leading = vector[pivot]
        vector = [value / leading for value in vector]
        for old_pivot, old_vector in list(basis.items()):
            if old_vector[pivot]:
                coefficient = old_vector[pivot]
                basis[old_pivot] = [
                    a - coefficient * b for a, b in zip(old_vector, vector)
                ]
        basis[pivot] = vector

    rows = [basis[pivot] for pivot in sorted(basis)]
    pivots: list[int] = []
    for row in rows:
        pivot = next(i for i, value in enumerate(row) if value)
        pivots.append(pivot)
        assert row[pivot] == 1
    assert len(pivots) == len(set(pivots))
    for i, pivot in enumerate(pivots):
        assert all(j == i or rows[j][pivot] == 0 for j in range(len(rows)))
    return rows


def apply_operators(
    graph_edges: Sequence[tuple[int, int]],
    low: Sequence[int],
    high: Sequence[int],
    rank_y: int,
    base: Sequence[Sequence[Fraction]],
    all_flats: Sequence[int],
) -> list[list[Fraction]]:
    m = len(graph_edges)
    covers = [[is_cover(x, y, all_flats) for y in high] for x in low]
    # In a matroid flat lattice, inclusion across adjacent ranks is precisely a cover.
    for i, x in enumerate(low):
        for j, y in enumerate(high):
            assert covers[i][j] == proper_subset(x, y)

    vectors: list[list[Fraction]] = []
    for operator in range(m + 1):  # edges first, D last
        for input_vector in base:
            output: list[Fraction] = []
            for i, x in enumerate(low):
                total = Fraction(0)
                for j, y in enumerate(high):
                    if not covers[i][j]:
                        continue
                    difference = y & ~x
                    if operator < m:
                        coefficient = Fraction((difference >> operator) & 1)
                    else:
                        denominator = m - x.bit_count()
                        assert denominator > 0
                        coefficient = Fraction(
                            rank_y * difference.bit_count(), denominator
                        )
                    total += coefficient * input_vector[j]
                output.append(total)
            vectors.append(output)
    return vectors


def serialize_basis(
    layer: Sequence[int], basis: Sequence[Sequence[Fraction]]
) -> list[dict[str, object]]:
    output: list[dict[str, object]] = []
    for vector in basis:
        entries = [
            [flat, str(value)] for flat, value in zip(layer, vector) if value
        ]
        output.append({"entries": entries})
    return output


def hilbert_with_certificate(
    n: int, graph_edges: Sequence[tuple[int, int]]
) -> tuple[list[int], dict[str, object]]:
    layers = flat_layers(n, graph_edges)
    all_flats = [flat for layer in layers for flat in layer]
    top_rank = len(layers) - 1
    base: list[list[Fraction]] = [[Fraction(1)]]
    dims = [1]
    spaces: list[dict[str, object]] = [
        {
            "j": 0,
            "flat_rank": top_rank,
            "basis": serialize_basis(layers[top_rank], base),
        }
    ]
    for rank_y in range(top_rank, 0, -1):
        low, high = layers[rank_y - 1], layers[rank_y]
        generated = apply_operators(
            graph_edges, low, high, rank_y, base, all_flats
        )
        base = echelon(generated, len(low))
        dims.append(len(base))
        spaces.append(
            {
                "j": top_rank - rank_y + 1,
                "flat_rank": rank_y - 1,
                "basis": serialize_basis(low, base),
            }
        )

    assert len(dims) == top_rank + 1
    assert dims == [len(space["basis"]) for space in spaces]
    certificate: dict[str, object] = {
        "vertex_count": n,
        "edges": [list(edge) for edge in graph_edges],
        "rank": top_rank,
        "flat_layers": layers,
        "flat_counts": [len(layer) for layer in layers],
        "cyclic_spaces": spaces,
    }
    return dims, certificate


def shifted_sum(h: Sequence[int]) -> list[int]:
    return [
        (h[j] if j < len(h) else 0) + (h[j - 1] if 0 < j <= len(h) else 0)
        for j in range(len(h) + 1)
    ]


def complement_type(n: int, graph_mask: int) -> tuple[bool, tuple[int, ...]]:
    complete = (1 << len(pairs(n))) - 1
    complement = complete ^ graph_mask
    comp_edges = mask_edges(n, complement)
    adjacency = [set() for _ in range(n)]
    for a, b in comp_edges:
        adjacency[a].add(b)
        adjacency[b].add(a)
    seen: set[int] = set()
    component_sizes: list[int] = []
    is_linear_forest = True
    for start in range(n):
        if start in seen:
            continue
        todo = [start]
        component: set[int] = set()
        while todo:
            vertex = todo.pop()
            if vertex in component:
                continue
            component.add(vertex)
            todo.extend(adjacency[vertex] - component)
        seen.update(component)
        internal_edges = sum(
            a in component and b in component for a, b in comp_edges
        )
        if internal_edges != len(component) - 1:
            is_linear_forest = False
        if any(len(adjacency[vertex]) > 2 for vertex in component):
            is_linear_forest = False
        component_sizes.append(len(component))
    return is_linear_forest, tuple(sorted(component_sizes, reverse=True))


def expected_delta(n: int, graph_mask: int) -> list[int]:
    zero = [0] * (n + 1)
    if n < 5:
        return zero
    linear, kind = complement_type(n, graph_mask)
    if not linear:
        return zero
    table = {
        (5,): [0, 0, 2, 2, 0, 0],
        (4, 1): [0, 0, 2, 2, 0, 0],
        (3, 2): [0, 0, 2, 2, 0, 0],
        (3, 1, 1): [0, 0, 1, 2, 0, 0],
        (2, 2, 1): [0, 0, 4, 0, 0, 0],
        (2, 1, 1, 1): [0, 0, 4, 0, 0, 0],
        (1, 1, 1, 1, 1): [0, 0, 4, 0, 0, 0],
    }
    assert kind in table
    return table[kind]


def reference_rows(path: Path) -> tuple[dict[tuple[int, int], dict[str, object]], str]:
    raw = path.read_bytes()
    digest = sha256(raw).hexdigest()
    assert digest == EXPECTED_REFERENCE_SHA256, (digest, EXPECTED_REFERENCE_SHA256)
    rows = json.loads(raw)
    by_key: dict[tuple[int, int], dict[str, object]] = {}
    for row in rows:
        n = row["n"]
        key = canonical_mask(n, edges_mask(n, row["edges"]))
        assert (n, key) not in by_key
        by_key[(n, key)] = row
    assert len(by_key) == 31
    return by_key, digest


def theta_mask() -> int:
    # Endpoints 0,1; paths 0-1, 0-2-1, and 0-3-4-1.
    return edges_mask(5, [(0, 1), (0, 2), (2, 1), (0, 3), (3, 4), (4, 1)])


def run(reference_path: Path) -> dict[str, object]:
    classes, orbit_audit = enumerate_graph_classes()
    reference, reference_digest = reference_rows(reference_path)
    assert set(classes) == set(reference)

    rows: list[dict[str, object]] = []
    mismatches: list[dict[str, object]] = []
    for n, graph_mask in classes:
        graph_edges = mask_edges(n, graph_mask)
        h, certificate = hilbert_with_certificate(n, graph_edges)

        plus_edges = graph_edges + ((0, n),)
        h_plus, certificate_plus = hilbert_with_certificate(n + 1, plus_edges)
        expected_product = shifted_sum(h)
        delta = [a - b for a, b in zip(h_plus, expected_product)]

        frozen_expected = expected_delta(n, graph_mask)
        assert delta == frozen_expected, (n, graph_edges, delta, frozen_expected)
        supplied = reference[(n, graph_mask)]
        comparisons = {
            "H": h == supplied["H"],
            "Hplus": h_plus == supplied["Hplus"],
            "delta": delta == supplied["delta"],
        }
        if not all(comparisons.values()):
            mismatches.append(
                {
                    "n": n,
                    "canonical_mask": graph_mask,
                    "comparisons": comparisons,
                    "computed": {"H": h, "Hplus": h_plus, "delta": delta},
                    "supplied": {
                        "H": supplied["H"],
                        "Hplus": supplied["Hplus"],
                        "delta": supplied["delta"],
                    },
                }
            )

        linear, comp_type = complement_type(n, graph_mask)
        rows.append(
            {
                "n": n,
                "canonical_mask": graph_mask,
                "edges": [list(edge) for edge in graph_edges],
                "edge_count": len(graph_edges),
                "complement_is_linear_forest": linear,
                "complement_component_sizes": list(comp_type),
                "H": h,
                "Hplus": h_plus,
                "delta": delta,
                "reference_comparisons": comparisons,
                "certificate": certificate,
                "certificate_plus": certificate_plus,
            }
        )

    assert not mismatches
    nonzero = [row for row in rows if any(row["delta"])]
    assert len(nonzero) == 7
    assert all(row["n"] == 5 for row in nonzero)
    assert all(row["complement_is_linear_forest"] for row in nonzero)
    assert all(
        bool(any(row["delta"]))
        == (row["n"] == 5 and row["complement_is_linear_forest"])
        for row in rows
    )
    least_edges = min(row["edge_count"] for row in nonzero)
    least = [row for row in nonzero if row["edge_count"] == least_edges]
    assert least_edges == 6 and len(least) == 1
    least_row = least[0]
    assert least_row["H"] == [1, 6, 11, 6, 1]
    assert least_row["Hplus"] == [1, 7, 19, 19, 7, 1]

    p5 = edges_mask(5, [(0, 1), (1, 2), (2, 3), (3, 4)])
    k5_minus_p5 = ((1 << len(pairs(5))) - 1) ^ p5
    assert canonical_mask(5, least_row["canonical_mask"]) == canonical_mask(5, k5_minus_p5)
    assert canonical_mask(5, least_row["canonical_mask"]) == canonical_mask(5, theta_mask())

    return {
        "method": {
            "graph_enumeration": "all labeled edge masks, quotiented by all vertex permutations",
            "flat_enumeration": "all edge subsets fixed by graphic closure",
            "covers": "explicit absence of an intermediate flat",
            "coefficient_field": "fractions.Fraction (exact Q)",
            "operators": "the frozen L_e and D formulas",
            "coloop_model": "one new pendant edge and vertex",
        },
        "reference_path_argument": str(reference_path),
        "reference_sha256": reference_digest,
        "orbit_audit": {str(n): values for n, values in orbit_audit.items()},
        "class_count": len(rows),
        "all_hilbert_vectors_match_reference": True,
        "mismatches": mismatches,
        "nonzero_count": len(nonzero),
        "least_edge_failure": {
            "edge_count": least_edges,
            "unique": len(least) == 1,
            "canonical_mask": least_row["canonical_mask"],
            "edges": least_row["edges"],
            "H": least_row["H"],
            "Hplus": least_row["Hplus"],
            "isomorphic_to_K5_minus_P5": True,
            "isomorphic_to_theta_1_2_3": True,
        },
        "rows": rows,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--reference", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.reference)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(
        json.dumps(
            {
                "class_count": result["class_count"],
                "all_hilbert_vectors_match_reference": result[
                    "all_hilbert_vectors_match_reference"
                ],
                "mismatch_count": len(result["mismatches"]),
                "nonzero_count": result["nonzero_count"],
                "least_edge_failure": result["least_edge_failure"],
                "output": str(args.output),
                "output_sha256": sha256(args.output.read_bytes()).hexdigest(),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
