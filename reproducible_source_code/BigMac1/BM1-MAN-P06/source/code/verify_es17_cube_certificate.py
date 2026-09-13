#!/usr/bin/env python3
"""Verify coverage, exact cube construction, and all 61 ES(6) DRAT leaves."""

from __future__ import annotations

import concurrent.futures
import itertools
import json
import subprocess
from pathlib import Path

from compact_sat import triple_variables


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "tmp/sat/es_17_6_direct_relations_prime_extreme.cnf"
CUBE_DIR = ROOT / "tmp/cubes/es17_first_window_prime_extreme"
MANIFEST = CUBE_DIR / "manifest.json"
SUMMARY = ROOT / "tmp/certification/es17_61cubes_120s/summary.json"
PROOF_DIR = ROOT / "tmp/certification/es17_61cubes_120s/proofs"
LRAT_DIR = ROOT / "tmp/certification/es17_61cubes_120s/lrat"
LRAT_SUMMARY = ROOT / "tmp/certification/es17_61cubes_120s/lrat_summary.json"
CHECKER = ROOT / "literature/external/drat-trim/drat-trim"
LRAT_CHECKER = ROOT / "literature/external/drat-trim/lrat-check"
RECORD = ROOT / "certificates/sat/es_17_6_extreme_61cube.json"


def read_dimacs(path: Path) -> tuple[int, list[tuple[int, ...]]]:
    variables = declared_clauses = None
    clauses: list[tuple[int, ...]] = []
    with path.open("r", encoding="ascii") as stream:
        for raw_line in stream:
            line = raw_line.strip()
            if not line or line.startswith("c"):
                continue
            if line.startswith("p cnf"):
                _, _, raw_variables, raw_clauses = line.split()
                variables = int(raw_variables)
                declared_clauses = int(raw_clauses)
                continue
            values = tuple(map(int, line.split()))
            assert values and values[-1] == 0
            clauses.append(values[:-1])
    assert variables is not None and declared_clauses == len(clauses)
    return variables, clauses


def clause_value(clause: tuple[int, ...], assignment: dict[int, bool]) -> bool:
    return any(assignment[abs(literal)] == (literal > 0) for literal in clause)


def expected_partition(
    base_clauses: list[tuple[int, ...]],
) -> tuple[tuple[int, ...], dict[str, tuple[int, ...]], int]:
    variables = triple_variables(17)
    local_triples = tuple(itertools.combinations(range(6), 3))
    local_variables = {variables[triple] for triple in local_triples}
    extreme_variables = {
        variables[triple] for triple in local_triples if triple[0] == 0
    }
    cube_variables = tuple(
        variables[triple] for triple in local_triples if triple[0] != 0
    )
    assert cube_variables == (121, 122, 123, 135, 136, 148, 226, 227, 239, 317)
    local_clauses = tuple(
        clause
        for clause in base_clauses
        if {abs(literal) for literal in clause} <= local_variables
    )
    retained: dict[str, tuple[int, ...]] = {}
    rejected = 0
    for bits in itertools.product((False, True), repeat=len(cube_variables)):
        assignment = {variable: True for variable in extreme_variables}
        assignment.update(dict(zip(cube_variables, bits)))
        if not all(clause_value(clause, assignment) for clause in local_clauses):
            rejected += 1
            continue
        tag = "".join("1" if bit else "0" for bit in bits)
        retained[tag] = tuple(
            variable if bit else -variable
            for variable, bit in zip(cube_variables, bits)
        )
    assert rejected == 963 and len(retained) == 61
    return cube_variables, retained, len(local_clauses)


def check_leaf(tag: str) -> tuple[str, int, int]:
    cnf = CUBE_DIR / f"cube_{tag}.cnf"
    proof = PROOF_DIR / f"cube_{tag}.drat"
    lrat = LRAT_DIR / f"cube_{tag}.lrat"
    assert cnf.is_file() and proof.is_file() and proof.stat().st_size > 0
    assert lrat.is_file() and lrat.stat().st_size > 0
    result = subprocess.run(
        [str(CHECKER), str(cnf), str(proof)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    assert result.returncode == 0, (tag, result.stdout[-2000:])
    assert "s VERIFIED" in result.stdout, (tag, result.stdout[-2000:])
    lrat_result = subprocess.run(
        [str(LRAT_CHECKER), str(cnf), str(lrat)],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
    )
    assert lrat_result.returncode == 0, (tag, lrat_result.stdout[-2000:])
    assert "c VERIFIED" in lrat_result.stdout, (tag, lrat_result.stdout[-2000:])
    return tag, proof.stat().st_size, lrat.stat().st_size


def main() -> None:
    assert CHECKER.is_file()
    base_variables, base_clauses = read_dimacs(BASE)
    assert base_variables == 680 and len(base_clauses) == 217_176
    cube_variables, retained, local_clause_count = expected_partition(base_clauses)

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert manifest["cube_variables"] == list(cube_variables)
    assert manifest["all_assignments"] == 1024
    assert manifest["locally_inconsistent_assignments_omitted"] == 963
    assert manifest["local_filter_clauses"] == local_clause_count
    assert manifest["cube_count"] == 61
    manifest_units = {
        item["cube"]: tuple(item["units"]) for item in manifest["cubes"]
    }
    assert manifest_units == retained

    # Each leaf must be the identical base clause list followed by its ten units.
    for tag, units in retained.items():
        variables, clauses = read_dimacs(CUBE_DIR / f"cube_{tag}.cnf")
        assert variables == base_variables
        assert clauses[: len(base_clauses)] == base_clauses
        assert clauses[len(base_clauses) :] == [(literal,) for literal in units]

    summary = json.loads(SUMMARY.read_text(encoding="utf-8"))
    assert summary["counts"] == {"UNSAT": 61}
    assert summary["complete_unsat_partition"] is True
    assert {item["cube"].removeprefix("cube_") for item in summary["results"]} == set(
        retained
    )

    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        checked = list(executor.map(check_leaf, sorted(retained)))
    total_proof_bytes = sum(drat_size for _, drat_size, _ in checked)
    total_lrat_bytes = sum(lrat_size for _, _, lrat_size in checked)
    assert len(checked) == 61 and total_proof_bytes == 288_562_058
    assert total_lrat_bytes == 871_234_978
    lrat_summary = json.loads(LRAT_SUMMARY.read_text(encoding="utf-8"))
    assert lrat_summary["all_lrat_verified"] is True
    assert lrat_summary["total_drat_bytes"] == total_proof_bytes
    assert lrat_summary["total_lrat_bytes"] == total_lrat_bytes
    record = json.loads(RECORD.read_text(encoding="utf-8"))
    assert record["global_es7_claim_solved"] is False
    assert record["base_formula"] == {
        "path": "tmp/sat/es_17_6_direct_relations_prime_extreme.cnf",
        "variables": 680,
        "clauses": 217176,
        "literal_occurrences": 849304,
    }
    assert record["partition"]["retained_covering_cubes"] == 61
    assert record["solving"]["total_drat_bytes"] == total_proof_bytes
    assert record["conversion_and_checking"]["total_lrat_bytes"] == total_lrat_bytes
    print("verified_es17_first_window_assignments=1024")
    print("verified_es17_locally_rejected_assignments=963")
    print("verified_es17_covering_cubes=61")
    print("verified_es17_drat_leaves=61")
    print(f"verified_es17_total_drat_bytes={total_proof_bytes}")
    print("verified_es17_lrat_leaves=61")
    print(f"verified_es17_total_lrat_bytes={total_lrat_bytes}")


if __name__ == "__main__":
    main()
