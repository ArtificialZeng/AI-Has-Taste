#!/usr/bin/env python3
"""Exact threshold enumeration for Reg5-free digraphs on seven vertices.

The 42 possible ordered arcs are stored as seven independent six-bit rows. A
depth-first traversal prunes a partial tuple only when six outgoing arcs on
every remaining row cannot reach 186. It therefore visits exactly every
digraph whose degree-square objective is at least 186. Containment is
non-induced: one of the 504 ten-arc Reg5 masks need only be a subset.
"""

import itertools
import math

import numba
import numpy as np

N = 7
THRESHOLD = 186
MAX_SCORE = N * (N - 1) ** 2


def make_patterns():
    arc_index = {}
    bit = 0
    for u in range(N):
        for v in range(N):
            if u != v:
                arc_index[u, v] = bit
                bit += 1

    masks = set()
    for support in itertools.combinations(range(N), 5):
        for image in itertools.permutations(support):
            mask = 0
            for i in range(5):
                for delta in (1, 2):
                    mask |= 1 << arc_index[image[i], image[(i + delta) % 5]]
            masks.add(mask)
    assert len(masks) == math.comb(N, 5) * 24 == 504
    return np.array(sorted(masks), dtype=np.int64)


@numba.njit(cache=False)
def visit(row, score, dense_mask, row_scores, patterns,
          candidate_hist, free_hist, maximizers, state):
    if score + (N - row) * (N - 1) ** 2 < THRESHOLD:
        return
    if row < N:
        shift = (N - 1) * row
        for row_mask in range(1 << (N - 1)):
            visit(row + 1, score + row_scores[row_mask],
                  dense_mask | (row_mask << shift), row_scores, patterns,
                  candidate_hist, free_hist, maximizers, state)
        return

    state[0] += 1
    candidate_hist[score] += 1
    for pattern in patterns:
        if dense_mask & pattern == pattern:
            state[1] += 1
            return
    free_hist[score] += 1
    if score > state[2]:
        state[2] = score
        state[3] = 1
        maximizers[0] = dense_mask
    elif score == state[2]:
        maximizers[state[3]] = dense_mask
        state[3] += 1


def generating_function_counts(row_scores):
    counts = [0] * (MAX_SCORE + 1)
    counts[0] = 1
    for _ in range(N):
        new = [0] * (MAX_SCORE + 1)
        for score, count in enumerate(counts):
            if count:
                for row_score in row_scores:
                    new[score + int(row_score)] += count
        counts = new
    return counts


patterns = make_patterns()
row_scores = np.array([mask.bit_count() ** 2 for mask in range(64)],
                      dtype=np.int64)
gf_count = generating_function_counts(row_scores)
gf_at_threshold = gf_count[THRESHOLD]
gf_strict = sum(gf_count[THRESHOLD + 1:])
gf_at_or_above = gf_at_threshold + gf_strict
assert gf_at_threshold == 439_992
assert gf_strict == 6_937_603
assert gf_at_or_above == 7_377_595

candidate_hist = np.zeros(MAX_SCORE + 1, dtype=np.int64)
free_hist = np.zeros(MAX_SCORE + 1, dtype=np.int64)
maximizers = np.zeros(gf_at_threshold, dtype=np.int64)
# state: tested, containing, best free score, number of maximizers
state = np.array([0, 0, -1, 0], dtype=np.int64)
visit(0, 0, 0, row_scores, patterns, candidate_hist, free_hist,
      maximizers, state)

assert state[0] == gf_at_or_above
assert all(candidate_hist[s] == 0 for s in range(THRESHOLD))
assert all(candidate_hist[s] == gf_count[s]
           for s in range(THRESHOLD, MAX_SCORE + 1))
assert int(free_hist.sum()) + state[1] == state[0]
reported_maximizers = sorted(map(int, maximizers[:state[3]]))

print(f"vertices={N}")
print(f"possible_arcs={N * (N - 1)}")
print(f"full_domain_size={1 << (N * (N - 1))}")
print(f"threshold={THRESHOLD}")
print(f"distinct_labeled_Reg5_masks={len(patterns)}")
print(f"generating_function_at_threshold={gf_at_threshold}")
print(f"generating_function_strictly_above={gf_strict}")
print(f"generating_function_at_or_above={gf_at_or_above}")
print(f"digraphs_tested_at_or_above_threshold={state[0]}")
print(f"digraphs_strictly_above_threshold={gf_strict}")
print(f"containing_at_or_above_threshold={state[1]}")
print(f"Reg5_free_at_or_above_threshold={int(free_hist.sum())}")
print("candidate_objective_histogram=" + ",".join(
    f"{score}:{candidate_hist[score]}"
    for score in range(THRESHOLD, MAX_SCORE + 1)
    if candidate_hist[score]
))
print("free_objective_histogram=" + ",".join(
    f"{score}:{free_hist[score]}"
    for score in range(THRESHOLD, MAX_SCORE + 1)
    if free_hist[score]
))
print(f"maximum_Reg5_free_L2_out={state[2]}")
print(f"maximizer_count={state[3]}")
for i, mask in enumerate(reported_maximizers):
    degrees = tuple(((mask >> (6 * u)) & 63).bit_count() for u in range(N))
    print(f"maximizer_{i}_dense_hex=0x{mask:011x}")
    print(f"maximizer_{i}_outdegrees=" + ",".join(map(str, degrees)))
