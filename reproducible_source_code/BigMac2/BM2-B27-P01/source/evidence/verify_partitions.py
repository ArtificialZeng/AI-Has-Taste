"""Exact finite audit of the collision-profile table (corroboration only)."""

from itertools import product


def actual_profile(u, v):
    groups = {}
    for bits in product((0, 1), repeat=3):
        support = bits[0] + u * bits[1] + v * bits[2]
        hamming_weight = sum(bits)
        counts = groups.setdefault(support, [0, 0, 0, 0])
        counts[hamming_weight] += 1
    return sorted(tuple(counts) for counts in groups.values())


def profile_number(u, v):
    if (u, v) == (1, 1):
        return 1
    if (u, v) in {(1, 2), (2, 1)}:
        return 2
    if (u == 1 and v >= 3) or (v == 1 and u >= 3) or (u == v and u >= 2):
        return 3
    if (v == u + 1 and u >= 2) or (u == v + 1 and v >= 2):
        return 4
    return 5


expected = {
    1: sorted([(1, 0, 0, 0), (0, 3, 0, 0), (0, 0, 3, 0), (0, 0, 0, 1)]),
    2: sorted([(1, 0, 0, 0), (0, 2, 0, 0), (0, 1, 1, 0), (0, 0, 2, 0), (0, 0, 0, 1)]),
    3: sorted([(1, 0, 0, 0), (0, 1, 0, 0), (0, 2, 0, 0), (0, 0, 1, 0), (0, 0, 2, 0), (0, 0, 0, 1)]),
    4: sorted([(1, 0, 0, 0), (0, 1, 0, 0), (0, 1, 0, 0), (0, 1, 1, 0), (0, 0, 1, 0), (0, 0, 1, 0), (0, 0, 0, 1)]),
    5: sorted([(1, 0, 0, 0), (0, 1, 0, 0), (0, 1, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 1, 0), (0, 0, 1, 0), (0, 0, 0, 1)]),
}

representatives = {1: (1, 1), 2: (1, 2), 3: (1, 4), 4: (4, 5), 5: (3, 7)}
for case, pair in representatives.items():
    assert actual_profile(*pair) == expected[case]
    print(f"case {case}, representative {pair}: exact match")

for u in range(1, 101):
    for v in range(1, 101):
        case = profile_number(u, v)
        assert actual_profile(u, v) == expected[case], (u, v, case, actual_profile(u, v))
print("all 10000 pairs with 1 <= u,v <= 100: exact match")

