#!/usr/bin/env python3
"""Independent exhaustive replay for evidence/strategy.json.

This verifier deliberately does not import the minimax solver.  In particular,
it canonicalizes by enumerating all 6 index permutations and all 24 colour
permutations, rather than using the solver's first-occurrence normalization.
"""

import argparse
import hashlib
import itertools
import json

N = 10
Q = 4
OMEGA = 9


def expected_edges():
    result = set()
    result.update((i, j) for i in range(3) for j in range(i + 1, 3))
    for level in (0, 1):
        for i in range(3):
            for j in range(3):
                if i != j:
                    result.add((3 * level + i, 3 * (level + 1) + j))
    result.update((6 + i, OMEGA) for i in range(3))
    return tuple(sorted((min(a, b), max(a, b)) for a, b in result))


EDGES = expected_edges()
NEIGHBORS = tuple(
    tuple(w for edge in EDGES if v in edge for w in edge if w != v)
    for v in range(N)
)
INDEX_ACTIONS = tuple(itertools.permutations(range(3)))
COLOR_ACTIONS = tuple(itertools.permutations(range(1, Q + 1)))


def decode(text):
    assert isinstance(text, str) and len(text) == N
    state = tuple(int(ch) for ch in text)
    assert all(0 <= x <= Q for x in state)
    return state


def encode(state):
    return "".join(str(x) for x in state)


def independently_canonicalize(state):
    candidates = []
    for index_map in INDEX_ACTIONS:
        moved = [0] * N
        for level in range(3):
            for i in range(3):
                moved[3 * level + index_map[i]] = state[3 * level + i]
        moved[OMEGA] = state[OMEGA]
        for color_map in COLOR_ACTIONS:
            candidates.append(tuple(0 if x == 0 else color_map[x - 1] for x in moved))
    return min(candidates)


def available(state, vertex):
    forbidden = {state[w] for w in NEIGHBORS[vertex] if state[w] != 0}
    return tuple(c for c in range(1, Q + 1) if c not in forbidden)


def legal_moves(state):
    return tuple(
        (v, c)
        for v in range(N)
        if state[v] == 0
        for c in available(state, v)
    )


def independent_terminal(state):
    if all(state):
        return "all"
    if any(state[v] == 0 and len(available(state, v)) == 0 for v in range(N)):
        return "dead"
    return None


def proper(state):
    return all(state[a] == 0 or state[b] == 0 or state[a] != state[b] for a, b in EDGES)


def check_group_actions():
    edge_set = set(EDGES)
    for p in INDEX_ACTIONS:
        vertex_map = list(range(N))
        for level in range(3):
            for i in range(3):
                vertex_map[3 * level + i] = 3 * level + p[i]
        vertex_map[OMEGA] = OMEGA
        image = {tuple(sorted((vertex_map[a], vertex_map[b]))) for a, b in EDGES}
        assert image == edge_set


def verify(path):
    raw = open(path, "rb").read()
    cert = json.loads(raw)
    assert cert["format"] == "m2c3-four-color-strategy-v1"
    assert cert["colors"] == Q
    assert tuple(tuple(edge) for edge in cert["edges"]) == EDGES
    assert len(EDGES) == 18
    assert tuple(map(len, NEIGHBORS)) == (4, 4, 4, 4, 4, 4, 3, 3, 3, 3)
    assert cert["winner"] in ("Alice", "Bob")
    check_group_actions()

    records = cert["nodes"]
    by_state = {}
    for node in records:
        state = decode(node["state"])
        assert node["state"] not in by_state
        by_state[node["state"]] = node
        assert proper(state)
        assert independently_canonicalize(state) == state
        count = sum(x != 0 for x in state)
        assert node["colored"] == count
        end = independent_terminal(state)
        assert node["terminal"] == end
        expected_turn = None if end else ("Alice" if count % 2 == 0 else "Bob")
        assert node["turn"] == expected_turn
        assert isinstance(node["alice_wins"], bool)

    initial = cert["initial_state"]
    assert initial == "0" * N and initial in by_state
    reachable = set()
    stack = [initial]
    checked_edges = 0
    opponent_moves = 0
    strategy_moves = 0
    terminal_all = 0
    terminal_dead = 0
    winner = cert["winner"]
    expected_alice_label = winner == "Alice"
    while stack:
        key = stack.pop()
        if key in reachable:
            continue
        reachable.add(key)
        node = by_state[key]
        state = decode(key)
        end = node["terminal"]
        edges = node["edges"]
        assert node["alice_wins"] == expected_alice_label
        if end:
            assert edges == []
            assert end == ("all" if winner == "Alice" else "dead")
            terminal_all += end == "all"
            terminal_dead += end == "dead"
            continue

        listed = [(edge["vertex"], edge["color"]) for edge in edges]
        if node["turn"] == winner:
            assert len(listed) == 1
            strategy_moves += 1
        else:
            # Exact ordered equality also rules out omissions and duplicates.
            assert tuple(listed) == legal_moves(state)
            opponent_moves += len(listed)

        for edge in edges:
            v, c = edge["vertex"], edge["color"]
            assert isinstance(v, int) and isinstance(c, int)
            assert (v, c) in legal_moves(state)
            child_raw = list(state)
            child_raw[v] = c
            child = independently_canonicalize(tuple(child_raw))
            target = edge["to"]
            assert encode(child) == target
            assert target in by_state
            assert by_state[target]["colored"] == node["colored"] + 1
            stack.append(target)
            checked_edges += 1

    assert reachable == set(by_state)
    assert terminal_all + terminal_dead > 0
    return {
        "status": "verified",
        "winner": winner,
        "chi_g_from_source_bounds": 4 if winner == "Alice" else 5,
        "nodes": len(reachable),
        "edges_replayed": checked_edges,
        "opponent_raw_moves_covered": opponent_moves,
        "strategy_moves_checked": strategy_moves,
        "terminal_all": terminal_all,
        "terminal_dead": terminal_dead,
        "certificate_sha256": hashlib.sha256(raw).hexdigest(),
        "canonical_actions_per_state": len(INDEX_ACTIONS) * len(COLOR_ACTIONS),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", nargs="?", default="evidence/strategy.json")
    parser.add_argument("--report")
    args = parser.parse_args()
    rendered = json.dumps(verify(args.certificate), indent=2, sort_keys=True) + "\n"
    if args.report:
        with open(args.report, "w", encoding="utf-8") as f:
            f.write(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
