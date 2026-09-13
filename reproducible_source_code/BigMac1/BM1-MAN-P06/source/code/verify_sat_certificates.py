#!/usr/bin/env python3
"""Independently rerun the checkers for the released finite SAT certificate."""

from __future__ import annotations

import json
import subprocess
from pathlib import Path

from compact_sat import clause_stream, triple_variables


ROOT = Path(__file__).resolve().parents[1]


def dimacs_counts(path: Path) -> tuple[int, int, int]:
    nvars = expected_clauses = clauses = literals = 0
    with path.open("r", encoding="ascii") as stream:
        for line in stream:
            if line.startswith("c"):
                continue
            if line.startswith("p cnf"):
                _, _, raw_vars, raw_clauses = line.split()
                nvars, expected_clauses = int(raw_vars), int(raw_clauses)
                continue
            values = [int(value) for value in line.split()]
            assert values and values[-1] == 0
            assert all(0 < abs(value) <= nvars for value in values[:-1])
            clauses += 1
            literals += len(values) - 1
    assert clauses == expected_clauses
    return nvars, clauses, literals


def dimacs_clauses(path: Path) -> tuple[tuple[int, ...], ...]:
    result = []
    with path.open("r", encoding="ascii") as stream:
        for line in stream:
            if line.startswith(("c", "p")):
                continue
            values = tuple(int(value) for value in line.split())
            assert values and values[-1] == 0
            result.append(values[:-1])
    return tuple(result)


def main() -> None:
    record = json.loads(
        (ROOT / "certificates/sat/es_9_5_factored.json").read_text(encoding="utf-8")
    )
    formula = ROOT / record["formula"]["path"]
    drat = ROOT / record["solver"]["proof"]
    lrat = ROOT / record["conversion_and_checking"]["lrat"]
    assert formula.stat().st_size == record["formula"]["bytes"]
    assert drat.stat().st_size == record["solver"]["proof_bytes"]
    assert lrat.stat().st_size == record["conversion_and_checking"]["lrat_bytes"]
    assert dimacs_counts(formula) == (
        record["formula"]["variables"],
        record["formula"]["clauses"],
        record["formula"]["literal_occurrences"],
    )
    regenerated = tuple(
        clause_stream(
            9,
            5,
            (),
            (),
            triple_variables(9),
            "signotope",
            "one-sided",
            False,
        )
    )
    assert dimacs_clauses(formula) == regenerated

    checker_dir = ROOT / "literature/external/drat-trim"
    drat_result = subprocess.run(
        [str(checker_dir / "drat-trim"), str(formula), str(drat)],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "s VERIFIED" in drat_result.stdout
    lrat_result = subprocess.run(
        [str(checker_dir / "lrat-check"), str(formula), str(lrat)],
        check=True,
        capture_output=True,
        text=True,
    )
    assert "c VERIFIED" in lrat_result.stdout
    print("verified_es_9_5_dimacs_counts")
    print("verified_es_9_5_exact_generator_reproduction")
    print("verified_es_9_5_drat_certificate")
    print("verified_es_9_5_lrat_certificate")


if __name__ == "__main__":
    main()
