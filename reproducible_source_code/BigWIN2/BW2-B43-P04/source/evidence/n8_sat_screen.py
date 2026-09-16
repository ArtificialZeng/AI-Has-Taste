#!/usr/bin/env python3
"""Exhaustive order-8 witness screen for the M_3(4) problem.

Every connected graph on eight vertices has a non-cut vertex.  Deleting such
a vertex leaves a connected seven-vertex graph, represented in NetworkX's
Graph Atlas.  We therefore extend every connected legal Atlas graph of order
seven by one vertex in every possible nonempty way compatible with degree at
most four.  Exact isomorphism tests remove duplicate extensions.

For each resulting legal graph G, a PySAT instance asks whether its B-conflict
graph has a proper 9-coloring.  Every returned model is checked directly.  An
independent exact DSATUR backtracker also checks the same decision.  Hence a
reported failure would be a candidate value-10 witness, but absence of a
failure is only a finite order-8 observation.
"""

import hashlib
import itertools
import json

import networkx as nx
from pysat.solvers import Solver


def is_legal(graph):
    """Check all graph-class hypotheses exactly."""
    if len(graph) == 0 or not nx.is_connected(graph):
        return False
    if max(dict(graph.degree()).values(), default=0) > 4:
        return False
    if max(nx.core_number(graph).values(), default=0) > 3:
        return False
    # A (not necessarily induced) K_{3,4} exists exactly when some triple has
    # at least four common neighbours.
    for triple in itertools.combinations(graph.nodes(), 3):
        common = set(graph.neighbors(triple[0]))
        common &= set(graph.neighbors(triple[1]))
        common &= set(graph.neighbors(triple[2]))
        if len(common) >= 4:
            return False
    return True


def conflict_graph(graph):
    """Construct Gamma_B(G), with its vertices indexed by sorted edges of G."""
    edges = sorted(tuple(sorted(edge)) for edge in graph.edges())
    conflict = nx.Graph()
    conflict.add_nodes_from(range(len(edges)))
    for i, (u, v) in enumerate(edges):
        for j in range(i + 1, len(edges)):
            x, y = edges[j]
            incident = len({u, v, x, y}) < 4
            opposite = (
                graph.has_edge(u, x) and graph.has_edge(v, y)
            ) or (
                graph.has_edge(u, y) and graph.has_edge(v, x)
            )
            if incident or opposite:
                conflict.add_edge(i, j)
    return conflict, edges


def checked_sat_coloring(graph, k):
    """Return a verified k-coloring, or None if the CNF is unsatisfiable."""
    vertices = list(graph.nodes())

    def variable(vertex, color):
        return vertex * k + color + 1

    clauses = []
    for vertex in vertices:
        clauses.append([variable(vertex, color) for color in range(k)])
        for first, second in itertools.combinations(range(k), 2):
            clauses.append(
                [-variable(vertex, first), -variable(vertex, second)]
            )
    for u, v in graph.edges():
        for color in range(k):
            clauses.append([-variable(u, color), -variable(v, color)])

    with Solver(name="g4", bootstrap_with=clauses) as solver:
        if not solver.solve():
            return None
        positive = set(literal for literal in solver.get_model() if literal > 0)

    coloring = {}
    for vertex in vertices:
        assigned = [
            color
            for color in range(k)
            if variable(vertex, color) in positive
        ]
        assert len(assigned) == 1
        coloring[vertex] = assigned[0]
    assert all(coloring[u] != coloring[v] for u, v in graph.edges())
    return coloring


def dsatur_k_colorable(graph, k):
    """Independent exact k-colorability decision by backtracking."""
    colors = {vertex: -1 for vertex in graph}
    saturation = {vertex: 0 for vertex in graph}
    degrees = dict(graph.degree())

    def search(colored):
        if colored == len(graph):
            return True
        uncolored = [vertex for vertex in graph if colors[vertex] < 0]
        vertex = max(
            uncolored,
            key=lambda item: (saturation[item].bit_count(), degrees[item]),
        )
        forbidden = saturation[vertex]
        for color in range(k):
            bit = 1 << color
            if forbidden & bit:
                continue
            colors[vertex] = color
            changed = []
            for neighbor in graph[vertex]:
                if colors[neighbor] < 0 and not saturation[neighbor] & bit:
                    changed.append((neighbor, saturation[neighbor]))
                    saturation[neighbor] |= bit
            if search(colored + 1):
                return True
            for neighbor, old_value in changed:
                saturation[neighbor] = old_value
            colors[vertex] = -1
        return False

    return search(0)


