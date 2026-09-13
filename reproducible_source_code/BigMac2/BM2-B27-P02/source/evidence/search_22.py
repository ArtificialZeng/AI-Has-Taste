#!/usr/bin/env python
"""Reproduce the constructive cycle-cut search that found a 22-set.

This is a witness finder, not a negative certificate. Its output is accepted
only after exact graph checks here and the separate dependency-free verifier in
verify_22.py. Run it with the configured research interpreter.
"""

from __future__ import annotations

import json

import networkx as nx
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import lil_matrix


N = 8
VERTICES = list(range(N * N))


def vertex(i: int, j: int) -> int:
    return (i % N) * N + (j % N)


EDGES = sorted(
    {
        tuple(sorted((vertex(i, j), vertex(i + 1, j))))
        for i in range(N)
        for j in range(N)
    }
    | {
        tuple(sorted((vertex(i, j), vertex(i, j + 1))))
        for i in range(N)
        for j in range(N)
    }
)
SPECIAL_EDGE = tuple(sorted((vertex(0, 0), vertex(0, 1))))


def complement_graph(selected: set[int]) -> nx.Graph:
    remaining = set(VERTICES) - selected
    graph = nx.Graph()
    graph.add_nodes_from(sorted(remaining))
    graph.add_edges_from((u, v) for u, v in EDGES if u in remaining and v in remaining)
    return graph


def main() -> None:
    cycles: list[frozenset[int]] = []
    seen_cycles: set[frozenset[int]] = set()

    def add_cycle(raw_cycle: list[int]) -> None:
        cycle = frozenset(raw_cycle)
        if cycle not in seen_cycles:
            seen_cycles.add(cycle)
            cycles.append(cycle)

    # Seed the cut pool with every facial square and every row/column ring.
    for i in range(N):
        for j in range(N):
            add_cycle(
                [
                    vertex(i, j),
                    vertex(i + 1, j),
                    vertex(i, j + 1),
                    vertex(i + 1, j + 1),
                ]
            )
    for i in range(N):
        add_cycle([vertex(i, j) for j in range(N)])
    for j in range(N):
        add_cycle([vertex(i, j) for i in range(N)])

    for iteration in range(300):
        rows: list[dict[int, int]] = []
        lower: list[float] = []
        upper: list[float] = []

        rows.append({v: 1 for v in VERTICES})
        lower.append(22)
        upper.append(22)
        for endpoint in SPECIAL_EDGE:
            rows.append({endpoint: 1})
            lower.append(1)
            upper.append(1)
        for u, v in EDGES:
            if (u, v) != SPECIAL_EDGE:
                rows.append({u: 1, v: 1})
                lower.append(-np.inf)
                upper.append(1)
        for cycle in cycles:
            rows.append({v: 1 for v in cycle})
            lower.append(1)
            upper.append(np.inf)

        matrix = lil_matrix((len(rows), len(VERTICES)), dtype=float)
        for row_index, row in enumerate(rows):
            for column, coefficient in row.items():
                matrix[row_index, column] = coefficient

        # A fixed tiny random objective makes successive feasible points varied
        # while leaving all mathematical requirements in the constraints.
        objective = np.random.default_rng(1777 + iteration).random(64) * 1e-4
        result = milp(
            objective,
            integrality=np.ones(64),
            bounds=Bounds(0, 1),
            constraints=LinearConstraint(matrix.tocsr(), lower, upper),
            options={"time_limit": 30},
        )
        if result.x is None:
            raise RuntimeError(
                "No candidate returned; this operational failure is not an exclusion proof"
            )

        selected = {v for v, value in enumerate(result.x) if value > 0.5}
        assert len(selected) == 22
        assert all(endpoint in selected for endpoint in SPECIAL_EDGE)
        assert {
            edge for edge in EDGES if edge[0] in selected and edge[1] in selected
        } == {SPECIAL_EDGE}

        graph = complement_graph(selected)
        cycle_basis = nx.cycle_basis(graph)
        if not cycle_basis:
            assert nx.is_tree(graph)
            coordinates = sorted([v // N, v % N] for v in selected)
            print(
                json.dumps(
                    {
                        "found": True,
                        "iteration": iteration,
                        "selected": coordinates,
                        "complement_vertices": graph.number_of_nodes(),
                        "complement_edges": graph.number_of_edges(),
                        "complement_is_tree": True,
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                )
            )
            return

        for cycle in cycle_basis:
            add_cycle(cycle)
        for cycle in nx.minimum_cycle_basis(graph):
            add_cycle(cycle)

    raise RuntimeError(
        "Iteration budget ended without a witness; this is not evidence that no 22-set exists"
    )


if __name__ == "__main__":
    main()
