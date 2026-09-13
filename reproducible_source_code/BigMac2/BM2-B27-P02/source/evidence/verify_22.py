#!/usr/bin/env python
"""Exact, dependency-free checker for 22-set-certificate.json.

Run with the research interpreter:
  /Users/mac/4prove-or-disprove-math/.research-venv/bin/python evidence/verify_22.py

All graph and bootstrap calculations use Python integers and finite sets.
"""

from __future__ import annotations

import json
from collections import deque
from pathlib import Path


ROOT = Path(__file__).resolve().parent
CERTIFICATE = ROOT / "22-set-certificate.json"
N = 8
VERTICES = {(i, j) for i in range(N) for j in range(N)}


def neighbors(vertex: tuple[int, int]) -> set[tuple[int, int]]:
    i, j = vertex
    return {
        ((i + 1) % N, j),
        ((i - 1) % N, j),
        (i, (j + 1) % N),
        (i, (j - 1) % N),
    }


def parse_vertex(raw: object) -> tuple[int, int]:
    assert isinstance(raw, list) and len(raw) == 2, f"bad vertex: {raw!r}"
    i, j = raw
    assert isinstance(i, int) and not isinstance(i, bool)
    assert isinstance(j, int) and not isinstance(j, bool)
    assert 0 <= i < N and 0 <= j < N, f"coordinate out of range: {raw!r}"
    return i, j


def induced_edges(vertices: set[tuple[int, int]]) -> set[tuple[tuple[int, int], tuple[int, int]]]:
    return {
        tuple(sorted((u, v)))
        for u in vertices
        for v in neighbors(u)
        if v in vertices
    }


def component_count(vertices: set[tuple[int, int]]) -> int:
    unseen = set(vertices)
    count = 0
    while unseen:
        count += 1
        start = min(unseen)
        unseen.remove(start)
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in neighbors(u) & unseen:
                unseen.remove(v)
                queue.append(v)
    return count


def main() -> None:
    document = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    assert document["threshold"] == 3
    raw_layers = document["layers"]
    assert [layer["round"] for layer in raw_layers] == list(range(len(raw_layers)))

    layers: list[set[tuple[int, int]]] = []
    for raw_layer in raw_layers:
        raw_vertices = raw_layer["vertices"]
        parsed = [parse_vertex(raw) for raw in raw_vertices]
        assert len(parsed) == len(set(parsed)), f"duplicate in round {raw_layer['round']}"
        layers.append(set(parsed))

    initial = layers[0]
    assert len(initial) == document["initial_size"] == 22
    infected = set(initial)

    for round_number, certified_layer in enumerate(layers[1:], start=1):
        recomputed_layer = {
            vertex
            for vertex in VERTICES - infected
            if len(neighbors(vertex) & infected) >= document["threshold"]
        }
        assert certified_layer == recomputed_layer, (
            f"round {round_number} mismatch: "
            f"missing={sorted(recomputed_layer - certified_layer)}, "
            f"extraneous={sorted(certified_layer - recomputed_layer)}"
        )
        infected.update(certified_layer)

    assert infected == VERTICES, f"closure stops at {len(infected)} vertices"
    assert not {
        vertex
        for vertex in VERTICES - infected
        if len(neighbors(vertex) & infected) >= document["threshold"]
    }

    complement = VERTICES - initial
    initial_edges = induced_edges(initial)
    complement_edges = induced_edges(complement)
    components = component_count(complement)
    checks = document["claimed_checks"]

    actual = {
        "layer_sizes": [len(layer) for layer in layers],
        "final_infected_size": len(infected),
        "rounds_after_initialization": len(layers) - 1,
        "initial_induced_edges": len(initial_edges),
        "complement_vertices": len(complement),
        "complement_induced_edges": len(complement_edges),
        "complement_components": components,
        "complement_is_tree": (
            components == 1 and len(complement_edges) == len(complement) - 1
        ),
    }
    assert actual == checks, f"summary mismatch: actual={actual}, claimed={checks}"
    assert initial_edges == {((0, 0), (0, 1))}

    print(json.dumps({"verified": True, **actual}, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
