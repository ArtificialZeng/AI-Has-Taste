#!/usr/bin/env python3
"""Fresh referee recomputation via 6^4 layerwise step permutations.

This deliberately parameterizes the necessary outdegree-one subdomain rather
than replaying either frozen 3^12 orbit-choice loop.
"""

from collections import Counter
from hashlib import sha256
from itertools import permutations, product
import json


N = 12
STEP_ORDERS = tuple(permutations((1, 2, 3)))


def cycles_of(successor: tuple[int, ...]) -> list[list[int]]:
    unseen = set(range(N))
    cycles: list[list[int]] = []
    while unseen:
        start = min(unseen)
        cycle = [start]
        unseen.remove(start)
        vertex = successor[start]
        while vertex != start:
            if vertex not in unseen:
                raise AssertionError("successor is not a permutation")
            cycle.append(vertex)
            unseen.remove(vertex)
            vertex = successor[vertex]
        cycles.append(cycle)
    return cycles


def main() -> None:
    survivors: list[dict[str, object]] = []
    types: Counter[str] = Counter()

    # order_by_layer[j][t] is the step leaving tail j+4t.  For each layer,
    # using a permutation of (1,2,3) is equivalent to selecting exactly one
    # tail for each step while also giving each tail exactly one outgoing arc.
    for order_by_layer in product(STEP_ORDERS, repeat=4):
        successor = [-1] * N
        for layer, step_order in enumerate(order_by_layer):
            for t, step in enumerate(step_order):
                tail = layer + 4 * t
                successor[tail] = (tail + step) % N

        if len(set(successor)) != N:
            continue
        successor_tuple = tuple(successor)
        cycles = cycles_of(successor_tuple)
        key = "+".join(map(str, sorted(map(len, cycles))))
        types[key] += 1
        survivors.append({"successor": list(successor_tuple), "cycles": cycles})

    survivors.sort(key=lambda item: item["successor"])
    serialized = json.dumps(
        survivors, sort_keys=True, separators=(",", ":")
    ).encode()
    result = {
        "parameterized_outdegree_one_selections": len(STEP_ORDERS) ** 4,
        "indegree_and_outdegree_one": len(survivors),
        "cycle_type_histogram": dict(sorted(types.items())),
        "hamilton_cycles": sum(len(item["cycles"]) == 1 for item in survivors),
        "canonical_degree_survivors_sha256": sha256(serialized).hexdigest(),
    }
    assert result == {
        "parameterized_outdegree_one_selections": 1296,
        "indegree_and_outdegree_one": 15,
        "cycle_type_histogram": {"4+8": 3, "6+6": 12},
        "hamilton_cycles": 0,
        "canonical_degree_survivors_sha256": (
            "b36456535b5da51566823d0c7781e5d398dd6beb8a4f85ce21a347d181a6f77b"
        ),
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
