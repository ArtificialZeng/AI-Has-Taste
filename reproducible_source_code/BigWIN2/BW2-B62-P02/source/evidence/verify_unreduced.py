#!/usr/bin/env python3
"""Independent unreduced verifier for the K_3,3 popular-dimension census.

Unlike orbit_pair_census.py, this program performs no symmetry reduction, no
Burnside calculation, and no popularity cache.  It enumerates all 13^6 labelled
profiles directly.  Its matching generator is an independent partial-function
generator.  Numba parallelizes exact integer loops but does not change them.
"""

import hashlib
from itertools import product
import platform
from pathlib import Path

import numba
import numpy as np
from numba import njit, prange


def make_orders():
    ans = []
    for r in product((0, 1, 2), repeat=3):
        levels = max(r) + 1
        if all(level in r for level in range(levels)):
            ans.append(r)
    assert len(ans) == 13
    return np.asarray(ans, dtype=np.int8)


def make_matchings_independently():
    """Enumerate injective partial functions men -> women; -1 is unmatched."""
    ans = []
    for assignment in product((-1, 0, 1, 2), repeat=3):
        used = [x for x in assignment if x >= 0]
        if len(used) != len(set(used)):
            continue
        partners = [3] * 6
        for man, woman in enumerate(assignment):
            if woman >= 0:
                partners[man] = woman
                partners[3 + woman] = man
        ans.append(partners)
    assert len(ans) == 34 and len({tuple(x) for x in ans}) == 34
    return np.asarray(ans, dtype=np.int8)


@njit(cache=True, inline="always")
def wins_singleton(i, ranks):
    for y in range(34):
        margin = 0
        for a in range(6):
            if ranks[i, a] < ranks[y, a]:
                margin += 1
            elif ranks[y, a] < ranks[i, a]:
                margin -= 1
        if margin < 0:
            return False
    return True


@njit(cache=True, inline="always")
def wins_pair(i, j, ranks):
    for y in range(34):
        margin = 0
        for a in range(6):
            best = min(ranks[i, a], ranks[j, a])
            if best < ranks[y, a]:
                margin += 1
            elif ranks[y, a] < best:
                margin -= 1
        if margin < 0:
            return False
    return True


@njit(cache=True)
def decode6(code):
    digits = np.empty(6, dtype=np.int8)
    quotient = code
    for a in range(5, -1, -1):
        digits[a] = quotient % 13
        quotient = quotient // 13
    return digits


@njit(cache=True, parallel=True)
def verify_every_labelled_profile(orders, matchings):
    total = 13 ** 6
    dimensions = np.empty(total, dtype=np.int8)
    winning_pairs = np.full((total, 2), -1, dtype=np.int8)
    for code in prange(total):
        digits = decode6(code)
        ranks = np.empty((34, 6), dtype=np.int8)
        for i in range(34):
            for a in range(6):
                partner = matchings[i, a]
                ranks[i, a] = 3 if partner == 3 else orders[digits[a], partner]

        dimension = 3
        for i in range(34):
            if wins_singleton(i, ranks):
                dimension = 1
                break
        if dimension == 3:
            for i in range(34):
                found = False
                for j in range(i + 1, 34):
                    if wins_pair(i, j, ranks):
                        dimension = 2
                        winning_pairs[code, 0] = i
                        winning_pairs[code, 1] = j
                        found = True
                        break
                if found:
                    break
        dimensions[code] = dimension
    return dimensions, winning_pairs


def profile_code(profile, orders):
    ids = {tuple(row): i for i, row in enumerate(orders.tolist())}
    code = 0
    for order in profile:
        code = 13 * code + ids[tuple(order)]
    return code


def edge_string(matching):
    return "{" + ",".join(f"m{i}-w{matching[i]}" for i in range(3)
                            if matching[i] != 3) + "}"


def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    orders = make_orders()
    matchings = make_matchings_independently()
    dimensions, pairs = verify_every_labelled_profile(orders, matchings)
    counts = np.bincount(dimensions, minlength=4)
    assert int(counts.sum()) == 13 ** 6
    assert counts[0] == 0 and counts[3] == 0

    triage_profile = ((0, 0, 0), (0, 1, 2), (0, 2, 1),
                      (0, 2, 1), (1, 2, 0), (1, 0, 0))
    code = profile_code(triage_profile, orders)
    assert dimensions[code] == 2 and min(pairs[code]) >= 0
    i, j = map(int, pairs[code])

    print(f"python={platform.python_version()} numpy={np.__version__} "
          f"numba={numba.__version__} platform={platform.platform()}")
    print(f"script_sha256={sha256(__file__)}")
    print(f"orders={len(orders)} matchings={len(matchings)} "
          f"labelled_profiles={len(dimensions)}")
    print(f"dimension_counts=d1:{int(counts[1])},d2:{int(counts[2])},d3:{int(counts[3])}")
    print(f"triage_profile_code={code} dimension={int(dimensions[code])}")
    print(f"triage_winning_pair_indices={i},{j}")
    print(f"triage_winning_pair={edge_string(matchings[i])};{edge_string(matchings[j])}")
    print("VERIFIED_UNREDUCED_ALL_PROFILES_HAVE_SINGLETON_OR_PAIR")


if __name__ == "__main__":
    main()
