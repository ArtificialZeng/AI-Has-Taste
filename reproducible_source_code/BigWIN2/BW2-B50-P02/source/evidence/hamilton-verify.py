#!/usr/bin/env python3
"""Independent exact verification of every atlas Hamilton-cycle witness."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "evidence" / "atlas-through-6.json"
CYCLES = ROOT / "evidence" / "hamilton-cycles.json"
REPORT = ROOT / "evidence" / "hamilton-verify.txt"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def acyclic(n: int, edges: list[tuple[int, int]], mask: int) -> bool:
    adjacency = [[] for _ in range(n)]
    indegree = [0] * n
    for bit, (u, v) in enumerate(edges):
        if (mask >> bit) & 1:
            u, v = v, u
        adjacency[u].append(v)
        indegree[v] += 1
    stack = [v for v in range(n) if indegree[v] == 0]
    seen = 0
    while stack:
        u = stack.pop()
        seen += 1
        for v in adjacency[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                stack.append(v)
    return seen == n


def hamming_one(left: str, right: str) -> bool:
    return sum(a != b for a, b in zip(left, right)) == 1


def main() -> None:
    atlas = json.loads(ATLAS.read_text())
    witness = json.loads(CYCLES.read_text())
    assert witness["atlas_sha256"] == sha256(ATLAS)
    by_id = {g["graph6"]: g for g in atlas["graphs"]}
    records = witness["cycles"]
    expected = {g["graph6"] for g in atlas["graphs"] if g["sigma"] == 0}
    actual = [record["graph6"] for record in records]
    assert len(actual) == len(set(actual)) == witness["count"] == 125
    assert set(actual) == expected

    positive_by_order = Counter()
    negative_by_order = Counter()
    total_vertices = 0
    for record in records:
        entry = by_id[record["graph6"]]
        n = entry["order"]
        edges = sorted(tuple(edge) for edge in entry["edges"])
        width = len(edges)
        generated = {
            format(mask, f"0{width}b")[::-1]
            for mask in range(1 << width)
            if acyclic(n, edges, mask)
        }
        # This reconstruction neither uses atlas orientation lists nor flip edges.
        assert len(generated) == entry["acyclic_orientation_count"]
        cycle = record["cycle"]
        assert len(cycle) == len(set(cycle)) == len(generated)
        assert set(cycle) == generated
        assert sum((-1) ** bits.count("1") for bits in generated) == 0
        if len(cycle) == 2:
            assert n == 2 and hamming_one(cycle[0], cycle[1])
        else:
            assert all(
                hamming_one(cycle[i], cycle[(i + 1) % len(cycle)])
                for i in range(len(cycle))
            )
        positive_by_order[n] += 1
        total_vertices += len(cycle)

    # Recompute the signature obstruction for every negative atlas entry.
    # A flip changes one bit, so the flip graph is bipartite by mask parity.
    # A Hamilton cycle must use equally many vertices in its two parts.
    negative_ids = []
    for entry in atlas["graphs"]:
        if entry["sigma"] == 0:
            continue
        n = entry["order"]
        edges = sorted(tuple(edge) for edge in entry["edges"])
        width = len(edges)
        generated = [
            mask for mask in range(1 << width) if acyclic(n, edges, mask)
        ]
        even = sum(mask.bit_count() % 2 == 0 for mask in generated)
        odd = len(generated) - even
        signed = even - odd
        assert abs(signed) == entry["sigma"] != 0
        assert even != odd
        negative_by_order[n] += 1
        negative_ids.append(entry["graph6"])

    lines = [
        "Hamilton atlas independent verification PASS",
        f"atlas_sha256={sha256(ATLAS)}",
        f"cycles_sha256={sha256(CYCLES)}",
        f"positive_count={sum(positive_by_order.values())}",
        "positive_by_order=" + json.dumps(dict(sorted(positive_by_order.items()))),
        f"positive_orientation_vertices={total_vertices}",
        f"signature_obstructed_negative_count={sum(negative_by_order.values())}",
        "signature_obstructed_negative_by_order="
        + json.dumps(dict(sorted(negative_by_order.items()))),
        "signature_obstructed_graph6=" + json.dumps(negative_ids),
        "zero_signature_negative_count=0",
        "subset_DP_required=0 (the positive search had no apparent failure)",
        "Method: reconstructed every acyclic orientation directly from each edge list; "
        "checked exact cycle coverage and every cyclic Hamming-one step; independently "
        "recomputed the parity imbalance for every nonzero-signature graph.",
    ]
    REPORT.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
