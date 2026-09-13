#!/usr/bin/env python3
"""Deterministic complete census of the 14--16 cycles in a graph6 ZIP member.

Each undirected cycle is serialized once: its least vertex is first and the
smaller of the two neighbours of that vertex is second.  Adjacency lists are
sorted, so the output order is deterministic.  The output is an ordinary
UTF-8 TSV file with one cycle per line: length, followed by its vertices.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from collections import Counter, deque
from pathlib import Path


def decode_graph6(raw: bytes) -> list[list[int]]:
    text = raw.decode("ascii").strip()
    if text.startswith(">>graph6<<"):
        text = text[10:]
    data = [ord(c) - 63 for c in text]
    if not data or any(c < 0 or c > 63 for c in data):
        raise ValueError("invalid graph6 alphabet")
    if data[0] <= 62:
        n, pos = data[0], 1
    elif len(data) >= 4 and data[1] <= 62:
        n = (data[1] << 12) | (data[2] << 6) | data[3]
        pos = 4
    else:
        raise ValueError("unsupported graph6 order encoding")
    bits = []
    for value in data[pos:]:
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    need = n * (n - 1) // 2
    if len(bits) < need:
        raise ValueError("truncated graph6 record")
    adj = [[] for _ in range(n)]
    bit = 0
    for high in range(1, n):
        for low in range(high):
            if bits[bit]:
                adj[low].append(high)
                adj[high].append(low)
            bit += 1
    return adj


def graph_checks(adj: list[list[int]]) -> dict[str, object]:
    n = len(adj)
    edges = sum(map(len, adj)) // 2
    simple = all(v not in nbrs and len(nbrs) == len(set(nbrs)) for v, nbrs in enumerate(adj))
    seen = {0}
    todo = [0]
    while todo:
        u = todo.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return {
        "vertices": n,
        "edges": edges,
        "degree_set": sorted({len(nbrs) for nbrs in adj}),
        "simple": simple,
        "connected": len(seen) == n,
    }


def cycles_14_to_16(adj: list[list[int]]):
    """Yield every undirected simple cycle of length 14, 15, or 16 once.

    Completeness: every yielded path is rooted at its least vertex.  Conversely,
    every target cycle has a unique least vertex and two traversal directions;
    the final direction test retains exactly the one whose second vertex is
    smaller than its penultimate vertex.  The BFS distance test only removes a
    prefix that cannot return to the root within the remaining length budget.
    """
    n = len(adj)
    max_len = 16
    on_path = bytearray(n)
    for root in range(n):
        dist = [-1] * n
        dist[root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            if dist[u] == max_len:
                continue
            for v in adj[u]:
                if v >= root and dist[v] < 0:
                    dist[v] = dist[u] + 1
                    queue.append(v)

        path = [root]
        on_path[root] = 1

        def dfs(u: int) -> None:
            edges_used = len(path) - 1
            for v in adj[u]:
                if v == root:
                    cycle_len = edges_used + 1
                    if 14 <= cycle_len <= 16 and path[1] < path[-1]:
                        yield_value.append(tuple(path))
                    continue
                if v <= root or on_path[v] or edges_used + 1 >= max_len:
                    continue
                remaining = max_len - (edges_used + 1)
                if dist[v] < 0 or dist[v] > remaining:
                    continue
                on_path[v] = 1
                path.append(v)
                dfs(v)
                path.pop()
                on_path[v] = 0

        # A small buffer avoids making the recursive routine itself a generator.
        yield_value: list[tuple[int, ...]] = []
        dfs(root)
        on_path[root] = 0
        yield from yield_value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    parser.add_argument("member")
    parser.add_argument("output", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()

    archive_bytes = args.archive.read_bytes()
    with zipfile.ZipFile(args.archive) as zf:
        member_bytes = zf.read(args.member)
    adj = decode_graph6(member_bytes)
    checks = graph_checks(adj)
    if checks != {
        "vertices": 812,
        "edges": 1218,
        "degree_set": [3],
        "simple": True,
        "connected": True,
    }:
        raise RuntimeError(f"unexpected frozen graph: {checks}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    digest = hashlib.sha256()
    counts: Counter[int] = Counter()
    with args.output.open("wb") as stream:
        for cycle in cycles_14_to_16(adj):
            line = (str(len(cycle)) + "\t" + "\t".join(map(str, cycle)) + "\n").encode()
            stream.write(line)
            digest.update(line)
            counts[len(cycle)] += 1

    report = {
        "schema": "cycle-census-v1",
        "archive_sha256": hashlib.sha256(archive_bytes).hexdigest(),
        "member": args.member,
        "member_sha256": hashlib.sha256(member_bytes).hexdigest(),
        "graph": checks,
        "canonicalization": "least vertex first; second vertex less than final vertex",
        "lengths": [14, 15, 16],
        "counts": {str(k): counts[k] for k in (14, 15, 16)},
        "total": sum(counts.values()),
        "census_file": args.output.as_posix(),
        "census_sha256": digest.hexdigest(),
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
