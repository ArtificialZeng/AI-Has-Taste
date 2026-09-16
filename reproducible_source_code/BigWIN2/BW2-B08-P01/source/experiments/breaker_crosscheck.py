#!/usr/bin/env python3
"""Small independent checks using SymPy rational rank and brute 16-bit masks."""
import argparse, json
import networkx as nx
import sympy as sp
from breaker_wlp_exact import edge_masks, independent, test_graph


def brute_layers(g):
    n = g.number_of_nodes()
    adj = edge_masks(g) + [1 << i for i in range(n)]
    for i in range(n):
        adj[i] |= 1 << (n+i)
    layers = [[] for _ in range(n+1)]
    for m in range(1 << (2*n)):
        if independent(m, adj): layers[m.bit_count()].append(m)
    return layers


def sympy_ranks(layers):
    ans=[]
    for d in range(len(layers)-1):
        up={m:i for i,m in enumerate(layers[d+1])}
        M=sp.zeros(len(up),len(layers[d]))
        for j,m in enumerate(layers[d]):
            for v in range(16):
                if not (m>>v)&1 and (m|(1<<v)) in up: M[up[m|(1<<v)],j]=1
        ans.append(M.rank())
    return ans


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("graph6", nargs="+"); args=ap.parse_args()
    for g6 in args.graph6:
        g=nx.from_graph6_bytes(g6.encode()); layers=brute_layers(g)
        exact=test_graph(g6)
        assert exact["hilbert"] == list(map(len,layers))
        sr=sympy_ranks(layers)
        assert exact["ranks_Q"] == sr
        print(json.dumps({"graph6":g6,"hilbert":exact["hilbert"],"ranks":sr,"ok":True}))

if __name__ == "__main__": main()
