#!/usr/bin/env python3
"""Fresh referee check using exact Fourier--Motzkin elimination.

This checker is deliberately independent of the candidate's active-set and
dual-ray implementations.  It eliminates the barycentric variables directly
from the rational feasibility system defining conv(A) + R^3_+.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from fractions import Fraction
from itertools import product
from pathlib import Path


Exponent = tuple[int, int, int]
Generators = tuple[Exponent, ...]
Inequality = tuple[tuple[Fraction, ...], Fraction]


def normalize(coefficients: tuple[Fraction, ...], rhs: Fraction) -> Inequality:
    """Normalize an inequality by a positive rational scalar."""

    denominators = [entry.denominator for entry in coefficients] + [rhs.denominator]
    scale = math.lcm(*denominators)
    integers = [int(entry * scale) for entry in coefficients] + [int(rhs * scale)]
    divisor = math.gcd(*integers)
    if divisor == 0:
        divisor = 1
    normalized = [Fraction(entry // divisor) for entry in integers]
    return tuple(normalized[:-1]), normalized[-1]


def eliminate_first(inequalities: list[Inequality]) -> list[Inequality]:
    """Project a system of <= inequalities along its first variable."""

    positive: list[Inequality] = []
    negative: list[Inequality] = []
    zero: list[Inequality] = []
    for inequality in inequalities:
        coefficient = inequality[0][0]
        if coefficient > 0:
            positive.append(inequality)
        elif coefficient < 0:
            negative.append(inequality)
        else:
            zero.append(inequality)

    projected: set[Inequality] = {
        normalize(coefficients[1:], rhs) for coefficients, rhs in zero
    }
    for p_coefficients, p_rhs in positive:
        p_scale = p_coefficients[0]
        for n_coefficients, n_rhs in negative:
            n_scale = -n_coefficients[0]
            coefficients = tuple(
                n_scale * p_coefficients[index] + p_scale * n_coefficients[index]
                for index in range(1, len(p_coefficients))
            )
            rhs = n_scale * p_rhs + p_scale * n_rhs
            projected.add(normalize(coefficients, rhs))
    return list(projected)


def rational_feasible(inequalities: list[Inequality], variable_count: int) -> bool:
    """Exact existential feasibility by the Fourier--Motzkin theorem."""

    current = inequalities
    for _ in range(variable_count):
        current = eliminate_first(current)
    return all(rhs >= 0 for coefficients, rhs in current if not coefficients)


def in_newton_polyhedron(generators: Generators, exponent: Exponent) -> bool:
    """Test whether exponent is in conv(generators)+R^3_+."""

    # Substitute lambda_last = 1 - sum(lambda_i) into lambda >= 0 and
    # sum(lambda_i * generator_i) <= exponent coordinatewise.
    last = generators[-1]
    variable_count = len(generators) - 1
    inequalities: list[Inequality] = []
    for index in range(variable_count):
        coefficients = tuple(
            Fraction(-1 if index == other else 0)
            for other in range(variable_count)
        )
        inequalities.append((coefficients, Fraction(0)))
    inequalities.append(
        (tuple(Fraction(1) for _ in range(variable_count)), Fraction(1))
    )
    for coordinate in range(3):
        coefficients = tuple(
            Fraction(generators[index][coordinate] - last[coordinate])
            for index in range(variable_count)
        )
        inequalities.append(
            (coefficients, Fraction(exponent[coordinate] - last[coordinate]))
        )
    return rational_feasible(inequalities, variable_count)


def in_input_ideal(generators: Generators, exponent: Exponent) -> bool:
    return any(
        all(generator[index] <= exponent[index] for index in range(3))
        for generator in generators
    )


def labeled_ideals() -> list[Generators]:
    """Generate the quantified class without quotienting variable labels."""

    ideals: list[Generators] = []
    for axes in product(range(1, 5), repeat=3):
        a, b, c = axes
        pure: Generators = ((a, 0, 0), (0, b, 0), (0, 0, c))
        ideals.append(pure)
        for mixed in product(range(a), range(b), range(c)):
            if sum(value != 0 for value in mixed) >= 2 and sum(mixed) <= 4:
                ideals.append(pure + (mixed,))
    assert len(ideals) == len(set(ideals)) == 517
    return ideals


def input_socle(generators: Generators) -> list[Exponent]:
    bounds = tuple(generators[index][index] for index in range(3))
    return [
        point
        for point in product(*(range(bound) for bound in bounds))
        if not in_input_ideal(generators, point)
        and all(
            in_input_ideal(
                generators,
                tuple(point[index] + (index == coordinate) for index in range(3)),
            )
            for coordinate in range(3)
        )
    ]


def closure_socle(generators: Generators) -> list[Exponent]:
    bounds = tuple(generators[index][index] for index in range(3))
    membership: dict[Exponent, bool] = {}

    def belongs(point: Exponent) -> bool:
        if point not in membership:
            membership[point] = in_newton_polyhedron(generators, point)
        return membership[point]

    return [
        point
        for point in product(*(range(bound) for bound in bounds))
        if not belongs(point)
        and all(
            belongs(
                tuple(point[index] + (index == coordinate) for index in range(3))
            )
            for coordinate in range(3)
        )
    ]


def main() -> None:
    frozen = json.loads(Path("evidence/lp_results.json").read_text(encoding="utf-8"))
    frozen_by_generators = {
        tuple(tuple(point) for point in record["generators"]): record
        for record in frozen["records"]
    }
    differences: Counter[int] = Counter()
    checked_socles = 0
    for generators in labeled_ideals():
        socle_i = input_socle(generators)
        socle_closed = closure_socle(generators)
        assert socle_i and socle_closed
        v_i = min(map(sum, socle_i))
        v_closed = min(map(sum, socle_closed))
        record = frozen_by_generators[generators]
        assert record["socle_I"] == [list(point) for point in socle_i]
        assert record["socle_closure"] == [list(point) for point in socle_closed]
        assert (record["v_I"], record["v_closure"]) == (v_i, v_closed)
        assert v_closed <= v_i
        differences[v_closed - v_i] += 1
        checked_socles += len(socle_i) + len(socle_closed)

    control: Generators = (
        (2, 0, 0),
        (0, 2, 0),
        (0, 0, 5),
        (1, 1, 1),
    )
    control_values = (
        min(map(sum, input_socle(control))),
        min(map(sum, closure_socle(control))),
    )
    assert control_values == (2, 3)
    assert differences == Counter({-6: 1, -5: 6, -4: 19, -3: 82, -2: 194, -1: 124, 0: 91})

    script_digest = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    payload = {
        "method": "exact-rational-Fourier-Motzkin-elimination",
        "labeled_ideal_count": 517,
        "socle_lists_compared": 1034,
        "socle_exponents_compared": checked_socles,
        "distribution": {str(key): differences[key] for key in sorted(differences)},
        "degree_five_control": {"v_I": 2, "v_closure": 3},
        "script_sha256": script_digest,
        "result": "exact agreement",
    }
    serialized = json.dumps(payload, indent=2, sort_keys=True) + "\n"
    Path("audit/referee_independent.json").write_text(serialized, encoding="utf-8")
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
