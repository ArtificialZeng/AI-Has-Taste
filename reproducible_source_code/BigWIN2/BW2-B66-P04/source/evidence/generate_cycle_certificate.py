#!/usr/bin/env python3
"""Generate the deterministic C4/C8 certificate for the frozen cubic census.

Usage:
  python3 evidence/generate_cycle_certificate.py CENSUS OUTPUT.json

For every eligible (census graph, deleted edge), the output contains the
lexicographically least normalized 4- or 8-cycle.  A normalized cycle starts
at its least vertex and uses the lexicographically smaller orientation.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import deque
from pathlib import Path


CENSUS_SHA256 = "f32e0b0a0dcaeee8b67fcd1896a261330abecd22bab3a4144463f9011732cac7"
SOURCE_SHA256 = "e0696f682554b3b51d04c3ce8601d9778a1a30a06b2cb7de02681361f21db681"
JOB_ID = "win-00066-p04-research-65f53c129997"
VERTICES = set(range(1, 13))


def parse_census(path: Path) -> list[tuple[int, dict[int, set[int]]]]:
    raw = path.read_bytes()
    got = hashlib.sha256(raw).hexdigest()
    if got != CENSUS_SHA256:
        raise ValueError(f"census SHA-256 {got}, expected {CENSUS_SHA256}")
    header = re.compile(rb"^Graph ([0-9]+):\s*$")
    row = re.compile(rb"^([0-9]+)\s*:\s*([0-9 ]+)\s*$")
    graphs: list[tuple[int, dict[int, set[int]]]] = []
    graph_id: int | None = None
    adjacency: dict[int, set[int]] = {}
    for line in raw.splitlines():
        match = header.match(line)
        if match:
            if graph_id is not None:
                validate_graph(graph_id, adjacency)
                graphs.append((graph_id, adjacency))
            graph_id = int(match.group(1))
            adjacency = {}
            continue
        match = row.match(line)
        if graph_id is not None and match and len(adjacency) < 12:
            vertex = int(match.group(1))
            adjacency[vertex] = {int(x) for x in match.group(2).split()}
    if graph_id is not None:
        validate_graph(graph_id, adjacency)
        graphs.append((graph_id, adjacency))
    if [number for number, _ in graphs] != list(range(1, 86)):
        raise ValueError("census graph identifiers are not exactly 1,...,85")
    return graphs


def validate_graph(graph_id: int, adjacency: dict[int, set[int]]) -> None:
    if set(adjacency) != VERTICES:
        raise ValueError(f"graph {graph_id}: vertex set is not 1,...,12")
    if any(len(adjacency[v]) != 3 or v in adjacency[v] for v in VERTICES):
        raise ValueError(f"graph {graph_id}: not loopless cubic")
    if any(v not in adjacency[u] for v in VERTICES for u in adjacency[v]):
        raise ValueError(f"graph {graph_id}: asymmetric adjacency")
    seen = {1}
    queue = deque([1])
    while queue:
        v = queue.popleft()
        for w in adjacency[v]:
            if w not in seen:
                seen.add(w)
                queue.append(w)
    if seen != VERTICES:
        raise ValueError(f"graph {graph_id}: disconnected")


def bfs_distance(
    adjacency: dict[int, set[int]], source: int, target: int | None,
    deleted: frozenset[int] | None,
) -> int | None:
    if target == source:
        return 0
    distance = {source: 0}
    queue = deque([source])
    while queue:
        v = queue.popleft()
        for w in adjacency[v]:
            if frozenset((v, w)) == deleted or w in distance:
                continue
            distance[w] = distance[v] + 1
            if w == target:
                return distance[w]
            queue.append(w)
    return None


def normalize_cycle(path: tuple[int, ...]) -> tuple[int, ...]:
    minimum = min(path)
    i = path.index(minimum)
    forward = path[i:] + path[:i]
    reverse_path = tuple(reversed(path))
    j = reverse_path.index(minimum)
    backward = reverse_path[j:] + reverse_path[:j]
    return min(forward, backward)


def least_cycle(
    adjacency: dict[int, set[int]], deleted: frozenset[int]
) -> tuple[int, ...] | None:
    cycles: set[tuple[int, ...]] = set()
    for wanted_length in (4, 8):
        for start in range(1, 13):
            def extend(path: tuple[int, ...]) -> None:
                if len(path) == wanted_length:
                    closing = frozenset((path[-1], start))
                    if start in adjacency[path[-1]] and closing != deleted:
                        cycles.add(normalize_cycle(path))
                    return
                for nxt in sorted(adjacency[path[-1]]):
                    if frozenset((path[-1], nxt)) != deleted and nxt not in path:
                        extend(path + (nxt,))
            extend((start,))
    return min(cycles) if cycles else None


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: generate_cycle_certificate.py CENSUS OUTPUT.json")
    graphs = parse_census(Path(sys.argv[1]))
    records: list[dict[str, object]] = []
    all_pairs = connected_deletions = 0
    for graph_id, adjacency in graphs:
        edges = sorted((v, w) for v in VERTICES for w in adjacency[v] if v < w)
        if len(edges) != 18:
            raise ValueError(f"graph {graph_id}: edge count is not 18")
        for source, target in edges:
            all_pairs += 1
            deleted = frozenset((source, target))
            distance = bfs_distance(adjacency, source, target, deleted)
            if distance is None:
                continue
            connected_deletions += 1
            if distance < 3:
                continue
            cycle = least_cycle(adjacency, deleted)
            if cycle is None:
                raise ValueError(f"no C4/C8 for graph {graph_id}, edge {source}-{target}")
            records.append({
                "graph": graph_id,
                "deleted_edge": [source, target],
                "distance": distance,
                "cycle": list(cycle),
            })
    document = {
        "format": "win-00066-p04-cycle-certificate-v1",
        "proposer_job_id": JOB_ID,
        "source_sha256": SOURCE_SHA256,
        "census_sha256": CENSUS_SHA256,
        "normalization": (
            "start at the least cycle vertex; choose the lexicographically "
            "smaller orientation; compare the resulting vertex tuples"
        ),
        "counts": {
            "census_graphs": len(graphs),
            "graph_edge_pairs": all_pairs,
            "connected_deletions": connected_deletions,
            "eligible_pairs": len(records),
        },
        "records": records,
    }
    Path(sys.argv[2]).write_text(
        json.dumps(document, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(document["counts"], sort_keys=True))


if __name__ == "__main__":
    main()
