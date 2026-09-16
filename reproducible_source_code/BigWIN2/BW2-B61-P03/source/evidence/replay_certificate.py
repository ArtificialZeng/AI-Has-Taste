#!/usr/bin/env python3
"""Independent replay checker for circuit_certificate.json.

This checker imports no code from the generator.  It reconstructs circuits by
walking from every ordered facet, then independently checks every subcollection
and every vertex permutation.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERTIFICATE = HERE / "circuit_certificate.json"


def turns(seq: tuple[int, ...]) -> set[tuple[int, ...]]:
    return {seq[k:] + seq[:k] for k in range(len(seq))}


def unoriented(seq: tuple[int, ...]) -> tuple[int, ...]:
    return min(turns(seq) | turns(tuple(reversed(seq))))


def windows(seq: tuple[int, ...]) -> frozenset[frozenset[int]]:
    return frozenset(
        frozenset((seq[k], seq[(k + 1) % len(seq)], seq[(k + 2) % len(seq)]))
        for k in range(len(seq))
    )


def replay() -> None:
    claimed = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    raw_words = claimed["facet_words_in_source_order"]
    triangles = tuple(frozenset(int(c) for c in text) for text in raw_words)
    if len(triangles) != 18 or len(set(triangles)) != 18:
        raise AssertionError("facet input is not the frozen 18-facet complex")
    triangle_number = {triangle: k for k, triangle in enumerate(triangles)}

    # Reconstruct edge-to-facet incidence in a different representation.
    edge_to_triangles: dict[tuple[int, int], list[int]] = {}
    for k, triangle in enumerate(triangles):
        for edge in itertools.combinations(sorted(triangle), 2):
            edge_to_triangles.setdefault(edge, []).append(k)
    if len(edge_to_triangles) != 27 or Counter(map(len, edge_to_triangles.values())) != {2: 27}:
        raise AssertionError("not every edge has exactly two incident facets")

    def step(ordered: tuple[int, int, int]) -> tuple[int, int, int]:
        a, b, c = ordered
        current = triangle_number[frozenset(ordered)]
        adjacent = edge_to_triangles[tuple(sorted((b, c)))]
        if len(adjacent) != 2 or current not in adjacent:
            raise AssertionError("bad transition incidence")
        following = adjacent[0] if adjacent[1] == current else adjacent[1]
        new_vertex = next(iter(triangles[following] - {b, c}))
        return b, c, new_vertex

    ordered_starts = sorted(
        perm for triangle in triangles for perm in itertools.permutations(sorted(triangle))
    )
    transition_lines = [
        "".join(map(str, start)) + "->" + "".join(map(str, step(start)))
        for start in ordered_starts
    ]
    digest = hashlib.sha256(("\n".join(transition_lines) + "\n").encode("ascii")).hexdigest()
    if digest != claimed["ordered_transition_table_sha256"]:
        raise AssertionError("ordered transition table digest mismatch")

    # Start at all 108 ordered facets rather than consuming claimed orbit data.
    directed_cycles: set[tuple[int, ...]] = set()
    for start in ordered_starts:
        path: list[tuple[int, int, int]] = []
        state = start
        while state not in path:
            path.append(state)
            state = step(state)
            if len(path) > 108:
                raise AssertionError("transition walk did not close")
        if state != start:
            raise AssertionError("transition map is not a disjoint union of cycles")
        first_vertices = tuple(state[0] for state in path)
        directed_cycles.add(min(turns(first_vertices)))
    if len(directed_cycles) != 18:
        raise AssertionError("wrong directed orbit count")

    valid_directed = {
        seq for seq in directed_cycles
        if len(windows(seq)) == len(seq)
        and all(window in triangle_number for window in windows(seq))
    }
    circuits = sorted({unoriented(seq) for seq in valid_directed})
    if len(valid_directed) != 18 or len(circuits) != 9:
        raise AssertionError("wrong valid/unoriented circuit counts")
    if any(len(seq) != 6 for seq in circuits):
        raise AssertionError("not all circuits have length six")

    claimed_circuits = sorted(tuple(map(int, row["word"])) for row in claimed["unoriented_circuits"])
    if circuits != claimed_circuits:
        raise AssertionError("circuit list mismatch")

    target = frozenset(triangles)
    circuit_faces = [windows(seq) for seq in circuits]
    covers: list[tuple[int, ...]] = []
    # Exhaust all 512 subsets, independently of the generator's cover loop.
    for selections in itertools.product((False, True), repeat=len(circuits)):
        chosen = tuple(k for k, selected in enumerate(selections) if selected)
        multiplicity = Counter(face for k in chosen for face in circuit_faces[k])
        if set(multiplicity) == target and set(multiplicity.values()) == {1}:
            covers.append(chosen)
    covers.sort()
    cover_words = [["".join(map(str, circuits[k])) for k in cover] for cover in covers]
    claimed_cover_words = [row["circuit_words"] for row in claimed["exact_covers"]]
    if cover_words != claimed_cover_words:
        raise AssertionError("exact-cover list mismatch")
    if Counter(map(len, covers)) != {3: 3}:
        raise AssertionError("one/two exclusion or three-cover count failed")

    # Independent exhaustive Aut(S) calculation and orbit/Burnside check.
    automorphisms: list[tuple[int, ...]] = []
    actions: list[tuple[int, ...]] = []
    cover_face_sets = [frozenset(circuit_faces[k] for k in cover) for cover in covers]
    cover_lookup = {cover: k for k, cover in enumerate(cover_face_sets)}
    for permutation in itertools.permutations(range(9)):
        image = frozenset(
            frozenset(permutation[v] for v in triangle) for triangle in triangles
        )
        if image != target:
            continue
        automorphisms.append(permutation)
        induced = []
        for cover in cover_face_sets:
            image_cover = frozenset(
                frozenset(frozenset(permutation[v] for v in face) for face in circuit)
                for circuit in cover
            )
            induced.append(cover_lookup[image_cover])
        actions.append(tuple(induced))
    if len(automorphisms) != 108:
        raise AssertionError("wrong automorphism group size")
    claimed_auts = claimed["automorphism_group"]["permutations_as_images_of_012345678"]
    if ["".join(map(str, p)) for p in automorphisms] != claimed_auts:
        raise AssertionError("automorphism list mismatch")
    action_counts = Counter(",".join(map(str, action)) for action in actions)
    if dict(sorted(action_counts.items())) != claimed["automorphism_group"]["action_on_exact_covers_counts"]:
        raise AssertionError("action count mismatch")
    fixed_sum = sum(sum(action[k] == k for k in range(3)) for action in actions)
    if fixed_sum != 108 or fixed_sum // len(automorphisms) != 1:
        raise AssertionError("Burnside quotient mismatch")

    counts = claimed["counts"]
    expected_counts = {
        "vertices": 9,
        "facets": 18,
        "edges": 27,
        "ordered_facet_states": 108,
        "directed_transition_orbits": 18,
        "valid_directed_transition_orbits": 18,
        "unoriented_circuits_mod_rotation_reversal": 9,
        "exact_covers": 3,
        "one_circuit_decompositions": 0,
        "two_circuit_decompositions": 0,
        "three_circuit_decompositions": 3,
        "automorphisms": 108,
        "minimum_decomposition_orbits_under_automorphisms": 1,
    }
    if counts != expected_counts:
        raise AssertionError("summary-count mismatch")
    if claimed["conclusion"]["c_S"] != 3:
        raise AssertionError("conclusion mismatch")
    print("REPLAY OK")
    print(json.dumps(expected_counts, sort_keys=True))


if __name__ == "__main__":
    replay()
