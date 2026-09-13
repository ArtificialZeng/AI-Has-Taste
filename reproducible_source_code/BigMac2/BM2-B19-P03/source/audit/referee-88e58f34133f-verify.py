#!/usr/bin/env python3
"""Fresh exact verification using only the frozen, listed text artifacts."""

from __future__ import annotations

import hashlib
import json
from collections import Counter, deque
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_MEMBER_SHA256 = (
    "8b074cd755a5d1e1e6a1d09a7888173821372e6cdcd501cfd2baf1a34bfeb08e"
)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def encode_graph6(adjacency: list[set[int]]) -> bytes:
    n = len(adjacency)
    if n <= 62:
        prefix = bytes([n + 63])
    elif n <= 258047:
        prefix = bytes(
            [126, ((n >> 12) & 63) + 63, ((n >> 6) & 63) + 63, (n & 63) + 63]
        )
    else:
        raise ValueError("order outside the graph6 range needed here")

    bits = [1 if low in adjacency[high] else 0 for high in range(1, n) for low in range(high)]
    bits.extend([0] * ((-len(bits)) % 6))
    payload = bytes(
        [63 + sum(bits[offset + j] << (5 - j) for j in range(6)) for offset in range(0, len(bits), 6)]
    )
    return prefix + payload


def girth(adjacency: list[set[int]]) -> int:
    """Compute girth exactly by deleting each edge and finding a shortest return path."""
    best = len(adjacency) + 1
    for u in range(len(adjacency)):
        for v in adjacency[u]:
            if u >= v:
                continue
            distance = [-1] * len(adjacency)
            distance[u] = 0
            queue = deque([u])
            while queue:
                x = queue.popleft()
                if distance[x] + 1 >= best:
                    continue
                for y in adjacency[x]:
                    if (x == u and y == v) or (x == v and y == u):
                        continue
                    if distance[y] < 0:
                        distance[y] = distance[x] + 1
                        if y == v:
                            best = min(best, distance[y] + 1)
                            queue.clear()
                            break
                        queue.append(y)
    return best


def parse_census(path: Path) -> list[tuple[int, tuple[int, ...]]]:
    records: list[tuple[int, tuple[int, ...]]] = []
    seen: set[tuple[int, ...]] = set()
    for line_number, raw in enumerate(path.read_text(encoding="ascii").splitlines(), 1):
        fields = [int(value) for value in raw.split()]
        if not fields:
            raise ValueError(f"empty census row {line_number}")
        length, vertices = fields[0], tuple(fields[1:])
        if length not in (14, 15, 16) or len(vertices) != length:
            raise ValueError(f"bad length on census row {line_number}")
        if len(set(vertices)) != length or min(vertices) < 0 or max(vertices) >= 812:
            raise ValueError(f"bad vertex list on census row {line_number}")
        if vertices[0] != min(vertices) or vertices[1] >= vertices[-1]:
            raise ValueError(f"noncanonical census row {line_number}")
        if vertices in seen:
            raise ValueError(f"duplicate census row {line_number}")
        seen.add(vertices)
        records.append((length, vertices))
    return records


def reconstruct_graph(census: list[tuple[int, tuple[int, ...]]]) -> list[set[int]]:
    adjacency = [set() for _ in range(812)]
    for _, cycle in census:
        for u, v in zip(cycle, cycle[1:] + cycle[:1]):
            if u == v:
                raise ValueError("loop in a census cycle")
            adjacency[u].add(v)
            adjacency[v].add(u)
    if any(len(neighbours) != 3 for neighbours in adjacency):
        raise ValueError("the union of serialized cycle edges is not cubic")
    if sum(map(len, adjacency)) // 2 != 1218:
        raise ValueError("unexpected reconstructed edge count")
    return adjacency


def connected(adjacency: list[set[int]]) -> bool:
    seen = {0}
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return len(seen) == len(adjacency)


def parse_instance(
    path: Path,
    census: list[tuple[int, tuple[int, ...]]],
    adjacency: list[set[int]],
) -> list[tuple[int, int, tuple[tuple[int, int], ...]]]:
    lines = path.read_text(encoding="ascii").splitlines()
    if lines[0].split() != ["812", str(len(census))]:
        raise ValueError("bad instance header")
    if len(lines) != len(census) + 1:
        raise ValueError("bad instance row count")
    rows = []
    for index, (raw, (cycle_length, cycle)) in enumerate(zip(lines[1:], census)):
        fields = [int(value) for value in raw.split()]
        requirement, length = fields[:2]
        if len(fields) != 2 + 2 * length:
            raise ValueError(f"bad field count on instance row {index}")
        pairs = tuple(zip(fields[2::2], fields[3::2]))
        if requirement != 33 - 2 * cycle_length or length != cycle_length:
            raise ValueError(f"bad requirement on instance row {index}")
        if tuple(vertex for vertex, _ in pairs) != cycle:
            raise ValueError(f"instance/census vertex mismatch on row {index}")
        cycle_set = set(cycle)
        for vertex, choice_type in pairs:
            if choice_type not in (0, 1, 2):
                raise ValueError(f"bad choice type on instance row {index}")
            outside = sorted(adjacency[vertex] - cycle_set)
            if len(outside) != 1:
                raise ValueError(f"cycle {index} has no unique noncycle edge at {vertex}")
            if sorted(adjacency[vertex])[choice_type] != outside[0]:
                raise ValueError(f"wrong outside-choice coordinate on instance row {index}")
        rows.append((requirement, length, pairs))
    return rows


