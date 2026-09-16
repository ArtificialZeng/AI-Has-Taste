#!/usr/bin/env python3
"""Exact Hilbert-basis and support audit for one fixed sign chamber.

Run from the project root with the separately supplied PyNormaliz installation:

    PYTHONPATH=/home/ailab/4math-open-problems/tools/pynormaliz \
      python3 evidence/verify_chamber_hilbert.py \
      --output evidence/chamber-hilbert-basis.json

All cone and polynomial-support calculations use integers or exact rationals.
The Normaliz Hilbert basis is computed twice, from independently reconstructed
V- and H-representations of the same cone, and every returned vector is then
checked directly in the saturated balanced lattice and against every defining
inequality.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
import math
from collections import Counter
from pathlib import Path

import PyNormaliz
import sympy as sp
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
from sympy.polys.domains import ZZ

from verify_sign_chamber import (
    H4,
    alpha_label,
    cut_cone,
    dot,
    enumerate_facets,
    exact_rank,
    support_audit,
    triangular_rays,
)


SOURCE_SHA256 = "8c450171f5fe6b12b21014c3e96e060d54fedb1b3e3418de1d26ada9d4921dab"
SIGN_PATTERN = "+++++--+++++-++"


def source_hash() -> str:
    return hashlib.sha256(Path("source.md").read_bytes()).hexdigest()


def lattice_and_chamber():
    """Reconstruct the saturated lattice and the fixed closed chamber."""
    rays, names = triangular_rays()
    ray_matrix = sp.Matrix(rays).T
    balance_matrix = sp.Matrix([[alpha[i] for alpha in H4] for i in range(3)])
    assert balance_matrix.rank() == 3
    assert ray_matrix.rank() == 12
    assert balance_matrix * ray_matrix == sp.zeros(3, 18)

    smith = smith_normal_form(ray_matrix, domain=ZZ)
    smith_invariants = tuple(
        abs(int(smith[i, i]))
        for i in range(min(smith.shape))
        if smith[i, i] != 0
    )
    assert smith_invariants == (1,) * 12

    # The columns are therefore a Z-basis of ker(balance_matrix) cap Z^15.
    lattice_basis = hermite_normal_form(ray_matrix)
    assert lattice_basis.shape == (15, 12)
    assert balance_matrix * lattice_basis == sp.zeros(3, 12)

    ray_coordinates = []
    for ray in rays:
        solutions = sp.linsolve((lattice_basis, sp.Matrix(ray)))
        solution = next(iter(solutions))
        assert all(entry.q == 1 for entry in solution)
        coordinate_vector = tuple(int(entry) for entry in solution)
        assert tuple(lattice_basis * sp.Matrix(coordinate_vector)) == ray
        ray_coordinates.append(coordinate_vector)
    ray_coordinates = tuple(ray_coordinates)

    facets = enumerate_facets(ray_coordinates)
    assert len(facets) == 18
    chamber_rays = ray_coordinates
    chamber_inequalities = facets
    sign_inequalities = []
    for coordinate, character in enumerate(SIGN_PATTERN):
        sign = 1 if character == "+" else -1
        inequality = tuple(
            sign * int(lattice_basis[coordinate, column])
            for column in range(12)
        )
        sign_inequalities.append(inequality)
        chamber_rays, chamber_inequalities = cut_cone(
            chamber_rays, chamber_inequalities, inequality
        )

    assert len(chamber_rays) == 48
    assert exact_rank(chamber_rays) == 12
    assert all(
        dot(inequality, ray) >= 0
        for inequality in chamber_inequalities
        for ray in chamber_rays
    )
    return {
        "rays": rays,
        "ray_names": names,
        "lattice_basis": lattice_basis,
        "smith_invariants": smith_invariants,
        "original_facets": facets,
        "sign_inequalities": tuple(sign_inequalities),
        "chamber_inequalities": chamber_inequalities,
        "chamber_rays": chamber_rays,
    }


def normaliz_hilbert_basis(chamber):
    """Cross-check the Hilbert basis from exact V- and H-descriptions."""
    rays = chamber["chamber_rays"]
    inequalities = chamber["chamber_inequalities"]
    cone_v = PyNormaliz.Cone(cone=[list(ray) for ray in rays])
    cone_h = PyNormaliz.Cone(
        inequalities=[list(inequality) for inequality in inequalities]
    )

    hilbert_v = tuple(sorted(map(tuple, cone_v.HilbertBasis())))
    hilbert_h = tuple(sorted(map(tuple, cone_h.HilbertBasis())))
    extreme_v = tuple(sorted(map(tuple, cone_v.ExtremeRays())))
    extreme_h = tuple(sorted(map(tuple, cone_h.ExtremeRays())))
    support_v = tuple(sorted(map(tuple, cone_v.SupportHyperplanes())))
    support_h = tuple(sorted(map(tuple, cone_h.SupportHyperplanes())))

    assert cone_v.Rank() == cone_h.Rank() == 12
    assert cone_v.IsPointed() and cone_h.IsPointed()
    assert hilbert_v == hilbert_h
    assert extreme_v == extreme_h == tuple(sorted(rays))
    assert support_v == support_h
    assert len(support_v) == 15
    assert len(hilbert_v) == 134
    assert len(set(hilbert_v)) == len(hilbert_v)
    assert (0,) * 12 not in hilbert_v
    return hilbert_v, support_v


def validate_and_support_test(chamber, hilbert_basis):
    """Directly validate all returned generators and audit their supports."""
    lattice_basis = chamber["lattice_basis"]
    inequalities = chamber["chamber_inequalities"]
    balance_matrix = sp.Matrix([[alpha[i] for alpha in H4] for i in range(3)])
    extreme_set = set(chamber["chamber_rays"])
    gammas = []
    for vector in hilbert_basis:
        assert len(vector) == 12
        assert all(isinstance(entry, int) for entry in vector)
        assert math.gcd(*(abs(entry) for entry in vector)) == 1
        assert all(dot(inequality, vector) >= 0 for inequality in inequalities)

        gamma = tuple(int(entry) for entry in lattice_basis * sp.Matrix(vector))
        assert tuple(balance_matrix * sp.Matrix(gamma)) == (0, 0, 0)
        assert all(
            entry >= 0 if SIGN_PATTERN[index] == "+" else entry <= 0
            for index, entry in enumerate(gamma)
        )
        recovered = next(iter(sp.linsolve((lattice_basis, sp.Matrix(gamma)))))
        assert tuple(int(entry) for entry in recovered) == vector
        gammas.append(gamma)

    records = support_audit(gammas)
    assert len(records) == len(hilbert_basis)
    assert all(record["missing_count"] == 0 for record in records)
    for vector, record in zip(hilbert_basis, records):
        record["lattice_coordinates"] = list(vector)
        record["is_extreme_ray"] = vector in extreme_set

    degrees = Counter(record["positive_degree"] for record in records)
    return records, degrees


def build_result():
    assert source_hash() == SOURCE_SHA256
    chamber = lattice_and_chamber()
    hilbert_basis, support_hyperplanes = normaliz_hilbert_basis(chamber)
    records, degrees = validate_and_support_test(chamber, hilbert_basis)
    extreme_count = sum(record["is_extreme_ray"] for record in records)
    assert extreme_count == 48

    return {
        "arithmetic": "exact integers/rationals; Normaliz exact affine monoid computation",
        "source_sha256": SOURCE_SHA256,
        "pynormaliz_version": importlib.metadata.version("pynormaliz"),
        "H4_order": [alpha_label(alpha) for alpha in H4],
        "balanced_lattice_rank": 12,
        "ray_lattice_smith_invariants": list(chamber["smith_invariants"]),
        "balanced_lattice_basis_rows": [
            [int(chamber["lattice_basis"][row, column]) for column in range(12)]
            for row in range(15)
        ],
        "sign_pattern": SIGN_PATTERN,
        "input_cone_facets": len(chamber["original_facets"]),
        "input_sign_inequalities": len(chamber["sign_inequalities"]),
        "defining_chamber_inequalities": [
            list(inequality) for inequality in chamber["chamber_inequalities"]
        ],
        "irredundant_chamber_support_hyperplanes": len(support_hyperplanes),
        "irredundant_support_hyperplanes": [
            list(inequality) for inequality in support_hyperplanes
        ],
        "chamber_extreme_rays": len(chamber["chamber_rays"]),
        "chamber_extreme_ray_lattice_coordinates": [
            list(ray) for ray in chamber["chamber_rays"]
        ],
        "hilbert_basis_size": len(hilbert_basis),
        "hilbert_basis_extreme_rays": extreme_count,
        "hilbert_basis_nonray_elements": len(hilbert_basis) - extreme_count,
        "positive_degree_distribution": {
            str(degree): count for degree, count in sorted(degrees.items())
        },
        "support_failures": sum(
            record["missing_count"] > 0 for record in records
        ),
        "maximum_numerator_support_size": max(
            record["numerator_support_size"] for record in records
        ),
        "maximum_denominator_support_size": max(
            record["denominator_support_size"] for record in records
        ),
        "cross_checks": {
            "V_and_H_normaliz_hilbert_bases_equal": True,
            "V_and_H_normaliz_extreme_rays_equal": True,
            "V_and_H_normaliz_support_hyperplanes_equal": True,
            "all_generators_in_saturated_balanced_lattice": True,
            "all_generators_satisfy_every_chamber_inequality": True,
            "all_generators_have_selected_coordinate_signs": True,
            "all_generators_pass_exact_support_containment": True,
        },
        "hilbert_basis_records": records,
        "scope": (
            "The complete affine semigroup of the single closed sign chamber "
            "+++++--+++++-++ inside BR_Q(4,3), not the other 4,073 strict "
            "sign chambers and not the full original conjecture."
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rendered = json.dumps(build_result(), indent=2, sort_keys=True) + "\n"
    if args.output is None:
        print(rendered, end="")
    else:
        args.output.write_text(rendered, encoding="utf-8")
        print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
