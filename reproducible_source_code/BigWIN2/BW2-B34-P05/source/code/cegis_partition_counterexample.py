#!/usr/bin/env python3
"""Lazy exact search for a counterexample to candidate C001.

The outer Z3 instance chooses a labelled triangle-free graph of maximum
degree six (optionally with a minimum-degree floor).  A separate inner Z3
instance finds a C001 partition of each graph candidate.  Whenever it finds
one, the outer instance receives the exact negation of that certificate.
Thus a returned graph is an exact counterexample, while an outer UNSAT result
excludes the declared finite graph class.  A timeout is only an incomplete
search result and has no mathematical consequence.

Unlike ``synthesize_partition_counterexample.py``, this CEGIS encoding adds
only partition blockers actually encountered.  It still does not export a
DRAT/LRAT proof for UNSAT.
"""

from __future__ import annotations

import argparse
import json
import time

import networkx as nx
import z3

from partition_probe import partition_certificate, verify_certificate


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--minimum-degree", type=int, default=0)
    parser.add_argument(
        "--degree-ordering",
        action="store_true",
        help="sound symmetry break d(0)>=d(1)>=...>=d(n-1)",
    )
    parser.add_argument("--timeout-ms", type=int, default=300_000)
    parser.add_argument("--progress-every", type=int, default=100)
    args = parser.parse_args()

    n = args.n
    if n < 1:
        raise SystemExit("n must be positive")
    if not 0 <= args.minimum_degree <= 6:
        raise SystemExit("minimum degree must lie between zero and six")

    edge = {
        (u, v): z3.Bool(f"e_{u}_{v}")
        for u in range(n)
        for v in range(u + 1, n)
    }

    def e(u: int, v: int):
        return edge[tuple(sorted((u, v)))]

    outer = z3.Solver()
    degrees = []
    for u in range(n):
        degree = z3.Sum(
            [z3.If(e(u, v), 1, 0) for v in range(n) if u != v]
        )
        degrees.append(degree)
        outer.add(degree >= args.minimum_degree, degree <= 6)
    if args.degree_ordering:
        for u in range(n - 1):
            outer.add(degrees[u] >= degrees[u + 1])
    for u in range(n):
        for v in range(u + 1, n):
            for w in range(v + 1, n):
                outer.add(z3.Not(z3.And(e(u, v), e(u, w), e(v, w))))

    start = time.monotonic()
    candidates = 0
    blockers = 0
    last_graph = None
    status = "unknown"
    counterexample = None

    while True:
        elapsed_ms = int(1000 * (time.monotonic() - start))
        remaining_ms = args.timeout_ms - elapsed_ms
        if remaining_ms <= 0:
            status = "timeout"
            break
        outer.set(timeout=remaining_ms)
        check = outer.check()
        if check == z3.unknown:
            status = "timeout" if "timeout" in outer.reason_unknown() else "unknown"
            break
        if check == z3.unsat:
            status = "unsat"
            break

        model = outer.model()
        graph = nx.Graph()
        graph.add_nodes_from(range(n))
        for (u, v), variable in edge.items():
            if z3.is_true(model.eval(variable, model_completion=True)):
                graph.add_edge(u, v)
        candidates += 1
        last_graph = nx.to_graph6_bytes(graph, header=False).decode().strip()

        certificate = partition_certificate(graph)
        if certificate is None:
            status = "sat"
            counterexample = {
                "graph6": last_graph,
                "size": graph.number_of_edges(),
                "degree_multiset": sorted(degree for _, degree in graph.degree()),
            }
            break
        assert verify_certificate(graph, certificate)

        a0 = set(certificate["A0"])
        a1 = set(certificate["A1"])
        a = a0 | a1
        b = set(certificate["B"])
        failures = []
        for part in (a0, a1):
            for u in part:
                for v in part:
                    if u < v:
                        failures.append(e(u, v))
        for v in a:
            failures.append(
                z3.Sum([z3.If(e(u, v), 1, 0) for u in a if u != v]) >= 3
            )
        for v in b:
            failures.append(
                z3.Sum([z3.If(e(u, v), 1, 0) for u in b if u != v]) >= 4
            )
        assert failures
        outer.add(z3.Or(failures))
        blockers += 1

        if args.progress_every and candidates % args.progress_every == 0:
            print(
                json.dumps(
                    {
                        "progress": True,
                        "candidates": candidates,
                        "partition_blockers": blockers,
                        "elapsed_ms": int(1000 * (time.monotonic() - start)),
                    },
                    sort_keys=True,
                ),
                flush=True,
            )

    result = {
        "tool": "code/cegis_partition_counterexample.py",
        "n": n,
        "minimum_degree": args.minimum_degree,
        "degree_ordering": args.degree_ordering,
        "maximum_degree": 6,
        "triangle_free": True,
        "timeout_ms": args.timeout_ms,
        "elapsed_ms": int(1000 * (time.monotonic() - start)),
        "z3_version": z3.get_version_string(),
        "status": status,
        "graph_candidates_checked": candidates,
        "partition_blockers_added": blockers,
        "last_graph6": last_graph,
        "counterexample": counterexample,
        "limitation": (
            "SAT is an exact finite counterexample. UNSAT is solver evidence "
            "without an exported proof trace. Timeout/unknown is inconclusive."
        ),
    }
    print(json.dumps(result, sort_keys=True))
    if status == "sat":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
