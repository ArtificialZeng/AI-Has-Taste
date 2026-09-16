#!/usr/bin/env python3
"""Exact finite certificate for the F^3 two-site-block transducer.

At times divisible by three the uniform background is (0,0).  Pair the sites
(2r-1,2r), encode each site (b,c) as 2*b+c, and encode a two-site block in
base four.  The induced map H=F^3 has block radius two.  This script proves,
by exhaustive integer enumeration of the relevant finite windows, that the
left and right path languages in three_step_factor_structure.md are H-invariant
and dynamically decoupled across their central interface for every length.
It does not prove that either induced permutation is a single cycle.
"""

from hashlib import sha256
from itertools import product

from research_three_step_factors import (
    CENTER,
    GENERIC,
    INNER,
    NEXT,
    OUTER,
    valid_left,
    valid_right,
)
from triage_small_cases import step


ZERO = 0


def paths(alphabet, length):
    """All length-`length` paths in NEXT whose first letter is in alphabet."""
    if length == 0:
        return [()]
    result = [(a,) for a in alphabet]
    for _ in range(1, length):
        result = [p + (b,) for p in result for b in NEXT[p[-1]]]
    return result


def block_to_sites(block):
    return block // 4, block % 4


def local_rule(window):
    """Output center block of H from five input blocks, left to right."""
    assert len(window) == 5
    b_def, c_def = set(), set()
    # The center block is r=0 and occupies sites -1,0.
    for r, block in zip(range(-2, 3), window):
        for site, cell in zip((2 * r - 1, 2 * r), block_to_sites(block)):
            if cell & 2:
                b_def.add(site)
            if cell & 1:
                c_def.add(site)
    state = (0, 0, b_def, c_def)
    for _ in range(3):
        state = step(*state)
    _, _, b_def, c_def = state
    left = 2 * (-1 in b_def) + (-1 in c_def)
    right = 2 * (0 in b_def) + (0 in c_def)
    return 4 * left + right


def image(word):
    """Apply the radius-two block rule to a zero-padded finite word."""
    padded = (ZERO, ZERO) + tuple(word) + (ZERO, ZERO)
    return tuple(local_rule(padded[j:j + 5]) for j in range(len(word)))


def spill(word):
    """The two output blocks immediately beyond each end."""
    padded = (ZERO,) * 4 + tuple(word) + (ZERO,) * 4
    # Input word begins at padded index 4.  Output centers -2,-1,n,n+1 have
    # five-block windows beginning at indices 0,1,n+2,n+3.
    n = len(word)
    return tuple(local_rule(padded[j:j + 5]) for j in (0, 1, n + 2, n + 3))


def all_left(length):
    if length == 0:
        return [()]
    return [p for p in paths(OUTER, length) if p[-1] in INNER]


def all_right(generic_length):
    if generic_length == 0:
        return [(3,)]
    result = []
    for first in CENTER:
        for second in NEXT[first]:
            for tail in paths((second,), generic_length):
                word = (first,) + tail
                if word[-1] in INNER:
                    result.append(word)
    return result


def transducer_digest():
    """Hash the full 16^5 truth table in lexicographic input order."""
    digest = sha256()
    counts = [0] * 16
    for window in product(range(16), repeat=5):
        output = local_rule(window)
        digest.update(bytes(window + (output,)))
        counts[output] += 1
    return digest.hexdigest(), tuple(counts)


def certify_interior():
    five = paths(GENERIC, 5)
    six = paths(GENERIC, 6)
    assert all(local_rule(p) in GENERIC for p in five)
    assert all(local_rule(p[1:]) in NEXT[local_rule(p[:5])] for p in six)
    return len(five), len(six)


