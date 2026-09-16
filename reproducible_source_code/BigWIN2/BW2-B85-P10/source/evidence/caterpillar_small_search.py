#!/usr/bin/env python3
"""Exact finite search for the zero-leg caterpillar domination claim.

Uses the standard three rooted states and independently cross-checks every
parameter vector of total order at most --bruteforce-max-n by subset
enumeration.  All arithmetic is Python integer arithmetic.
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict


def trim(p: list[int]) -> list[int]:
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(*polys: list[int]) -> list[int]:
    out = [0] * max(map(len, polys))
    for p in polys:
        for i, value in enumerate(p):
            out[i] += value
    return trim(out)


def sub(p: list[int], q: list[int]) -> list[int]:
    out = p + [0] * max(0, len(q) - len(p))
    for i, value in enumerate(q):
        out[i] -= value
    assert all(value >= 0 for value in out)
    return trim(out)


def mul(p: list[int], q: list[int]) -> list[int]:
    if p == [0] or q == [0]:
        return [0]
    out = [0] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return trim(out)


def caterpillar_adjacency(a: tuple[int, ...]) -> list[list[int]]:
    k = len(a)
    n = k + sum(a)
    adjacency = [[] for _ in range(n)]
    for i in range(k - 1):
        adjacency[i].append(i + 1)
        adjacency[i + 1].append(i)
    leaf = k
    for spine, count in enumerate(a):
        for _ in range(count):
            adjacency[spine].append(leaf)
            adjacency[leaf].append(spine)
            leaf += 1
    assert leaf == n
    return adjacency


def rooted_states(
    adjacency: list[list[int]], vertex: int, parent: int
) -> tuple[list[int], list[int], list[int]]:
    children = [u for u in adjacency[vertex] if u != parent]
    states = [rooted_states(adjacency, u, vertex) for u in children]

    # A: root chosen.  B: root not chosen but dominated below.
    # C: root not chosen and requires domination by its parent.
    A = [0, 1]
    for child_A, child_B, child_C in states:
        A = mul(A, add(child_A, child_B, child_C))

    internally_valid = [1]
    no_child_chosen = [1]
    for child_A, child_B, _ in states:
        internally_valid = mul(internally_valid, add(child_A, child_B))
        no_child_chosen = mul(no_child_chosen, child_B)
    B = sub(internally_valid, no_child_chosen)
    C = no_child_chosen
    return A, B, C


def dp_polynomial(a: tuple[int, ...]) -> list[int]:
    adjacency = caterpillar_adjacency(a)
    A, B, _ = rooted_states(adjacency, 0, -1)
    out = add(A, B)
    n = len(adjacency)
    return out + [0] * (n + 1 - len(out))


def brute_polynomial(a: tuple[int, ...]) -> list[int]:
    adjacency = caterpillar_adjacency(a)
    n = len(adjacency)
    closed = []
    for v, neighbors in enumerate(adjacency):
        mask = 1 << v
        for u in neighbors:
            mask |= 1 << u
        closed.append(mask)
    target = (1 << n) - 1
    coeffs = [0] * (n + 1)
    for chosen in range(1 << n):
        dominated = 0
        remaining = chosen
        while remaining:
            bit = remaining & -remaining
            dominated |= closed[bit.bit_length() - 1]
            remaining -= bit
        if dominated == target:
            coeffs[chosen.bit_count()] += 1
    return coeffs


def weak_compositions(total: int, length: int):
    if length == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for rest in weak_compositions(total - first, length - 1):
            yield (first,) + rest


def validate_recurrence(bruteforce_max_n: int) -> dict[str, int]:
    comparisons = 0
    endpoint_reductions = 0
    for n in range(1, bruteforce_max_n + 1):
        for k in range(1, n + 1):
            for a in weak_compositions(n - k, k):
                dp = dp_polynomial(a)
                brute = brute_polynomial(a)
                assert dp == brute, (a, dp, brute)
                comparisons += 1
                if k >= 2 and a[0] == 0:
                    reduced = (a[1] + 1,) + a[2:]
                    assert dp == dp_polynomial(reduced), (a, reduced)
                    endpoint_reductions += 1
                if k >= 2 and a[-1] == 0:
                    reduced = a[:-2] + (a[-2] + 1,)
                    assert dp == dp_polynomial(reduced), (a, reduced)
                    endpoint_reductions += 1
    return {
        "parameter_vectors_dp_vs_bruteforce": comparisons,
        "endpoint_reduction_checks": endpoint_reductions,
    }


def normalized_cores(n: int):
    for k in range(3, n - 1):
        remainder = n - k - 2
        if remainder < 0:
            continue
        for b in weak_compositions(remainder, k):
            a = (b[0] + 1,) + b[1:-1] + (b[-1] + 1,)
            if not any(value == 0 for value in a[1:-1]):
                continue
            if a > tuple(reversed(a)):
                continue
            yield a


def search(max_n: int) -> dict[str, object]:
    cases_by_n: dict[int, int] = defaultdict(int)
    cases = 0
    minors = 0
    best = None
    for n in range(1, max_n + 1):
        for a in normalized_cores(n):
            coeffs = dp_polynomial(a)
            cases += 1
            cases_by_n[n] += 1
            for j in range(1, n):
                slack = coeffs[j] * coeffs[j] - coeffs[j - 1] * coeffs[j + 1]
                minors += 1
                if slack < 0:
                    return {
                        "status": "counterexample",
                        "first_total_order": n,
                        "parameter_vector": list(a),
                        "coefficients_d_0_through_d_N": coeffs,
                        "violating_index": j,
                        "slack": slack,
                        "cases_completed_before_certificate": cases - 1,
                        "minors_checked_through_certificate": minors,
                    }
                if coeffs[j - 1] * coeffs[j + 1] > 0:
                    record = {
                        "slack": slack,
                        "total_order": n,
                        "parameter_vector": list(a),
                        "index": j,
                        "triple": [coeffs[j - 1], coeffs[j], coeffs[j + 1]],
                    }
                    if best is None or (slack, n, a, j) < (
                        best["slack"],
                        best["total_order"],
                        tuple(best["parameter_vector"]),
                        best["index"],
                    ):
                        best = record
    return {
        "status": "no_counterexample_in_covered_range",
        "coverage": {
            "normalized_core_conditions": (
                "k>=3, endpoint legs positive, at least one internal zero; "
                "one representative modulo reversal"
            ),
            "total_order_N": [1, max_n],
            "parameter_vectors": cases,
            "log_concavity_minors": minors,
            "cases_by_N": {str(n): cases_by_n[n] for n in sorted(cases_by_n)},
        },
        "smallest_positive-support_slack": best,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=18)
    parser.add_argument("--bruteforce-max-n", type=int, default=10)
    args = parser.parse_args()
    assert 1 <= args.bruteforce_max_n <= args.max_n

    result = {
        "method": {
            "arithmetic": "exact integers",
            "tree_dp_states": ["root chosen", "root dominated below", "root needs parent"],
            "enumeration_order": "increasing total order N",
        },
        "independent_validation": validate_recurrence(args.bruteforce_max_n),
        "search": search(args.max_n),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
