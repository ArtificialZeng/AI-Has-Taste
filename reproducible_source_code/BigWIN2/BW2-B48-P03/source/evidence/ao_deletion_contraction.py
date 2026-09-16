#!/usr/bin/env python3
"""Exact acyclic-orientation count by deletion--contraction.

The core recurrence is a(G)=a(G-e)+a(G/e), with loops discarded and parallel
edges simplified after contraction.  Exact block factorization and the
simplicial-vertex identity a(G)=(deg(v)+1)a(G-v) are used as reductions.  The
implementation is independent of evidence/chromatic_fk_transfer.py and never
constructs a chromatic polynomial.
"""

from functools import lru_cache
import argparse


def grid_edges(rows, cols):
    edges = []
    for c in range(cols):
        for r in range(rows - 1):
            edges.append((c * rows + r, c * rows + r + 1))
    for c in range(cols - 1):
        for r in range(rows):
            edges.append((c * rows + r, (c + 1) * rows + r))
    return tuple(sorted(edges))


def adjacency(edges):
    adj = {}
    for u, v in edges:
        adj.setdefault(u, set()).add(v)
        adj.setdefault(v, set()).add(u)
    return adj


def biconnected_edge_blocks(edges):
    """Tarjan edge-stack algorithm; return tuples of edges in all blocks."""
    adj = adjacency(edges)
    disc, low, parent = {}, {}, {}
    stack = []
    blocks = []
    clock = 0

    def dfs(u):
        nonlocal clock
        clock += 1
        disc[u] = low[u] = clock
        for v in sorted(adj[u]):
            e = (min(u, v), max(u, v))
            if v not in disc:
                parent[v] = u
                stack.append(e)
                dfs(v)
                low[u] = min(low[u], low[v])
                if low[v] >= disc[u]:
                    block = []
                    while True:
                        x = stack.pop()
                        block.append(x)
                        if x == e:
                            break
                    blocks.append(tuple(sorted(block)))
            elif parent.get(u) != v and disc[v] < disc[u]:
                stack.append(e)
                low[u] = min(low[u], disc[v])

    for u in sorted(adj):
        if u not in disc:
            dfs(u)
            assert not stack
    return tuple(blocks)


def contract(edges, u, v):
    """Contract v into u (the smaller endpoint) and simplify parallel edges."""
    assert u < v
    out = set()
    for a, b in edges:
        a = u if a == v else a
        b = u if b == v else b
        if a != b:
            out.add((min(a, b), max(a, b)))
    return tuple(sorted(out))


calls = 0
cache_hits_at_start = 0


@lru_cache(maxsize=None)
def ao(edges):
    global calls
    calls += 1
    if not edges:
        return 1

    # Orientations of distinct blocks are independent, including bridge blocks.
    blocks = biconnected_edge_blocks(edges)
    if len(blocks) > 1:
        ans = 1
        for block in blocks:
            ans *= ao(block)
        return ans

    adj = adjacency(edges)
    # Removing a simplicial vertex exposes no additional cyclic constraint;
    # it has deg(v)+1 insertion positions in any topological color order.
    for v in sorted(adj, key=lambda x: (len(adj[x]), x)):
        nbr = sorted(adj[v])
        if all((min(a, b), max(a, b)) in edges
               for i, a in enumerate(nbr) for b in nbr[i + 1:]):
            reduced = tuple(e for e in edges if v not in e)
            return (len(nbr) + 1) * ao(reduced)

    # Prefer an edge in many short cycles (large common neighbourhood), then
    # low endpoint degree.  The choice changes cost, never the recurrence.
    def score(e):
        u, v = e
        common = len(adj[u] & adj[v])
        return (common, -(len(adj[u]) + len(adj[v])), -u, -v)

    e = max(edges, key=score)
    deleted = tuple(x for x in edges if x != e)
    contracted = contract(edges, *e)
    return ao(deleted) + ao(contracted)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--rows", type=int, default=3)
    ap.add_argument("--cols", type=int, default=9)
    args = ap.parse_args()
    edges = grid_edges(args.rows, args.cols)
    value = ao(edges)
    info = ao.cache_info()
    print(f"graph=P_{args.rows} square P_{args.cols}")
    print(f"vertices={args.rows * args.cols}")
    print(f"edges={len(edges)}")
    print("vertex_numbering=(column*rows+row), zero_based")
    print("edge_list=" + repr(list(edges)))
    print(f"acyclic_orientations={value}")
    print(f"acyclic_orientations_mod_4={value % 4}")
    print(f"deletion_contraction_unique_states={calls}")
    print(f"cache_hits={info.hits}")


if __name__ == "__main__":
    main()
