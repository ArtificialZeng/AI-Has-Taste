#!/usr/bin/env python3
"""Exact exhaustive WLP test for whiskered graphs supplied as graph6.

Discovery/enumeration program.  Arithmetic ranks are over Q via FLINT fmpz_mat.
The serialized per-graph output is intended to be checked independently.
"""
import argparse, hashlib, json, platform, sys, time
from pathlib import Path
import networkx as nx
from flint import fmpz_mat


def edge_masks(g):
    n = g.number_of_nodes()
    a = [0] * n
    for u, v in g.edges():
        a[u] |= 1 << v
        a[v] |= 1 << u
    return a


def independent(mask, adj):
    while mask:
        b = mask & -mask
        v = b.bit_length() - 1
        mask ^= b
        if adj[v] & mask:
            return False
    return True


def alpha_exact(adj):
    return max(m.bit_count() for m in range(1 << len(adj)) if independent(m, adj))


def whiskered_independent_layers(adj):
    """Return masks by cardinality for w(G), originals 0..n-1, leaves n..2n-1."""
    n = len(adj)
    alln = (1 << n) - 1
    layers = [[] for _ in range(n + 1)]
    for xmask in range(1 << n):
        if not independent(xmask, adj):
            continue
        allowed_y = alln ^ xmask
        y = allowed_y
        while True:
            mask = xmask | (y << n)
            layers[mask.bit_count()].append(mask)
            if y == 0:
                break
            y = (y - 1) & allowed_y
    return layers


def inclusion_matrix(lower, upper):
    ri = {m: i for i, m in enumerate(upper)}
    nr, nc = len(upper), len(lower)
    entries = [0] * (nr * nc)
    for j, m in enumerate(lower):
        width = max((x.bit_length() for x in upper), default=0)
        absent = ((1 << width) - 1) ^ m
        while absent:
            b = absent & -absent
            absent ^= b
            i = ri.get(m | b)
            if i is not None:
                entries[i * nc + j] = 1
    return fmpz_mat(nr, nc, entries)


def test_graph(g6):
    g = nx.from_graph6_bytes(g6.encode("ascii"))
    adj = edge_masks(g)
    alpha = alpha_exact(adj)
    layers = whiskered_independent_layers(adj)
    hilbert = [len(x) for x in layers]
    ranks, failure = [], None
    for d in range(g.number_of_nodes()):
        nr, nc = hilbert[d + 1], hilbert[d]
        rank = int(inclusion_matrix(layers[d], layers[d + 1]).rank())
        ranks.append(rank)
        if failure is None and rank < min(nr, nc):
            failure = {"degree": d, "rank": rank, "target_rank": min(nr, nc)}
    return {"graph6": g6, "edges": g.number_of_edges(), "alpha": alpha,
            "hilbert": hilbert, "ranks_Q": ranks, "wlp": failure is None,
            "first_failure": failure}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--only-alpha-ge", type=int, default=3)
    args = ap.parse_args()
    inp, out = Path(args.input), Path(args.output)
    total = tested = wlp = 0
    started = time.time()
    with inp.open("rb") as fi, out.open("w", encoding="utf-8") as fo:
        for raw in fi:
            if raw.startswith(b">") or not raw.strip():
                continue
            total += 1
            g6 = raw.strip().decode("ascii")
            g = nx.from_graph6_bytes(g6.encode())
            a = alpha_exact(edge_masks(g))
            if a < args.only_alpha_ge:
                continue
            rec = test_graph(g6)
            tested += 1
            wlp += int(rec["wlp"])
            fo.write(json.dumps(rec, sort_keys=True) + "\n")
            if tested % 100 == 0:
                print(json.dumps({"total_seen": total, "tested": tested, "wlp": wlp,
                                  "elapsed_s": round(time.time()-started, 3)}), flush=True)
    datahash = hashlib.sha256(out.read_bytes()).hexdigest()
    summary = {"total_graphs": total, "tested_alpha_ge": tested,
               "wlp_counterexamples": wlp, "seconds": time.time()-started,
               "output_sha256": datahash, "python": sys.version,
               "platform": platform.platform()}
    Path(str(out)+".summary.json").write_text(json.dumps(summary, indent=2)+"\n")
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
