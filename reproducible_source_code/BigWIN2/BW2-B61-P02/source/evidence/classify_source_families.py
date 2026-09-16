#!/usr/bin/env python3
"""Classify census representatives by Hall-universal families in the source.

Predicates are deliberately literal and finite.  The Proposition 4.9 predicate
tries every assignment of vertices to its totally-Hall-universal core, star
centers, and leaves.  The disjoint-union closure in Remark 4.12 is also applied.
"""

import csv
import itertools
import sys

import networkx as nx


def pairs(n):
    return [(u, v) for v in range(1, n) for u in range(v)]


def graph_from_mask(n, mask):
    g = nx.Graph()
    g.add_nodes_from(range(n))
    g.add_edges_from(edge for k, edge in enumerate(pairs(n)) if (mask >> k) & 1)
    return g


def has_spanning_12_factor(g):
    """Theorem 4.6: a vertex permutation using only edges of g."""
    vertices = tuple(g.nodes())
    if not vertices:
        return True
    return any(all(g.has_edge(v, image) for v, image in zip(vertices, perm))
               for perm in itertools.permutations(vertices))


def is_complete_multipartite_covered(g):
    """Theorem 4.16, including its exact numerical condition."""
    n = len(g)
    if n < 2:
        return False
    complement = nx.complement(g)
    parts = list(nx.connected_components(complement))
    # Each complement component must be a clique; there must be at least two
    # nonempty multipartition parts, exactly as in Theorem 4.16.
    if len(parts) < 2:
        return False
    for part in parts:
        if complement.subgraph(part).number_of_edges() != len(part) * (len(part) - 1) // 2:
            return False
    maximum = max(map(len, parts))
    return n - maximum <= 2 or 2 * maximum - n <= 2


def is_grid(g):
    n = len(g)
    for m in range(1, n + 1):
        if n % m:
            continue
        k = n // m
        candidate = nx.cartesian_product(nx.path_graph(m), nx.path_graph(k))
        if nx.is_isomorphic(g, candidate):
            return True
    return n == 0  # P_0 convention is not needed for coverage (it is a forest).


def proposition_49(g):
    """Exact recognition by exhaustive core/center/leaf role assignment."""
    vertices = tuple(g.nodes())
    n = len(vertices)
    # Role 0=core, 1=center, 2=leaf.  At least one star is required here; the
    # k=0 case is already Theorem 4.6.
    for roles in itertools.product(range(3), repeat=n):
        role = dict(zip(vertices, roles))
        core = [v for v in vertices if role[v] == 0]
        centers = [v for v in vertices if role[v] == 1]
        leaves = [v for v in vertices if role[v] == 2]
        if not centers or not leaves:
            continue
        if not has_spanning_12_factor(g.subgraph(core).copy()):
            continue
        used = {c: 0 for c in centers}
        good = True
        for leaf in leaves:
            neighbors = list(g.neighbors(leaf))
            if len(neighbors) != 1 or neighbors[0] not in used:
                good = False
                break
            used[neighbors[0]] += 1
        if good and all(used.values()):
            return True
    return False


def direct_reasons(g):
    reasons = []
    if any(g.degree(v) == 0 for v in g):
        reasons.append("isolated_vertex:Prop2.10")
    if len(g) == 0 or nx.is_forest(g):
        reasons.append("forest:Thm4.11")
    if has_spanning_12_factor(g):
        reasons.append("spanning_12_factor:Thm4.6")
    if proposition_49(g):
        reasons.append("star_attachment:Prop4.9")
    if is_complete_multipartite_covered(g):
        reasons.append("complete_multipartite:Thm4.16")
    if is_grid(g):
        reasons.append("grid:Thm4.19")
    return reasons


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: classify_source_families.py census.tsv output.tsv")
    with open(sys.argv[1], newline="", encoding="ascii") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    output_rows = []
    for row in rows:
        n = int(row["n"])
        g = graph_from_mask(n, int(row["g_edge_mask"]))
        reasons = direct_reasons(g)
        component_reasons = []
        if n and not reasons:
            all_components_covered = True
            for vertices in nx.connected_components(g):
                cr = direct_reasons(g.subgraph(vertices).copy())
                if not cr:
                    all_components_covered = False
                    break
                component_reasons.append(cr[0])
            if all_components_covered and len(component_reasons) > 1:
                reasons.append("disjoint_union:Remark4.12[" + ",".join(component_reasons) + "]")
        if int(row["bad_count"]) != 0:
            status = "negative"
        elif reasons:
            status = "positive_source_covered"
        else:
            status = "positive_new_finite_census"
        output_rows.append((n, row["graph6"], row["g_edge_mask"], status, ";".join(reasons)))
    with open(sys.argv[2], "w", newline="", encoding="ascii") as stream:
        writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
        writer.writerow(["n", "graph6", "g_edge_mask", "status", "source_reasons"])
        writer.writerows(output_rows)
    uncovered = [r for r in output_rows if r[3] == "positive_new_finite_census"]
    print(f"classes={len(output_rows)} source_covered={len(output_rows)-len(uncovered)} uncovered={len(uncovered)}")
    print("first_uncovered=" + (f"n={uncovered[0][0]},graph6={uncovered[0][1]},mask={uncovered[0][2]}" if uncovered else "none"))


if __name__ == "__main__":
    main()
