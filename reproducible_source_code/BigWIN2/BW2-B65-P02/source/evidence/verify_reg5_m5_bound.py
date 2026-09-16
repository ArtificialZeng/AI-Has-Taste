#!/usr/bin/env python3
"""Independent full-domain verification of the m=5 upper bound.

Unlike reg5_m5_enum.py, this traverses a Cartesian product of five row choices,
represents patterns as sets of ordered pairs, and focuses on the threshold 66.
"""

import itertools

N = 5
ROW_ARCS = []
ROW_SCORES = []
for u in range(N):
    heads = tuple(v for v in range(N) if v != u)
    choices = []
    scores = []
    for row_mask in range(16):
        choices.append(
            frozenset((u, v) for k, v in enumerate(heads) if row_mask & (1 << k))
        )
        scores.append(row_mask.bit_count() ** 2)
    ROW_ARCS.append(tuple(choices))
    ROW_SCORES.append(tuple(scores))


def regular_arcs(permutation):
    return frozenset(
        (permutation[u], permutation[v])
        for u in range(N)
        for v in range(N)
        if u != v and ((v - u) % N) in (1, 2)
    )


patterns = tuple({regular_arcs(p) for p in itertools.permutations(range(N))})
assert len(patterns) == 24
checked = 0
above_threshold = 0
above_threshold_containing = 0
at_threshold_free = 0

for rows in itertools.product(range(16), repeat=N):
    checked += 1
    score = sum(ROW_SCORES[u][rows[u]] for u in range(N))
    if score < 66:
        continue
    arcs = frozenset().union(*(ROW_ARCS[u][rows[u]] for u in range(N)))
    contains = any(pattern <= arcs for pattern in patterns)
    if score > 66:
        above_threshold += 1
        above_threshold_containing += contains
    elif not contains:
        at_threshold_free += 1

assert checked == 16**5 == 2**20
assert above_threshold == above_threshold_containing
assert at_threshold_free == 10
print(f"row_choice_tuples_checked={checked}")
print(f"distinct_labeled_Reg5_sets={len(patterns)}")
print(f"digraphs_with_L2_out_above_66={above_threshold}")
print(f"above_66_containing_Reg5={above_threshold_containing}")
print(f"Reg5_free_digraphs_at_66={at_threshold_free}")
print("certified_upper_bound=66")
