#!/usr/bin/env python3
"""Exact CP-SAT optimization of the frozen three-family product.

The model has one Boolean variable for each of the 155 vertices in each of
the three ordered parts.  Every serialized forbidden triple contributes the
clause not(x_i and y_j and z_k).  Integer multiplication constraints define
the exact cardinality product.

Two lossless symmetry reductions are imposed: family sizes are sorted, and a
member of the largest family is mapped to RREF vertex 0 using transitivity of
GL(5,2).  After that normalization, a selected member of the second family
can be mapped to one of three representatives, according to its intersection
dimension with vertex 0.
"""

from __future__ import annotations

import hashlib
import json
import os
import time
from pathlib import Path

from ortools.sat.python import cp_model


ROOT = Path(__file__).resolve().parent
SUMMARY_PATH = ROOT / "rref_hypergraph_summary.json"
EDGE_PATH = ROOT / "forbidden_triples_u8.bin"
MODE = os.environ.get("SEARCH_MODE", "max_product")
if MODE not in {"max_product", "nonstar_equality"}:
    raise ValueError(f"unknown SEARCH_MODE={MODE!r}")
RESULT_PATH = ROOT / (
    "cpsat_product_result.json"
    if MODE == "max_product"
    else "cpsat_equality_result.json"
)


def span_mask(basis: list[int]) -> int:
    vectors = [0]
    for row in basis:
        vectors += [vector ^ row for vector in vectors]
    return sum(1 << vector for vector in vectors)


def main() -> None:
    start = time.monotonic()
    summary = json.loads(SUMMARY_PATH.read_text(encoding="utf-8"))
    edge_data = EDGE_PATH.read_bytes()
    assert len(edge_data) == 3 * summary["edge_count"]
    assert hashlib.sha256(edge_data).hexdigest() == summary["edge_file_sha256"]
    bases = summary["rref_bases"]
    masks = [span_mask(basis) for basis in bases]
    assert len(masks) == 155 and len(set(masks)) == 155

    model = cp_model.CpModel()
    families = [
        [model.new_bool_var(f"f{part}_{index}") for index in range(155)]
        for part in range(3)
    ]
    x, y, z = families
    counts = [model.new_int_var(1, 155, f"size{part}") for part in range(3)]
    for variables, count in zip(families, counts):
        model.add(count == sum(variables))

    # Family-part permutation symmetry.
    model.add(counts[0] >= counts[1])
    model.add(counts[1] >= counts[2])
    # GL(5,2) is transitive on 3-subspaces.
    model.add(x[0] == 1)

    # Stabilizer orbits of a second 3-subspace are indexed by intersection
    # dimension 1, 2, or 3 with vertex 0.
    representatives = {}
    for index, mask in enumerate(masks):
        dimension = (masks[0] & mask).bit_count().bit_length() - 1
        representatives.setdefault(dimension, index)
    assert set(representatives) == {1, 2, 3}
    model.add_bool_or([y[representatives[d]] for d in (1, 2, 3)])

    view = memoryview(edge_data)
    for position in range(0, len(view), 3):
        model.add_bool_or([
            x[view[position]].Not(),
            y[view[position + 1]].Not(),
            z[view[position + 2]].Not(),
        ])

    pair_product = model.new_int_var(1, 155 ** 2, "pair_product")
    product = model.new_int_var(1, 155 ** 3, "product")
    model.add_multiplication_equality(pair_product, counts[:2])
    model.add_multiplication_equality(product, [pair_product, counts[2]])
    excluded_stars = 0
    if MODE == "max_product":
        model.maximize(product)
    else:
        model.add(product == 35 ** 3)
        # Over F_2, each nonzero vector is the unique nonzero representative
        # of a 1-space.  Exclude, one by one, the exact assignment in which all
        # three parts are the full star through that vector.
        for vector in range(1, 32):
            vector_star = {
                index for index, mask in enumerate(masks)
                if mask & (1 << vector)
            }
            assert len(vector_star) == 35
            model.add_bool_or([
                variable.Not() if index in vector_star else variable
                for variables in families
                for index, variable in enumerate(variables)
            ])
            excluded_stars += 1

    # Supply the known common-star construction as a lower-bound hint only in
    # the optimization mode; it is deliberately excluded in the equality test.
    star = set(summary["star_through_vector_1_indices"])
    if MODE == "max_product":
        for variables in families:
            for index, variable in enumerate(variables):
                model.add_hint(variable, int(index in star))
        for count in counts:
            model.add_hint(count, 35)
        model.add_hint(pair_product, 35 ** 2)
        model.add_hint(product, 35 ** 3)

    build_seconds = time.monotonic() - start
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = float(
        os.environ.get("CP_SAT_SECONDS", "600")
    )
    solver.parameters.num_search_workers = int(os.environ.get("CP_SAT_WORKERS", "32"))
    solver.parameters.random_seed = 260905848
    solver.parameters.symmetry_level = 3
    solver.parameters.log_search_progress = os.environ.get("CP_SAT_LOG", "0") == "1"
    status_code = solver.solve(model)
    solve_seconds = time.monotonic() - start - build_seconds
    status = solver.status_name(status_code)

    result = {
        "solver": "OR-Tools CP-SAT",
        "ortools_version": __import__("ortools").__version__,
        "search_mode": MODE,
        "status": status,
        "model_semantics": "exact integer/Boolean",
        "edge_file_sha256": summary["edge_file_sha256"],
        "edge_count": summary["edge_count"],
        "symmetry_reductions": {
            "ordered_sizes": "size0 >= size1 >= size2",
            "fixed_vertex": "f0_0 = 1 by GL(5,2) transitivity",
            "second_part_orbit_representatives": representatives,
        },
        "build_seconds": build_seconds,
        "solve_seconds": solve_seconds,
        "wall_seconds": time.monotonic() - start,
        "conflicts": solver.num_conflicts,
        "branches": solver.num_branches,
    }
    if MODE == "nonstar_equality":
        result.update({
            "required_product": 35 ** 3,
            "excluded_exact_common_stars": excluded_stars,
        })
    if status_code in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        selected = [
            [index for index, variable in enumerate(variables)
             if solver.value(variable)]
            for variables in families
        ]
        actual_counts = [len(indices) for indices in selected]
        actual_product = actual_counts[0] * actual_counts[1] * actual_counts[2]
        assert actual_counts == [solver.value(count) for count in counts]
        assert actual_product == solver.value(product)
        forbidden_witness = next(
            (
                (first, second, third)
                for first in selected[0]
                for second in selected[1]
                for third in selected[2]
                if (masks[first] & masks[second] & masks[third]).bit_count() == 1
            ),
            None,
        )
        assert forbidden_witness is None
        result.update({
            "objective_product": actual_product,
            "best_objective_bound": solver.best_objective_bound,
            "counts": actual_counts,
            "selected_vertex_indices": selected,
            "independent_primal_replay_passed": True,
            "is_common_supplied_star": all(set(indices) == star for indices in selected),
        })
    RESULT_PATH.write_text(
        json.dumps(result, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