def invariant_key(graph):
    """Cheap invariant used only to bucket subsequent exact iso tests."""
    return (
        tuple(sorted(dict(graph.degree()).values())),
        sum(nx.triangles(graph).values()) // 3,
        nx.weisfeiler_lehman_graph_hash(graph, iterations=8),
    )


def legal_order_seven_bases():
    return [
        nx.convert_node_labels_to_integers(graph, ordering="sorted")
        for graph in nx.graph_atlas_g()
        if len(graph) == 7 and is_legal(graph)
    ]


def order_eight_representatives():
    """Generate one exact-isomorphism representative per legal class."""
    buckets = {}
    raw_legal_extensions = 0
    exact_iso_comparisons = 0
    for base in legal_order_seven_bases():
        available = [vertex for vertex in base if base.degree(vertex) < 4]
        for size in range(1, min(4, len(available)) + 1):
            for neighborhood in itertools.combinations(available, size):
                graph = base.copy()
                graph.add_node(7)
                graph.add_edges_from((7, vertex) for vertex in neighborhood)
                if not is_legal(graph):
                    continue
                raw_legal_extensions += 1
                key = invariant_key(graph)
                bucket = buckets.setdefault(key, [])
                duplicate = False
                for representative in bucket:
                    exact_iso_comparisons += 1
                    if nx.is_isomorphic(graph, representative):
                        duplicate = True
                        break
                if not duplicate:
                    bucket.append(graph)
    representatives = [
        graph for key in sorted(buckets, key=repr) for graph in buckets[key]
    ]
    return representatives, raw_legal_extensions, exact_iso_comparisons


def main():
    representatives, raw_count, iso_comparisons = order_eight_representatives()
    witnesses = []
    edge_histogram = {}
    clique_histogram = {}
    encoded_representatives = []
    for index, graph in enumerate(representatives):
        assert len(graph) == 8 and is_legal(graph)
        conflict, edges = conflict_graph(graph)
        sat_coloring = checked_sat_coloring(conflict, 9)
        dsatur_answer = dsatur_k_colorable(conflict, 9)
        assert (sat_coloring is not None) == dsatur_answer
        edge_histogram[len(edges)] = edge_histogram.get(len(edges), 0) + 1
        clique = max((len(item) for item in nx.find_cliques(conflict)), default=0)
        clique_histogram[clique] = clique_histogram.get(clique, 0) + 1
        graph6 = nx.to_graph6_bytes(graph, header=False).decode().strip()
        encoded_representatives.append(graph6)
        if sat_coloring is None:
            witnesses.append(
                {
                    "representative_index": index,
                    "graph6": graph6,
                    "edges": edges,
                    "conflict_edges": sorted(conflict.edges()),
                }
            )

    encoding = "\n".join(sorted(encoded_representatives)).encode("ascii")
    result = {
        "networkx_version": nx.__version__,
        "generation_basis": (
            "all connected legal order-7 Graph Atlas representatives, "
            "extended by one nonisolated vertex of degree 1..4"
        ),
        "legal_order_7_bases": len(legal_order_seven_bases()),
        "raw_legal_extensions": raw_count,
        "exact_iso_comparisons": iso_comparisons,
        "connected_legal_order_8_isomorphism_classes": len(representatives),
        "edge_count_histogram": sorted(edge_histogram.items()),
        "conflict_clique_number_histogram": sorted(clique_histogram.items()),
        "representative_graph6_multiset_sha256": hashlib.sha256(encoding).hexdigest(),
        "pysat_solver": "Glucose4 (g4)",
        "independent_decision": "exact DSATUR backtracking",
        "non_9_colorable_witness_count": len(witnesses),
        "witnesses": witnesses,
        "scope": (
            "exact finite observation for connected legal graphs on exactly "
            "eight vertices; not a universal upper-bound proof"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
