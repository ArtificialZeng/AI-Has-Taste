#!/usr/bin/env python3
"""Exact cellular chains for anchored configuration spaces of finite graphs.

Cells are encoded directly from Definition 4.13: a product cell is retained
iff every anchor occurs as a vertex factor.  All arithmetic used for boundary
checks and finite-field ranks is exact.
"""

from __future__ import annotations

import argparse
from collections import Counter
import itertools
import json
from pathlib import Path

import networkx as nx


def graph_edges(graph: nx.Graph) -> list[tuple[int, int]]:
    """Return the fixed orientation u -> v, u < v, in lexicographic order."""
    return sorted((min(u, v), max(u, v)) for u, v in graph.edges())


def anchored_cells(
    vertices: tuple[int, ...],
    edges: list[tuple[int, int]],
    anchors: frozenset[int],
    n: int,
) -> list[list[tuple[int, ...]]]:
    """Enumerate all anchored product cells, grouped by dimension.

    A vertex factor v is encoded by v.  Edge e_j is encoded by |V|+j.
    """
    nv = len(vertices)
    max_dim = n - len(anchors)
    result: list[list[tuple[int, ...]]] = []
    positions = range(n)
    for dim in range(max_dim + 1):
        cells: list[tuple[int, ...]] = []
        for edge_positions in itertools.combinations(positions, dim):
            edge_position_set = set(edge_positions)
            vertex_positions = [j for j in positions if j not in edge_position_set]
            for edge_ids in itertools.product(range(len(edges)), repeat=dim):
                for vertex_values in itertools.product(vertices, repeat=n - dim):
                    if not anchors.issubset(vertex_values):
                        continue
                    cell = [0] * n
                    for j, eid in zip(edge_positions, edge_ids):
                        cell[j] = nv + eid
                    for j, v in zip(vertex_positions, vertex_values):
                        cell[j] = v
                    cells.append(tuple(cell))
        result.append(cells)
    return result


def boundary_columns(
    cells: list[list[tuple[int, ...]]],
    edges: list[tuple[int, int]],
    nv: int,
) -> list[list[list[tuple[int, int]]]]:
    """Return sparse columns for d_dim: C_dim -> C_(dim-1).

    The outer list has a dummy entry for dimension zero.  A sparse column is
    a list of (row, coefficient) pairs with coefficients in {-1,+1}.
    """
    boundaries: list[list[list[tuple[int, int]]]] = [[]]
    for dim in range(1, len(cells)):
        row_index = {cell: i for i, cell in enumerate(cells[dim - 1])}
        columns: list[list[tuple[int, int]]] = []
        for cell in cells[dim]:
            column: list[tuple[int, int]] = []
            earlier_edges = 0
            for pos, factor in enumerate(cell):
                if factor < nv:
                    continue
                eid = factor - nv
                tail, head = edges[eid]
                koszul = -1 if earlier_edges % 2 else 1
                for endpoint, endpoint_sign in ((tail, -1), (head, 1)):
                    face = list(cell)
                    face[pos] = endpoint
                    column.append((row_index[tuple(face)], koszul * endpoint_sign))
                earlier_edges += 1
            columns.append(column)
        boundaries.append(columns)
    return boundaries


def verify_boundary_squared_zero(
    boundaries: list[list[list[tuple[int, int]]]],
) -> bool:
    for dim in range(2, len(boundaries)):
        lower = boundaries[dim - 1]
        for column in boundaries[dim]:
            image: dict[int, int] = {}
            for middle_row, coefficient in column:
                for low_row, low_coefficient in lower[middle_row]:
                    image[low_row] = image.get(low_row, 0) + coefficient * low_coefficient
            if any(image.values()):
                return False
    return True


def rank_mod_2(columns: list[list[tuple[int, int]]]) -> int:
    basis: dict[int, int] = {}
    for column in columns:
        vector = 0
        for row, coefficient in column:
            if coefficient & 1:
                vector ^= 1 << row
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = vector
                break
            vector ^= basis[pivot]
    return len(basis)


