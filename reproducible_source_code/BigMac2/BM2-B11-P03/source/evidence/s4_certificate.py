#!/usr/bin/env python3
"""Exact certificate for (S4/H) x (S4/H), H=< (12), (34) >.

Only integer arithmetic and fractions from Python's standard library are used.
The output is deterministic JSON and contains the complete double-coset
partition, subgroup intersections, a table-of-marks calculation, and the
power-sum cycle-index identity.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path


Permutation = tuple[int, int, int, int]
IDENTITY: Permutation = (1, 2, 3, 4)
S4: tuple[Permutation, ...] = tuple(itertools.permutations(range(1, 5)))


def compose(p: Permutation, q: Permutation) -> Permutation:
    """Return p after q."""
    return tuple(p[q[i] - 1] for i in range(4))  # type: ignore[return-value]


def inverse(p: Permutation) -> Permutation:
    ans = [0, 0, 0, 0]
    for i, image in enumerate(p, start=1):
        ans[image - 1] = i
    return tuple(ans)  # type: ignore[return-value]


def transposition(i: int, j: int) -> Permutation:
    p = list(IDENTITY)
    p[i - 1], p[j - 1] = p[j - 1], p[i - 1]
    return tuple(p)  # type: ignore[return-value]


def cycle_permutation(cycle: tuple[int, ...]) -> Permutation:
    p = list(IDENTITY)
    for a, b in zip(cycle, cycle[1:] + cycle[:1]):
        p[a - 1] = b
    return tuple(p)  # type: ignore[return-value]


def cycles(p: Permutation) -> str:
    seen: set[int] = set()
    pieces: list[str] = []
    for start in range(1, 5):
        if start in seen:
            continue
        orbit: list[int] = []
        x = start
        while x not in seen:
            seen.add(x)
            orbit.append(x)
            x = p[x - 1]
        if len(orbit) > 1:
            pieces.append("(" + "".join(map(str, orbit)) + ")")
    return "".join(pieces) if pieces else "e"


def record(p: Permutation) -> dict[str, object]:
    return {"cycles": cycles(p), "one_line": list(p)}


def generated_by(generators: tuple[Permutation, ...]) -> frozenset[Permutation]:
    group = {IDENTITY}
    changed = True
    while changed:
        changed = False
        for x in tuple(group):
            for y in generators:
                for product in (compose(x, y), compose(y, x)):
                    if product not in group:
                        group.add(product)
                        changed = True
    return frozenset(group)


def conjugate_group(g: Permutation, group: frozenset[Permutation]) -> frozenset[Permutation]:
    gi = inverse(g)
    return frozenset(compose(compose(g, h), gi) for h in group)


def double_coset(group: frozenset[Permutation], g: Permutation) -> frozenset[Permutation]:
    return frozenset(compose(compose(h1, g), h2) for h1 in group for h2 in group)


def right_cosets(group: frozenset[Permutation]) -> tuple[frozenset[Permutation], ...]:
    unseen = set(S4)
    ans: list[frozenset[Permutation]] = []
    while unseen:
        g = min(unseen)
        coset = frozenset(compose(g, h) for h in group)
        ans.append(coset)
        unseen -= coset
    return tuple(ans)


def subgroup_mark(k_group: frozenset[Permutation], l_group: frozenset[Permutation]) -> int:
    """Number of points of S4/L fixed pointwise by K."""
    count = 0
    for coset in right_cosets(l_group):
        representative = min(coset)
        if all(
            frozenset(compose(k, x) for x in coset) == coset
            for k in k_group
        ):
            # The explicit action test avoids assuming a coset convention.
            count += 1
        # Cross-check the usual containment criterion for this representative.
        ri = inverse(representative)
        criterion = all(
            compose(compose(ri, k), representative) in l_group for k in k_group
        )
        action_test = all(
            frozenset(compose(k, x) for x in coset) == coset for k in k_group
        )
        assert criterion == action_test
    return count


def determinant_fraction(matrix: list[list[int | Fraction]]) -> Fraction:
    a = [[Fraction(x) for x in row] for row in matrix]
    det = Fraction(1)
    n = len(a)
    for col in range(n):
        pivot = next((r for r in range(col, n) if a[r][col]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det *= -1
        pivot_value = a[col][col]
        det *= pivot_value
        for j in range(col, n):
            a[col][j] /= pivot_value
        for r in range(col + 1, n):
            factor = a[r][col]
            for j in range(col, n):
                a[r][j] -= factor * a[col][j]
    return det


def determinant(matrix: list[list[int]]) -> int:
    det = determinant_fraction(matrix)
    assert det.denominator == 1
    return det.numerator


def solve(matrix: list[list[int]], rhs: list[int]) -> list[Fraction]:
    n = len(matrix)
    a = [[Fraction(x) for x in row] + [Fraction(rhs[i])] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(r for r in range(col, n) if a[r][col])
        a[col], a[pivot] = a[pivot], a[col]
        pivot_value = a[col][col]
        a[col] = [x / pivot_value for x in a[col]]
        for r in range(n):
            if r == col:
                continue
            factor = a[r][col]
            a[r] = [a[r][j] - factor * a[col][j] for j in range(n + 1)]
    return [a[i][-1] for i in range(n)]


def cycle_type(p: Permutation) -> tuple[int, ...]:
    seen: set[int] = set()
    lengths: list[int] = []
    for start in range(1, 5):
        if start in seen:
            continue
        length = 0
        x = start
        while x not in seen:
            seen.add(x)
            length += 1
            x = p[x - 1]
        lengths.append(length)
    return tuple(sorted(lengths, reverse=True))


def z_value(partition: tuple[int, ...]) -> int:
    multiplicities = Counter(partition)
    ans = 1
    for part, multiplicity in multiplicities.items():
        ans *= part ** multiplicity * math.factorial(multiplicity)
    return ans


def cycle_index(group: frozenset[Permutation]) -> dict[tuple[int, ...], Fraction]:
    counts = Counter(cycle_type(h) for h in group)
    return {partition: Fraction(count, len(group)) for partition, count in counts.items()}


def kronecker_power(index: dict[tuple[int, ...], Fraction]) -> dict[tuple[int, ...], Fraction]:
    return {
        partition: coefficient * coefficient * z_value(partition)
        for partition, coefficient in index.items()
    }


def add_indices(*terms: tuple[int, dict[tuple[int, ...], Fraction]]) -> dict[tuple[int, ...], Fraction]:
    ans: dict[tuple[int, ...], Fraction] = {}
    for multiplier, index in terms:
        for partition, coefficient in index.items():
            ans[partition] = ans.get(partition, Fraction(0)) + multiplier * coefficient
    return {partition: coefficient for partition, coefficient in ans.items() if coefficient}


def fraction_string(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def serialized_index(index: dict[tuple[int, ...], Fraction]) -> dict[str, str]:
    return {
        ",".join(map(str, partition)): fraction_string(index[partition])
        for partition in sorted(index, reverse=True)
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    t12 = transposition(1, 2)
    t34 = transposition(3, 4)
    t23 = transposition(2, 3)
    block_swap = compose(transposition(1, 3), transposition(2, 4))
    h_group = generated_by((t12, t34))
    trivial = frozenset({IDENTITY})
    assert len(h_group) == 4

    representative_data = [
        ("e", IDENTITY),
        ("(23)", t23),
        ("(13)(24)", block_swap),
    ]
    cosets: list[frozenset[Permutation]] = []
    double_coset_records: list[dict[str, object]] = []
    for label, g in representative_data:
        dc = double_coset(h_group, g)
        intersection = h_group & conjugate_group(g, h_group)
        assert len(dc) == len(h_group) ** 2 // len(intersection)
        cosets.append(dc)
        double_coset_records.append(
            {
                "representative": label,
                "representative_one_line": list(g),
                "size": len(dc),
                "intersection_order": len(intersection),
                "intersection": [record(x) for x in sorted(intersection)],
                "members": [record(x) for x in sorted(dc)],
            }
        )

    assert all(cosets[i].isdisjoint(cosets[j]) for i in range(3) for j in range(i))
    assert frozenset().union(*cosets) == frozenset(S4)
    assert [len(dc) for dc in cosets] == [4, 16, 4]
    assert [len(h_group & conjugate_group(g, h_group)) for _, g in representative_data] == [4, 1, 4]

    normalizer = frozenset(g for g in S4 if conjugate_group(g, h_group) == h_group)
    assert len(normalizer) == 8
    assert cosets[0] | cosets[2] == normalizer
    assert cosets[1] == frozenset(S4) - normalizer

    basis_groups: dict[str, frozenset[Permutation]] = {
        "(4)": generated_by((cycle_permutation((1, 2, 3, 4)),)),
        "(3,1)": generated_by((cycle_permutation((1, 2, 3)),)),
        "(2,2)": h_group,
        "(2,1,1)": generated_by((t12,)),
        "(1,1,1,1)": trivial,
    }
    basis_order = list(basis_groups)
    mark_matrix = [
        [subgroup_mark(basis_groups[row], basis_groups[column]) for column in basis_order]
        for row in basis_order
    ]
    h_column = [row[basis_order.index("(2,2)")] for row in mark_matrix]
    product_marks = [value * value for value in h_column]
    coefficients = solve(mark_matrix, product_marks)
    assert coefficients == [Fraction(0), Fraction(0), Fraction(2), Fraction(0), Fraction(1)]
    mark_determinant = determinant(mark_matrix)
    assert mark_determinant != 0
    reconstructed_marks = [
        sum(Fraction(mark_matrix[i][j]) * coefficients[j] for j in range(5))
        for i in range(5)
    ]
    assert reconstructed_marks == [Fraction(x) for x in product_marks]

    h_index = cycle_index(h_group)
    trivial_index = cycle_index(trivial)
    lhs_index = kronecker_power(h_index)
    rhs_index = add_indices((2, h_index), (1, trivial_index))
    assert lhs_index == rhs_index
    power_sum_order = [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]
    basis_indices = {name: cycle_index(group) for name, group in basis_groups.items()}
    cycle_index_matrix = [
        [basis_indices[name].get(partition, Fraction(0)) for name in basis_order]
        for partition in power_sum_order
    ]
    cycle_index_determinant = determinant_fraction(cycle_index_matrix)
    assert cycle_index_determinant == Fraction(1, 24)

    certificate = {
        "schema": "s4-double-coset-certificate-v1",
        "conventions": {
            "permutation_one_line": "[g(1),g(2),g(3),g(4)]",
            "composition": "p after q",
            "H": [record(x) for x in sorted(h_group)],
        },
        "group_order": len(S4),
        "normalizer": {
            "order": len(normalizer),
            "members": [record(x) for x in sorted(normalizer)],
            "equals_union_of_representatives": ["e", "(13)(24)"],
        },
        "double_cosets": double_coset_records,
        "partition_checks": {
            "pairwise_disjoint": True,
            "union_is_S4": True,
            "sizes": [len(dc) for dc in cosets],
            "size_sum": sum(len(dc) for dc in cosets),
            "outside_normalizer_is_(23)_double_coset": True,
        },
        "orbit_stabilizers": ["H", "trivial", "H"],
        "species_decomposition": {
            "identity": "K_(2,2) x K_(2,2) = 2 K_(2,2) + K_(1,1,1,1)",
            "coefficients_in_partition_order": {
                "(4)": 0,
                "(3,1)": 0,
                "(2,2)": 2,
                "(2,1,1)": 0,
                "(1,1,1,1)": 1,
            },
        },
        "table_of_marks": {
            "row_subgroups": basis_order,
            "column_species": basis_order,
            "matrix": mark_matrix,
            "determinant": mark_determinant,
            "K_(2,2)_marks": h_column,
            "product_marks": product_marks,
            "unique_rational_solution": [fraction_string(x) for x in coefficients],
            "reconstructed_marks": [fraction_string(x) for x in reconstructed_marks],
        },
        "cycle_index": {
            "power_sum_key": "comma-separated partition of 4",
            "row_power_sums": [",".join(map(str, partition)) for partition in power_sum_order],
            "column_species": basis_order,
            "basis_coefficient_matrix": [
                [fraction_string(value) for value in row] for row in cycle_index_matrix
            ],
            "basis_coefficient_determinant": fraction_string(cycle_index_determinant),
            "integral_relation_module_among_five_basis_indices": "zero",
            "Z_H": serialized_index(h_index),
            "Z_trivial": serialized_index(trivial_index),
            "Z_H_kronecker_Z_H": serialized_index(lhs_index),
            "2Z_H_plus_Z_trivial": serialized_index(rhs_index),
            "identity_verified": True,
            "kronecker_rule": "p_lambda star p_mu = delta_(lambda,mu) z_lambda p_lambda",
        },
    }
    rendered = json.dumps(certificate, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
