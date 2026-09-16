#!/usr/bin/env python3
"""Exhaustive order-9 witness screen for the M_3(4) problem.

Every connected graph on at least two vertices has a non-cut vertex.  Deleting
one from a connected legal graph on nine vertices leaves a connected legal
graph on eight vertices.  This program first reconstructs one representative
of every such order-8 class by the exact procedure in n8_sat_screen.py, then
restores a new nonisolated vertex in every possible neighborhood of size at
most four.  Exact NetworkX isomorphism tests, after invariant bucketing, remove
duplicate order-9 extensions.

For each representative G, a PySAT instance asks whether Gamma_B(G) has a
proper 9-coloring.  Every SAT model is checked directly, and an independent
exact DSATUR backtracker checks the same decision.  If an UNSAT instance is
ever found, the JSON output includes the coloring CNF and Glucose4 DRUP proof,
in addition to the graph itself, so that the proposed witness is checkable.
Absence of a witness is only an exact finite observation at order nine.
"""

import hashlib
import itertools
import json
import sys

import networkx as nx
from pysat.solvers import Solver

from n8_sat_screen import order_eight_representatives


def is_legal(graph):
    """Check all graph-class hypotheses exactly."""
    if len(graph) == 0 or not nx.is_connected(graph):
        return False
    if max(dict(graph.degree()).values(), default=0) > 4:
        return False
    if max(nx.core_number(graph).values(), default=0) > 3:
        return False
    # There is a K_{3,4} subgraph iff some triple has four common neighbors.
    for triple in itertools.combinations(graph.nodes(), 3):
        common = set(graph.neighbors(triple[0]))
        common &= set(graph.neighbors(triple[1]))
        common &= set(graph.neighbors(triple[2]))
        if len(common) >= 4:
            return False
    return True


def conflict_graph(graph):
    """Construct Gamma_B(G), indexing its vertices by sorted edges of G."""
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


def coloring_clauses(graph, k):
    """Standard exactly-one-color CNF for a proper k-coloring."""
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
    return clauses


def checked_sat_coloring(graph, k):
    """Return (verified coloring, None), or (None, DRUP proof) if UNSAT."""
    clauses = coloring_clauses(graph, k)

    def variable(vertex, color):
        return vertex * k + color + 1

    with Solver(name="g4", bootstrap_with=clauses) as solver:
        if solver.solve():
            positive = {
                literal for literal in solver.get_model() if literal > 0
            }
        else:
            positive = None

    if positive is None:
        # Rerun only a rare UNSAT case with proof logging enabled.
        with Solver(name="g4", bootstrap_with=clauses, with_proof=True) as solver:
            assert not solver.solve()
            proof = solver.get_proof()
        assert proof
        return None, proof

    coloring = {}
    for vertex in graph:
        assigned = [
            color for color in range(k) if variable(vertex, color) in positive
        ]
        assert len(assigned) == 1
        coloring[vertex] = assigned[0]
    assert all(coloring[u] != coloring[v] for u, v in graph.edges())
    return coloring, None


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
    """Isomorphism invariants used only to bucket exact iso tests."""
    return (
        tuple(sorted(dict(graph.degree()).values())),
        sum(nx.triangles(graph).values()) // 3,
        nx.weisfeiler_lehman_graph_hash(graph, iterations=9),
    )


def extension_is_legal(base, neighborhood):
    """Restore vertex 8 and exactly verify the nonautomatic hypotheses."""
    graph = base.copy()
    graph.add_node(8)
    graph.add_edges_from((8, vertex) for vertex in neighborhood)
    # Max degree and connectivity are automatic from the caller.  If the new
    # vertex has degree <=3, deleting it first extends a 3-degeneracy ordering
    # of the legal base.  Degree four needs an explicit core-number check.
    if len(neighborhood) == 4 and max(nx.core_number(graph).values()) > 3:
        return None
    # The base has no K_{3,4}; nevertheless, a new one involving vertex 8 can
    # appear.  The common-neighbor characterization checks all possibilities.
    for triple in itertools.combinations(graph.nodes(), 3):
        common = set(graph.neighbors(triple[0]))
        common &= set(graph.neighbors(triple[1]))
        common &= set(graph.neighbors(triple[2]))
        if len(common) >= 4:
            return None
    return graph


