#!/usr/bin/env python3
"""Generate canonical unlabeled graph representatives through six vertices.

The NetworkX graph atlas is used only as a source of one representative per
isomorphism class.  Every representative is independently canonicalized by
trying all vertex permutations.  Edge-mask bit k corresponds to (u,v) in the
graph6 order (0,1),(0,2),(1,2),(0,3),... .
"""

from itertools import permutations
import networkx as nx


def pairs(n):
    return [(u, v) for v in range(1, n) for u in range(v)]


def encode_graph6(n, edge_bits):
    bits = [(edge_bits >> k) & 1 for k in range(n * (n - 1) // 2)]
    while len(bits) % 6:
        bits.append(0)
    payload = []
    for i in range(0, len(bits), 6):
        value = 0
        for bit in bits[i : i + 6]:
            value = (value << 1) | bit
        payload.append(chr(63 + value))
    return chr(63 + n) + "".join(payload)


def canonical_form(graph):
    n = graph.number_of_nodes()
    old_edges = {frozenset(e) for e in graph.edges()}
    best = None
    for order in permutations(range(n)):
        mask = 0
        for k, (u, v) in enumerate(pairs(n)):
            if frozenset((order[u], order[v])) in old_edges:
                mask |= 1 << k
        code = encode_graph6(n, mask)
        item = (code, mask)
        if best is None or item < best:
            best = item
    return best


def main():
    rows = []
    for graph in nx.graph_atlas_g():
        n = graph.number_of_nodes()
        if n <= 6:
            code, mask = canonical_form(graph)
            rows.append((n, code, mask))
    rows.sort()
    expected = [1, 1, 2, 4, 11, 34, 156]
    counts = [sum(n == k for n, _, _ in rows) for k in range(7)]
    assert counts == expected, (counts, expected)
    assert len({(n, code) for n, code, _ in rows}) == len(rows)
    print("n\tgraph6\tedge_mask")
    for n, code, mask in rows:
        print(f"{n}\t{code}\t{mask}")


if __name__ == "__main__":
    main()