def rank_mod_p(columns: list[list[tuple[int, int]]], p: int) -> int:
    if p == 2:
        return rank_mod_2(columns)
    basis: dict[int, dict[int, int]] = {}
    for column in columns:
        vector: dict[int, int] = {}
        for row, coefficient in column:
            value = (vector.get(row, 0) + coefficient) % p
            if value:
                vector[row] = value
            elif row in vector:
                del vector[row]
        while vector:
            pivot = max(vector)
            if pivot not in basis:
                inverse = pow(vector[pivot], -1, p)
                vector = {row: (value * inverse) % p for row, value in vector.items()}
                basis[pivot] = vector
                break
            factor = vector[pivot]
            pivot_vector = basis[pivot]
            for row, value in pivot_vector.items():
                new_value = (vector.get(row, 0) - factor * value) % p
                if new_value:
                    vector[row] = new_value
                elif row in vector:
                    del vector[row]
    return len(basis)


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.parent[y] = x
        self.size[x] += self.size[y]
        return True


def fundamental_cycle_matrix(
    cells: list[list[tuple[int, ...]]],
    boundaries: list[list[list[tuple[int, int]]]],
) -> tuple[list[list[tuple[int, int]]], int, int]:
    """Coordinate matrix of d2 in an integral basis of ker(d1).

    A spanning forest of the 1-skeleton is selected greedily.  Fundamental
    cycles indexed by nonforest 1-cells form a Z-basis of ker(d1), and the
    coordinate of any cycle on a given basis vector equals its coefficient on
    that vector's unique nonforest edge.  Hence restricting d2 to nonforest
    rows is exactly its matrix in this integral cycle basis.
    """
    if len(cells) < 3:
        return [], 0, len(cells[0])
    uf = UnionFind(len(cells[0]))
    chords: list[int] = []
    for edge_index, column in enumerate(boundaries[1]):
        endpoints = [row for row, coefficient in column if coefficient]
        if len(endpoints) != 2:
            raise AssertionError("a 1-cell did not have two distinct endpoints")
        if not uf.union(endpoints[0], endpoints[1]):
            chords.append(edge_index)
    chord_row = {edge_index: row for row, edge_index in enumerate(chords)}
    matrix_columns: list[list[tuple[int, int]]] = []
    for column in boundaries[2]:
        restricted = [
            (chord_row[edge_index], coefficient)
            for edge_index, coefficient in column
            if edge_index in chord_row
        ]
        matrix_columns.append(restricted)
    component_count = len({uf.find(i) for i in range(len(cells[0]))})
    expected_cycle_rank = len(cells[1]) - len(cells[0]) + component_count
    if expected_cycle_rank != len(chords):
        raise AssertionError("spanning-forest cycle rank mismatch")
    return matrix_columns, len(chords), component_count


def smith_summary(
    columns: list[list[tuple[int, int]]], nrows: int
) -> dict:
    """Compute the exact Smith diagonal of a modest sparse integer matrix."""
    from sympy import Matrix, ZZ
    from sympy.matrices.normalforms import smith_normal_form

    dense = [[0] * len(columns) for _ in range(nrows)]
    for column_index, column in enumerate(columns):
        for row, coefficient in column:
            dense[row][column_index] += coefficient
    smith = smith_normal_form(Matrix(dense), domain=ZZ)
    diagonal = [
        abs(int(smith[i, i]))
        for i in range(min(smith.shape))
        if smith[i, i] != 0
    ]
    return {
        "shape": [nrows, len(columns)],
        "nonzero_diagonal_count": len(diagonal),
        "diagonal_value_counts": {
            str(value): count for value, count in sorted(Counter(diagonal).items())
        },
        "cokernel_free_rank": nrows - len(diagonal),
    }


