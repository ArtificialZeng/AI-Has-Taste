#!/usr/bin/env python3
"""Coverage/hash/proof-replay audit for the proposed finite disproof."""

from __future__ import annotations

import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE_SHA256 = "6ce58a7ef27abff3de2371ca219430179879b43f26e8da5e94927a140aa70a75"
EXPECTED = {4: 1, 6: 2, 8: 5, 10: 19, 12: 85, 14: 509, 16: 4060, 18: 41301}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_run(args: list[str]) -> str:
    result = subprocess.run(args, cwd=ROOT, check=False, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    assert result.returncode == 0, (args, result.stdout[-2000:])
    return result.stdout


def main() -> None:
    assert sha256(ROOT / "source.md") == SOURCE_SHA256
    checked_run(["python3", "evidence/scripts/verify_census.py"])
    checked_run(["python3", "evidence/scripts/verify_witnesses.py"])

    census = {
        n: (ROOT / "census" / f"n{n:02d}.g6").read_bytes().splitlines()
        for n in EXPECTED
    }
    assert {n: len(rows) for n, rows in census.items()} == EXPECTED

    result_rows = [json.loads(line) for line in (ROOT / "evidence" / "coloring_witnesses.jsonl").read_text().splitlines()]
    expected_result_count = sum(EXPECTED[n] for n in EXPECTED if n <= 16)
    assert len(result_rows) == expected_result_count == 4681
    seen = set()
    classifications = Counter()
    for row in result_rows:
        key = (row["n"], row["index"])
        assert key not in seen
        seen.add(key)
        assert row["n"] <= 16
        assert census[row["n"]][row["index"]].decode("ascii") == row["graph6"]
        classifications[(row["n"], row["classification"])] += 1

    certification = json.loads((ROOT / "evidence" / "unsat_certification.json").read_text())
    assert certification["status"] == "all DRAT proofs VERIFIED"
    records = {(row["n"], row["index"], row["predicate"]): row for row in certification["records"]}
    assert len(records) == certification["record_count"] == 329
    needed = set()
    for row in result_rows:
        if row["classification"] == "A_unsat_observed":
            needed.add((row["n"], row["index"], "A"))
        elif row["classification"] == "A_sat_E_unsat_observed":
            needed.add((row["n"], row["index"], "E"))
    assert set(records) == needed

    replayed = 0
    for key in sorted(records):
        record = records[key]
        cnf = ROOT / record["cnf"]
        proof = ROOT / record["proof"]
        assert sha256(cnf) == record["cnf_sha256"]
        assert sha256(proof) == record["proof_sha256"]
        output = checked_run(["tools/drat-trim", str(cnf), str(proof)])
        assert "s VERIFIED" in output
        replayed += 1

    candidates = [row for row in result_rows if row["classification"] == "A_sat_E_unsat_observed"]
    assert candidates and min(row["n"] for row in candidates) == 16
    assert all(row["n"] == 16 for row in candidates)
    assert len(candidates) == 16
    report = {
        "script": str(Path(__file__).relative_to(ROOT)),
        "source_sha256": SOURCE_SHA256,
        "census_counts": EXPECTED,
        "census_total": sum(EXPECTED.values()),
        "result_rows_through_order_16": len(result_rows),
        "classification_counts": {
            f"n{n}_{kind}": count for (n, kind), count in sorted(classifications.items())
        },
        "proofs_replayed": replayed,
        "candidate_count": len(candidates),
        "candidate_order": 16,
        "candidate_graph6": [row["graph6"] for row in candidates],
        "conclusion": (
            "Conditional on the documented census completeness and CNF semantics, all 16 listed graphs "
            "are Type 1 without equitable 4-total colorings, and none exists at smaller order."
        ),
        "status": "pass",
    }
    output = ROOT / "evidence" / "resolution_audit.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
