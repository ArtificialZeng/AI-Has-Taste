#!/usr/bin/env python3
"""Exact tests of a two-factor structure in the three-step RESOCA orbit.

For family parameter k=2*i, the sampled state F^(3q)(u,c^(k)) is tested on
the interval [-k-1,k].  Its left factor consists of sites [-k-1,-2], and its
right factor of sites [-1,k].  All assertions use exact integer/set operations.
"""

from triage_small_cases import formula, step


# A block is two adjacent sites.  A site is encoded by 2*b+c, and a block by
# 4*(left site)+(right site).  The ten generic block symbols below are
# .c,.b,c.,cb,b.,bc,x.,xc,xb,xx in that order after sorting by code.
GENERIC = (1, 2, 4, 6, 8, 9, 12, 13, 14, 15)
OUTER = frozenset((1, 2, 12, 13, 14, 15))
INNER = frozenset((1, 2, 6, 9, 13, 14, 15))
CENTER = frozenset((0, 3))
NEXT = {
    0: frozenset((4, 6, 8, 9)),
    1: frozenset((1, 2, 8, 9)),
    2: frozenset((1, 2, 4, 6)),
    3: frozenset(GENERIC),
    4: frozenset((4, 6, 8, 9)),
    6: frozenset((1, 2, 4, 6)),
    8: frozenset((4, 6, 8, 9)),
    9: frozenset((1, 2, 8, 9)),
    12: frozenset((4, 6, 8, 9)),
    13: frozenset((1, 2, 8, 9)),
    14: frozenset((1, 2, 4, 6)),
    15: frozenset(GENERIC),
}


def three_steps(state):
    for _ in range(3):
        state = step(*state)
    return state


def mask_pair(b_def, c_def, left, right):
    """Encode both defect sets on a finite interval as two exact bit masks."""
    b_mask = 0
    c_mask = 0
    for site in range(left, right + 1):
        bit = 1 << (site - left)
        if site in b_def:
            b_mask |= bit
        if site in c_def:
            c_mask |= bit
    return b_mask, c_mask


def block_word(b_def, c_def, left, right):
    cells = [2 * (site in b_def) + (site in c_def)
             for site in range(left, right + 1)]
    assert len(cells) % 2 == 0
    return tuple(4 * cells[j] + cells[j + 1]
                 for j in range(0, len(cells), 2))


def valid_left(word):
    if not word:
        return True
    return (word[0] in OUTER and word[-1] in INNER
            and all(b in NEXT[a] for a, b in zip(word, word[1:])))


def valid_right(word):
    if word == (3,):
        return True
    return (len(word) >= 2 and word[0] in CENTER and word[-1] in INNER
            and all(b in NEXT[a] for a, b in zip(word, word[1:])))


def path_counts(i):
    """Count the two finite path languages by exact adjacency-matrix DP."""
    if i == 0:
        return 1, 1

    left_vector = {symbol: int(symbol in OUTER) for symbol in GENERIC}
    for _ in range(i - 1):
        left_vector = {
            b: sum(left_vector[a] for a in GENERIC if b in NEXT[a])
            for b in GENERIC
        }
    left_count = sum(left_vector[a] for a in INNER)

    # A right word has i+1 blocks.  Sum the possible first edges from its
    # center symbol 0 or 3, then take i-1 generic edges.
    right_vector = {
        b: sum(b in NEXT[a] for a in CENTER) for b in GENERIC
    }
    for _ in range(i - 1):
        right_vector = {
            b: sum(right_vector[a] for a in GENERIC if b in NEXT[a])
            for b in GENERIC
        }
    right_count = sum(right_vector[a] for a in INNER)
    return left_count, right_count


