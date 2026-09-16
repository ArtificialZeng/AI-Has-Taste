#!/usr/bin/env python3
"""Independent replay of the strict order-seven upper-bound search.

This checker enumerates degree vectors first and then products of row subsets
having exactly those degrees, unlike the score-pruned dense-mask traversal in
reg5_m7_enum.py. It represents Reg5 copies as ten adjacency-array indices. It
also parses and validates every reported maximizer and its T_4(7) structure.
"""

import itertools
import math
import pathlib
import re

import numba
import numpy as np

N = 7
BOUND = 186


def make_pattern_arcs():
    patterns = set()
    for support in itertools.combinations(range(N), 5):
        for image in itertools.permutations(support):
            arcs = tuple(sorted(
                image[i] * N + image[(i + delta) % 5]
                for i in range(5) for delta in (1, 2)
            ))
            patterns.add(arcs)
    assert len(patterns) == math.comb(N, 5) * 24 == 504
    return np.array(sorted(patterns), dtype=np.int64)


patterns = make_pattern_arcs()
row_choices = np.full((N, 20), -1, dtype=np.int64)
row_choice_counts = np.zeros(N, dtype=np.int64)
for degree in range(N):
    choices = [mask for mask in range(64) if mask.bit_count() == degree]
    row_choice_counts[degree] = len(choices)
    row_choices[degree, :len(choices)] = choices


@numba.njit(cache=False)
def contains_reg5(adjacency, pattern_arcs):
    for p in range(pattern_arcs.shape[0]):
        present = True
        for a in range(10):
            if adjacency[pattern_arcs[p, a]] == 0:
                present = False
                break
        if present:
            return True
    return False


@numba.njit(cache=False)
def visit_rows(row, degrees, adjacency, pattern_arcs, choices,
               choice_counts, state):
    if row == N:
        state[1] += 1
        if contains_reg5(adjacency, pattern_arcs):
            state[2] += 1
        return
    for choice_index in range(choice_counts[degrees[row]]):
        compressed = choices[degrees[row], choice_index]
        bit = 0
        for v in range(N):
            if v != row:
                adjacency[row * N + v] = (compressed >> bit) & 1
                bit += 1
        visit_rows(row + 1, degrees, adjacency, pattern_arcs, choices,
                   choice_counts, state)


@numba.njit(cache=False)
def visit_degrees(position, score, degrees, adjacency, pattern_arcs,
                  choices, choice_counts, state):
    if position == N:
        if score > BOUND:
            state[0] += 1
            visit_rows(0, degrees, adjacency, pattern_arcs, choices,
                       choice_counts, state)
        return
    for degree in range(N):
        degrees[position] = degree
        visit_degrees(position + 1, score + degree * degree, degrees,
                      adjacency, pattern_arcs, choices, choice_counts, state)


degrees = np.zeros(N, dtype=np.int64)
adjacency = np.zeros(N * N, dtype=np.uint8)
# state: strict degree vectors, strict digraphs, strict containing Reg5
state = np.zeros(3, dtype=np.int64)
visit_degrees(0, 0, degrees, adjacency, patterns, row_choices,
              row_choice_counts, state)
assert state[0] == 2_647
assert state[1] == 6_937_603
assert state[2] == state[1]

enum_log = pathlib.Path(__file__).with_name("reg5_m7_enum.log").read_text(
    encoding="utf-8")
reported_best = int(re.search(
    r"^maximum_Reg5_free_L2_out=(\d+)$", enum_log, re.M).group(1))
reported_count = int(re.search(
    r"^maximizer_count=(\d+)$", enum_log, re.M).group(1))
reported_masks = [int(value, 16) for value in re.findall(
    r"dense_hex=0x([0-9a-f]+)", enum_log)]
assert len(reported_masks) == reported_count
assert len(set(reported_masks)) == reported_count


def adjacency_from_mask(mask):
    matrix = [[0] * N for _ in range(N)]
    bit = 0
    for u in range(N):
        for v in range(N):
            if u != v:
                matrix[u][v] = (mask >> bit) & 1
                bit += 1
    return matrix


t4_count = 0
for mask in reported_masks:
    matrix = adjacency_from_mask(mask)
    objective = sum(sum(row) ** 2 for row in matrix)
    flat = np.array(sum(matrix, []), dtype=np.uint8)
    assert objective == reported_best == BOUND
    assert not contains_reg5(flat, patterns)

    missing_pairs = []
    for u in range(N):
        for v in range(u + 1, N):
            if not matrix[u][v] and not matrix[v][u]:
                missing_pairs.append((u, v))
            else:
                assert matrix[u][v] and matrix[v][u]
    components = [{u} for u in range(N)]
    for u, v in missing_pairs:
        cu = next(component for component in components if u in component)
        cv = next(component for component in components if v in component)
        if cu is not cv:
            cu.update(cv)
            components.remove(cv)
    assert sorted(map(len, components)) == [1, 2, 2, 2]
    assert len(missing_pairs) == 3
    t4_count += 1

assert t4_count == reported_count == 105
print(f"distinct_labeled_Reg5_sets={len(patterns)}")
print(f"strict_degree_vectors={state[0]}")
print(f"strict_digraphs_checked={state[1]}")
print(f"strict_digraphs_containing_Reg5={state[2]}")
print("strict_Reg5_free_digraphs=0")
print(f"replayed_maximizers={reported_count}")
print(f"all_replayed_objectives={reported_best}")
print("all_replayed_Reg5_free=true")
print("all_replayed_are_T4_7=true")
print(f"certified_upper_bound={BOUND}")
