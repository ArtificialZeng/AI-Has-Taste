#!/usr/bin/env python3
"""Reproduce the published D(n), 1 <= n <= 43, by exact reduced scans."""

from functools import lru_cache
from math import isqrt

from mn_scan import beta_set, dimension, partitions, remove_hooks, beta_to_partition


PUBLISHED = (
    1, 2, 2, 2, 1, 1, 4, 1, 1, 1, 4, 1, 4, 1, 2,
    2, 1, 2, 2, 3, 1, 3, 2, 2, 2, 3, 2, 1, 3, 1,
    5, 1, 3, 1, 2, 1, 1, 1, 5, 1, 3, 1, 7,
)


@lru_cache(maxsize=None)
def mixed_character(beta, threes, twos):
    if threes:
        return sum(sign * mixed_character(new_beta, threes - 1, twos)
                   for new_beta, sign in remove_hooks(beta, 3))
    if twos:
        return sum(sign * mixed_character(new_beta, 0, twos - 1)
                   for new_beta, sign in remove_hooks(beta, 2))
    return dimension(beta_to_partition(beta))


def is_loeschian(number):
    bound = 2 * isqrt(number) + 3
    for x in range(-bound, bound + 1):
        for y in range(-bound, bound + 1):
            if x * x + x * y + y * y == number:
                return True
    return False


def s2(n):
    for s in range(n // 2 + 1):
        m = n - 2 * s
        u = (isqrt(8 * m + 1) - 1) // 2
        if u * (u + 1) // 2 == m:
            return s
    raise AssertionError


def s3(n):
    for s in range(n // 3 + 1):
        if is_loeschian(3 * (n - 3 * s) + 1):
            return s
    raise AssertionError


def zero_free(n, threes, twos, rows):
    if threes == twos == 0:
        return True
    return all(mixed_character(beta_set(lam), threes, twos) != 0 for lam in rows)


def reduced_survivors(n):
    rows = tuple(partitions(n))
    if n == 1:
        return [(0, 0, 1)]
    if n == 2:
        # The exceptional transposition column is not covered by parity reduction.
        return [(0, 0, 2), (0, 1, 0)]
    survivors = []
    for a in range(s3(n) + 1):
        for b in range(0, s2(n) + 1, 2):
            c = n - 3 * a - 2 * b
            if c >= 0 and zero_free(n, a, b, rows):
                survivors.append((a, b, c))
    return survivors


def main():
    observed = []
    survivors_43 = None
    for n in range(1, 44):
        survivors = reduced_survivors(n)
        observed.append(len(survivors))
        if n == 43:
            survivors_43 = survivors
        print(f"n={n} D={len(survivors)} expected={PUBLISHED[n-1]} match={len(survivors)==PUBLISHED[n-1]}")
    print(f"observed={tuple(observed)}")
    print(f"published={PUBLISHED}")
    print(f"survivors_43_as_(a,b,c)={survivors_43}")
    assert tuple(observed) == PUBLISHED
    assert survivors_43 == [(0, 0, 43), (0, 4, 35), (0, 8, 27),
                            (1, 2, 36), (1, 4, 32), (1, 6, 28),
                            (1, 10, 20)]
    print("table_match=all 43 values and all seven S_43 survivors passed")


if __name__ == "__main__":
    main()
