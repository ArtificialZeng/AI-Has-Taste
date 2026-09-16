#!/usr/bin/env python3
"""Exact three-coordinate Cayley tests around order-seven permutation seeds.

There are 112 unsigned 7 by 7 permutation matrices P with exactly one fixed
point, exactly one antidiagonal 1, and cycle type 1+3+3.  These are precisely
the unsigned permutation Euler points that lie in the identity Cayley chart.
For every such P, this script exhausts the 81 choices of one skew coordinate
joining each pair of the three cycle-components.  It computes the quadratic
terms of D(Q)-1 and A(Q)-1 at P exactly over QQ.

For the same deterministic 50 anchors used by cayley_100_slices.py, the script
also selects a third edge, constructs the full numerator equations in x,y,z,
factors each of the three coordinate-projection resultants over QQ, and screens
an exact rational grid in (x,y).  At every screened (x,y), all rational z are
enumerated from the linear factors of the specialized polynomial gcd; z is not
bounded by the grid.

The efficient exact formula used below follows from
S_P=(I-P)(I+P)^(-1), B=(I+S_P)^(-1)=(I+P)/2, and

  Q(S_P+E) = 2 (I+B E)^(-1) B - I.

The Taylor terms are L=-2BEB and H=2BEBEB, so the quadratic part of a sum
of selected entry-squares is sum(L_ij^2)+2 sum(P_ij H_ij).
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
from collections import Counter
from pathlib import Path

import sympy as sp

import cayley_100_slices as base


N = 7
X, Y, Z = sp.symbols("x y z")
VARIABLES = (X, Y, Z)
MONOMIALS_2 = (X**2, Y**2, Z**2, X * Y, X * Z, Y * Z)
SEED = "win-00039-p12-cayley-triangles-v1"


def qstr(value: sp.Expr) -> str:
    value = sp.cancel(value)
    if value.is_Rational:
        return str(value)
    raise ValueError(f"expected a rational number, got {value!r}")


def edge_name(edge: tuple[int, int]) -> str:
    return f"s{edge[0] + 1}{edge[1] + 1}"


def sorted_edge(i: int, j: int) -> tuple[int, int]:
    return (i, j) if i < j else (j, i)


def add_skew_entry(matrix: sp.Matrix, edge: tuple[int, int], value: sp.Expr) -> None:
    i, j = sorted_edge(*edge)
    matrix[i, j] = value
    matrix[j, i] = -value


def primitive_poly(expression: sp.Expr) -> sp.Poly:
    numerator, _ = sp.fraction(sp.cancel(expression))
    polynomial = sp.Poly(numerator, *VARIABLES, domain=sp.QQ)
    return polynomial.primitive()[1]


def initial_form(poly: sp.Poly) -> sp.Poly:
    minimum_degree = min(sum(monomial) for monomial, coefficient in poly.terms() if coefficient)
    expression = sum(
        coefficient * X ** monomial[0] * Y ** monomial[1] * Z ** monomial[2]
        for monomial, coefficient in poly.terms()
        if sum(monomial) == minimum_degree
    )
    return sp.Poly(expression, *VARIABLES, domain=sp.QQ).primitive()[1]


def coefficient_hash(poly: sp.Poly) -> str:
    canonical = [
        [list(monomial), qstr(coefficient)]
        for monomial, coefficient in poly.terms()
    ]
    payload = json.dumps(canonical, separators=(",", ":"), ensure_ascii=True)
    return hashlib.sha256(payload.encode()).hexdigest()


def factor_degrees(poly: sp.Poly) -> list[dict]:
    _, factors = sp.factor_list(poly)
    return [
        {
            "total_degree": int(factor.total_degree()),
            "multiplicity": int(multiplicity),
            "term_count": len(factor.terms()),
            "coefficient_hash": coefficient_hash(factor.primitive()[1]),
        }
        for factor, multiplicity in factors
    ]


def linear_roots(poly: sp.Poly, variable: sp.Symbol) -> list[sp.Rational]:
    roots: set[sp.Rational] = set()
    _, factors = sp.factor_list(poly)
    for factor, _ in factors:
        if factor.degree(variable) == 1:
            a, b = factor.all_coeffs()
            root = sp.cancel(-b / a)
            if not root.is_Rational:
                raise AssertionError("linear factor over QQ had a nonrational root")
            roots.add(root)
    return sorted(roots, key=lambda r: (int(sp.denom(r)), int(sp.numer(r))))


def components(permutation: tuple[int, ...]) -> tuple[int, list[int], list[int]]:
    cycles = base.permutation_cycles(permutation)
    singleton = next(cycle[0] for cycle in cycles if len(cycle) == 1)
    triples = sorted((cycle for cycle in cycles if len(cycle) == 3), key=min)
    return singleton, triples[0], triples[1]


def triangle_edges(
    singleton: int,
    first_cycle: list[int],
    second_cycle: list[int],
    first_vertex: int,
    middle_vertices: tuple[int, int],
    third_vertex: int,
) -> tuple[tuple[int, int], tuple[int, int], tuple[int, int]]:
    return (
        sorted_edge(singleton, first_vertex),
        sorted_edge(*middle_vertices),
        sorted_edge(singleton, third_vertex),
    )


def taylor_quadratics(
    permutation: tuple[int, ...],
    edges: tuple[tuple[int, int], tuple[int, int], tuple[int, int]],
) -> tuple[sp.Poly, sp.Poly]:
    identity = sp.eye(N)
    p_matrix = base.permutation_matrix(permutation)
    b_matrix = (identity + p_matrix) / 2
    perturbation = sp.zeros(N)
    for edge, variable in zip(edges, VARIABLES):
        add_skew_entry(perturbation, edge, variable)
    linear = -2 * b_matrix * perturbation * b_matrix
    quadratic = 2 * b_matrix * perturbation * b_matrix * perturbation * b_matrix

    fixed_rows = [i for i in range(N) if permutation[i] == i]
    anti_rows = [i for i in range(N) if permutation[i] == N - 1 - i]
    if len(fixed_rows) != 1 or len(anti_rows) != 1:
        raise AssertionError("anchor does not have exactly one selected entry")
    fixed = fixed_rows[0]
    anti_row = anti_rows[0]
    anti_column = N - 1 - anti_row

    diagonal_quadratic = sp.expand(
        sum(linear[i, i] ** 2 for i in range(N))
        + 2 * quadratic[fixed, fixed]
    )
    antidiagonal_quadratic = sp.expand(
        sum(linear[i, N - 1 - i] ** 2 for i in range(N))
        + 2 * quadratic[anti_row, anti_column]
    )
    return (
        sp.Poly(diagonal_quadratic, *VARIABLES, domain=sp.QQ),
        sp.Poly(antidiagonal_quadratic, *VARIABLES, domain=sp.QQ),
    )


def quadratic_coefficients(poly: sp.Poly) -> tuple[sp.Rational, ...]:
    return tuple(poly.coeff_monomial(monomial) for monomial in MONOMIALS_2)


def tangent_census(permutations: list[tuple[int, ...]]) -> dict:
    types: Counter[tuple[tuple[sp.Rational, ...], tuple[sp.Rational, ...]]] = Counter()
    failures: list[dict] = []
    family_count = 0
    for permutation_index, permutation in enumerate(permutations):
        singleton, first_cycle, second_cycle = components(permutation)
        for first_vertex in first_cycle:
            for middle_vertices in itertools.product(first_cycle, second_cycle):
                for third_vertex in second_cycle:
                    edges = triangle_edges(
                        singleton,
                        first_cycle,
                        second_cycle,
                        first_vertex,
                        middle_vertices,
                        third_vertex,
                    )
                    diagonal, antidiagonal = taylor_quadratics(permutation, edges)
                    d_coefficients = quadratic_coefficients(diagonal)
                    a_coefficients = quadratic_coefficients(antidiagonal)
                    types[(d_coefficients, a_coefficients)] += 1
                    family_count += 1
                    valid = (
                        d_coefficients == (sp.Rational(-2), 0, sp.Rational(-2), 0, 0, 0)
                        and a_coefficients[1] != 0
                    )
                    if not valid:
                        failures.append(
                            {
                                "permutation_index": permutation_index,
                                "permutation_one_based": [entry + 1 for entry in permutation],
                                "edges": [edge_name(edge) for edge in edges],
                                "diagonal_coefficients": list(map(qstr, d_coefficients)),
                                "antidiagonal_coefficients": list(map(qstr, a_coefficients)),
                            }
                        )

    type_records = []
    for (d_coefficients, a_coefficients), count in sorted(
        types.items(), key=lambda item: (tuple(map(str, item[0][0])), tuple(map(str, item[0][1])))
    ):
        type_records.append(
            {
                "count": count,
                "monomial_order": ["x^2", "y^2", "z^2", "xy", "xz", "yz"],
                "diagonal_coefficients": list(map(qstr, d_coefficients)),
                "antidiagonal_coefficients": list(map(qstr, a_coefficients)),
            }
        )

    return {
        "permutation_count": len(permutations),
        "edge_choices_per_permutation": 81,
        "family_count": family_count,
        "quadratic_type_count": len(types),
        "failed_certificate_count": len(failures),
        "failures": failures,
        "types": type_records,
        "certificate": {
            "diagonal_quadratic_in_every_family": "-2*x^2-2*z^2",
            "antidiagonal_y_squared_coefficient_never_zero": True,
            "real_tangent_conclusion": (
                "The only common real tangent vector is zero: the diagonal form "
                "forces x=z=0, and then the nonzero y^2 coefficient in the "
                "antidiagonal form forces y=0.  The sequential tangent-cone "
                "criterion therefore makes the anchor an isolated real common zero."
            ),
        },
    }


def selected_edges(slice_index: int, permutation: tuple[int, ...]) -> tuple[tuple[int, int], ...]:
    singleton, first_cycle, second_cycle = components(permutation)
    first_options = [(singleton, vertex) for vertex in first_cycle]
    middle_options = list(itertools.product(first_cycle, second_cycle))
    third_options = [(singleton, vertex) for vertex in second_cycle]
    first = first_options[
        base.digest_integer(f"anchor:{slice_index}:first") % len(first_options)
    ]
    middle = middle_options[
        base.digest_integer(f"anchor:{slice_index}:second") % len(middle_options)
    ]
    third = third_options[
        base.digest_integer(f"anchor3:{slice_index}:third") % len(third_options)
    ]
    return tuple(sorted_edge(*edge) for edge in (first, middle, third))


def rational_grid() -> list[sp.Rational]:
    return sorted(
        {
            sp.Rational(numerator, denominator)
            for denominator in range(1, 7)
            for numerator in range(-12, 13)
            if abs(sp.Rational(numerator, denominator)) <= 3
        },
        key=lambda value: (abs(value), value),
    )


def exact_solution_record(q_matrix: sp.Matrix, values: tuple[sp.Rational, ...]) -> dict:
    evaluated = q_matrix.subs(dict(zip(VARIABLES, values))).applyfunc(sp.cancel)
    if any(not entry.is_Rational for entry in evaluated):
        raise AssertionError("reconstructed matrix was not rational")
    identity = sp.eye(N)
    diagonal_sum = sp.cancel(sum(evaluated[i, i] ** 2 for i in range(N)))
    antidiagonal_sum = sp.cancel(sum(evaluated[i, N - 1 - i] ** 2 for i in range(N)))
    squares = [sp.cancel(entry**2) for entry in evaluated]
    if evaluated * evaluated.T != identity or diagonal_sum != 1 or antidiagonal_sum != 1:
        raise AssertionError("stored solution failed exact Euler verification")
    return {
        "x": qstr(values[0]),
        "y": qstr(values[1]),
        "z": qstr(values[2]),
        "orthogonal": True,
        "diagonal_sum": "1",
        "antidiagonal_sum": "1",
        "distinct_entry_squares": len(set(squares)),
        "proper": len(set(squares)) == N * N,
    }


def analyze_selected_slice(
    slice_index: int,
    permutation: tuple[int, ...],
    grid: list[sp.Rational],
) -> dict:
    identity = sp.eye(N)
    p_matrix = base.permutation_matrix(permutation)
    b_matrix = (identity + p_matrix) / 2
    edges = selected_edges(slice_index, permutation)
    perturbation = sp.zeros(N)
    for edge, variable in zip(edges, VARIABLES):
        add_skew_entry(perturbation, edge, variable)
    q_matrix = 2 * (identity + b_matrix * perturbation).inv(method="DM") * b_matrix - identity
    diagonal = primitive_poly(sum(q_matrix[i, i] ** 2 for i in range(N)) - 1)
    antidiagonal = primitive_poly(
        sum(q_matrix[i, N - 1 - i] ** 2 for i in range(N)) - 1
    )
    if diagonal.eval({X: 0, Y: 0, Z: 0}) or antidiagonal.eval({X: 0, Y: 0, Z: 0}):
        raise AssertionError("selected slice did not pass through its anchor")

    taylor_diagonal, taylor_antidiagonal = taylor_quadratics(permutation, edges)
    if initial_form(diagonal).monic() != taylor_diagonal.monic():
        raise AssertionError("full diagonal equation and Taylor calculation disagree")
    if initial_form(antidiagonal).monic() != taylor_antidiagonal.monic():
        raise AssertionError("full antidiagonal equation and Taylor calculation disagree")

    projection_records = {}
    resultants = {}
    for eliminated in VARIABLES:
        retained = tuple(variable for variable in VARIABLES if variable != eliminated)
        resultant = sp.Poly(
            sp.resultant(diagonal.as_expr(), antidiagonal.as_expr(), eliminated),
            *retained,
            domain=sp.QQ,
        ).primitive()[1]
        resultants[eliminated] = resultant
        projection_records[str(eliminated)] = {
            "retained_variables": list(map(str, retained)),
            "total_degree": int(resultant.total_degree()),
            "term_count": len(resultant.terms()),
            "coefficient_hash": coefficient_hash(resultant),
            "factors_over_Q": factor_degrees(resultant),
        }

    # R_z(x,y)=0 is necessary for a common z.  For every grid pair satisfying
    # it, the specialized gcd finds the common z-polynomial, and its linear
    # factors enumerate all rational z without imposing a z height bound.
    projected_zeros = []
    solutions: set[tuple[sp.Rational, sp.Rational, sp.Rational]] = set()
    z_resultant = resultants[Z]
    for x_value in grid:
        for y_value in grid:
            if z_resultant.eval({X: x_value, Y: y_value}) != 0:
                continue
            f_specialized = sp.Poly(
                diagonal.as_expr().subs({X: x_value, Y: y_value}), Z, domain=sp.QQ
            )
            g_specialized = sp.Poly(
                antidiagonal.as_expr().subs({X: x_value, Y: y_value}), Z, domain=sp.QQ
            )
            common = sp.gcd(f_specialized, g_specialized)
            rational_z = linear_roots(common, Z) if common.degree() > 0 else []
            projected_zeros.append(
                {
                    "x": qstr(x_value),
                    "y": qstr(y_value),
                    "specialized_gcd_degree": int(common.degree()),
                    "rational_z": list(map(qstr, rational_z)),
                }
            )
            for z_value in rational_z:
                if diagonal.eval({X: x_value, Y: y_value, Z: z_value}) != 0:
                    raise AssertionError("enumerated root failed diagonal equation")
                if antidiagonal.eval({X: x_value, Y: y_value, Z: z_value}) != 0:
                    raise AssertionError("enumerated root failed antidiagonal equation")
                solutions.add((x_value, y_value, z_value))

    return {
        "slice_id": f"anchor-triangle-{slice_index:03d}",
        "anchor_permutation_one_based": [entry + 1 for entry in permutation],
        "active_parameters": [edge_name(edge) for edge in edges],
        "diagonal_numerator": {
            "total_degree": int(diagonal.total_degree()),
            "term_count": len(diagonal.terms()),
            "coefficient_hash": coefficient_hash(diagonal),
        },
        "antidiagonal_numerator": {
            "total_degree": int(antidiagonal.total_degree()),
            "term_count": len(antidiagonal.terms()),
            "coefficient_hash": coefficient_hash(antidiagonal),
        },
        "tangent_quadratics": {
            "monomial_order": ["x^2", "y^2", "z^2", "xy", "xz", "yz"],
            "diagonal_coefficients": list(map(qstr, quadratic_coefficients(taylor_diagonal))),
            "antidiagonal_coefficients": list(map(qstr, quadratic_coefficients(taylor_antidiagonal))),
        },
        "coordinate_projection_resultants": projection_records,
        "grid_projected_zero_count": len(projected_zeros),
        "grid_projected_zeros": projected_zeros,
        "rational_solutions": [
            exact_solution_record(q_matrix, values)
            for values in sorted(solutions, key=lambda triple: tuple(map(str, triple)))
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    permutations = base.valid_anchor_permutations()
    if len(permutations) != 112:
        raise AssertionError("unexpected number of valid permutation anchors")
    grid = rational_grid()
    census = tangent_census(permutations)
    if census["failed_certificate_count"]:
        raise AssertionError("tangent isolation certificate failed")

    selected = []
    for index, permutation in enumerate(permutations[:50]):
        print(f"[{index + 1:02d}/50] anchor-triangle-{index:03d}", flush=True)
        selected.append(analyze_selected_slice(index, permutation, grid))

    all_solutions = [solution for record in selected for solution in record["rational_solutions"]]
    non_anchor_solutions = [
        solution
        for solution in all_solutions
        if (solution["x"], solution["y"], solution["z"]) != ("0", "0", "0")
    ]
    all_projection_factors = [
        factor
        for record in selected
        for projection in record["coordinate_projection_resultants"].values()
        for factor in projection["factors_over_Q"]
    ]
    output = {
        "schema": "win-00039-p12/exact-cayley-triangles/v1",
        "purpose": (
            "Exact local obstruction and full-equation tests for three-coordinate "
            "Cayley triangle families through unsigned permutation Euler points"
        ),
        "deterministic_seed": SEED,
        "software": {"python": platform.python_version(), "sympy": sp.__version__},
        "method": {
            "parameterization": "Q=2*(I+B*E)^(-1)*B-I with B=(I+P)/2",
            "permutation_filter": (
                "all permutations of 0,...,6 with one fixed point, one "
                "antidiagonal hit, and cycle type 1+3+3"
            ),
            "triangle_edges": (
                "x joins singleton to first 3-cycle; y joins first to second "
                "3-cycle; z joins singleton to second 3-cycle"
            ),
            "factorization_domain": "QQ",
            "selected_full_slice_count": 50,
            "grid_definition": (
                "reduced rationals p/q with -12<=p<=12, 1<=q<=6, and |p/q|<=3"
            ),
            "grid_value_count": len(grid),
            "grid_projected_pair_count_per_slice": len(grid) ** 2,
            "z_coverage": (
                "for each screened (x,y), every rational z is enumerated from "
                "linear factors of the specialized gcd; z is unbounded"
            ),
            "scope_warning": (
                "The tangent certificate is local to the stated affine "
                "three-coordinate families.  Projection irreducibility and the "
                "bounded (x,y) screen do not prove global nonexistence or positive genus."
            ),
        },
        "tangent_census": census,
        "summary": {
            "full_slice_count": len(selected),
            "coordinate_projection_resultant_count": 3 * len(selected),
            "irreducible_coordinate_projection_resultant_count": sum(
                len(projection["factors_over_Q"]) == 1
                and projection["factors_over_Q"][0]["multiplicity"] == 1
                for record in selected
                for projection in record["coordinate_projection_resultants"].values()
            ),
            "minimum_projection_factor_degree": min(
                factor["total_degree"] for factor in all_projection_factors
            ),
            "rational_solution_count_with_slice_multiplicity": len(all_solutions),
            "non_anchor_rational_solution_count_with_slice_multiplicity": len(non_anchor_solutions),
            "proper_solution_count_with_slice_multiplicity": sum(
                solution["proper"] for solution in all_solutions
            ),
            "best_distinct_entry_squares": max(
                (solution["distinct_entry_squares"] for solution in all_solutions),
                default=None,
            ),
        },
        "selected_slices": selected,
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps(output["summary"], sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
