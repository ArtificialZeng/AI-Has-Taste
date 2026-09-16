#!/usr/bin/env python3
"""Deterministically verify the explicit AVD total coloring."""
import json
from pathlib import Path

data = json.loads((Path(__file__).parent / "triage-6-coloring.json").read_text())
vertices = {f"{i}{j}" for i in range(3) for j in range(3)}
edges = {
    "-".join(sorted((u, v)))
    for u in vertices
    for v in vertices
    if u < v and (u[0] == v[0] or u[1] == v[1])
}
assert set(data["vertex_colors"]) == vertices
assert set(data["edge_colors"]) == edges
palette = set(data["palette"])
assert palette == set(range(1, 7))
assert set(data["vertex_colors"].values()) <= palette
assert set(data["edge_colors"].values()) <= palette

incident = {u: [] for u in vertices}
for edge, color in data["edge_colors"].items():
    u, v = edge.split("-")
    incident[u].append(color)
    incident[v].append(color)
    assert data["vertex_colors"][u] != data["vertex_colors"][v]

color_sets = {}
for u in vertices:
    local = [data["vertex_colors"][u], *incident[u]]
    assert len(local) == 5 and len(set(local)) == 5
    color_sets[u] = set(local)
    assert palette - color_sets[u] == {data["missing_colors"][u]}

for edge in edges:
    u, v = edge.split("-")
    assert color_sets[u] != color_sets[v]

print("PASS: 9 vertices, 18 edges, proper AVD total coloring with 6 colors")
