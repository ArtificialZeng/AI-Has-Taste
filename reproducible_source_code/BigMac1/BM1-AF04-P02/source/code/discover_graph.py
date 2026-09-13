#!/usr/bin/env python3
"""Construct the STS(15) Pasch-switch quotient graph exactly.

Discovery uses nauty's labelg only for canonical isomorphism-class names.
The released verifier deliberately does not import this module and does not
invoke nauty.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import os
import platform
import subprocess
import sys
from collections import Counter, deque
from pathlib import Path

N = 15
LABELG = "/opt/homebrew/bin/labelg"


def normalize(blocks):
    return tuple(sorted(tuple(sorted(b)) for b in blocks))


def validate_sts(blocks):
    blocks = normalize(blocks)
    if len(blocks) != 35 or len(set(blocks)) != 35:
        raise ValueError("an STS(15) must have 35 distinct blocks")
    pairs = Counter()
    for b in blocks:
        if len(b) != 3 or len(set(b)) != 3 or min(b) < 0 or max(b) >= N:
            raise ValueError(f"invalid block {b}")
        for p in itertools.combinations(b, 2):
            pairs[p] += 1
    if len(pairs) != 105 or set(pairs.values()) != {1}:
        raise ValueError("pair coverage is not identically one")
    return blocks


def projective_seed():
    """The lines on the nonzero vectors of F_2^4, renamed 0,...,14."""
    blocks = set()
    for x in range(1, 16):
        for y in range(x + 1, 16):
            z = x ^ y
            if y < z:
                blocks.add(tuple(sorted((x - 1, y - 1, z - 1))))
    return validate_sts(blocks)


def bose_antipasch_seed():
    """Bose's STS(15) over Z_5 x Z_3; this instance is anti-Pasch."""
    point = lambda x, i: 3 * x + i
    blocks = set()
    for x in range(5):
        blocks.add(tuple(sorted((point(x, 0), point(x, 1), point(x, 2)))))
    inverse_two = 3  # 2*3 = 1 (mod 5)
    for x in range(5):
        for y in range(x + 1, 5):
            z = (x + y) * inverse_two % 5
            for i in range(3):
                blocks.add(
                    tuple(
                        sorted(
                            (point(x, i), point(y, i), point(z, (i + 1) % 3))
                        )
                    )
                )
    return validate_sts(blocks)


def graph6_encode(n, edges):
    if not (0 <= n <= 62):
        raise ValueError("this encoder handles graph6 orders at most 62")
    edge_set = {tuple(sorted(e)) for e in edges}
    bits = []
    for j in range(1, n):
        for i in range(j):
            bits.append(1 if (i, j) in edge_set else 0)
    while len(bits) % 6:
        bits.append(0)
    payload = []
    for start in range(0, len(bits), 6):
        value = sum(bits[start + k] << (5 - k) for k in range(6))
        payload.append(chr(value + 63))
    return chr(n + 63) + "".join(payload)


def graph6_decode(text):
    text = text.strip()
    if not text or text.startswith(">>"):
        raise ValueError("missing or unsupported graph6 record")
    n = ord(text[0]) - 63
    if not (0 <= n <= 62):
        raise ValueError("unsupported graph6 order")
    bits = []
    for char in text[1:]:
        value = ord(char) - 63
        if not (0 <= value <= 63):
            raise ValueError("invalid graph6 payload")
        bits.extend((value >> (5 - k)) & 1 for k in range(6))
    need = n * (n - 1) // 2
    if len(bits) < need:
        raise ValueError("truncated graph6 payload")
    edges = set()
    cursor = 0
    for j in range(1, n):
        for i in range(j):
            if bits[cursor]:
                edges.add((i, j))
            cursor += 1
    return n, edges


def incidence_graph6(blocks):
    blocks = validate_sts(blocks)
    edges = [(point, N + j) for j, block in enumerate(blocks) for point in block]
    return graph6_encode(50, edges)


