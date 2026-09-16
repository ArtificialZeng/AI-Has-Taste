#!/usr/bin/env python3
"""Discovery-only CP-SAT model for max |A+A|; solver bounds are not certificates."""
import argparse
import json
import platform
import time
from ortools.sat.python import cp_model
import ortools


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=38)
    ap.add_argument("--k", type=int, default=12)
    ap.add_argument("--seconds", type=float, default=300)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--seed", type=int, default=1238)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    model = cp_model.CpModel()
    x = {i: model.new_bool_var(f"x_{i}") for i in range(1, args.n + 1)}
    model.add(sum(x.values()) == args.k)
    # Translation gives a representative with minimum 1.
    model.add(x[1] == 1)
    by_sum = {s: [] for s in range(2, 2 * args.n + 1)}
    for i in range(1, args.n + 1):
        for j in range(i, args.n + 1):
            if i == j:
                z = x[i]
            else:
                z = model.new_bool_var(f"z_{i}_{j}")
                model.add(z <= x[i])
                model.add(z <= x[j])
                model.add(z >= x[i] + x[j] - 1)
            by_sum[i + j].append(z)
    y = {}
    for s, reps in by_sum.items():
        y[s] = model.new_bool_var(f"y_{s}")
        model.add(y[s] <= sum(reps))
    model.maximize(sum(y.values()))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.num_search_workers = args.workers
    solver.parameters.random_seed = args.seed
    solver.parameters.log_search_progress = True
    t0 = time.time()
    status = solver.solve(model)
    elapsed = time.time() - t0
    chosen = [i for i in x if solver.boolean_value(x[i])] if status in (
        cp_model.OPTIMAL, cp_model.FEASIBLE) else None
    sums = sorted({a + b for p, a in enumerate(chosen or []) for b in (chosen or [])[p:]})
    record = {
        "purpose": "discovery only; not an upper-bound certificate",
        "python": platform.python_version(),
        "ortools": ortools.__version__,
        "parameters": vars(args),
        "status": solver.status_name(status),
        "objective": len(sums) if chosen is not None else None,
        "solver_objective": solver.objective_value if chosen is not None else None,
        "solver_best_bound": solver.best_objective_bound,
        "chosen": chosen,
        "sums": sums,
        "elapsed_seconds": elapsed,
        "response_stats": solver.response_stats(),
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(record, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
