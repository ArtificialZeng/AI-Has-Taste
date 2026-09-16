#!/usr/bin/env python3
"""Exact order-16 Cayley-host search for P_3 square P_4.

All five abelian group types are represented by invariant-factor tuples.
Translation fixes the grid corner (0,0) at the group identity.  Therefore the
four omitted elements form a subset of the 15 nonidentity elements.  The edge
count proves that only symmetric connection sets of size four and omitted
quadruples spanning exactly one host edge can work.  After those necessary
filters, exact degree and fixed-corner graph-isomorphism checks are applied.
"""

from itertools import combinations, product
import json


GROUPS = (
    ("Z_16", (16,)),
    ("Z_2_x_Z_8", (2, 8)),
    ("Z_4_x_Z_4", (4, 4)),
    ("Z_2_x_Z_2_x_Z_4", (2, 2, 4)),
    ("Z_2_power_4", (2, 2, 2, 2)),
)
EXPECTED_CONNECTION_SET_COUNTS = {
    "Z_16": 21,
    "Z_2_x_Z_8": 33,
    "Z_4_x_Z_4": 33,
    "Z_2_x_Z_2_x_Z_4": 125,
    "Z_2_power_4": 1365,
}
GRID_VERTICES = tuple((i, j) for i in range(3) for j in range(4))
GRID_CORNER_INDEX = GRID_VERTICES.index((0, 0))
TARGET_DEGREES = tuple(sorted([2] * 4 + [3] * 6 + [4] * 2))


def grid_adjacency_masks() -> tuple[int, ...]:
    masks = []
    for i, j in GRID_VERTICES:
        mask = 0
        for k, (ip, jp) in enumerate(GRID_VERTICES):
            if abs(i - ip) + abs(j - jp) == 1:
                mask |= 1 << k
        masks.append(mask)
    return tuple(masks)


GRID_ADJACENCY = grid_adjacency_masks()
GRID_DEGREES = tuple(mask.bit_count() for mask in GRID_ADJACENCY)


def add(x: tuple[int, ...], y: tuple[int, ...], moduli: tuple[int, ...]):
    return tuple((a + b) % modulus for a, b, modulus in zip(x, y, moduli))


def negate(x: tuple[int, ...], moduli: tuple[int, ...]):
    return tuple((-a) % modulus for a, modulus in zip(x, moduli))


def symmetric_connection_sets(
    elements: tuple[tuple[int, ...], ...], moduli: tuple[int, ...]
) -> tuple[frozenset[tuple[int, ...]], ...]:
    """Enumerate every inverse-closed nonidentity subset of cardinality four."""
    zero = tuple(0 for _ in moduli)
    unseen = set(elements)
    unseen.remove(zero)
    inverse_orbits = []
    while unseen:
        x = min(unseen)
        orbit = frozenset((x, negate(x, moduli)))
        inverse_orbits.append(orbit)
        unseen.difference_update(orbit)

    selected_sets = []
    for orbit_count in range(1, 5):
        for chosen in combinations(inverse_orbits, orbit_count):
            selected = frozenset().union(*chosen)
            if len(selected) == 4:
                selected_sets.append(selected)
    assert len(selected_sets) == len(set(selected_sets))
    return tuple(selected_sets)


def fixed_corner_isomorphism(
    host_adjacency: tuple[int, ...], host_degrees: tuple[int, ...]
) -> tuple[int, ...] | None:
    """Map grid indices to image indices, fixing corner 0 at group identity."""
    vertex_count = len(GRID_VERTICES)
    mapping = [-1] * vertex_count
    mapping[GRID_CORNER_INDEX] = 0
    used_mask = 1
    if GRID_DEGREES[GRID_CORNER_INDEX] != host_degrees[0]:
        return None

    def compatible(grid_vertex: int, host_vertex: int) -> bool:
        if GRID_DEGREES[grid_vertex] != host_degrees[host_vertex]:
            return False
        for mapped_grid, mapped_host in enumerate(mapping):
            if mapped_host < 0:
                continue
            grid_edge = bool(GRID_ADJACENCY[grid_vertex] & (1 << mapped_grid))
            host_edge = bool(host_adjacency[host_vertex] & (1 << mapped_host))
            if grid_edge != host_edge:
                return False
        return True

    def search(current_used_mask: int) -> bool:
        if current_used_mask.bit_count() == vertex_count:
            return True
        chosen_grid = -1
        chosen_candidates = None
        for grid_vertex in range(vertex_count):
            if mapping[grid_vertex] >= 0:
                continue
            candidates = [
                host_vertex
                for host_vertex in range(vertex_count)
                if not current_used_mask & (1 << host_vertex)
                and compatible(grid_vertex, host_vertex)
            ]
            if not candidates:
                return False
            if chosen_candidates is None or len(candidates) < len(chosen_candidates):
                chosen_grid = grid_vertex
                chosen_candidates = candidates
        assert chosen_grid >= 0 and chosen_candidates is not None
        for host_vertex in chosen_candidates:
            mapping[chosen_grid] = host_vertex
            if search(current_used_mask | (1 << host_vertex)):
                return True
            mapping[chosen_grid] = -1
        return False

    return tuple(mapping) if search(used_mask) else None


