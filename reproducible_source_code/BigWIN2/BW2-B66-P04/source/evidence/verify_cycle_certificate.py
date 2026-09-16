#!/usr/bin/env python3
"""Independent replay verifier for the win-00066-p04 certificate.

This verifier does not import or call the generator.  In particular, it finds
cycles by choosing edge subsets and checking the 2-regular connected condition,
rather than by the generator's vertex-path DFS.

Usage: python3 evidence/verify_cycle_certificate.py CENSUS CERTIFICATE.json
"""

from __future__ import annotations

import hashlib
import itertools
import json
import re
import sys
from collections import deque
from pathlib import Path


EXPECTED_CENSUS_HASH = "f32e0b0a0dcaeee8b67fcd1896a261330abecd22bab3a4144463f9011732cac7"
EXPECTED_SOURCE_HASH = "e0696f682554b3b51d04c3ce8601d9778a1a30a06b2cb7de02681361f21db681"
EXPECTED_FORMAT = "win-00066-p04-cycle-certificate-v1"


def load_graphs(filename: str) -> list[dict[int, set[int]]]:
    data = Path(filename).read_bytes()
    if hashlib.sha256(data).hexdigest() != EXPECTED_CENSUS_HASH:
        raise ValueError("frozen census hash mismatch")
    starts = list(re.finditer(rb"(?m)^Graph ([0-9]+):\r?$", data))
    if [int(x.group(1)) for x in starts] != list(range(1, 86)):
        raise ValueError("expected exactly the numbered graphs 1 through 85")
    graphs: list[dict[int, set[int]]] = []
    line_pattern = re.compile(rb"(?m)^([1-9]|1[0-2])\s*:\s*([0-9 ]+)\s*$")
    for index, start in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(data)
        block = data[start.end():end]
        rows = line_pattern.findall(block)
        if len(rows) < 12:
            raise ValueError(f"graph {index + 1}: fewer than 12 adjacency rows")
        adjacency = {
            int(v): {int(w) for w in neighbors.split()} for v, neighbors in rows[:12]
        }
        expected_vertices = set(range(1, 13))
        if set(adjacency) != expected_vertices:
            raise ValueError(f"graph {index + 1}: wrong vertex set")
        edge_count = 0
        for v in expected_vertices:
            if v in adjacency[v] or len(adjacency[v]) != 3:
                raise ValueError(f"graph {index + 1}: loop or noncubic vertex")
            for w in adjacency[v]:
                if w not in expected_vertices or v not in adjacency[w]:
                    raise ValueError(f"graph {index + 1}: invalid adjacency")
                if v < w:
                    edge_count += 1
        if edge_count != 18:
            raise ValueError(f"graph {index + 1}: wrong edge count")
        if component(adjacency, 1, None) != expected_vertices:
            raise ValueError(f"graph {index + 1}: disconnected")
        graphs.append(adjacency)
    return graphs


def component(
    graph: dict[int, set[int]], start: int, omitted: tuple[int, int] | None
) -> set[int]:
    reached = {start}
    pending = [start]
    while pending:
        v = pending.pop()
        for w in graph[v]:
            if omitted is not None and {v, w} == set(omitted):
                continue
            if w not in reached:
                reached.add(w)
                pending.append(w)
    return reached


def separation(
    graph: dict[int, set[int]], source: int, target: int
) -> int | None:
    distances = {source: 0}
    queue = deque([source])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if {v, w} == {source, target} or w in distances:
                continue
            distances[w] = distances[v] + 1
            if w == target:
                return distances[w]
            queue.append(w)
    return None


def cycle_from_edge_set(chosen: tuple[tuple[int, int], ...]) -> tuple[int, ...] | None:
    local: dict[int, list[int]] = {}
    for v, w in chosen:
        local.setdefault(v, []).append(w)
        local.setdefault(w, []).append(v)
    if len(local) != len(chosen) or any(len(neighbors) != 2 for neighbors in local.values()):
        return None
    first = min(local)
    options: list[tuple[int, ...]] = []
    for second in local[first]:
        path = [first, second]
        previous, current = first, second
        while len(path) < len(chosen):
            following = local[current][0] if local[current][0] != previous else local[current][1]
            if following in path:
                return None
            path.append(following)
            previous, current = current, following
        if first not in local[current]:
            return None
        options.append(tuple(path))
    return min(options)


