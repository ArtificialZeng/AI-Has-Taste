#!/usr/bin/env python3
"""Independently verify the direct six-set relations on all 6-point signotopes."""

from __future__ import annotations

import itertools

from compact_sat import triple_variables
from direct_six_sat import convex_relations


def at_most_one_change(bits: tuple[bool, bool, bool, bool]) -> bool:
    return sum(a != b for a, b in zip(bits, bits[1:])) <= 1


def main() -> None:
    triples = tuple(itertools.combinations(range(6), 3))
    variables = triple_variables(6)
    relations = convex_relations((0, 1, 2, 3, 4, 5), variables)
    signotope_count = 0
    convex_count = 0
    for bits in itertools.product((False, True), repeat=len(triples)):
        assignment = dict(zip(triples, bits))
        if not all(
            at_most_one_change(
                tuple(
                    assignment[triple]
                    for triple in (
                        (b, c, d),
                        (a, c, d),
                        (a, b, d),
                        (a, b, c),
                    )
                )
            )
            for a, b, c, d in itertools.combinations(range(6), 4)
        ):
            continue
        signotope_count += 1
        all_quads_even = all(
            sum(assignment[triple] for triple in itertools.combinations(quad, 3)) % 2 == 0
            for quad in itertools.combinations(range(6), 4)
        )

        def literal_value(literal: int) -> bool:
            triple = triples[abs(literal) - 1]
            return assignment[triple] == (literal > 0)

        satisfies_relation = any(
            len({literal_value(literal) for literal in relation}) == 1
            for relation in relations
        )
        assert all_quads_even == satisfies_relation
        convex_count += int(all_quads_even)
    assert signotope_count == 908
    assert convex_count == 16
    print("verified_six_point_signotopes=908")
    print("verified_concave_six_point_signotopes=892")
    print("verified_direct_relations_equal_all_four_sets_even")


if __name__ == "__main__":
    main()
