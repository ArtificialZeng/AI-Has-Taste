#!/usr/bin/env python3
"""Exact power-sum CSF by direct spanning-edge-subset enumeration."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict

from graph6_utils import parse_graph6


def csf_power_sum(line: bytes) -> dict[tuple[int, ...], int]:
    n, _adj, edges = parse_graph6(line)
    coefficients: dict[tuple[int, ...], int] = defaultdict(int)
    for mask in range(1 << len(edges)):
        parent = list(range(n))
        size = [1] * n

        def find(v: int) -> int:
            while parent[v] != v:
                parent[v] = parent[parent[v]]
                v = parent[v]
            return v

        for edge_index, (u, v) in enumerate(edges):
            if (mask >> edge_index) & 1:
                ru, rv = find(u), find(v)
                if ru != rv:
                    if size[ru] < size[rv]:
                        ru, rv = rv, ru
                    parent[rv] = ru
                    size[ru] += size[rv]
        partition = tuple(sorted((size[v] for v in range(n) if find(v) == v), reverse=True))
        coefficients[partition] += -1 if mask.bit_count() & 1 else 1
    return {part: value for part, value in sorted(coefficients.items()) if value}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("graph6")
    args = parser.parse_args()
    coefficients = csf_power_sum(args.graph6.encode("ascii"))
    print(json.dumps({"graph6": args.graph6, "power_sum": [[list(k), v] for k, v in coefficients.items()]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
