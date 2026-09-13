#!/usr/bin/env python3
"""Build symmetry-restricted orientation CNFs for diagnostic SAT attacks.

The Cayley labels are affine maps (a,b), index (a-1)*29+b.  A coloring
(choice of right generator t,g,g^-1) invariant under a left subgroup is still
a legitimate full orientation.  This script identifies vertices in each left
subgroup orbit, deduplicates the resulting clauses, and emits the quotient.
It does not assert that every unrestricted solution has such symmetry.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import zipfile
from pathlib import Path

from cycle_census import decode_graph6

P = 29
T = (28, 0)
G = (3, 1)
GI = (10, 19)
GENERATORS = (T, G, GI)


def pair(v: int) -> tuple[int, int]:
    return v // P + 1, v % P


def index(x: tuple[int, int]) -> int:
    a, b = x
    return (a - 1) * P + b


def mul(x: tuple[int, int], y: tuple[int, int]) -> tuple[int, int]:
    a, b = x
    c, d = y
    return a * c % P, (a * d + b) % P


def subgroup(mode: str, order: int) -> list[tuple[int, int]]:
    if mode == "translation":
        if order != 29:
            raise ValueError("the translation subgroup has order 29")
        return [(1, b) for b in range(P)]
    if 28 % order:
        raise ValueError("scaling order must divide 28")
    # 2 is primitive modulo 29; 2^(28/order) generates the requested subgroup.
    gen = pow(2, 28 // order, P)
    return [(pow(gen, j, P), 0) for j in range(order)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("archive", type=Path)
    ap.add_argument("member")
    ap.add_argument("census", type=Path)
    ap.add_argument("mode", choices=("scaling", "translation"))
    ap.add_argument("order", type=int)
    ap.add_argument("cnf", type=Path)
    ap.add_argument("map", type=Path)
    args = ap.parse_args()

    with zipfile.ZipFile(args.archive) as zf:
        adj = decode_graph6(zf.read(args.member))
    H = subgroup(args.mode, args.order)
    orbit_of = [-1] * len(adj)
    orbits = []
    for v in range(len(adj)):
        if orbit_of[v] >= 0:
            continue
        orb = sorted({index(mul(h, pair(v))) for h in H})
        oid = len(orbits)
        for w in orb:
            if orbit_of[w] not in (-1, oid):
                raise RuntimeError("left orbits overlap")
            orbit_of[w] = oid
        orbits.append(orb)
    if any(x < 0 for x in orbit_of):
        raise RuntimeError("orbit partition incomplete")

    def var(v: int, typ: int) -> int:
        return 3 * orbit_of[v] + typ + 1

    clauses: set[tuple[int, ...]] = set()
    for oid in range(len(orbits)):
        lits = tuple(3 * oid + typ + 1 for typ in range(3))
        clauses.add(lits)
        for x, y in itertools.combinations(lits, 2):
            clauses.add((-y, -x))

    cycle_count = {14: 0, 15: 0, 16: 0}
    with args.census.open() as stream:
        for raw in stream:
            f = [int(x) for x in raw.split()]
            L, cycle = f[0], f[1:]
            cycle_count[L] += 1
            outside_lits = []
            for i, v in enumerate(cycle):
                inside = {cycle[i - 1], cycle[(i + 1) % L]}
                outside = next(w for w in adj[v] if w not in inside)
                targets = [index(mul(pair(v), s)) for s in GENERATORS]
                if sorted(targets) != sorted(adj[v]):
                    raise RuntimeError("Cayley label/generator mismatch")
                typ = targets.index(outside)
                outside_lits.append(var(v, typ))
            choose = 3 * L - 32
            for sub in itertools.combinations(outside_lits, choose):
                clauses.add(tuple(sorted(set(sub))))

    ordered = sorted(clauses, key=lambda c: (len(c), c))
    with args.cnf.open("w") as out:
        out.write(f"c invariant under left {args.mode} subgroup of order {args.order}\n")
        out.write(f"p cnf {3*len(orbits)} {len(ordered)}\n")
        for clause in ordered:
            out.write(" ".join(map(str, clause)) + " 0\n")
    mapping = {
        "schema": "orientation-quotient-v1",
        "restriction": f"left-{args.mode}-subgroup-invariant",
        "subgroup_order": args.order,
        "orbit_count": len(orbits),
        "variables": 3 * len(orbits),
        "clauses": len(ordered),
        "orbits": orbits,
        "generator_types": [[28, 0], [3, 1], [10, 19]],
        "cycle_counts": {str(k): cycle_count[k] for k in (14, 15, 16)},
    }
    args.map.write_text(json.dumps(mapping, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in mapping.items() if k != "orbits"}, sort_keys=True))


if __name__ == "__main__":
    main()
