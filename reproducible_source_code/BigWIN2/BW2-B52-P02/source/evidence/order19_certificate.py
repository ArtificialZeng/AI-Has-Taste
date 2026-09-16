#!/usr/bin/env python3
"""Direct exact verification of the claimed order-19 host certificate."""

import json


MODULUS = 19
VERTICES = tuple((i, j) for i in range(3) for j in range(4))
CONNECTION_SET = frozenset((1, 4, 15, 18))


def label(vertex):
    i, j = vertex
    return (-i - 4 * j) % MODULUS


def main():
    labels = tuple(label(vertex) for vertex in VERTICES)
    assert len(set(labels)) == 12
    edge_differences = set()
    nonedge_differences = set()
    edge_pairs = nonedge_pairs = 0
    for u, (i, j) in enumerate(VERTICES):
        for v in range(u + 1, len(VERTICES)):
            ip, jp = VERTICES[v]
            grid_edge = abs(i - ip) + abs(j - jp) == 1
            difference = (labels[v] - labels[u]) % MODULUS
            cayley_edge = difference in CONNECTION_SET
            assert grid_edge == cayley_edge
            signed_differences = (difference, (-difference) % MODULUS)
            if grid_edge:
                edge_pairs += 1
                edge_differences.update(signed_differences)
            else:
                nonedge_pairs += 1
                nonedge_differences.update(signed_differences)
    assert edge_pairs == 17 and nonedge_pairs == 49
    assert edge_differences == set(CONNECTION_SET)
    assert edge_differences.isdisjoint(nonedge_differences)
    result = {
        "arithmetic": "exact integer arithmetic modulo 19",
        "group": "Z_19",
        "formula": "f(i,j) = -i - 4j (mod 19)",
        "connection_set": sorted(CONNECTION_SET),
        "grid_vertex_order": [list(vertex) for vertex in VERTICES],
        "labels_in_grid_vertex_order": list(labels),
        "distinct_labels_checked": len(set(labels)),
        "edge_pairs_checked": edge_pairs,
        "nonedge_pairs_checked": nonedge_pairs,
        "all_unordered_pairs_checked": edge_pairs + nonedge_pairs,
        "signed_edge_difference_set": sorted(edge_differences),
        "signed_nonedge_difference_set": sorted(nonedge_differences),
        "difference_sets_disjoint": True,
        "conclusion": "the labeling is an induced embedding in Cay(Z_19,{+-1,+-4})",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