def parse_certificate(
    path: Path, census: list[tuple[int, tuple[int, ...]]]
) -> tuple[dict[str, str], dict[int, int]]:
    metadata: dict[str, str] = {}
    weights: dict[int, int] = {}
    for line_number, raw in enumerate(path.read_text(encoding="ascii").splitlines(), 1):
        if raw.startswith("#"):
            body = raw[1:].strip()
            if " " in body:
                key, value = body.split(" ", 1)
                metadata[key] = value
            else:
                metadata["schema"] = body
            continue
        fields = [int(value) for value in raw.split()]
        index, weight, length = fields[:3]
        vertices = tuple(fields[3:])
        if index in weights or weight <= 0 or not 0 <= index < len(census):
            raise ValueError(f"bad certificate index/weight on line {line_number}")
        if (length, vertices) != census[index]:
            raise ValueError(f"certificate/census mismatch on line {line_number}")
        weights[index] = weight
    if metadata.get("schema") != "exact-cycle-weight-certificate-v1":
        raise ValueError("bad certificate schema")
    if int(metadata.get("nonzero_weights", -1)) != len(weights):
        raise ValueError("bad declared support size")
    return metadata, weights


def main() -> None:
    census_path = ROOT / "evidence/cycles_14_16.tsv"
    instance_path = ROOT / "evidence/orientation_search_instance.tsv"
    certificate_path = ROOT / "evidence/exact_cycle_weights.tsv"
    census = parse_census(census_path)
    adjacency = reconstruct_graph(census)
    if not connected(adjacency):
        raise ValueError("reconstructed graph is disconnected")

    graph6 = encode_graph6(adjacency)
    variants = {
        "bare": graph6,
        "LF": graph6 + b"\n",
        "CRLF": graph6 + b"\r\n",
        "header+bare": b">>graph6<<" + graph6,
        "header+LF": b">>graph6<<" + graph6 + b"\n",
    }
    matching_serializations = [name for name, data in variants.items() if sha256(data) == EXPECTED_MEMBER_SHA256]
    if matching_serializations != ["CRLF"]:
        raise ValueError(f"reconstructed graph6 digest mismatch: {matching_serializations}")

    instance = parse_instance(instance_path, census, adjacency)
    metadata, weights = parse_certificate(certificate_path, census)
    if metadata.get("census_sha256") != sha256(census_path.read_bytes()):
        raise ValueError("certificate census digest mismatch")

    scores = [[0, 0, 0] for _ in range(812)]
    weighted_requirement = 0
    support = Counter()
    weight_sums = Counter()
    for index, weight in weights.items():
        requirement, length, pairs = instance[index]
        weighted_requirement += weight * requirement
        support[length] += 1
        weight_sums[length] += weight
        for vertex, choice_type in pairs:
            scores[vertex][choice_type] += weight

    assignment_upper_bound = sum(max(row) for row in scores)
    gap = weighted_requirement - assignment_upper_bound
    if gap <= 0:
        raise ValueError("no strict weighted contradiction")
    if int(metadata.get("total_weight", -1)) != sum(weights.values()):
        raise ValueError("declared total weight mismatch")

    result = {
        "schema": "fresh-referee-exact-check-v1",
        "status": "verified_unsat",
        "inputs": {
            "census_sha256": sha256(census_path.read_bytes()),
            "instance_sha256": sha256(instance_path.read_bytes()),
            "certificate_sha256": sha256(certificate_path.read_bytes()),
        },
        "reconstructed_graph": {
            "vertices": len(adjacency),
            "edges": sum(map(len, adjacency)) // 2,
            "degree_set": sorted({len(row) for row in adjacency}),
            "connected": connected(adjacency),
            "girth": girth(adjacency),
            "graph6_serialization": matching_serializations[0],
            "graph6_member_sha256": sha256(variants[matching_serializations[0]]),
        },
        "cycle_counts": {str(k): sum(length == k for length, _ in census) for k in (14, 15, 16)},
        "constraints": len(census),
        "certificate_support": len(weights),
        "support_by_length": {str(k): support[k] for k in (14, 15, 16)},
        "weight_by_length": {str(k): weight_sums[k] for k in (14, 15, 16)},
        "weighted_cycle_lower_bound": weighted_requirement,
        "assignment_upper_bound": assignment_upper_bound,
        "strict_gap": gap,
        "vertex_upper_bound_range": [min(map(max, scores)), max(map(max, scores))],
    }
    output = ROOT / "audit/referee-88e58f34133f-check.json"
    output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
