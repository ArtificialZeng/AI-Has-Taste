#!/usr/bin/env python3
"""Independent exact replay of degree4_exact_certificate.json.

This checker deliberately does not import the producing enumerator.  It builds
row groups directly from Cartesian products of rotations (rather than generator
closure), obtains double cosets as BFS orbits for the H x L action, and solves
the cycle-index systems by the Leibniz determinant/Cramer's rule (rather than
Gaussian elimination).
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, deque
from fractions import Fraction
from itertools import permutations, product
from math import factorial
from pathlib import Path


SOURCE_SHA256 = "fd372110ceb5d92c5c134bc70354af09f46731ff1e3866c04dfe2edbb257e7bf"


def mul(a, b):
    return tuple(a[b[j]] for j in range(len(a)))


def inv(a):
    result = [None] * len(a)
    for j, value in enumerate(a):
        result[value] = j
    return tuple(result)


def partition_list(total, largest=None):
    if total == 0:
        return [()]
    largest = total if largest is None else min(total, largest)
    result = []
    for head in range(largest, 0, -1):
        for tail in partition_list(total - head, head):
            result.append((head,) + tail)
    return result


def pkey(partition):
    return ",".join(str(x) for x in partition)


def one_line(permutation):
    return "".join(str(x + 1) for x in permutation)


def parse_fraction(value):
    return Fraction(value)


def ftext(value):
    return str(value.numerator) if value.denominator == 1 else str(value)


def cycles(permutation):
    remaining = set(range(len(permutation)))
    lengths = []
    while remaining:
        start = min(remaining)
        point = start
        length = 0
        while point in remaining:
            remaining.remove(point)
            length += 1
            point = permutation[point]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def row_group_direct(alpha):
    """List every tuple of independent block rotations directly."""
    n = sum(alpha)
    blocks = []
    offset = 0
    for width in alpha:
        rotations = []
        for exponent in range(width):
            mapping = list(range(n))
            for position in range(width):
                mapping[offset + position] = offset + (position + exponent) % width
            rotations.append(tuple(mapping))
        blocks.append(rotations)
        offset += width
    result = set()
    for choices in product(*blocks):
        mapping = tuple(range(n))
        for block_rotation in choices:
            mapping = mul(block_rotation, mapping)
        result.add(mapping)
    assert len(result) == factorial(0) * product_of(alpha)
    return frozenset(result)


def product_of(values):
    answer = 1
    for value in values:
        answer *= value
    return answer


def hxk_orbits(symmetric_group, h_group, k_group):
    """Compute H\\S/K as action orbits x -> h*x*k^{-1} by BFS."""
    unseen = set(symmetric_group)
    orbits = []
    right_steps = tuple(inv(k) for k in k_group)
    while unseen:
        seed = min(unseen)
        orbit = {seed}
        queue = deque([seed])
        while queue:
            x = queue.popleft()
            for h in h_group:
                for k_inverse in right_steps:
                    y = mul(mul(h, x), k_inverse)
                    if y not in orbit:
                        orbit.add(y)
                        queue.append(y)
        unseen.difference_update(orbit)
        orbits.append(frozenset(orbit))
    assert set().union(*(set(x) for x in orbits)) == set(symmetric_group)
    assert sum(map(len, orbits)) == len(symmetric_group)
    return orbits


def stabilizer_intersection(h_group, representative, k_group):
    """Test h in r K r^-1 by membership, without constructing a conjugate set."""
    rinverse = inv(representative)
    return frozenset(
        h
        for h in h_group
        if mul(mul(rinverse, h), representative) in k_group
    )


def row_group_matches(subgroup, groups, symmetric_group):
    """Exhaust all row-group conjugacy targets and retain the first witness."""
    matches = []
    for alpha, target in groups.items():
        witness = None
        for s in symmetric_group:
            sinverse = inv(s)
            transported = frozenset(mul(mul(s, x), sinverse) for x in subgroup)
            if transported == target:
                witness = s
                break
        if witness is not None:
            matches.append({"partition": pkey(alpha), "conjugator": one_line(witness)})
    return matches


def index_vector(group, types):
    counts = Counter(cycles(x) for x in group)
    return [Fraction(counts[t], len(group)) for t in types]


def centralizer_size(partition):
    multiplicities = Counter(partition)
    return product_of(
        size**count * factorial(count) for size, count in multiplicities.items()
    )


def internal_product(left, right, types):
    return [left[j] * right[j] * centralizer_size(types[j]) for j in range(len(types))]


def permutation_sign(permutation):
    inversions = sum(
        permutation[i] > permutation[j]
        for i in range(len(permutation))
        for j in range(i + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def det_leibniz(matrix):
    n = len(matrix)
    answer = Fraction(0)
    for sigma in permutations(range(n)):
        term = Fraction(permutation_sign(sigma))
        for row in range(n):
            term *= matrix[row][sigma[row]]
        answer += term
    return answer


def cramer_solve(matrix, rhs):
    denominator = det_leibniz(matrix)
    assert denominator
    answer = []
    for column in range(len(matrix)):
        replaced = [list(row) for row in matrix]
        for row in range(len(matrix)):
            replaced[row][column] = rhs[row]
        answer.append(det_leibniz(replaced) / denominator)
    return answer


def expected_vector_json(types, vector):
    return {pkey(types[j]): ftext(vector[j]) for j in range(len(types))}


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replay(certificate_path, source_path):
    assert sha256(source_path) == SOURCE_SHA256
    certificate = json.loads(certificate_path.read_text(encoding="utf-8"))
    assert certificate["schema"] == "independent-row-k-products-exact-v1"
    assert set(certificate["degrees"]) == {"1", "2", "3", "4"}

    checked_pairs = 0
    checked_double_cosets = 0
    checked_memberships = 0
    degree_determinants = {}
    degree_nonnegative = {}

    for n in range(1, 5):
        types = partition_list(n)
        alphas = partition_list(n)
        keys = [pkey(x) for x in alphas]
        degree = certificate["degrees"][str(n)]
        assert degree["partitions"] == keys
        assert degree["power_sum_types"] == keys
        assert set(degree["ordered_pairs"]) == {
            f"{pkey(a)}|{pkey(b)}" for a in alphas for b in alphas
        }
        groups = {alpha: row_group_direct(alpha) for alpha in alphas}
        symmetric_group = tuple(permutations(range(n)))
        vectors = {alpha: index_vector(groups[alpha], types) for alpha in alphas}
        matrix = [[vectors[alpha][row] for alpha in alphas] for row in range(len(types))]
        determinant = det_leibniz(matrix)
        assert determinant
        assert ftext(determinant) == degree["basis_determinant"]
        assert degree["basis_rank"] == len(alphas)
        assert degree["basis_matrix_rows_types_cols_partitions"] == [
            [ftext(value) for value in row] for row in matrix
        ]
        for alpha in alphas:
            assert degree["group_orders"][pkey(alpha)] == len(groups[alpha])
            assert degree["basis_cycle_indices"][pkey(alpha)] == expected_vector_json(
                types, vectors[alpha]
            )

        every_nonnegative = True
        negative_pair_keys = []
        for alpha in alphas:
            for beta in alphas:
                checked_pairs += 1
                pair_key = f"{pkey(alpha)}|{pkey(beta)}"
                record = degree["ordered_pairs"][pair_key]
                independent_orbits = hxk_orbits(
                    symmetric_group, groups[alpha], groups[beta]
                )
                stored_orbits = record["double_cosets"]
                assert len(independent_orbits) == len(stored_orbits)
                orbit_index_sum = [Fraction(0) for _ in types]
                orbit_basis_counts = Counter()
                all_orbits_unique_row_groups = True
                for orbit, stored in zip(independent_orbits, stored_orbits):
                    checked_double_cosets += 1
                    checked_memberships += len(orbit)
                    representative = min(orbit)
                    assert stored["representative"] == one_line(representative)
                    assert stored["elements"] == [one_line(x) for x in sorted(orbit)]
                    assert stored["size"] == len(orbit)
                    intersection = stabilizer_intersection(
                        groups[alpha], representative, groups[beta]
                    )
                    assert len(orbit) * len(intersection) == len(groups[alpha]) * len(groups[beta])
                    assert stored["intersection_order"] == len(intersection)
                    assert stored["intersection_elements"] == [
                        one_line(x) for x in sorted(intersection)
                    ]
                    counts = Counter(cycles(x) for x in intersection)
                    assert stored["intersection_cycle_counts"] == {
                        pkey(t): counts[t] for t in types if counts[t]
                    }
                    matches = row_group_matches(intersection, groups, symmetric_group)
                    assert stored["independent_row_conjugacy_matches"] == matches
                    if len(matches) == 1:
                        orbit_basis_counts[matches[0]["partition"]] += 1
                    else:
                        all_orbits_unique_row_groups = False
                    ivector = index_vector(intersection, types)
                    orbit_index_sum = [
                        orbit_index_sum[j] + ivector[j] for j in range(len(types))
                    ]

                product_vector = internal_product(vectors[alpha], vectors[beta], types)
                assert orbit_index_sum == product_vector
                assert record["product_cycle_index"] == expected_vector_json(types, product_vector)
                assert record["orbit_sum_cycle_index"] == expected_vector_json(types, orbit_index_sum)
                expansion = cramer_solve(matrix, product_vector)
                stored_expansion = {
                    key: ftext(expansion[j]) for j, key in enumerate(keys)
                }
                assert record["basis_expansion"] == stored_expansion
                nonnegative = all(x.denominator == 1 and x >= 0 for x in expansion)
                assert record["nonnegative_integral"] is nonnegative
                assert (
                    record["all_orbits_are_unique_independent_row_groups"]
                    is all_orbits_unique_row_groups
                )
                expected_orbit_multiplicities = (
                    {key: orbit_basis_counts[key] for key in keys}
                    if all_orbits_unique_row_groups
                    else None
                )
                assert record["orbit_basis_multiplicities"] == expected_orbit_multiplicities
                if n <= 3:
                    assert all_orbits_unique_row_groups
                    assert expansion == [Fraction(orbit_basis_counts[key]) for key in keys]
                every_nonnegative &= nonnegative
                if any(x < 0 for x in expansion):
                    negative_pair_keys.append(pair_key)
        assert checked_pairs >= degree["ordered_pair_count"]
        assert every_nonnegative is degree["all_expansions_nonnegative_integral"]
        assert negative_pair_keys == degree["pairs_with_negative_coefficient"]
        degree_determinants[str(n)] = ftext(determinant)
        degree_nonnegative[str(n)] = every_nonnegative

    target = certificate["degrees"]["4"]["ordered_pairs"]["2,2|4"]
    assert target["basis_expansion"] == {
        "4": "0", "3,1": "0", "2,2": "2", "2,1,1": "-2", "1,1,1,1": "2"
    }
    assert target["double_cosets"][0]["independent_row_conjugacy_matches"] == [
        {"partition": "1,1,1,1", "conjugator": "1234"}
    ]
    assert target["double_cosets"][1]["independent_row_conjugacy_matches"] == []
    assert checked_pairs == 39
    assert all(degree_nonnegative[str(n)] for n in range(1, 4))
    assert not degree_nonnegative["4"]
    return {
        "schema": "independent-row-k-products-replay-v1",
        "status": "passed",
        "source_sha256": SOURCE_SHA256,
        "certificate_sha256": sha256(certificate_path),
        "replay_script_sha256": sha256(Path(__file__)),
        "independence": [
            "row groups generated by Cartesian products of rotations",
            "double cosets recomputed as H x L action orbits by BFS",
            "basis solutions recomputed by Leibniz determinants and Cramer's rule",
            "producer module was not imported",
        ],
        "basis_determinants_degrees_1_to_4": degree_determinants,
        "ordered_pairs_replayed": checked_pairs,
        "double_cosets_replayed": checked_double_cosets,
        "double_coset_element_memberships_replayed": checked_memberships,
        "all_pairs_degrees_1_to_3_nonnegative_integral": True,
        "all_low_degree_orbits_identified_as_row_group_species": True,
        "degree_4_negative_ordered_pairs": ["4|2,2", "2,2|4"],
        "target_double_transposition_stabilizer_has_no_row_group_conjugate": True,
        "target_expansion": target["basis_expansion"],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--source", type=Path, default=Path("source.md"))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = replay(args.certificate, args.source)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
