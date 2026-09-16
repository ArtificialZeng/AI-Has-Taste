#!/usr/bin/env python3
"""Independent exhaustive replay checker for q4_strategy.json.gz.

This file deliberately does not import the solver.  It reconstructs the graph,
enumerates its automorphisms via graph isomorphism, and canonicalizes by direct
enumeration of all four-colour renamings.
"""

from __future__ import annotations

import argparse
import gzip
import hashlib
import itertools
import json
from collections import Counter
from pathlib import Path

import networkx as nx

VERTICES = tuple((m, i) for m in range(4) for i in range(3)) + ("omega",)
INDEX = {v: i for i, v in enumerate(VERTICES)}
N = len(VERTICES)
Q = 4
EMPTY = 4


def reconstruct_graph() -> nx.Graph:
    g = nx.Graph()
    g.add_nodes_from(VERTICES)
    for i in range(3):
        for j in range(i + 1, 3):
            g.add_edge((0, i), (0, j))
    for layer in range(3):
        for i in range(3):
            for j in range(3):
                if i != j:
                    g.add_edge((layer, i), (layer + 1, j))
    for i in range(3):
        g.add_edge((3, i), "omega")
    return g


G = reconstruct_graph()
NEIGHBORS = tuple(tuple(INDEX[w] for w in G.neighbors(v)) for v in VERTICES)


def enumerate_automorphisms() -> tuple[tuple[int, ...], ...]:
    maps = []
    matcher = nx.algorithms.isomorphism.GraphMatcher(G, G)
    for mapping in matcher.isomorphisms_iter():
        maps.append(tuple(INDEX[mapping[v]] for v in VERTICES))
    maps.sort()
    if len(maps) != len(set(maps)):
        raise AssertionError("automorphism enumerator produced duplicates")
    return tuple(maps)


AUTOMORPHISMS = enumerate_automorphisms()  # old index -> new index
COLOR_PERMUTATIONS = tuple(itertools.permutations(range(Q)))


def canonical(position: tuple[int, ...]) -> tuple[int, ...]:
    # A direct 6*24 orbit enumeration, independent of the solver's
    # first-occurrence normalization implementation.
    best = None
    for vertex_map in AUTOMORPHISMS:
        moved = [EMPTY] * N
        for old, new in enumerate(vertex_map):
            moved[new] = position[old]
        for color_map in COLOR_PERMUTATIONS:
            candidate = tuple(EMPTY if c == EMPTY else color_map[c] for c in moved)
            if best is None or candidate < best:
                best = candidate
    if best is None:
        raise AssertionError("empty symmetry orbit")
    return best


def is_proper(position: tuple[int, ...]) -> bool:
    return all(
        position[INDEX[a]] == EMPTY
        or position[INDEX[b]] == EMPTY
        or position[INDEX[a]] != position[INDEX[b]]
        for a, b in G.edges()
    )


def forbidden(position: tuple[int, ...], v: int) -> set[int]:
    return {position[w] for w in NEIGHBORS[v] if position[w] != EMPTY}


def terminal_winner(position: tuple[int, ...]) -> str | None:
    if EMPTY not in position:
        return "alice"
    if any(position[v] == EMPTY and len(forbidden(position, v)) == Q for v in range(N)):
        return "bob"
    return None


