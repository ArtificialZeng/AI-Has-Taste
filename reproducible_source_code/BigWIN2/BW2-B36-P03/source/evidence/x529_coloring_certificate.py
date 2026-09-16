#!/usr/bin/env python3
"""Generate or verify a complete coloring certificate for x=529.

The certificate is independent of any optimization solver.  For each of the
263 possible even gaps, it gives a proper coloring of the exact compatibility
graph from problem.md with at most 41 colors.  Since every 42-column witness
would be a 42-clique, the colorings exclude all such witnesses.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
import sys


FORMAT = "win36-x529-compatibility-coloring-v1"


def compatible(v: int, w: int, d: int) -> bool:
    """Return adjacency in G_{529,d}, using the definition verbatim."""
    entries = (v, v + d, w, w + d)
    return len(set(entries)) == 4 and all(
        math.gcd(entries[i], entries[j]) == 1
        for i in range(4)
        for j in range(i + 1, 4)
    )


def graph(x: int, d: int) -> tuple[list[int], dict[int, set[int]]]:
    vertices = [v for v in range(2, x - d + 1) if math.gcd(v, v + d) == 1]
    neighbors = {v: set() for v in vertices}
    for i, v in enumerate(vertices):
        for w in vertices[i + 1 :]:
            if compatible(v, w, d):
                neighbors[v].add(w)
                neighbors[w].add(v)
    return vertices, neighbors


def dsatur(vertices: list[int], neighbors: dict[int, set[int]]) -> list[int]:
    """Deterministic DSATUR greedy coloring (ascending vertex tie-break)."""
    color: dict[int, int] = {}
    neighbor_colors = {v: set() for v in vertices}
    uncolored = set(vertices)
    while uncolored:
        v = min(
            uncolored,
            key=lambda w: (-len(neighbor_colors[w]), -len(neighbors[w]), w),
        )
        forbidden = neighbor_colors[v]
        c = 0
        while c in forbidden:
            c += 1
        color[v] = c
        uncolored.remove(v)
        for w in neighbors[v] & uncolored:
            neighbor_colors[w].add(c)
    return [color[v] for v in vertices]


def payload_hash(payload: dict) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def generate(path: pathlib.Path) -> None:
    x = 529
    records = []
    for d in range(2, 527, 2):
        vertices, neighbors = graph(x, d)
        colors = dsatur(vertices, neighbors)
        color_count = max(colors, default=-1) + 1
        if color_count > 41:
            raise RuntimeError(f"construction used {color_count} colors at d={d}")
        records.append(
            {
                "d": d,
                "vertices": vertices,
                "colors": colors,
                "color_count": color_count,
                "edge_count": sum(map(len, neighbors.values())) // 2,
            }
        )
    payload = {
        "format": FORMAT,
        "x": x,
        "target_columns_excluded": 42,
        "even_gaps": records,
    }
    document = {"payload": payload, "payload_sha256": payload_hash(payload)}
    path.write_text(json.dumps(document, indent=2, sort_keys=True) + "\n")


def verify(path: pathlib.Path) -> dict:
    document = json.loads(path.read_text())
    payload = document["payload"]
    failures: list[str] = []
    if payload.get("format") != FORMAT:
        failures.append("wrong format identifier")
    if payload.get("x") != 529:
        failures.append("x is not 529")
    if payload.get("target_columns_excluded") != 42:
        failures.append("target is not 42")
    if document.get("payload_sha256") != payload_hash(payload):
        failures.append("payload hash mismatch")

    records = payload.get("even_gaps", [])
    recorded_gaps = [record.get("d") for record in records]
    expected_gaps = list(range(2, 527, 2))
    if recorded_gaps != expected_gaps:
        failures.append("gap list is not exactly 2,4,...,526 in order")

    checked_edges = 0
    maximum_colors = 0
    maximum_color_gaps: list[int] = []
    for record in records:
        d = record.get("d")
        if not isinstance(d, int) or d not in expected_gaps:
            failures.append(f"invalid gap record {d!r}")
            continue
        expected_vertices, neighbors = graph(529, d)
        vertices = record.get("vertices")
        colors = record.get("colors")
        if vertices != expected_vertices:
            failures.append(f"d={d}: vertex list is not exactly C_{{529,d}}")
            continue
        if not isinstance(colors, list) or len(colors) != len(vertices):
            failures.append(f"d={d}: color vector has wrong length")
            continue
        if any(not isinstance(c, int) or c < 0 for c in colors):
            failures.append(f"d={d}: colors must be nonnegative integers")
            continue
        actual_count = max(colors, default=-1) + 1
        if record.get("color_count") != actual_count:
            failures.append(f"d={d}: stated color count is wrong")
        if actual_count > 41:
            failures.append(f"d={d}: coloring uses {actual_count} > 41 colors")
        if actual_count > maximum_colors:
            maximum_colors = actual_count
            maximum_color_gaps = [d]
        elif actual_count == maximum_colors:
            maximum_color_gaps.append(d)
        by_vertex = dict(zip(vertices, colors))
        edge_count = 0
        for v in vertices:
            for w in neighbors[v]:
                if v < w:
                    edge_count += 1
                    if by_vertex[v] == by_vertex[w]:
                        failures.append(
                            f"d={d}: compatible starts {v},{w} share color {by_vertex[v]}"
                        )
        checked_edges += edge_count
        if record.get("edge_count") != edge_count:
            failures.append(f"d={d}: stated edge count is wrong")

    summary = {
        "certificate": str(path),
        "verified": not failures,
        "gaps_checked": len(records),
        "expected_gaps": 263,
        "compatible_edges_checked": checked_edges,
        "maximum_color_count": maximum_colors,
        "gaps_attaining_maximum_color_count": maximum_color_gaps,
        "failures": failures,
    }
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=("generate", "verify"))
    parser.add_argument("certificate", type=pathlib.Path)
    args = parser.parse_args()
    if args.mode == "generate":
        generate(args.certificate)
    summary = verify(args.certificate)
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["verified"] else 1


if __name__ == "__main__":
    sys.exit(main())
