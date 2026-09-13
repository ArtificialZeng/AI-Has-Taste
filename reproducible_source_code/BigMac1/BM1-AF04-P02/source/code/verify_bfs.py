#!/usr/bin/env python3
"""Standalone all-pairs BFS verifier for the serialized quotient edge list."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import deque
from pathlib import Path


def fail(message):
    print(f"REJECTED: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path):
    try:
        with open(path, encoding="utf-8") as stream:
            return json.load(stream)
    except Exception as exc:
        fail(f"cannot parse {path}: {exc}")


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def distances(adjacency, source):
    result = {source: 0}
    queue = deque([source])
    while queue:
        x = queue.popleft()
        for y in sorted(adjacency[x]):
            if y not in result:
                result[y] = result[x] + 1
                queue.append(y)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("edges", nargs="?", default="certificate/quotient_edges.json")
    parser.add_argument("result", nargs="?", default="certificate/result.json")
    args = parser.parse_args()
    edge_doc = read(args.edges)
    claimed = read(args.result)
    if set(edge_doc) != {"schema", "vertices", "edges"}:
        fail("edge document has unexpected keys")
    if edge_doc["schema"] != "sts15-pasch-edges-v1":
        fail("edge schema mismatch")
    vertices = edge_doc["vertices"]
    if vertices != [f"V{i:03d}" for i in range(80)]:
        fail("vertex universe/order mismatch")
    adjacency = {v: set() for v in vertices}
    normalized = []
    for edge in edge_doc["edges"]:
        if (
            not isinstance(edge, list)
            or len(edge) != 2
            or edge[0] not in adjacency
            or edge[1] not in adjacency
            or not edge[0] < edge[1]
        ):
            fail("malformed edge")
        normalized.append(tuple(edge))
        adjacency[edge[0]].add(edge[1])
        adjacency[edge[1]].add(edge[0])
    if normalized != sorted(set(normalized)):
        fail("edges are not sorted and distinct")

    unseen = set(vertices)
    components = []
    while unseen:
        root = min(unseen)
        component = set(distances(adjacency, root))
        components.append(sorted(component))
        unseen -= component
    components.sort(key=lambda c: (-len(c), c))
    if [len(c) for c in components] != [79, 1]:
        fail("component sizes are not 79+1")

    main_component = components[0]
    rows = {source: distances(adjacency, source) for source in main_component}
    if any(set(row) != set(main_component) for row in rows.values()):
        fail("a BFS row does not cover the main component")
    diameter = max(max(row.values()) for row in rows.values())
    diameter_pairs = [
        [x, y]
        for i, x in enumerate(main_component)
        for y in main_component[i + 1 :]
        if rows[x][y] == diameter
    ]
    eccentricities = {
        vertex: (0 if vertex == components[1][0] else max(rows[vertex].values()))
        for vertex in vertices
    }
    radius = min(eccentricities[v] for v in main_component)
    if claimed.get("vertex_count") != 80:
        fail("claimed vertex count mismatch")
    if claimed.get("edge_count") != len(normalized):
        fail("claimed edge count mismatch")
    if claimed.get("components") != components:
        fail("claimed components mismatch")
    if claimed.get("component_sizes") != [79, 1]:
        fail("claimed component sizes mismatch")
    if claimed.get("diameter") != diameter:
        fail("claimed diameter mismatch")
    if claimed.get("component_diameters") != [diameter, 0]:
        fail("claimed component diameters mismatch")
    if claimed.get("all_diameter_pairs") != diameter_pairs:
        fail("claimed diameter pairs mismatch")
    if claimed.get("eccentricities") != eccentricities:
        fail("claimed eccentricities mismatch")
    if claimed.get("radius") != radius:
        fail("claimed radius mismatch")

    u, v = claimed["diameter_pair"]
    if [u, v] not in diameter_pairs:
        fail("chosen diameter pair is not extremal")
    endpoint_row = [rows[u].get(vertex) for vertex in vertices]
    if claimed.get("distance_row_from_first_endpoint") != endpoint_row:
        fail("claimed endpoint distance row mismatch")
    path = claimed.get("geodesic")
    if (
        not isinstance(path, list)
        or path[0] != u
        or path[-1] != v
        or len(path) - 1 != diameter
        or any(path[i + 1] not in adjacency[path[i]] for i in range(len(path) - 1))
    ):
        fail("claimed geodesic is not a length-diameter path")

    record = {
        "status": "VERIFIED",
        "vertex_count": 80,
        "edge_count": len(normalized),
        "component_sizes": [79, 1],
        "diameter": diameter,
        "diameter_pairs": diameter_pairs,
        "edge_input_sha256": sha256(args.edges),
        "result_input_sha256": sha256(args.result),
        "verifier_sha256": sha256(__file__),
    }
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
