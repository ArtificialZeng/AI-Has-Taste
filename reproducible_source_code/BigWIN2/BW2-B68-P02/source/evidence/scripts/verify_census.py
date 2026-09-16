#!/usr/bin/env python3
"""Independent format/property/coverage checks for the cubic graph6 census."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import networkx as nx


ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {4: 1, 6: 2, 8: 5, 10: 19, 12: 85, 14: 509, 16: 4060, 18: 41301}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    rows = []
    all_codes: set[bytes] = set()
    combined = bytearray()
    for n, expected in EXPECTED.items():
        path = ROOT / "census" / f"n{n:02d}.g6"
        raw = path.read_bytes()
        codes = raw.splitlines()
        assert raw.endswith(b"\n"), f"missing terminal newline: {path}"
        assert len(codes) == expected, (n, len(codes), expected)
        assert len(codes) == len(set(codes)), f"duplicate graph6 code at n={n}"
        assert all(code not in all_codes for code in codes), f"cross-file duplicate at n={n}"
        all_codes.update(codes)
        for index, code in enumerate(codes):
            graph = nx.from_graph6_bytes(code)
            assert graph.number_of_nodes() == n, (n, index, graph.number_of_nodes())
            assert graph.number_of_edges() == 3 * n // 2, (n, index)
            assert not graph.is_multigraph(), (n, index)
            assert nx.number_of_selfloops(graph) == 0, (n, index)
            assert all(degree == 3 for _, degree in graph.degree()), (n, index)
            assert nx.is_connected(graph), (n, index)
            # Re-encoding checks the graph6 decoder/encoder round trip on the
            # generator's fixed vertex labels; it is not a second canonizer.
            encoded = nx.to_graph6_bytes(graph, header=False).strip()
            assert encoded == code, (n, index, code, encoded)
        combined.extend(raw)
        rows.append(
            {
                "n": n,
                "count": len(codes),
                "sha256": sha256(raw),
                "first_graph6": codes[0].decode("ascii"),
                "last_graph6": codes[-1].decode("ascii"),
            }
        )

    assert len(all_codes) == sum(EXPECTED.values()) == 45982
    report = {
        "checker": str(Path(__file__).relative_to(ROOT)),
        "networkx_version": nx.__version__,
        "checks": [
            "graph6 decode/re-encode",
            "order and edge count",
            "simplicity and looplessness",
            "3-regularity",
            "connectedness",
            "literal canonical-code uniqueness",
            "expected order-by-order counts",
        ],
        "limitation": (
            "Literal uniqueness is decisive only conditional on geng -l producing "
            "canonical labels; this checker is not an independent canonizer."
        ),
        "orders": rows,
        "total": len(all_codes),
        "combined_order": "n=4,6,...,18; within each file geng -l traversal/output order",
        "combined_sha256": sha256(bytes(combined)),
        "status": "pass",
    }
    output = ROOT / "evidence" / "census_verification.json"
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
