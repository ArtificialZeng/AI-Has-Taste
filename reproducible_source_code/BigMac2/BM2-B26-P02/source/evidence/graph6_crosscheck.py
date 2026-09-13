#!/Users/mac/4prove-or-disprove-math/.research-venv/bin/python
"""Cross-check the project graph6 codec against NetworkX's implementation."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path

import networkx as nx

from build_rooted_streams import decode_graph6, encode_graph6


def main() -> None:
    inventory = Path(__file__).with_name("order8-connected-nontrees.g6")
    records = inventory.read_bytes().splitlines()
    edge_distribution: Counter[int] = Counter()
    for record in records:
        graph = nx.from_graph6_bytes(record)
        assert len(graph) == 8
        assert nx.is_connected(graph)
        masks = [0] * 8
        for u, v in graph.edges:
            masks[u] |= 1 << v
            masks[v] |= 1 << u
        assert masks == decode_graph6(record)
        assert encode_graph6(masks, 0) == record
        edge_distribution[graph.number_of_edges()] += 1
    print(json.dumps({
        "status": "pass",
        "library": f"networkx {nx.__version__}",
        "records_cross_checked": len(records),
        "connected_records": len(records),
        "codec_roundtrips": len(records),
        "minimum_edges": min(edge_distribution),
        "maximum_edges": max(edge_distribution),
        "edge_distribution": dict(sorted(edge_distribution.items())),
        "inventory_sha256": hashlib.sha256(inventory.read_bytes()).hexdigest(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
