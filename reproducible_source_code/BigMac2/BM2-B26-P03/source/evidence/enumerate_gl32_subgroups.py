#!/usr/bin/env python3
"""Exact subgroup and irreducibility certificate for GL(3,2).

Vectors are the integers 0,...,7, with bit i the coefficient of e_i.
A matrix is stored by the images of (e_0,e_1,e_2), i.e. by its three
column-vectors.  No external algebra package is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, deque
from pathlib import Path


IDENTITY = (1, 2, 4)


def apply_matrix(matrix: tuple[int, int, int], vector: int) -> int:
    out = 0
    for i, column in enumerate(matrix):
        if (vector >> i) & 1:
            out ^= column
    return out


def compose(
    left: tuple[int, int, int], right: tuple[int, int, int]
) -> tuple[int, int, int]:
    """Return left o right."""
    return tuple(apply_matrix(left, column) for column in right)


def span(vectors: tuple[int, ...] | list[int]) -> frozenset[int]:
    result = {0}
    for vector in vectors:
        result |= {x ^ vector for x in tuple(result)}
    return frozenset(result)


def canonical_basis(subspace: frozenset[int]) -> list[int]:
    basis: list[int] = []
    current = frozenset({0})
    for vector in sorted(subspace - {0}):
        if vector not in current:
            basis.append(vector)
            current = span(basis)
    assert current == subspace
    return basis


def subgroup_mask(subgroup: frozenset[int]) -> int:
    value = 0
    for element in subgroup:
        value |= 1 << element
    return value


def mask_hex(mask: int, width: int) -> str:
    return f"0x{mask:0{width}x}"


def vector_bits(vector: int) -> str:
    return format(vector, "03b")[::-1]


def matrix_rows(matrix: tuple[int, int, int]) -> list[list[int]]:
    return [[(matrix[column] >> row) & 1 for column in range(3)] for row in range(3)]


def build_group():
    matrices = sorted(
        {
            columns
            for a in range(1, 8)
            for b in range(1, 8)
            for c in range(1, 8)
            if len(span(columns := (a, b, c))) == 8
        }
    )
    assert len(matrices) == 168
    assert IDENTITY in matrices
    index = {matrix: i for i, matrix in enumerate(matrices)}
    identity = index[IDENTITY]
    multiplication = [
        [index[compose(left, right)] for right in matrices] for left in matrices
    ]
    inverses = []
    for i in range(168):
        candidates = [
            j
            for j in range(168)
            if multiplication[i][j] == identity and multiplication[j][i] == identity
        ]
        assert len(candidates) == 1
        inverses.append(candidates[0])
    return matrices, multiplication, inverses, identity


def generated_subgroup(
    generators: tuple[int, ...] | list[int],
    multiplication: list[list[int]],
    inverses: list[int],
    identity: int,
) -> frozenset[int]:
    steps = tuple(dict.fromkeys(tuple(generators) + tuple(inverses[g] for g in generators)))
    seen = {identity}
    queue = deque([identity])
    while queue:
        element = queue.popleft()
        for step in steps:
            product = multiplication[element][step]
            if product not in seen:
                seen.add(product)
                queue.append(product)
    return frozenset(seen)


def enumerate_subgroups(multiplication, inverses, identity):
    trivial = frozenset({identity})
    generators_by_group: dict[frozenset[int], tuple[int, ...]] = {trivial: ()}
    queue = deque([trivial])
    adjunctions = 0
    while queue:
        subgroup = queue.popleft()
        generators = generators_by_group[subgroup]
        for element in range(168):
            if element in subgroup:
                continue
            adjunctions += 1
            generated = generated_subgroup(
                generators + (element,), multiplication, inverses, identity
            )
            if generated not in generators_by_group:
                generators_by_group[generated] = generators + (element,)
                queue.append(generated)
    ordered = sorted(generators_by_group, key=lambda h: (len(h), subgroup_mask(h)))
    return ordered, generators_by_group, adjunctions


def verify_subgroup(subgroup, multiplication, inverses, identity):
    if identity not in subgroup:
        return False
    if any(inverses[x] not in subgroup for x in subgroup):
        return False
    return all(multiplication[x][y] in subgroup for x in subgroup for y in subgroup)


def conjugate_subgroup(subgroup, by, multiplication, inverses):
    by_inverse = inverses[by]
    return frozenset(
        multiplication[multiplication[by_inverse][element]][by] for element in subgroup
    )


def enumerate_subspaces():
    spaces = []
    for mask in range(256):
        members = frozenset(v for v in range(8) if (mask >> v) & 1)
        if 0 not in members:
            continue
        if all((x ^ y) in members for x in members for y in members):
            spaces.append(members)
    spaces.sort(key=lambda w: (len(w), sum(1 << v for v in w)))
    assert Counter(len(w) for w in spaces) == Counter({1: 1, 2: 7, 4: 7, 8: 1})
    return spaces


def invariant_subspaces(subgroup, matrices, subspaces):
    answer = []
    for subspace in subspaces:
        if len(subspace) not in (2, 4):
            continue
        if all(
            frozenset(apply_matrix(matrices[element], vector) for vector in subspace)
            == subspace
            for element in subgroup
        ):
            answer.append(subspace)
    return answer


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    matrices, multiplication, inverses, identity = build_group()
    subgroups, generators_by_group, adjunctions = enumerate_subgroups(
        multiplication, inverses, identity
    )
    subgroup_set = set(subgroups)

    # Exact internal checks, including the local saturation criterion proving
    # completeness of the enumerated subgroup collection.
    assert all(
        verify_subgroup(subgroup, multiplication, inverses, identity)
        for subgroup in subgroups
    )
    saturation_checks = 0
    for subgroup in subgroups:
        generators = generators_by_group[subgroup]
        assert generated_subgroup(generators, multiplication, inverses, identity) == subgroup
        for element in range(168):
            saturation_checks += 1
            generated = generated_subgroup(
                generators + (element,), multiplication, inverses, identity
            )
            assert generated in subgroup_set

    # Conjugacy orbits and canonical representatives.
    unseen = set(subgroups)
    conjugacy_classes = []
    while unseen:
        seed = min(unseen, key=subgroup_mask)
        orbit = {
            conjugate_subgroup(seed, g, multiplication, inverses) for g in range(168)
        }
        assert orbit <= subgroup_set
        canonical = min(orbit, key=subgroup_mask)
        conjugacy_classes.append((canonical, orbit))
        unseen -= orbit
    conjugacy_classes.sort(key=lambda item: (len(item[0]), subgroup_mask(item[0])))
    assert sum(len(orbit) for _, orbit in conjugacy_classes) == len(subgroups)
    assert len(set().union(*(orbit for _, orbit in conjugacy_classes))) == len(subgroups)

    class_of = {}
    for class_id, (_, orbit) in enumerate(conjugacy_classes):
        for subgroup in orbit:
            assert subgroup not in class_of
            class_of[subgroup] = class_id

    subspaces = enumerate_subspaces()
    irreducible_classes = []
    class_records = []
    for class_id, (representative, orbit) in enumerate(conjugacy_classes):
        invariant = invariant_subspaces(representative, matrices, subspaces)
        irreducible = not invariant
        if irreducible:
            irreducible_classes.append(class_id)
        class_records.append(
            {
                "class_id": class_id,
                "order": len(representative),
                "orbit_size": len(orbit),
                "normalizer_order": 168 // len(orbit),
                "representative_subgroup_id": subgroups.index(representative),
                "representative_element_ids": sorted(representative),
                "representative_generator_ids": list(generators_by_group[representative]),
                "representative_mask_hex": mask_hex(subgroup_mask(representative), 42),
                "irreducible": irreducible,
                "invariant_proper_nonzero_subspaces": [
                    {
                        "dimension": len(canonical_basis(space)),
                        "vector_ids": sorted(space),
                        "basis_vector_ids": canonical_basis(space),
                        "basis_vectors_bits_e0_e1_e2": [
                            vector_bits(v) for v in canonical_basis(space)
                        ],
                    }
                    for space in invariant
                ],
                "member_subgroup_ids": sorted(subgroups.index(h) for h in orbit),
            }
        )

    subgroup_records = []
    for subgroup_id, subgroup in enumerate(subgroups):
        subgroup_records.append(
            {
                "subgroup_id": subgroup_id,
                "order": len(subgroup),
                "element_ids": sorted(subgroup),
                "generator_ids": list(generators_by_group[subgroup]),
                "mask_hex": mask_hex(subgroup_mask(subgroup), 42),
                "conjugacy_class_id": class_of[subgroup],
            }
        )

    matrix_records = [
        {
            "element_id": i,
            "columns_as_vector_ids": list(matrix),
            "rows": matrix_rows(matrix),
            "inverse_element_id": inverses[i],
        }
        for i, matrix in enumerate(matrices)
    ]

    certificate = {
        "schema": "gl32-subgroup-irreducibility-certificate-v1",
        "arithmetic": "exact F_2 bit arithmetic",
        "representation": {
            "vectors": "integers 0..7; bit i is coefficient of e_i",
            "matrices": "three image columns; composition table is left o right",
            "subgroups": "lists of IDs into group_elements",
        },
        "group": {
            "name": "GL(3,2)",
            "order": len(matrices),
            "identity_element_id": identity,
            "group_elements": matrix_records,
        },
        "subspaces": [
            {
                "dimension": len(canonical_basis(space)),
                "vector_ids": sorted(space),
                "basis_vector_ids": canonical_basis(space),
            }
            for space in subspaces
        ],
        "subgroup_enumeration": {
            "method": (
                "Breadth-first from {1}; for every discovered H and every g outside H, "
                "adjoin <H,g>. The final listed family is explicitly checked closed under "
                "all 168 adjunctions. Any subgroup K=<g1,...,gr> is therefore in the family "
                "by induction on r."
            ),
            "subgroup_count": len(subgroups),
            "counts_by_order": {
                str(order): count
                for order, count in sorted(Counter(map(len, subgroups)).items())
            },
            "discovery_nonmember_adjunctions": adjunctions,
            "saturation_checks": saturation_checks,
            "all_subgroup_axioms_verified": True,
            "all_stored_generators_regenerated_exactly": True,
            "closed_under_every_single_element_adjunction": True,
            "subgroups": subgroup_records,
        },
        "conjugacy_classification": {
            "class_count": len(conjugacy_classes),
            "partition_verified": True,
            "coverage_subgroup_count": sum(len(orbit) for _, orbit in conjugacy_classes),
            "classes": class_records,
        },
        "irreducibility": {
            "criterion": (
                "No invariant subspace of size 2 or 4; all seven subspaces of each size "
                "were tested under every representative element."
            ),
            "one_dimensional_subspaces_tested_per_class": 7,
            "two_dimensional_subspaces_tested_per_class": 7,
            "irreducible_class_ids": irreducible_classes,
            "irreducible_class_count": len(irreducible_classes),
        },
    }

    # Hash a compact mathematical core before adding the self-hash.
    core = json.dumps(certificate, sort_keys=True, separators=(",", ":")).encode()
    certificate["certificate_core_sha256"] = hashlib.sha256(core).hexdigest()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")

    print(
        json.dumps(
            {
                "group_order": 168,
                "subgroup_count": len(subgroups),
                "counts_by_order": dict(sorted(Counter(map(len, subgroups)).items())),
                "conjugacy_class_count": len(conjugacy_classes),
                "class_orders": [len(rep) for rep, _ in conjugacy_classes],
                "irreducible_class_ids": irreducible_classes,
                "irreducible_class_orders": [
                    len(conjugacy_classes[i][0]) for i in irreducible_classes
                ],
                "output": str(args.output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
