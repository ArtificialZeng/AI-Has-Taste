#!/usr/bin/env python3
"""Independent exact verifier for the ordered-split lower-bound witness."""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from pathlib import Path


def fail(message: str) -> None:
    raise SystemExit(f"FAIL: {message}")


def main() -> None:
    if len(sys.argv) != 2:
        fail("usage: verify_split_witness.py CERTIFICATE.json")
    path = Path(sys.argv[1])
    raw = path.read_bytes()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        fail(f"malformed JSON: {exc}")
    required = {
        "schema_version",
        "vertices_in_displayed_order",
        "edges",
        "claimed_unique_partition",
        "claimed_edge_types_in_edge_order",
    }
    if not required.issubset(data):
        fail(f"missing fields: {sorted(required - set(data))}")
    vertices = data["vertices_in_displayed_order"]
    if len(vertices) != 4 or len(set(vertices)) != 4:
        fail("the vertex list must contain four distinct labels")
    vertex_set = set(vertices)
    edges = {frozenset(e) for e in data["edges"]}
    if any(len(e) != 2 or not e <= vertex_set for e in edges):
        fail("every edge must have two distinct declared endpoints")
    expected_path = {
        frozenset((vertices[0], vertices[1])),
        frozenset((vertices[1], vertices[2])),
        frozenset((vertices[2], vertices[3])),
    }
    if edges != expected_path:
        fail("the declared graph is not the displayed four-vertex path")

    partitions = []
    # Independent implementation: Q is accepted precisely when every pair in
    # Q is an edge and every pair outside Q is a nonedge.
    for size in range(5):
        for q_tuple in itertools.combinations(vertices, size):
            q = frozenset(q_tuple)
            i_set = frozenset(vertex_set - q)
            q_clique = all(frozenset(pair) in edges for pair in itertools.combinations(q, 2))
            i_independent = all(
                frozenset(pair) not in edges for pair in itertools.combinations(i_set, 2)
            )
            if q_clique and i_independent:
                partitions.append((q, i_set))

    claimed_q = frozenset(data["claimed_unique_partition"]["Q"])
    claimed_i = frozenset(data["claimed_unique_partition"]["I"])
    if partitions != [(claimed_q, claimed_i)]:
        fail(f"partition claim mismatch; computed {partitions}")

    position = {v: j for j, v in enumerate(vertices)}
    types = []
    for e in data["edges"]:
        x, y = sorted(e, key=position.get)
        if x in claimed_q and y in claimed_q:
            types.append("QQ")
        elif x in claimed_q and y in claimed_i:
            types.append("QI")
        elif x in claimed_i and y in claimed_q:
            types.append("IQ")
        else:
            fail("an edge lies inside the claimed independent part")
    if types != data["claimed_edge_types_in_edge_order"]:
        fail(f"edge-type claim mismatch; computed {types}")
    if set(types) != {"QQ", "QI", "IQ"}:
        fail("the three required types are not all realized")

    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_hash = hashlib.sha256(raw).hexdigest()
    print(
        "OK split_witness "
        f"partitions={len(partitions)} types={','.join(types)} "
        f"input_sha256={input_hash} code_sha256={code_hash}"
    )


if __name__ == "__main__":
    main()
