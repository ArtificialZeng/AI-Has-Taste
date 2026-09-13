#!/usr/bin/env python3
"""Fail-closed consistency audit for the bicyclic-core theorem document."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--theorem", type=Path, required=True)
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--audit", type=Path, required=True)
    parser.add_argument("--attacks", type=Path, required=True)
    parser.add_argument("--sharpness", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    theorem = args.theorem.read_text(encoding="utf-8")
    source = json.loads(args.source.read_text(encoding="utf-8"))
    audit = json.loads(args.audit.read_text(encoding="utf-8"))
    attacks = json.loads(args.attacks.read_text(encoding="utf-8"))
    sharpness = json.loads(args.sharpness.read_text(encoding="utf-8"))
    records = source["records"]

    determinant_counts = Counter(int(record["determinant"]) for record in records)
    type_counts = Counter(record["core_type"] for record in records)
    proof_modes = Counter(record.get("proof_mode") for record in records)
    source_nodes = sum(record.get("branch_and_bound", {}).get("nodes", 0) for record in records)
    checks = {
        "source_hash_bound": sha256(args.source) == audit["source_sha256"]
        == "286465529d9e1b65716790ac01e87b68f8a7593a5dadd3a415c247bc2f74c3df",
        "audit_pass": audit.get("status") == "PASS" and audit.get("counterexample_found") is False,
        "domain_count": len(records) == audit.get("bicyclic_graphs") == 2678,
        "nonsingular_count": sum(not record["singular"] for record in records)
        == audit.get("nonsingular_cores") == 719,
        "determinant_distribution": determinant_counts
        == Counter({-9: 3, -5: 6, -4: 62, -1: 625, 0: 1959, 3: 17, 4: 6}),
        "type_distribution": type_counts == Counter({"D": 345, "F": 514, "T": 1819}),
        "proof_modes": proof_modes["root_proper_colouring"] == 29
        and proof_modes["complete_exact_target_search"] == 690,
        "source_nodes": source_nodes == 48_967_729,
        "independent_calls": audit.get("independent_search_total_calls") == 41_704_342,
        "independent_domain_match": audit.get("source_edge_lists_match_independent_isomorphism_set") is True,
        "engine_selftest": audit.get("search_engine_selftest", {}).get("status") == "PASS",
        "attacks_fail_closed": attacks.get("all_attacks_rejected") is True
        and len(attacks.get("attacks", {})) == 5
        and all(item.get("rejected") for item in attacks["attacks"].values()),
        "sharpness_pass": sharpness.get("status") == "PASS"
        and sharpness.get("ambient_order") == 62
        and sharpness.get("ambient_rank") == 10
        and sharpness.get("ambient_reduced") is True
        and sharpness.get("core_edge_count") == 11
        and sharpness.get("core_cyclomatic_number") == 2
        and sharpness.get("core_determinant") == -1,
        "scope_honest": "unrestricted" in theorem
        and "rank-ten rank--order conjecture is still neither proved nor disproved" in theorem,
        "no_floating_claim": "No floating-point eigenvalue" in theorem,
    }
    required_hashes = [
        sha256(args.source), sha256(args.audit), sha256(args.attacks), sha256(args.sharpness)
    ]
    checks["artifact_hashes_printed"] = all(value in theorem for value in required_hashes)
    if not all(checks.values()):
        raise AssertionError({key: value for key, value in checks.items() if not value})

    payload = {
        "status": "PASS",
        "fatal": 0,
        "major": 0,
        "minor": 0,
        "theorem": str(args.theorem),
        "theorem_sha256": sha256(args.theorem),
        "checks": checks,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
