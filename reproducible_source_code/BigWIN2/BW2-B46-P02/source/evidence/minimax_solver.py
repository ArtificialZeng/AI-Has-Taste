#!/usr/bin/env python3
"""Exact four-colour minimax and strategy-certificate exporter for M_2(C_3).

The solver quotients only by the manifest S_3 index action and colour-name
permutations.  The exported DAG nevertheless lists every raw legal move at
the losing player's nodes, so an independent replay does not trust the
quotienting for branch coverage.
"""

from functools import lru_cache
from itertools import permutations
import argparse
import hashlib
import json
import sys
import time

N = 10
Q = 4
ROOT = 9
INDEX_PERMS = tuple(permutations(range(3)))


def graph():
    edges = set()
    for i in range(3):
        for j in range(i + 1, 3):
            edges.add((i, j))
    for layer in (0, 1):
        for i in range(3):
            for j in range(3):
                if i != j:
                    a, b = 3 * layer + i, 3 * (layer + 1) + j
                    edges.add((min(a, b), max(a, b)))
    for i in range(3):
        edges.add((6 + i, ROOT))
    adj = [set() for _ in range(N)]
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)
    return tuple(tuple(sorted(x)) for x in adj), tuple(sorted(edges))


ADJ, EDGES = graph()


def colour_normalize(s):
    table = {}
    nxt = 1
    out = []
    for x in s:
        if x == 0:
            out.append(0)
        else:
            if x not in table:
                table[x] = nxt
                nxt += 1
            out.append(table[x])
    return tuple(out)


@lru_cache(maxsize=None)
def canonical(s):
    best = None
    for p in INDEX_PERMS:
        t = [0] * N
        for layer in range(3):
            base = 3 * layer
            for i in range(3):
                t[base + p[i]] = s[base + i]
        t[ROOT] = s[ROOT]
        u = colour_normalize(t)
        if best is None or u < best:
            best = u
    return best


def available(s, v):
    used = {s[w] for w in ADJ[v] if s[w]}
    return tuple(c for c in range(1, Q + 1) if c not in used)


def terminal(s):
    if all(s):
        return "all"
    if any(s[v] == 0 and not available(s, v) for v in range(N)):
        return "dead"
    return None


def legal_moves(s):
    return tuple((v, c) for v in range(N) if s[v] == 0 for c in available(s, v))


def play(s, move):
    v, c = move
    t = list(s)
    t[v] = c
    return tuple(t)


CALLS = 0


@lru_cache(maxsize=None)
def alice_wins(s):
    global CALLS
    CALLS += 1
    end = terminal(s)
    if end == "all":
        return True
    if end == "dead":
        return False
    alice_turn = sum(x != 0 for x in s) % 2 == 0
    moves = legal_moves(s)

    # Immediate terminal moves first.  This is only an ordering optimization.
    ranked = []
    for move in moves:
        child = canonical(play(s, move))
        end_child = terminal(child)
        priority = 0 if end_child else 1
        ranked.append((priority, move, child))
    if alice_turn:
        ranked.sort(key=lambda x: (-x[0], x[1]))
        return any(alice_wins(child) for _, _, child in ranked)
    ranked.sort(key=lambda x: (x[0], x[1]))
    return all(alice_wins(child) for _, _, child in ranked)


def choose_winner_move(s, winner):
    target = winner == "Alice"
    for move in legal_moves(s):
        child = canonical(play(s, move))
        if alice_wins(child) == target:
            return move, child
    raise AssertionError("winning node has no outcome-preserving move")


def export_certificate(initial_outcome, destination):
    winner = "Alice" if initial_outcome else "Bob"
    todo = [canonical((0,) * N)]
    seen = set()
    nodes = []
    while todo:
        s = todo.pop()
        if s in seen:
            continue
        seen.add(s)
        end = terminal(s)
        count = sum(x != 0 for x in s)
        turn = None if end else ("Alice" if count % 2 == 0 else "Bob")
        node = {
            "state": "".join(map(str, s)),
            "colored": count,
            "turn": turn,
            "terminal": end,
            "alice_wins": alice_wins(s),
            "edges": [],
        }
        if not end:
            if turn == winner:
                chosen = [choose_winner_move(s, winner)]
            else:
                chosen = [(move, canonical(play(s, move))) for move in legal_moves(s)]
            for (v, c), child in chosen:
                node["edges"].append({
                    "vertex": v,
                    "color": c,
                    "to": "".join(map(str, child)),
                })
                todo.append(child)
        nodes.append(node)

    nodes.sort(key=lambda n: (n["colored"], n["state"]))
    cert = {
        "format": "m2c3-four-color-strategy-v1",
        "winner": winner,
        "initial_state": "0" * N,
        "vertices": [f"v{i+1}^{layer}" for layer in range(3) for i in range(3)] + ["omega"],
        "edges": [list(e) for e in EDGES],
        "colors": Q,
        "canonicalization": "minimum over simultaneous S3 index permutations after first-occurrence color normalization",
        "opponent_branch_policy": "every raw legal (vertex,color) move from each canonical opponent state",
        "strategy_branch_policy": "one outcome-preserving legal move from each canonical winner state",
        "nodes": nodes,
    }
    payload = json.dumps(cert, indent=2, sort_keys=True) + "\n"
    with open(destination, "w", encoding="utf-8") as f:
        f.write(payload)
    return len(nodes), len(payload), hashlib.sha256(payload.encode()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="evidence/strategy.json")
    args = parser.parse_args()
    if len(EDGES) != 18 or tuple(map(len, ADJ)) != (4, 4, 4, 4, 4, 4, 3, 3, 3, 3):
        raise AssertionError("graph construction mismatch")
    started = time.monotonic()
    initial = canonical((0,) * N)
    result = alice_wins(initial)
    elapsed = time.monotonic() - started
    node_count, byte_count, digest = export_certificate(result, args.output)
    print(json.dumps({
        "winner": "Alice" if result else "Bob",
        "chi_g": 4 if result else 5,
        "solver_states": alice_wins.cache_info().currsize,
        "canonical_cache": canonical.cache_info().currsize,
        "recursive_calls": CALLS,
        "certificate_nodes": node_count,
        "certificate_bytes": byte_count,
        "certificate_sha256": digest,
        "elapsed_seconds": elapsed,
        "output": args.output,
    }, sort_keys=True))


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
