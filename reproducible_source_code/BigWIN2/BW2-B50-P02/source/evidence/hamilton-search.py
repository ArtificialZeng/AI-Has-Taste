#!/usr/bin/env python3
"""Deterministically find Hamilton cycles in every sigma-zero atlas entry.

This is only a positive-witness search: no solver failure is interpreted as
non-Hamiltonicity.  The emitted cycles are checked again by a verifier that
does not import OR-Tools and reconstructs the orientation graphs from G.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

from ortools.sat.python import cp_model
import ortools


ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "evidence" / "atlas-through-6.json"
OUTPUT = ROOT / "evidence" / "hamilton-cycles.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_cycle(cycle: list[str]) -> list[str]:
    """Rotate to the least item and choose the lexicographically least sense."""
    start = min(range(len(cycle)), key=cycle.__getitem__)
    forward = cycle[start:] + cycle[:start]
    backward_raw = list(reversed(cycle))
    start = min(range(len(cycle)), key=backward_raw.__getitem__)
    backward = backward_raw[start:] + backward_raw[:start]
    return min(forward, backward)


def solve(entry: dict) -> tuple[list[str], dict]:
    vertices = entry["orientation_bit_vectors"]
    index = {bits: i for i, bits in enumerate(vertices)}
    model = cp_model.CpModel()
    arcs = []
    arc_var = {}
    for left, right in entry["flip_edges"]:
        i, j = index[left], index[right]
        for source, target in ((i, j), (j, i)):
            var = model.new_bool_var(f"a_{source}_{target}")
            arcs.append((source, target, var))
            arc_var[source, target] = var
    model.add_circuit(arcs)

    solver = cp_model.CpSolver()
    solver.parameters.num_search_workers = 1
    solver.parameters.random_seed = 0
    # A limit prevents an operational stall; UNKNOWN is fatal, never negative.
    solver.parameters.max_time_in_seconds = 60.0
    status = solver.solve(model)
    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        raise RuntimeError(
            f"{entry['graph6']}: positive search did not finish: "
            f"{solver.status_name(status)}"
        )

    successor = {
        source: target
        for (source, target), var in arc_var.items()
        if solver.boolean_value(var)
    }
    if len(successor) != len(vertices):
        raise AssertionError(f"{entry['graph6']}: incomplete successor map")
    order = [0]
    while len(order) < len(vertices):
        nxt = successor[order[-1]]
        if nxt in order:
            raise AssertionError(f"{entry['graph6']}: premature subtour")
        order.append(nxt)
    if successor[order[-1]] != order[0]:
        raise AssertionError(f"{entry['graph6']}: selected arcs do not close")

    cycle = canonical_cycle([vertices[i] for i in order])
    stats = {
        "status": solver.status_name(status),
        "branches": solver.num_branches,
        "conflicts": solver.num_conflicts,
    }
    return cycle, stats


def main() -> None:
    atlas = json.loads(ATLAS.read_text())
    targets = [g for g in atlas["graphs"] if g["sigma"] == 0]
    # The atlas is already in increasing order and canonical graph6 order, but
    # sort explicitly so the search order is part of this program's contract.
    targets.sort(key=lambda g: (g["order"], g["graph6"]))
    records = []
    for entry in targets:
        cycle, stats = solve(entry)
        records.append(
            {
                "graph6": entry["graph6"],
                "order": entry["order"],
                "sigma": entry["sigma"],
                "acyclic_orientation_count": entry["acyclic_orientation_count"],
                "cycle": cycle,
                "search": stats,
            }
        )
        print(
            entry["order"], entry["graph6"], len(cycle),
            stats["status"], stats["branches"], stats["conflicts"],
            flush=True,
        )

    result = {
        "schema": "win-00050-p02-hamilton-cycles-v1",
        "atlas_sha256": sha256(ATLAS),
        "solver": {
            "name": "OR-Tools CP-SAT AddCircuit",
            "ortools_version": ortools.__version__,
            "num_search_workers": 1,
            "random_seed": 0,
            "per_instance_time_limit_seconds": 60.0,
            "failure_policy": "UNKNOWN/INFEASIBLE aborts and is never a negative result",
        },
        "scope": "all and only sigma-zero entries, increasing (order, graph6)",
        "cycle_convention": "a two-vertex cyclic Gray code is accepted for K2",
        "count": len(records),
        "cycles": records,
    }
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(f"wrote {OUTPUT.relative_to(ROOT)} with {len(records)} cycles")


if __name__ == "__main__":
    main()
