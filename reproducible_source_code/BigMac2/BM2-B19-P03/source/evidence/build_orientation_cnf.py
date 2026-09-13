#!/usr/bin/env python3
"""Build a transparent DIMACS encoding of the frozen orientation CSP.

Variable ``3*v+i+1`` means that vertex ``v`` chooses its ``i``-th neighbour
in the sorted adjacency list.  One positive ternary clause and three binary
clauses impose exactly one choice at each vertex.

On an L-cycle in a cubic graph, each vertex has one unique neighbour outside
the cycle.  The required upper bound on cycle-edge choices is equivalent to
at least ``33-2*L`` vertices choosing those outside neighbours.  At least k of
n literals is encoded without auxiliary variables: every (n-k+1)-subset is a
clause.  This equivalence is immediate because a violation has at least
n-k+1 false literals, and conversely.
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


def variable(v: int, w: int, adj: list[list[int]]) -> int:
    return 3 * v + adj[v].index(w) + 1


def read_cycles(path: Path, adj: list[list[int]]):
    digest = hashlib.sha256()
    counts: Counter[int] = Counter()
    seen: set[tuple[int, ...]] = set()
    with path.open("rb") as stream:
        for line_number, raw in enumerate(stream, 1):
            digest.update(raw)
            fields = [int(x) for x in raw.split()]
            if not fields:
                continue
            length, cycle = fields[0], tuple(fields[1:])
            if length not in (14, 15, 16) or len(cycle) != length:
                raise ValueError(f"bad length on census line {line_number}")
            if len(set(cycle)) != length or cycle[0] != min(cycle) or cycle[1] >= cycle[-1]:
                raise ValueError(f"noncanonical cycle on census line {line_number}")
            if cycle in seen:
                raise ValueError(f"duplicate cycle on census line {line_number}")
            seen.add(cycle)
            for i, v in enumerate(cycle):
                if cycle[(i + 1) % length] not in adj[v]:
                    raise ValueError(f"nonedge on census line {line_number}")
            counts[length] += 1
            yield cycle
    read_cycles.digest = digest.hexdigest()
    read_cycles.counts = counts


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    parser.add_argument("member")
    parser.add_argument("census", type=Path)
    parser.add_argument("cnf", type=Path)
    parser.add_argument("report", type=Path)
    args = parser.parse_args()

    with zipfile.ZipFile(args.archive) as zf:
        member_bytes = zf.read(args.member)
    adj = decode_graph6(member_bytes)
    if len(adj) != 812 or any(len(nbrs) != 3 for nbrs in adj):
        raise RuntimeError("the input is not the frozen 812-vertex cubic graph")
    for nbrs in adj:
        nbrs.sort()

    # Consume once to validate and obtain exact cycle counts before the header.
    cycles = list(read_cycles(args.census, adj))
    census_digest = read_cycles.digest
    counts = read_cycles.counts
    vertex_clauses = 4 * len(adj)
    cycle_clauses = sum(
        math.comb(length, 3 * length - 32) * counts[length]
        for length in (14, 15, 16)
    )
    clauses = vertex_clauses + cycle_clauses
    variables = 3 * len(adj)

    cnf_hash = hashlib.sha256()
    with args.cnf.open("wb") as out:
        def emit(text: str) -> None:
            raw = text.encode("ascii")
            out.write(raw)
            cnf_hash.update(raw)

        emit("c frozen AGL(1,29) H15 orientation CSP\n")
        emit("c variable 3*v+i+1: vertex v chooses sorted_neighbor[v][i]\n")
        emit("c cycle clauses require at least 33-2L outside choices\n")
        emit(f"p cnf {variables} {clauses}\n")
        for v, nbrs in enumerate(adj):
            lits = [variable(v, w, adj) for w in nbrs]
            emit(" ".join(map(str, lits)) + " 0\n")
            for a, b in itertools.combinations(lits, 2):
                emit(f"-{a} -{b} 0\n")
        for cycle in cycles:
            length = len(cycle)
            outside = []
            for i, v in enumerate(cycle):
                cycle_nbrs = {cycle[i - 1], cycle[(i + 1) % length]}
                external = [w for w in adj[v] if w not in cycle_nbrs]
                if len(external) != 1:
                    raise RuntimeError("cubic outside-neighbour invariant failed")
                outside.append(variable(v, external[0], adj))
            subset_size = 3 * length - 32
            for subset in itertools.combinations(outside, subset_size):
                emit(" ".join(map(str, subset)) + " 0\n")

    report = {
        "schema": "orientation-cnf-v1",
        "member": args.member,
        "member_sha256": hashlib.sha256(member_bytes).hexdigest(),
        "census_file": args.census.as_posix(),
        "census_sha256": census_digest,
        "cycle_counts": {str(k): counts[k] for k in (14, 15, 16)},
        "variable_semantics": "3*v+i+1 iff v chooses sorted adjacency entry i",
        "cycle_semantics": "at least 33-2L unique outside-neighbour literals true",
        "cardinality_encoding": "all subsets of size n-k+1 are positive clauses",
        "variables": variables,
        "clauses": clauses,
        "cnf_file": args.cnf.as_posix(),
        "cnf_sha256": cnf_hash.hexdigest(),
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
