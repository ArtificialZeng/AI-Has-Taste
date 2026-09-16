#!/usr/bin/env python3
"""Exact exhaustive certificate for independent-row K-products through degree 4.

No external package is used.  Permutations are image tuples and all linear
algebra is over fractions.Fraction.  The emitted JSON records every element of
every double coset, its stabilizer intersection, each cycle-index vector, and
the unique expansion in the independent-row K-basis.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import factorial
from pathlib import Path


def compose(p, q):
    """Return p after q."""
    return tuple(p[q[i]] for i in range(len(p)))


def inverse(p):
    ans = [0] * len(p)
    for i, image in enumerate(p):
        ans[image] = i
    return tuple(ans)


def identity(n):
    return tuple(range(n))


def partitions(n, ceiling=None):
    if n == 0:
        yield ()
        return
    if ceiling is None or ceiling > n:
        ceiling = n
    for first in range(ceiling, 0, -1):
        for tail in partitions(n - first, first):
            yield (first,) + tail


def cycle_type(p):
    seen = [False] * len(p)
    parts = []
    for start in range(len(p)):
        if not seen[start]:
            cur = start
            length = 0
            while not seen[cur]:
                seen[cur] = True
                length += 1
                cur = p[cur]
            parts.append(length)
    return tuple(sorted(parts, reverse=True))


def independent_row_group(alpha):
    """Construct the direct product of cycles on consecutive row blocks."""
    n = sum(alpha)
    generators = []
    offset = 0
    for part in alpha:
        if part > 1:
            g = list(range(n))
            for j in range(part):
                g[offset + j] = offset + (j + 1) % part
            generators.append(tuple(g))
        offset += part

    group = {identity(n)}
    frontier = [identity(n)]
    while frontier:
        x = frontier.pop()
        for g in generators:
            y = compose(x, g)
            if y not in group:
                group.add(y)
                frontier.append(y)
    expected_order = 1
    for part in alpha:
        expected_order *= part
    assert len(group) == expected_order
    return frozenset(group)


def conjugate_group(r, subgroup):
    rinv = inverse(r)
    return frozenset(compose(compose(r, x), rinv) for x in subgroup)


def frac_text(q):
    return str(q.numerator) if q.denominator == 1 else f"{q.numerator}/{q.denominator}"


def perm_text(p):
    return "".join(str(x + 1) for x in p)


def part_text(alpha):
    return ",".join(map(str, alpha))


def vector_json(types, vector, omit_zero=False):
    return {
        part_text(t): frac_text(vector[t])
        for t in types
        if not omit_zero or vector[t]
    }


def cycle_index(subgroup, types):
    counts = Counter(cycle_type(x) for x in subgroup)
    return {t: Fraction(counts[t], len(subgroup)) for t in types}


def z_value(alpha):
    counts = Counter(alpha)
    ans = 1
    for size, multiplicity in counts.items():
        ans *= size**multiplicity * factorial(multiplicity)
    return ans


def star(left, right, types):
    return {t: left[t] * right[t] * z_value(t) for t in types}


def rank(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        scale = a[pivot_row][col]
        a[pivot_row] = [x / scale for x in a[pivot_row]]
        for r in range(rows):
            if r != pivot_row and a[r][col]:
                scale = a[r][col]
                a[r] = [a[r][c] - scale * a[pivot_row][c] for c in range(cols)]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    n = len(a)
    ans = Fraction(1)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            ans = -ans
        pivot_value = a[col][col]
        ans *= pivot_value
        for r in range(col + 1, n):
            if a[r][col]:
                scale = a[r][col] / pivot_value
                for c in range(col + 1, n):
                    a[r][c] -= scale * a[col][c]
    return ans


def solve_square(matrix, rhs):
    n = len(matrix)
    aug = [
        [Fraction(matrix[r][c]) for c in range(n)] + [Fraction(rhs[r])]
        for r in range(n)
    ]
    for col in range(n):
        pivot = next((r for r in range(col, n) if aug[r][col]), None)
        assert pivot is not None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x / scale for x in aug[col]]
        for r in range(n):
            if r != col and aug[r][col]:
                scale = aug[r][col]
                aug[r] = [aug[r][c] - scale * aug[col][c] for c in range(n + 1)]
    return [aug[r][-1] for r in range(n)]


def enumerate_double_cosets(full_group, left, right):
    unseen = set(full_group)
    answer = []
    while unseen:
        representative = min(unseen)
        elements = frozenset(
            compose(compose(h, representative), ell)
            for h in left
            for ell in right
        )
        assert representative in elements
        assert elements <= unseen
        unseen.difference_update(elements)
        intersection = left & conjugate_group(representative, right)
        assert len(elements) * len(intersection) == len(left) * len(right)
        answer.append((representative, elements, intersection))
    assert sum(len(elements) for _, elements, _ in answer) == len(full_group)
    assert set().union(*(set(elements) for _, elements, _ in answer)) == set(full_group)
    return answer


def row_group_conjugacy_matches(subgroup, groups, full_group):
    """Return every K-basis stabilizer conjugate to subgroup, with a witness."""
    matches = []
    for alpha, row_group in groups.items():
        conjugator = next(
            (
                s
                for s in full_group
                if conjugate_group(s, subgroup) == row_group
            ),
            None,
        )
        if conjugator is not None:
            matches.append(
                {
                    "partition": part_text(alpha),
                    "conjugator": perm_text(conjugator),
                }
            )
    return matches


def make_certificate():
    certificate = {
        "schema": "independent-row-k-products-exact-v1",
        "arithmetic": "integer permutation enumeration and fractions.Fraction only",
        "permutation_convention": "one-line images, composition p_after_q",
        "degrees": {},
    }
    total_pairs = 0
    for n in range(1, 5):
        parts = list(partitions(n))
        types = list(partitions(n))
        full_group = tuple(permutations(range(n)))
        groups = {alpha: independent_row_group(alpha) for alpha in parts}
        indices = {alpha: cycle_index(groups[alpha], types) for alpha in parts}
        basis_matrix = [[indices[alpha][t] for alpha in parts] for t in types]
        basis_rank = rank(basis_matrix)
        basis_det = determinant(basis_matrix)
        assert basis_rank == len(parts) and basis_det

        degree = {
            "partitions": [part_text(x) for x in parts],
            "power_sum_types": [part_text(x) for x in types],
            "group_orders": {part_text(x): len(groups[x]) for x in parts},
            "basis_cycle_indices": {
                part_text(alpha): vector_json(types, indices[alpha]) for alpha in parts
            },
            "basis_matrix_rows_types_cols_partitions": [
                [frac_text(x) for x in row] for row in basis_matrix
            ],
            "basis_rank": basis_rank,
            "basis_determinant": frac_text(basis_det),
            "ordered_pairs": {},
        }

        all_nonnegative_integral = True
        negative_pairs = []
        for alpha in parts:
            for beta in parts:
                total_pairs += 1
                double_cosets = enumerate_double_cosets(
                    full_group, groups[alpha], groups[beta]
                )
                direct = star(indices[alpha], indices[beta], types)
                orbit_sum = {t: Fraction(0) for t in types}
                orbit_records = []
                orbit_basis_counts = Counter()
                all_orbits_are_unique_row_groups = True
                for representative, elements, intersection in double_cosets:
                    orbit_index = cycle_index(intersection, types)
                    orbit_sum = {t: orbit_sum[t] + orbit_index[t] for t in types}
                    type_counts = Counter(cycle_type(x) for x in intersection)
                    conjugacy_matches = row_group_conjugacy_matches(
                        intersection, groups, full_group
                    )
                    if len(conjugacy_matches) == 1:
                        orbit_basis_counts[conjugacy_matches[0]["partition"]] += 1
                    else:
                        all_orbits_are_unique_row_groups = False
                    orbit_records.append(
                        {
                            "representative": perm_text(representative),
                            "elements": [perm_text(x) for x in sorted(elements)],
                            "size": len(elements),
                            "intersection_order": len(intersection),
                            "intersection_elements": [
                                perm_text(x) for x in sorted(intersection)
                            ],
                            "intersection_cycle_counts": {
                                part_text(t): type_counts[t]
                                for t in types
                                if type_counts[t]
                            },
                            "independent_row_conjugacy_matches": conjugacy_matches,
                        }
                    )
                assert orbit_sum == direct
                rhs = [direct[t] for t in types]
                expansion = solve_square(basis_matrix, rhs)
                reconstructed = [
                    sum(basis_matrix[row][col] * expansion[col] for col in range(len(parts)))
                    for row in range(len(types))
                ]
                assert reconstructed == rhs
                nonnegative_integral = all(
                    x.denominator == 1 and x.numerator >= 0 for x in expansion
                )
                all_nonnegative_integral &= nonnegative_integral
                if any(x < 0 for x in expansion):
                    negative_pairs.append(f"{part_text(alpha)}|{part_text(beta)}")
                key = f"{part_text(alpha)}|{part_text(beta)}"
                degree["ordered_pairs"][key] = {
                    "double_cosets": orbit_records,
                    "product_cycle_index": vector_json(types, direct),
                    "orbit_sum_cycle_index": vector_json(types, orbit_sum),
                    "basis_expansion": {
                        part_text(parts[j]): frac_text(expansion[j])
                        for j in range(len(parts))
                    },
                    "nonnegative_integral": nonnegative_integral,
                    "all_orbits_are_unique_independent_row_groups": (
                        all_orbits_are_unique_row_groups
                    ),
                    "orbit_basis_multiplicities": (
                        {
                            part_text(gamma): orbit_basis_counts[part_text(gamma)]
                            for gamma in parts
                        }
                        if all_orbits_are_unique_row_groups
                        else None
                    ),
                }
                if n <= 3:
                    assert all_orbits_are_unique_row_groups
                    assert expansion == [
                        Fraction(orbit_basis_counts[part_text(gamma)])
                        for gamma in parts
                    ]
        degree["ordered_pair_count"] = len(parts) ** 2
        degree["all_expansions_nonnegative_integral"] = all_nonnegative_integral
        degree["pairs_with_negative_coefficient"] = negative_pairs
        certificate["degrees"][str(n)] = degree

    # Frozen target checks, including the named representatives e and (23).
    target = certificate["degrees"]["4"]["ordered_pairs"]["2,2|4"]
    assert target["basis_expansion"] == {
        "4": "0",
        "3,1": "0",
        "2,2": "2",
        "2,1,1": "-2",
        "1,1,1,1": "2",
    }
    assert target["product_cycle_index"] == {
        "4": "0",
        "3,1": "0",
        "2,2": "1/2",
        "2,1,1": "0",
        "1,1,1,1": "3/2",
    }
    assert [x["representative"] for x in target["double_cosets"]] == ["1234", "1324"]
    assert [x["size"] for x in target["double_cosets"]] == [16, 8]
    assert [x["intersection_order"] for x in target["double_cosets"]] == [1, 2]
    assert target["double_cosets"][1]["intersection_cycle_counts"] == {
        "2,2": 1,
        "1,1,1,1": 1,
    }
    assert target["double_cosets"][0]["independent_row_conjugacy_matches"] == [
        {"partition": "1,1,1,1", "conjugator": "1234"}
    ]
    assert target["double_cosets"][1]["independent_row_conjugacy_matches"] == []
    assert not target["all_orbits_are_unique_independent_row_groups"]
    assert target["orbit_basis_multiplicities"] is None
    assert all(
        certificate["degrees"][str(n)]["all_expansions_nonnegative_integral"]
        for n in range(1, 4)
    )
    certificate["summary"] = {
        "degrees_checked": [1, 2, 3, 4],
        "ordered_partition_pairs_checked": total_pairs,
        "all_double_cosets_explicitly_partition_the_symmetric_group": True,
        "all_orbit_sums_equal_internal_products": True,
        "all_basis_ranks_full": True,
        "all_pairs_degrees_1_to_3_nonnegative_integral": True,
        "all_low_degree_orbit_stabilizers_conjugate_to_unique_row_groups": True,
        "target_expansion": "2 K_(2,2) - 2 K_(2,1,1) + 2 K_(1,1,1,1)",
        "target_species_orbits": "K_(1,1,1,1) plus X^4/<(12)(34)>",
        "target_double_transposition_stabilizer_is_not_a_row_group": True,
        "target_has_nonnegative_integral_expansion": False,
        "degree_four_is_first_failure": True,
    }
    return certificate


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    certificate = make_certificate()
    rendered = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    print(json.dumps(certificate["summary"], sort_keys=True))


if __name__ == "__main__":
    main()
