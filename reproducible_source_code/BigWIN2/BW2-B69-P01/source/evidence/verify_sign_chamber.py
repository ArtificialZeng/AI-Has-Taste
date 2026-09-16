#!/usr/bin/env python3
"""Exact finite audit beyond the 18 primitive triangular rays.

This script works in the balanced lattice, enumerates all full-dimensional
coordinate-sign chambers by exact linear rational arithmetic, constructs one
closed chamber adjacent to rho_(002;1), and tests sparse polynomial supports.
The only nonstandard dependencies are SymPy and z3-solver.
"""

from __future__ import annotations

import itertools
import json
import math

import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ
from sympy.polys.matrices import DomainMatrix
from z3 import Bool, BoolVal, If, Or, Real, Solver, Sum, is_true, sat

from verify_triangular_rays import (
    H2,
    H4,
    H4_INDEX,
    P,
    add,
    alpha_label,
    unit,
)


def triangular_rays():
    rays = []
    names = []
    for beta in H2:
        for i in range(3):
            j, k = tuple(column for column in range(3) if column != i)
            gamma = [0] * len(H4)
            for alpha in (
                add(beta, unit(i), unit(i)),
                add(beta, unit(j), unit(k)),
            ):
                gamma[H4_INDEX[alpha]] += 1
            for alpha in (
                add(beta, unit(i), unit(j)),
                add(beta, unit(i), unit(k)),
            ):
                gamma[H4_INDEX[alpha]] -= 1
            rays.append(tuple(gamma))
            names.append(f"rho_({alpha_label(beta)};{i + 1})")
    return tuple(rays), tuple(names)


def dot(left, right):
    return sum(a * b for a, b in zip(left, right))


