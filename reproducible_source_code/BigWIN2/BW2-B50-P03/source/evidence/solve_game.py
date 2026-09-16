#!/usr/bin/env python3
"""Exact four-colour minimax for M_3(C_3), with a replayable strategy DAG.

The certificate contains the canonical position at every node and raw moves
from that representative.  Colour names are canonicalized by first occurrence;
the six simultaneous index permutations are used as graph automorphisms.
"""

from __future__ import annotations

import argparse
import gzip
import io
import itertools
import json
import sys
import time
from functools import lru_cache

N = 13
Q = 4
EMPTY = 4
OMEGA = 12


def vertex(m: int, i: int) -> int:
    return 3 * m + i


def build_graph() -> tuple[tuple[int, ...], tuple[tuple[int, int], ...]]:
    edges: set[tuple[int, int]] = set()

    def add(a: int, b: int) -> None:
        edges.add((a, b) if a < b else (b, a))

    for i in range(3):
        for j in range(i + 1, 3):
            add(vertex(0, i), vertex(0, j))
    for m in range(3):
        for i in range(3):
            for j in range(3):
                if i != j:
                    add(vertex(m, i), vertex(m + 1, j))
    for i in range(3):
        add(vertex(3, i), OMEGA)

    adj = [0] * N
    for a, b in edges:
        adj[a] |= 1 << b
        adj[b] |= 1 << a
    return tuple(adj), tuple(sorted(edges))


ADJ, EDGES = build_graph()


def index_automorphisms() -> tuple[tuple[int, ...], ...]:
    maps = []
    for p in itertools.permutations(range(3)):
        maps.append(tuple([vertex(m, p[i]) for m in range(4) for i in range(3)] + [OMEGA]))
    return tuple(maps)


AUTS = index_automorphisms()  # old vertex -> new vertex


def normalize_colors(s: tuple[int, ...]) -> tuple[int, ...]:
    relabel: dict[int, int] = {}
    nxt = 0
    out = []
    for c in s:
        if c == EMPTY:
            out.append(EMPTY)
        else:
            if c not in relabel:
                relabel[c] = nxt
                nxt += 1
            out.append(relabel[c])
    return tuple(out)


@lru_cache(maxsize=None)
def canonical(s: tuple[int, ...]) -> tuple[int, ...]:
    best = None
    for a in AUTS:
        t = [EMPTY] * N
        for old, new in enumerate(a):
            t[new] = s[old]
        u = normalize_colors(tuple(t))
        if best is None or u < best:
            best = u
    assert best is not None
    return best


def colour_masks(s: tuple[int, ...]) -> tuple[int, ...]:
    masks = [0] * N
    for v, c in enumerate(s):
        if c != EMPTY:
            bit = 1 << c
            nb = ADJ[v]
            while nb:
                lsb = nb & -nb
                masks[lsb.bit_length() - 1] |= bit
                nb -= lsb
    return tuple(masks)


def terminal(s: tuple[int, ...], masks: tuple[int, ...] | None = None) -> str | None:
    if EMPTY not in s:
        return "alice"
    if masks is None:
        masks = colour_masks(s)
    if any(c == EMPTY and masks[v] == (1 << Q) - 1 for v, c in enumerate(s)):
        return "bob"
    return None


def raw_moves(s: tuple[int, ...], masks: tuple[int, ...] | None = None):
    if masks is None:
        masks = colour_masks(s)
    for v, old in enumerate(s):
        if old == EMPTY:
            for c in range(Q):
                if not (masks[v] >> c) & 1:
                    t = list(s)
                    t[v] = c
                    yield v, c, canonical(tuple(t))


stats = {"calls": 0, "unique_children": 0}
choice: dict[tuple[int, ...], tuple[int, int, tuple[int, ...]]] = {}


