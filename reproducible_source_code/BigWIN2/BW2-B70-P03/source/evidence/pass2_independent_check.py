#!/usr/bin/env python3
"""Independent small-case checker for the anchored cubical chain complex.

This intentionally does not import anchored_cubical.py.  It enumerates all
product cells from the full factor alphabet, forms signed faces, and performs
sparse Gaussian elimination over finite fields.  It also builds the
compatibility nerve directly for the r=2 rank comparison.
"""

from __future__ import annotations

from collections import defaultdict
from itertools import combinations, product
import json
import math


def connected(vertices, edges):
    if not vertices:
        return False
    adjacency = {v: set() for v in vertices}
    for u, v in edges:
        adjacency[u].add(v)
        adjacency[v].add(u)
    seen = {vertices[0]}
    stack = [vertices[0]]
    while stack:
        stack.extend(adjacency[stack.pop()] - seen)
        seen.update(stack)
    return len(seen) == len(vertices)


def cells_and_boundaries(vertices, edges, anchors, n):
    vertex_factors = [("v", v) for v in vertices]
    edge_factors = [("e", u, v) for u, v in edges]
    by_dimension = defaultdict(list)
    for cell in product(vertex_factors + edge_factors, repeat=n):
        present = {factor[1] for factor in cell if factor[0] == "v"}
        if anchors <= present:
            by_dimension[sum(factor[0] == "e" for factor in cell)].append(cell)
    cells = [by_dimension[d] for d in range(n - len(anchors) + 1)]
    boundaries = [[]]
    for d in range(1, len(cells)):
        row = {cell: index for index, cell in enumerate(cells[d - 1])}
        columns = []
        for cell in cells[d]:
            column = {}
            edge_number = 0
            for coordinate, factor in enumerate(cell):
                if factor[0] != "e":
                    continue
                sign = -1 if edge_number % 2 else 1
                for endpoint, endpoint_sign in ((factor[1], -1), (factor[2], 1)):
                    face = list(cell)
                    face[coordinate] = ("v", endpoint)
                    index = row[tuple(face)]
                    column[index] = column.get(index, 0) + sign * endpoint_sign
                edge_number += 1
            columns.append(column)
        boundaries.append(columns)
    return cells, boundaries


def rank_mod_p(columns, p):
    pivots = {}
    for original in columns:
        column = {row: value % p for row, value in original.items() if value % p}
        while column:
            pivot = min(column)
            if pivot not in pivots:
                inverse = pow(column[pivot], -1, p)
                pivots[pivot] = {row: value * inverse % p for row, value in column.items()}
                break
            multiplier = column[pivot]
            for row, value in pivots[pivot].items():
                replacement = (column.get(row, 0) - multiplier * value) % p
                if replacement:
                    column[row] = replacement
                else:
                    column.pop(row, None)
    return len(pivots)


def check_square_zero(boundaries):
    for d in range(2, len(boundaries)):
        for column in boundaries[d]:
            image = {}
            for middle, coefficient in column.items():
                for row, lower_coefficient in boundaries[d - 1][middle].items():
                    image[row] = image.get(row, 0) + coefficient * lower_coefficient
            if any(image.values()):
                return False
    return True


def field_betti(cells, boundaries, p):
    ranks = [0] + [rank_mod_p(boundary, p) for boundary in boundaries[1:]]
    return [
        len(cells[d]) - ranks[d] - (ranks[d + 1] if d + 1 < len(ranks) else 0)
        for d in range(len(cells))
    ]


def compatibility_nerve_r2(m, p):
    injections = [(a, b) for a in range(m) for b in range(m) if a != b]
    simplices = defaultdict(list)
    for mask in range(1, 1 << len(injections)):
        chosen = tuple(index for index in range(len(injections)) if mask >> index & 1)
        assignments = {}
        compatible = True
        for index in chosen:
            a, b = injections[index]
            for coordinate, anchor in ((a, 0), (b, 1)):
                if coordinate in assignments and assignments[coordinate] != anchor:
                    compatible = False
                    break
                assignments[coordinate] = anchor
            if not compatible:
                break
        if compatible:
            simplices[len(chosen) - 1].append(chosen)
    max_dimension = max(simplices)
    cells = [simplices[d] for d in range(max_dimension + 1)]
    boundaries = [[]]
    for d in range(1, len(cells)):
        row = {simplex: index for index, simplex in enumerate(cells[d - 1])}
        columns = []
        for simplex in cells[d]:
            column = {}
            for omitted in range(d + 1):
                face = simplex[:omitted] + simplex[omitted + 1 :]
                column[row[face]] = -1 if omitted % 2 else 1
            columns.append(column)
        boundaries.append(columns)
    assert check_square_zero(boundaries)
    return field_betti(cells, boundaries, p), [len(group) for group in cells]


