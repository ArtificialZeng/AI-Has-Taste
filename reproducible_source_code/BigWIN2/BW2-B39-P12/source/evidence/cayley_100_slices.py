#!/usr/bin/env python3
"""Exact deterministic two-parameter Cayley slices for the order-seven problem.

This script generates 100 affine two-parameter slices of the 21-dimensional
space of 7 x 7 rational skew matrices.  The first 50 slices have generic small
rational frozen coordinates.  The final 50 pass through distinct signed-free
permutation Euler points whose cycle type is 1+3+3, so their inverse Cayley
coordinates exist and are small integers.

For every slice it constructs Q=(I-S)(I+S)^(-1), clears the denominators of
D(Q)-1 and A(Q)-1, computes and factors their y-resultant over QQ, enumerates
all rational x-roots (exactly the roots of the linear factors), and then uses
the specialized polynomial gcd to enumerate every rational y-coordinate.
Each resulting Q is checked by exact rational arithmetic.

The fact that I+S is nonsingular needs no exceptional-case search: for every
real skew-symmetric S, (I+S)v=0 would imply
0=v^T(I+S)v=v^Tv.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path

import sympy as sp


N = 7
X, Y = sp.symbols("x y")
PARAMETERS = tuple((i, j) for i in range(N) for j in range(i + 1, N))
GENERIC_POOL = (
    sp.Rational(-3, 2),
    sp.Rational(-2, 3),
    sp.Rational(-1, 2),
    sp.Rational(-1, 3),
    sp.Rational(1, 3),
    sp.Rational(1, 2),
    sp.Rational(2, 3),
    sp.Rational(3, 2),
)
SEED = "win-00039-p12-cayley-v1"


def digest_integer(label: str) -> int:
    return int.from_bytes(hashlib.sha256(f"{SEED}:{label}".encode()).digest(), "big")


def qstr(value: sp.Expr) -> str:
    value = sp.cancel(value)
    if value.is_Rational:
        return str(value)
    raise ValueError(f"expected a rational number, got {value!r}")


def parameter_name(pair: tuple[int, int]) -> str:
    return f"s{pair[0] + 1}{pair[1] + 1}"


def matrix_from_coordinates(coordinates: list[sp.Expr]) -> sp.Matrix:
    matrix = sp.zeros(N)
    for (i, j), value in zip(PARAMETERS, coordinates):
        matrix[i, j] = value
        matrix[j, i] = -value
    return matrix


def normalized_polynomial(expression: sp.Expr) -> sp.Poly:
    numerator, _ = sp.fraction(sp.cancel(expression))
    polynomial = sp.Poly(numerator, X, Y, domain=sp.QQ)
    if polynomial.is_zero:
        return polynomial
    return polynomial.monic()


def factor_record(poly: sp.Poly, variable: sp.Symbol) -> dict:
    unit, factors = sp.factor_list(poly)
    return {
        "unit": qstr(unit),
        "factors": [
            {
                "degree": int(factor.degree(variable)),
                "multiplicity": int(multiplicity),
                "coefficients_high_to_low": [qstr(c) for c in factor.all_coeffs()],
            }
            for factor, multiplicity in factors
        ],
    }


def linear_roots(poly: sp.Poly, variable: sp.Symbol) -> list[sp.Rational]:
    roots: set[sp.Rational] = set()
    _, factors = sp.factor_list(poly)
    for factor, _ in factors:
        if factor.degree(variable) == 1:
            a, b = factor.all_coeffs()
            root = sp.cancel(-b / a)
            if not root.is_Rational:
                raise AssertionError("linear polynomial over QQ had a nonrational root")
            roots.add(root)
    return sorted(roots, key=lambda r: (int(sp.denom(r)), int(sp.numer(r))))


def permutation_cycles(permutation: tuple[int, ...]) -> list[list[int]]:
    seen: set[int] = set()
    cycles: list[list[int]] = []
    for start in range(N):
        if start in seen:
            continue
        cycle: list[int] = []
        cursor = start
        while cursor not in seen:
            seen.add(cursor)
            cycle.append(cursor)
            cursor = permutation[cursor]
        cycles.append(cycle)
    return cycles


def valid_anchor_permutations() -> list[tuple[int, ...]]:
    valid: list[tuple[int, ...]] = []
    for permutation in itertools.permutations(range(N)):
        fixed = sum(permutation[i] == i for i in range(N))
        antidiagonal = sum(permutation[i] == N - 1 - i for i in range(N))
        cycle_type = sorted(map(len, permutation_cycles(permutation)))
        if fixed == antidiagonal == 1 and cycle_type == [1, 3, 3]:
            valid.append(permutation)
    valid.sort(key=lambda p: digest_integer("permutation:" + ",".join(map(str, p))))
    return valid


def permutation_matrix(permutation: tuple[int, ...]) -> sp.Matrix:
    matrix = sp.zeros(N)
    for i, j in enumerate(permutation):
        matrix[i, j] = 1
    return matrix


def generic_specs() -> list[dict]:
    active_pairs = list(itertools.combinations(range(len(PARAMETERS)), 2))
    active_pairs.sort(key=lambda pair: digest_integer(f"active:{pair[0]}:{pair[1]}"))
    specs: list[dict] = []
    for slice_index, (a, b) in enumerate(active_pairs[:50]):
        coordinates: list[sp.Expr] = []
        for parameter_index in range(len(PARAMETERS)):
            pool_index = digest_integer(
                f"generic:{slice_index}:parameter:{parameter_index}"
            ) % len(GENERIC_POOL)
            coordinates.append(GENERIC_POOL[pool_index])
        coordinates[a] = X
        coordinates[b] = Y
        specs.append(
            {
                "slice_id": f"generic-{slice_index:03d}",
                "cohort": "generic-small-rational",
                "active_indices": [a, b],
                "coordinates": coordinates,
                "anchor_permutation": None,
            }
        )
    return specs


def anchor_specs() -> list[dict]:
    specs: list[dict] = []
    identity = sp.eye(N)
    for slice_index, permutation in enumerate(valid_anchor_permutations()[:50]):
        p_matrix = permutation_matrix(permutation)
        # Cycle type 1+3+3 implies -1 is not an eigenvalue.
        s_anchor = (identity - p_matrix) * (identity + p_matrix).inv()
        if s_anchor + s_anchor.T != sp.zeros(N):
            raise AssertionError("inverse Cayley transform was not skew")
        cycles = permutation_cycles(permutation)
        singleton = next(cycle for cycle in cycles if len(cycle) == 1)
        triples = sorted((cycle for cycle in cycles if len(cycle) == 3), key=min)

        first_edge_options = [(singleton[0], vertex) for vertex in triples[0]]
        second_edge_options = list(itertools.product(triples[0], triples[1]))
        first = first_edge_options[
            digest_integer(f"anchor:{slice_index}:first") % len(first_edge_options)
        ]
        second = second_edge_options[
            digest_integer(f"anchor:{slice_index}:second") % len(second_edge_options)
        ]
        active_edges = [tuple(sorted(first)), tuple(sorted(second))]
        active_indices = [PARAMETERS.index(edge) for edge in active_edges]

        coordinates = [s_anchor[i, j] for i, j in PARAMETERS]
        # Both selected edges join distinct cycle components, so their anchor
        # values are zero.  This assertion documents that the slice passes
        # through the stated Euler permutation at (x,y)=(0,0).
        if any(coordinates[index] != 0 for index in active_indices):
            raise AssertionError("chosen anchoring edge was nonzero")
        coordinates[active_indices[0]] = X
        coordinates[active_indices[1]] = Y
        specs.append(
            {
                "slice_id": f"anchor-{slice_index:03d}",
                "cohort": "improper-euler-anchor",
                "active_indices": active_indices,
                "coordinates": coordinates,
                "anchor_permutation": [entry + 1 for entry in permutation],
            }
        )
    return specs


def exact_matrix_record(q_matrix: sp.Matrix, x_value: sp.Rational, y_value: sp.Rational) -> dict:
    evaluated = q_matrix.subs({X: x_value, Y: y_value}).applyfunc(sp.cancel)
    if any(not entry.is_Rational for entry in evaluated):
        raise AssertionError("a reconstructed entry was not rational")
    identity = sp.eye(N)
    orthogonal = evaluated * evaluated.T == identity
    diagonal_sum = sp.cancel(sum(evaluated[i, i] ** 2 for i in range(N)))
    antidiagonal_sum = sp.cancel(sum(evaluated[i, N - 1 - i] ** 2 for i in range(N)))
    squares = [sp.cancel(entry**2) for entry in evaluated]
    distinct_square_count = len(set(squares))
    verified = orthogonal and diagonal_sum == 1 and antidiagonal_sum == 1
    if not verified:
        raise AssertionError("reconstructed common zero failed exact matrix verification")
    return {
        "x": qstr(x_value),
        "y": qstr(y_value),
        "orthogonal": True,
        "diagonal_sum": qstr(diagonal_sum),
        "antidiagonal_sum": qstr(antidiagonal_sum),
        "distinct_entry_squares": distinct_square_count,
        "proper": distinct_square_count == N * N,
        "matrix": [[qstr(evaluated[i, j]) for j in range(N)] for i in range(N)],
    }


def analyze_slice(spec: dict) -> dict:
    s_matrix = matrix_from_coordinates(spec["coordinates"])
    identity = sp.eye(N)
    q_matrix = (identity - s_matrix) * (identity + s_matrix).inv(method="DM")
    diagonal_equation = normalized_polynomial(
        sum(q_matrix[i, i] ** 2 for i in range(N)) - 1
    )
    antidiagonal_equation = normalized_polynomial(
        sum(q_matrix[i, N - 1 - i] ** 2 for i in range(N)) - 1
    )
    common_component = sp.gcd(diagonal_equation, antidiagonal_equation)
    resultant_expression = sp.resultant(
        diagonal_equation.as_expr(), antidiagonal_equation.as_expr(), Y
    )
    resultant = sp.Poly(resultant_expression, X, domain=sp.QQ)

    rational_solutions: list[dict] = []
    vertical_component = False
    rational_x_roots: list[sp.Rational] = []
    if not resultant.is_zero:
        rational_x_roots = linear_roots(resultant, X)
        for x_value in rational_x_roots:
            f_at_x = sp.Poly(diagonal_equation.as_expr().subs(X, x_value), Y, domain=sp.QQ)
            g_at_x = sp.Poly(antidiagonal_equation.as_expr().subs(X, x_value), Y, domain=sp.QQ)
            specialized_gcd = sp.gcd(f_at_x, g_at_x)
            if specialized_gcd.is_zero:
                vertical_component = True
                continue
            for y_value in linear_roots(specialized_gcd, Y):
                if diagonal_equation.eval({X: x_value, Y: y_value}) != 0:
                    raise AssertionError("enumerated y-root failed the diagonal equation")
                if antidiagonal_equation.eval({X: x_value, Y: y_value}) != 0:
                    raise AssertionError("enumerated y-root failed the antidiagonal equation")
                rational_solutions.append(exact_matrix_record(q_matrix, x_value, y_value))

    frozen = {
        parameter_name(PARAMETERS[index]): qstr(value)
        for index, value in enumerate(spec["coordinates"])
        if index not in spec["active_indices"]
    }
    record = {
        "slice_id": spec["slice_id"],
        "cohort": spec["cohort"],
        "active_parameters": [
            parameter_name(PARAMETERS[index]) for index in spec["active_indices"]
        ],
        "frozen_parameters": frozen,
        "anchor_permutation_one_based": spec["anchor_permutation"],
        "diagonal_numerator": {
            "degree_x": int(diagonal_equation.degree(X)),
            "degree_y": int(diagonal_equation.degree(Y)),
            "term_count": len(diagonal_equation.terms()),
        },
        "antidiagonal_numerator": {
            "degree_x": int(antidiagonal_equation.degree(X)),
            "degree_y": int(antidiagonal_equation.degree(Y)),
            "term_count": len(antidiagonal_equation.terms()),
        },
        "bivariate_gcd_total_degree": (
            -1 if common_component.is_zero else int(common_component.total_degree())
        ),
        "resultant_zero": resultant.is_zero,
        "resultant_degree": -1 if resultant.is_zero else int(resultant.degree(X)),
        "resultant_factorization_over_Q": (
            None if resultant.is_zero else factor_record(resultant, X)
        ),
        "rational_x_roots": [qstr(root) for root in rational_x_roots],
        "vertical_rational_component_detected": vertical_component,
        "rational_solutions": rational_solutions,
    }
    return record


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    specs = generic_specs() + anchor_specs()
    if len(specs) != 100:
        raise AssertionError("the test must contain exactly 100 slices")

    slices: list[dict] = []
    for index, spec in enumerate(specs, start=1):
        print(f"[{index:03d}/100] {spec['slice_id']}", flush=True)
        slices.append(analyze_slice(spec))

    all_solutions = [
        (record["slice_id"], solution)
        for record in slices
        for solution in record["rational_solutions"]
    ]
    best = None
    if all_solutions:
        best_slice, best_solution = max(
            all_solutions, key=lambda item: item[1]["distinct_entry_squares"]
        )
        best = {"slice_id": best_slice, **best_solution}

    result = {
        "schema": "win-00039-p12/exact-cayley-slices/v1",
        "purpose": (
            "Exact two-parameter slice search for rational Q in SO(7) with "
            "D(Q)=A(Q)=1 and 49 distinct entry-squares"
        ),
        "deterministic_seed": SEED,
        "software": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
        },
        "method": {
            "parameterization": "Q=(I-S)(I+S)^(-1), S^T=-S",
            "generic_slice_count": 50,
            "anchored_slice_count": 50,
            "eliminated_variable": "y",
            "factorization_domain": "QQ",
            "rational_root_rule": (
                "A rational root of a QQ polynomial occurs in a linear "
                "irreducible factor; specialized gcds give all matching y-roots."
            ),
            "denominator_rule": (
                "I+S is nonsingular for every real skew S because "
                "v^T(I+S)v=v^Tv."
            ),
        },
        "summary": {
            "slice_count": len(slices),
            "nonzero_resultants": sum(not record["resultant_zero"] for record in slices),
            "positive_dimensional_bivariate_gcds": sum(
                record["bivariate_gcd_total_degree"] > 0 for record in slices
            ),
            "vertical_rational_components": sum(
                record["vertical_rational_component_detected"] for record in slices
            ),
            "rational_solution_count_with_slice_multiplicity": len(all_solutions),
            "proper_solution_count_with_slice_multiplicity": sum(
                solution["proper"] for _, solution in all_solutions
            ),
            "best_distinct_entry_squares": (
                None if best is None else best["distinct_entry_squares"]
            ),
        },
        "best_rational_solution": best,
        "slices": slices,
    }
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result["summary"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
