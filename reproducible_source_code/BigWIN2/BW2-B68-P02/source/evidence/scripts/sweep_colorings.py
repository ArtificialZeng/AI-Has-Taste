#!/usr/bin/env python3
"""SAT sweep for A(G), E(G), with directly replayable positive witnesses.

This is a classifier/witness generator, not an UNSAT certification pipeline.
An UNSAT solver result is recorded only as an observation.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import networkx as nx
from pysat.card import CardEnc, EncType
from pysat.formula import CNF, IDPool
from pysat.solvers import Solver


ROOT = Path(__file__).resolve().parents[2]
ORDERS = (4, 6, 8, 10, 12, 14, 16, 18)


def total_graph_elements(graph: nx.Graph) -> tuple[list[tuple[str, int, int]], list[tuple[int, int]]]:
    """Return stable elements and all unordered total-color conflicts."""
    n = graph.number_of_nodes()
    edges = sorted((min(u, v), max(u, v)) for u, v in graph.edges())
    elements = [("v", v, -1) for v in range(n)] + [("e", u, v) for u, v in edges]
    conflicts: set[tuple[int, int]] = set()
    edge_index = {(u, v): n + i for i, (u, v) in enumerate(edges)}
    for u, v in edges:
        conflicts.add((u, v))
        ei = edge_index[(u, v)]
        conflicts.add((min(u, ei), max(u, ei)))
        conflicts.add((min(v, ei), max(v, ei)))
    for vertex in range(n):
        incident = sorted(
            edge_index[(min(vertex, neighbor), max(vertex, neighbor))]
            for neighbor in graph.neighbors(vertex)
        )
        for i in range(len(incident)):
            for j in range(i + 1, len(incident)):
                conflicts.add((incident[i], incident[j]))
    return elements, sorted(conflicts)


def build_cnf(graph: nx.Graph, equitable: bool) -> tuple[CNF, list[list[int]]]:
    elements, conflicts = total_graph_elements(graph)
    pool = IDPool()
    variables = [[pool.id((element, color)) for color in range(4)] for element in range(len(elements))]
    cnf = CNF()
    for row in variables:
        cnf.append(row)
        for i in range(4):
            for j in range(i + 1, 4):
                cnf.append([-row[i], -row[j]])
    for first, second in conflicts:
        for color in range(4):
            cnf.append([-variables[first][color], -variables[second][color]])
    # Color permutation symmetry: element 0 may be assigned color 0.
    cnf.append([variables[0][0]])
    if equitable:
        total = len(elements)
        lower = total // 4
        upper = (total + 3) // 4
        for color in range(4):
            literals = [row[color] for row in variables]
            cnf.extend(
                CardEnc.atleast(literals, bound=lower, vpool=pool, encoding=EncType.seqcounter).clauses
            )
            cnf.extend(
                CardEnc.atmost(literals, bound=upper, vpool=pool, encoding=EncType.seqcounter).clauses
            )
    return cnf, variables


def solve(graph: nx.Graph, equitable: bool) -> tuple[bool, list[int] | None]:
    cnf, variables = build_cnf(graph, equitable)
    with Solver(name="cadical195", bootstrap_with=cnf.clauses) as solver:
        sat = solver.solve()
        if not sat:
            return False, None
        positive = set(literal for literal in solver.get_model() if literal > 0)
        colors = [next(color for color, variable in enumerate(row) if variable in positive) for row in variables]
        return True, colors


def verify_witness(graph: nx.Graph, colors: list[int], equitable: bool) -> None:
    elements, conflicts = total_graph_elements(graph)
    assert len(colors) == len(elements)
    assert all(0 <= color < 4 for color in colors)
    assert all(colors[first] != colors[second] for first, second in conflicts)
    if equitable:
        counts = [colors.count(color) for color in range(4)]
        assert max(counts) - min(counts) <= 1, counts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-order", type=int, default=18)
    args = parser.parse_args()
    output = ROOT / "evidence" / "coloring_witnesses.jsonl"
    summary_path = ROOT / "evidence" / "coloring_sweep_summary.json"
    started = time.monotonic()
    summary_orders = []
    total_e_sat = total_e_unsat = total_a_sat_after_e_unsat = total_a_unsat = 0
    with output.open("w") as stream:
        for n in ORDERS:
            if n > args.max_order:
                break
            codes = (ROOT / "census" / f"n{n:02d}.g6").read_bytes().splitlines()
            counts = {"E_sat": 0, "E_unsat": 0, "A_sat_after_E_unsat": 0, "A_unsat": 0}
            order_started = time.monotonic()
            for index, raw_code in enumerate(codes):
                graph = nx.from_graph6_bytes(raw_code)
                e_sat, colors = solve(graph, equitable=True)
                row = {"n": n, "index": index, "graph6": raw_code.decode("ascii")}
                if e_sat:
                    assert colors is not None
                    verify_witness(graph, colors, equitable=True)
                    counts["E_sat"] += 1
                    row.update({"classification": "E_sat", "colors": colors})
                else:
                    counts["E_unsat"] += 1
                    a_sat, a_colors = solve(graph, equitable=False)
                    if a_sat:
                        assert a_colors is not None
                        verify_witness(graph, a_colors, equitable=False)
                        counts["A_sat_after_E_unsat"] += 1
                        row.update({"classification": "A_sat_E_unsat_observed", "colors": a_colors})
                    else:
                        counts["A_unsat"] += 1
                        row.update({"classification": "A_unsat_observed"})
                stream.write(json.dumps(row, separators=(",", ":"), sort_keys=True) + "\n")
            elapsed = time.monotonic() - order_started
            counts.update({"n": n, "graphs": len(codes), "seconds": round(elapsed, 6)})
            summary_orders.append(counts)
            total_e_sat += counts["E_sat"]
            total_e_unsat += counts["E_unsat"]
            total_a_sat_after_e_unsat += counts["A_sat_after_E_unsat"]
            total_a_unsat += counts["A_unsat"]
            stream.flush()
            print(json.dumps(counts, sort_keys=True), flush=True)
    raw_output = output.read_bytes()
    report = {
        "script": str(Path(__file__).relative_to(ROOT)),
        "solver": "PySAT cadical195",
        "scope": f"orders <= {args.max_order}",
        "orders": summary_orders,
        "totals": {
            "E_sat": total_e_sat,
            "E_unsat": total_e_unsat,
            "A_sat_after_E_unsat": total_a_sat_after_e_unsat,
            "A_unsat": total_a_unsat,
        },
        "witness_file": str(output.relative_to(ROOT)),
        "witness_file_sha256": hashlib.sha256(raw_output).hexdigest(),
        "seconds": round(time.monotonic() - started, 6),
        "epistemic_status": (
            "Every SAT row includes a coloring checked directly. UNSAT rows are solver observations, "
            "not certificates and not mathematical conclusions."
        ),
    }
    summary_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
