#!/usr/bin/env python3
"""Adversarial semantic mutations for the independent Q5 referee.

The mutations are applied in memory after loading hash-bound originals.  Thus
rejection tests the mathematics/schema checks, not merely the SHA-256 gate.
No project implementation under src/, tests/, or discovery/ is imported.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

import independent_verifier as iv


HERE = Path(__file__).resolve().parent


def expect_reject(name: str, category: str, mutate_and_verify) -> dict:
    try:
        mutate_and_verify()
    except iv.AuditFailure as exc:
        return {"name": name, "category": category, "status": "REJECTED", "reason": str(exc)}
    except (KeyError, TypeError, ValueError, json.JSONDecodeError) as exc:
        return {"name": name, "category": category, "status": "REJECTED", "reason": f"{type(exc).__name__}: {exc}"}
    raise RuntimeError(f"FAIL OPEN: mutation accepted: {name}")


def main() -> int:
    binding, inputs = iv.load_bound_inputs(enforce_hashes=True)
    contract = binding["semantic_contract"]
    results: list[dict] = []

    def changed_chamber_graph() -> None:
        mutant = copy.deepcopy(contract)
        mutant["chambers"]["triangle"] = [[0, 1], [0, 2]]
        iv.verify_chamber_graphs(mutant)

    results.append(expect_reject("change_chamber_graph", "chamber graph", changed_chamber_graph))

    def changed_certificate_coefficient() -> None:
        mutant = copy.deepcopy(inputs["star4"])
        mutant["all_leaves_one_polynomial_degree_descending"][-1] = -63
        iv.verify_star4(mutant)

    results.append(expect_reject("change_certificate_coefficient", "certificate coefficient", changed_certificate_coefficient))

    def changed_resultant_factor() -> None:
        mutant = copy.deepcopy(inputs["q3"])
        mutant["primitive_resultant"] = "-64*b^2*(b-1)^6*(b^2-b+1)^3"
        iv.verify_q3(mutant)

    results.append(expect_reject("change_resultant_factor", "certificate factor", changed_resultant_factor))

    def deleted_wall() -> None:
        mutant = copy.deepcopy(inputs["triangle"])
        mutant["ordered_closure_constraints"]["low_pair_closure"].pop()
        iv.verify_triangle(mutant)

    results.append(expect_reject("delete_pair_wall", "wall deletion", deleted_wall))

    def changed_root_interval() -> None:
        mutant = copy.deepcopy(inputs["star1"])
        mutant["surviving_component"]["alpha_isolating_interval"] = [[5, 2], [13, 5]]
        iv.verify_star1(mutant)

    results.append(expect_reject("change_algebraic_root_interval", "root isolation", changed_root_interval))

    def flipped_hessian_sign() -> None:
        mutant = copy.deepcopy(inputs["star1"])
        mutant["hessian"]["reduced_quadratic_forms_mod_13alpha2-48alpha+39"]["large_block"]["sign"] = "positive"
        iv.verify_star1(mutant)

    results.append(expect_reject("flip_hessian_sign", "Hessian signature", flipped_hessian_sign))

    def changed_support_path() -> None:
        mutant = copy.deepcopy(contract)
        mutant["support_paths"]["d4"][-1] = [0, 2]
        iv.verify_d4_transverse(mutant)

    results.append(expect_reject("change_support_path", "support path", changed_support_path))

    def deleted_star1_margin() -> None:
        mutant = copy.deepcopy(inputs["star1"])
        mutant["chart"]["pair_margins"].pop()
        iv.verify_star1(mutant)

    results.append(expect_reject("delete_star1_margin", "wall deletion (second implementation)", deleted_star1_margin))

    def duplicate_json_key() -> None:
        iv.load_json_strict('{"schema":"bad","schema":"q5-star2-bernstein-v1"}')

    results.append(expect_reject("duplicate_json_key", "parser ambiguity", duplicate_json_key))

    def boolean_in_integer_slot() -> None:
        iv.reject_noncanonical_booleans({"expected_saturated_dimension": False})

    results.append(expect_reject("boolean_in_integer_slot", "type confusion", boolean_in_integer_slot))

    iv.require(len(results) >= 6, "too few mutation categories")
    iv.require(all(record["status"] == "REJECTED" for record in results), "a mutation was not rejected")
    output = {
        "schema": "q5-independent-referee-mutations-v1",
        "status": "PASS",
        "hash_bound_originals": True,
        "semantic_mutations": True,
        "count": len(results),
        "results": results,
        "mutation_verifier_sha256": iv.sha256_file(Path(__file__)),
        "independent_verifier_sha256": iv.sha256_file(HERE / "independent_verifier.py"),
        "binding_sha256": iv.sha256_file(HERE / "frozen_inputs.json"),
    }
    (HERE / "mutation_results.json").write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"PASS: {len(results)} semantic mutations rejected fail closed")
    for record in results:
        print(f"{record['name']}: {record['reason']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
