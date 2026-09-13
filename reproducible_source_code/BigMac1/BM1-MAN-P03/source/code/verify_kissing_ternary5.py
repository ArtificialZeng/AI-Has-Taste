#!/usr/bin/env python3
"""Exact bitset verifier for normalized ternary kissing codes in R^5."""

from itertools import product
import hashlib
from pathlib import Path


VERTICES = [v for v in product((-1, 0, 1), repeat=5) if any(v)]
N = len(VERTICES)


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def weight(v):
    return sum(x * x for x in v)


def compatible(u, v):
    """Return <u/||u||,v/||v||> <= 1/2 using exact integers."""
    dot = sum(x * y for x, y in zip(u, v))
    if dot <= 0:
        return True
    return 4 * dot * dot <= weight(u) * weight(v)


ADJ = [0] * N
for i, u in enumerate(VERTICES):
    for j, v in enumerate(VERTICES[:i]):
        if compatible(u, v):
            ADJ[i] |= 1 << j
            ADJ[j] |= 1 << i


def maximum_clique(candidates, initial=()):
    """Tomita-style exact branch and bound with greedy coloring bounds."""
    best = list(initial)
    nodes = 0

    def color_sort(mask):
        order = []
        bounds = []
        color = 0
        remaining = mask
        while remaining:
            color += 1
            available = remaining
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                order.append(v)
                bounds.append(color)
                remaining ^= bit
                available ^= bit
                available &= ~ADJ[v]
        return order, bounds

    def expand(clique, mask):
        nonlocal best, nodes
        nodes += 1
        order, bounds = color_sort(mask)
        for pos in range(len(order) - 1, -1, -1):
            if len(clique) + bounds[pos] <= len(best):
                return
            v = order[pos]
            bit = 1 << v
            expand(clique + [v], mask & ADJ[v])
            mask &= ~bit
            if len(clique) + mask.bit_count() <= len(best):
                return
        if len(clique) > len(best):
            best = clique[:]

    expand(list(initial), candidates)
    return best, nodes


def main():
    require(N == 242, "wrong number of nonzero ternary vectors")
    d5 = [i for i, v in enumerate(VERTICES) if weight(v) == 2]
    require(len(d5) == 40, "wrong D5 root count")
    require(
        all((ADJ[u] >> v) & 1 for pos, u in enumerate(d5) for v in d5[:pos]),
        "D5 is not a kissing clique",
    )

    full, full_nodes = maximum_clique((1 << N) - 1)
    require(len(full) == 40, "global clique number is not 40")

    expected = {1: 33, 2: 40, 3: 38, 4: 35, 5: 31}
    conditioned = {}
    node_counts = {}
    for w in range(1, 6):
        canonical = next(i for i, v in enumerate(VERTICES) if weight(v) == w)
        clique, nodes = maximum_clique(ADJ[canonical], initial=(canonical,))
        conditioned[w] = len(clique)
        node_counts[w] = nodes
    require(conditioned == expected, f"conditioned maxima mismatch: {conditioned}")

    # Signed coordinate permutations act transitively on every fixed-weight shell.
    # Since all non-weight-2 conditioned maxima are below 40, every maximum code
    # is contained in the 40-element weight-2 shell, hence equals D5.
    require(all(conditioned[w] < 40 for w in (1, 3, 4, 5)),
            "equality classification failed")

    code_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print("VERIFIED: normalized nonzero {-1,0,1}^5 kissing maximum = 40")
    print("VERIFIED: the unique maximum subset is the D5 root system")
    print(f"conditioned_maxima={conditioned}")
    print(f"search_nodes_full={full_nodes} conditioned={node_counts}")
    print(f"verifier_sha256={code_hash}")


if __name__ == "__main__":
    main()
