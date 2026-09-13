#!/usr/bin/env python3
"""Exact certificate for the five-vertex-support layer of (HC4).

The program uses only Python's standard library.  It reconstructs V_4, the
384 coordinate-permutation/coordinate-complement symmetries, all 4368
five-subsets, normalized volumes by integer determinants, and the restricted
difference polynomials.  With --write it serializes every nonzero coefficient
of every affinely independent orbit representative.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from collections import Counter
from pathlib import Path


DIMENSION = 4
SUPPORT_SIZE = 5
ZERO_EXPONENT = (0,) * SUPPORT_SIZE


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


PERMUTATIONS_5 = tuple(itertools.permutations(range(5)))
PERMUTATION_SIGNS_5 = tuple(permutation_sign(p) for p in PERMUTATIONS_5)


def determinant_5(matrix: tuple[tuple[int, ...], ...]) -> int:
    """Leibniz determinant; deliberately transparent and integer-only."""
    assert len(matrix) == 5 and all(len(row) == 5 for row in matrix)
    return sum(
        sign * math.prod(matrix[row][permutation[row]] for row in range(5))
        for permutation, sign in zip(PERMUTATIONS_5, PERMUTATION_SIGNS_5)
    )


def normalized_volume(
    support: tuple[int, ...], vertices: tuple[tuple[int, ...], ...]
) -> int:
    matrix = tuple(tuple(vertices[index]) + (1,) for index in support)
    return abs(determinant_5(matrix))


def multiply_by_linear_sum(
    polynomial: dict[tuple[int, ...], int], variable_indices: tuple[int, ...]
) -> dict[tuple[int, ...], int]:
    result: dict[tuple[int, ...], int] = {}
    for exponent, coefficient in polynomial.items():
        for variable in variable_indices:
            new_exponent = list(exponent)
            new_exponent[variable] += 1
            key = tuple(new_exponent)
            result[key] = result.get(key, 0) + coefficient
    return result


def restricted_difference_coefficients(
    support: tuple[int, ...],
    vertices: tuple[tuple[int, ...], ...],
    volume: int,
) -> tuple[dict[tuple[int, ...], int], tuple[tuple[int, ...], ...]]:
    """Coefficients of Q_4 - Vol(T) prod(x_j)(sum(x_j))^3 on T."""
    points = tuple(vertices[index] for index in support)
    facet_factors = tuple(
        tuple(j for j, point in enumerate(points) if point[coordinate] == bit)
        for coordinate in range(DIMENSION)
        for bit in (0, 1)
    )
    assert all(facet_factors), "An independent support cannot miss a facet side"

    rhs = {ZERO_EXPONENT: 1}
    for factor in facet_factors:
        rhs = multiply_by_linear_sum(rhs, factor)

    sum_cubed = {ZERO_EXPONENT: 1}
    all_variables = tuple(range(SUPPORT_SIZE))
    for _ in range(3):
        sum_cubed = multiply_by_linear_sum(sum_cubed, all_variables)

    difference = dict(rhs)
    for exponent, coefficient in sum_cubed.items():
        shifted = tuple(power + 1 for power in exponent)
        difference[shifted] = difference.get(shifted, 0) - volume * coefficient

    difference = {
        exponent: coefficient
        for exponent, coefficient in difference.items()
        if coefficient != 0
    }
    return difference, facet_factors


def make_certificate() -> dict[str, object]:
    vertices = tuple(itertools.product((0, 1), repeat=DIMENSION))
    vertex_to_index = {vertex: index for index, vertex in enumerate(vertices)}

    group_maps = []
    for coordinate_permutation in itertools.permutations(range(DIMENSION)):
        for complement_mask in vertices:
            group_maps.append(
                tuple(
                    vertex_to_index[
                        tuple(
                            vertex[coordinate_permutation[j]] ^ complement_mask[j]
                            for j in range(DIMENSION)
                        )
                    ]
                    for vertex in vertices
                )
            )
    group_maps = tuple(group_maps)
    assert len(group_maps) == 384
    assert len(set(group_maps)) == 384

    def image(support: tuple[int, ...], group_map: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(sorted(group_map[index] for index in support))

    def canonical(support: tuple[int, ...]) -> tuple[int, ...]:
        return min(image(support, group_map) for group_map in group_maps)

    orbit_members: dict[tuple[int, ...], list[tuple[int, ...]]] = {}
    all_supports = tuple(itertools.combinations(range(len(vertices)), SUPPORT_SIZE))
    assert len(all_supports) == math.comb(16, 5) == 4368
    for support in all_supports:
        orbit_members.setdefault(canonical(support), []).append(support)

    assert len(orbit_members) == 27
    assert sum(len(members) for members in orbit_members.values()) == 4368

    records = []
    volume_support_counts: Counter[int] = Counter()
    orbit_size_counts: Counter[int] = Counter()
    independent_orbits = 0
    independent_supports = 0

    for orbit_number, representative in enumerate(sorted(orbit_members), start=1):
        members = orbit_members[representative]
        distinct_images = {image(representative, group_map) for group_map in group_maps}
        stabilizer_size = sum(
            image(representative, group_map) == representative
            for group_map in group_maps
        )
        assert distinct_images == set(members)
        assert len(members) * stabilizer_size == len(group_maps)

        volume = normalized_volume(representative, vertices)
        assert all(normalized_volume(member, vertices) == volume for member in members)
        volume_support_counts[volume] += len(members)
        orbit_size_counts[len(members)] += 1

        record: dict[str, object] = {
            "orbit_number": orbit_number,
            "representative_indices": list(representative),
            "representative_vertices": [
                "".join(str(bit) for bit in vertices[index]) for index in representative
            ],
            "orbit_size": len(members),
            "stabilizer_size": stabilizer_size,
            "normalized_volume": volume,
            "affinely_independent": volume > 0,
        }

        if volume > 0:
            independent_orbits += 1
            independent_supports += len(members)
            difference, facet_factors = restricted_difference_coefficients(
                representative, vertices, volume
            )
            assert difference
            assert min(difference.values()) > 0
            histogram = Counter(difference.values())
            record["facet_factor_variable_indices"] = [list(f) for f in facet_factors]
            record["difference_certificate"] = {
                "identity": (
                    "prod_{coordinate=0..3,bit=0..1} "
                    "sum_{j:v_j[coordinate]=bit} x_j "
                    "- normalized_volume*prod_j(x_j)*(sum_j(x_j))^3"
                ),
                "nonzero_term_count": len(difference),
                "minimum_coefficient": min(difference.values()),
                "maximum_coefficient": max(difference.values()),
                "coefficient_histogram": {
                    str(coefficient): count
                    for coefficient, count in sorted(histogram.items())
                },
                "coefficients": [
                    {"exponents": list(exponent), "coefficient": coefficient}
                    for exponent, coefficient in sorted(difference.items())
                ],
            }
        records.append(record)

    assert independent_orbits == 17
    assert independent_supports == 3008
    assert volume_support_counts == Counter({0: 1360, 1: 2672, 2: 320, 3: 16})
    assert orbit_size_counts == Counter({192: 13, 64: 4, 96: 4, 384: 3, 16: 2, 48: 1})

    return {
        "schema": "hc4-five-support-certificate-v1",
        "arithmetic": "exact integers only",
        "vertex_order": ["".join(str(bit) for bit in vertex) for vertex in vertices],
        "symmetry_group": {
            "description": "all coordinate permutations followed by independent coordinate complements",
            "order": len(group_maps),
        },
        "coverage": {
            "all_five_subsets": len(all_supports),
            "orbit_count": len(records),
            "independent_orbit_count": independent_orbits,
            "dependent_orbit_count": len(records) - independent_orbits,
            "independent_support_count": independent_supports,
            "dependent_support_count": len(all_supports) - independent_supports,
            "orbit_size_counts": {
                str(size): count for size, count in sorted(orbit_size_counts.items())
            },
            "normalized_volume_support_counts": {
                str(volume): count
                for volume, count in sorted(volume_support_counts.items())
            },
        },
        "result": {
            "independent_orbits_with_coefficientwise_nonnegative_difference": independent_orbits,
            "independent_orbits_with_nonzero_difference": independent_orbits,
            "negative_coefficients_found": 0,
        },
        "orbits": records,
    }


def canonical_json_bytes(certificate: dict[str, object]) -> bytes:
    return (json.dumps(certificate, indent=2, sort_keys=True) + "\n").encode("utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--write",
        type=Path,
        help="write the complete deterministic JSON certificate to this path",
    )
    parser.add_argument(
        "--check",
        type=Path,
        help="check that this file byte-for-byte equals the reconstructed certificate",
    )
    arguments = parser.parse_args()

    certificate = make_certificate()
    payload = canonical_json_bytes(certificate)
    digest = hashlib.sha256(payload).hexdigest()

    if arguments.write is not None:
        arguments.write.write_bytes(payload)
    if arguments.check is not None:
        existing = arguments.check.read_bytes()
        assert existing == payload, "stored certificate differs from exact reconstruction"

    coverage = certificate["coverage"]
    result = certificate["result"]
    print(
        json.dumps(
            {
                "certificate_sha256": digest,
                "coverage": coverage,
                "result": result,
                "status": "verified",
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