@lru_cache(maxsize=None)
def alice_wins(s: tuple[int, ...]) -> bool:
    stats["calls"] += 1
    masks = colour_masks(s)
    end = terminal(s, masks)
    if end is not None:
        return end == "alice"

    alice_turn = (sum(c != EMPTY for c in s) % 2 == 0)
    moves = list(raw_moves(s, masks))
    # Symmetry-equivalent raw moves have the same child value.
    distinct: dict[tuple[int, ...], tuple[int, int, tuple[int, ...]]] = {}
    for move in moves:
        distinct.setdefault(move[2], move)
    stats["unique_children"] += len(distinct)

    if alice_turn:
        for move in distinct.values():
            if alice_wins(move[2]):
                choice[s] = move
                return True
        return False
    for move in distinct.values():
        if not alice_wins(move[2]):
            choice[s] = move
            return False
    return True


def strategy_nodes(root: tuple[int, ...], winner: str):
    """Traverse only the winner's strategy and every adversary raw reply."""
    ids: dict[tuple[int, ...], int] = {root: 0}
    nodes = []
    pending = [root]
    while pending:
        s = pending.pop()
        node_id = ids[s]
        masks = colour_masks(s)
        end = terminal(s, masks)
        node = {"id": node_id, "position": list(s)}
        if end is not None:
            node["terminal"] = end
            node["moves"] = []
            nodes.append(node)
            continue

        alice_turn = sum(c != EMPTY for c in s) % 2 == 0
        player = "alice" if alice_turn else "bob"
        node["turn"] = player
        all_moves = list(raw_moves(s, masks))
        if player == winner:
            picked = choice.get(s)
            if picked is None:
                # This can happen only if a cached answer was established through
                # an equivalent parent before its local representative was visited.
                target = winner == "alice"
                picked = next(m for m in all_moves if alice_wins(m[2]) == target)
            selected = [picked]
        else:
            selected = all_moves

        entries = []
        for v, c, child in selected:
            if child not in ids:
                ids[child] = len(ids)
                pending.append(child)
            entries.append({"vertex": v, "color": c, "child": ids[child]})
        node["moves"] = entries
        nodes.append(node)
    nodes.sort(key=lambda x: x["id"])
    return nodes


def write_gzip_json(path: str, obj) -> None:
    # mtime=0 and an empty stored filename make the compressed certificate
    # byte-for-byte reproducible, independently of its output pathname.
    with open(path, "wb") as destination:
        with gzip.GzipFile(
            fileobj=destination, filename="", mode="wb", compresslevel=9, mtime=0
        ) as raw:
            with io.TextIOWrapper(raw, encoding="utf-8") as f:
                json.dump(obj, f, separators=(",", ":"), sort_keys=True)
                f.write("\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="evidence/q4_strategy.json.gz")
    args = parser.parse_args()
    started = time.time()
    root = canonical((EMPTY,) * N)
    aw = alice_wins(root)
    winner = "alice" if aw else "bob"
    solved = time.time()
    print(f"winner {winner}", file=sys.stderr)
    print(f"cache_states {alice_wins.cache_info().currsize}", file=sys.stderr)
    print(f"canonical_states {canonical.cache_info().currsize}", file=sys.stderr)
    print(f"solve_seconds {solved-started:.3f}", file=sys.stderr)
    nodes = strategy_nodes(root, winner)
    certificate = {
        "format": "M3C3-q4-strategy-v1",
        "q": Q,
        "empty": EMPTY,
        "vertex_order": [f"v{m}_{i}" for m in range(4) for i in range(3)] + ["omega"],
        "root": 0,
        "winner": winner,
        "canonicalization": "lexicographic minimum over graph automorphisms after first-occurrence color normalization",
        "nodes": nodes,
    }
    write_gzip_json(args.output, certificate)
    print(f"dag_nodes {len(nodes)}", file=sys.stderr)
    print(f"dag_edges {sum(len(n['moves']) for n in nodes)}", file=sys.stderr)
    print(f"total_seconds {time.time()-started:.3f}", file=sys.stderr)


if __name__ == "__main__":
    main()