def independently_least_cycle(
    graph: dict[int, set[int]], removed: tuple[int, int]
) -> tuple[int, ...] | None:
    available = [
        (v, w) for v in range(1, 13) for w in graph[v]
        if v < w and {v, w} != set(removed)
    ]
    candidates: list[tuple[int, ...]] = []
    for length in (4, 8):
        for edge_subset in itertools.combinations(available, length):
            cycle = cycle_from_edge_set(edge_subset)
            if cycle is not None:
                candidates.append(cycle)
    return min(candidates) if candidates else None


def verify_record_cycle(
    graph: dict[int, set[int]], removed: tuple[int, int], listed: tuple[int, ...]
) -> None:
    if len(listed) not in (4, 8) or len(set(listed)) != len(listed):
        raise ValueError("listed cycle is not simple of length 4 or 8")
    for i, v in enumerate(listed):
        w = listed[(i + 1) % len(listed)]
        if w not in graph.get(v, set()) or {v, w} == set(removed):
            raise ValueError("listed cycle uses a nonedge or deleted edge")
    reverse = (listed[0],) + tuple(reversed(listed[1:]))
    if listed[0] != min(listed) or listed != min(listed, reverse):
        raise ValueError("listed cycle is not normalized")


def main() -> None:
    if len(sys.argv) != 3:
        raise SystemExit("usage: verify_cycle_certificate.py CENSUS CERTIFICATE.json")
    graphs = load_graphs(sys.argv[1])
    certificate_bytes = Path(sys.argv[2]).read_bytes()
    certificate = json.loads(certificate_bytes)
    if certificate.get("format") != EXPECTED_FORMAT:
        raise ValueError("certificate format mismatch")
    if certificate.get("census_sha256") != EXPECTED_CENSUS_HASH:
        raise ValueError("certificate names the wrong census")
    if certificate.get("source_sha256") != EXPECTED_SOURCE_HASH:
        raise ValueError("certificate names the wrong frozen source")

    expected: dict[tuple[int, int, int], int] = {}
    edge_pairs = connected_count = 0
    for graph_number, graph in enumerate(graphs, start=1):
        for v in range(1, 13):
            for w in sorted(graph[v]):
                if v >= w:
                    continue
                edge_pairs += 1
                distance = separation(graph, v, w)
                if distance is None:
                    continue
                connected_count += 1
                if distance >= 3:
                    expected[(graph_number, v, w)] = distance

    records = certificate.get("records")
    if not isinstance(records, list):
        raise ValueError("records is not a list")
    observed: dict[tuple[int, int, int], tuple[int, ...]] = {}
    for position, record in enumerate(records):
        try:
            graph_number = record["graph"]
            source, target = record["deleted_edge"]
            stated_distance = record["distance"]
            cycle = tuple(record["cycle"])
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(f"malformed record {position}") from error
        key = (graph_number, source, target)
        if key in observed:
            raise ValueError(f"duplicate record for {key}")
        if key not in expected:
            raise ValueError(f"ineligible or unknown pair {key}")
        if stated_distance != expected[key]:
            raise ValueError(f"wrong distance for {key}")
        graph = graphs[graph_number - 1]
        verify_record_cycle(graph, (source, target), cycle)
        independently_found = independently_least_cycle(graph, (source, target))
        if cycle != independently_found:
            raise ValueError(
                f"record {key} is not lexicographically least: "
                f"listed {cycle}, independently found {independently_found}"
            )
        observed[key] = cycle
    if set(observed) != set(expected):
        missing = sorted(set(expected) - set(observed))
        extra = sorted(set(observed) - set(expected))
        raise ValueError(f"pair coverage mismatch; missing={missing}, extra={extra}")

    correct_counts = {
        "census_graphs": 85,
        "graph_edge_pairs": edge_pairs,
        "connected_deletions": connected_count,
        "eligible_pairs": len(expected),
    }
    if certificate.get("counts") != correct_counts:
        raise ValueError(
            f"certificate counts {certificate.get('counts')} != {correct_counts}"
        )
    print("VERIFIED")
    print(f"census_sha256={EXPECTED_CENSUS_HASH}")
    print(f"certificate_sha256={hashlib.sha256(certificate_bytes).hexdigest()}")
    for name, count in correct_counts.items():
        print(f"{name}={count}")
    print("all_cycles_valid_and_lexicographically_least=true")


if __name__ == "__main__":
    main()
