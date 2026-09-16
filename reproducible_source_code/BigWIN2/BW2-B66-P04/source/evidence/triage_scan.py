#!/usr/bin/env python3
"""Cheap exact scan for the order-12 two-attachment triage.

Usage: python evidence/triage_scan.py /path/to/12_3_3.asc
The input hash and every parsed graph are validated before the scan.
"""

from __future__ import annotations

import hashlib
import re
import sys
from collections import deque
from pathlib import Path


EXPECTED_SHA256 = "f32e0b0a0dcaeee8b67fcd1896a261330abecd22bab3a4144463f9011732cac7"


def parse_census(path: Path) -> list[dict[int, set[int]]]:
    raw = path.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        raise ValueError(f"unexpected census SHA-256: {digest}")
    blocks = re.split(rb"(?=Graph [0-9]+:\r?\n)", raw)
    graphs: list[dict[int, set[int]]] = []
    row = re.compile(rb"^([0-9]+)\s*:\s*([0-9 ]+)\s*$")
    for block in blocks:
        if not block.startswith(b"Graph "):
            continue
        adj: dict[int, set[int]] = {}
        for line in block.splitlines()[1:]:
            match = row.match(line)
            if match and len(adj) < 12:
                vertex = int(match.group(1))
                adj[vertex] = {int(x) for x in match.group(2).split()}
            if len(adj) == 12:
                break
        validate_graph(adj)
        graphs.append(adj)
    return graphs


def validate_graph(adj: dict[int, set[int]]) -> None:
    if set(adj) != set(range(1, 13)):
        raise ValueError("graph does not have vertex set {1,...,12}")
    if any(len(adj[v]) != 3 or v in adj[v] for v in adj):
        raise ValueError("graph is not simple cubic")
    if any(v not in adj[u] for v in adj for u in adj[v]):
        raise ValueError("adjacency relation is not symmetric")
    if reachable(adj, 1, None) != set(adj):
        raise ValueError("graph is disconnected")


def reachable(
    adj: dict[int, set[int]], start: int, deleted: frozenset[int] | None
) -> set[int]:
    seen = {start}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if deleted == frozenset((v, w)) or w in seen:
                continue
            seen.add(w)
            queue.append(w)
    return seen


def distance_without_edge(
    adj: dict[int, set[int]], source: int, target: int
) -> int | None:
    deleted = frozenset((source, target))
    distance = {source: 0}
    queue = deque([source])
    while queue:
        v = queue.popleft()
        for w in adj[v]:
            if frozenset((v, w)) == deleted or w in distance:
                continue
            distance[w] = distance[v] + 1
            if w == target:
                return distance[w]
            queue.append(w)
    return None


def canonical_cycle(path: tuple[int, ...]) -> tuple[int, ...]:
    # The DFS starts at the unique least vertex of the cycle.
    return min(path, (path[0],) + tuple(reversed(path[1:])))


def cycles_of_length(adj: dict[int, set[int]], length: int) -> set[tuple[int, ...]]:
    found: set[tuple[int, ...]] = set()
    for start in sorted(adj):
        def visit(path: tuple[int, ...]) -> None:
            if len(path) == length:
                if start in adj[path[-1]]:
                    found.add(canonical_cycle(path))
                return
            for nxt in sorted(adj[path[-1]]):
                if nxt > start and nxt not in path:
                    visit(path + (nxt,))
        visit((start,))
    return found


def cycle_edges(cycle: tuple[int, ...]) -> set[frozenset[int]]:
    return {
        frozenset((cycle[i], cycle[(i + 1) % len(cycle)]))
        for i in range(len(cycle))
    }


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("usage: triage_scan.py /path/to/12_3_3.asc")
    graphs = parse_census(Path(sys.argv[1]))
    edge_pairs = connected_deletions = eligible = bad = 0
    for adj in graphs:
        cycles = cycles_of_length(adj, 4) | cycles_of_length(adj, 8)
        indexed_cycles = [(cycle, cycle_edges(cycle)) for cycle in cycles]
        edges = sorted((v, w) for v in adj for w in adj[v] if v < w)
        if len(edges) != 18:
            raise ValueError("cubic graph does not have 18 edges")
        for source, target in edges:
            edge_pairs += 1
            distance = distance_without_edge(adj, source, target)
            if distance is None:
                continue
            connected_deletions += 1
            if distance < 3:
                continue
            eligible += 1
            deleted = frozenset((source, target))
            if not any(deleted not in edgeset for _, edgeset in indexed_cycles):
                bad += 1
    print(f"census_graphs={len(graphs)}")
    print(f"graph_edge_pairs={edge_pairs}")
    print(f"connected_deletions={connected_deletions}")
    print(f"eligible_distance_ge_3={eligible}")
    print(f"eligible_without_C4_or_C8={bad}")


if __name__ == "__main__":
    main()
