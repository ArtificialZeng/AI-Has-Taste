#!/usr/bin/env python3
"""Exact audit of every lossless reduction used by the SAT encodings."""

from __future__ import annotations

import hashlib
import json
from itertools import combinations, permutations
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SUMMARY_PATH = ROOT / "rref_hypergraph_summary.json"
EDGE_PATH = ROOT / "forbidden_triples_u8.bin"
RESULT_PATH = ROOT / "reduction_audit.json"
TARGET_ABOVE = 42_876
TARGET_EQUALITY = 35 ** 3


def rref(rows: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    work = [row for row in rows if row]
    pivot_row = 0
    for column in range(5):
        pivot = 1 << column
        found = next(
            (index for index in range(pivot_row, len(work))
             if work[index] & pivot),
            None,
        )
        if found is None:
            continue
        work[pivot_row], work[found] = work[found], work[pivot_row]
        for index in range(len(work)):
            if index != pivot_row and work[index] & pivot:
                work[index] ^= work[pivot_row]
        pivot_row += 1
        if pivot_row == len(work):
            break
    return tuple(work[:pivot_row])


def span_mask(basis: tuple[int, ...] | list[int]) -> int:
    vectors = [0]
    for row in basis:
        vectors += [vector ^ row for vector in vectors]
    return sum(1 << vector for vector in vectors)


def apply_map(vector: int, images: tuple[int, ...]) -> int:
    result = 0
    for coordinate in range(5):
        if vector & (1 << coordinate):
            result ^= images[coordinate]
    return result


def minimal_sorted_product_boundary() -> list[tuple[int, int, int]]:
    boundary = []
    for first in range(1, 156):
        for second in range(1, first + 1):
            for third in range(1, second + 1):
                if first * second * third < TARGET_ABOVE:
                    continue
                if (
                    (first - 1) * second * third < TARGET_ABOVE
                    and first * (second - 1) * third < TARGET_ABOVE
                    and first * second * (third - 1) < TARGET_ABOVE
                ):
                    boundary.append((first, second, third))
    return boundary


def main() -> None:
    summary = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
    bases = [tuple(basis) for basis in summary["rref_bases"]]
    basis_to_index = {basis: index for index, basis in enumerate(bases)}
    masks = [span_mask(basis) for basis in bases]
    assert len(bases) == len(basis_to_index) == len(set(masks)) == 155
    assert all(len(basis) == 3 and rref(basis) == basis for basis in bases)

    # Independent completeness check: every independent triple of nonzero
    # vectors reduces to one of the frozen bases, and conversely.
    independently_enumerated = sorted({
        rref(triple)
        for triple in combinations(range(1, 32), 3)
        if len(rref(triple)) == 3
    })
    assert independently_enumerated == bases

    edge_data = EDGE_PATH.read_bytes()
    assert len(edge_data) == 3 * 2_499_840
    assert hashlib.sha256(edge_data).hexdigest() == summary["edge_file_sha256"]

    # Construct, for every 3-subspace, an explicit invertible linear map that
    # takes U0=<e1,e2,e3> to it. This verifies the transitivity normalization.
    transitivity_witnesses = []
    for basis in bases:
        images = list(basis)
        for vector in range(1, 32):
            if len(rref(images + [vector])) > len(images):
                images.append(vector)
            if len(images) == 5:
                break
        assert len(rref(images)) == 5
        assert rref(tuple(apply_map(1 << i, tuple(images)) for i in range(3))) == basis
        transitivity_witnesses.append(tuple(images))
    assert len(set(transitivity_witnesses)) == 155

    u0_mask = masks[0]
    representatives: dict[int, int] = {}
    dimension_classes: dict[int, set[int]] = {1: set(), 2: set(), 3: set()}
    for index, mask in enumerate(masks):
        dimension = (u0_mask & mask).bit_count().bit_length() - 1
        dimension_classes[dimension].add(index)
        representatives.setdefault(dimension, index)
    assert representatives == {3: 0, 2: 1, 1: 13}

    # Enumerate all maps stabilizing U0. Images of e1,e2,e3 are an ordered
    # basis of U0; the quotient images of e4,e5 are an ordered basis of F_2^2;
    # their U0 components are arbitrary. Count: 168*6*8^2 = 64,512.
    u0_ordered_bases = [
        triple for triple in permutations(range(1, 8), 3)
        if len(rref(triple)) == 3
    ]
    quotient_ordered_bases = [
        (first, second)
        for first in range(1, 4)
        for second in range(1, 4)
        if first != second
    ]
    assert len(u0_ordered_bases) == 168
    assert len(quotient_ordered_bases) == 6
    stabilizer_maps = set()
    orbit_sets: dict[int, set[int]] = {1: set(), 2: set(), 3: set()}
    for u_basis in u0_ordered_bases:
        for quotient_basis in quotient_ordered_bases:
            for first_u_component in range(8):
                for second_u_component in range(8):
                    images = (
                        *u_basis,
                        first_u_component | (quotient_basis[0] << 3),
                        second_u_component | (quotient_basis[1] << 3),
                    )
                    assert len(rref(images)) == 5
                    stabilizer_maps.add(images)
                    for dimension, representative in representatives.items():
                        image_basis = rref(tuple(
                            apply_map(row, images)
                            for row in bases[representative]
                        ))
                        orbit_sets[dimension].add(basis_to_index[image_basis])
    assert len(stabilizer_maps) == 64_512
    assert orbit_sets == dimension_classes

    # Validate the exact product-threshold antichain on the complete sorted
    # cardinality cube, not merely on solver-reached values.
    boundary = minimal_sorted_product_boundary()
    assert len(boundary) == 829
    for first in range(1, 156):
        for second in range(1, first + 1):
            for third in range(1, second + 1):
                represented = any(
                    first >= a and second >= b and third >= c
                    for a, b, c in boundary
                )
                assert represented == (
                    first * second * third >= TARGET_ABOVE
                )

    equality_size_triples = [
        (first, second, third)
        for first in range(1, 156)
        for second in range(1, first + 1)
        for third in range(1, second + 1)
        if first * second * third == TARGET_EQUALITY
    ]
    assert equality_size_triples == [
        (35, 35, 35), (49, 35, 25), (125, 49, 7)
    ]

    stars = []
    for vector in range(1, 32):
        star = frozenset(
            index for index, mask in enumerate(masks)
            if mask & (1 << vector)
        )
        assert len(star) == 35
        assert all(
            masks[first] & masks[second] & masks[third] & (1 << vector)
            for first in star for second in star for third in star
        )
        stars.append(star)
    assert len(set(stars)) == 31

    result = {
        "status": "PASSED",
        "canonical_rref_subspaces": len(bases),
        "edge_file_sha256": summary["edge_file_sha256"],
        "transitivity_witnesses": len(transitivity_witnesses),
        "stabilizer_size": len(stabilizer_maps),
        "stabilizer_representatives": {
            str(dimension): representatives[dimension]
            for dimension in sorted(representatives)
        },
        "stabilizer_orbit_sizes": {
            str(dimension): len(orbit_sets[dimension])
            for dimension in sorted(orbit_sets)
        },
        "product_above_target": TARGET_ABOVE,
        "minimal_product_boundary_triples": len(boundary),
        "complete_sorted_cardinality_cube_checked": True,
        "equality_target": TARGET_EQUALITY,
        "equality_sorted_size_triples": equality_size_triples,
        "distinct_full_stars": len(stars),
        "common_star_feasibility_checked": True,
    }
    RESULT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
