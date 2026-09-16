#!/usr/bin/env python3
"""Exact two-row witness search for x=529.

For a fixed even gap d, this builds the graph from problem.md using only
integer equality and math.gcd predicates.  OR-Tools CP-SAT is asked for a
clique of the requested size.  Any positive answer is then checked directly
against the original all-distinct/all-pairs-coprime conditions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
import platform
import sys
import time

from ortools.sat.python import cp_model


def columns_are_compatible(v: int, w: int, d: int) -> bool:
    entries = (v, v + d, w, w + d)
    return len(set(entries)) == 4 and all(
        math.gcd(entries[i], entries[j]) == 1
        for i in range(4)
        for j in range(i + 1, 4)
    )


def verify_witness(x: int, d: int, starts: list[int], target: int) -> dict:
    entries = [a for v in starts for a in (v, v + d)]
    range_ok = d > 0 and all(2 <= v <= x - d for v in starts)
    distinct_ok = len(starts) == target and len(set(starts)) == target
    entries_distinct = len(set(entries)) == 2 * target
    bad_gcd_pairs = [
        [entries[i], entries[j], math.gcd(entries[i], entries[j])]
        for i in range(len(entries))
        for j in range(i + 1, len(entries))
        if math.gcd(entries[i], entries[j]) != 1
    ]
    return {
        "x": x,
        "d": d,
        "target_columns": target,
        "starts": starts,
        "entries": entries,
        "range_ok": range_ok,
        "starts_distinct": distinct_ok,
        "entries_distinct": entries_distinct,
        "pair_count_checked": len(entries) * (len(entries) - 1) // 2,
        "bad_gcd_pairs": bad_gcd_pairs,
        "verified": range_ok and distinct_ok and entries_distinct and not bad_gcd_pairs,
    }


def solve_gap(x: int, d: int, target: int, seconds: float) -> dict:
    vertices = [v for v in range(2, x - d + 1) if math.gcd(v, v + d) == 1]
    model = cp_model.CpModel()
    choose = [model.new_bool_var(f"v_{v}") for v in vertices]
    incompatible = 0
    for i, v in enumerate(vertices):
        for j in range(i + 1, len(vertices)):
            if not columns_are_compatible(v, vertices[j], d):
                model.add(choose[i] + choose[j] <= 1)
                incompatible += 1
    model.add(sum(choose) >= target)

    solver = cp_model.CpSolver()
    solver.parameters.num_search_workers = 1
    solver.parameters.random_seed = 0
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.log_search_progress = False
    started = time.monotonic()
    status = solver.solve(model)
    elapsed = time.monotonic() - started
    record = {
        "d": d,
        "vertices": len(vertices),
        "incompatible_pairs": incompatible,
        "status": solver.status_name(status),
        "wall_seconds": elapsed,
        "branches": solver.num_branches,
        "conflicts": solver.num_conflicts,
    }
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        starts = [v for v, var in zip(vertices, choose) if solver.value(var)]
        # The >= target model can return more; a target-sized subset suffices.
        record["witness"] = verify_witness(x, d, starts[:target], target)
    return record


def parse_gap_spec(spec: str, x: int) -> list[int]:
    if spec == "all":
        return list(range(2, x - 2, 2))
    gaps = [int(part) for part in spec.split(",")]
    if any(d <= 0 or d >= x - 1 or d % 2 for d in gaps):
        raise ValueError("gaps must be positive even integers at most x-3")
    return gaps


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--x", type=int, default=529)
    parser.add_argument("--target", type=int, default=42)
    parser.add_argument("--gaps", default="42", help="comma list, or 'all'")
    parser.add_argument("--seconds-per-gap", type=float, default=300.0)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()
    gaps = parse_gap_spec(args.gaps, args.x)

    result = {
        "method": "integer-gcd graph plus deterministic single-worker OR-Tools CP-SAT",
        "python": platform.python_version(),
        "ortools": __import__("ortools").__version__,
        "parameters": {
            "x": args.x,
            "target": args.target,
            "gaps_requested": gaps,
            "seconds_per_gap": args.seconds_per_gap,
        },
        "gap_results": [],
    }
    for d in gaps:
        record = solve_gap(args.x, d, args.target, args.seconds_per_gap)
        result["gap_results"].append(record)
        print(json.dumps(record, sort_keys=True), flush=True)
        if record.get("witness", {}).get("verified"):
            result["termination"] = "verified_witness"
            break
    else:
        result["termination"] = "all_requested_gaps_processed"

    canonical = json.dumps(result, sort_keys=True, separators=(",", ":")).encode()
    result["payload_sha256"] = hashlib.sha256(canonical).hexdigest()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    return 0 if result["termination"] == "verified_witness" else 1


if __name__ == "__main__":
    sys.exit(main())
