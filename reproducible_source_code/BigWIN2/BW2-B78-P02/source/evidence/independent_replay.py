#!/usr/bin/env python3
"""Independent exact replay of the lexicographically first census witness.

This verifier intentionally does not import exact_census.py or SymPy.  It uses
Fraction Gaussian elimination and direct determinant/cofactor formulas.
"""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path


COMPLEXES = ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2))
TAU = (0, 2, 1, 5, 4, 3)
EDGES = tuple((i, j) for i in range(6) for j in range(6) if i != j)
TARGET = ((0, 1), (0, 3), (1, 2), (4, 0))
TARGET_PAIR = (0, 1)  # reaction row 0, species Y


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def determinant(matrix: list[list[F]]) -> F:
    work = [row[:] for row in matrix]
    result = F(1)
    size = len(work)
    for col in range(size):
        pivot = next((row for row in range(col, size) if work[row][col]), None)
        if pivot is None:
            return F(0)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            result = -result
        value = work[col][col]
        result *= value
        for row in range(col + 1, size):
            factor = work[row][col] / value
            for k in range(col + 1, size):
                work[row][k] -= factor * work[col][k]
    return result


def null_basis(stoich: list[list[F]]) -> tuple[int, list[list[F]]]:
    """RREF null basis as rows (one row for each reaction)."""
    work = [row[:] for row in stoich]
    row = 0
    pivots: list[int] = []
    for col in range(len(work[0])):
        pivot = next((r for r in range(row, 2) if work[r][col]), None)
        if pivot is None:
            continue
        work[row], work[pivot] = work[pivot], work[row]
        value = work[row][col]
        work[row] = [x / value for x in work[row]]
        for r in range(2):
            if r != row and work[r][col]:
                factor = work[r][col]
                work[r] = [work[r][k] - factor * work[row][k]
                           for k in range(len(work[0]))]
        pivots.append(col)
        row += 1
        if row == 2:
            break
    rank = len(pivots)
    free = [col for col in range(len(work[0])) if col not in pivots]
    basis = [[F(0) for _ in free] for _ in range(len(work[0]))]
    for basis_col, free_col in enumerate(free):
        basis[free_col][basis_col] = F(1)
        for pivot_row, pivot_col in enumerate(pivots):
            basis[pivot_col][basis_col] = -work[pivot_row][free_col]
    return rank, basis


def exact_positive_kernel(gale: list[list[F]]) -> list[F] | None:
    dimension = len(gale[0])
    if dimension == 1:
        for sign in (F(1), F(-1)):
            flux = [row[0] * sign for row in gale]
            if all(x > 0 for x in flux):
                return flux
        return None
    assert dimension == 2
    for z0 in (F(1), F(-1)):
        lower = None
        upper = None
        impossible = False
        for a, b in gale:
            constant = a * z0
            if b > 0:
                bound = -constant / b
                lower = bound if lower is None else max(lower, bound)
            elif b < 0:
                bound = -constant / b
                upper = bound if upper is None else min(upper, bound)
            elif constant <= 0:
                impossible = True
                break
        if impossible or (lower is not None and upper is not None and lower >= upper):
            continue
        if lower is None and upper is None:
            z1 = F(0)
        elif lower is None:
            z1 = upper - 1
        elif upper is None:
            z1 = lower + 1
        else:
            z1 = (lower + upper) / 2
        flux = [a * z0 + b * z1 for a, b in gale]
        if all(x > 0 for x in flux):
            return flux
    return None


def matrices(network: tuple[tuple[int, int], ...]) -> tuple[list[list[F]], list[list[F]]]:
    q = len(network)
    sources = [[F(COMPLEXES[network[j][0]][m]) for j in range(q)] for m in range(2)]
    stoich = [[F(COMPLEXES[network[j][1]][m] - COMPLEXES[network[j][0]][m])
               for j in range(q)] for m in range(2)]
    return stoich, sources


def generic_det_nonzero(stoich: list[list[F]], sources: list[list[F]]) -> bool:
    q = len(stoich[0])
    return any(sources[0][j] and sources[1][k]
               and stoich[0][j] * stoich[1][k] - stoich[1][j] * stoich[0][k]
               for j in range(q) for k in range(q))


def cofactor(stoich: list[list[F]], sources: list[list[F]], gale: list[list[F]],
             reaction_row: int, species: int) -> tuple[bool, list[F], list[F]]:
    q = len(stoich[0])
    other = 1 - species
    kept_rows = [row for row in range(q) if row != reaction_row]
    sign = F(-1 if (reaction_row + species) % 2 else 1)
    generic = False
    coefficients = [F(0) for _ in range(q)]
    for variable_row in kept_rows:
        if not sources[other][variable_row]:
            continue
        matrix = []
        for row in kept_rows:
            matrix.append([F(row == variable_row)] + gale[row][:])
        value = sign * determinant(matrix)
        if value:
            generic = True
            coefficients[variable_row] = value * sources[other][variable_row]
    normal_form = [sum(coefficients[row] * gale[row][col] for row in range(q))
                   for col in range(len(gale[0]))]
    return generic, coefficients, normal_form


