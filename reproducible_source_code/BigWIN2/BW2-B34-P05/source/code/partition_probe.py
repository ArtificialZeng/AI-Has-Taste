#!/usr/bin/env python3
"""Exact Z3 probe for a sufficient partition condition.

The tested property is the existence of V(G)=A disjoint-union B such that
G[A] is bipartite with maximum degree at most 2 and G[B] has maximum
degree at most 3.  Such a partition gives a 5-colouring of a triangle-free
graph: use two colours on A and three colours on B (Brooks componentwise).

This is a falsification tool, not a proof of the universal property.
"""

from __future__ import annotations

import argparse
import json
import random
from pathlib import Path

import networkx as nx
import z3


def partition_certificate(g: nx.Graph):
    vertices = list(g.nodes())
    in_a = {v: z3.Bool(f"a_{v}") for v in vertices}
    side = {v: z3.Bool(f"s_{v}") for v in vertices}
    solver = z3.Solver()

    for u, v in g.edges():
        # Adjacent vertices that are both in A must be on opposite sides.
        solver.add(z3.Implies(z3.And(in_a[u], in_a[v]), side[u] != side[v]))

    for v in vertices:
        a_degree = z3.Sum([z3.If(in_a[u], 1, 0) for u in g.neighbors(v)])
        b_degree = z3.Sum([z3.If(z3.Not(in_a[u]), 1, 0) for u in g.neighbors(v)])
        solver.add(z3.Implies(in_a[v], a_degree <= 2))
        solver.add(z3.Implies(z3.Not(in_a[v]), b_degree <= 3))

    if solver.check() != z3.sat:
        return None
    model = solver.model()
    a = sorted(v for v in vertices if z3.is_true(model.eval(in_a[v], model_completion=True)))
    b = sorted(set(vertices) - set(a))
    a0 = sorted(v for v in a if not z3.is_true(model.eval(side[v], model_completion=True)))
    a1 = sorted(set(a) - set(a0))
    return {"A0": a0, "A1": a1, "B": b}


def verify_certificate(g: nx.Graph, cert: dict) -> bool:
    a0, a1, b = map(set, (cert["A0"], cert["A1"], cert["B"]))
    if a0 & a1 or a0 & b or a1 & b or a0 | a1 | b != set(g.nodes()):
        return False
    a = a0 | a1
    if any((u in a0 and v in a0) or (u in a1 and v in a1) for u, v in g.edges()):
        return False
    if max((g.subgraph(a).degree(v) for v in a), default=0) > 2:
        return False
    if max((g.subgraph(b).degree(v) for v in b), default=0) > 3:
        return False
    return True


def greedy_triangle_free_graph(n: int, rng: random.Random) -> nx.Graph:
    g = nx.Graph()
    g.add_nodes_from(range(n))
    pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
    rng.shuffle(pairs)
    # Random maximal graph subject to triangle-freeness and the degree cap.
    for u, v in pairs:
        if g.degree(u) >= 6 or g.degree(v) >= 6:
            continue
        if set(g.neighbors(u)).isdisjoint(g.neighbors(v)) and rng.random() < 0.82:
            g.add_edge(u, v)
    return g


def graph_record(name: str, g: nx.Graph) -> dict:
    assert nx.number_of_selfloops(g) == 0
    assert max((d for _, d in g.degree()), default=0) <= 6
    assert not any(nx.triangles(g).values())
    cert = partition_certificate(g)
    return {
        "name": name,
        "order": g.number_of_nodes(),
        "size": g.number_of_edges(),
        "maximum_degree": max((d for _, d in g.degree()), default=0),
        "partition_found": cert is not None,
        "certificate_verified": cert is not None and verify_certificate(g, cert),
        "graph6": nx.to_graph6_bytes(g, header=False).decode().strip(),
        "certificate": cert,
    }


def clebsch_graph() -> nx.Graph:
    """Return the 5-regular Clebsch graph as Q_4 plus antipodal edges."""
    g = nx.hypercube_graph(4)
    for v in list(g.nodes()):
        antipode = tuple(1 - x for x in v)
        g.add_edge(v, antipode)
    return nx.convert_node_labels_to_integers(g)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=3405)
    parser.add_argument("--random-per-order", type=int, default=40)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rng = random.Random(args.seed)

    records = []
    atlas_count = 0
    for i, g in enumerate(nx.graph_atlas_g()):
        if g.number_of_nodes() > 7:
            continue
        if max((d for _, d in g.degree()), default=0) <= 6 and not any(nx.triangles(g).values()):
            records.append(graph_record(f"atlas-{i}", nx.convert_node_labels_to_integers(g)))
            atlas_count += 1

    named = {
        "petersen": nx.petersen_graph(),
        "chvatal": nx.chvatal_graph(),
        "groetzsch": nx.mycielskian(nx.cycle_graph(5)),
        "clebsch": clebsch_graph(),
        "K6,6": nx.complete_bipartite_graph(6, 6),
    }
    for name, g in named.items():
        records.append(graph_record(name, g))

    random_count = 0
    for n in range(8, 61):
        for j in range(args.random_per_order):
            g = greedy_triangle_free_graph(n, rng)
            records.append(graph_record(f"random-n{n}-i{j}", g))
            random_count += 1

    failures = [r for r in records if not r["partition_found"]]
    bad_certificates = [r for r in records if r["partition_found"] and not r["certificate_verified"]]
    result = {
        "tool": "code/partition_probe.py",
        "seed": args.seed,
        "solver": z3.get_version_string(),
        "networkx": nx.__version__,
        "property": "V=A0 disjoint A1 disjoint B; A0,A1 independent; Delta(G[A0 union A1])<=2; Delta(G[B])<=3",
        "coverage": {
            "all_unlabelled_graphs_in_networkx_atlas_with_n_at_most_7_filtered_to_triangle_free_Delta_at_most_6": atlas_count,
            "named_graphs": sorted(named),
            "random_greedy_graphs": random_count,
            "random_orders": [8, 60],
            "random_per_order": args.random_per_order,
        },
        "tested": len(records),
        "failures": failures,
        "bad_certificates": bad_certificates,
        "records": records,
        "limitation": "Random cases are not exhaustive; the atlas is exhaustive only through order 7. SAT only certifies each listed finite instance.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: result[k] for k in ["seed", "coverage", "tested"]}, sort_keys=True))
    print(f"failures={len(failures)} bad_certificates={len(bad_certificates)}")
    if failures or bad_certificates:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
