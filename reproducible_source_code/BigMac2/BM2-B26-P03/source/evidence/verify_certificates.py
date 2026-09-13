#!/usr/bin/env python3
"""Standalone exact verifier for the GL(3,2) research certificates.

This file intentionally does not import either certificate-generating script.
It reconstructs the group table, subgroup closure, conjugacy orbits,
irreducibility tests, and all weak-EKR tests from the serialized records.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, deque
from pathlib import Path


def act(columns: tuple[int, int, int], vector: int) -> int:
    return (columns[0] if vector & 1 else 0) ^ (columns[1] if vector & 2 else 0) ^ (
        columns[2] if vector & 4 else 0
    )


def compose(a: tuple[int, int, int], b: tuple[int, int, int]):
    return tuple(act(a, column) for column in b)


def invertible(columns: tuple[int, int, int]) -> bool:
    return len({act(columns, vector) for vector in range(8)}) == 8


def all_spaces():
    result = []
    for bits in range(256):
        members = frozenset(v for v in range(8) if bits & (1 << v))
        if 0 in members and all(x ^ y in members for x in members for y in members):
            result.append(members)
    return sorted(result, key=lambda w: (len(w), tuple(sorted(w))))


def generated(seed, step_ids, product, inverse, identity):
    steps = set(step_ids)
    steps |= {inverse[x] for x in tuple(steps)}
    found = set(seed)
    found.add(identity)
    queue = deque(found)
    while queue:
        x = queue.popleft()
        for step in steps:
            for y in (product[x][step], product[step][x]):
                if y not in found:
                    found.add(y)
                    queue.append(y)
    return frozenset(found)


def difference(members):
    return frozenset(x ^ y for x in members for y in members)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--subgroups", type=Path, required=True)
    parser.add_argument("--weak-ekr", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    subgroup_raw = args.subgroups.read_bytes()
    weak_raw = args.weak_ekr.read_bytes()
    cert = json.loads(subgroup_raw)
    weak = json.loads(weak_raw)

    matrices = [
        tuple(item["columns_as_vector_ids"])
        for item in cert["group"]["group_elements"]
    ]
    expected_matrices = {
        (a, b, c)
        for a in range(8)
        for b in range(8)
        for c in range(8)
        if invertible((a, b, c))
    }
    assert len(expected_matrices) == 168
    assert set(matrices) == expected_matrices
    position = {matrix: i for i, matrix in enumerate(matrices)}
    product = [[position[compose(a, b)] for b in matrices] for a in matrices]
    identity = position[(1, 2, 4)]
    inverse = []
    for x in range(168):
        choices = [
            y
            for y in range(168)
            if product[x][y] == identity == product[y][x]
        ]
        assert len(choices) == 1
        inverse.append(choices[0])

    subgroup_records = cert["subgroup_enumeration"]["subgroups"]
    subgroups = [frozenset(item["element_ids"]) for item in subgroup_records]
    assert len(subgroups) == len(set(subgroups)) == 179
    assert Counter(map(len, subgroups)) == Counter(
        {1: 1, 2: 21, 3: 28, 4: 35, 6: 28, 7: 8, 8: 21, 12: 14, 21: 8, 24: 14, 168: 1}
    )
    subgroup_lookup = {group: i for i, group in enumerate(subgroups)}
    direct_product_checks = 0
    for record, subgroup in zip(subgroup_records, subgroups):
        assert identity in subgroup
        assert all(inverse[x] in subgroup for x in subgroup)
        for x in subgroup:
            for y in subgroup:
                direct_product_checks += 1
                assert product[x][y] in subgroup
        regenerated = generated({identity}, record["generator_ids"], product, inverse, identity)
        assert regenerated == subgroup

    saturation_checks = 0
    for subgroup in subgroups:
        for g in range(168):
            saturation_checks += 1
            # Use every element of H as a step, rather than trusting the stored
            # generator list, so this saturation check is independent of it.
            overgroup = generated(
                subgroup, set(subgroup) | {g}, product, inverse, identity
            )
            assert overgroup in subgroup_lookup
    assert saturation_checks == 179 * 168 == 30072

    class_records = cert["conjugacy_classification"]["classes"]
    assert len(class_records) == 15
    seen = set()
    computed_irreducible_ids = []
    spaces = all_spaces()
    assert Counter(map(len, spaces)) == Counter({1: 1, 2: 7, 4: 7, 8: 1})
    conjugacy_checks = 0
    for class_record in class_records:
        class_id = class_record["class_id"]
        representative = frozenset(class_record["representative_element_ids"])
        computed_orbit = set()
        for g in range(168):
            conjugacy_checks += len(representative)
            conjugate = frozenset(
                product[product[inverse[g]][x]][g] for x in representative
            )
            assert conjugate in subgroup_lookup
            computed_orbit.add(subgroup_lookup[conjugate])
        assert computed_orbit == set(class_record["member_subgroup_ids"])
        assert len(computed_orbit) == class_record["orbit_size"]
        assert not (seen & computed_orbit)
        seen |= computed_orbit

        invariant = []
        for space in spaces:
            if len(space) not in (2, 4):
                continue
            if all(
                frozenset(act(matrices[x], v) for v in space) == space
                for x in representative
            ):
                invariant.append(space)
        stored_invariant = {
            frozenset(item["vector_ids"])
            for item in class_record["invariant_proper_nonzero_subspaces"]
        }
        assert set(invariant) == stored_invariant
        assert class_record["irreducible"] == (not invariant)
        if not invariant:
            computed_irreducible_ids.append(class_id)
    assert seen == set(range(179))
    assert computed_irreducible_ids == [7, 11, 14]

    weak_results = {item["class_id"]: item for item in weak["class_results"]}
    assert set(weak_results) == set(computed_irreducible_ids)
    total_pair_checks = 0
    weak_summary = []
    for class_id in computed_irreducible_ids:
        class_record = class_records[class_id]
        subgroup = frozenset(class_record["representative_element_ids"])
        violations = 0
        antecedents = 0
        by_dimension = Counter()
        for space in spaces:
            union = frozenset(
                act(matrices[x], v) for x in subgroup for v in space
            )
            dimension = {1: 0, 2: 1, 4: 2, 8: 3}[len(space)]
            for bits in range(256):
                total_pair_checks += 1
                subset = frozenset(v for v in range(8) if bits & (1 << v))
                if difference(subset) <= union:
                    antecedents += 1
                    if len(subset) > len(space):
                        violations += 1
                        by_dimension[dimension] += 1
        stored = weak_results[class_id]
        assert stored["pair_tests"] == 4096
        assert stored["antecedent_true_tests"] == antecedents
        assert stored["violation_count"] == violations
        assert stored["violation_counts_by_W_dimension"] == {
            str(key): value for key, value in sorted(by_dimension.items())
        }
        assert stored["weak_ekr_passes"] == (violations == 0)
        witness = stored["canonical_failure_witness"]
        W = frozenset(witness["W"]["vector_ids"])
        A = frozenset(witness["A"]["vector_ids"])
        U = frozenset(act(matrices[x], v) for x in subgroup for v in W)
        assert difference(A) <= U and len(A) > len(W)
        assert set(witness["A_minus_A"]["vector_ids"]) == set(difference(A))
        assert set(witness["U_L_W"]["vector_ids"]) == set(U)
        weak_summary.append(
            {
                "class_id": class_id,
                "order": len(subgroup),
                "antecedent_true_tests": antecedents,
                "violations": violations,
                "witness_verified": True,
            }
        )
    assert total_pair_checks == 3 * 16 * 256 == 12288
    assert all(item["violations"] > 0 for item in weak_summary)

    report = {
        "schema": "gl32-independent-verification-v1",
        "verifier_independence": (
            "Standalone implementation; imports neither generating script and "
            "reconstructs the matrix group and every tested relation from JSON."
        ),
        "inputs": {
            str(args.subgroups): hashlib.sha256(subgroup_raw).hexdigest(),
            str(args.weak_ekr): hashlib.sha256(weak_raw).hexdigest(),
            "source.md": hashlib.sha256(Path("source.md").read_bytes()).hexdigest(),
        },
        "checks": {
            "all_168_invertible_matrices_reconstructed": True,
            "subgroup_count": len(subgroups),
            "subgroup_direct_product_checks": direct_product_checks,
            "subgroup_single_adjunction_saturation_checks": saturation_checks,
            "conjugacy_class_count": len(class_records),
            "conjugacy_element_checks": conjugacy_checks,
            "subgroup_partition_coverage": len(seen),
            "irreducible_class_ids": computed_irreducible_ids,
            "weak_ekr_pair_checks": total_pair_checks,
            "weak_ekr_summary": weak_summary,
            "all_checks_passed": True,
        },
    }
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["checks"], sort_keys=True))


if __name__ == "__main__":
    main()
