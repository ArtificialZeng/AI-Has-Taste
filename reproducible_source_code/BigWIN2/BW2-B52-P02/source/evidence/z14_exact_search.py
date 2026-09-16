#!/usr/bin/env python3
"""Exact corner-normalized induced-host search for P_3 square P_4 in Z/14Z.

Translate a fixed grid corner to 0.  A 12-element image in Z/14Z then
omits two of the 13 nonzero residues.  The seven negation-orbits on the
nonzero residues (six pairs and the singleton {7}) give all 128 symmetric
connection sets.  Thus this script examines exactly C(13,2)*128 = 9,984
normalized host candidates.  Graph isomorphism is checked by exact
backtracking constrained to map the fixed grid corner to residue 0.
"""

from itertools import combinations
import json


MODULUS = 14
GRID_VERTICES = tuple((i, j) for i in range(3) for j in range(4))
GRID_CORNER = (0, 0)
GRID_CORNER_INDEX = GRID_VERTICES.index(GRID_CORNER)
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


def connection_set(mask: int) -> frozenset[int]:
    selected = set()
    for difference in range(1, 7):
        if mask & (1 << (difference - 1)):
            selected.add(difference)
            selected.add(MODULUS - difference)
    if mask & (1 << 6):
        selected.add(7)
    return frozenset(selected)


def host_adjacency_masks(
    image: tuple[int, ...], selected: frozenset[int]
) -> tuple[int, ...]:
    masks = []
    for x in image:
        mask = 0
        for k, y in enumerate(image):
            if x != y and (y - x) % MODULUS in selected:
                mask |= 1 << k
        masks.append(mask)
    return tuple(masks)


def fixed_corner_isomorphism(
    host_adjacency: tuple[int, ...], host_degrees: tuple[int, ...]
) -> tuple[int, ...] | None:
    """Return grid-index -> host-index bijection, fixing the corner at 0."""
    vertex_count = len(GRID_VERTICES)
    mapping = [-1] * vertex_count
    mapping[GRID_CORNER_INDEX] = 0  # image is sorted and contains residue 0
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
        chosen_candidates: list[int] | None = None
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
    image: tuple[int, ...],
    selected: frozenset[int],
    mapping: tuple[int, ...],
) -> dict[str, int]:
    labels = tuple(image[mapping[k]] for k in range(len(GRID_VERTICES)))
    assert labels[GRID_CORNER_INDEX] == 0
    assert len(set(labels)) == len(GRID_VERTICES)

    edge_pairs = nonedge_pairs = 0
    for u in range(len(GRID_VERTICES)):
        for v in range(u + 1, len(GRID_VERTICES)):
            is_grid_edge = bool(GRID_ADJACENCY[u] & (1 << v))
            is_cayley_edge = (labels[v] - labels[u]) % MODULUS in selected
            assert is_grid_edge == is_cayley_edge
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
    image_count = connection_count = candidate_count = 0
    degree_match_count = corner_degree_match_count = isomorphism_count = 0
    fixed_corner_checks = 0
    first_witness = None

    all_connection_sets = tuple(connection_set(mask) for mask in range(128))
    assert len(set(all_connection_sets)) == 128

    for omitted_pair in combinations(range(1, MODULUS), 2):
        image_count += 1
        image = tuple(x for x in range(MODULUS) if x not in omitted_pair)
        assert len(image) == 12 and image[0] == 0

        for mask, selected in enumerate(all_connection_sets):
            connection_count += 1
            candidate_count += 1
            adjacency = host_adjacency_masks(image, selected)
            degrees = tuple(row.bit_count() for row in adjacency)
            signature = tuple(sorted(degrees))
            if signature != TARGET_DEGREES:
                continue
            degree_match_count += 1
            if degrees[0] != 2:
                continue
            corner_degree_match_count += 1
            fixed_corner_checks += 1
            mapping = fixed_corner_isomorphism(adjacency, degrees)
            if mapping is None:
                continue
            isomorphism_count += 1
            if first_witness is None:
                pair_checks = verify_witness(image, selected, mapping)
                labels = tuple(image[mapping[k]] for k in range(len(GRID_VERTICES)))
                first_witness = {
                    "omitted_residues": list(omitted_pair),
                    "connection_mask": mask,
                    "connection_set": sorted(selected),
                    "grid_vertex_order": [list(vertex) for vertex in GRID_VERTICES],
                    "labels_in_grid_vertex_order": list(labels),
                    "label_by_grid_vertex": {
                        f"{i},{j}": labels[k]
                        for k, (i, j) in enumerate(GRID_VERTICES)
                    },
                    "verification": pair_checks,
                }

    assert image_count == 78
    assert connection_count == 78 * 128
    assert candidate_count == 9984
    assert isomorphism_count == 0 or first_witness is not None

    result = {
        "arithmetic": "exact integer enumeration",
        "group": "Z_14",
        "normalization": "the fixed grid corner (0,0) has label 0",
        "omitted_pairs_tested": image_count,
        "symmetric_connection_sets_tested_per_image": 128,
        "normalized_host_candidates_tested": candidate_count,
        "target_degree_multiset": list(TARGET_DEGREES),
        "candidates_with_target_degree_multiset": degree_match_count,
        "candidates_also_with_zero_of_degree_two": corner_degree_match_count,
        "fixed_corner_isomorphism_checks": fixed_corner_checks,
        "isomorphic_host_candidates": isomorphism_count,
        "first_witness": first_witness,
        "conclusion": (
            "an induced Abelian Cayley embedding exists in Z_14"
            if first_witness is not None
            else "no induced Abelian Cayley embedding exists in Z_14"
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
