#!/usr/bin/env python3
"""Independent exact checks of the four-point parity theorem and CNF counts."""

from __future__ import annotations

import itertools
import math

from compact_sat import (
    counts,
    parity_guard_clauses,
    signotope_clauses,
    signotope_direct_clauses,
    signotope_prime_clauses,
    triple_variables,
)


Point = tuple[int, int]


def orient(a: Point, b: Point, c: Point) -> int:
    determinant = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    return (determinant > 0) - (determinant < 0)


def convex_hull(points: tuple[Point, ...]) -> list[Point]:
    ordered = sorted(points)

    def half(sequence: list[Point]) -> list[Point]:
        result: list[Point] = []
        for point in sequence:
            while len(result) >= 2 and orient(result[-2], result[-1], point) <= 0:
                result.pop()
            result.append(point)
        return result

    lower = half(ordered)
    upper = half(list(reversed(ordered)))
    return lower[:-1] + upper[:-1]


def evaluate_clause(clause: tuple[int, ...], assignment: dict[int, bool]) -> bool:
    return any(assignment[abs(literal)] == (literal > 0) for literal in clause)


def verify_coordinate_samples() -> int:
    grid = tuple(itertools.product(range(4), repeat=2))
    checked = 0
    for points in itertools.combinations(grid, 4):
        signs = tuple(
            orient(points[i], points[j], points[k])
            for i, j, k in itertools.combinations(range(4), 3)
        )
        if 0 in signs:
            continue
        convex = len(convex_hull(points)) == 4
        parity_product = math.prod(signs)
        assert convex == (parity_product == 1)
        checked += 1
    return checked


def verify_cnf_truth_table() -> None:
    variables = triple_variables(4)
    indicator = 5
    clauses = tuple(parity_guard_clauses((0, 1, 2, 3), indicator, variables))
    assert len(clauses) == 8
    base = tuple(variables[triple] for triple in itertools.combinations(range(4), 3))
    for bits in itertools.product((False, True), repeat=4):
        odd = sum(bits) % 2 == 1
        for flag in (False, True):
            assignment = dict(zip(base, bits))
            assignment[indicator] = flag
            accepted = all(evaluate_clause(clause, assignment) for clause in clauses)
            assert accepted == ((not flag) or odd)
        assert any(
            all(
                evaluate_clause(
                    clause,
                    dict(zip(base, bits)) | {indicator: flag},
                )
                for clause in clauses
            )
            for flag in (False, True)
        )

    signotope = tuple(signotope_clauses((0, 1, 2, 3), variables))
    signotope_direct = tuple(signotope_direct_clauses((0, 1, 2, 3), variables))
    signotope_prime = tuple(signotope_prime_clauses((0, 1, 2, 3), variables))
    restricted = tuple(
        parity_guard_clauses(
            (0, 1, 2, 3), indicator, variables, signotope_restricted=True
        )
    )
    assert len(signotope) == 4
    assert len(signotope_direct) == 8
    assert len(signotope_prime) == 8
    assert len(restricted) == 4
    for bits in itertools.product((False, True), repeat=4):
        assignment = dict(zip(base, bits))
        sequence = (bits[3], bits[2], bits[1], bits[0])
        valid_signotope = sum(a != b for a, b in zip(sequence, sequence[1:])) <= 1
        accepted_compact = all(evaluate_clause(clause, assignment) for clause in signotope)
        accepted_direct = all(
            evaluate_clause(clause, assignment) for clause in signotope_direct
        )
        accepted_prime = all(
            evaluate_clause(clause, assignment) for clause in signotope_prime
        )
        assert accepted_compact == valid_signotope
        assert accepted_direct == valid_signotope
        assert accepted_prime == valid_signotope
        assert accepted_compact == accepted_direct
        if valid_signotope:
            odd = sum(bits) % 2 == 1
            for flag in (False, True):
                accepted = all(
                    evaluate_clause(clause, assignment | {indicator: flag})
                    for clause in restricted
                )
                assert accepted == ((not flag) or odd)

    equivalence = tuple(
        parity_guard_clauses(
            (0, 1, 2, 3),
            indicator,
            variables,
            signotope_restricted=True,
            equivalence=True,
        )
    )
    assert len(equivalence) == 8
    for bits in itertools.product((False, True), repeat=4):
        assignment = dict(zip(base, bits))
        sequence = (bits[3], bits[2], bits[1], bits[0])
        valid_signotope = sum(a != b for a, b in zip(sequence, sequence[1:])) <= 1
        if valid_signotope:
            odd = sum(bits) % 2 == 1
            for flag in (False, True):
                accepted = all(
                    evaluate_clause(clause, assignment | {indicator: flag})
                    for clause in equivalence
                )
                assert accepted == (flag == odd)

    factored_equivalence = tuple(
        parity_guard_clauses(
            (0, 1, 2, 3),
            indicator,
            variables,
            signotope_restricted=True,
            equivalence=True,
            factored_reverse=True,
        )
    )
    assert len(factored_equivalence) == 8
    assert all(len(clause) == 3 for clause in factored_equivalence)
    for bits in itertools.product((False, True), repeat=4):
        assignment = dict(zip(base, bits))
        sequence = (bits[3], bits[2], bits[1], bits[0])
        valid_signotope = sum(a != b for a, b in zip(sequence, sequence[1:])) <= 1
        if valid_signotope:
            odd = sum(bits) % 2 == 1
            for flag in (False, True):
                accepted = all(
                    evaluate_clause(clause, assignment | {indicator: flag})
                    for clause in factored_equivalence
                )
                assert accepted == (flag == odd)


