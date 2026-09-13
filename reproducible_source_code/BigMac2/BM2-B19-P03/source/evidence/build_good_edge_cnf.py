#!/usr/bin/env python3
"""Diagnostic restriction: forbid each vertex's least-useful C14 choice.

For every vertex/incident edge, count the 14-cycles on which choosing that
edge points outside.  On the frozen graph the counts are always a permutation
of (13,13,9), so there is one uniquely inferior edge.  This builder permits
only the two count-13 choices and uses one Boolean per vertex.  SAT would be a
certificate for the unrestricted problem; UNSAT concerns only this explicitly
restricted family.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import zipfile
from collections import Counter
from pathlib import Path

from cycle_census import decode_graph6


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("archive", type=Path)
    ap.add_argument("member")
    ap.add_argument("census", type=Path)
    ap.add_argument("cnf", type=Path)
    ap.add_argument("map", type=Path)
    args = ap.parse_args()
    with zipfile.ZipFile(args.archive) as zf:
        member_bytes = zf.read(args.member)
        adj = decode_graph6(member_bytes)
    for nbrs in adj:
        nbrs.sort()
    cycles = []
    for raw in args.census.read_text().splitlines():
        f = [int(x) for x in raw.split()]
        cycles.append(f[1:])

    outside14 = [[0, 0, 0] for _ in adj]
    for cycle in cycles:
        if len(cycle) != 14:
            continue
        inside = set(cycle)
        for v in cycle:
            for typ, w in enumerate(adj[v]):
                if w not in inside:
                    outside14[v][typ] += 1
    if any(sorted(row) != [9, 13, 13] for row in outside14):
        raise RuntimeError("expected the exact (9,13,13) local count profile")
    good_types = [[i for i, value in enumerate(row) if value == 13] for row in outside14]

    clauses = []
    indicator_counts = Counter()
    for cycle in cycles:
        L = len(cycle)
        inside = set(cycle)
        indicators = []
        for v in cycle:
            outside_typ = next(i for i, w in enumerate(adj[v]) if w not in inside)
            if outside_typ == good_types[v][0]:
                indicators.append(-(v + 1))
            elif outside_typ == good_types[v][1]:
                indicators.append(v + 1)
            # The omitted bad type is identically false in this restriction.
        required = 33 - 2 * L
        if len(indicators) < required:
            clauses.append(())
            continue
        indicator_counts[(L, len(indicators))] += 1
        for subset in itertools.combinations(indicators, len(indicators) - required + 1):
            clauses.append(tuple(subset))

    with args.cnf.open("w") as out:
        out.write("c restriction to the two locally maximum C14-outside choices\n")
        out.write(f"p cnf {len(adj)} {len(clauses)}\n")
        for clause in clauses:
            out.write(" ".join(map(str, clause)) + " 0\n")
    report = {
        "schema": "good-edge-restriction-v1",
        "status_scope": "SAT proves original; UNSAT only refutes this restriction",
        "member_sha256": hashlib.sha256(member_bytes).hexdigest(),
        "variables": len(adj),
        "clauses": len(clauses),
        "local_outside_count_profile": [9, 13, 13],
        "global_max_outside_incidence": sum(max(row) for row in outside14),
        "global_required_outside_incidence": 5 * sum(len(c) == 14 for c in cycles),
        "good_types_by_vertex": good_types,
        "sorted_neighbors_by_vertex": adj,
        "cycle_indicator_histogram": {
            f"L{L}_m{m}": count for (L, m), count in sorted(indicator_counts.items())
        },
        "literal_semantics": "v+1 true selects good_types[v][1], false selects good_types[v][0]",
    }
    args.map.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k not in ("good_types_by_vertex", "sorted_neighbors_by_vertex")}, sort_keys=True))


if __name__ == "__main__":
    main()