def certify_boundaries():
    # Any violation at a boundary is visible within block radius two; the
    # length-six prefix/suffix tests below deliberately include some paths
    # that may not extend to the opposite accepted boundary.  Thus they are
    # a harmless strengthening.  Short words, where the two boundary windows
    # overlap, are checked separately.
    left_prefixes = paths(OUTER, 6)
    left_suffixes = [p for p in paths(GENERIC, 6) if p[-1] in INNER]
    right_prefixes = []
    for first in CENTER:
        for second in NEXT[first]:
            right_prefixes.extend((first,) + p for p in paths((second,), 5))

    for word in left_prefixes:
        out = image(word)
        assert spill(word)[:2] == (ZERO, ZERO)
        assert out[0] in OUTER
        assert all(b in NEXT[a] for a, b in zip(out[:4], out[1:4]))
    for word in right_prefixes:
        out = image(word)
        assert spill(word)[:2] == (ZERO, ZERO)
        assert out[0] in CENTER
        assert out[1] in NEXT[out[0]]
        assert all(x in GENERIC for x in out[1:4])
        assert all(b in NEXT[a] for a, b in zip(out[1:4], out[2:4]))
    for word in left_suffixes:
        out = image(word)
        assert spill(word)[2:] == (ZERO, ZERO)
        assert out[-1] in INNER
        assert all(x in GENERIC for x in out[-4:])
        assert all(b in NEXT[a] for a, b in zip(out[-4:], out[-3:]))

    # The right and left languages have the same generic terminal condition.
    # Test every overlapping-boundary case explicitly.
    short_left = short_right = 0
    for length in range(0, 6):
        for word in all_left(length):
            out = image(word)
            assert spill(word) == (ZERO, ZERO, ZERO, ZERO)
            assert valid_left(out)
            short_left += 1
        for word in all_right(length):
            out = image(word)
            assert spill(word) == (ZERO, ZERO, ZERO, ZERO)
            assert valid_right(out)
            short_right += 1
    return len(left_prefixes), len(right_prefixes), len(left_suffixes), short_left, short_right


def certify_interface():
    # Put the interface between block -1 (left) and block 0 (right).  H has
    # radius two, so only the last two left outputs and first two right outputs
    # can see across it.  Length-four contexts contain every such possibility.
    left_contexts = [p for p in paths(GENERIC, 4) if p[-1] in INNER]
    right_contexts = []
    for first in CENTER:
        for second in NEXT[first]:
            right_contexts.extend((first,) + p for p in paths((second,), 3))

    checked = 0
    for left in left_contexts:
        isolated_left = image(left)
        for right in right_contexts:
            joined = image(left + right)
            isolated_right = image(right)
            assert joined[-len(right) - 2:-len(right)] == isolated_left[-2:]
            assert joined[len(left):len(left) + 2] == isolated_right[:2]
            checked += 1

    # Explicitly cover all shorter equal-length factor pairs, for which an
    # outer boundary can lie inside the radius-two interface window.
    short_pairs = 0
    for i in range(0, 4):
        for left in all_left(i):
            for right in all_right(i):
                joined = image(left + right)
                assert joined == image(left) + image(right)
                assert spill(left + right) == (ZERO, ZERO, ZERO, ZERO)
                short_pairs += 1
    return len(left_contexts), len(right_contexts), checked, short_pairs


def certify_finite_language_counts():
    # A redundant sanity check against the closed forms at several lengths.
    rows = []
    for i in range(0, 7):
        a = len(all_left(i))
        b = len(all_right(i))
        assert a == (4 ** (i + 1) - 1) // 3
        assert b == (2 * 4 ** (i + 1) - 5) // 3
        rows.append((i, a, b))
    return rows


if __name__ == "__main__":
    digest, output_counts = transducer_digest()
    interior = certify_interior()
    boundaries = certify_boundaries()
    interface = certify_interface()
    count_rows = certify_finite_language_counts()
    print(f"full_truth_table_rows={16**5} sha256={digest}")
    print("output_counts=" + ",".join(map(str, output_counts)))
    print(f"interior_five_windows={interior[0]} interior_six_windows={interior[1]}")
    print(
        "boundary_left_prefixes={} boundary_right_prefixes={} "
        "boundary_generic_suffixes={} short_left_words={} short_right_words={}".format(
            *boundaries
        )
    )
    print(
        "interface_left_contexts={} interface_right_contexts={} "
        "interface_pairs={} short_factor_pairs={}".format(*interface)
    )
    for i, a, b in count_rows:
        print(f"i={i} left_words={a} right_words={b}")
    print("certificate=PASS scope=invariance_and_interface_decoupling_only")
