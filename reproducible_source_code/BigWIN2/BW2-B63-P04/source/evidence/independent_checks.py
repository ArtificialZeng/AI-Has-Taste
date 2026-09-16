#!/usr/bin/env python3
"""Independent spot audit of the exhaustive order-21 computation.

This pass uses NetworkX graph objects, a vertex-deletion recurrence for the
independence polynomial, and Bareiss elimination on the Hurwitz matrix.  These
are deliberately different from the level-sequence tree DP and Routh rows in
``census21.py``.  It checks every 5,000th census item plus both endpoints.
"""

from __future__ import annotations

import functools
import hashlib
import importlib.util
import json
from pathlib import Path

import networkx as nx
import numpy as np


ROOT = Path(__file__).resolve().parent
EXPECTED = 2_144_505


def load_primary():
    spec = importlib.util.spec_from_file_location("census21", ROOT / "census21.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def add(a: tuple[int, ...], b: tuple[int, ...]):
    return tuple((a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(max(len(a), len(b))))


def deletion_independence_polynomial(graph: nx.Graph):
    """Exact P(G)=P(G-v)+zP(G-N[v]) recurrence on vertex masks."""
    n = len(graph)
    neighbor_mask = [sum(1 << w for w in graph[v]) for v in range(n)]

    @functools.lru_cache(maxsize=None)
    def visit(mask: int):
        if mask == 0:
            return (1,)
        vertices = [v for v in range(n) if mask >> v & 1]
        v = max(vertices, key=lambda w: (neighbor_mask[w] & mask).bit_count())
        without_v = mask & ~(1 << v)
        excluded = visit(without_v)
        included = (0,) + visit(without_v & ~neighbor_mask[v])
        return add(excluded, included)

    return list(visit((1 << n) - 1))


def hurwitz_determinants(coefficients: list[int]):
    """Leading Hurwitz determinants by fraction-free Bareiss elimination."""
    # a[j] multiplies s^(degree-j).
    a = list(reversed(coefficients))
    degree = len(a) - 1
    matrix = []
    for i in range(1, degree + 1):
        matrix.append([a[2 * j - i] if 0 <= 2 * j - i <= degree else 0 for j in range(1, degree + 1)])
    determinants = [matrix[0][0]]
    previous = 1
    for k in range(degree - 1):
        pivot = matrix[k][k]
        if pivot == 0:
            return determinants + [0]
        for i in range(k + 1, degree):
            for j in range(k + 1, degree):
                numerator = matrix[i][j] * pivot - matrix[i][k] * matrix[k][j]
                assert numerator % previous == 0
                matrix[i][j] = numerator // previous
        previous = pivot
        determinants.append(matrix[k + 1][k + 1])
    return determinants


def bfs_parent(graph: nx.Graph):
    parent = [-1] * len(graph)
    for v, w in nx.bfs_edges(graph, 0):
        parent[w] = v
    return parent


def main():
    primary = load_primary()
    stored_codes = np.memmap(ROOT / "census21" / "canonical.u64", dtype="<u8", mode="r")
    selected_indices = set(range(5_000, EXPECTED + 1, 5_000)) | {1, EXPECTED}
    count = checked = 0
    digest = hashlib.sha256()
    degree_histogram: dict[int, int] = {}
    for count, graph in enumerate(nx.nonisomorphic_trees(21), 1):
        if count not in selected_indices:
            continue
        adjacency = [list(graph[v]) for v in range(21)]
        code = primary.canonical_code(adjacency)
        assert code == int(stored_codes[count - 1])
        deletion_coefficients = deletion_independence_polynomial(graph)
        tree_dp_coefficients = primary.independence_polynomial([0] * 21, bfs_parent(graph))
        assert deletion_coefficients == tree_dp_coefficients
        assert deletion_coefficients[:3] == [1, 21, 190]
        determinants = hurwitz_determinants(deletion_coefficients)
        assert len(determinants) == len(deletion_coefficients) - 1
        assert all(value > 0 for value in determinants)
        status, column = primary.routh_first_column(deletion_coefficients)
        assert status == "regular" and all(value > 0 for value in column)
        degree = len(deletion_coefficients) - 1
        degree_histogram[degree] = degree_histogram.get(degree, 0) + 1
        digest.update((f"{count}|{code:x}|{','.join(map(str, deletion_coefficients))}|{','.join(map(str, determinants))}\n").encode())
        checked += 1
    assert count == EXPECTED
    assert checked == len(selected_indices)
    report = {
        "audit": "independent graph/deletion-polynomial/Bareiss-Hurwitz spot check",
        "networkx_generated_count": count,
        "selection_rule": "indices 1 and 2144505 and every positive multiple of 5000",
        "selected_count": checked,
        "canonical_code_matches": checked,
        "tree_dp_equals_vertex_deletion_recurrence": checked,
        "positive_complete_hurwitz_determinant_sequences": checked,
        "degree_histogram_in_sample": {str(k): v for k, v in sorted(degree_histogram.items())},
        "selected_certificate_sha256": digest.hexdigest(),
        "networkx_version": nx.__version__,
    }
    (ROOT / "census21" / "independent-checks.json").write_text(json.dumps(report, sort_keys=True, indent=2) + "\n")
    print(json.dumps(report, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
