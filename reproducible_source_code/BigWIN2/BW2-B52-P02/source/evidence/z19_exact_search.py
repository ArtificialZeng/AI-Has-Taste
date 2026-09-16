#!/usr/bin/env python3
"""Exact corner-normalized search of the unique order-19 Abelian group."""

from itertools import combinations
import json

from z16_exact_search import (
    GRID_ADJACENCY,
    GRID_CORNER_INDEX,
    GRID_VERTICES,
    TARGET_DEGREES,
    fixed_corner_isomorphism,
)


MODULUS = 19


def verify_witness(labels, selected):
    assert labels[GRID_CORNER_INDEX] == 0 and len(set(labels)) == 12
    edge_pairs = nonedge_pairs = 0
    for u in range(12):
        for v in range(u + 1, 12):
            is_cayley_edge = (labels[v] - labels[u]) % MODULUS in selected
            is_grid_edge = bool(GRID_ADJACENCY[u] & (1 << v))
            assert is_cayley_edge == is_grid_edge
            edge_pairs += is_grid_edge
            nonedge_pairs += not is_grid_edge
    assert edge_pairs == 17 and nonedge_pairs == 49
    return {
        "distinct_labels_checked": len(set(labels)),
        "edge_pairs_checked": edge_pairs,
        "nonedge_pairs_checked": nonedge_pairs,
        "all_unordered_pairs_checked": edge_pairs + nonedge_pairs,
    }


def main():
    sign_pairs = tuple(frozenset((x, MODULUS - x)) for x in range(1, 10))
    connection_sets = []
    for pair_count in (2, 3):
        connection_sets.extend(
            frozenset().union(*chosen) for chosen in combinations(sign_pairs, pair_count)
        )
    assert len(connection_sets) == 36 + 84 == 120
    omitted_sets = tuple(combinations(range(1, MODULUS), 7))
    assert len(omitted_sets) == 31824

    candidate_count = omitted_edge_match_count = degree_match_count = 0
    corner_match_count = isomorphism_checks = isomorphism_count = 0
    counts_by_degree = {
        4: {"connection_sets": 0, "pairs": 0, "omitted_edge_matches": 0,
            "degree_matches": 0, "corner_matches": 0, "isomorphisms": 0},
        6: {"connection_sets": 0, "pairs": 0, "omitted_edge_matches": 0,
            "degree_matches": 0, "corner_matches": 0, "isomorphisms": 0},
    }
    first_witness = None

    for selected in connection_sets:
        degree = len(selected)
        required_omitted_edges = 17 - 5 * degree // 2
        assert (degree, required_omitted_edges) in ((4, 7), (6, 2))
        degree_counts = counts_by_degree[degree]
        degree_counts["connection_sets"] += 1
        neighbor_masks = []
        for x in range(MODULUS):
            mask = 0
            for difference in selected:
                mask |= 1 << ((x + difference) % MODULUS)
            assert mask.bit_count() == degree
            neighbor_masks.append(mask)

        for omitted in omitted_sets:
            candidate_count += 1
            degree_counts["pairs"] += 1
            omitted_mask = sum(1 << k for k in omitted)
            twice_internal_edges = sum(
                (neighbor_masks[k] & omitted_mask).bit_count() for k in omitted
            )
            assert twice_internal_edges % 2 == 0
            if twice_internal_edges != 2 * required_omitted_edges:
                continue
            omitted_edge_match_count += 1
            degree_counts["omitted_edge_matches"] += 1

            image = tuple(k for k in range(MODULUS) if not omitted_mask & (1 << k))
            assert image[0] == 0 and len(image) == 12
            degrees = tuple(
                degree - (neighbor_masks[k] & omitted_mask).bit_count() for k in image
            )
            if tuple(sorted(degrees)) != TARGET_DEGREES:
                continue
            degree_match_count += 1
            degree_counts["degree_matches"] += 1
            if degrees[0] != 2:
                continue
            corner_match_count += 1
            degree_counts["corner_matches"] += 1

            image_position = {host_vertex: k for k, host_vertex in enumerate(image)}
            adjacency = []
            for host_vertex in image:
                row = 0
                neighbors_in_image = neighbor_masks[host_vertex] & ~omitted_mask
                while neighbors_in_image:
                    low_bit = neighbors_in_image & -neighbors_in_image
                    neighbor = low_bit.bit_length() - 1
                    row |= 1 << image_position[neighbor]
                    neighbors_in_image -= low_bit
                adjacency.append(row)
            adjacency_tuple = tuple(adjacency)
            assert tuple(row.bit_count() for row in adjacency_tuple) == degrees

            isomorphism_checks += 1
            mapping = fixed_corner_isomorphism(adjacency_tuple, degrees)
            if mapping is None:
                continue
            isomorphism_count += 1
            degree_counts["isomorphisms"] += 1
            if first_witness is None:
                labels = tuple(image[mapping[k]] for k in range(12))
                first_witness = {
                    "group": "Z_19",
                    "host_degree": degree,
                    "connection_set": sorted(selected),
                    "omitted_residues": list(omitted),
                    "grid_vertex_order": [list(vertex) for vertex in GRID_VERTICES],
                    "labels_in_grid_vertex_order": list(labels),
                    "label_by_grid_vertex": {
                        f"{i},{j}": labels[k]
                        for k, (i, j) in enumerate(GRID_VERTICES)
                    },
                    "verification": verify_witness(labels, selected),
                }

    assert candidate_count == 120 * 31824
    result = {
        "arithmetic": "exact integer enumeration",
        "group": "Z_19",
        "normalization": "the fixed grid corner (0,0) has label 0",
        "completeness": (
            "all inverse-closed connection sets of forced size 4 or 6 and all "
            "omitted seven-subsets avoiding the normalized identity"
        ),
        "structural_filter": (
            "19d/2 minus (7d minus e_U) equals 17, so 5d/2+e_U=17; "
            "d is even and at least 4, hence only (d,e_U)=(4,7) or (6,2)"
        ),
        "symmetric_connection_sets_tested": len(connection_sets),
        "omitted_seven_subsets_tested_per_connection_set": 31824,
        "normalized_candidate_pairs_tested": candidate_count,
        "candidates_with_required_omitted_edge_count": omitted_edge_match_count,
        "target_degree_multiset": list(TARGET_DEGREES),
        "candidates_with_target_degree_multiset": degree_match_count,
        "candidates_also_with_zero_of_degree_two": corner_match_count,
        "fixed_corner_isomorphism_checks": isomorphism_checks,
        "isomorphic_host_candidates": isomorphism_count,
        "counts_by_host_degree": counts_by_degree,
        "first_witness": first_witness,
        "conclusion": (
            "an induced Abelian Cayley embedding exists in Z_19"
            if first_witness is not None else
            "no induced Abelian Cayley embedding exists in Z_19"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
