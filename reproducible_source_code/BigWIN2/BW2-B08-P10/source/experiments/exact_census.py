#!/usr/bin/env python3
"""Exact order-n census for the line-graph signature inequality.

Input is graph6, one graph per line.  All inertia computations use rational
congruence elimination (fractions.Fraction); no floating-point arithmetic is
used.  The 9 by 9 matrix is M=Q(G)-2I and
sig A(L(G)) = sig(M)-(|E|-|V|+1)+1.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from collections import Counter, defaultdict
from fractions import Fraction


def decode_graph6(line: bytes):
    s = line.strip()
    if s.startswith(b">>graph6<<"):
        s = s[10:]
    if not s or s[0] >= 126:
        raise ValueError("only short graph6 records (n<=62) are accepted")
    n = s[0] - 63
    bits = []
    for ch in s[1:]:
        if not 63 <= ch <= 126:
            raise ValueError("invalid graph6 byte")
        value = ch - 63
        bits.extend((value >> j) & 1 for j in range(5, -1, -1))
    need = n * (n - 1) // 2
    if len(bits) < need:
        raise ValueError("truncated graph6 record")
    edges = []
    k = 0
    # graph6 order: (0,1),(0,2),(1,2),(0,3),...
    for j in range(1, n):
        for i in range(j):
            if bits[k]:
                edges.append((i, j))
            k += 1
    return s.decode("ascii"), n, edges


def inertia_symmetric(matrix):
    """Return (positive, zero, negative) by exact congruence elimination."""
    a = [[Fraction(x) for x in row] for row in matrix]
    pos = neg = 0
    while a:
        size = len(a)
        pivot = next((i for i in range(size) if a[i][i]), None)
        if pivot is not None:
            if pivot:
                a[0], a[pivot] = a[pivot], a[0]
                for row in a:
                    row[0], row[pivot] = row[pivot], row[0]
            d = a[0][0]
            pos += d > 0
            neg += d < 0
            a = [[a[i][j] - a[i][0] * a[0][j] / d
                  for j in range(1, size)] for i in range(1, size)]
            continue
        pair = next(((i, j) for i in range(size) for j in range(i + 1, size)
                     if a[i][j]), None)
        if pair is None:
            return pos, size, neg
        i, j = pair
        order = [i, j] + [k for k in range(size) if k not in (i, j)]
        a = [[a[r][c] for c in order] for r in order]
        d = a[0][1]
        # [[0,d],[d,0]] is a hyperbolic pair.
        pos += 1
        neg += 1
        a = [[a[r][c] - (a[r][0] * a[1][c] + a[r][1] * a[0][c]) / d
              for c in range(2, size)] for r in range(2, size)]
    return pos, 0, neg


def q_minus_2(n, edges):
    a = [[0] * n for _ in range(n)]
    degree = [0] * n
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1
        a[u][v] = a[v][u] = 1
    for i, d in enumerate(degree):
        a[i][i] = d - 2
    return a


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="-", help="graph6 file, or - for stdin")
    ap.add_argument("--output", required=True)
    ap.add_argument("--expected-n", type=int, default=9)
    ap.add_argument("--retain-slack", type=int, default=2)
    args = ap.parse_args()
    stream = sys.stdin.buffer if args.input == "-" else open(args.input, "rb")
    digest = hashlib.sha256()
    totals = Counter()
    by_edges = defaultdict(Counter)
    retained = []
    for raw in stream:
        if not raw.strip() or raw.startswith(b">>"):
            continue
        digest.update(raw)
        g6, n, edges = decode_graph6(raw)
        if n != args.expected_n:
            raise ValueError(f"unexpected order {n} in {g6}")
        m = len(edges)
        p, z, q = inertia_symmetric(q_minus_2(n, edges))
        c = m - n + 1
        signature = (p - q) - c + 1
        slack = c + 1 - 2 * signature
        if slack < 0:
            status = "violation"
        elif slack == 0:
            status = "equality"
        else:
            status = "strict"
        totals[status] += 1
        by_edges[m][status] += 1
        by_edges[m][f"signature_{signature}"] += 1
        if slack <= args.retain_slack:
            retained.append({"graph6": g6, "n": n, "m": m, "c": c,
                             "inertia_Q_minus_2": [p, z, q],
                             "line_graph_signature": signature, "slack": slack})
    if stream is not sys.stdin.buffer:
        stream.close()
    result = {
        "schema_version": 1,
        "arithmetic": "fractions.Fraction exact rational congruence elimination",
        "python": platform.python_version(),
        "input_sha256": digest.hexdigest(),
        "expected_order": args.expected_n,
        "graph_count": sum(totals.values()),
        "totals": dict(sorted(totals.items())),
        "by_edges": {str(k): dict(sorted(v.items())) for k, v in sorted(by_edges.items())},
        "retained_slack_at_most": args.retain_slack,
        "retained": retained,
    }
    with open(args.output, "w", encoding="utf-8") as fh:
        json.dump(result, fh, indent=2, sort_keys=True)
        fh.write("\n")
    print(json.dumps({k: result[k] for k in ("graph_count", "totals", "input_sha256")}))


if __name__ == "__main__":
    main()
