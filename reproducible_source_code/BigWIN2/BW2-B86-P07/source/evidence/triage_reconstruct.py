#!/usr/bin/env python3
"""Exact intake checks for the five-vertex subdivided claw instance."""

from itertools import combinations, permutations
from math import comb


LOCAL_VERTICES = tuple(range(5))
LOCAL_PAIRS = tuple(combinations(LOCAL_VERTICES, 2))
PAIR_INDEX = {pair: index for index, pair in enumerate(LOCAL_PAIRS)}
TSTAR_EDGES = ((0, 1), (0, 2), (0, 3), (3, 4))


def edge_mask(edges):
    mask = 0
    for u, v in edges:
        pair = (u, v) if u < v else (v, u)
        mask |= 1 << PAIR_INDEX[pair]
    return mask


def permuted_tstar_masks():
    masks = set()
    for permutation in permutations(LOCAL_VERTICES):
        masks.add(edge_mask((permutation[u], permutation[v]) for u, v in TSTAR_EDGES))
    return masks


def comparable_masks(copies):
    comparable = set()
    for pattern in range(1 << len(LOCAL_PAIRS)):
        if any((pattern & copy) == pattern or (pattern & copy) == copy for copy in copies):
            comparable.add(pattern)
    return comparable


def induced_local_mask(vertices, global_edges):
    mask = 0
    for index, (i, j) in enumerate(LOCAL_PAIRS):
        edge = tuple(sorted((vertices[i], vertices[j])))
        if edge in global_edges:
            mask |= 1 << index
    return mask


def check_two_k4(copies, comparable):
    global_edges = {
        edge
        for component in (range(4), range(4, 8))
        for edge in combinations(component, 2)
    }
    masks = {
        induced_local_mask(vertices, global_edges)
        for vertices in combinations(range(8), 5)
    }
    legal = all(mask in copies or mask not in comparable for mask in masks)
    return legal, len(tuple(combinations(range(8), 5))), sorted({mask.bit_count() for mask in masks})


def main():
    copies = permuted_tstar_masks()
    comparable = comparable_masks(copies)
    forbidden = comparable - copies
    lower_ok, five_sets, induced_edge_counts = check_two_k4(copies, comparable)

    assert len(copies) == 60
    assert len(forbidden) == 757
    assert lower_ok
    assert induced_edge_counts == [4, 6]

    print("method=exhaustive integer bitmask enumeration")
    print("five_vertex_edge_patterns=1024")
    print(f"labeled_tstar_copies={len(copies)}")
    print(f"comparable_patterns_including_tstar={len(comparable)}")
    print(f"forbidden_comparable_nonisomorphic_patterns={len(forbidden)}")
    print(f"nine_vertex_five_sets={comb(9, 5)}")
    print(f"full_encoding_clauses={comb(9, 5) * len(forbidden)}")
    print(f"two_k4_five_sets_checked={five_sets}")
    print(f"two_k4_distinct_induced_edge_counts={induced_edge_counts}")
    print(f"two_k4_is_tstar_exact={str(lower_ok).lower()}")


if __name__ == "__main__":
    main()
