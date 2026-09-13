#!/usr/bin/env python3
"""Enumerate and spectrally screen all unlabeled biconnected graphs, n=4..8.

Discovery uses 80-decimal-digit symmetric eigensolving.  Every graph whose
observed gap is at most 1.01 receives an exact certificate consisting of its
integer characteristic polynomial and disjoint rational isolating intervals
for every real root.  A rational lower bound on the positive-root square sum
then certifies s^+(G)>n for each such near-minimizer.

Requirements: nauty `geng`, NetworkX, mpmath, and SymPy.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import networkx as nx
import sympy as sp


X = sp.Symbol("x")
WORKING_DPS = 80
CANDIDATE_TOLERANCE = mp.mpf("1e-50")
NEAR_GAP_CUTOFF = mp.mpf("1.01")
ISOLATION_EPSILON = sp.Rational(1, 10**20)


def fraction_pair(value: sp.Rational) -> list[int]:
    q = sp.Rational(value)
    return [int(q.p), int(q.q)]


def exact_certificate(graph: nx.Graph) -> dict:
    n = graph.number_of_nodes()
    adjacency = sp.zeros(n)
    for u, v in graph.edges():
        adjacency[u, v] = adjacency[v, u] = 1
    polynomial = sp.Poly(adjacency.charpoly(X).as_expr(), X, domain=sp.ZZ)
    intervals = polynomial.intervals(eps=ISOLATION_EPSILON)

    serialized = []
    lower = sp.Rational(0)
    upper = sp.Rational(0)
    positive_multiplicity = 0
    total_multiplicity = 0
    for (left, right), multiplicity in intervals:
        left = sp.Rational(left)
        right = sp.Rational(right)
        total_multiplicity += int(multiplicity)
        serialized.append(
            {
                "left": fraction_pair(left),
                "right": fraction_pair(right),
                "multiplicity": int(multiplicity),
            }
        )
        if left > 0:
            positive_multiplicity += int(multiplicity)
            lower += multiplicity * left**2
            upper += multiplicity * right**2
        elif right > 0:
            raise RuntimeError("root interval straddles zero")

    if total_multiplicity != n:
        raise RuntimeError("characteristic polynomial has unaccounted roots")
    if lower <= n:
        raise RuntimeError("chosen isolation precision does not certify strictness")

    return {
        "characteristic_polynomial_coefficients": [
            int(c) for c in polynomial.all_coeffs()
        ],
        "characteristic_polynomial_factorization": str(sp.factor(polynomial.as_expr())),
        "real_root_isolating_intervals": serialized,
        "positive_root_multiplicity": positive_multiplicity,
        "splus_lower_bound": fraction_pair(lower),
        "splus_upper_bound": fraction_pair(upper),
        "gap_lower_bound": fraction_pair(lower - n),
        "certificate_check": "sum(left_endpoint^2 * multiplicity) > n",
    }


def graph_record(graph: nx.Graph, code: str, eigenvalues: list[mp.mpf]) -> dict:
    n = graph.number_of_nodes()
    splus = mp.fsum(value**2 for value in eigenvalues if value > 0)
    gap = splus - n
    triangles = sum(nx.triangles(graph).values()) // 3
    return {
        "graph6": code,
        "edges": graph.number_of_edges(),
        "degree_sequence": sorted((d for _, d in graph.degree()), reverse=True),
        "triangles": triangles,
        "eigenvalues_80dps": [mp.nstr(value, 75) for value in eigenvalues],
        "splus_80dps": mp.nstr(splus, 75),
        "gap_80dps": mp.nstr(gap, 75),
    }


def enumerate_order(n: int) -> dict:
    completed = subprocess.run(
        ["geng", "-q", "-C", str(n)], check=True, capture_output=True
    )
    encodings = completed.stdout.splitlines()
    noncycles = []
    candidates = []
    near = []

    for raw in encodings:
        graph = nx.from_graph6_bytes(raw)
        if all(degree == 2 for _, degree in graph.degree()):
            continue
        code = raw.decode("ascii")
        matrix = mp.matrix(
            [[int(graph.has_edge(i, j)) for j in range(n)] for i in range(n)]
        )
        eigenvalues = [mp.mpf(v) for v in mp.eigsy(matrix, eigvals_only=True)]
        record = graph_record(graph, code, eigenvalues)
        gap = mp.mpf(record["gap_80dps"])
        noncycles.append((gap, record))
        if abs(gap) <= CANDIDATE_TOLERANCE:
            exact = exact_certificate(graph)
            candidates.append(record | {"exact_certificate": exact})
        if gap <= NEAR_GAP_CUTOFF:
            exact = exact_certificate(graph)
            near.append(record | {"exact_certificate": exact})

    noncycles.sort(key=lambda item: (item[0], item[1]["graph6"]))
    near.sort(key=lambda item: (mp.mpf(item["gap_80dps"]), item["graph6"]))
    return {
        "order": n,
        "unlabeled_biconnected_generated": len(encodings),
        "unlabeled_biconnected_noncycles": len(noncycles),
        "minimum_observed_gap": noncycles[0][1],
        "candidate_count": len(candidates),
        "candidates": candidates,
        "near_gap_definition": "80-dps observed splus-n <= 1.01",
        "near_gap_count": len(near),
        "near_gap_exact_certificates": near,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    if shutil.which("geng") is None:
        raise SystemExit("nauty geng is not on PATH")

    mp.mp.dps = WORKING_DPS
    orders = [enumerate_order(n) for n in range(4, 9)]
    geng_help = subprocess.run(
        ["geng", "-help"], check=True, capture_output=True, text=True
    ).stdout.splitlines()
    geng_usage = next(line.strip() for line in geng_help if line.strip())
    result = {
        "scope": {
            "orders": [4, 5, 6, 7, 8],
            "generator": "geng -q -C n (one graph6 encoding per unlabeled biconnected graph)",
            "cycle_filter": "exclude the unique 2-regular graph at each order",
            "precision_decimal_digits": WORKING_DPS,
            "equality_candidate_tolerance": "abs(splus-n) <= 1e-50",
            "exact_near_gap_cutoff": "splus-n <= 1.01 at 80 dps",
        },
        "software": {
            "geng": geng_usage,
            "networkx": nx.__version__,
            "mpmath": mp.__version__,
            "sympy": sp.__version__,
        },
        "orders": orders,
        "totals": {
            "unlabeled_biconnected_generated": sum(
                row["unlabeled_biconnected_generated"] for row in orders
            ),
            "unlabeled_biconnected_noncycles": sum(
                row["unlabeled_biconnected_noncycles"] for row in orders
            ),
            "equality_candidates": sum(row["candidate_count"] for row in orders),
            "near_gap_graphs_exactly_certified_strict": sum(
                row["near_gap_count"] for row in orders
            ),
        },
        "interpretation": (
            "This is an exact-isomorphism-class enumeration but only finite evidence. "
            "No equality candidate occurs. Rational root isolation proves every recorded "
            "near-gap graph has splus>n; the all-orders conclusion is supplied separately "
            "by evidence/strictness_proof.md."
        ),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
