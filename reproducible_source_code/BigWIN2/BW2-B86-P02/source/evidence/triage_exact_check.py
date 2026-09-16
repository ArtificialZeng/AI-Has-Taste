#!/usr/bin/env python3
"""Exact finite check for the (n,t)=(4,1) Cayley graph.

Only integer/tuple operations from the Python standard library are used.
Permutations are tuples of images of 1,2,3,4 and composition is functional.
"""

from itertools import permutations


N = 4
S4 = tuple(permutations(range(1, N + 1)))
IDENTITY = tuple(range(1, N + 1))


def compose(p, q):
    """Return p after q."""
    return tuple(p[q[i] - 1] for i in range(N))


def inverse(p):
    ans = [0] * N
    for i, image in enumerate(p, 1):
        ans[image - 1] = i
    return tuple(ans)


def parity(p):
    return sum(p[i] > p[j] for i in range(N) for j in range(i + 1, N)) % 2


def fixed_points(p):
    return sum(image == i for i, image in enumerate(p, 1))


def cycle_string(p):
    seen = set()
    cycles = []
    for start in range(1, N + 1):
        if start in seen or p[start - 1] == start:
            seen.add(start)
            continue
        cycle = []
        x = start
        while x not in seen:
            seen.add(x)
            cycle.append(x)
            x = p[x - 1]
        cycles.append("(" + "".join(map(str, cycle)) + ")")
    return "()" if not cycles else "".join(cycles)


F1 = frozenset(p for p in S4 if fixed_points(p) == 1)
A4 = frozenset(p for p in S4 if parity(p) == 0)
V4 = frozenset(
    {
        IDENTITY,
        (2, 1, 4, 3),  # (12)(34)
        (3, 4, 1, 2),  # (13)(24)
        (4, 3, 2, 1),  # (14)(23)
    }
)

assert len(S4) == 24 and len(A4) == 12 and len(V4) == 4
assert all(inverse(s) in F1 for s in F1)
assert F1 == A4 - V4

# Pan's left-Cayley convention: g is adjacent to s*g for s in F1.
neighbors = {g: frozenset(compose(s, g) for s in F1) for g in S4}
assert all(g not in neighbors[g] for g in S4)
assert all((h in neighbors[g]) == (g in neighbors[h]) for g in S4 for h in S4)


def components():
    unseen = set(S4)
    result = []
    while unseen:
        root = min(unseen)
        reached = {root}
        frontier = [root]
        unseen.remove(root)
        while frontier:
            g = frontier.pop()
            for h in neighbors[g]:
                if h in unseen:
                    unseen.remove(h)
                    reached.add(h)
                    frontier.append(h)
        result.append(frozenset(reached))
    return tuple(sorted(result, key=lambda c: (parity(min(c)), min(c))))


COMPONENTS = components()
assert len(COMPONENTS) == 2
assert sorted(map(len, COMPONENTS)) == [12, 12]
assert {frozenset(p for p in S4 if parity(p) == e) for e in (0, 1)} == set(COMPONENTS)


def v4_cosets(component):
    unseen = set(component)
    cosets = []
    while unseen:
        g = min(unseen)
        coset = frozenset(compose(v, g) for v in V4)
        assert coset <= component
        unseen -= coset
        cosets.append(coset)
    return tuple(sorted(cosets, key=lambda c: min(c)))


PARTITIONS = tuple(v4_cosets(component) for component in COMPONENTS)
for component, parts in zip(COMPONENTS, PARTITIONS):
    assert len(parts) == 3 and all(len(part) == 4 for part in parts)
    assert set().union(*map(set, parts)) == set(component)
    for i, part_i in enumerate(parts):
        for j, part_j in enumerate(parts):
            for g in part_i:
                for h in part_j:
                    if g != h:
                        assert (h in neighbors[g]) == (i != j)

edge_count = sum(len(neighbors[g]) for g in S4) // 2
component_edge_counts = [sum(len(neighbors[g] & component) for g in component) // 2 for component in COMPONENTS]
component_aut_order = (24**3) * 6
full_aut_order = (component_aut_order**2) * 2
pan_order = 24 * 24 * 2

print("F1 cycle types:", " ".join(sorted(cycle_string(p) for p in F1)))
print("F1 = A4 \\ V4:", F1 == A4 - V4)
print("degrees:", sorted({len(neighbors[g]) for g in S4}))
print("component sizes:", [len(c) for c in COMPONENTS])
print("component parities:", [sorted({parity(g) for g in c}) for c in COMPONENTS])
for index, parts in enumerate(PARTITIONS, 1):
    rendered = ["{" + ",".join(sorted(cycle_string(p) for p in part)) + "}" for part in parts]
    print(f"component {index} V4-cosets:", " | ".join(rendered))
print("component edge counts:", component_edge_counts)
print("total edge count:", edge_count)
print("verified graph: 2 K_{4,4,4}")
print("Aut(K_{4,4,4}) order = (4!)^3 3! =", component_aut_order)
print("Aut(2 K_{4,4,4}) order = ((4!)^3 3!)^2 2! =", full_aut_order)
print("Pan conjectured group order at n=4 = 2(4!)^2 =", pan_order)