def verify_witness(
    labels: tuple[tuple[int, ...], ...],
    selected: frozenset[tuple[int, ...]],
    moduli: tuple[int, ...],
) -> dict[str, int]:
    assert labels[GRID_CORNER_INDEX] == tuple(0 for _ in moduli)
    assert len(set(labels)) == 12
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


def search_group(name: str, moduli: tuple[int, ...]) -> dict:
    elements = tuple(product(*(range(modulus) for modulus in moduli)))
    assert len(elements) == 16
    zero = tuple(0 for _ in moduli)
    assert elements[0] == zero
    index = {element: k for k, element in enumerate(elements)}
    nonzero_indices = tuple(range(1, 16))
    omitted_quadruples = tuple(combinations(nonzero_indices, 4))
    assert len(omitted_quadruples) == 1365

    connection_sets = symmetric_connection_sets(elements, moduli)
    assert len(connection_sets) == EXPECTED_CONNECTION_SET_COUNTS[name]

    pair_count = one_edge_count = degree_match_count = corner_match_count = 0
    isomorphism_checks = isomorphism_count = 0
    first_witness = None

    for selected in connection_sets:
        neighbor_masks = []
        for x in elements:
            mask = 0
            for difference in selected:
                mask |= 1 << index[add(x, difference, moduli)]
            assert mask.bit_count() == 4
            neighbor_masks.append(mask)

        for omitted in omitted_quadruples:
            pair_count += 1
            omitted_mask = sum(1 << k for k in omitted)
            twice_internal_edges = sum(
                (neighbor_masks[k] & omitted_mask).bit_count() for k in omitted
            )
            assert twice_internal_edges % 2 == 0
            if twice_internal_edges != 2:
                continue
            one_edge_count += 1

            image_indices = tuple(k for k in range(16) if not omitted_mask & (1 << k))
            assert image_indices[0] == 0 and len(image_indices) == 12
            degrees = tuple(
                4 - (neighbor_masks[k] & omitted_mask).bit_count()
                for k in image_indices
            )
            if tuple(sorted(degrees)) != TARGET_DEGREES:
                continue
            degree_match_count += 1
            if degrees[0] != 2:
                continue
            corner_match_count += 1

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
            if first_witness is None:
                image = tuple(elements[k] for k in image_indices)
                labels = tuple(image[mapping[k]] for k in range(12))
                verification = verify_witness(labels, selected, moduli)
                first_witness = {
                    "moduli": list(moduli),
                    "connection_set": [list(x) for x in sorted(selected)],
                    "omitted_elements": [list(elements[k]) for k in omitted],
                    "grid_vertex_order": [list(vertex) for vertex in GRID_VERTICES],
                    "labels_in_grid_vertex_order": [list(x) for x in labels],
                    "label_by_grid_vertex": {
                        f"{i},{j}": list(labels[k])
                        for k, (i, j) in enumerate(GRID_VERTICES)
                    },
                    "verification": verification,
                }

    assert pair_count == len(connection_sets) * 1365
    assert isomorphism_count == 0 or first_witness is not None
    return {
        "group": name,
        "moduli": list(moduli),
        "symmetric_connection_sets_of_size_four_tested": len(connection_sets),
        "omitted_quadruples_tested_per_connection_set": 1365,
        "normalized_candidate_pairs_tested": pair_count,
        "candidates_with_exactly_one_omitted_edge": one_edge_count,
        "candidates_with_target_degree_multiset": degree_match_count,
        "candidates_also_with_identity_of_degree_two": corner_match_count,
        "fixed_corner_isomorphism_checks": isomorphism_checks,
        "isomorphic_host_candidates": isomorphism_count,
        "first_witness": first_witness,
    }


def main() -> None:
    group_results = [search_group(name, moduli) for name, moduli in GROUPS]
    witnesses = [
        result["first_witness"] for result in group_results
        if result["first_witness"] is not None
    ]
    result = {
        "arithmetic": "exact finite-group and integer enumeration",
        "target": "P_3 square P_4",
        "normalization": "the fixed grid corner (0,0) has label the identity",
        "completeness": (
            "all five abelian group isomorphism types of order 16; every inverse-closed "
            "connection set of forced cardinality 4; every four-element omitted subset "
            "avoiding the normalized identity"
        ),
        "structural_filter": (
            "32 host edges minus (16 minus e_U) deleted incident edges equals "
            "16+e_U=17, so the omitted quadruple spans e_U=1 edge"
        ),
        "target_degree_multiset": list(TARGET_DEGREES),
        "groups": group_results,
        "total_normalized_candidate_pairs_tested": sum(
            result["normalized_candidate_pairs_tested"] for result in group_results
        ),
        "total_isomorphic_host_candidates": sum(
            result["isomorphic_host_candidates"] for result in group_results
        ),
        "first_witness": witnesses[0] if witnesses else None,
        "conclusion": (
            "an induced Abelian Cayley embedding exists at order 16"
            if witnesses else
            "no induced Abelian Cayley embedding exists at order 16"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
