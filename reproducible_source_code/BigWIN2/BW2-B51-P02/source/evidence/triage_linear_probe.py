"""Deterministic heuristic probe for a 4-dimensional linear code.

Each 24-bit integer encodes an edge subset in the order printed on success.
Connectivity tests are exact. Failure to find a witness is not an upper bound.
"""

import random


SEED = 5102
TRIALS = 1_000_000
VERTICES = [(i, j) for i in range(3) for j in range(4)]
INDEX = {v: k for k, v in enumerate(VERTICES)}
EDGES = []
for i in range(3):
    for j in range(4):
        EDGES.append((INDEX[(i, j)], INDEX[((i + 1) % 3, j)]))
for i in range(3):
    for j in range(4):
        EDGES.append((INDEX[(i, j)], INDEX[(i, (j + 1) % 4)]))
assert len(EDGES) == 24
assert len({tuple(sorted(edge)) for edge in EDGES}) == 24


def connected(mask):
    adjacency = [0] * 12
    for k, (u, v) in enumerate(EDGES):
        if (mask >> k) & 1:
            adjacency[u] |= 1 << v
            adjacency[v] |= 1 << u
    seen = 1
    frontier = 1
    while frontier:
        neighbors = 0
        pending = frontier
        while pending:
            bit = pending & -pending
            u = bit.bit_length() - 1
            pending -= bit
            neighbors |= adjacency[u]
        frontier = neighbors & ~seen
        seen |= frontier
    return seen == (1 << 12) - 1


rng = random.Random(SEED)
for trial in range(1, TRIALS + 1):
    generators = [rng.getrandbits(24) for _ in range(4)]
    words = []
    for coefficients in range(1, 16):
        word = 0
        for k in range(4):
            if (coefficients >> k) & 1:
                word ^= generators[k]
        if not connected(word):
            break
        words.append(word)
    else:
        if len(set(words)) == 15:
            print(f"witness at trial {trial}")
            print("edges", EDGES)
            print("generators", [f"{x:06x}" for x in generators])
            print("weights", [x.bit_count() for x in words])
            break
else:
    print(f"no witness in {TRIALS} trials with seed {SEED}")
