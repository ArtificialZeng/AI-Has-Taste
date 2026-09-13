#!/usr/bin/env python3
"""Build a compact, transparent CNF for the frozen orientation CSP.

Original variable ``3*v+i+1`` says that vertex ``v`` chooses its ``i``-th
neighbour in sorted order.  Each vertex has exactly one choice.

For an L-cycle, let x_1,...,x_L be its outside-neighbour choice literals.
The desired inequality is equivalent to sum(x_i) >= 33-2L.  The L=16
constraints are single clauses.  For the L=14 constraints, a definitional
dynamic-programming encoding introduces S(i,j), meaning that at least j of
the first i literals are true, and asserts S(14,5).  The recurrence is

  S(i,j) <-> S(i-1,j) or (x_i and S(i-1,j-1)),

with S(i,0)=true and S(0,j)=false.  Each equivalence is emitted as its four
standard CNF implications after simplifying constants.  Thus projection to
the original variables is exactly the stated cardinality constraint.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import zipfile
from collections import Counter
from pathlib import Path

from cycle_census import decode_graph6


def original_variable(v: int, w: int, adj: list[list[int]]) -> int:
    return 3 * v + adj[v].index(w) + 1


def read_cycles(path: Path, adj: list[list[int]]) -> tuple[list[tuple[int, ...]], str, Counter[int]]:
    digest = hashlib.sha256()
    counts: Counter[int] = Counter()
    seen: set[tuple[int, ...]] = set()
    cycles: list[tuple[int, ...]] = []
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
            cycles.append(cycle)
    return cycles, digest.hexdigest(), counts


def add_at_least_dp(
    literals: list[int],
    required: int,
    clauses: list[tuple[int, ...]],
    next_variable: int,
) -> int:
    """Append an exact DP encoding of sum(literals) >= required.

    Returns the first unused variable number.  ``None`` below denotes a
    Boolean constant: A=None is false and B=None is true in their respective
    boundary roles.
    """
    if required <= 0:
        return next_variable
    if required == 1:
        clauses.append(tuple(literals))
        return next_variable
    if required > len(literals):
        clauses.append(())
        return next_variable

    previous: dict[int, int] = {}
    for i, x_lit in enumerate(literals, 1):
        current: dict[int, int] = {}
        for j in range(1, min(i, required) + 1):
            s_var = next_variable
            next_variable += 1
            current[j] = s_var
            a_var = previous.get(j)       # false when absent
            b_var = previous.get(j - 1) if j > 1 else None  # true for j=1

            # S -> A or x.
            clauses.append((-s_var, x_lit) if a_var is None else (-s_var, a_var, x_lit))
            # S -> A or B (tautological when B is the true boundary).
            if j > 1:
                clauses.append((-s_var, b_var) if a_var is None else (-s_var, a_var, b_var))
            # A -> S (absent A is false, hence tautological).
            if a_var is not None:
                clauses.append((-a_var, s_var))
            # x and B -> S (B is true at j=1).
            clauses.append((-x_lit, s_var) if j == 1 else (-x_lit, -b_var, s_var))
        previous = current
    clauses.append((previous[required],))
    return next_variable


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
        raise RuntimeError("input is not the frozen 812-vertex cubic graph")
    for nbrs in adj:
        nbrs.sort()
    cycles, census_digest, counts = read_cycles(args.census, adj)

    original_variables = 3 * len(adj)
    next_variable = original_variables + 1
    clauses: list[tuple[int, ...]] = []
    for v, nbrs in enumerate(adj):
        choices = tuple(original_variable(v, w, adj) for w in nbrs)
        clauses.append(choices)
        for a, b in itertools.combinations(choices, 2):
            clauses.append((-a, -b))

    for cycle in cycles:
        outside_literals: list[int] = []
        inside = set(cycle)
        for v in cycle:
            outside = [w for w in adj[v] if w not in inside]
            if len(outside) != 1:
                raise RuntimeError("unique outside-neighbour invariant failed")
            outside_literals.append(original_variable(v, outside[0], adj))
        next_variable = add_at_least_dp(
            outside_literals, 33 - 2 * len(cycle), clauses, next_variable
        )

    total_variables = next_variable - 1
    cnf_hash = hashlib.sha256()
    with args.cnf.open("wb") as out:
        def emit(raw: bytes) -> None:
            out.write(raw)
            cnf_hash.update(raw)

        emit(b"c compact frozen AGL(1,29) H15 orientation CSP\n")
        emit(b"c original variable 3*v+i+1 selects sorted_neighbor[v][i]\n")
        emit(b"c auxiliary variables define exact sequential DP cardinalities\n")
        emit(f"p cnf {total_variables} {len(clauses)}\n".encode("ascii"))
        for clause in clauses:
            emit((" ".join(map(str, clause)) + " 0\n").encode("ascii"))

    report = {
        "schema": "compact-orientation-cnf-v1",
        "member": args.member,
        "member_sha256": hashlib.sha256(member_bytes).hexdigest(),
        "census_file": args.census.as_posix(),
        "census_sha256": census_digest,
        "cycle_counts": {str(k): counts[k] for k in (14, 15, 16)},
        "original_variable_semantics": "3*v+i+1 iff v chooses sorted adjacency entry i",
        "cardinality_semantics": "S(i,j) iff at least j of the first i outside-choice literals are true",
        "encoding": "definitional DP recurrence; L16 at-least-one constraints emitted directly",
        "original_variables": original_variables,
        "auxiliary_variables": total_variables - original_variables,
        "variables": total_variables,
        "clauses": len(clauses),
        "cnf_file": args.cnf.as_posix(),
        "cnf_sha256": cnf_hash.hexdigest(),
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