def analyze(
    graph: nx.Graph,
    anchors: frozenset[int],
    n: int,
    primes: list[int],
    exact_smith: bool = False,
) -> dict:
    vertices = tuple(sorted(graph.nodes()))
    edges = graph_edges(graph)
    cells = anchored_cells(vertices, edges, anchors, n)
    boundaries = boundary_columns(cells, edges, len(vertices))
    if not verify_boundary_squared_zero(boundaries):
        raise AssertionError("boundary squared is nonzero")
    cycle_matrix, cycle_rank, component_count = fundamental_cycle_matrix(cells, boundaries)
    cycle_ranks = {str(p): rank_mod_p(cycle_matrix, p) for p in primes} if len(cells) >= 3 else {}
    generic_cycle_rank = max(cycle_ranks.values(), default=0)

    boundary_ranks: dict[str, list[int]] = {}
    for p in primes:
        boundary_ranks[str(p)] = [0] + [rank_mod_p(boundaries[dim], p) for dim in range(1, len(boundaries))]
    generic_boundary_ranks = [
        max(boundary_ranks[str(p)][dim] for p in primes)
        for dim in range(len(boundaries))
    ]
    generic_betti = []
    field_betti: dict[str, list[int]] = {str(p): [] for p in primes}
    for dim in range(len(cells)):
        next_generic_rank = generic_boundary_ranks[dim + 1] if dim + 1 < len(cells) else 0
        generic_betti.append(len(cells[dim]) - generic_boundary_ranks[dim] - next_generic_rank)
        for p in primes:
            next_rank = boundary_ranks[str(p)][dim + 1] if dim + 1 < len(cells) else 0
            field_betti[str(p)].append(
                len(cells[dim]) - boundary_ranks[str(p)][dim] - next_rank
            )
    # UCT: dim H_i(F_p)-beta_i=t_i(p)+t_(i-1)(p), where t_i(p)
    # counts the p-primary cyclic summands of integral H_i.
    torsion_multiplicities: dict[str, list[int]] = {}
    for p in primes:
        previous = 0
        values = []
        for dim in range(len(cells)):
            current = field_betti[str(p)][dim] - generic_betti[dim] - previous
            values.append(current)
            previous = current
        torsion_multiplicities[str(p)] = values
    torsion_prime_flags = [
        p for p in primes if any(value > 0 for value in torsion_multiplicities[str(p)])
    ]
    result = {
        "vertices": list(vertices),
        "edges": [list(edge) for edge in edges],
        "anchors": sorted(anchors),
        "n": n,
        "cell_counts": [len(group) for group in cells],
        "boundary_squared_zero": True,
        "components": component_count,
        "cycle_lattice_rank": cycle_rank,
        "d2_cycle_coordinate_ranks": cycle_ranks,
        "generic_d2_cycle_rank_observed": generic_cycle_rank,
        "boundary_ranks_by_prime": boundary_ranks,
        "generic_boundary_ranks_observed": generic_boundary_ranks,
        "betti_numbers_observed": generic_betti,
        "field_betti_numbers": field_betti,
        "torsion_multiplicities_by_prime_and_degree": torsion_multiplicities,
        "torsion_prime_flags": torsion_prime_flags,
    }
    if exact_smith and len(cells) >= 3:
        result["exact_d2_cycle_coordinate_smith"] = smith_summary(
            cycle_matrix, cycle_rank
        )
    return result


def named_graph(name: str) -> nx.Graph:
    if name == "k4":
        return nx.complete_graph(4)
    if name == "k5":
        return nx.complete_graph(5)
    if name == "k6":
        return nx.complete_graph(6)
    if name == "k33":
        return nx.complete_bipartite_graph(3, 3)
    if name == "diamond":
        graph = nx.complete_graph(4)
        graph.remove_edge(2, 3)
        return graph
    if name == "paw":
        graph = nx.Graph([(0, 1), (1, 2), (2, 0), (0, 3)])
        graph.add_nodes_from(range(4))
        return graph
    if name == "triangle":
        return nx.cycle_graph(3)
    if name == "path3":
        return nx.path_graph(3)
    raise ValueError(f"unknown graph name: {name}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--graph",
        choices=["k4", "k5", "k6", "k33", "diamond", "paw", "triangle", "path3"],
        required=True,
    )
    parser.add_argument("--anchors", required=True, help="comma-separated vertex labels")
    parser.add_argument("--n", type=int, required=True)
    parser.add_argument("--primes", default="2,3,5,7,101,1000003")
    parser.add_argument("--smith", action="store_true", help="compute exact Smith form of d2 on the cycle lattice")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    anchors = frozenset(int(x) for x in args.anchors.split(",") if x != "")
    primes = [int(x) for x in args.primes.split(",")]
    result = analyze(named_graph(args.graph), anchors, args.n, primes, args.smith)
    result["graph_name"] = args.graph
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered)
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
