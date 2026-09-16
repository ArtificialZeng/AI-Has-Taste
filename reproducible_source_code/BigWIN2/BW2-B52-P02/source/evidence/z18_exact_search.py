#!/usr/bin/env python3
"""Exact search of both order-18 Abelian Cayley host types."""

from itertools import combinations, product
import json

from z16_exact_search import (
    GRID_ADJACENCY,
    GRID_CORNER_INDEX,
    GRID_VERTICES,
    TARGET_DEGREES,
    add,
    fixed_corner_isomorphism,
    negate,
)


GROUPS = (("Z_18", (18,)), ("Z_3_x_Z_6", (3, 6)))


def connection_sets(elements, moduli):
    zero = tuple(0 for _ in moduli)
    unseen = set(elements)
    unseen.remove(zero)
    orbits = []
    while unseen:
        x = min(unseen)
        orbit = frozenset((x, negate(x, moduli)))
        orbits.append(orbit)
        unseen.difference_update(orbit)
    answer = []
    for orbit_count in range(1, 6):
        for chosen in combinations(orbits, orbit_count):
            selected = frozenset().union(*chosen)
            if len(selected) in (4, 5):
                answer.append(selected)
    assert len(answer) == len(set(answer)) == 56
    assert sum(len(selected) == 4 for selected in answer) == 28
    assert sum(len(selected) == 5 for selected in answer) == 28
    return tuple(answer)


def verify_witness(labels, selected, moduli):
    zero = tuple(0 for _ in moduli)
    assert labels[GRID_CORNER_INDEX] == zero and len(set(labels)) == 12
    edge_pairs = nonedge_pairs = 0
    for u in range(12):
        for v in range(u + 1, 12):
            difference = add(labels[v], negate(labels[u], moduli), moduli)
            is_cayley_edge = difference in selected
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


def search_group(name, moduli):
    elements = tuple(product(*(range(modulus) for modulus in moduli)))
    assert len(elements) == 18
    zero = tuple(0 for _ in moduli)
    assert elements[0] == zero
    index = {x: k for k, x in enumerate(elements)}
    omitted_sets = tuple(combinations(range(1, 18), 6))
    assert len(omitted_sets) == 12376
    selected_sets = connection_sets(elements, moduli)

    pair_count = omitted_edge_match_count = degree_match_count = corner_match_count = 0
    isomorphism_checks = isomorphism_count = 0
    counts_by_degree = {
        4: {"connection_sets": 0, "pairs": 0, "omitted_edge_matches": 0,
            "degree_matches": 0, "corner_matches": 0, "isomorphisms": 0},
        5: {"connection_sets": 0, "pairs": 0, "omitted_edge_matches": 0,
            "degree_matches": 0, "corner_matches": 0, "isomorphisms": 0},
    }
    first_witness = None

    for selected in selected_sets:
        degree = len(selected)
        required_omitted_edges = 17 - 3 * degree
        assert (degree, required_omitted_edges) in ((4, 5), (5, 2))
        degree_counts = counts_by_degree[degree]
        degree_counts["connection_sets"] += 1
        neighbor_masks = []
        for x in elements:
            mask = 0
            for difference in selected:
                mask |= 1 << index[add(x, difference, moduli)]
            assert mask.bit_count() == degree
            neighbor_masks.append(mask)

        for omitted in omitted_sets:
            pair_count += 1
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

            image_indices = tuple(k for k in range(18) if not omitted_mask & (1 << k))
            assert image_indices[0] == 0 and len(image_indices) == 12
            degrees = tuple(
                degree - (neighbor_masks[k] & omitted_mask).bit_count()
                for k in image_indices
            )
            if tuple(sorted(degrees)) != TARGET_DEGREES:
                continue
            degree_match_count += 1
            degree_counts["degree_matches"] += 1
            if degrees[0] != 2:
                continue
            corner_match_count += 1
            degree_counts["corner_matches"] += 1

            image_position = {host_index: k for k, host_index in enumerate(image_indices)}
            adjacency = []
            for host_index in image_indices:
                row = 0
                neighbors_in_image = neighbor_masks[host_index] & ~omitted_mask
                while neighbors_in_image:
                    low_bit = neighbors_in_image & -neighbors_in_image
                    neighbor_index = low_bit.bit_length() - 1
                    row |= 1 << image_position[neighbor_index]
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
                image = tuple(elements[k] for k in image_indices)
                labels = tuple(image[mapping[k]] for k in range(12))
                first_witness = {
                    "group": name,
                    "moduli": list(moduli),
                    "host_degree": degree,
                    "connection_set": [list(x) for x in sorted(selected)],
                    "omitted_elements": [list(elements[k]) for k in omitted],
                    "grid_vertex_order": [list(vertex) for vertex in GRID_VERTICES],
                    "labels_in_grid_vertex_order": [list(x) for x in labels],
                    "label_by_grid_vertex": {
                        f"{i},{j}": list(labels[k])
                        for k, (i, j) in enumerate(GRID_VERTICES)
                    },
                    "verification": verify_witness(labels, selected, moduli),
                }

    assert pair_count == 56 * 12376
    return {
        "group": name,
        "moduli": list(moduli),
        "symmetric_connection_sets_tested": 56,
        "omitted_six_subsets_tested_per_connection_set": 12376,
        "normalized_candidate_pairs_tested": pair_count,
        "candidates_with_required_omitted_edge_count": omitted_edge_match_count,
        "candidates_with_target_degree_multiset": degree_match_count,
        "candidates_also_with_identity_of_degree_two": corner_match_count,
        "fixed_corner_isomorphism_checks": isomorphism_checks,
        "isomorphic_host_candidates": isomorphism_count,
        "counts_by_host_degree": counts_by_degree,
        "first_witness": first_witness,
    }


def main():
    groups = [search_group(name, moduli) for name, moduli in GROUPS]
    witnesses = [group["first_witness"] for group in groups if group["first_witness"]]
    result = {
        "arithmetic": "exact finite-group and integer enumeration",
        "target": "P_3 square P_4",
        "normalization": "the fixed grid corner (0,0) has label the identity",
        "completeness": (
            "both abelian group types of order 18; all forced inverse-closed "
            "connection sets of size 4 or 5; all omitted six-subsets avoiding identity"
        ),
        "structural_filter": (
            "9d minus (6d minus e_U) equals 17, so 3d+e_U=17; target maximum "
            "degree gives d at least 4, hence only (d,e_U)=(4,5) or (5,2)"
        ),
        "groups": groups,
        "total_normalized_candidate_pairs_tested": sum(
            group["normalized_candidate_pairs_tested"] for group in groups
        ),
        "total_isomorphic_host_candidates": sum(
            group["isomorphic_host_candidates"] for group in groups
        ),
        "first_witness": witnesses[0] if witnesses else None,
        "conclusion": (
            "an induced Abelian Cayley embedding exists at order 18"
            if witnesses else "no induced Abelian Cayley embedding exists at order 18"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
