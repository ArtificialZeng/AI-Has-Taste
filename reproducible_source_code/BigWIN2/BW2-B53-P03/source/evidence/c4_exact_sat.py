#!/usr/bin/env python3
"""Exact, independently modeled checks for the C4 order-gadget subsystem.

Model ``eager`` uses one Boolean for each unordered pair and explicitly adds
both forbidden directed 3-cycles for every triple.  Model ``rank`` uses integer
positions, AllDifferent, and a reified before-both/after-both alternative for
each arithmetic progression.  They share only the mathematical instance
constructor, not the order/AP encoding.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import time

from pysat.solvers import Solver
from ortools.sat.python import cp_model


def instance(M: int):
    values = list(range(M + 1, 2 * M + 1))
    aps = []
    for a in values:
        for c in range(a + 2, 2 * M + 1, 2):
            b = (a + c) // 2
            aps.append((a, b, c))
    attacks = [
        (2 * M - 13, M + 1),
        (2 * M - 11, M + 2),
        (2 * M - 5, M + 5),
        (2 * M - 10, M + 3),
    ]
    return values, aps, attacks


def digest_instance(M: int) -> str:
    values, aps, attacks = instance(M)
    payload = json.dumps({"M": M, "values": values, "aps": aps,
                          "attacks": attacks}, separators=(",", ":"))
    return hashlib.sha256(payload.encode()).hexdigest()


def eager(M: int, solver_name: str):
    values, aps, attacks = instance(M)
    pair = {}
    next_var = 1
    for i, a in enumerate(values):
        for b in values[i + 1:]:
            pair[a, b] = next_var
            next_var += 1

    def lit_before(a: int, b: int) -> int:
        if a < b:
            return pair[a, b]
        return -pair[b, a]

    s = Solver(name=solver_name)
    clause_count = 0
    # A tournament is transitive iff neither directed 3-cycle occurs.
    for i, a in enumerate(values):
        for j in range(i + 1, len(values)):
            b = values[j]
            xab = pair[a, b]
            for c in values[j + 1:]:
                xbc = pair[b, c]
                xac = pair[a, c]
                s.add_clause([-xab, -xbc, xac])
                s.add_clause([xab, xbc, -xac])
                clause_count += 2
    # The arithmetic midpoint is not between its endpoints.
    for a, b, c in aps:
        xab, xbc = pair[a, b], pair[b, c]
        s.add_clause([-xab, -xbc])
        s.add_clause([xab, xbc])
        clause_count += 2
    for u, v in attacks:
        s.add_clause([lit_before(u, v)])
        clause_count += 1
    sat = s.solve()
    order = None
    if sat:
        positive = set(x for x in s.get_model() if x > 0)
        order = sorted(values, key=lambda a: sum(
            (pair[b, a] in positive) if b < a else
            (pair[a, b] not in positive) for b in values if b != a))
    stats = s.accum_stats()
    s.delete()
    return {"status": "SAT" if sat else "UNSAT", "variables": next_var - 1,
            "clauses": clause_count, "solver_stats": stats, "order": order}


def rank_model(M: int, seconds: float, workers: int):
    values, aps, attacks = instance(M)
    model = cp_model.CpModel()
    rank = {v: model.NewIntVar(0, M - 1, f"r_{v}") for v in values}
    model.AddAllDifferent(list(rank.values()))
    for k, (a, b, c) in enumerate(aps):
        b_first = model.NewBoolVar(f"mid_first_{k}")
        model.Add(rank[b] < rank[a]).OnlyEnforceIf(b_first)
        model.Add(rank[b] < rank[c]).OnlyEnforceIf(b_first)
        model.Add(rank[b] > rank[a]).OnlyEnforceIf(b_first.Not())
        model.Add(rank[b] > rank[c]).OnlyEnforceIf(b_first.Not())
    for u, v in attacks:
        model.Add(rank[u] < rank[v])
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    status_code = solver.Solve(model)
    status = solver.StatusName(status_code)
    order = None
    if status_code in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        order = sorted(values, key=lambda v: solver.Value(rank[v]))
    return {"status": status, "variables": len(model.Proto().variables),
            "constraints": len(model.Proto().constraints),
            "conflicts": solver.NumConflicts(), "branches": solver.NumBranches(),
            "wall_time": solver.WallTime(), "order": order}


def verify_order(M: int, order):
    values, aps, attacks = instance(M)
    if order is None or sorted(order) != values or len(set(order)) != M:
        return False, "not a permutation of the block"
    pos = {v: i for i, v in enumerate(order)}
    for a, b, c in aps:
        if (pos[a] < pos[b] < pos[c]) or (pos[c] < pos[b] < pos[a]):
            return False, f"monotone AP {(a, b, c)}"
    for u, v in attacks:
        if not pos[u] < pos[v]:
            return False, f"failed attack {(u, v)}"
    return True, "complete direct verification passed"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("M", type=int, nargs="+")
    p.add_argument("--models", choices=("eager", "rank", "both"), default="both")
    p.add_argument("--solver", default="cadical195")
    p.add_argument("--seconds", type=float, default=300.0)
    p.add_argument("--workers", type=int, default=1)
    args = p.parse_args()
    print(json.dumps({"python": platform.python_version(), "platform": platform.platform(),
                      "solver": args.solver, "rank_workers": args.workers}, sort_keys=True))
    for M in args.M:
        rec = {"M": M, "instance_sha256": digest_instance(M)}
        if args.models in ("eager", "both"):
            t = time.monotonic()
            rec["eager"] = eager(M, args.solver)
            rec["eager"]["elapsed"] = time.monotonic() - t
            if rec["eager"]["order"] is not None:
                rec["eager"]["verification"] = verify_order(M, rec["eager"]["order"])
        if args.models in ("rank", "both"):
            rec["rank"] = rank_model(M, args.seconds, args.workers)
            if rec["rank"]["order"] is not None:
                rec["rank"]["verification"] = verify_order(M, rec["rank"]["order"])
        print(json.dumps(rec, sort_keys=True))


if __name__ == "__main__":
    main()