def representative_from_canonical_graph6(record):
    n, edges = graph6_decode(record)
    if n != 50:
        raise ValueError("STS(15) incidence graph must have 50 vertices")
    adjacency = [set() for _ in range(n)]
    for x, y in edges:
        adjacency[x].add(y)
        adjacency[y].add(x)
    points = sorted(i for i, row in enumerate(adjacency) if len(row) == 7)
    block_vertices = sorted(i for i, row in enumerate(adjacency) if len(row) == 3)
    if len(points) != 15 or len(block_vertices) != 35:
        raise ValueError("canonical graph has the wrong incidence degree classes")
    rank = {point: i for i, point in enumerate(points)}
    blocks = []
    for vertex in block_vertices:
        if not adjacency[vertex] <= set(points):
            raise ValueError("canonical graph is not bipartite incidence data")
        blocks.append(tuple(sorted(rank[p] for p in adjacency[vertex])))
    return validate_sts(blocks)


def canonicalize_many(systems, labelg=LABELG):
    if not systems:
        return []
    records = [incidence_graph6(system) for system in systems]
    proc = subprocess.run(
        [labelg, "-q", "-g"],
        input="\n".join(records) + "\n",
        text=True,
        capture_output=True,
        check=True,
    )
    canonical = [line.strip() for line in proc.stdout.splitlines() if line.strip()]
    if len(canonical) != len(records):
        raise RuntimeError(
            f"labelg returned {len(canonical)} records for {len(records)} inputs"
        )
    return canonical


def pasch_configurations(blocks):
    """Discovery enumerator: inspect every four-block subset."""
    blocks = validate_sts(blocks)
    answer = []
    for indices in itertools.combinations(range(35), 4):
        chosen = tuple(blocks[i] for i in indices)
        support = set().union(*map(set, chosen))
        if len(support) != 6:
            continue
        if all(sum(point in block for block in chosen) == 2 for point in support):
            answer.append(chosen)
    return tuple(answer)


def pasch_mate(configuration):
    old = {tuple(block) for block in configuration}
    support = sorted(set().union(*map(set, old)))
    if len(old) != 4 or len(support) != 6:
        raise ValueError("malformed Pasch configuration")
    covered_pairs = {
        pair for block in old for pair in itertools.combinations(sorted(block), 2)
    }
    mate = {
        triple
        for triple in itertools.combinations(support, 3)
        if triple not in old
        and all(pair in covered_pairs for pair in itertools.combinations(triple, 2))
    }
    if len(mate) != 4:
        raise ValueError("Pasch mate is not a four-block trade")
    mate_pairs = {
        pair for block in mate for pair in itertools.combinations(block, 2)
    }
    if mate_pairs != covered_pairs:
        raise ValueError("Pasch trade does not preserve pair coverage")
    return tuple(sorted(mate))


def switch(blocks, configuration):
    old = set(configuration)
    switched = (set(blocks) - old) | set(pasch_mate(configuration))
    return validate_sts(switched)


def construct_classes(labelg=LABELG):
    pg_record = canonicalize_many([projective_seed()], labelg)[0]
    representatives = {
        pg_record: representative_from_canonical_graph6(pg_record)
    }
    queue = deque([pg_record])
    discovery_parent = {pg_record: None}
    while queue:
        source_record = queue.popleft()
        source = representatives[source_record]
        configurations = pasch_configurations(source)
        switched = [switch(source, config) for config in configurations]
        target_records = canonicalize_many(switched, labelg)
        for target_record in target_records:
            if target_record not in representatives:
                representatives[target_record] = representative_from_canonical_graph6(
                    target_record
                )
                discovery_parent[target_record] = source_record
                queue.append(target_record)
    if len(representatives) != 79:
        raise RuntimeError(
            f"projective-seed closure has {len(representatives)} classes, not 79"
        )

    anti_record = canonicalize_many([bose_antipasch_seed()], labelg)[0]
    anti_rep = representative_from_canonical_graph6(anti_record)
    if pasch_configurations(anti_rep):
        raise RuntimeError("Bose seed was expected to be anti-Pasch")
    if anti_record in representatives:
        raise RuntimeError("anti-Pasch seed unexpectedly lies in the Pasch closure")
    representatives[anti_record] = anti_rep
    discovery_parent[anti_record] = None
    if len(representatives) != 80:
        raise RuntimeError("failed to construct exactly 80 classes")
    return representatives, discovery_parent, pg_record, anti_record


