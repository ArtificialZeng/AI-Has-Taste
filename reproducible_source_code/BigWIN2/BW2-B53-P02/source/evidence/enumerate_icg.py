#!/usr/bin/env python3
"""Exact census of ICG_n(D) for n <= 60.

This implementation uses integer bit sets for graph predicates and a canonical
DSATUR backtracker for proper 3-colour partitions.  Its JSONL output contains
one record for every legal (n,D), in deterministic order, together with a
directly checkable witness for the first exclusion predicate that applies.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import Counter, deque
from pathlib import Path


def proper_divisors(n: int) -> list[int]:
    return [d for d in range(1, n) if n % d == 0]


def graph(n: int, ds: tuple[int, ...]) -> list[int]:
    chosen = set(ds)
    adj = [0] * n
    for u in range(n):
        for v in range(u + 1, n):
            if math.gcd(v - u, n) in chosen:
                adj[u] |= 1 << v
                adj[v] |= 1 << u
    return adj


def edge_count(adj: list[int]) -> int:
    return sum(a.bit_count() for a in adj) // 2


def components(adj: list[int]) -> list[list[int]]:
    unseen = (1 << len(adj)) - 1
    out: list[list[int]] = []
    while unseen:
        start_bit = unseen & -unseen
        start = start_bit.bit_length() - 1
        unseen ^= start_bit
        q = [start]
        comp: list[int] = []
        for u in q:
            comp.append(u)
            new = adj[u] & unseen
            while new:
                b = new & -new
                new ^= b
                unseen ^= b
                q.append(b.bit_length() - 1)
        out.append(sorted(comp))
    return out


def find_triangle(adj: list[int]) -> list[int] | None:
    for u, au in enumerate(adj):
        later = au & ~((1 << (u + 1)) - 1)
        while later:
            b = later & -later
            later ^= b
            v = b.bit_length() - 1
            common = adj[u] & adj[v] & ~((1 << (v + 1)) - 1)
            if common:
                w = (common & -common).bit_length() - 1
                return [u, v, w]
    return None


def bipartite_certificate(adj: list[int]) -> tuple[list[int] | None, list[int] | None]:
    """Return (two-colouring, None) or (None, odd cycle in cyclic order)."""
    n = len(adj)
    color = [-1] * n
    parent = [-1] * n
    for root in range(n):
        if color[root] != -1:
            continue
        color[root] = 0
        q: deque[int] = deque([root])
        while q:
            u = q.popleft()
            nbrs = adj[u]
            while nbrs:
                b = nbrs & -nbrs
                nbrs ^= b
                v = b.bit_length() - 1
                if color[v] == -1:
                    color[v] = color[u] ^ 1
                    parent[v] = u
                    q.append(v)
                elif color[v] == color[u]:
                    pu: list[int] = []
                    x = u
                    while x != -1:
                        pu.append(x)
                        x = parent[x]
                    pv: list[int] = []
                    x = v
                    while x != -1:
                        pv.append(x)
                        x = parent[x]
                    pos = {x: i for i, x in enumerate(pu)}
                    j = next(i for i, x in enumerate(pv) if x in pos)
                    i = pos[pv[j]]
                    cycle = pu[: i + 1] + list(reversed(pv[:j]))
                    return None, cycle
    return color, None


def canonical_partition(colors: list[int]) -> tuple[tuple[int, ...], ...]:
    classes = []
    for c in range(3):
        classes.append(tuple(v for v, x in enumerate(colors) if x == c))
    return tuple(sorted(classes))


def three_color_partitions(adj: list[int], limit: int = 2) -> list[list[list[int]]]:
    """Enumerate canonical 3-colour partitions, stopping after ``limit``.

    Colour names are broken by order of first introduction.  Vertex choice is
    DSATUR with label-independent ties, so each unordered partition is reached
    exactly once.
    """
    n = len(adj)
    colors = [-1] * n
    found: list[tuple[tuple[int, ...], ...]] = []
    found_set: set[tuple[tuple[int, ...], ...]] = set()

    first = max(range(n), key=lambda v: (adj[v].bit_count(), -v))
    colors[first] = 0

    def choose_vertex() -> tuple[int, set[int]]:
        best_v = -1
        best_seen: set[int] = set()
        best_key = (-1, -1, 1)
        for v in range(n):
            if colors[v] != -1:
                continue
            seen: set[int] = set()
            nbrs = adj[v]
            while nbrs:
                b = nbrs & -nbrs
                nbrs ^= b
                c = colors[b.bit_length() - 1]
                if c != -1:
                    seen.add(c)
            key = (len(seen), adj[v].bit_count(), -v)
            if key > best_key:
                best_key = key
                best_v = v
                best_seen = seen
        return best_v, best_seen

    def visit(colored: int, max_used: int) -> None:
        if len(found) >= limit:
            return
        if colored == n:
            if max_used == 2:
                p = canonical_partition(colors)
                if p not in found_set:
                    found_set.add(p)
                    found.append(p)
            return
        v, forbidden = choose_vertex()
        for c in range(min(2, max_used + 1) + 1):
            if c in forbidden:
                continue
            # The only permitted new colour is the next consecutive name.
            if c > max_used + 1:
                continue
            colors[v] = c
            visit(colored + 1, max(max_used, c))
            colors[v] = -1
            if len(found) >= limit:
                return

    visit(1, 0)
    return [[list(cls) for cls in p] for p in found]


def adjacency_digest(adj: list[int]) -> str:
    h = hashlib.sha256()
    width = max(1, (len(adj) + 7) // 8)
    for row in adj:
        h.update(row.to_bytes(width, "little"))
    return h.hexdigest()


def classify(n: int, mask: int, divs: list[int]) -> dict:
    ds = tuple(d for i, d in enumerate(divs) if mask & (1 << i))
    adj = graph(n, ds)
    rec: dict = {
        "n": n,
        "mask": mask,
        "D": list(ds),
        "edges": edge_count(adj),
        "adjacency_sha256": adjacency_digest(adj),
    }
    if rec["edges"] == 0:
        rec.update(reason="edgeless")
        return rec
    comps = components(adj)
    if len(comps) != 1:
        rec.update(reason="disconnected", components=comps)
        return rec
    tri = find_triangle(adj)
    if tri is not None:
        rec.update(reason="triangle", triangle=tri)
        return rec
    two_coloring, odd_cycle = bipartite_certificate(adj)
    if two_coloring is not None:
        rec.update(reason="bipartite", bipartition=[
            [v for v, c in enumerate(two_coloring) if c == 0],
            [v for v, c in enumerate(two_coloring) if c == 1],
        ])
        return rec
    parts = three_color_partitions(adj, 2)
    rec["odd_cycle"] = odd_cycle
    if not parts:
        rec.update(reason="not_3_colorable")
    elif len(parts) > 1:
        rec.update(reason="nonunique_3_colorable", color_partitions=parts)
    else:
        rec.update(reason="qualifies", unique_color_partition=parts[0])
    return rec


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-n", type=int, default=60)
    ap.add_argument("--records", type=Path, required=True)
    ap.add_argument("--summary", type=Path, required=True)
    args = ap.parse_args()

    per_n: dict[str, dict] = {}
    total = 0
    qualifiers: list[dict] = []
    h = hashlib.sha256()
    with args.records.open("w", encoding="utf-8") as out:
        for n in range(1, args.max_n + 1):
            divs = proper_divisors(n)
            counts: Counter[str] = Counter()
            for mask in range(1 << len(divs)):
                rec = classify(n, mask, divs)
                line = json.dumps(rec, sort_keys=True, separators=(",", ":"))
                out.write(line + "\n")
                h.update((line + "\n").encode())
                counts[rec["reason"]] += 1
                total += 1
                if rec["reason"] == "qualifies":
                    qualifiers.append({
                        "n": n,
                        "D": rec["D"],
                        "partition": rec["unique_color_partition"],
                        "odd_cycle": rec["odd_cycle"],
                        "adjacency_sha256": rec["adjacency_sha256"],
                    })
            per_n[str(n)] = {
                "proper_divisors": divs,
                "pairs": 1 << len(divs),
                "reasons": dict(sorted(counts.items())),
            }
    summary = {
        "algorithm": "bitset predicates plus canonical DSATUR partition enumeration",
        "max_n": args.max_n,
        "total_pairs": total,
        "records_sha256": h.hexdigest(),
        "per_n": per_n,
        "qualifiers": qualifiers,
        "least_qualifying_order": min((q["n"] for q in qualifiers), default=None),
    }
    args.summary.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
