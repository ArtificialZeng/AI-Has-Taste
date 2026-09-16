#!/usr/bin/env python3
"""Exhaustive order-10 witness screen for the M_3(4) problem.

Every connected graph on at least two vertices has a non-cut vertex.  Deleting
one from a connected legal graph on ten vertices leaves a connected legal
graph on nine vertices.  This program reconstructs all exact order-9 classes
using n9_sat_screen.py, restores one nonisolated vertex in every possible
neighborhood of size at most four, and removes duplicates by exact NetworkX
isomorphism tests after invariant bucketing.

For every representative, Glucose4 finds a 9-coloring of Gamma_B(G), or logs
a DRUP proof if none exists.  SAT models are checked edge by edge, and a
separate exact DSATUR backtracker checks every decision.  Exhaustion is only
an exact finite observation at order ten, not a universal theorem.
"""

import hashlib
import itertools
import json
import sys

import networkx as nx

from n9_sat_screen import (
    checked_sat_coloring,
    coloring_clauses,
    conflict_graph,
    dsatur_k_colorable,
    is_legal,
    order_nine_representatives,
)


def invariant_key(graph):
    """Isomorphism invariants used only to bucket exact iso tests."""
    return (
        tuple(sorted(dict(graph.degree()).values())),
        sum(nx.triangles(graph).values()) // 3,
        nx.weisfeiler_lehman_graph_hash(graph, iterations=10),
    )


def extension_is_legal(base, neighborhood):
    """Restore vertex 9 and exactly check the nonautomatic hypotheses."""
    neighborhood = tuple(neighborhood)

    # Any new K_{3,4} has vertex 9 on one side of its bipartition.  If 9 is
    # on the four-vertex side, three members of its neighborhood already have
    # three common old neighbors.  If 9 is on the three-vertex side, two old
    # vertices have all four members of N(9) as common neighbors.  These two
    # tests are exactly the affected cases of the common-neighbor criterion.
    if len(neighborhood) >= 3:
        for triple in itertools.combinations(neighborhood, 3):
            common = set(base.neighbors(triple[0]))
            common &= set(base.neighbors(triple[1]))
            common &= set(base.neighbors(triple[2]))
            if len(common) >= 3:
                return None
    if len(neighborhood) == 4:
        target = set(neighborhood)
        for first, second in itertools.combinations(base.nodes(), 2):
            if target <= set(base.neighbors(first)) and target <= set(
                base.neighbors(second)
            ):
                return None

    graph = base.copy()
    graph.add_node(9)
    graph.add_edges_from((9, vertex) for vertex in neighborhood)
    # When deg(9)<=3, deleting 9 first extends a 3-degeneracy ordering of the
    # base.  Only degree four can create a 4-core.
    if len(neighborhood) == 4 and max(nx.core_number(graph).values()) > 3:
        return None
    return graph


def order_ten_representatives():
    """Generate one exact-isomorphism representative per legal class."""
    bases, n9_raw, n9_iso, n9_provenance = order_nine_representatives()
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
        if (base_index + 1) % 250 == 0:
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
        "connected_legal_order_9_bases": len(bases),
        "order_9_raw_legal_extensions": n9_raw,
        "order_9_exact_iso_comparisons": n9_iso,
        **n9_provenance,
    }
    return representatives, raw_legal_extensions, exact_iso_comparisons, provenance


def main():
    representatives, raw_count, iso_comparisons, provenance = (
        order_ten_representatives()
    )
    witnesses = []
    edge_histogram = {}
    clique_histogram = {}
    encoded_representatives = []
    coloring_records = []
    for index, graph in enumerate(representatives):
        assert len(graph) == 10 and is_legal(graph)
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
                graph6
                + ":"
                + ",".join(
                    str(sat_coloring[vertex]) for vertex in sorted(conflict)
                )
            )
        if (index + 1) % 5000 == 0:
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
            "all connected legal order-9 representatives reconstructed "
            "exactly, extended by one nonisolated vertex of degree 1..4"
        ),
        **provenance,
        "raw_legal_order_10_extensions": raw_count,
        "exact_order_10_iso_comparisons": iso_comparisons,
        "connected_legal_order_10_isomorphism_classes": len(representatives),
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
            "ten vertices; not a universal upper-bound proof"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
