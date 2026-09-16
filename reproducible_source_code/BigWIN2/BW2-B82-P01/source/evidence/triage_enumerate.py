#!/usr/bin/env python3
"""Independent exhaustive check of the Z_10 slice reduction for E(8,4).

This script assumes only the already-derived reduced equations
  A,D subset Z_10, |A|=8, |D|=5, 1_A * 1_D = 4.
It enumerates all 45 choices of A and all 252 choices of D, reconstructs all
ten columns A intersect (x-D) for every valid pair, and compares their union
with all 70 four-subsets of A.  It does not treat computation as a proof.
"""

from itertools import combinations

G = tuple(range(10))


def mask(xs):
    return sum(1 << x for x in xs)


def convolve(A, D, x):
    return sum((x - a) % 10 in D for a in A)


def columns(A, D):
    return tuple(
        mask(a for a in A if (x - a) % 10 in D)
        for x in G
    )


rows = []
total_valid_pairs = 0
for A_tuple in combinations(G, 8):
    A = frozenset(A_tuple)
    B = tuple(x for x in G if x not in A)
    target = {mask(C) for C in combinations(A_tuple, 4)}
    valid = []
    accessible = set()
    for D_tuple in combinations(G, 5):
        D = frozenset(D_tuple)
        if all(convolve(A, D, x) == 4 for x in G):
            cols = columns(A, D)
            assert all(c.bit_count() == 4 for c in cols)
            valid.append((mask(D), cols))
            accessible.update(cols)
    total_valid_pairs += len(valid)
    rows.append((B, valid, target, accessible))

assert len(rows) == 45
assert total_valid_pairs == 200
assert sum(bool(valid) for _, valid, _, _ in rows) == 25
assert all(len(target) == 70 for _, _, target, _ in rows)
assert not any(target <= accessible for _, _, target, accessible in rows)

print("Exhaustive Z_10 slice table")
print("A is represented by its two-point complement B; masks use bits 0,...,9.")
print("For each valid D mask, the following ten masks are reconstructed columns.")
print("A_count=45 D_per_A=252 tested_pairs=11340 valid_pairs=200")
print("valid_A_count=25 target_columns_per_A=70 exact_cover_possible=no")
for B, valid, target, accessible in rows:
    print(
        f"B={B} valid_D={len(valid)} accessible={len(accessible)} "
        f"missing={len(target-accessible)}"
    )
    for dmask, cols in valid:
        print(
            f"  D=0x{dmask:03x} columns="
            + ",".join(f"0x{c:03x}" for c in cols)
        )
