#!/usr/bin/env python3
"""Exhaustively test the weak-EKR implication for certified GL(3,2) classes."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


def apply_matrix(matrix: tuple[int, int, int], vector: int) -> int:
    result = 0
    for i, column in enumerate(matrix):
        if (vector >> i) & 1:
            result ^= column
    return result


def vector_bits(vector: int) -> str:
    return format(vector, "03b")[::-1]


def matrix_rows(matrix: tuple[int, int, int]) -> list[list[int]]:
    return [[(matrix[column] >> row) & 1 for column in range(3)] for row in range(3)]


def all_subspaces() -> list[frozenset[int]]:
    spaces = []
    for mask in range(256):
        space = frozenset(v for v in range(8) if (mask >> v) & 1)
        if 0 in space and all(x ^ y in space for x in space for y in space):
            spaces.append(space)
    spaces.sort(key=lambda w: (len(w), sum(1 << v for v in w)))
    assert Counter(map(len, spaces)) == Counter({1: 1, 2: 7, 4: 7, 8: 1})
    return spaces


def canonical_basis(space: frozenset[int]) -> list[int]:
    basis = []
    generated = {0}
    for vector in sorted(space - {0}):
        if vector not in generated:
            basis.append(vector)
            generated |= {x ^ vector for x in tuple(generated)}
    assert generated == set(space)
    return basis


def difference_set(subset: frozenset[int]) -> frozenset[int]:
    return frozenset(x ^ y for x in subset for y in subset)


def subset_from_mask(mask: int) -> frozenset[int]:
    return frozenset(v for v in range(8) if (mask >> v) & 1)


def encode_vectors(vectors: frozenset[int] | list[int]) -> dict:
    values = sorted(vectors)
    return {
        "vector_ids": values,
        "vectors_bits_e0_e1_e2": [vector_bits(v) for v in values],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--subgroup-certificate", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    raw_certificate = args.subgroup_certificate.read_bytes()
    certificate = json.loads(raw_certificate)
    assert certificate["schema"] == "gl32-subgroup-irreducibility-certificate-v1"
    group = certificate["group"]
    assert group["order"] == 168
    matrices = [
        tuple(record["columns_as_vector_ids"]) for record in group["group_elements"]
    ]
    assert len(matrices) == len(set(matrices)) == 168
    subgroups = certificate["subgroup_enumeration"]["subgroups"]
    class_records = certificate["conjugacy_classification"]["classes"]
    irreducible_ids = certificate["irreducibility"]["irreducible_class_ids"]
    assert irreducible_ids == [
        record["class_id"] for record in class_records if record["irreducible"]
    ]
    assert len(irreducible_ids) == 3

    spaces = all_subspaces()
    class_results = []
    for class_id in irreducible_ids:
        class_record = class_records[class_id]
        representative = frozenset(class_record["representative_element_ids"])
        subgroup_record = subgroups[class_record["representative_subgroup_id"]]
        assert representative == frozenset(subgroup_record["element_ids"])
        generator_ids = class_record["representative_generator_ids"]

        tests = 0
        antecedent_true = 0
        violation_records = []
        violation_counts_by_dimension = Counter()
        union_data = []
        for space in spaces:
            union = frozenset(
                apply_matrix(matrices[element], vector)
                for element in representative
                for vector in space
            )
            union_data.append(
                {
                    "dimension": len(canonical_basis(space)),
                    "subspace_vector_ids": sorted(space),
                    "orbit_union_vector_ids": sorted(union),
                }
            )
            for subset_mask in range(256):
                tests += 1
                subset = subset_from_mask(subset_mask)
                differences = difference_set(subset)
                if differences <= union:
                    antecedent_true += 1
                    if len(subset) > len(space):
                        violation_counts_by_dimension[len(canonical_basis(space))] += 1
                        violation_records.append(
                            (
                                len(canonical_basis(space)),
                                sum(1 << v for v in space),
                                len(subset),
                                subset_mask,
                                space,
                                subset,
                                differences,
                                union,
                            )
                        )

        assert tests == 16 * 256 == 4096
        violation_records.sort(key=lambda item: item[:4])
        passes = not violation_records
        witness = None
        if violation_records:
            _, _, _, subset_mask, space, subset, differences, union = violation_records[0]
            basis = canonical_basis(space)
            assert differences <= union
            assert len(subset) > len(space)
            witness = {
                "W": {
                    "dimension": len(basis),
                    "basis": encode_vectors(basis),
                    **encode_vectors(space),
                },
                "A": {"subset_mask_hex": f"0x{subset_mask:02x}", **encode_vectors(subset)},
                "A_minus_A": encode_vectors(differences),
                "U_L_W": encode_vectors(union),
                "inclusion_verified": True,
                "A_cardinality": len(subset),
                "W_cardinality": len(space),
                "strict_inequality_verified": True,
            }

        class_results.append(
            {
                "class_id": class_id,
                "representative_subgroup_id": class_record["representative_subgroup_id"],
                "L_order": len(representative),
                "L_element_ids": sorted(representative),
                "L_generator_ids": generator_ids,
                "L_generators": [
                    {
                        "element_id": generator,
                        "columns_as_vector_ids": list(matrices[generator]),
                        "rows": matrix_rows(matrices[generator]),
                    }
                    for generator in generator_ids
                ],
                "irreducibility_certificate": {
                    "all_7_lines_tested": True,
                    "all_7_planes_tested": True,
                    "proper_nonzero_invariant_subspaces": [],
                },
                "weak_ekr_passes": passes,
                "pair_tests": tests,
                "antecedent_true_tests": antecedent_true,
                "violation_count": len(violation_records),
                "violation_counts_by_W_dimension": {
                    str(key): value
                    for key, value in sorted(violation_counts_by_dimension.items())
                },
                "orbit_unions_for_all_16_subspaces": union_data,
                "canonical_failure_witness": witness,
            }
        )

    assert all(not result["weak_ekr_passes"] for result in class_results)
    assert {result["L_order"] for result in class_results} == {7, 21, 168}
    output = {
        "schema": "gl32-weak-ekr-classification-certificate-v1",
        "arithmetic": "exact F_2 bit arithmetic; exhaustive finite enumeration",
        "source_sha256": hashlib.sha256(Path("source.md").read_bytes()).hexdigest(),
        "subgroup_certificate_path": str(args.subgroup_certificate),
        "subgroup_certificate_sha256": hashlib.sha256(raw_certificate).hexdigest(),
        "scope": {
            "irreducible_conjugacy_class_ids": irreducible_ids,
            "irreducible_class_orders": [result["L_order"] for result in class_results],
            "subspaces_per_class": 16,
            "subsets_per_subspace": 256,
            "pairs_per_class": 4096,
            "total_pairs": sum(result["pair_tests"] for result in class_results),
        },
        "classification": {
            "passing_class_ids": [],
            "failing_class_ids": irreducible_ids,
            "statement": (
                "There are exactly three GL(3,2)-conjugacy classes of irreducible "
                "subgroups, of orders 7, 21, and 168, and all three fail P(L)."
            ),
        },
        "class_results": class_results,
    }
    core = json.dumps(output, sort_keys=True, separators=(",", ":")).encode()
    output["certificate_core_sha256"] = hashlib.sha256(core).hexdigest()
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "classification": output["classification"],
                "total_pairs": output["scope"]["total_pairs"],
                "classes": [
                    {
                        "class_id": result["class_id"],
                        "order": result["L_order"],
                        "passes": result["weak_ekr_passes"],
                        "violations": result["violation_count"],
                        "witness": result["canonical_failure_witness"],
                    }
                    for result in class_results
                ],
                "output": str(args.output),
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
