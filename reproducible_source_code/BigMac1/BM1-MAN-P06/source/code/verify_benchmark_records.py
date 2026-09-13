#!/usr/bin/env python3
"""Check that serialized benchmark summaries agree with retained solver logs."""

from __future__ import annotations

import json
import math
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def extract_integer(pattern: str, text: str) -> int:
    match = re.search(pattern, text, re.MULTILINE)
    assert match is not None
    return int(match.group(1))


def main() -> None:
    summary = json.loads(
        (ROOT / "certificates/benchmark_summary.json").read_text(encoding="utf-8")
    )
    for record in summary["es_9_5_same_machine_runs"]:
        log = (ROOT / record["log"]).read_text(encoding="utf-8")
        assert ("s UNSATISFIABLE" in log) == (record["status"] == "UNSAT")
        assert ("s UNKNOWN" in log) == (record["status"] == "UNKNOWN")
        assert extract_integer(r"^c conflicts:\s+(\d+)", log) == record["conflicts"]
        assert extract_integer(r"^c decisions:\s+(\d+)", log) == record["decisions"]
        assert (
            extract_integer(r"^c clauses_learned:\s+(\d+)", log)
            == record["learned_clauses"]
        )
        if record["drat_proof"] is not None:
            proof = ROOT / record["drat_proof"]
            formula = ROOT / record["formula"]
            assert proof.stat().st_size == record["drat_proof_bytes"]
            checked = subprocess.run(
                [
                    str(ROOT / "literature/external/drat-trim/drat-trim"),
                    str(formula),
                    str(proof),
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            assert "s VERIFIED" in checked.stdout

    es6 = summary["es_17_6_recommended_formula"]
    es6_log = (ROOT / es6["log"]).read_text(encoding="utf-8")
    assert "s UNKNOWN" in es6_log
    assert extract_integer(r"^c conflicts:\s+(\d+)", es6_log) == es6["conflicts"]
    assert extract_integer(r"^c decisions:\s+(\d+)", es6_log) == es6["decisions"]

    cube_summary = json.loads(
        (ROOT / summary["es_17_6_cube_scout"]["summary"]).read_text(encoding="utf-8")
    )
    assert cube_summary["counts"] == {"UNKNOWN": 16}
    assert cube_summary["complete_unsat_partition"] is False
    certified = summary["es_17_6_certified_partition"]
    certified_summary = json.loads(
        (ROOT / certified["summary"]).read_text(encoding="utf-8")
    )
    assert certified_summary["counts"] == {"UNSAT": 61}
    assert certified_summary["complete_unsat_partition"] is True
    assert len(certified_summary["results"]) == certified["covering_cubes"] == 61
    assert math.isclose(
        sum(item["wall_seconds"] for item in certified_summary["results"]),
        certified["sum_leaf_wall_seconds"],
        abs_tol=1e-9,
    )
    lrat_summary = json.loads(
        (ROOT / certified["lrat_summary"]).read_text(encoding="utf-8")
    )
    assert lrat_summary["all_lrat_verified"] is True
    assert lrat_summary["cubes"] == certified["lrat_leaves_checked"] == 61
    assert lrat_summary["total_lrat_bytes"] == certified["total_lrat_bytes"]
    print("verified_serialized_solver_benchmarks")
    print("verified_es_17_6_monolithic_search_was_inconclusive")
    print("verified_es_17_6_certified_partition_record")


if __name__ == "__main__":
    main()
