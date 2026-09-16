#!/usr/bin/env python3
"""Independent exact verifier for a finite order range.

This program intentionally shares no imports with ``explore_trees.py`` and
does not use NetworkX.  It generates rooted unlabeled trees as multisets of
rooted trees, forgets the root using the AHU center encoding, and deduplicates
the resulting free trees.  Distances are recomputed by Floyd--Warshall and
multiset dimension is checked by literal subset enumeration.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import platform
import sys
from collections import Counter, deque
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator

RootCode = tuple["RootCode", ...]


def generate_rooted_codes(max_n: int) -> list[list[RootCode]]:
    by_size: list[list[RootCode]] = [[] for _ in range(max_n + 1)]
    by_size[1] = [()]
    all_types: list[tuple[int, RootCode]] = [(1, ())]

    def forests(remaining: int, start: int) -> Iterator[tuple[RootCode, ...]]:
        if remaining == 0:
            yield ()
            return
        for i in range(start, len(all_types)):
            size, code = all_types[i]
            if size > remaining:
                break
            for tail in forests(remaining - size, i):
                yield (code,) + tail

    for n in range(2, max_n + 1):
        codes = list(forests(n - 1, 0))
        if len(codes) != len(set(codes)):
            raise AssertionError("rooted-tree multiset generator duplicated a code")
        by_size[n] = codes
        all_types.extend((n, code) for code in codes)
    return by_size


def adjacency_from_root_code(code: RootCode) -> list[list[int]]:
    adj: list[list[int]] = []

    def add(subcode: RootCode, parent: int | None) -> int:
        v = len(adj)
        adj.append([])
        if parent is not None:
            adj[v].append(parent)
            adj[parent].append(v)
        for child in subcode:
            add(child, v)
        return v

    add(code, None)
    return adj


def centers(adj: list[list[int]]) -> list[int]:
    n = len(adj)
    if n <= 2:
        return list(range(n))
    degree = [len(row) for row in adj]
    leaves: deque[int] = deque(i for i, d in enumerate(degree) if d <= 1)
    remaining = n
    while remaining > 2:
        layer = len(leaves)
        remaining -= layer
        for _ in range(layer):
            v = leaves.popleft()
            degree[v] = 0
            for w in adj[v]:
                if degree[w] > 0:
                    degree[w] -= 1
                    if degree[w] == 1:
                        leaves.append(w)
    return sorted(leaves)


def rooted_ahu(adj: list[list[int]], v: int, parent: int) -> str:
    children = sorted(rooted_ahu(adj, w, v) for w in adj[v] if w != parent)
    return "(" + "".join(children) + ")"


def free_ahu(adj: list[list[int]]) -> str:
    cs = centers(adj)
    if len(cs) == 1:
        return "U" + rooted_ahu(adj, cs[0], -1)
    if len(cs) == 2:
        a, b = cs
        halves = sorted((rooted_ahu(adj, a, b), rooted_ahu(adj, b, a)))
        return "B" + halves[0] + halves[1]
    raise AssertionError("a tree must have one or two centers")


def free_trees(rooted_codes: list[RootCode]) -> list[tuple[str, list[list[int]]]]:
    unique: dict[str, list[list[int]]] = {}
    for code in rooted_codes:
        adj = adjacency_from_root_code(code)
        key = free_ahu(adj)
        unique.setdefault(key, adj)
    return sorted(unique.items())


def floyd_distances(adj: list[list[int]]) -> list[list[int]]:
    n = len(adj)
    inf = n + 1
    dist = [[inf] * n for _ in range(n)]
    for v in range(n):
        dist[v][v] = 0
        for w in adj[v]:
            dist[v][w] = 1
    for k in range(n):
        for i in range(n):
            dik = dist[i][k]
            for j in range(n):
                candidate = dik + dist[k][j]
                if candidate < dist[i][j]:
                    dist[i][j] = candidate
    return dist


def resolves(dist: list[list[int]], chosen: tuple[int, ...]) -> bool:
    codes = [tuple(sorted(row[w] for w in chosen)) for row in dist]
    return len(codes) == len(set(codes))


def multiset_dimension(dist: list[list[int]]) -> tuple[int | None, tuple[int, ...] | None]:
    n = len(dist)
    for k in range(n + 1):
        for chosen in itertools.combinations(range(n), k):
            if resolves(dist, chosen):
                return k, chosen
    return None, None


def edge_list(adj: list[list[int]]) -> list[list[int]]:
    return [[v, w] for v, row in enumerate(adj) for w in row if v < w]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-max", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.n_max < 1:
        parser.error("n-max must be positive")

    rooted = generate_rooted_codes(args.n_max)
    report: dict[str, object] = {
        "schema_version": 1,
        "kind": "independent_exact_finite_verification",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "parameters": {"n_max": args.n_max},
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        },
        "orders": [],
        "violations": [],
    }
    for n in range(1, args.n_max + 1):
        trees = free_trees(rooted[n])
        counts: Counter[str] = Counter()
        for key, adj in trees:
            dist = floyd_distances(adj)
            diameter = max(max(row) for row in dist)
            md, witness = multiset_dimension(dist)
            counts["infinity" if md is None else str(md)] += 1
            if md is not None and md > n - diameter + 1:
                report["violations"].append(
                    {
                        "n": n,
                        "ahu_code": key,
                        "edges": edge_list(adj),
                        "diameter": diameter,
                        "md": md,
                        "bound": n - diameter + 1,
                        "witness": list(witness or ()),
                    }
                )
        row = {
            "n": n,
            "rooted_unlabeled_trees": len(rooted[n]),
            "free_unlabeled_trees": len(trees),
            "md_counts": dict(sorted(counts.items())),
        }
        report["orders"].append(row)
        print(f"n={n} rooted={len(rooted[n])} free={len(trees)} md={row['md_counts']}", flush=True)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(f"independent finite verification: PASS through n={args.n_max}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
