#!/usr/bin/env python3
"""Fail-closed verifier for serialized breaker-search output.

This file deliberately does not import breaker_search.  It reconstructs each
retained explicit tree from its edge list, checks the tree axioms, recomputes
the rooted two-state knapsack using sparse degree dictionaries, and recomputes
Delta directly from its definition.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path


def add_sparse(p: dict[int, int], q: dict[int, int]) -> dict[int, int]:
    out = dict(p)
    for degree, coefficient in q.items():
        out[degree] = out.get(degree, 0) + coefficient
    return {d: c for d, c in out.items() if c}


def multiply_sparse(p: dict[int, int], q: dict[int, int]) -> dict[int, int]:
    out: dict[int, int] = {}
    for d, c in p.items():
        for e, f in q.items():
            out[d + e] = out.get(d + e, 0) + c * f
    return {d: c for d, c in out.items() if c}


def validate_and_recompute(n: int, raw_edges: list[list[int]]) -> list[int]:
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if not isinstance(raw_edges, list) or len(raw_edges) != n - 1:
        raise ValueError("a tree certificate must have exactly n-1 edges")
    parent_dsu = list(range(n))

    def find(x: int) -> int:
        while parent_dsu[x] != x:
            parent_dsu[x] = parent_dsu[parent_dsu[x]]
            x = parent_dsu[x]
        return x

    adj = [[] for _ in range(n)]
    seen_edges: set[tuple[int, int]] = set()
    for edge in raw_edges:
        if not isinstance(edge, list) or len(edge) != 2:
            raise ValueError("every edge must be a two-element JSON list")
        u, v = edge
        if not isinstance(u, int) or not isinstance(v, int) or not (0 <= u < n and 0 <= v < n):
            raise ValueError("edge endpoint outside 0,...,n-1")
        if u == v:
            raise ValueError("loop")
        key = (min(u, v), max(u, v))
        if key in seen_edges:
            raise ValueError("duplicate edge")
        seen_edges.add(key)
        ru, rv = find(u), find(v)
        if ru == rv:
            raise ValueError("cycle")
        parent_dsu[ru] = rv
        adj[u].append(v)
        adj[v].append(u)
    if len({find(v) for v in range(n)}) != 1:
        raise ValueError("disconnected")

    # Use the largest-labeled vertex as root, distinct from discovery's root 0.
    root = n - 1
    parent = [-2] * n
    parent[root] = -1
    queue = [root]
    for v in queue:
        for w in sorted(adj[v], reverse=True):
            if parent[w] == -2:
                parent[w] = v
                queue.append(w)
    state: list[tuple[dict[int, int], dict[int, int]] | None] = [None] * n
    for v in reversed(queue):
        root_out = {0: 1}
        root_in = {1: 1}
        for w in adj[v]:
            if parent[w] == v:
                assert state[w] is not None
                child_out, child_in = state[w]
                root_out = multiply_sparse(root_out, add_sparse(child_out, child_in))
                root_in = multiply_sparse(root_in, child_out)
        state[v] = root_out, root_in
    assert state[root] is not None
    total = add_sparse(*state[root])
    max_degree = max(total)
    coefficients = [total.get(k, 0) for k in range(max_degree + 1)]
    if coefficients[0] != 1 or any(x <= 0 for x in coefficients):
        raise ValueError("invalid reconstructed independent-set sequence")
    return coefficients


def delta_from_suffix_maxima(a: list[int]) -> tuple[int | None, list[int] | None]:
    if len(a) < 3:
        return None, None
    # For fixed ell the maximizing k and m are independently the left and
    # right maxima.  This is an exact rearrangement of the literal definition,
    # not a floating-point shortcut.
    right_value = [0] * len(a)
    right_index = [0] * len(a)
    value, index = a[-1], len(a) - 1
    for j in range(len(a) - 1, -1, -1):
        if a[j] > value:
            value, index = a[j], j
        right_value[j], right_index[j] = value, index
    left_value, left_index = a[0], 0
    best = None
    triple = None
    for ell in range(1, len(a) - 1):
        if a[ell - 1] > left_value:
            left_value, left_index = a[ell - 1], ell - 1
        candidate = min(left_value - a[ell], right_value[ell + 1] - a[ell])
        if best is None or candidate > best:
            best = candidate
            triple = [left_index, ell, right_index[ell + 1]]
    return best, triple


def verify_generic_lemmas(data: dict) -> None:
    sum_witness = data["lemma_audit"]["generic_sum_closure_counterexample"]
    a, b = sum_witness["a"], sum_witness["b"]
    total = [x + y for x, y in zip(a, b)]
    if total != sum_witness["a_plus_b"] or delta_from_suffix_maxima(total)[0] != 1:
        raise ValueError("generic sum witness failed")
    conv_witness = data["lemma_audit"]["generic_convolution_closure_counterexample"]
    a, b = conv_witness["a"], conv_witness["b"]
    conv = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            conv[i + j] += x * y
    if conv != conv_witness["convolution"] or delta_from_suffix_maxima(conv)[0] != 1:
        raise ValueError("generic convolution witness failed")


def gather_explicit_candidates(data: dict) -> list[dict]:
    phases = data["phases"]
    candidates: list[dict] = []
    for item in (
        phases["repeated_hubs"].get("best"),
        phases["known_style_hub_and_path_arm_families"]["galvin"].get("best"),
        phases["known_style_hub_and_path_arm_families"]["three_arm"].get("best"),
        phases["known_style_hub_and_path_arm_families"].get("known_26_vertex_benchmark"),
        phases["fixed_order_subtree_prune_regraft"].get("counterexample"),
        phases["repeated_hubs"].get("counterexample"),
        phases["known_style_hub_and_path_arm_families"].get("counterexample"),
    ):
        if item is not None:
            candidates.append(item)
    candidates.extend(phases["fixed_order_subtree_prune_regraft"].get("retained_best_per_size", []))
    return candidates


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    raw = args.input.read_bytes()
    data = json.loads(raw)
    if data.get("schema") != "breaker-search-v1":
        raise ValueError("wrong or missing schema")
    if data.get("decision_rule") != "Delta>0 using exact Python integers":
        raise ValueError("unexpected decision convention")
    verify_generic_lemmas(data)
    candidates = gather_explicit_candidates(data)
    verified = []
    for candidate in candidates:
        coefficients = candidate.get("coefficients")
        edges = candidate.get("edges")
        n = candidate.get("n")
        if not isinstance(coefficients, list) or not all(isinstance(x, int) for x in coefficients):
            raise ValueError(f"missing integer coefficients in {candidate.get('label')}")
        rebuilt = validate_and_recompute(n, edges)
        if rebuilt != coefficients:
            raise ValueError(f"coefficient mismatch in {candidate.get('label')}")
        delta, _ = delta_from_suffix_maxima(rebuilt)
        if delta != candidate.get("delta"):
            raise ValueError(f"Delta mismatch in {candidate.get('label')}")
        verified.append({"label": candidate.get("label"), "n": n, "delta": delta})

    search_counterexamples = data.get("counterexamples_found")
    if not isinstance(search_counterexamples, list):
        raise ValueError("counterexamples_found must be a list")
    for candidate in search_counterexamples:
        rebuilt = validate_and_recompute(candidate["n"], candidate["edges"])
        delta, triple = delta_from_suffix_maxima(rebuilt)
        if rebuilt != candidate["coefficients"] or delta is None or delta <= 0:
            raise ValueError("purported counterexample is not certified")
        verified.append({"label": candidate.get("label"), "n": candidate["n"], "delta": delta, "triple": triple})

    verifier_hash = hashlib.sha256(Path(__file__).resolve().read_bytes()).hexdigest()
    print(json.dumps({
        "status": "PASS",
        "input_sha256": hashlib.sha256(raw).hexdigest(),
        "verifier_sha256": verifier_hash,
        "python": sys.version,
        "explicit_candidates_verified": verified,
        "certified_counterexample_count": len(search_counterexamples),
        "scope_warning": "PASS verifies serialized explicit trees; it does not certify completeness of heuristic search phases.",
    }, indent=2))


if __name__ == "__main__":
    main()
