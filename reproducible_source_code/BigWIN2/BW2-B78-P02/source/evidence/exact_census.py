#!/usr/bin/env python3
"""Exact exhaustive census for the frozen six-complex sensitivity question.

The program enumerates every orbit under X<->Y, applies the three frozen
retention filters, and computes every relevant inverse cofactor after
restriction to S v = 0.  All arithmetic after enumeration is over QQ.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from itertools import combinations
from math import comb, gcd
from pathlib import Path

import sympy as sp


COMPLEXES = ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2))
COMPLEX_NAMES = ("0", "X", "Y", "2X", "X+Y", "2Y")
TAU = (0, 2, 1, 5, 4, 3)
EDGES = tuple((i, j) for i in range(6) for j in range(6) if i != j)
SPECIES = ("X", "Y")


def qstr(value: sp.Rational | int) -> str:
    value = sp.Rational(value)
    return str(value.p) if value.q == 1 else f"{value.p}/{value.q}"


def qmatrix(matrix: sp.Matrix) -> list[list[str]]:
    return [[qstr(matrix[i, j]) for j in range(matrix.cols)]
            for i in range(matrix.rows)]


def edge_text(edge: tuple[int, int]) -> str:
    return f"{COMPLEX_NAMES[edge[0]]}->{COMPLEX_NAMES[edge[1]]}"


def move_network(network: tuple[tuple[int, int], ...]) -> tuple[tuple[int, int], ...]:
    return tuple(sorted((TAU[i], TAU[j]) for i, j in network))


def canonical_networks() -> tuple[list[tuple[tuple[int, int], ...]], int]:
    representatives: set[tuple[tuple[int, int], ...]] = set()
    fixed = 0
    for size in (3, 4):
        for network in combinations(EDGES, size):
            image = move_network(network)
            fixed += network == image
            representatives.add(min(network, image))
    ordered = sorted(representatives)
    assert sum(comb(30, size) for size in (3, 4)) == 31465
    assert fixed == 133
    assert len(ordered) == 15799
    return ordered, fixed


def matrices(network: tuple[tuple[int, int], ...]) -> tuple[sp.Matrix, sp.Matrix]:
    sources = sp.Matrix(2, len(network),
                        lambda m, j: COMPLEXES[network[j][0]][m])
    stoich = sp.Matrix(2, len(network),
                       lambda m, j: (COMPLEXES[network[j][1]][m]
                                     - COMPLEXES[network[j][0]][m]))
    return stoich, sources


def integer_gale(stoich: sp.Matrix) -> sp.Matrix:
    """Return SymPy's deterministic rational null basis, primitively scaled."""
    basis = stoich.nullspace()
    assert len(basis) == stoich.cols - 2
    columns = []
    for column in basis:
        denominators = [int(sp.denom(x)) for x in column]
        scale = 1
        for denominator in denominators:
            scale = scale * denominator // gcd(scale, denominator)
        entries = [int(x * scale) for x in column]
        divisor = 0
        for entry in entries:
            divisor = gcd(divisor, abs(entry))
        entries = [entry // divisor for entry in entries]
        first = next(entry for entry in entries if entry)
        if first < 0:
            entries = [-entry for entry in entries]
        columns.append(sp.Matrix(entries))
    gale = sp.Matrix.hstack(*columns)
    assert stoich * gale == sp.zeros(2, gale.cols)
    return gale


def _strict_interval_witness(gale: sp.Matrix, z0: int) -> sp.Matrix | None:
    lower: sp.Rational | None = None
    upper: sp.Rational | None = None
    for row in range(gale.rows):
        a, b = gale[row, 0], gale[row, 1]
        constant = a * z0
        if b > 0:
            bound = -constant / b
            lower = bound if lower is None else max(lower, bound)
        elif b < 0:
            bound = -constant / b
            upper = bound if upper is None else min(upper, bound)
        elif constant <= 0:
            return None
    if lower is not None and upper is not None and lower >= upper:
        return None
    if lower is None and upper is None:
        z1 = sp.Rational(0)
    elif lower is None:
        z1 = upper - 1
    elif upper is None:
        z1 = lower + 1
    else:
        z1 = (lower + upper) / 2
    z = sp.Matrix([z0, z1])
    return z if all(value > 0 for value in gale * z) else None


def positive_flux(gale: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix] | None:
    """Find an exact strictly positive kernel vector, or certify none exists.

    For nullity one there are only the two orientations.  For nullity two,
    every feasible open cone with z_0 != 0 meets z_0=+/-1; strict feasibility
    at z_0=0 also has a nearby point with z_0 != 0.  Exact open-interval
    arithmetic therefore decides the system of homogeneous inequalities.
    """
    if gale.cols == 1:
        for sign in (1, -1):
            z = sp.Matrix([sign])
            flux = gale * z
            if all(value > 0 for value in flux):
                return z, flux
        return None
    assert gale.cols == 2
    for z0 in (1, -1):
        z = _strict_interval_witness(gale, z0)
        if z is not None:
            return z, gale * z
    return None


def generic_determinant_terms(stoich: sp.Matrix, sources: sp.Matrix) -> list[dict]:
    terms = []
    for j in range(stoich.cols):
        if sources[0, j] == 0:
            continue
        for k in range(stoich.cols):
            if sources[1, k] == 0:
                continue
            coefficient = stoich[0, j] * stoich[1, k] - stoich[1, j] * stoich[0, k]
            if coefficient:
                terms.append({"rx_row": j, "ry_row": k, "coefficient": qstr(coefficient)})
    return terms


def cofactor_data(stoich: sp.Matrix, sources: sp.Matrix, gale: sp.Matrix,
                  reaction_row: int, species: int) -> dict:
    """Compute one signed adjugate cofactor and its restriction to ker(S)."""
    q = stoich.cols
    other = 1 - species
    rows = [row for row in range(q) if row != reaction_row]
    generic_terms = []
    specialized_coefficients = [sp.Rational(0) for _ in range(q)]
    cofactor_sign = -1 if (reaction_row + species) % 2 else 1

    for variable_row in rows:
        if sources[other, variable_row] == 0:
            continue
        first_column = [sp.Integer(row == variable_row) for row in rows]
        minor = sp.Matrix([[first_column[i]] + [gale[row, col] for col in range(gale.cols)]
                           for i, row in enumerate(rows)])
        coefficient = cofactor_sign * minor.det()
        if coefficient:
            generic_terms.append({
                "row": variable_row,
                "variable": f"r_{variable_row}_{SPECIES[other]}",
                "coefficient": qstr(coefficient),
            })
            specialized_coefficients[variable_row] = coefficient * sources[other, variable_row]

    normal_form = []
    for col in range(gale.cols):
        normal_form.append(sum(specialized_coefficients[row] * gale[row, col]
                               for row in range(q)))

    result = {
        "reaction_row": reaction_row,
        "species": SPECIES[species],
        "generic_terms": generic_terms,
        "generic_nonzero": bool(generic_terms),
        "mass_action_coefficients_in_v": [qstr(x) for x in specialized_coefficients],
        "mass_action_normal_form_in_z": [qstr(x) for x in normal_form],
        "mass_action_identically_zero": bool(generic_terms) and all(x == 0 for x in normal_form),
    }

    if result["mass_action_identically_zero"]:
        pivot_pair = next((pair for pair in combinations(range(q), 2)
                           if stoich[:, pair].det() != 0), None)
        assert pivot_pair is not None
        j, k = pivot_pair
        system = sp.Matrix([[stoich[0, j], stoich[1, j]],
                            [stoich[0, k], stoich[1, k]]])
        rhs = sp.Matrix([specialized_coefficients[j], specialized_coefficients[k]])
        multipliers = system.inv() * rhs
        assert all(specialized_coefficients[row]
                   == multipliers[0] * stoich[0, row] + multipliers[1] * stoich[1, row]
                   for row in range(q))
        result["ideal_identity_multipliers"] = [qstr(x) for x in multipliers]
    return result


def polynomial_terms(expression: sp.Expr, variables: tuple[sp.Symbol, ...]) -> list[dict]:
    polynomial = sp.Poly(sp.expand(expression), *variables, domain=sp.QQ)
    return [{"exponents": list(monomial), "coefficient": qstr(coefficient)}
            for monomial, coefficient in polynomial.terms() if coefficient]


def mass_action_determinant(sources: sp.Matrix, gale: sp.Matrix) -> list[dict]:
    variables = sp.symbols(f"z0:{gale.cols}")
    z = sp.Matrix(variables)
    flux = gale * z
    matrix = sp.Matrix([
        [flux[row] * sources[0, row], flux[row] * sources[1, row]]
        + [gale[row, col] for col in range(gale.cols)]
        for row in range(gale.rows)
    ])
    return polynomial_terms(matrix.det(), variables)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def run(manifest_path: Path, summary_path: Path) -> dict:
    networks, fixed = canonical_networks()
    counts = {
        "labelled_networks": 31465,
        "swap_fixed_networks": fixed,
        "canonical_orbits": len(networks),
        "rank_two": 0,
        "positive_kernel": 0,
        "generic_determinant_nonzero": 0,
        "retained": 0,
        "mass_action_determinant_zero": 0,
        "generic_nonzero_pairs": 0,
        "additional_mass_action_zero_pairs": 0,
    }
    first_witness = None
    first_witness_orbit = None
    first_witness_pair_index = None

    with manifest_path.open("w", encoding="utf-8", newline="\n") as manifest:
        for orbit_index, network in enumerate(networks):
            stoich, sources = matrices(network)
            rank_two = stoich.rank() == 2
            record = {
                "orbit_index": orbit_index,
                "network": [list(edge) for edge in network],
                "network_text": [edge_text(edge) for edge in network],
                "rank_two": rank_two,
            }
            if not rank_two:
                record["retained"] = False
                record["rejection"] = "rank"
                manifest.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")
                continue
            counts["rank_two"] += 1
            gale = integer_gale(stoich)
            positive = positive_flux(gale)
            record["positive_kernel"] = positive is not None
            if positive is None:
                record["retained"] = False
                record["rejection"] = "strict_positive_kernel"
                record["gale"] = qmatrix(gale)
                manifest.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")
                continue
            counts["positive_kernel"] += 1
            z_witness, flux_witness = positive
            generic_det_terms = generic_determinant_terms(stoich, sources)
            record["generic_determinant_nonzero"] = bool(generic_det_terms)
            if not generic_det_terms:
                record["retained"] = False
                record["rejection"] = "generic_determinant"
                record["gale"] = qmatrix(gale)
                record["positive_z"] = [qstr(x) for x in z_witness]
                record["positive_flux"] = [qstr(x) for x in flux_witness]
                manifest.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")
                continue
            counts["generic_determinant_nonzero"] += 1
            counts["retained"] += 1
            determinant_terms = mass_action_determinant(sources, gale)
            determinant_nonzero = bool(determinant_terms)
            if not determinant_nonzero:
                counts["mass_action_determinant_zero"] += 1

            pairs = []
            for reaction_row in range(len(network)):
                for species in range(2):
                    pair = cofactor_data(stoich, sources, gale, reaction_row, species)
                    pair["reaction"] = list(network[reaction_row])
                    pair["reaction_text"] = edge_text(network[reaction_row])
                    if pair["generic_nonzero"]:
                        counts["generic_nonzero_pairs"] += 1
                    is_witness = (pair["mass_action_identically_zero"] and determinant_nonzero)
                    pair["is_witness"] = is_witness
                    if is_witness:
                        counts["additional_mass_action_zero_pairs"] += 1
                        if first_witness is None:
                            first_witness = {
                                "orbit_index": orbit_index,
                                "network": [list(edge) for edge in network],
                                "network_text": [edge_text(edge) for edge in network],
                                "reaction_row": reaction_row,
                                "reaction": list(network[reaction_row]),
                                "reaction_text": edge_text(network[reaction_row]),
                                "species": SPECIES[species],
                                "stoichiometric_matrix": qmatrix(stoich),
                                "source_matrix": qmatrix(sources),
                                "gale": qmatrix(gale),
                                "positive_z": [qstr(x) for x in z_witness],
                                "positive_flux": [qstr(x) for x in flux_witness],
                                "generic_determinant_terms": generic_det_terms,
                                "mass_action_determinant_in_z": determinant_terms,
                                "pair_certificate": pair,
                            }
                            first_witness_orbit = orbit_index
                            first_witness_pair_index = 2 * reaction_row + species
                    pairs.append(pair)

            record.update({
                "retained": True,
                "stoichiometric_matrix": qmatrix(stoich),
                "source_matrix": qmatrix(sources),
                "gale": qmatrix(gale),
                "positive_z": [qstr(x) for x in z_witness],
                "positive_flux": [qstr(x) for x in flux_witness],
                "generic_determinant_terms": generic_det_terms,
                "mass_action_determinant_in_z": determinant_terms,
                "mass_action_determinant_nonzero": determinant_nonzero,
                "pairs": pairs,
            })
            manifest.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")

    manifest_hash = sha256(manifest_path)
    summary = {
        "arithmetic": "exact rational/integer arithmetic via SymPy QQ",
        "canonical_order": "sorted reaction tuples, then reaction row, then X<Y",
        "counts": counts,
        "first_witness": first_witness,
        "first_witness_orbit_index": first_witness_orbit,
        "first_witness_pair_index_within_orbit": first_witness_pair_index,
        "manifest_file": manifest_path.as_posix(),
        "manifest_sha256": manifest_hash,
    }
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=Path("evidence/census-manifest.jsonl"))
    parser.add_argument("--summary", type=Path, default=Path("evidence/census-summary.json"))
    arguments = parser.parse_args()
    summary = run(arguments.manifest, arguments.summary)
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
