#!/usr/bin/env python3
"""Exact radius-six exchange search around the Appendix C 333-plane code.

For an outside subspace X, its blocker B(X) is the set of published planes at
distance below four from X.  Any exchange deleting at most six planes can be
normalized by restoring every deletion not in the union of blockers of the
chosen additions.  Consequently it suffices to enumerate all unions of
blocker sets having cardinality at most six and solve the exact compatibility
clique problem among eligible additions for each union.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import sys
import time
from collections import Counter, defaultdict, deque
from pathlib import Path

import replay_appendix_c as core


DEFAULT_RADIUS = 6


def elements(mask: int) -> tuple[int, ...]:
    result: list[int] = []
    while mask:
        bit = mask & -mask
        result.append(bit.bit_length() - 1)
        mask ^= bit
    return tuple(result)


def subset_masks(mask: int) -> list[int]:
    values = elements(mask)
    result: list[int] = []
    for size in range(len(values) + 1):
        for choice in itertools.combinations(values, size):
            subset = 0
            for value in choice:
                subset |= 1 << value
            result.append(subset)
    return result


def build_union_closure(blockers: set[int], radius: int) -> tuple[list[int], dict[str, int]]:
    by_size: dict[int, list[int]] = {
        size: sorted(mask for mask in blockers if mask.bit_count() == size)
        for size in range(radius + 1)
    }
    index: dict[tuple[int, int], dict[int, list[int]]] = {}
    for block_size in range(1, radius + 1):
        block_list = by_size[block_size]
        for overlap_size in range(1, block_size + 1):
            current: dict[int, list[int]] = defaultdict(list)
            for block in block_list:
                for choice in itertools.combinations(elements(block), overlap_size):
                    key = 0
                    for value in choice:
                        key |= 1 << value
                    current[key].append(block)
            index[(block_size, overlap_size)] = dict(current)

    seen = set(blockers)
    seen.add(0)
    queue = deque(sorted(seen, key=lambda value: (value.bit_count(), value)))
    while queue:
        current_union = queue.popleft()
        current_size = current_union.bit_count()
        if current_size >= radius:
            continue
        room = radius - current_size
        current_elements = elements(current_union)
        for block_size in range(1, radius + 1):
            minimum_overlap = max(0, block_size - room)
            if minimum_overlap == 0:
                candidates = by_size[block_size]
            elif minimum_overlap > len(current_elements):
                continue
            else:
                collected: set[int] = set()
                lookup = index[(block_size, minimum_overlap)]
                for choice in itertools.combinations(current_elements, minimum_overlap):
                    key = 0
                    for value in choice:
                        key |= 1 << value
                    collected.update(lookup.get(key, ()))
                candidates = collected
            for block in candidates:
                new_union = current_union | block
                if new_union == current_union or new_union.bit_count() > radius:
                    continue
                if new_union not in seen:
                    seen.add(new_union)
                    queue.append(new_union)
    ordered = sorted(seen, key=lambda value: (value.bit_count(), value))
    census = Counter(value.bit_count() for value in ordered)
    return ordered, {str(size): census[size] for size in range(radius + 1)}


def maximum_clique(vertices: list[int], dimensions: dict[int, int]) -> tuple[int, list[int]]:
    count = len(vertices)
    if count == 0:
        return 0, []
    adjacency = [0] * count
    for i, first in enumerate(vertices):
        first_dim = dimensions[first]
        for j in range(i + 1, count):
            second = vertices[j]
            intersection_size = (first & second).bit_count()
            intersection_dim = intersection_size.bit_length() - 1
            if first_dim + dimensions[second] - 2 * intersection_dim >= 4:
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i

    best_size = 0
    best_vertices: list[int] = []

    def color_sort(candidate_mask: int) -> tuple[list[int], list[int]]:
        order: list[int] = []
        bounds: list[int] = []
        uncolored = candidate_mask
        color = 0
        while uncolored:
            color += 1
            available = uncolored
            while available:
                bit = available & -available
                vertex = bit.bit_length() - 1
                order.append(vertex)
                bounds.append(color)
                uncolored ^= bit
                available ^= bit
                available &= ~adjacency[vertex]
        return order, bounds

    def expand(candidate_mask: int, chosen: list[int]) -> None:
        nonlocal best_size, best_vertices
        if not candidate_mask:
            if len(chosen) > best_size:
                best_size = len(chosen)
                best_vertices = chosen.copy()
            return
        order, color_bounds = color_sort(candidate_mask)
        for index in range(len(order) - 1, -1, -1):
            if len(chosen) + color_bounds[index] <= best_size:
                return
            vertex = order[index]
            bit = 1 << vertex
            if not (candidate_mask & bit):
                continue
            chosen.append(vertex)
            expand(candidate_mask & adjacency[vertex], chosen)
            chosen.pop()
            candidate_mask ^= bit

    expand((1 << count) - 1, [])
    return best_size, [vertices[index] for index in best_vertices]


def basis_strings(mask: int) -> list[str]:
    return [core.binary_row(row) for row in core.basis_from_mask(mask)]


def canonical_line(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, default=Path("data/appendix_c_333.json"))
    parser.add_argument("--output", type=Path, default=Path("experiments/radius6_search.json"))
    parser.add_argument("--radius", type=int, default=DEFAULT_RADIUS)
    args = parser.parse_args()
    if not 0 <= args.radius <= 10:
        parser.error("--radius must lie between 0 and 10")
    radius = args.radius
    started = time.time()

    planes, _ = core.load_published_code(args.data)
    plane_set = set(planes)
    spaces = core.enumerate_subspaces()
    dimensions = {space: core.dimension(space) for space in spaces}

    candidates_by_blocker: dict[int, list[int]] = defaultdict(list)
    blocker_histogram: Counter[int] = Counter()
    all_limited_candidates: list[tuple[int, int]] = []
    for candidate in spaces:
        if candidate in plane_set:
            continue
        blocker_mask = 0
        for index, plane in enumerate(planes):
            intersection_size = (candidate & plane).bit_count()
            intersection_dim = intersection_size.bit_length() - 1
            if dimensions[candidate] + 3 - 2 * intersection_dim < 4:
                blocker_mask |= 1 << index
        blocker_count = blocker_mask.bit_count()
        blocker_histogram[blocker_count] += 1
        if blocker_count <= radius:
            candidates_by_blocker[blocker_mask].append(candidate)
            all_limited_candidates.append((candidate, blocker_mask))

    blocker_sets = set(candidates_by_blocker)
    removal_unions, union_census = build_union_closure(blocker_sets, radius)

    blocker_map_hash = hashlib.sha256()
    for candidate, blockers in sorted(all_limited_candidates):
        blocker_map_hash.update(canonical_line({
            "basis": basis_strings(candidate),
            "blockers": list(elements(blockers))
        }))

    trace_hash = hashlib.sha256()
    best_size = -1
    best_by_removed: dict[int, int] = {size: -1 for size in range(radius + 1)}
    maximum_eligible = 0
    maximum_eligible_by_removed: dict[int, int] = {size: 0 for size in range(radius + 1)}
    selected_witnesses: dict[int, dict[str, object]] = {}
    sets_with_result_at_least_334 = 0
    for removal in removal_unions:
        eligible: list[int] = []
        for blocker_subset in subset_masks(removal):
            eligible.extend(candidates_by_blocker.get(blocker_subset, ()))
        eligible = sorted(eligible)
        omega, additions = maximum_clique(eligible, dimensions)
        removed_count = removal.bit_count()
        result_size = 333 - removed_count + omega
        maximum_eligible = max(maximum_eligible, len(eligible))
        maximum_eligible_by_removed[removed_count] = max(
            maximum_eligible_by_removed[removed_count], len(eligible)
        )
        best_size = max(best_size, result_size)
        if result_size > best_by_removed[removed_count]:
            best_by_removed[removed_count] = result_size
            selected_witnesses[removed_count] = {
                "removed_indices": list(elements(removal)),
                "added_bases": [basis_strings(mask) for mask in additions],
                "eligible_candidate_count": len(eligible),
                "addition_clique_size": omega,
                "result_size": result_size
            }
        if result_size >= 334:
            sets_with_result_at_least_334 += 1
        trace_hash.update(canonical_line({
            "removed_indices": list(elements(removal)),
            "eligible_candidate_count": len(eligible),
            "addition_clique_size": omega,
            "result_size": result_size
        }))

    result = {
        "schema": "radius-six-exchange-search-v1" if radius == 6 else "radius-exchange-search-diagnostic-v1",
        "scope": f"all codes obtained by deleting at most {radius} planes from the Appendix C 333-code and adding arbitrary mutually compatible ambient subspaces",
        "normalization": "each deletion set is reduced to the union of blocker sets of its selected additions",
        "arithmetic": "exact integer bit masks over F_2",
        "randomness": None,
        "python": sys.version.split()[0],
        "platform": platform.platform(),
        "radius": radius,
        "ambient_subspaces": len(spaces),
        "published_planes": len(planes),
        "outside_candidates_by_blocker_count_0_through_6": {
            str(size): blocker_histogram[size] for size in range(radius + 1)
        },
        "unique_blocker_sets_by_size_0_through_6": {
            str(size): sum(mask.bit_count() == size for mask in blocker_sets)
            for size in range(radius + 1)
        },
        "normalized_removal_unions_by_size": union_census,
        "normalized_removal_unions_total": len(removal_unions),
        "maximum_eligible_candidate_count": maximum_eligible,
        "maximum_eligible_candidate_count_by_removed": {
            str(size): maximum_eligible_by_removed[size] for size in range(radius + 1)
        },
        "best_code_size": best_size,
        "best_code_size_by_normalized_removed": {
            str(size): best_by_removed[size] for size in range(radius + 1)
        },
        "sets_with_result_at_least_334": sets_with_result_at_least_334,
        "selected_witnesses": {str(size): selected_witnesses[size] for size in sorted(selected_witnesses)},
        "blocker_map_sha256": blocker_map_hash.hexdigest(),
        "full_search_trace_sha256": trace_hash.hexdigest(),
        "data_sha256": hashlib.sha256(args.data.read_bytes()).hexdigest(),
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds_diagnostic_only": round(time.time() - started, 6)
    }
    args.output.write_bytes(canonical_line(result))
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