def mass_det_nonzero(stoich: list[list[F]], sources: list[list[F]],
                     gale: list[list[F]]) -> bool:
    """Test det(S R_MA) on v=Gz; det([R_MA|G]) differs by a nonzero scalar."""
    d = len(gale[0])
    linear = [[[sum(stoich[a][j] * sources[m][j] * gale[j][ell]
                       for j in range(len(gale)))
                for ell in range(d)] for m in range(2)] for a in range(2)]
    coefficients = {}
    for i in range(d):
        for j in range(d):
            exponent = tuple((1 if ell == i else 0) + (1 if ell == j else 0)
                             for ell in range(d))
            coefficients[exponent] = coefficients.get(exponent, F(0)) + (
                linear[0][0][i] * linear[1][1][j]
                - linear[0][1][i] * linear[1][0][j]
            )
    return any(coefficients.values())


def classify(network: tuple[tuple[int, int], ...]) -> tuple[bool, list[tuple[int, int]]]:
    stoich, sources = matrices(network)
    rank, gale = null_basis(stoich)
    if rank != 2 or exact_positive_kernel(gale) is None or not generic_det_nonzero(stoich, sources):
        return False, []
    det_ok = mass_det_nonzero(stoich, sources, gale)
    witnesses = []
    for reaction_row in range(len(network)):
        for species in range(2):
            generic, _, normal_form = cofactor(stoich, sources, gale, reaction_row, species)
            if generic and not any(normal_form) and det_ok:
                witnesses.append((reaction_row, species))
    return True, witnesses


def main() -> None:
    representatives = set()
    fixed = 0
    for size in (3, 4):
        for network in combinations(EDGES, size):
            image = tuple(sorted((TAU[i], TAU[j]) for i, j in network))
            fixed += network == image
            representatives.add(min(network, image))
    ordered = sorted(representatives)
    target_index = ordered.index(TARGET)
    assert (len(ordered), fixed, target_index) == (15799, 133, 303)

    retained_prefix = 0
    prefix_generic_pairs = 0
    prefix_witnesses = []
    for orbit_index, network in enumerate(ordered[:target_index + 1]):
        retained, witnesses = classify(network)
        retained_prefix += retained
        stoich, sources = matrices(network)
        rank, gale = null_basis(stoich)
        if retained:
            for reaction_row in range(len(network)):
                for species in range(2):
                    generic, _, _ = cofactor(stoich, sources, gale, reaction_row, species)
                    prefix_generic_pairs += generic
        for pair in witnesses:
            prefix_witnesses.append((orbit_index, pair))

    # There is no witness in an earlier orbit or at the earlier pair (row 0,X).
    # The same target network also has a later witness at (row 1,Y), which does
    # not affect the requested lexicographic minimum.
    assert prefix_witnesses == [(303, TARGET_PAIR), (303, (1, 1))]
    assert prefix_witnesses[0] == (303, TARGET_PAIR)

    stoich, sources = matrices(TARGET)
    rank, gale = null_basis(stoich)
    generic, coefficients, normal_form = cofactor(stoich, sources, gale, *TARGET_PAIR)
    flux = [F(2), F(1), F(2), F(2)]
    residual = [sum(stoich[m][j] * flux[j] for j in range(4)) for m in range(2)]
    assert rank == 2 and generic and normal_form == [F(0), F(0)]
    # This verifier's first Gale column is the negative of the census basis,
    # so both determinant and cofactor have the opposite harmless scale.
    assert coefficients == [F(0), F(0), F(1), F(-1)]
    assert residual == [F(0), F(0)] and all(x > 0 for x in flux)

    # Direct matrices at the positive flux: determinant 8 and signed cofactor 0.
    mass_matrix = [
        [flux[row] * sources[0][row], flux[row] * sources[1][row]] + gale[row]
        for row in range(4)
    ]
    direct_det = determinant(mass_matrix)
    kept = [1, 2, 3]
    direct_minor = [[mass_matrix[row][col] for col in (0, 2, 3)] for row in kept]
    signed_cofactor = -determinant(direct_minor)
    assert direct_det != 0 and signed_cofactor == 0

    manifest = Path("evidence/census-manifest.jsonl")
    source = Path("source.md")
    report = {
        "method": "independent Fraction Gaussian elimination and direct determinant formulas",
        "source_sha256": sha256(source),
        "manifest_sha256": sha256(manifest),
        "canonical_orbits": len(ordered),
        "target_orbit_index": target_index,
        "orbits_replayed_through_target": target_index + 1,
        "retained_orbits_through_target": retained_prefix,
        "generic_nonzero_pairs_through_target": prefix_generic_pairs,
        "witnesses_through_target": [[index, list(pair)] for index, pair in prefix_witnesses],
        "first_witness_in_frozen_order": [303, list(TARGET_PAIR)],
        "target_network": [list(edge) for edge in TARGET],
        "target_pair": {"reaction_row": 0, "species": "Y"},
        "target_stoichiometric_matrix": [[str(x) for x in row] for row in stoich],
        "target_gale_basis": [[str(x) for x in row] for row in gale],
        "positive_flux": [str(x) for x in flux],
        "steady_state_residual": [str(x) for x in residual],
        "specialized_cofactor_coefficients_in_v": [str(x) for x in coefficients],
        "specialized_cofactor_normal_form": [str(x) for x in normal_form],
        "ideal_identity": "v_2-v_3 = (Sv)_Y (opposite Gale orientation from census)",
        "direct_mass_action_determinant_at_positive_flux": str(direct_det),
        "direct_signed_cofactor_at_positive_flux": str(signed_cofactor),
    }
    output = Path("evidence/independent-replay.json")
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