def order_nine_representatives():
    """Generate one exact-isomorphism representative per legal class."""
    bases, n8_raw, n8_iso = order_eight_representatives()
    buckets = {}
    raw_legal_extensions = 0
    exact_iso_comparisons = 0
    for base_index, base in enumerate(bases):
        available = [vertex for vertex in base if base.degree(vertex) < 4]
        for size in range(1, min(4, len(available)) + 1):
            for neighborhood in itertools.combinations(available, size):
                graph = extension_is_legal(base, neighborhood)
                if graph is None:
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
        if (base_index + 1) % 100 == 0:
            class_count = sum(len(bucket) for bucket in buckets.values())
            print(
                f"generation {base_index + 1}/{len(bases)} bases; "
                f"raw={raw_legal_extensions}; classes={class_count}",
                file=sys.stderr,
                flush=True,
            )
    representatives = [
        graph for key in sorted(buckets, key=repr) for graph in buckets[key]
    ]
    provenance = {
        "connected_legal_order_8_bases": len(bases),
        "order_8_raw_legal_extensions": n8_raw,
        "order_8_exact_iso_comparisons": n8_iso,
    }
    return representatives, raw_legal_extensions, exact_iso_comparisons, provenance


def main():
    representatives, raw_count, iso_comparisons, provenance = (
        order_nine_representatives()
    )
    witnesses = []
    edge_histogram = {}
    clique_histogram = {}
    encoded_representatives = []
    coloring_records = []
    for index, graph in enumerate(representatives):
        assert len(graph) == 9 and is_legal(graph)
        conflict, edges = conflict_graph(graph)
        sat_coloring, drup_proof = checked_sat_coloring(conflict, 9)
        dsatur_answer = dsatur_k_colorable(conflict, 9)
        assert (sat_coloring is not None) == dsatur_answer
        edge_histogram[len(edges)] = edge_histogram.get(len(edges), 0) + 1
        clique = max((len(item) for item in nx.find_cliques(conflict)), default=0)
        clique_histogram[clique] = clique_histogram.get(clique, 0) + 1
        graph6 = nx.to_graph6_bytes(graph, header=False).decode().strip()
        encoded_representatives.append(graph6)
        if sat_coloring is None:
            clauses = coloring_clauses(conflict, 9)
            witnesses.append(
                {
                    "representative_index": index,
                    "graph6": graph6,
                    "edges": edges,
                    "conflict_edges": sorted(conflict.edges()),
                    "coloring_cnf_num_variables": 9 * len(conflict),
                    "coloring_cnf_clauses": clauses,
                    "glucose4_drup_proof": drup_proof,
                }
            )
        else:
            coloring_records.append(
                graph6 + ":" + ",".join(
                    str(sat_coloring[vertex]) for vertex in sorted(conflict)
                )
            )
        if (index + 1) % 1000 == 0:
            print(
                f"coloring {index + 1}/{len(representatives)} classes; "
                f"witnesses={len(witnesses)}",
                file=sys.stderr,
                flush=True,
            )

    encoding = "\n".join(sorted(encoded_representatives)).encode("ascii")
    coloring_encoding = "\n".join(sorted(coloring_records)).encode("ascii")
    result = {
        "networkx_version": nx.__version__,
        "generation_basis": (
            "all connected legal order-8 representatives reconstructed "
            "exactly, extended by one nonisolated vertex of degree 1..4"
        ),
        **provenance,
        "raw_legal_order_9_extensions": raw_count,
        "exact_order_9_iso_comparisons": iso_comparisons,
        "connected_legal_order_9_isomorphism_classes": len(representatives),
        "edge_count_histogram": sorted(edge_histogram.items()),
        "conflict_clique_number_histogram": sorted(clique_histogram.items()),
        "representative_graph6_multiset_sha256": hashlib.sha256(encoding).hexdigest(),
        "verified_sat_coloring_records_sha256": hashlib.sha256(
            coloring_encoding
        ).hexdigest(),
        "pysat_solver": "Glucose4 (g4)",
        "independent_decision": "exact DSATUR backtracking",
        "non_9_colorable_witness_count": len(witnesses),
        "witnesses": witnesses,
        "scope": (
            "exact finite observation for connected legal graphs on exactly "
            "nine vertices; not a universal upper-bound proof"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
