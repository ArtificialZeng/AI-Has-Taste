#!/usr/bin/env python3
"""Exact feasibility check for the frozen C4 square C4 fast-robber game.

This is a small transparent attractor computation, not a compressed certificate.
Cops are represented as sorted multisets.  A cop may stay or traverse one edge;
after their simultaneous move, the robber may move to any vertex in its component
of the graph with all cop-occupied vertices deleted.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json


N = 16
VERTICES = tuple(range(N))
COORD = tuple((v // 4, v % 4) for v in VERTICES)
EDGES = tuple(
    sorted(
        {
            tuple(sorted((4 * x + y, 4 * ((x + dx) % 4) + (y + dy) % 4)))
            for x in range(4)
            for y in range(4)
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))
        }
    )
)
NEIGHBORS = tuple(
    tuple(sorted({v} | {b if a == v else a for a, b in EDGES if a == v or b == v}))
    for v in VERTICES
)
GRAPH_SHA256 = hashlib.sha256(
    json.dumps({"vertices": VERTICES, "edges": EDGES}, separators=(",", ":")).encode()
).hexdigest()
ALL = (1 << N) - 1


def component_masks(occupied: int) -> tuple[int, ...]:
    result = [0] * N
    unseen = ALL & ~occupied
    while unseen:
        seed_bit = unseen & -unseen
        frontier = seed_bit
        component = 0
        while frontier:
            bit = frontier & -frontier
            frontier ^= bit
            vertex = bit.bit_length() - 1
            component |= bit
            for neighbor in NEIGHBORS[vertex]:
                neighbor_bit = 1 << neighbor
                if unseen & neighbor_bit and not (component & neighbor_bit):
                    frontier |= neighbor_bit
        unseen &= ~component
        for vertex in VERTICES:
            if component & (1 << vertex):
                result[vertex] = component
    return tuple(result)


def solve(k: int) -> dict[str, object]:
    configurations = tuple(itertools.combinations_with_replacement(VERTICES, k))
    index = {configuration: i for i, configuration in enumerate(configurations)}
    occupied = tuple(sum(1 << vertex for vertex in set(configuration)) for configuration in configurations)
    components = tuple(component_masks(mask) for mask in occupied)
    successors: list[tuple[int, ...]] = []
    transition_count = 0
    for configuration in configurations:
        destinations = {
            tuple(sorted(destination))
            for destination in itertools.product(*(NEIGHBORS[vertex] for vertex in configuration))
        }
        successor = tuple(sorted(index[destination] for destination in destinations))
        transition_count += len(successor)
        successors.append(successor)

    # winning[i] is the bit mask of legal robber vertices from which configuration
    # i wins at the start of a cop turn.  This least fixed point is the reachability
    # attractor: one cop move must make every robber response already winning.
    winning = [0] * len(configurations)
    rounds = 0
    while True:
        good_after_move = [0] * len(configurations)
        for i in range(len(configurations)):
            good = occupied[i]  # a move onto the robber captures immediately
            for robber in VERTICES:
                if not (occupied[i] & (1 << robber)):
                    component = components[i][robber]
                    if component & ~winning[i] == 0:
                        good |= 1 << robber
            good_after_move[i] = good

        changed = False
        updated = winning.copy()
        for i, successor_list in enumerate(successors):
            good = winning[i]
            for j in successor_list:
                good |= good_after_move[j]
            good &= ~occupied[i] & ALL
            if good != winning[i]:
                updated[i] = good
                changed = True
        if not changed:
            break
        winning = updated
        rounds += 1

    winning_initial = [
        configurations[i]
        for i in range(len(configurations))
        if ((~occupied[i]) & ALL) & ~winning[i] == 0
    ]
    legal_states = sum(N - len(set(configuration)) for configuration in configurations)
    winning_states = sum(mask.bit_count() for mask in winning)
    return {
        "cop_count": k,
        "configurations": len(configurations),
        "legal_cop_turn_states": legal_states,
        "configuration_transitions": transition_count,
        "attractor_rounds": rounds,
        "winning_cop_turn_states": winning_states,
        "winning_initial_configuration_count": len(winning_initial),
        "first_winning_initial_configuration": winning_initial[0] if winning_initial else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-cops", type=int, default=4)
    args = parser.parse_args()
    report = {
        "convention": {
            "vertex_encoding": "(x,y) maps to 4*x+y for x,y in Z/4Z",
            "cop_configuration": "sorted multiset; each cop stays or moves to a neighbor simultaneously",
            "robber_response": "any vertex in the current component after deleting occupied vertices",
            "turn_state": "start of cop turn; robber vertex is unoccupied",
        },
        "graph_sha256": GRAPH_SHA256,
        "results": [solve(k) for k in range(1, args.max_cops + 1)],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
