#!/usr/bin/env python3
"""Check the exact weighted-cycle contradiction for the frozen graph.

The checker uses integer arithmetic only.  It independently decodes the fixed
graph6 member and validates every cycle carried by the certificate; it neither
imports the certificate builder nor reads the floating-point LP ray.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from collections import Counter, deque
from pathlib import Path


EXPECTED_ARCHIVE_SHA256 = "5dd250b705e4ed8e9fe6be625285adffea0d98d9f18b3640071ed4a6e4290fe4"
EXPECTED_MEMBER_SHA256 = "8b074cd755a5d1e1e6a1d09a7888173821372e6cdcd501cfd2baf1a34bfeb08e"
EXPECTED_SOURCE_SHA256 = "29441258d1fb9526154bab4ea6f8c973728e4ab25b86dc18932baa2b03e5e596"
EXPECTED_CENSUS_SHA256 = "1aebbf14917b5d14aaed298898e5386e78f7dd4b2d322fb06118c35f4c8344a8"
EXPECTED_RAY_SHA256 = "65dbf463002e2978e500375938014e442d1c1c25899f0e92fd6b6e0bf44bab21"
EXPECTED_VERTICES = 812
EXPECTED_EDGES = 1218


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def decode_graph6(record: bytes) -> list[list[int]]:
    """Decode one graph6 record without using the census implementation."""
    text = record.decode("ascii").strip()
    if text.startswith(">>graph6<<"):
        text = text[len(">>graph6<<") :]
    symbols = [ord(char) - 63 for char in text]
    if not symbols or any(symbol < 0 or symbol > 63 for symbol in symbols):
        raise ValueError("invalid graph6 alphabet")
    if symbols[0] <= 62:
        order, cursor = symbols[0], 1
    elif len(symbols) >= 4 and symbols[1] <= 62:
        order = (symbols[1] << 12) + (symbols[2] << 6) + symbols[3]
        cursor = 4
    else:
        raise ValueError("unsupported graph6 order prefix")

    adjacency = [[] for _ in range(order)]
    bit_number = 0
    available_bits = 6 * (len(symbols) - cursor)
    required_bits = order * (order - 1) // 2
    if available_bits < required_bits:
        raise ValueError("truncated graph6 record")
    for high in range(1, order):
        for low in range(high):
            symbol = symbols[cursor + bit_number // 6]
            bit = (symbol >> (5 - bit_number % 6)) & 1
            if bit:
                adjacency[low].append(high)
                adjacency[high].append(low)
            bit_number += 1
    for neighbours in adjacency:
        neighbours.sort()
    return adjacency


def graph_girth(adjacency: list[list[int]]) -> int:
    answer = len(adjacency) + 1
    for root in range(len(adjacency)):
        distance = [-1] * len(adjacency)
        parent = [-1] * len(adjacency)
        distance[root] = 0
        queue = deque([root])
        while queue:
            vertex = queue.popleft()
            if 2 * distance[vertex] + 1 >= answer:
                continue
            for neighbour in adjacency[vertex]:
                if distance[neighbour] < 0:
                    distance[neighbour] = distance[vertex] + 1
                    parent[neighbour] = vertex
                    queue.append(neighbour)
                elif parent[vertex] != neighbour:
                    answer = min(answer, distance[vertex] + distance[neighbour] + 1)
    return answer


def canonical_cycle(vertices: tuple[int, ...]) -> tuple[int, ...]:
    minimum = min(vertices)
    position = vertices.index(minimum)
    forward = vertices[position:] + vertices[:position]
    reverse_all = tuple(reversed(vertices))
    reverse_position = reverse_all.index(minimum)
    reverse = reverse_all[reverse_position:] + reverse_all[:reverse_position]
    return min(forward, reverse)


def parse_certificate(path: Path) -> tuple[dict[str, str], list[tuple[int, int, tuple[int, ...]]]]:
    metadata: dict[str, str] = {}
    records: list[tuple[int, int, tuple[int, ...]]] = []
    for line_number, line in enumerate(path.read_text(encoding="ascii").splitlines(), 1):
        if not line:
            raise ValueError(f"blank certificate line {line_number}")
        if line.startswith("#"):
            body = line[1:].strip()
            if body == "exact-cycle-weight-certificate-v1":
                metadata["schema"] = body
            elif " " in body:
                key, value = body.split(" ", 1)
                metadata[key] = value
            continue
        fields = [int(part) for part in line.split()]
        if len(fields) < 4:
            raise ValueError(f"short certificate row {line_number}")
        cycle_index, weight, length = fields[:3]
        vertices = tuple(fields[3:])
        if len(vertices) != length:
            raise ValueError(f"length mismatch on certificate row {line_number}")
        records.append((cycle_index, weight, vertices))
    return metadata, records


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    parser.add_argument("member")
    parser.add_argument("certificate", type=Path)
    parser.add_argument("source", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()

    archive_bytes = args.archive.read_bytes()
    if sha256(archive_bytes) != EXPECTED_ARCHIVE_SHA256:
        raise ValueError("archive SHA-256 does not match the frozen deposit")
    with zipfile.ZipFile(args.archive) as archive:
        member_bytes = archive.read(args.member)
    if sha256(member_bytes) != EXPECTED_MEMBER_SHA256:
        raise ValueError("graph6 member SHA-256 does not match the frozen base")
    if sha256(args.source.read_bytes()) != EXPECTED_SOURCE_SHA256:
        raise ValueError("immutable source.md digest mismatch")

    adjacency = decode_graph6(member_bytes)
    if len(adjacency) != EXPECTED_VERTICES:
        raise ValueError("wrong graph order")
    if any(len(neighbours) != 3 or len(set(neighbours)) != 3 for neighbours in adjacency):
        raise ValueError("frozen graph is not simple cubic")
    edge_count = sum(map(len, adjacency)) // 2
    if edge_count != EXPECTED_EDGES:
        raise ValueError("wrong graph size")
    girth = graph_girth(adjacency)
    if girth != 14:
        raise ValueError(f"wrong graph girth: {girth}")

    certificate_bytes = args.certificate.read_bytes()
    metadata, records = parse_certificate(args.certificate)
    if metadata.get("schema") != "exact-cycle-weight-certificate-v1":
        raise ValueError("wrong certificate schema")
    if metadata.get("census_sha256") != EXPECTED_CENSUS_SHA256:
        raise ValueError("certificate is not bound to the canonical census")
    if metadata.get("ray_sha256") != EXPECTED_RAY_SHA256:
        raise ValueError("certificate construction provenance has changed")
    if int(metadata.get("nonzero_weights", "-1")) != len(records):
        raise ValueError("declared support size mismatch")

    seen_indices: set[int] = set()
    seen_cycles: set[tuple[int, ...]] = set()
    scores = [{neighbour: 0 for neighbour in neighbours} for neighbours in adjacency]
    support_by_length: Counter[int] = Counter()
    weight_by_length: Counter[int] = Counter()
    weighted_requirement = 0
    total_weight = 0

    for cycle_index, weight, vertices in records:
        length = len(vertices)
        if cycle_index < 0 or cycle_index >= 7308 or cycle_index in seen_indices:
            raise ValueError(f"invalid or duplicate census index {cycle_index}")
        seen_indices.add(cycle_index)
        if weight <= 0:
            raise ValueError(f"nonpositive weight at census index {cycle_index}")
        if length not in (14, 15, 16):
            raise ValueError(f"invalid cycle length {length}")
        if len(set(vertices)) != length or any(v < 0 or v >= len(adjacency) for v in vertices):
            raise ValueError(f"cycle {cycle_index} is not vertex-simple")
        normalized = canonical_cycle(vertices)
        if vertices != normalized:
            raise ValueError(f"cycle {cycle_index} is not canonically serialized")
        if normalized in seen_cycles:
            raise ValueError(f"duplicate cycle at census index {cycle_index}")
        seen_cycles.add(normalized)
        cycle_set = set(vertices)
        for position, vertex in enumerate(vertices):
            previous_vertex = vertices[position - 1]
            next_vertex = vertices[(position + 1) % length]
            if previous_vertex not in adjacency[vertex] or next_vertex not in adjacency[vertex]:
                raise ValueError(f"nonedge in cycle {cycle_index}")
            outside = [neighbour for neighbour in adjacency[vertex] if neighbour not in cycle_set]
            if len(outside) != 1:
                raise ValueError(f"cycle {cycle_index} lacks a unique outside edge at {vertex}")
            scores[vertex][outside[0]] += weight
        requirement = 33 - 2 * length
        weighted_requirement += weight * requirement
        total_weight += weight
        support_by_length[length] += 1
        weight_by_length[length] += weight

    vertex_upper_bounds = [max(vertex_scores.values()) for vertex_scores in scores]
    assignment_upper_bound = sum(vertex_upper_bounds)
    contradiction_gap = weighted_requirement - assignment_upper_bound
    uniform_vertex_cap = max(vertex_upper_bounds)
    uniform_assignment_upper_bound = len(adjacency) * uniform_vertex_cap
    uniform_gap = weighted_requirement - uniform_assignment_upper_bound
    if contradiction_gap <= 0:
        raise ValueError("weighted inequalities do not give a strict contradiction")
    if uniform_gap <= 0:
        raise ValueError("even the declared uniform per-vertex bound must contradict demand")
    if int(metadata.get("total_weight", "-1")) != total_weight:
        raise ValueError("declared total weight mismatch")
    expected_support = " ".join(
        f"{length}:{support_by_length[length]}" for length in (14, 15, 16)
    )
    if metadata.get("support_by_length") != expected_support:
        raise ValueError("declared support-by-length mismatch")

    report = {
        "schema": "exact-cycle-weight-check-v1",
        "status": "verified_unsat",
        "arithmetic": "exact integers",
        "archive_sha256": sha256(archive_bytes),
        "graph_member": args.member,
        "graph_member_sha256": sha256(member_bytes),
        "source_sha256": sha256(args.source.read_bytes()),
        "certificate_sha256": sha256(certificate_bytes),
        "construction_ray_sha256": metadata["ray_sha256"],
        "canonical_census_sha256": metadata["census_sha256"],
        "graph": {
            "vertices": len(adjacency),
            "edges": edge_count,
            "degree": 3,
            "girth": girth,
        },
        "certificate": {
            "positive_cycle_weights": len(records),
            "support_by_length": {str(k): support_by_length[k] for k in (14, 15, 16)},
            "weight_by_length": {str(k): weight_by_length[k] for k in (14, 15, 16)},
            "total_weight": total_weight,
            "maximum_weight": max(weight for _, weight, _ in records),
        },
        "weighted_cycle_lower_bound": weighted_requirement,
        "assignment_upper_bound": assignment_upper_bound,
        "strict_gap": contradiction_gap,
        "vertex_upper_bound_range": [min(vertex_upper_bounds), max(vertex_upper_bounds)],
        "uniform_vertex_cap": uniform_vertex_cap,
        "uniform_assignment_upper_bound": uniform_assignment_upper_bound,
        "uniform_strict_gap": uniform_gap,
        "reason": (
            "Every allowed neighbour choice contributes at most the recorded per-vertex "
            "maximum, but every satisfying orientation would have to meet the strictly "
            "larger weighted sum of cycle outside-choice requirements."
        ),
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
