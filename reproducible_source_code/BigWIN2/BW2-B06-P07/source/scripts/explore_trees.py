#!/usr/bin/env python3
"""Exact discovery enumerator for the tree multiset-dimension conjecture.

This is discovery code, not by itself a certificate.  It enumerates NetworkX's
nonisomorphic trees, computes every distance by BFS, and tests vertex subsets
in increasing cardinality.  Two different exact representations are used to
cross-check every reported resolving witness.
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

import networkx as nx


def adjacency(g: nx.Graph) -> list[list[int]]:
    nodes = sorted(g.nodes())
    relabel = {v: i for i, v in enumerate(nodes)}
    return [sorted(relabel[w] for w in g.neighbors(v)) for v in nodes]


def bfs_distances(adj: list[list[int]], source: int) -> list[int]:
    n = len(adj)
    dist = [-1] * n
    dist[source] = 0
    q: deque[int] = deque([source])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if dist[w] == -1:
                dist[w] = dist[v] + 1
                q.append(w)
    if any(x < 0 for x in dist):
        raise ValueError("input is disconnected")
    return dist


def distance_matrix(adj: list[list[int]]) -> list[list[int]]:
    return [bfs_distances(adj, v) for v in range(len(adj))]


def is_resolving_sorted(dist: list[list[int]], chosen: tuple[int, ...]) -> bool:
    """Definition-level evaluator: literally sort distances to W."""
    seen: set[tuple[int, ...]] = set()
    for row in dist:
        code = tuple(sorted(row[w] for w in chosen))
        if code in seen:
            return False
        seen.add(code)
    return True


def shell_masks(dist: list[list[int]]) -> list[list[int]]:
    diameter = max(max(row) for row in dist)
    masks: list[list[int]] = []
    for row in dist:
        spheres = [0] * (diameter + 1)
        for w, d in enumerate(row):
            spheres[d] |= 1 << w
        masks.append(spheres)
    return masks


def is_resolving_shells(masks: list[list[int]], chosen_mask: int) -> bool:
    """Independent evaluator: count W in every exact-distance sphere."""
    seen: set[tuple[int, ...]] = set()
    for spheres in masks:
        code = tuple((chosen_mask & sphere).bit_count() for sphere in spheres)
        if code in seen:
            return False
        seen.add(code)
    return True


def exact_md(dist: list[list[int]]) -> tuple[int | None, tuple[int, ...] | None, int]:
    n = len(dist)
    masks = shell_masks(dist)
    tested = 0
    for k in range(0, n + 1):
        for chosen in itertools.combinations(range(n), k):
            tested += 1
            chosen_mask = sum(1 << v for v in chosen)
            if is_resolving_shells(masks, chosen_mask):
                if not is_resolving_sorted(dist, chosen):
                    raise AssertionError("independent evaluators disagree")
                return k, chosen, tested
    return None, None, tested


def tree_edges(adj: list[list[int]]) -> list[list[int]]:
    return [[v, w] for v, nbrs in enumerate(adj) for w in nbrs if v < w]


def unique_path(adj: list[list[int]], source: int, target: int) -> list[int]:
    parent = [-1] * len(adj)
    parent[source] = source
    q: deque[int] = deque([source])
    while q and parent[target] < 0:
        v = q.popleft()
        for w in adj[v]:
            if parent[w] < 0:
                parent[w] = v
                q.append(w)
    out = [target]
    while out[-1] != source:
        out.append(parent[out[-1]])
    out.reverse()
    return out


def p01_candidate_exists(adj: list[list[int]], dist: list[list[int]]) -> bool:
    """Test all diametral paths: all off-path vertices plus at most two on-path."""
    n = len(adj)
    diameter = max(max(row) for row in dist)
    for a in range(n):
        for b in range(a + 1, n):
            if dist[a][b] != diameter:
                continue
            path = unique_path(adj, a, b)
            on_path = set(path)
            off_path = tuple(v for v in range(n) if v not in on_path)
            for k in range(0, min(2, len(path)) + 1):
                for extra in itertools.combinations(path, k):
                    chosen = tuple(sorted(off_path + extra))
                    if is_resolving_sorted(dist, chosen):
                        return True
    return False


def canonical_text(edges: list[list[int]]) -> str:
    return ";".join(f"{u}-{v}" for u, v in edges)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-min", type=int, default=1)
    parser.add_argument("--n-max", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--retain-p01-failures", type=int, default=20)
    args = parser.parse_args()
    if args.n_min < 1 or args.n_max < args.n_min:
        parser.error("require 1 <= n-min <= n-max")

    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report: dict[str, object] = {
        "schema_version": 1,
        "kind": "exact_discovery_enumeration",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "parameters": {"n_min": args.n_min, "n_max": args.n_max},
        "environment": {
            "python": sys.version,
            "platform": platform.platform(),
            "networkx": nx.__version__,
            "script_sha256": source_hash,
        },
        "orders": [],
        "violations": [],
        "p01_failures": [],
    }

    for n in range(args.n_min, args.n_max + 1):
        if n == 1:
            graphs = [nx.empty_graph(1)]
        else:
            graphs = nx.nonisomorphic_trees(n)
        count = 0
        md_counts: Counter[str] = Counter()
        diameter_counts: Counter[str] = Counter()
        tested_subsets = 0
        finite_count = 0
        p01_failure_count = 0
        for index, g in enumerate(graphs):
            count += 1
            adj = adjacency(g)
            dist = distance_matrix(adj)
            diameter = max(max(row) for row in dist)
            md, witness, tested = exact_md(dist)
            tested_subsets += tested
            md_key = "infinity" if md is None else str(md)
            md_counts[md_key] += 1
            diameter_counts[str(diameter)] += 1
            edges = tree_edges(adj)
            if md is not None:
                finite_count += 1
                bound = n - diameter + 1
                if md > bound:
                    report["violations"].append(
                        {
                            "n": n,
                            "index": index,
                            "edges": edges,
                            "diameter": diameter,
                            "md": md,
                            "bound": bound,
                            "witness": list(witness or ()),
                            "edge_text_sha256": hashlib.sha256(
                                canonical_text(edges).encode()
                            ).hexdigest(),
                        }
                    )
                if not p01_candidate_exists(adj, dist):
                    p01_failure_count += 1
                    if len(report["p01_failures"]) < args.retain_p01_failures:
                        report["p01_failures"].append(
                            {
                                "n": n,
                                "index": index,
                                "edges": edges,
                                "diameter": diameter,
                                "md": md,
                                "bound": n - diameter + 1,
                            }
                        )
        report["orders"].append(
            {
                "n": n,
                "nonisomorphic_trees": count,
                "finite_md": finite_count,
                "md_counts": dict(sorted(md_counts.items())),
                "diameter_counts": dict(sorted(diameter_counts.items(), key=lambda x: int(x[0]))),
                "tested_subsets_until_first_witness_or_exhaustion": tested_subsets,
                "p01_failure_count_among_finite_md": p01_failure_count,
            }
        )
        print(
            f"n={n} trees={count} md={dict(sorted(md_counts.items()))} "
            f"violations={len(report['violations'])} p01_failures={p01_failure_count}",
            flush=True,
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
