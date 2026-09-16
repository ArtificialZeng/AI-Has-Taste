#!/usr/bin/env python3
"""Synthesize a smallest counterexample to the bipartite-(2)/subcubic partition.

For a fixed labelled order n, the SMT formula quantifies graph edges
existentially and explicitly conjoins the failure of every one of the 3^n
vertex assignments to A0, A1, or B.  Thus UNSAT excludes every labelled (and
hence every unlabelled) triangle-free graph of that order.  Z3's answer is an
exact Boolean/cardinality result, but no independently checkable DRAT proof is
exported by this script.
"""

from __future__ import annotations

import argparse
import itertools
import json

import networkx as nx
import z3


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--timeout-ms", type=int, default=300000)
    args = parser.parse_args()
    n = args.n
    if not 1 <= n <= 11:
        raise SystemExit("This explicit 3^n encoding is limited to 1 <= n <= 11.")

    edge = {(u, v): z3.Bool(f"e_{u}_{v}") for u in range(n) for v in range(u + 1, n)}

    def e(u: int, v: int):
        return edge[tuple(sorted((u, v)))]

    solver = z3.Solver()
    solver.set(timeout=args.timeout_ms)
    for u, v, w in itertools.combinations(range(n), 3):
        solver.add(z3.Not(z3.And(e(u, v), e(u, w), e(v, w))))
    for v in range(n):
        solver.add(z3.Sum([z3.If(e(u, v), 1, 0) for u in range(n) if u != v]) <= 6)

    assignments = 0
    for state in itertools.product(range(3), repeat=n):
        # state 0=A0, 1=A1, 2=B.  Require this assignment to fail at least
        # one certificate condition.
        failures = []
        for u, v in itertools.combinations(range(n), 2):
            if state[u] == state[v] and state[u] in (0, 1):
                failures.append(e(u, v))
        a = {v for v in range(n) if state[v] in (0, 1)}
        b = set(range(n)) - a
        for v in a:
            failures.append(z3.Sum([z3.If(e(u, v), 1, 0) for u in a if u != v]) >= 3)
        for v in b:
            failures.append(z3.Sum([z3.If(e(u, v), 1, 0) for u in b if u != v]) >= 4)
        solver.add(z3.Or(failures))
        assignments += 1

    status = solver.check()
    result = {
        "tool": "code/synthesize_partition_counterexample.py",
        "n": n,
        "assignments_explicitly_blocked": assignments,
        "triangle_free": True,
        "maximum_degree_cap": 6,
        "z3_version": z3.get_version_string(),
        "timeout_ms": args.timeout_ms,
        "status": str(status),
        "limitation": "UNSAT is solver evidence; this run does not emit an independently checkable proof trace.",
    }
    if status == z3.sat:
        model = solver.model()
        g = nx.Graph()
        g.add_nodes_from(range(n))
        for (u, v), var in edge.items():
            if z3.is_true(model.eval(var, model_completion=True)):
                g.add_edge(u, v)
        result.update({
            "graph6": nx.to_graph6_bytes(g, header=False).decode().strip(),
            "size": g.number_of_edges(),
            "degree_multiset": sorted(d for _, d in g.degree()),
        })
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
