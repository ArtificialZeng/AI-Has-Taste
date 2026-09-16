#!/usr/bin/env python3
"""Exact exhaustive certificate for all two-valued vectors on {0,1}^4.

For every unordered nontrivial bipartition {U, V minus U}, choose the unique side U
not containing vertex (1,1,1,1).  The script expands H_4 on the ray family
x_v=a for v in U and x_v=b otherwise, and checks that all nine integer
coefficients of H_4(a,b) are nonnegative.  Thus H_4(a,b)>=0 for a,b>=0.
"""

from hashlib import sha256
from itertools import combinations, permutations, product
from math import comb, prod


VERTICES = list(product((0, 1), repeat=4))
FACET_MASKS = [sum(1 << j for j, v in enumerate(VERTICES) if v[i] == bit)
               for i in range(4) for bit in (0, 1)]


def sign(permutation):
    inversions = sum(permutation[i] > permutation[j]
                     for i in range(4) for j in range(i + 1, 4))
    return -1 if inversions % 2 else 1


SIGNED_PERMUTATIONS = [(p, sign(p)) for p in permutations(range(4))]


def normalized_volume(simplex):
    base = VERTICES[simplex[0]]
    matrix = [[VERTICES[simplex[column + 1]][row] - base[row]
               for column in range(4)] for row in range(4)]
    return abs(sum(s * prod(matrix[row][p[row]] for row in range(4))
                   for p, s in SIGNED_PERMUTATIONS))


def multiply(f, g):
    result = [0] * (len(f) + len(g) - 1)
    for i, a in enumerate(f):
        for j, b in enumerate(g):
            result[i + j] += a * b
    return result


def h_coefficients(mask, weighted_simplex_masks):
    """Coefficients of a^k b^(8-k), returned in increasing k."""
    size = mask.bit_count()
    a_coeff = [0] * 6
    for simplex_mask, volume in weighted_simplex_masks:
        a_coeff[(simplex_mask & mask).bit_count()] += volume

    b_coeff = [1]
    for facet_mask in FACET_MASKS:
        intersection = (facet_mask & mask).bit_count()
        b_coeff = multiply(b_coeff, [8 - intersection, intersection])

    t_cubed = [comb(3, k) * size**k * (16 - size)**(3 - k)
               for k in range(4)]
    at_cubed = multiply(a_coeff, t_cubed)
    at_cubed.extend([0] * (9 - len(at_cubed)))
    return tuple(b_coeff[k] - at_cubed[k] for k in range(9))


def main():
    volume_counts = {0: 0, 1: 0, 2: 0, 3: 0}
    weighted_simplex_masks = []
    for simplex in combinations(range(16), 5):
        volume = normalized_volume(simplex)
        volume_counts[volume] = volume_counts.get(volume, 0) + 1
        if volume:
            weighted_simplex_masks.append(
                (sum(1 << j for j in simplex), volume))

    if volume_counts != {0: 1360, 1: 2672, 2: 320, 3: 16}:
        raise AssertionError(f"unexpected volume distribution: {volume_counts}")

    digest = sha256()
    negative = []
    zero_count = 0
    positive_minimum = None
    tested = 0
    # Bit 15, corresponding to (1,1,1,1), is absent.  These masks are exactly
    # one representative of every unordered nontrivial bipartition.
    for mask in range(1, 1 << 15):
        coefficients = h_coefficients(mask, weighted_simplex_masks)
        # At a=b=1 the vector is all ones, independently of the bipartition.
        if sum(coefficients) != 3_014_656:
            raise AssertionError((mask, sum(coefficients)))
        digest.update(f"{mask}:".encode("ascii"))
        digest.update(",".join(map(str, coefficients)).encode("ascii"))
        digest.update(b"\n")
        tested += 1
        zero_count += sum(c == 0 for c in coefficients)
        local_positives = [c for c in coefficients if c > 0]
        if local_positives:
            candidate = min(local_positives)
            positive_minimum = candidate if positive_minimum is None else min(positive_minimum, candidate)
        if min(coefficients) < 0:
            negative.append((mask, coefficients))

    print(f"volume_distribution={volume_counts}")
    print(f"canonical_bipartitions_tested={tested}")
    print(f"coefficients_tested={tested * 9}")
    print(f"negative_coefficients={sum(sum(c < 0 for c in row) for _, row in negative)}")
    print(f"zero_coefficients={zero_count}")
    print(f"smallest_positive_coefficient={positive_minimum}")
    print("invariant_h_at_one=3014656")
    print(f"certificate_sha256={digest.hexdigest()}")
    if negative:
        print(f"first_negative={negative[0]}")
        raise SystemExit(1)
    print("certificate=PASS")


if __name__ == "__main__":
    main()
