#!/usr/bin/env python3
"""Generate the exact CNF for a size-k admissible subset of [n]."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path


def forbidden_triples(n: int):
    for a, b, c in itertools.combinations(range(1, n + 1), 3):
        g = math.gcd(a, b)
        if math.gcd(a, c) == g and math.gcd(b, c) == g:
            yield a, b, c


def build(n: int, k: int):
    """Return clauses for forbidden triples and an exact DP cardinality circuit.

    Variable x_i (1 <= i <= n) selects i.  Variable s(i,j) represents
    'at least j of x_1,...,x_i are true'.  Every recurrence is encoded as an
    equivalence, and s(n,k) is asserted.
    """
    clauses = [[-a, -b, -c] for a, b, c in forbidden_triples(n)]
    next_var = n
    s = {}
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            next_var += 1
            s[i, j] = next_var
            z = next_var
            if j == 1:
                if i == 1:
                    clauses += [[-z, i], [-i, z]]
                else:
                    a = s[i - 1, 1]
                    clauses += [[-z, a, i], [-a, z], [-i, z]]
            elif j == i:
                a = s[i - 1, j - 1]
                clauses += [[-z, a], [-z, i], [-a, -i, z]]
            else:
                a, b = s[i - 1, j], s[i - 1, j - 1]
                # z <-> a OR (b AND x_i)
                clauses += [[-z, a, b], [-z, a, i], [-a, z], [-b, -i, z]]
    clauses.append([s[n, k]])
    return next_var, clauses


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, required=True)
    ap.add_argument("--k", type=int, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--meta", type=Path)
    args = ap.parse_args()
    nv, clauses = build(args.n, args.k)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="ascii", newline="\n") as f:
        f.write(f"p cnf {nv} {len(clauses)}\n")
        for clause in clauses:
            f.write(" ".join(map(str, clause)) + " 0\n")
    digest = hashlib.sha256(args.output.read_bytes()).hexdigest()
    meta = {"n": args.n, "k": args.k, "variables": nv,
            "clauses": len(clauses), "cnf_sha256": digest}
    if args.meta:
        args.meta.parent.mkdir(parents=True, exist_ok=True)
        args.meta.write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(meta, sort_keys=True))


if __name__ == "__main__":
    main()
