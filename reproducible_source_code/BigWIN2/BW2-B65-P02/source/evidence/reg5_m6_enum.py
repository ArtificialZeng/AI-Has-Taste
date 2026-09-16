#!/usr/bin/env python3
"""Exact threshold enumeration for Reg5-free digraphs on six vertices.

The thirty possible arcs are stored in six independent five-bit rows.  A
depth-first traversal prunes a partial row tuple only when even filling every
remaining row cannot bring its degree-square objective to THRESHOLD.  Thus
every digraph with objective at least THRESHOLD, and no other leaf, is tested.
Containment is non-induced: a ten-arc Reg5 mask need only be a subset.
"""

import itertools
from collections import Counter

N = 6
THRESHOLD = 114
ROW_MASK = (1 << (N - 1)) - 1
HEADS = tuple(tuple(v for v in range(N) if v != u) for u in range(N))
ARC_INDEX = {
    (u, v): (N - 1) * u + k
    for u in range(N)
    for k, v in enumerate(HEADS[u])
}
ROW_SCORES = tuple(mask.bit_count() ** 2 for mask in range(1 << (N - 1)))


def regular_mask(support, permutation):
    """Return the global arc mask for one labeling on a five-set support."""
    image = tuple(support[permutation[i]] for i in range(5))
    mask = 0
    for i in range(5):
        for j in range(5):
            if i != j and ((j - i) % 5) in (1, 2):
                mask |= 1 << ARC_INDEX[image[i], image[j]]
    return mask


def matrix_rows(mask):
    for u in range(N):
        yield " ".join(
            "0" if u == v else str((mask >> ARC_INDEX[u, v]) & 1)
            for v in range(N)
        )


patterns = tuple(
    sorted(
        {
            regular_mask(support, permutation)
            for support in itertools.combinations(range(N), 5)
            for permutation in itertools.permutations(range(5))
        }
    )
)
assert len(patterns) == 6 * 24 == 144

tested_at_or_above = 0
containing_at_or_above = 0
candidate_histogram = Counter()
free_histogram = Counter()
best_free = -1
maximizers = []


def visit(row, score, global_mask):
    global tested_at_or_above, containing_at_or_above, best_free, maximizers
    if score + (N - row) * (N - 1) ** 2 < THRESHOLD:
        return
    if row == N:
        tested_at_or_above += 1
        candidate_histogram[score] += 1
        if any(global_mask & pattern == pattern for pattern in patterns):
            containing_at_or_above += 1
            return
        free_histogram[score] += 1
        if score > best_free:
            best_free = score
            maximizers = [global_mask]
        elif score == best_free:
            maximizers.append(global_mask)
        return
    shift = (N - 1) * row
    for row_mask, row_score in enumerate(ROW_SCORES):
        visit(row + 1, score + row_score, global_mask | (row_mask << shift))


visit(0, 0, 0)
assert sum(candidate_histogram.values()) == tested_at_or_above
assert sum(free_histogram.values()) + containing_at_or_above == tested_at_or_above
assert best_free == THRESHOLD

print(f"vertices={N}")
print(f"possible_arcs={N * (N - 1)}")
print(f"full_domain_size={1 << (N * (N - 1))}")
print(f"threshold={THRESHOLD}")
print(f"distinct_labeled_Reg5_masks={len(patterns)}")
print(f"digraphs_tested_at_or_above_threshold={tested_at_or_above}")
print(f"digraphs_strictly_above_threshold={sum(c for s, c in candidate_histogram.items() if s > THRESHOLD)}")
print(f"containing_at_or_above_threshold={containing_at_or_above}")
print(f"Reg5_free_at_or_above_threshold={sum(free_histogram.values())}")
print("candidate_objective_histogram=" + ",".join(f"{s}:{candidate_histogram[s]}" for s in sorted(candidate_histogram)))
print("free_objective_histogram=" + ",".join(f"{s}:{free_histogram[s]}" for s in sorted(free_histogram)))
print(f"maximum_Reg5_free_L2_out={best_free}")
print(f"maximizer_count={len(maximizers)}")

for i, mask in enumerate(sorted(maximizers)):
    degrees = tuple(
        ((mask >> ((N - 1) * u)) & ROW_MASK).bit_count() for u in range(N)
    )
    print(f"maximizer_{i}_dense_hex=0x{mask:08x}")
    print(f"maximizer_{i}_outdegrees=" + ",".join(map(str, degrees)))
    print("\n".join(matrix_rows(mask)))
