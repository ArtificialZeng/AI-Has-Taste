#!/usr/bin/env python3
"""Exact unsymmetrized horizon-9 solver for the 4x4 transversal game.

The exported certificate is a positional O policy.  Its graph is implicit:
from every reachable X state all legal moves are edges, while from every
reachable nonterminal O state the certificate gives one edge.  No board
symmetry is used by the search or by the export.
"""

from __future__ import annotations

import argparse
import itertools
import json
from functools import lru_cache
from pathlib import Path

FULL = (1 << 16) - 1
HORIZON = 9


def transversal_masks() -> tuple[int, ...]:
    return tuple(
        sum(1 << (4 * row + col) for row, col in enumerate(perm))
        for perm in itertools.permutations(range(4))
    )


TRANSVERSALS = transversal_masks()
WIN = bytearray(1 << 16)
for occupied in range(1 << 16):
    WIN[occupied] = any(occupied & t == t for t in TRANSVERSALS)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("summary", type=Path)
    args = parser.parse_args()

    o_choice: dict[tuple[int, int], int] = {}
    calls = 0

    @lru_cache(maxsize=None)
    def defend(x_mask: int, o_mask: int) -> bool:
        """Whether O can ensure X has not won by the end of ply 9."""
        nonlocal calls
        calls += 1
        if WIN[x_mask]:
            return False
        if WIN[o_mask]:
            return True
        ply = (x_mask | o_mask).bit_count()
        if ply >= HORIZON:
            return True

        free = FULL ^ (x_mask | o_mask)
        if ply % 2 == 0:  # X to move: O's defense must cover every X move.
            while free:
                bit = free & -free
                free -= bit
                if not defend(x_mask | bit, o_mask):
                    return False
            return True

        # O to move: one successful legal reply suffices.
        while free:
            bit = free & -free
            free -= bit
            if defend(x_mask, o_mask | bit):
                o_choice[(x_mask, o_mask)] = bit.bit_length() - 1
                return True
        return False

    root_value = defend(0, 0)

    # Traverse exactly the policy graph reachable from the root.  Rechecking
    # defend here is only for export; the independent verifier trusts neither.
    reachable_o: dict[tuple[int, int], int] = {}
    reached: set[tuple[int, int]] = set()
    stack = [(0, 0)]
    graph_edges = 0
    x_nodes = 0
    o_nodes = 0
    terminal_nodes = 0
    while stack:
        state = stack.pop()
        if state in reached:
            continue
        reached.add(state)
        x_mask, o_mask = state
        ply = (x_mask | o_mask).bit_count()
        if WIN[x_mask] or WIN[o_mask] or ply >= HORIZON:
            terminal_nodes += 1
            continue
        free = FULL ^ (x_mask | o_mask)
        if ply % 2 == 0:
            x_nodes += 1
            while free:
                bit = free & -free
                free -= bit
                child = (x_mask | bit, o_mask)
                if root_value and not defend(*child):
                    raise RuntimeError("inconsistent successful root policy")
                graph_edges += 1
                stack.append(child)
        else:
            o_nodes += 1
            if not root_value:
                raise RuntimeError("witness export is not implemented for a false root")
            move = o_choice[(x_mask, o_mask)]
            bit = 1 << move
            reachable_o[state] = move
            graph_edges += 1
            stack.append((x_mask, o_mask | bit))

    policy = [
        {"x_mask": x_mask, "o_mask": o_mask, "move": move}
        for (x_mask, o_mask), move in sorted(reachable_o.items())
    ]
    certificate = {
        "format": "transversal-4x4-horizon-policy-v1",
        "horizon": HORIZON,
        "root_x_mask": 0,
        "root_o_mask": 0,
        "conclusion": "O_defends_through_ply_9" if root_value else "X_forces_by_ply_9",
        "cell_index": "4*row+column, with rows and columns numbered 0..3",
        "policy": policy,
    }
    args.certificate.write_text(json.dumps(certificate, separators=(",", ":")) + "\n")

    cache = defend.cache_info()
    summary = {
        "solver": "exact unsymmetrized AND-OR search",
        "horizon": HORIZON,
        "transversal_count": len(TRANSVERSALS),
        "root_defense_value": root_value,
        "evaluated_distinct_states": cache.currsize,
        "recursive_cache_hits": cache.hits,
        "recursive_calls_on_new_states": calls,
        "reachable_policy_states": len(reached),
        "reachable_x_nodes": x_nodes,
        "reachable_o_nodes": o_nodes,
        "reachable_terminal_nodes": terminal_nodes,
        "reachable_graph_edges": graph_edges,
        "exported_o_choices": len(policy),
    }
    args.summary.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
