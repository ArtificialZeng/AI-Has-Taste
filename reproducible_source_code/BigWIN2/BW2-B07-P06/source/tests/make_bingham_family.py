#!/usr/bin/env python3
"""Construct Definition 3.1 of arXiv:2607.09563v1."""

from __future__ import annotations

import argparse
import json

import networkx as nx


def pair(c: int) -> tuple[nx.Graph, nx.Graph]:
    if c < 4:
        raise ValueError("c must be at least 4")
    # Vertex keys (side, kind, index), with 1 <= index <= c-1.
    base = nx.Graph()
    for side in ("L", "R"):
        for i in range(1, c):
            base.add_edge((side, "v", i), (side, "f", i))
            if i > 1:
                base.add_edge((side, "v", i - 1), (side, "v", i))
    g = base.copy()
    g.add_edge(("L", "v", c - 1), ("R", "v", 1))
    g.add_edge(("L", "f", 2), ("R", "v", 1))
    h = base.copy()
    h.add_edge(("L", "v", c - 1), ("R", "f", 1))
    h.add_edge(("L", "v", 2), ("R", "v", 1))
    return nx.convert_node_labels_to_integers(g), nx.convert_node_labels_to_integers(h)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("c", type=int)
    args = parser.parse_args()
    g, h = pair(args.c)
    print(
        json.dumps(
            {
                "c": args.c,
                "graph6_g": nx.to_graph6_bytes(g, header=False).strip().decode(),
                "graph6_h": nx.to_graph6_bytes(h, header=False).strip().decode(),
            }
        )
    )


if __name__ == "__main__":
    main()
