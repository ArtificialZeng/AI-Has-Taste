#!/usr/bin/env python3
"""Standalone checker for the transparent pass-2 SAT certificates.

This file does not import the RDS parser or Z3 census implementation.  It reads
only JSON, reconstructs each labelled tournament, and recounts every pair in
the five claimed strict orders.
"""

import argparse
import hashlib
import itertools
import json
import sys

import networkx as nx


N = 9
EXPECTED = 254
PAIRS = list(itertools.combinations(range(N), 2))


def fail(message):
    raise SystemExit("verification failed: " + message)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", nargs="?", default="evidence/research_pass2_results.json")
    ap.add_argument("--output", default="evidence/research_pass2_verification.json")
    args = ap.parse_args()

    raw = open(args.input, "rb").read()
    data = json.loads(raw)
    records = data.get("records")
    if not isinstance(records, list) or len(records) != EXPECTED:
        fail("expected exactly 254 records")
    if data.get("matrix_count") != EXPECTED or data.get("tallies") != {
        "sat": EXPECTED, "unsat": 0, "unknown": 0
    }:
        fail("top-level counts do not describe a complete positive census")

    seen = set()
    graphs = []
    arc_recounts = 0
    canonical_lines = []
    for expected_index, rec in enumerate(records, 1):
        if rec.get("index") != expected_index or rec.get("solver_status") != "sat":
            fail(f"bad record index/status at {expected_index}")
        bits = rec.get("upper_triangle_bits")
        if not isinstance(bits, str) or len(bits) != len(PAIRS) or set(bits) - {"0", "1"}:
            fail(f"bad 36-bit adjacency encoding at {expected_index}")
        if bits in seen:
            fail(f"duplicate labelled tournament at {expected_index}")
        seen.add(bits)
        if rec.get("sha256_bitstring") != hashlib.sha256(bits.encode()).hexdigest():
            fail(f"bad adjacency digest at {expected_index}")
        if rec.get("upper_triangle_order") != [list(p) for p in PAIRS]:
            fail(f"unexpected pair ordering at {expected_index}")
        graph = nx.DiGraph()
        graph.add_nodes_from(range(N))
        for bit, (a, b) in zip(bits, PAIRS):
            graph.add_edge(a, b) if bit == "1" else graph.add_edge(b, a)
        graphs.append(graph)

        orders = rec.get("five_orders_zero_based")
        if not isinstance(orders, list) or len(orders) != 5:
            fail(f"not five orders at {expected_index}")
        positions = []
        for voter, order in enumerate(orders):
            if not isinstance(order, list) or sorted(order) != list(range(N)):
                fail(f"voter {voter} is not a permutation at {expected_index}")
            positions.append({vertex: rank for rank, vertex in enumerate(order)})

        for bit, (a, b) in zip(bits, PAIRS):
            support_a_b = sum(pos[a] < pos[b] for pos in positions)
            support_target = support_a_b if bit == "1" else 5 - support_a_b
            if support_target != 3:
                fail(f"arc {a},{b} has support {support_target} at {expected_index}")
            arc_recounts += 1
        canonical_lines.append(bits + ":" + ",".join("".join(map(str, o)) for o in orders))

    # Exact directed-graph isomorphism, restricted first by the necessary
    # out-degree multiset invariant.  This confirms that the 254 serialized
    # representatives are pairwise non-isomorphic, not merely differently labelled.
    buckets = {}
    for index, graph in enumerate(graphs):
        degree_key = tuple(sorted(dict(graph.out_degree()).values()))
        buckets.setdefault(degree_key, []).append(index)
    iso_candidate_pairs = 0
    for indices in buckets.values():
        for offset, left in enumerate(indices):
            for right in indices[offset + 1:]:
                iso_candidate_pairs += 1
                if nx.is_isomorphic(graphs[left], graphs[right]):
                    fail(f"records {left + 1} and {right + 1} are isomorphic")

    certificate_digest = hashlib.sha256(("\n".join(canonical_lines) + "\n").encode()).hexdigest()
    report = {
        "verifier": "research_pass2_verify.py (JSON-only; no Z3 or RDS-parser import)",
        "input_file": args.input,
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "records_verified": len(records),
        "distinct_labelled_tournaments": len(seen),
        "pairwise_nonisomorphic_tournaments": len(graphs),
        "isomorphism_candidate_pairs_checked": iso_candidate_pairs,
        "permutations_verified": 5 * len(records),
        "target_arcs_recounted": arc_recounts,
        "all_target_arc_supports": 3,
        "canonical_certificate_sha256": certificate_digest,
        "status": "PASS",
    }
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
        f.write("\n")
    json.dump(report, sys.stdout, indent=2)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
