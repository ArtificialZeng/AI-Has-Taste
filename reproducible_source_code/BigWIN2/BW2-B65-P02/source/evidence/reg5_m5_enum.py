#!/usr/bin/env python3
"""Exhaustively enumerate all labeled loopless digraphs on five vertices.

Dense bit 4*u+k represents the k-th possible head from tail u, with the
diagonal omitted.  Containment is non-induced: a Reg5 pattern is present when
all ten of its arc bits occur in the digraph mask.
"""

import itertools

N = 5
HEADS = tuple(tuple(v for v in range(N) if v != u) for u in range(N))
ARC_INDEX = {
    (u, v): 4 * u + k
    for u in range(N)
    for k, v in enumerate(HEADS[u])
}


def regular_mask(permutation):
    mask = 0
    for u in range(N):
        for v in range(N):
            if u != v and ((v - u) % N) in (1, 2):
                mask |= 1 << ARC_INDEX[permutation[u], permutation[v]]
    return mask


def objective(mask):
    return sum(((mask >> (4 * u)) & 15).bit_count() ** 2 for u in range(N))


def matrix_rows(mask):
    for u in range(N):
        yield " ".join(
            "0" if u == v else str((mask >> ARC_INDEX[u, v]) & 1)
            for v in range(N)
        )


patterns = tuple(sorted({regular_mask(p) for p in itertools.permutations(range(N))}))
total = 1 << (N * (N - 1))
free_count = 0
containing_count = 0
best = -1
maximizers = []
histogram = [0] * 81

for mask in range(total):
    if any(mask & pattern == pattern for pattern in patterns):
        containing_count += 1
        continue
    free_count += 1
    value = objective(mask)
    histogram[value] += 1
    if value > best:
        best = value
        maximizers = [mask]
    elif value == best:
        maximizers.append(mask)

print(f"vertices={N}")
print(f"possible_arcs={N * (N - 1)}")
print(f"enumerated_digraphs={total}")
print(f"distinct_labeled_Reg5_masks={len(patterns)}")
print(f"Reg5_free_digraphs={free_count}")
print(f"Reg5_containing_digraphs={containing_count}")
print(f"partition_check={free_count + containing_count}")
print(f"maximum_L2_out={best}")
print(f"maximizer_count={len(maximizers)}")
print(f"maximum_histogram_count={histogram[best]}")
for i, mask in enumerate(maximizers):
    print(f"maximizer_{i}_dense_hex=0x{mask:05x}")
    print("\n".join(matrix_rows(mask)))