def bfs(adjacency, source):
    distance = {source: 0}
    parent = {source: None}
    queue = deque([source])
    while queue:
        x = queue.popleft()
        for y in sorted(adjacency[x]):
            if y not in distance:
                distance[y] = distance[x] + 1
                parent[y] = x
                queue.append(y)
    return distance, parent


def graph_result(vertex_ids, edges):
    adjacency = {v: set() for v in vertex_ids}
    for x, y in edges:
        adjacency[x].add(y)
        adjacency[y].add(x)

    components = []
    unseen = set(vertex_ids)
    while unseen:
        root = min(unseen)
        component = set(bfs(adjacency, root)[0])
        components.append(sorted(component))
        unseen -= component
    components.sort(key=lambda c: (-len(c), c))

    all_distances = {}
    eccentricities = {}
    diameter = -1
    diameter_pairs = []
    for component in components:
        if len(component) == 1:
            eccentricities[component[0]] = 0
            all_distances[component[0]] = {component[0]: 0}
            continue
        for source in component:
            distances, _ = bfs(adjacency, source)
            if set(distances) != set(component):
                raise RuntimeError("BFS component mismatch")
            all_distances[source] = distances
            eccentricities[source] = max(distances.values())
        component_diameter = max(eccentricities[v] for v in component)
        if len(component) == 79:
            diameter = component_diameter
            diameter_pairs = [
                (x, y)
                for i, x in enumerate(component)
                for y in component[i + 1 :]
                if all_distances[x][y] == component_diameter
            ]
    if diameter < 0 or not diameter_pairs:
        raise RuntimeError("no nontrivial diameter pair found")

    u, v = min(diameter_pairs)
    distances, parent = bfs(adjacency, u)
    path = [v]
    while path[-1] != u:
        path.append(parent[path[-1]])
    path.reverse()
    layers = []
    for d in range(diameter + 1):
        layers.append(sorted(x for x in components[0] if distances[x] == d))

    main_component = components[0]
    radius = min(eccentricities[v] for v in main_component)
    centers = sorted(v for v in main_component if eccentricities[v] == radius)
    degree_sequence = sorted(len(adjacency[v]) for v in vertex_ids)
    return {
        "vertex_count": len(vertex_ids),
        "edge_count": len(edges),
        "components": components,
        "component_sizes": [len(c) for c in components],
        "component_diameters": [diameter, 0],
        "diameter": diameter,
        "diameter_pair": [u, v],
        "diameter_pair_count": len(diameter_pairs),
        "all_diameter_pairs": [list(p) for p in sorted(diameter_pairs)],
        "geodesic": path,
        "distance_row_from_first_endpoint": [
            distances.get(vertex) for vertex in vertex_ids
        ],
        "bfs_layers_from_first_endpoint": layers,
        "eccentricities": {
            vertex: eccentricities[vertex] for vertex in sorted(eccentricities)
        },
        "radius": radius,
        "centers": centers,
        "degree_sequence": degree_sequence,
    }


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as stream:
        json.dump(value, stream, indent=2, sort_keys=True)
        stream.write("\n")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="certificate")
    parser.add_argument("--labelg", default=LABELG)
    args = parser.parse_args()
    output = Path(args.output)

    representatives, parents, pg_record, anti_record = construct_classes(args.labelg)
    ordered_records = sorted(
        representatives, key=lambda record: representatives[record]
    )
    ids = {record: f"V{i:03d}" for i, record in enumerate(ordered_records)}
    vertices = []
    for record in ordered_records:
        rep = representatives[record]
        vertices.append(
            {
                "id": ids[record],
                "blocks": [list(block) for block in rep],
                "canonical_graph6": record,
                "pasch_count": len(pasch_configurations(rep)),
                "seed_role": (
                    "projective"
                    if record == pg_record
                    else "anti-Pasch"
                    if record == anti_record
                    else None
                ),
            }
        )

    edges = set()
    rows = {}
    for record in ordered_records:
        source_id = ids[record]
        rep = representatives[record]
        configurations = pasch_configurations(rep)
        switched = [switch(rep, config) for config in configurations]
        targets = canonicalize_many(switched, args.labelg)
        row = []
        for configuration, target_record in zip(configurations, targets):
            if target_record not in ids:
                raise RuntimeError("a switch target is outside the 80-class universe")
            target_id = ids[target_record]
            row.append(
                {
                    "removed": [list(block) for block in configuration],
                    "added": [list(block) for block in pasch_mate(configuration)],
                    "target": target_id,
                }
            )
            if source_id != target_id:
                edges.add(tuple(sorted((source_id, target_id))))
        rows[source_id] = {
            "pasch_count": len(configurations),
            "self_switch_occurrences": sum(
                item["target"] == source_id for item in row
            ),
            "distinct_targets_including_self": sorted(
                {item["target"] for item in row}
            ),
            "switches": row,
        }

    edge_list = sorted(edges)
    result = graph_result([v["id"] for v in vertices], edge_list)
    result.update(
        {
            "schema": "sts15-pasch-result-v1",
            "graph_convention": "undirected simple quotient; loops and multiplicities discarded",
            "projective_seed_id": ids[pg_record],
            "anti_pasch_id": ids[anti_record],
            "total_pasch_occurrences": sum(v["pasch_count"] for v in vertices),
            "pasch_count_multiset": sorted(v["pasch_count"] for v in vertices),
            "max_pasch_count": max(v["pasch_count"] for v in vertices),
            "min_pasch_count": min(v["pasch_count"] for v in vertices),
        }
    )

    reps_doc = {
        "schema": "sts15-representatives-v1",
        "point_set": list(range(15)),
        "canonicalizer": {
            "method": "degree-separated 50-vertex incidence graph canonicalized by nauty labelg -q -g",
            "executable": args.labelg,
            "executable_sha256": sha256_file(args.labelg),
        },
        "construction": {
            "component_seed": "PG(3,2) on nonzero F_2^4 vectors",
            "isolated_seed": "Bose STS(15) over Z_5 x Z_3",
            "closure_size_from_component_seed": 79,
        },
        "vertices": vertices,
    }
    edges_doc = {
        "schema": "sts15-pasch-edges-v1",
        "vertices": [v["id"] for v in vertices],
        "edges": [list(edge) for edge in edge_list],
    }
    rows_doc = {
        "schema": "sts15-pasch-switch-occurrences-v1",
        "rows": rows,
    }
    provenance = {
        "schema": "sts15-discovery-provenance-v1",
        "command": "python3 code/discover_graph.py --output certificate",
        "python": sys.version,
        "platform": platform.platform(),
        "labelg": args.labelg,
        "labelg_sha256": sha256_file(args.labelg),
        "seed": None,
        "randomness": "none",
        "objective_convention": "simple quotient graph; ignore loops and multiplicity",
    }
    write_json(output / "representatives.json", reps_doc)
    write_json(output / "quotient_edges.json", edges_doc)
    write_json(output / "switch_occurrences.json", rows_doc)
    write_json(output / "result.json", result)
    write_json(output / "discovery_provenance.json", provenance)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