def primitive_integer(vector):
    denominators = [sp.denom(entry) for entry in vector]
    common_denominator = sp.ilcm(*denominators)
    integers = [int(entry * common_denominator) for entry in vector]
    divisor = math.gcd(*(abs(entry) for entry in integers))
    return tuple(entry // divisor for entry in integers)


def exact_rank(rows, width=12):
    if not rows:
        return 0
    return DomainMatrix.from_list_sympy(
        len(rows), width, [list(row) for row in rows]
    ).rank()


def enumerate_facets(ray_coordinates):
    """Enumerate all facets of a 12-cone from its 18 rays, exactly.

    Every facet contains 11 linearly independent rays.  Thus checking all
    11-subsets is a complete finite enumeration, not a floating-point hull.
    """
    facets = set()
    for indices in itertools.combinations(range(len(ray_coordinates)), 11):
        rows = [ray_coordinates[index] for index in indices]
        matrix = DomainMatrix.from_list_sympy(11, 12, rows)
        if matrix.rank() != 11:
            continue
        nullspace = matrix.to_field().nullspace().to_Matrix()
        assert nullspace.rows == 1
        normal = primitive_integer(list(nullspace.row(0)))
        values = [dot(normal, ray) for ray in ray_coordinates]
        if all(value <= 0 for value in values):
            normal = tuple(-entry for entry in normal)
            values = [-value for value in values]
        if all(value >= 0 for value in values):
            facets.add(normal)
    return tuple(sorted(facets))


def cut_cone(rays, inequalities, new_inequality):
    """One exact double-description cut, using the rank-10 edge test."""
    values = {ray: dot(new_inequality, ray) for ray in rays}
    kept = [ray for ray in rays if values[ray] >= 0]
    positive = [ray for ray in rays if values[ray] > 0]
    negative = [ray for ray in rays if values[ray] < 0]
    active = {
        ray: frozenset(
            index
            for index, inequality in enumerate(inequalities)
            if dot(inequality, ray) == 0
        )
        for ray in rays
    }
    rank_cache = {}
    new_rays = []
    for positive_ray in positive:
        for negative_ray in negative:
            common = tuple(sorted(active[positive_ray] & active[negative_ray]))
            if common not in rank_cache:
                rank_cache[common] = exact_rank(
                    [inequalities[index] for index in common]
                )
            if rank_cache[common] != 10:
                continue
            positive_value = values[positive_ray]
            negative_value = values[negative_ray]
            intersection = primitive_integer(
                [
                    (-negative_value) * a + positive_value * b
                    for a, b in zip(positive_ray, negative_ray)
                ]
            )
            assert dot(new_inequality, intersection) == 0
            new_rays.append(intersection)
    output = tuple(sorted(set(kept + new_rays)))
    output_inequalities = inequalities + (tuple(new_inequality),)
    assert all(
        dot(inequality, ray) >= 0
        for ray in output
        for inequality in output_inequalities
    )
    return output, output_inequalities


def enumerate_full_dimensional_sign_patterns(rays):
    """Enumerate strict orthants meeting relint(C), using exact SMT-LRA."""
    coefficients = [Real(f"lambda_{index}") for index in range(len(rays))]
    signs = [Bool(f"positive_{index}") for index in range(len(H4))]
    solver = Solver()
    solver.add(*(coefficient >= 1 for coefficient in coefficients))
    gamma = [
        Sum(
            *[
                rays[ray_index][coordinate] * coefficients[ray_index]
                for ray_index in range(len(rays))
            ]
        )
        for coordinate in range(len(H4))
    ]
    solver.add(
        *[
            If(signs[index], gamma[index] >= 1, gamma[index] <= -1)
            for index in range(len(H4))
        ]
    )

    patterns = []
    while solver.check() == sat:
        model = solver.model()
        pattern = tuple(
            is_true(model.eval(sign, model_completion=True)) for sign in signs
        )
        patterns.append(pattern)
        solver.add(
            Or(
                *[
                    sign != BoolVal(pattern[index])
                    for index, sign in enumerate(signs)
                ]
            )
        )
    return tuple(patterns)


def compressed_base_supports():
    # Every product of t coefficient polynomials has row sum t.  Retaining
    # columns 1 and 2 in each row is therefore injective: column 3 is forced.
    return tuple(
        {
            tuple(monomial[3 * row + column] for row in range(4) for column in range(2))
            for monomial in P[alpha]
        }
        for alpha in H4
    )


BASE_SUPPORTS = compressed_base_supports()


def product_support(exponents, cache):
    key = tuple(exponents)
    if key in cache:
        return cache[key]
    support = {(0,) * 8}
    factors = []
    for index, exponent in enumerate(exponents):
        factors.extend([index] * exponent)
    factors.sort(key=lambda index: len(BASE_SUPPORTS[index]))
    for index in factors:
        support = {
            tuple(a + b for a, b in zip(left, right))
            for left in support
            for right in BASE_SUPPORTS[index]
        }
    cache[key] = support
    return support


def support_audit(gammas):
    cache = {}
    records = []
    for gamma in gammas:
        positive = tuple(max(entry, 0) for entry in gamma)
        negative = tuple(max(-entry, 0) for entry in gamma)
        assert sum(positive) == sum(negative)
        numerator = product_support(positive, cache)
        denominator = product_support(negative, cache)
        missing = numerator - denominator
        records.append(
            {
                "gamma": list(gamma),
                "positive_degree": sum(positive),
                "numerator_support_size": len(numerator),
                "denominator_support_size": len(denominator),
                "missing_count": len(missing),
            }
        )
    return records


def main():
    rays, names = triangular_rays()
    ray_matrix = sp.Matrix(rays).T
    balance_matrix = sp.Matrix([[alpha[i] for alpha in H4] for i in range(3)])
    assert balance_matrix.rank() == 3
    assert ray_matrix.rank() == 12
    assert balance_matrix * ray_matrix == sp.zeros(3, 18)

    smith = smith_normal_form(ray_matrix, domain=ZZ)
    smith_invariants = [
        abs(int(smith[index, index]))
        for index in range(min(smith.shape))
        if smith[index, index] != 0
    ]
    assert smith_invariants == [1] * 12

    # Since the ray lattice is saturated and has the full rational balanced
    # span, these HNF columns are a basis of ker(balance_matrix) cap Z^15.
    lattice_basis = hermite_normal_form(ray_matrix)
    assert lattice_basis.shape == (15, 12)
    ray_coordinates = []
    for ray in rays:
        solution = next(iter(sp.linsolve((lattice_basis, sp.Matrix(ray)))))
        assert all(entry.q == 1 for entry in solution)
        ray_coordinates.append(tuple(int(entry) for entry in solution))
    ray_coordinates = tuple(ray_coordinates)

    facets = enumerate_facets(ray_coordinates)
    assert len(facets) == 18

    patterns = enumerate_full_dimensional_sign_patterns(rays)
    target_index = names.index("rho_(002;1)")
    target = rays[target_index]
    adjacent_patterns = [
        pattern
        for pattern in patterns
        if all(
            target[index] == 0 or pattern[index] == (target[index] > 0)
            for index in range(len(H4))
        )
    ]
    assert len(patterns) == 4074
    assert len(adjacent_patterns) == 256

    selected_pattern_text = "+++++--+++++-++"
    selected_pattern = tuple(character == "+" for character in selected_pattern_text)
    assert selected_pattern in adjacent_patterns

    # A compact exact strict-interior certificate for the selected orthant.
    interior_coefficients = (7, 1, 6, 2, 2, 1, 1, 1, 1, 1, 7, 11, 1, 2, 1, 1, 2, 3)
    interior_gamma = tuple(
        sum(
            interior_coefficients[ray_index] * rays[ray_index][coordinate]
            for ray_index in range(len(rays))
        )
        for coordinate in range(len(H4))
    )
    assert all(coefficient > 0 for coefficient in interior_coefficients)
    assert all(entry != 0 for entry in interior_gamma)
    assert tuple(entry > 0 for entry in interior_gamma) == selected_pattern

    chamber_rays = ray_coordinates
    chamber_inequalities = facets
    for coordinate, positive in enumerate(selected_pattern):
        sign = 1 if positive else -1
        inequality = tuple(
            sign * int(lattice_basis[coordinate, column]) for column in range(12)
        )
        chamber_rays, chamber_inequalities = cut_cone(
            chamber_rays, chamber_inequalities, inequality
        )
    assert len(chamber_rays) == 48
    assert exact_rank(chamber_rays) == 12

    chamber_gammas = []
    for ray in chamber_rays:
        gamma = tuple(int(entry) for entry in lattice_basis * sp.Matrix(ray))
        assert math.gcd(*(abs(entry) for entry in gamma)) == 1
        assert all(
            (entry >= 0 if selected_pattern[index] else entry <= 0)
            for index, entry in enumerate(gamma)
        )
        chamber_gammas.append(gamma)
    chamber_records = support_audit(chamber_gammas)
    assert all(record["missing_count"] == 0 for record in chamber_records)

    # A separate global falsification screen: all distinct sums arising from
    # multisets of two or three original rays.  Duplicates are tested once.
    seen_sums = set()
    small_sum_counts = {}
    cache = {}
    for number_of_summands in (2, 3):
        new_count = 0
        for indices in itertools.combinations_with_replacement(
            range(len(rays)), number_of_summands
        ):
            gamma = tuple(
                sum(rays[index][coordinate] for index in indices)
                for coordinate in range(len(H4))
            )
            if gamma in seen_sums:
                continue
            seen_sums.add(gamma)
            new_count += 1
            positive = tuple(max(entry, 0) for entry in gamma)
            negative = tuple(max(-entry, 0) for entry in gamma)
            numerator = product_support(positive, cache)
            denominator = product_support(negative, cache)
            assert numerator <= denominator
        small_sum_counts[str(number_of_summands)] = new_count
    assert small_sum_counts == {"2": 162, "3": 984}

    output = {
        "arithmetic": "exact integers/rationals; exact z3 linear rational arithmetic",
        "H4_order": [alpha_label(alpha) for alpha in H4],
        "ray_names_in_order": list(names),
        "balanced_lattice_rank": 12,
        "ray_lattice_smith_invariants": smith_invariants,
        "cone_facet_count": len(facets),
        "full_dimensional_strict_sign_patterns": len(patterns),
        "full_dimensional_chambers_whose_closure_contains_rho_002_1": len(
            adjacent_patterns
        ),
        "selected_chamber": {
            "sign_pattern": selected_pattern_text,
            "strict_interior_ray_coefficients": list(interior_coefficients),
            "strict_interior_gamma": list(interior_gamma),
            "primitive_extreme_ray_count": len(chamber_gammas),
            "positive_degree_distribution": {
                str(degree): sum(
                    record["positive_degree"] == degree for record in chamber_records
                )
                for degree in sorted(
                    {record["positive_degree"] for record in chamber_records}
                )
            },
            "rays_failing_support_containment": sum(
                record["missing_count"] > 0 for record in chamber_records
            ),
            "ray_support_records": chamber_records,
        },
        "distinct_small_ray_sums_tested": {
            "two_summands": small_sum_counts["2"],
            "three_summands_new_after_two": small_sum_counts["3"],
            "total": len(seen_sums),
            "support_failures": 0,
        },
        "scope_warning": (
            "The 48 vectors are the real-cone extreme rays of one closed sign "
            "chamber, not its affine-semigroup Hilbert basis."
        ),
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
