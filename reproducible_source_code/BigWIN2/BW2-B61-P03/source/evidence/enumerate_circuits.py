#!/usr/bin/env python3
"""Exact enumerator and certificate generator for win-00061-p03.

Only the Python standard library is used.  The output is deterministic.
"""

from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter, defaultdict
from pathlib import Path


FACET_WORDS = (
    "105", "053", "537", "374", "741", "410",
    "216", "165", "658", "587", "872", "721",
    "023", "236", "364", "648", "480", "802",
)
FACETS = tuple(frozenset(map(int, word)) for word in FACET_WORDS)
FACET_ID = {facet: i for i, facet in enumerate(FACETS)}
VERTICES = tuple(range(9))


def rotations(word: tuple[int, ...]) -> list[tuple[int, ...]]:
    return [word[i:] + word[:i] for i in range(len(word))]


def canonical_directed(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(rotations(word))


def canonical_unoriented(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(rotations(word) + rotations(tuple(reversed(word))))


def word_text(word: tuple[int, ...]) -> str:
    return "".join(map(str, word))


def circuit_facets(word: tuple[int, ...]) -> frozenset[frozenset[int]]:
    n = len(word)
    return frozenset(
        frozenset((word[i], word[(i + 1) % n], word[(i + 2) % n]))
        for i in range(n)
    )


def main() -> None:
    if len(FACET_ID) != 18 or any(len(facet) != 3 for facet in FACETS):
        raise AssertionError("input is not 18 distinct three-element facets")

    edge_incidence: dict[frozenset[int], list[tuple[int, int]]] = defaultdict(list)
    for facet_id, facet in enumerate(FACETS):
        for opposite in facet:
            edge_incidence[facet - {opposite}].append((facet_id, opposite))
    if len(edge_incidence) != 27 or any(len(x) != 2 for x in edge_incidence.values()):
        raise AssertionError("input is not a closed triangulated surface")

    def successor(state: tuple[int, int, int]) -> tuple[int, int, int]:
        a, b, c = state
        current_id = FACET_ID[frozenset(state)]
        choices = edge_incidence[frozenset((b, c))]
        other = [(facet_id, d) for facet_id, d in choices if facet_id != current_id]
        if len(other) != 1:
            raise AssertionError("ordered transition is not unique")
        return (b, c, other[0][1])

    states = sorted(
        permutation
        for facet in FACETS
        for permutation in itertools.permutations(sorted(facet))
    )
    transitions = [(state, successor(state)) for state in states]
    if len(states) != 108 or len({target for _, target in transitions}) != 108:
        raise AssertionError("successor is not a permutation of the ordered states")

    unseen = set(states)
    directed_orbits: list[dict[str, object]] = []
    while unseen:
        start = min(unseen)
        orbit: list[tuple[int, int, int]] = []
        state = start
        while state not in orbit:
            if state not in unseen:
                raise AssertionError("orbits merged before closing")
            orbit.append(state)
            unseen.remove(state)
            state = successor(state)
        if state != start:
            raise AssertionError("orbit did not return to its initial state")
        word = tuple(state[0] for state in orbit)
        ids = tuple(FACET_ID[frozenset(state)] for state in orbit)
        directed_orbits.append({
            "word": word_text(canonical_directed(word)),
            "length": len(word),
            "facet_ids_in_order": list(ids),
            "facet_projection_injective": len(ids) == len(set(ids)),
        })
    directed_orbits.sort(key=lambda item: item["word"])

    valid_directed = [
        tuple(map(int, item["word"]))
        for item in directed_orbits
        if item["facet_projection_injective"]
    ]
    circuits_by_word: dict[tuple[int, ...], frozenset[frozenset[int]]] = {}
    directed_multiplicity: Counter[tuple[int, ...]] = Counter()
    for word in valid_directed:
        canonical = canonical_unoriented(word)
        directed_multiplicity[canonical] += 1
        facets = circuit_facets(canonical)
        if canonical in circuits_by_word and circuits_by_word[canonical] != facets:
            raise AssertionError("canonical circuit collision")
        circuits_by_word[canonical] = facets
    circuits = sorted(circuits_by_word)
    if any(directed_multiplicity[word] != 2 for word in circuits):
        raise AssertionError("reversal did not pair the directed circuits")

    circuit_records = []
    for word in circuits:
        facets = circuits_by_word[word]
        circuit_records.append({
            "word": word_text(word),
            "length": len(word),
            "facet_ids": sorted(FACET_ID[facet] for facet in facets),
            "reversal_directed_orbit_multiplicity": directed_multiplicity[word],
        })

    all_facets = frozenset(FACETS)
    exact_covers: list[tuple[tuple[int, ...], ...]] = []
    # There are only nine circuits, so all 2^9 subcollections can be checked.
    for mask in range(1 << len(circuits)):
        chosen = tuple(circuits[i] for i in range(len(circuits)) if mask & (1 << i))
        pieces = [circuits_by_word[word] for word in chosen]
        if sum(map(len, pieces)) != 18:
            continue
        union = frozenset().union(*pieces)
        if union == all_facets:
            exact_covers.append(chosen)
    exact_covers.sort()

    circuit_index = {circuits_by_word[word]: i for i, word in enumerate(circuits)}
    cover_sets = [frozenset(circuits_by_word[word] for word in cover) for cover in exact_covers]
    cover_index = {cover: i for i, cover in enumerate(cover_sets)}

    automorphisms: list[tuple[int, ...]] = []
    cover_actions: list[tuple[int, ...]] = []
    for permutation in itertools.permutations(VERTICES):
        image_facets = frozenset(
            frozenset(permutation[vertex] for vertex in facet) for facet in FACETS
        )
        if image_facets != all_facets:
            continue
        automorphisms.append(permutation)
        action = []
        for cover in cover_sets:
            image_cover = frozenset(
                frozenset(
                    frozenset(permutation[vertex] for vertex in facet)
                    for facet in circuit
                )
                for circuit in cover
            )
            if image_cover not in cover_index:
                raise AssertionError("automorphism does not preserve exact covers")
            action.append(cover_index[image_cover])
        cover_actions.append(tuple(action))

    unseen_covers = set(range(len(exact_covers)))
    cover_orbits: list[list[int]] = []
    while unseen_covers:
        seed = min(unseen_covers)
        orbit = sorted({action[seed] for action in cover_actions})
        cover_orbits.append(orbit)
        unseen_covers.difference_update(orbit)

    transition_lines = [
        f"{word_text(source)}->{word_text(target)}" for source, target in transitions
    ]
    transition_sha256 = hashlib.sha256(
        ("\n".join(transition_lines) + "\n").encode("ascii")
    ).hexdigest()
    action_counts = Counter(",".join(map(str, action)) for action in cover_actions)
    fixed_sum = sum(sum(action[i] == i for i in range(len(exact_covers))) for action in cover_actions)

    certificate = {
        "format": "win-00061-p03-exact-circuit-certificate-v1",
        "facet_words_in_source_order": list(FACET_WORDS),
        "counts": {
            "vertices": 9,
            "facets": 18,
            "edges": 27,
            "ordered_facet_states": len(states),
            "directed_transition_orbits": len(directed_orbits),
            "valid_directed_transition_orbits": len(valid_directed),
            "unoriented_circuits_mod_rotation_reversal": len(circuits),
            "exact_covers": len(exact_covers),
            "one_circuit_decompositions": sum(len(cover) == 1 for cover in exact_covers),
            "two_circuit_decompositions": sum(len(cover) == 2 for cover in exact_covers),
            "three_circuit_decompositions": sum(len(cover) == 3 for cover in exact_covers),
            "automorphisms": len(automorphisms),
            "minimum_decomposition_orbits_under_automorphisms": len(cover_orbits),
        },
        "edge_incidence": {
            "".join(map(str, sorted(edge))): [facet_id for facet_id, _ in sorted(incidence)]
            for edge, incidence in sorted(edge_incidence.items(), key=lambda item: tuple(sorted(item[0])))
        },
        "ordered_transition_table_sha256": transition_sha256,
        "directed_transition_orbits": directed_orbits,
        "unoriented_circuits": circuit_records,
        "exact_covers": [
            {"circuit_words": [word_text(word) for word in cover], "size": len(cover)}
            for cover in exact_covers
        ],
        "automorphism_group": {
            "permutations_as_images_of_012345678": [word_text(p) for p in automorphisms],
            "action_on_exact_covers_counts": dict(sorted(action_counts.items())),
            "orbits_on_exact_cover_indices": cover_orbits,
            "burnside_fixed_point_sum": fixed_sum,
            "burnside_orbit_count": fixed_sum // len(automorphisms),
        },
        "conclusion": {
            "c_S": min(map(len, exact_covers)),
            "explicit_minimum_decomposition": [word_text(word) for word in exact_covers[0]],
            "minimum_decompositions_before_automorphisms": len(exact_covers),
            "minimum_decompositions_mod_rotation_reversal_circuit_order_and_automorphisms": len(cover_orbits),
        },
    }

    output = Path(__file__).with_name("circuit_certificate.json")
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(certificate["counts"], sort_keys=True))
    print(json.dumps(certificate["conclusion"], sort_keys=True))
    print(f"wrote {output}")


if __name__ == "__main__":
    main()
