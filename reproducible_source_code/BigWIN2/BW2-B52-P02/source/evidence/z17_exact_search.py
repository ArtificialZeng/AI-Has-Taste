#!/usr/bin/env python3
"""Exact corner-normalized order-17 search for P_3 square P_4.

This imports only generic exact helpers and target constants from the order-16
enumerator.  In Z/17Z a symmetric connection set has even cardinality.  The
edge equation forces cardinality four and forces the five omitted vertices to
span exactly three host edges.
"""

from itertools import combinations
import json

from z16_exact_search import (
    GRID_ADJACENCY,
    GRID_CORNER_INDEX,
    GRID_VERTICES,
    TARGET_DEGREES,
    fixed_corner_isomorphism,
)


MODULUS = 17


def verify_witness(labels: tuple[int, ...], selected: frozenset[int]) -> dict[str, int]:
    assert labels[GRID_CORNER_INDEX] == 0
    assert len(set(labels)) == 12
    edge_pairs = nonedge_pairs = 0
    for u in range(12):
        for v in range(u + 1, 12):
            is_cayley_edge = (labels[v] - labels[u]) % MODULUS in selected
            is_grid_edge = bool(GRID_ADJACENCY[u] & (1 << v))
            assert is_cayley_edge == is_grid_edge
            if is_grid_edge:
                edge_pairs += 1
            else:
                nonedge_pairs += 1
    assert edge_pairs == 17 and nonedge_pairs == 49
    return {
        "distinct_labels_checked": len(set(labels)),
        "edge_pairs_checked": edge_pairs,
        "nonedge_pairs_checked": nonedge_pairs,
        "all_unordered_pairs_checked": edge_pairs + nonedge_pairs,
    }


def main() -> None:
    elements = tuple(range(MODULUS))
    sign_pairs = tuple(frozenset((x, MODULUS - x)) for x in range(1, 9))
    connection_sets = tuple(
        frozenset().union(*chosen) for chosen in combinations(sign_pairs, 2)
    )
    assert len(connection_sets) == 28 and len(set(connection_sets)) == 28
    omitted_quintuples = tuple(combinations(range(1, MODULUS), 5))
    assert len(omitted_quintuples) == 4368

    pair_count = three_edge_count = degree_match_count = corner_match_count = 0
    isomorphism_checks = isomorphism_count = 0
    first_witness = None

    for selected in connection_sets:
        neighbor_masks = []
        for x in elements:
            mask = 0
            for difference in selected:
                mask |= 1 << ((x + difference) % MODULUS)
            assert mask.bit_count() == 4
            neighbor_masks.append(mask)

        for omitted in omitted_quintuples:
            pair_count += 1
            omitted_mask = sum(1 << k for k in omitted)
            twice_internal_edges = sum(
                (neighbor_masks[k] & omitted_mask).bit_count() for k in omitted
            )
            assert twice_internal_edges % 2 == 0
            if twice_internal_edges != 6:
                continue
            three_edge_count += 1

            image = tuple(k for k in elements if not omitted_mask & (1 << k))
            assert image[0] == 0 and len(image) == 12
            degrees = tuple(
                4 - (neighbor_masks[k] & omitted_mask).bit_count() for k in image
            )
            if tuple(sorted(degrees)) != TARGET_DEGREES:
                continue
            degree_match_count += 1
            if degrees[0] != 2:
                continue
            corner_match_count += 1

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
            if first_witness is None:
                labels = tuple(image[mapping[k]] for k in range(12))
                first_witness = {
                    "group": "Z_17",
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

    assert pair_count == 28 * 4368
    assert isomorphism_count == 0 or first_witness is not None
    result = {
        "arithmetic": "exact integer enumeration",
        "group": "Z_17",
        "normalization": "the fixed grid corner (0,0) has label 0",
        "completeness": (
            "all 28 inverse-closed connection sets of forced size 4 and all "
            "4368 omitted five-subsets avoiding the normalized identity"
        ),
        "structural_filter": (
            "17d/2 minus (5d minus e_U) equals 17; symmetry makes d even and "
            "maximum target degree makes d at least 4, hence d=4 and e_U=3"
        ),
        "symmetric_connection_sets_of_size_four_tested": 28,
        "omitted_quintuples_tested_per_connection_set": 4368,
        "normalized_candidate_pairs_tested": pair_count,
        "candidates_with_exactly_three_omitted_edges": three_edge_count,
        "target_degree_multiset": list(TARGET_DEGREES),
        "candidates_with_target_degree_multiset": degree_match_count,
        "candidates_also_with_zero_of_degree_two": corner_match_count,
        "fixed_corner_isomorphism_checks": isomorphism_checks,
        "isomorphic_host_candidates": isomorphism_count,
        "first_witness": first_witness,
        "conclusion": (
            "an induced Abelian Cayley embedding exists in Z_17"
            if first_witness is not None else
            "no induced Abelian Cayley embedding exists in Z_17"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
