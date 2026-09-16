#!/usr/bin/env python3
"""Verifier for every serialized graph and partition certificate in a probe run."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import networkx as nx


def verify(g: nx.Graph, cert: dict) -> None:
    a0, a1, b = map(set, (cert["A0"], cert["A1"], cert["B"]))
    vertices = set(g.nodes())
    assert not (a0 & a1 or a0 & b or a1 & b)
    assert a0 | a1 | b == vertices
    assert all(not ((u in a0 and v in a0) or (u in a1 and v in a1)) for u, v in g.edges())
    a = a0 | a1
    assert max((g.subgraph(a).degree(v) for v in a), default=0) <= 2
    assert max((g.subgraph(b).degree(v) for v in b), default=0) <= 3


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("data", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.data.read_text())
    assert not payload["failures"]
    assert not payload["bad_certificates"]
    count = 0
    for record in payload["records"]:
        g = nx.from_graph6_bytes(record["graph6"].encode())
        assert g.number_of_nodes() == record["order"]
        assert g.number_of_edges() == record["size"]
        assert max((d for _, d in g.degree()), default=0) <= 6
        assert not any(nx.triangles(g).values())
        assert record["partition_found"] and record["certificate_verified"]
        verify(g, record["certificate"])
        count += 1
    assert count == payload["tested"]
    print(json.dumps({
        "verified": True,
        "records": count,
        "seed": payload["seed"],
        "coverage": payload["coverage"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