def check(i):
    k = 2 * i
    initial = (0, 0, {0}, set(range(-k, k + 1, 2)))
    state = initial

    left_period = (4 ** (i + 1) - 1) // 3
    right_period = (2 * 4 ** (i + 1) - 5) // 3
    sampled_period = formula(i) // 3
    assert sampled_period == left_period * right_period

    left_cycle = []
    right_cycle = []
    first_left_return = None
    first_right_return = None
    support_confined = True
    interface_preserved = True
    block_language_preserved = True

    initial_left = mask_pair(initial[2], initial[3], -k - 1, -2)
    initial_right = mask_pair(initial[2], initial[3], -1, k)

    for q in range(sampled_period):
        bg_b, bg_c, b_def, c_def = state
        assert (bg_b, bg_c) == (0, 0)

        support_confined &= all(-k - 1 <= x <= k for x in b_def | c_def)
        interface_preserved &= (-1 not in b_def and -1 not in c_def)
        interface_preserved &= ((0 in b_def) == (0 in c_def))

        left = mask_pair(b_def, c_def, -k - 1, -2)
        right = mask_pair(b_def, c_def, -1, k)
        left_word = block_word(b_def, c_def, -k - 1, -2)
        right_word = block_word(b_def, c_def, -1, k)
        block_language_preserved &= valid_left(left_word)
        block_language_preserved &= valid_right(right_word)

        if q < left_period:
            left_cycle.append(left)
        else:
            assert left == left_cycle[q % left_period]
        if q < right_period:
            right_cycle.append(right)
        else:
            assert right == right_cycle[q % right_period]

        if q > 0 and left == initial_left and first_left_return is None:
            first_left_return = q
        if q > 0 and right == initial_right and first_right_return is None:
            first_right_return = q

        state = three_steps(state)

    # If a factor first returns only at the last sample before its next cycle,
    # the loop above does not encounter the endpoint; distinctness is equivalent.
    assert len(set(left_cycle)) == left_period
    assert len(set(right_cycle)) == right_period
    assert first_left_return is None or first_left_return == left_period
    assert first_right_return is None or first_right_return == right_period
    assert state == initial
    assert support_confined
    assert interface_preserved
    assert block_language_preserved
    language_counts = path_counts(i)
    assert language_counts == (left_period, right_period)

    return {
        "i": i,
        "family_k": k,
        "left_period": left_period,
        "right_period": right_period,
        "gcd": __import__("math").gcd(left_period, right_period),
        "sampled_period": sampled_period,
        "least_F_period": 3 * sampled_period,
        "language_counts": f"{language_counts[0]}x{language_counts[1]}",
        "language_match": True,
        "support": f"[{-(k + 1)},{k}]",
        "interface": "site -1 is 00; site 0 is 00 or 11",
    }


def check_prefix(i):
    """Held-out factor test without enumerating the much longer full orbit."""
    k = 2 * i
    state = (0, 0, {0}, set(range(-k, k + 1, 2)))
    left_period = (4 ** (i + 1) - 1) // 3
    right_period = (2 * 4 ** (i + 1) - 5) // 3
    left_cycle = []
    right_cycle = []

    for q in range(right_period + 1):
        _, _, b_def, c_def = state
        assert all(-k - 1 <= x <= k for x in b_def | c_def)
        assert -1 not in b_def and -1 not in c_def
        assert (0 in b_def) == (0 in c_def)

        left = mask_pair(b_def, c_def, -k - 1, -2)
        right = mask_pair(b_def, c_def, -1, k)
        assert valid_left(block_word(b_def, c_def, -k - 1, -2))
        assert valid_right(block_word(b_def, c_def, -1, k))

        if q < left_period:
            left_cycle.append(left)
        else:
            assert left == left_cycle[q % left_period]
        if q < right_period:
            right_cycle.append(right)
        else:
            assert right == right_cycle[0]

        if q != right_period:
            state = three_steps(state)

    assert len(set(left_cycle)) == left_period
    assert len(set(right_cycle)) == right_period
    assert path_counts(i) == (left_period, right_period)
    return {
        "i": i,
        "family_k": k,
        "prefix_samples": right_period + 1,
        "left_first_return": left_period,
        "right_first_return": right_period,
        "language_counts": f"{left_period}x{right_period}",
        "language_match": True,
        "full_return_tested": False,
    }


if __name__ == "__main__":
    for index in range(6):
        result = check(index)
        print(" ".join(f"{key}={value}" for key, value in result.items()))
    result = check_prefix(6)
    print(" ".join(f"{key}={value}" for key, value in result.items()))
