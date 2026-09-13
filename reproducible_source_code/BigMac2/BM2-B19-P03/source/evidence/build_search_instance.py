#!/usr/bin/env python3
"""Emit the exact CSP as a small incidence file for heuristic model search."""

from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path

from cycle_census import decode_graph6


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("archive", type=Path)
    ap.add_argument("member")
    ap.add_argument("census", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("report", type=Path)
    args = ap.parse_args()
    with zipfile.ZipFile(args.archive) as zf:
        member_bytes = zf.read(args.member)
    adj = decode_graph6(member_bytes)
    for row in adj:
        row.sort()
    rows: list[str] = []
    counts = {14: 0, 15: 0, 16: 0}
    for raw in args.census.read_text().splitlines():
        fields = [int(x) for x in raw.split()]
        length, cycle = fields[0], fields[1:]
        counts[length] += 1
        inside = set(cycle)
        items = []
        for v in cycle:
            outside = [w for w in adj[v] if w not in inside]
            if len(outside) != 1:
                raise RuntimeError("unique outside neighbour failed")
            items.extend((v, adj[v].index(outside[0])))
        rows.append(" ".join(map(str, (33 - 2 * length, length, *items))))
    payload = f"{len(adj)} {len(rows)}\n" + "\n".join(rows) + "\n"
    args.output.write_text(payload)
    report = {
        "schema": "orientation-search-instance-v1",
        "member_sha256": hashlib.sha256(member_bytes).hexdigest(),
        "census_sha256": hashlib.sha256(args.census.read_bytes()).hexdigest(),
        "vertices": len(adj),
        "constraints": len(rows),
        "cycle_counts": {str(k): counts[k] for k in (14, 15, 16)},
        "format": "required length followed by (vertex,outside-choice-type) pairs",
        "output_sha256": hashlib.sha256(payload.encode()).hexdigest(),
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
