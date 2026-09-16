#!/usr/bin/env python3
"""Replay an ASCII DRUP trace by reverse unit propagation.

Deletion lines are deliberately ignored.  Keeping deleted clauses only
strengthens the replay formula, and every retained non-input clause has first
been checked RUP, so this is a sound DRUP check.  A distinct SAT backend is
used only as a unit-propagation engine; no satisfiability search is requested.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

from pysat.formula import CNF
from pysat.solvers import Solver


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def parse_clause(line: str, line_number: int) -> tuple[bool, list[int]]:
    fields = line.split()
    deletion = bool(fields and fields[0] == "d")
    if deletion:
        fields = fields[1:]
    if not fields or fields[-1] != "0":
        raise ValueError(f"proof line {line_number} has no terminal 0")
    clause = [int(field) for field in fields[:-1]]
    if any(literal == 0 for literal in clause):
        raise ValueError(f"proof line {line_number} has an interior 0")
    return deletion, clause


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("cnf", type=Path)
    parser.add_argument("proof", type=Path)
    parser.add_argument("--solver", default="minisat22")
    parser.add_argument("--output", type=Path)
    parser.add_argument(
        "--provenance", default="win-00084-p06-research-3dd502da7309"
    )
    args = parser.parse_args()

    started = time.monotonic()
    formula = CNF(from_file=args.cnf)
    additions = 0
    deletions_ignored = 0
    empty_line = None
    failure: dict[str, object] | None = None

    with Solver(name=args.solver, bootstrap_with=formula.clauses) as checker:
        with args.proof.open("r", encoding="ascii") as handle:
            for line_number, raw in enumerate(handle, start=1):
                line = raw.strip()
                if not line or line.startswith("c"):
                    continue
                deletion, clause = parse_clause(line, line_number)
                if deletion:
                    deletions_ignored += 1
                    continue
                additions += 1
                propagated, _ = checker.propagate(
                    assumptions=[-literal for literal in clause]
                )
                if propagated:
                    failure = {
                        "line": line_number,
                        "clause": clause,
                        "reason": "negated clause did not cause a unit-propagation conflict",
                    }
                    break
                checker.add_clause(clause)
                if not clause:
                    empty_line = line_number
                    # The empty clause must be the final substantive addition.

    accepted = failure is None and empty_line is not None
    report: dict[str, object] = {
        "provenance": args.provenance,
        "check": "DRUP reverse unit propagation; deletion lines retained implicitly",
        "unit_propagation_backend": args.solver,
        "cnf_file": str(args.cnf),
        "cnf_sha256": sha256(args.cnf),
        "proof_file": str(args.proof),
        "proof_sha256": sha256(args.proof),
        "input_variables": formula.nv,
        "input_clauses": len(formula.clauses),
        "rup_additions_checked": additions,
        "deletions_ignored_soundly": deletions_ignored,
        "empty_clause_line": empty_line,
        "accepted": accepted,
        "elapsed_seconds": round(time.monotonic() - started, 6),
    }
    if failure is not None:
        report["failure"] = failure
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")
    raise SystemExit(0 if accepted else 1)


if __name__ == "__main__":
    main()
