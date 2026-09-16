#!/usr/bin/env python3
"""Small graph6 and unicyclic utilities, with no graph-library dependency."""

from __future__ import annotations

from collections import deque


def parse_graph6(line: bytes) -> tuple[int, list[list[int]], list[tuple[int, int]]]:
    """Parse graph6 for 0 <= n <= 62 and return adjacency lists and edges."""
    s = line.strip()
    if s.startswith(b">>graph6<<"):
        s = s[len(b">>graph6<<") :]
    if not s:
        raise ValueError("empty graph6 record")
    n = s[0] - 63
    if not 0 <= n <= 62:
        raise ValueError("only the one-byte graph6 order format is supported")
    bits: list[int] = []
    for ch in s[1:]:
        value = ch - 63
        if not 0 <= value < 64:
            raise ValueError("invalid graph6 character")
        bits.extend((value >> shift) & 1 for shift in range(5, -1, -1))
    needed = n * (n - 1) // 2
    if len(bits) < needed:
        raise ValueError("truncated graph6 record")
    adj = [[] for _ in range(n)]
    edges: list[tuple[int, int]] = []
    at = 0
    for j in range(1, n):
        for i in range(j):
            if bits[at]:
                adj[i].append(j)
                adj[j].append(i)
                edges.append((i, j))
            at += 1
    return n, adj, edges


def unicyclic_decomposition(
    adj: list[list[int]],
) -> tuple[list[int], set[int], list[int], list[int]]:
    """Return cyclic order, cycle set, rooted-forest parent array, DFS order."""
    n = len(adj)
    remaining_degree = [len(a) for a in adj]
    queue = deque(i for i, d in enumerate(remaining_degree) if d <= 1)
    on_cycle = [True] * n
    while queue:
        v = queue.popleft()
        if not on_cycle[v]:
            continue
        on_cycle[v] = False
        for w in adj[v]:
            if on_cycle[w]:
                remaining_degree[w] -= 1
                if remaining_degree[w] == 1:
                    queue.append(w)
    cycle_set = {i for i, yes in enumerate(on_cycle) if yes}
    if len(cycle_set) < 3:
        raise ValueError("graph is not unicyclic")
    if any(sum(w in cycle_set for w in adj[v]) != 2 for v in cycle_set):
        raise ValueError("cycle core is not a simple cycle")

    first = min(cycle_set)
    cycle = [first]
    previous = -1
    current = first
    while True:
        choices = [w for w in adj[current] if w in cycle_set and w != previous]
        if not choices:
            raise ValueError("broken cycle")
        nxt = choices[0]
        if nxt == first:
            break
        if nxt in cycle:
            raise ValueError("premature cycle closure")
        cycle.append(nxt)
        previous, current = current, nxt
    if len(cycle) != len(cycle_set):
        raise ValueError("cycle traversal missed vertices")

    parent = [-2] * n
    order: list[int] = []
    stack = list(reversed(cycle))
    for root in cycle:
        parent[root] = -1
    while stack:
        v = stack.pop()
        order.append(v)
        for w in adj[v]:
            if w in cycle_set or parent[w] != -2:
                continue
            parent[w] = v
            stack.append(w)
    if len(order) != n:
        raise ValueError("graph is disconnected")
    return cycle, cycle_set, parent, order


def structural_data(
    adj: list[list[int]], cycle: list[int]
) -> tuple[tuple[int, ...], int, int]:
    degrees = tuple(sorted((len(a) for a in adj), reverse=True))
    rooted_tree_count = sum(len(adj[v]) >= 3 for v in cycle)
    internal_edge_count = len(adj) - sum(d == 1 for d in degrees)
    return degrees, rooted_tree_count, internal_edge_count
