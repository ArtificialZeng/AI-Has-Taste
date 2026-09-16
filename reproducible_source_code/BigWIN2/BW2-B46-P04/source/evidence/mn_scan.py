#!/usr/bin/env python3
"""Exact scan of the two unresolved reduced columns for S_44.

For a beta set B of fixed cardinality r, removing a rim hook of length k
replaces x in B by x-k when x-k is nonnegative and absent.  Its MN sign is
(-1)^h, where h is the number of beta numbers strictly between x-k and x.
After all nontrivial cycles are removed, the value at the remaining 1-cycles
is the Specht-module dimension, computed by the hook-length formula.
"""

from functools import lru_cache
from hashlib import sha256
from math import factorial


def partitions(n, upper=None):
    """Generate all partitions of n in reverse lexicographic order."""
    if n == 0:
        yield ()
        return
    if upper is None or upper > n:
        upper = n
    for first in range(upper, 0, -1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


@lru_cache(maxsize=None)
def dimension(partition):
    """Exact f^lambda by the hook-length formula."""
    n = sum(partition)
    product = 1
    for i, row in enumerate(partition):
        for j in range(row):
            below = sum(1 for lower in partition[i + 1 :] if lower > j)
            product *= row - j + below
    return factorial(n) // product


def beta_set(partition):
    r = len(partition)
    return tuple(sorted((part + r - i - 1 for i, part in enumerate(partition)),
                        reverse=True))


def beta_to_partition(beta):
    r = len(beta)
    padded = tuple(x - r + i + 1 for i, x in enumerate(beta))
    assert all(x >= 0 for x in padded)
    return tuple(x for x in padded if x)


@lru_cache(maxsize=None)
def remove_hooks(beta, length):
    """Return (new beta set, MN sign) for all removable hooks of length."""
    occupied = set(beta)
    moves = []
    for x in beta:
        target = x - length
        if target < 0 or target in occupied:
            continue
        height = sum(target < y < x for y in beta)
        changed = list(beta)
        changed[changed.index(x)] = target
        changed.sort(reverse=True)
        moves.append((tuple(changed), -1 if height % 2 else 1))
    return tuple(moves)


@lru_cache(maxsize=None)
def repeated_hook_character(beta, length, multiplicity):
    """MN recurrence for (length^multiplicity, 1^remaining_size)."""
    if multiplicity == 0:
        return dimension(beta_to_partition(beta))
    return sum(sign * repeated_hook_character(new_beta, length, multiplicity - 1)
               for new_beta, sign in remove_hooks(beta, length))


def character(partition, length, multiplicity):
    return repeated_hook_character(beta_set(partition), length, multiplicity)


def self_test():
    # Standard S_3 and S_4 character-table columns, independently tabulated.
    cases = {
        (3, 2, 1): {
            (3,): (1, 1),
            (2, 1): (0, -1),
            (1, 1, 1): (-1, 1),
        },
        (4, 2, 1): {
            (4,): (1, 1),
            (3, 1): (1, -1),
            (2, 2): (0, 2),
            (2, 1, 1): (-1, -1),
            (1, 1, 1, 1): (-1, 1),
        },
    }
    for (n, length, _), rows in cases.items():
        for lam, (at_one_hook, at_two_hooks) in rows.items():
            assert sum(lam) == n
            assert character(lam, length, 1) == at_one_hook
            if n == 4:
                assert character(lam, length, 2) == at_two_hooks


def scan(n, multiplicity):
    count = 0
    zero_rows = []
    nonzero_digest = sha256()
    min_abs = None
    min_rows = []
    value_counts = {}
    for lam in partitions(n):
        count += 1
        value = character(lam, 2, multiplicity)
        nonzero_digest.update((repr(lam) + ":" + str(value) + "\n").encode())
        value_counts[value] = value_counts.get(value, 0) + 1
        if value == 0:
            zero_rows.append(lam)
        else:
            magnitude = abs(value)
            if min_abs is None or magnitude < min_abs:
                min_abs = magnitude
                min_rows = [(lam, value)]
            elif magnitude == min_abs:
                min_rows.append((lam, value))
    assert count == 75175  # p(44), an independent standard partition count.
    return {
        "partitions": count,
        "zero_count": len(zero_rows),
        "first_zero": zero_rows[0] if zero_rows else None,
        "all_zero_rows": zero_rows,
        "min_abs_nonzero": min_abs,
        "distinct_values": len(value_counts),
        "value_range": (min(value_counts), max(value_counts)),
        "ordered_column_sha256": nonzero_digest.hexdigest(),
    }


def main():
    self_test()
    print("self_test=S3,S4 exact columns passed")
    print("partition_order=reverse_lexicographic")
    for multiplicity in (2, 4):
        result = scan(44, multiplicity)
        print(f"mu=(2^{multiplicity},1^{44-2*multiplicity})")
        for key, value in result.items():
            print(f"{key}={value}")


if __name__ == "__main__":
    main()