def predicted_connected_betti(cycle_rank, r, n, nerve_betti):
    dimension = n - r
    answer = [0] * (dimension + 1)
    for j in range(dimension + 1):
        m = n - j
        betti = [1] if r == 1 else nerve_betti[m]
        multiplier = math.comb(n, j) * cycle_rank**j
        for degree, value in enumerate(betti):
            total_degree = j + degree
            if total_degree <= dimension:
                answer[total_degree] += multiplier * value
    return answer


def predicted_cell_counts(vertex_count, edge_count, r, n):
    answer = []
    for d in range(n - r + 1):
        onto_anchor_count = sum(
            (-1) ** omitted
            * math.comb(r, omitted)
            * (vertex_count - omitted) ** (n - d)
            for omitted in range(r + 1)
        )
        answer.append(math.comb(n, d) * edge_count**d * onto_anchor_count)
    return answer


def all_graphs(vertex_count):
    vertices = tuple(range(vertex_count))
    possible_edges = tuple(combinations(vertices, 2))
    for mask in range(1 << len(possible_edges)):
        edges = tuple(edge for index, edge in enumerate(possible_edges) if mask >> index & 1)
        if connected(vertices, edges):
            yield vertices, edges


def main():
    primes = (2, 3, 5)
    nerve = {}
    nerve_cell_counts = {}
    for p in primes:
        nerve[p] = {}
        for m in (2, 3, 4):
            nerve[p][m], nerve_cell_counts[m] = compatibility_nerve_r2(m, p)

    tested = {"r1_n3": 0, "r2_n4": 0}
    maximum_cells = {"r1_n3": [0, 0, 0], "r2_n4": [0, 0, 0]}
    failures = []
    graph_counts = {}
    for vertex_count in range(1, 5):
        graphs = list(all_graphs(vertex_count))
        graph_counts[str(vertex_count)] = len(graphs)
        for vertices, edges in graphs:
            cycle_rank = len(edges) - len(vertices) + 1
            for anchor in vertices:
                cells, boundaries = cells_and_boundaries(vertices, edges, {anchor}, 3)
                tested["r1_n3"] += 1
                maximum_cells["r1_n3"] = [max(a, b) for a, b in zip(maximum_cells["r1_n3"], map(len, cells))]
                expected = predicted_connected_betti(cycle_rank, 1, 3, None)
                expected_cells = predicted_cell_counts(len(vertices), len(edges), 1, 3)
                if list(map(len, cells)) != expected_cells:
                    failures.append(["cell-count", vertex_count, edges, [anchor], 3])
                if not check_square_zero(boundaries):
                    failures.append(["square", vertex_count, edges, [anchor], 3])
                for p in primes:
                    observed = field_betti(cells, boundaries, p)
                    if observed != expected:
                        failures.append(["rank", p, vertex_count, edges, [anchor], observed, expected])

            if vertex_count >= 2:
                for anchors in combinations(vertices, 2):
                    cells, boundaries = cells_and_boundaries(vertices, edges, set(anchors), 4)
                    tested["r2_n4"] += 1
                    maximum_cells["r2_n4"] = [max(a, b) for a, b in zip(maximum_cells["r2_n4"], map(len, cells))]
                    if not check_square_zero(boundaries):
                        failures.append(["square", vertex_count, edges, anchors, 4])
                    expected_cells = predicted_cell_counts(len(vertices), len(edges), 2, 4)
                    if list(map(len, cells)) != expected_cells:
                        failures.append(["cell-count", vertex_count, edges, anchors, 4])
                    for p in primes:
                        expected = predicted_connected_betti(cycle_rank, 2, 4, nerve[p])
                        observed = field_betti(cells, boundaries, p)
                        if observed != expected:
                            failures.append(["rank", p, vertex_count, edges, anchors, observed, expected])

    output = {
        "arithmetic": "exact integer boundaries and finite fields",
        "primes": list(primes),
        "connected_labeled_graph_counts": graph_counts,
        "tested_graph_anchor_pairs": tested,
        "maximum_cell_counts": maximum_cells,
        "compatibility_nerve_r2_cell_counts": nerve_cell_counts,
        "compatibility_nerve_r2_betti_by_prime": {
            str(p): {str(m): nerve[p][m] for m in nerve[p]} for p in primes
        },
        "boundary_square_and_rank_failures": failures,
        "all_checks_passed": not failures,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