def legal_moves(position: tuple[int, ...]):
    for v in range(N):
        if position[v] == EMPTY:
            unavailable = forbidden(position, v)
            for color in range(Q):
                if color not in unavailable:
                    child = list(position)
                    child[v] = color
                    yield v, color, canonical(tuple(child))


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def verify(certificate_path: Path) -> dict:
    with gzip.open(certificate_path, "rt", encoding="utf-8") as f:
        cert = json.load(f)

    if cert.get("format") != "M3C3-q4-strategy-v1":
        raise AssertionError("unexpected certificate format")
    if cert.get("q") != Q or cert.get("empty") != EMPTY:
        raise AssertionError("wrong q or empty marker")
    winner = cert.get("winner")
    if winner not in ("alice", "bob"):
        raise AssertionError("invalid winner")

    nodes_list = cert.get("nodes")
    if not isinstance(nodes_list, list) or not nodes_list:
        raise AssertionError("missing nodes")
    nodes = {node["id"]: node for node in nodes_list}
    if len(nodes) != len(nodes_list) or set(nodes) != set(range(len(nodes_list))):
        raise AssertionError("node IDs must be unique and consecutive")
    root_id = cert.get("root")
    if root_id not in nodes:
        raise AssertionError("missing root")

    positions: dict[int, tuple[int, ...]] = {}
    depths: Counter[int] = Counter()
    terminal_counts: Counter[str] = Counter()
    edge_count = 0
    adversary_edges = 0
    for node_id, node in nodes.items():
        position = tuple(node.get("position", ()))
        if len(position) != N or any(type(c) is not int or c < 0 or c > EMPTY for c in position):
            raise AssertionError(f"node {node_id}: invalid position encoding")
        if not is_proper(position):
            raise AssertionError(f"node {node_id}: improper coloring")
        if canonical(position) != position:
            raise AssertionError(f"node {node_id}: noncanonical position")
        positions[node_id] = position
        depths[sum(c != EMPTY for c in position)] += 1

    if positions[root_id] != (EMPTY,) * N:
        raise AssertionError("root is not the empty position")

    # Every transition is replayed, and every adversary raw move (not merely
    # one move per symmetry orbit) must occur exactly once.
    for node_id, node in nodes.items():
        position = positions[node_id]
        end = terminal_winner(position)
        moves = node.get("moves")
        if not isinstance(moves, list):
            raise AssertionError(f"node {node_id}: moves is not a list")
        if end is not None:
            terminal_counts[end] += 1
            if node.get("terminal") != end or moves:
                raise AssertionError(f"node {node_id}: wrong terminal label or outgoing move")
            continue
        if "terminal" in node:
            raise AssertionError(f"node {node_id}: spurious terminal label")
        colored = sum(c != EMPTY for c in position)
        turn = "alice" if colored % 2 == 0 else "bob"
        if node.get("turn") != turn:
            raise AssertionError(f"node {node_id}: wrong turn")

        legal = {(v, c): child for v, c, child in legal_moves(position)}
        supplied_pairs = []
        for entry in moves:
            v, c, child_id = entry.get("vertex"), entry.get("color"), entry.get("child")
            if type(v) is not int or type(c) is not int or type(child_id) is not int:
                raise AssertionError(f"node {node_id}: malformed move")
            pair = (v, c)
            if pair not in legal:
                raise AssertionError(f"node {node_id}: illegal move {pair}")
            if child_id not in positions or positions[child_id] != legal[pair]:
                raise AssertionError(f"node {node_id}: wrong canonical child for {pair}")
            if sum(x != EMPTY for x in positions[child_id]) != colored + 1:
                raise AssertionError(f"node {node_id}: transition does not increase depth by one")
            supplied_pairs.append(pair)
        edge_count += len(moves)

        if turn == winner:
            if len(moves) != 1:
                raise AssertionError(f"node {node_id}: winner must prescribe exactly one move")
        else:
            adversary_edges += len(moves)
            legal_pairs = Counter(legal.keys())
            if Counter(supplied_pairs) != legal_pairs:
                missing = sorted((legal_pairs - Counter(supplied_pairs)).elements())
                extra = sorted((Counter(supplied_pairs) - legal_pairs).elements())
                raise AssertionError(
                    f"node {node_id}: incomplete or duplicate adversary replies; "
                    f"legal={len(legal)} supplied={len(supplied_pairs)} "
                    f"missing={missing[:5]} extra={extra[:5]}"
                )

    # Evaluate the supplied acyclic strategy from leaves upward.  All children
    # at adversary nodes, and the prescribed child at winner nodes, must retain
    # the certified winner.
    certified: dict[int, str] = {}
    ids_by_depth = sorted(nodes, key=lambda i: sum(c != EMPTY for c in positions[i]), reverse=True)
    for node_id in ids_by_depth:
        node = nodes[node_id]
        end = terminal_winner(positions[node_id])
        if end is not None:
            certified[node_id] = end
        else:
            child_winners = [certified[e["child"]] for e in node["moves"]]
            if not child_winners or any(w != winner for w in child_winners):
                raise AssertionError(f"node {node_id}: strategy does not force {winner}")
            certified[node_id] = winner
    if certified[root_id] != winner:
        raise AssertionError("root winner not certified")

    return {
        "status": "verified",
        "certificate": str(certificate_path),
        "certificate_sha256": sha256(certificate_path),
        "winner": winner,
        "graph": {
            "vertices": G.number_of_nodes(),
            "edges": G.number_of_edges(),
            "degree_multiset": sorted(dict(G.degree()).values()),
            "automorphisms_independently_enumerated": len(AUTOMORPHISMS),
            "color_permutations_checked_per_automorphism": len(COLOR_PERMUTATIONS),
        },
        "strategy_dag": {
            "nodes": len(nodes),
            "edges": edge_count,
            "adversary_edges": adversary_edges,
            "nodes_by_colored_vertices": dict(sorted(depths.items())),
            "terminal_nodes": dict(sorted(terminal_counts.items())),
        },
        "checks": [
            "independent graph reconstruction",
            "independent graph-automorphism enumeration",
            "direct color-permutation canonicalization",
            "proper positions and legal moves",
            "terminal conditions",
            "canonical child reconstruction",
            "complete adversary raw-move branching",
            "winner strategy induction",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", default="evidence/q4_strategy.json.gz")
    parser.add_argument("--report", default="evidence/q4_verification.json")
    args = parser.parse_args()
    report = verify(Path(args.certificate))
    Path(args.report).write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