def verify_signotope_clause_minimality() -> None:
    assignments = tuple(itertools.product((False, True), repeat=4))
    good = {
        bits
        for bits in assignments
        if sum(left != right for left, right in zip(bits, bits[1:])) <= 1
    }
    bad = set(assignments) - good
    implicate_covers = []
    for signs in itertools.product((-1, 0, 1), repeat=4):
        if signs == (0, 0, 0, 0):
            continue

        def clause_value(bits: tuple[bool, ...]) -> bool:
            return any(
                bit if sign > 0 else not bit
                for bit, sign in zip(bits, signs)
                if sign
            )

        if all(clause_value(bits) for bits in good):
            covered = frozenset(bits for bits in bad if not clause_value(bits))
            if covered:
                implicate_covers.append(covered)
    for size in range(1, 4):
        assert not any(
            set().union(*selection) == bad
            for selection in itertools.combinations(implicate_covers, size)
        )
    assert any(
        set().union(*selection) == bad
        for selection in itertools.combinations(implicate_covers, 4)
    )


def verify_counts() -> None:
    compact = counts(33, 7, ax5_mode="reduced")
    assert compact == {
        "variables": 46376,
        "clauses": 14092848,
        "literal_occurrences": 208119120,
        "triple_variables": 5456,
        "four_set_indicators": 40920,
        "consistency_clauses": 9493440,
        "parity_clauses": 327360,
        "exclusion_clauses": 4272048,
        "hull_clauses": 0,
        "symmetry_clauses": 0,
    }
    original_variables = math.comb(33, 3) + 14 * math.comb(33, 4)
    original_clauses = (
        math.prod(range(29, 34)) // 3
        + 71 * math.comb(33, 4)
        + math.comb(33, 7)
    )
    original_literals = (
        6 * (math.prod(range(29, 34)) // 3)
        + 196 * math.comb(33, 4)
        + 280 * math.comb(33, 7)
    )
    assert original_variables == 578336
    assert original_clauses == 16670808
    assert original_literals == 1261154400

    quadruples = math.comb(33, 4)
    seven_sets = math.comb(33, 7)
    subercaseaux_variables = math.comb(33, 3) + quadruples
    subercaseaux_clauses = 4 * quadruples + 16 * quadruples + seven_sets
    subercaseaux_literals = (
        3 * 4 * quadruples + 5 * 16 * quadruples + 35 * seven_sets
    )
    assert subercaseaux_variables == 46376
    assert subercaseaux_clauses == 5090448
    assert subercaseaux_literals == 153286320

    signotope_compact = counts(33, 7, ax5_mode="signotope")
    assert signotope_compact == {
        "variables": 46376,
        "clauses": 4599408,
        "literal_occurrences": 150503760,
        "triple_variables": 5456,
        "four_set_indicators": 40920,
        "consistency_clauses": 163680,
        "parity_clauses": 163680,
        "exclusion_clauses": 4272048,
        "hull_clauses": 0,
        "symmetry_clauses": 0,
    }
    signotope_direct = counts(33, 7, ax5_mode="signotope-direct")
    assert signotope_direct == {
        "variables": 46376,
        "clauses": 4763088,
        "literal_occurrences": 151322160,
        "triple_variables": 5456,
        "four_set_indicators": 40920,
        "consistency_clauses": 327360,
        "parity_clauses": 163680,
        "exclusion_clauses": 4272048,
        "hull_clauses": 0,
        "symmetry_clauses": 0,
    }
    full_factored = counts(
        33, 7, ax5_mode="signotope", parity_mode="equivalence-factored"
    )
    assert full_factored == {
        "variables": 46376,
        "clauses": 4763088,
        "literal_occurrences": 150994800,
        "triple_variables": 5456,
        "four_set_indicators": 40920,
        "consistency_clauses": 163680,
        "parity_clauses": 327360,
        "exclusion_clauses": 4272048,
        "hull_clauses": 0,
        "symmetry_clauses": 0,
    }


def main() -> None:
    checked = verify_coordinate_samples()
    verify_cnf_truth_table()
    verify_signotope_clause_minimality()
    verify_counts()
    print(f"verified_general_position_grid_quadruples={checked}")
    print("verified_four_orientation_product_characterizes_convexity")
    print("verified_eight_clause_one_sided_parity_guard")
    print("verified_four_clause_signotope_equals_direct_eight_clause_encoding")
    print("verified_eight_prime_ternary_signotope_clauses")
    print("verified_four_clauses_are_minimal_without_auxiliary_variables")
    print("verified_signotope_restricted_four_clause_guard")
    print("verified_signotope_restricted_eight_clause_equivalence")
    print("verified_signotope_restricted_all_ternary_factored_equivalence")
    print("verified_33_point_formula_counts")
    print("verified_subercaseaux_public_fixed_order_counts")


if __name__ == "__main__":
    main()
