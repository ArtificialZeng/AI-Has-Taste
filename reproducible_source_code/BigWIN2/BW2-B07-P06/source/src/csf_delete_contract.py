#!/usr/bin/env python3
"""Independent exact weighted deletion-contraction CSF evaluator."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from functools import lru_cache

from graph6_utils import parse_graph6


State = tuple[tuple[int, ...], tuple[tuple[int, int], ...]]


def normalize(weights: tuple[int, ...], edges: tuple[tuple[int, int], ...]) -> State:
    # Deterministic relabel by current vertex order; parallel edges are
    # irrelevant to proper coloring and are collapsed.
    simple = tuple(sorted({(min(u, v), max(u, v)) for u, v in edges if u != v}))
    return weights, simple


def contract(state: State, edge: tuple[int, int]) -> State:
    weights, edges = state
    u, v = edge
    if u > v:
        u, v = v, u
    new_weights = list(weights)
    new_weights[u] += new_weights[v]
    del new_weights[v]

    def mapped(x: int) -> int:
        if x == v:
            return u
        return x - 1 if x > v else x

    new_edges = []
    for a, b in edges:
        if (a, b) == edge:
            continue
        aa, bb = mapped(a), mapped(b)
        if aa != bb:
            new_edges.append((min(aa, bb), max(aa, bb)))
    return normalize(tuple(new_weights), tuple(new_edges))


@lru_cache(maxsize=None)
def evaluate(state: State) -> tuple[tuple[tuple[int, ...], int], ...]:
    weights, edges = state
    if not edges:
        return ((tuple(sorted(weights, reverse=True)), 1),)
    edge = edges[-1]
    deleted = normalize(weights, edges[:-1])
    contracted = contract(state, edge)
    result: dict[tuple[int, ...], int] = defaultdict(int)
    for part, value in evaluate(deleted):
        result[part] += value
    for part, value in evaluate(contracted):
        result[part] -= value
    return tuple(sorted((part, value) for part, value in result.items() if value))


def csf_power_sum(line: bytes) -> dict[tuple[int, ...], int]:
    n, _adj, edges = parse_graph6(line)
    state = normalize((1,) * n, tuple(edges))
    return dict(evaluate(state))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("graph6")
    args = parser.parse_args()
    coefficients = csf_power_sum(args.graph6.encode("ascii"))
    print(json.dumps({"graph6": args.graph6, "power_sum": [[list(k), v] for k, v in coefficients.items()]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
