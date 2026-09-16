#!/usr/bin/env python3
"""Exact census for the diameter-three boundary problem in source.md.

Two enumeration routes are used:

1. NetworkX's Graph Atlas supplies one representative of every unlabeled
   graph of order at most seven.  We record the connected-unlabeled input
   counts and apply the filters requested in source.md.
2. Independently, every one of the 2^(n choose 2) labeled simple graphs is
   scanned for n <= the first failing order.  Every labeled counterexample is
   reduced to the lexicographically least graph6 string over all labelings.

All domination tests are exhaustive subset searches.  This script uses no
floating-point arithmetic and makes no random choices.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

import networkx as nx


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "evidence" / "diameter3_census.json"


def subset_counts(G: nx.Graph, total: bool) -> tuple[list[int], list[list[int]]]:
    """Return counts by cardinality and all minimum witnesses."""
    vertices = tuple(sorted(G.nodes()))
    counts: list[int] = []
    minimum: list[list[int]] = []
    found = False
    for size in range(len(vertices) + 1):
        count = 0
        witnesses: list[list[int]] = []
        for candidate in itertools.combinations(vertices, size):
            chosen = set(candidate)
            tested = vertices if total else (v for v in vertices if v not in chosen)
            if all(any(w in chosen for w in G[v]) for v in tested):
                count += 1
                witnesses.append(list(candidate))
        counts.append(count)
        if count and not found:
            minimum = witnesses
            found = True
    return counts, minimum


def invariant_record(G: nx.Graph) -> dict:
    domination_counts, domination_witnesses = subset_counts(G, total=False)
    total_counts, total_witnesses = subset_counts(G, total=True)
    gamma = next(i for i, count in enumerate(domination_counts) if count)
    gamma_t = next(i for i, count in enumerate(total_counts) if count)
    return {
        "order": len(G),
        "size": G.number_of_edges(),
        "connected": nx.is_connected(G),
        "pendant_vertices": sorted(v for v in G if G.degree(v) == 1),
        "diameter": nx.diameter(G),
        "gamma": gamma,
        "dominating_subset_counts_by_size": domination_counts,
        "minimum_dominating_sets": domination_witnesses,
        "gamma_t": gamma_t,
        "total_dominating_subset_counts_by_size": total_counts,
        "minimum_total_dominating_sets": total_witnesses,
    }


def g6_for_order(G: nx.Graph, order: tuple[int, ...]) -> str:
    """Encode G in graph6 using exactly the supplied vertex order (n <= 62)."""
    n = len(order)
    assert n <= 62
    bits = [int(G.has_edge(order[i], order[j])) for j in range(1, n) for i in range(j)]
    bits.extend([0] * ((-len(bits)) % 6))
    body = "".join(
        chr(63 + sum(bits[start + i] << (5 - i) for i in range(6)))
        for start in range(0, len(bits), 6)
    )
    return chr(n + 63) + body


def canonical_graph6(G: nx.Graph) -> str:
    """Lexicographically least graph6 string among all vertex permutations."""
    vertices = tuple(G.nodes())
    return min(g6_for_order(G, order) for order in itertools.permutations(vertices))


def qualifies_except_total(G: nx.Graph) -> tuple[bool, dict | None]:
    if not nx.is_connected(G):
        return False, None
    if not any(G.degree(v) == 1 for v in G):
        return False, None
    if nx.diameter(G) != 3:
        return False, None
    record = invariant_record(G)
    if record["gamma"] != 2:
        return False, record
    return True, record


def atlas_census() -> tuple[list[dict], int, dict[str, nx.Graph]]:
    atlas = nx.graph_atlas_g()
    rows: list[dict] = []
    first_failing_order = -1
    failures: dict[str, nx.Graph] = {}
    for n in range(1, 8):
        connected = [G for G in atlas if len(G) == n and nx.is_connected(G)]
        pendant = [G for G in connected if any(G.degree(v) == 1 for v in G)]
        diameter_three = [G for G in pendant if nx.diameter(G) == 3]
        gamma_two: list[tuple[nx.Graph, dict]] = []
        for G in diameter_three:
            record = invariant_record(G)
            if record["gamma"] == 2:
                gamma_two.append((G, record))
        distribution = Counter(record["gamma_t"] for _, record in gamma_two)
        bad = [(G, record) for G, record in gamma_two if record["gamma_t"] > 2]
        rows.append(
            {
                "order": n,
                "connected_unlabeled_inputs": len(connected),
                "with_pendant_vertex": len(pendant),
                "also_diameter_3": len(diameter_three),
                "also_gamma_2": len(gamma_two),
                "gamma_t_distribution_after_all_hypotheses": {
                    str(key): distribution[key] for key in sorted(distribution)
                },
                "counterexamples": len(bad),
            }
        )
        if bad:
            first_failing_order = n
            for G, _ in bad:
                failures[canonical_graph6(G)] = G.copy()
            break
    assert first_failing_order != -1
    return rows, first_failing_order, failures


def graph_from_edge_mask(n: int, mask: int) -> nx.Graph:
    G = nx.Graph()
    G.add_nodes_from(range(n))
    possible_edges = list(itertools.combinations(range(n), 2))
    G.add_edges_from(edge for bit, edge in enumerate(possible_edges) if mask & (1 << bit))
    return G


def labeled_audit(first_failing_order: int) -> tuple[list[dict], set[str]]:
    rows: list[dict] = []
    canonical_failures: set[str] = set()
    for n in range(1, first_failing_order + 1):
        masks = 1 << (n * (n - 1) // 2)
        connected_count = 0
        hypothesis_count = 0
        failure_count = 0
        for mask in range(masks):
            G = graph_from_edge_mask(n, mask)
            if not nx.is_connected(G):
                continue
            connected_count += 1
            qualifies, record = qualifies_except_total(G)
            if not qualifies:
                continue
            assert record is not None
            hypothesis_count += 1
            if record["gamma_t"] > 2:
                failure_count += 1
                canonical_failures.add(canonical_graph6(G))
        rows.append(
            {
                "order": n,
                "all_labeled_simple_graphs": masks,
                "connected_labeled_graphs": connected_count,
                "labeled_graphs_meeting_hypotheses": hypothesis_count,
                "labeled_counterexamples": failure_count,
            }
        )
    return rows, canonical_failures


def main() -> None:
    atlas_rows, first_order, atlas_failures = atlas_census()
    labeled_rows, labeled_failures = labeled_audit(first_order)
    assert set(atlas_failures) == labeled_failures

    counterexamples: list[dict] = []
    for graph6 in sorted(labeled_failures):
        # Decoding the canonical string fixes the labels used in the certificate.
        G = nx.from_graph6_bytes(graph6.encode("ascii"))
        record = invariant_record(G)
        record.update(
            {
                "canonical_graph6": graph6,
                "canonicalization": "lexicographically least graph6 over all n! labelings",
                "adjacency": {str(v): sorted(G[v]) for v in sorted(G)},
                "edges": [list(edge) for edge in sorted(G.edges())],
                "hypotheses_verified": bool(
                    record["connected"]
                    and record["pendant_vertices"]
                    and record["diameter"] == 3
                    and record["gamma"] == 2
                ),
                "conclusion_fails": record["gamma_t"] > 2,
            }
        )
        counterexamples.append(record)

    pairwise_nonisomorphic = all(
        not nx.is_isomorphic(
            nx.from_graph6_bytes(a["canonical_graph6"].encode("ascii")),
            nx.from_graph6_bytes(b["canonical_graph6"].encode("ascii")),
        )
        for a, b in itertools.combinations(counterexamples, 2)
    )
    source_sha256 = hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest()
    result = {
        "job_id": "win-00058-p03-research-fa19420fa5ab",
        "method": {
            "arithmetic": "exact Boolean/integer computation",
            "atlas_route": (
                "networkx.graph_atlas_g(), documented as all unlabeled graphs with at most 7 vertices; "
                "one representative is processed per connected isomorphism class"
            ),
            "independent_route": (
                "all 2^(n choose 2) labeled simple graphs scanned for every n through the first failing order"
            ),
            "domination": "all vertex subsets tested directly from the open-neighborhood definitions",
            "canonicalization": "all n! vertex orders tested; retain lexicographically least graph6",
            "networkx_version": nx.__version__,
            "source_md_sha256": source_sha256,
        },
        "atlas_census": atlas_rows,
        "all_labeled_audit": labeled_rows,
        "result": {
            "diameter_three_universal_assertion": False,
            "least_counterexample_order": first_order,
            "counterexample_isomorphism_class_count_at_least_order": len(counterexamples),
            "pairwise_nonisomorphic": pairwise_nonisomorphic,
            "atlas_and_all_labeled_routes_agree": True,
            "canonical_graph6_strings": [item["canonical_graph6"] for item in counterexamples],
        },
        "counterexamples": counterexamples,
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result["result"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
