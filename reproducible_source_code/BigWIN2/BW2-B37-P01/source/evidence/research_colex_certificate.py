#!/usr/bin/env python3
"""Exact all-length certificate that H is a colexicographic successor.

The ordered predecessor lists below define recursively ordered path lists.
Their adjacent-pair languages are summarized by all factors and boundary
segments of length at most five.  The summary recurrence is exact.  Once its
finite state repeats, it covers every later length by induction.  Each local
record is compared with the independently computed five-block rule for F^3.
"""

from dataclasses import dataclass

from research_block_transducer import local_rule


K = 5
T = (0, 1, 2, 4, 6, 8, 9, 12, 13, 14, 15)
ORDER = {
    0: (1, 9, 13, 14, 6, 2, 15),
    1: (14, 6, 2, 15, 1, 9, 13),
    2: (14, 6, 2, 15, 1, 9, 13),
    4: (8, 12, 4, 14, 6, 2, 15),
    6: (8, 12, 4, 14, 6, 2, 15),
    8: (15, 1, 9, 13, 8, 12, 4),
    9: (15, 1, 9, 13, 8, 12, 4),
    12: (15,),
    13: (15,),
    14: (15,),
    15: (15,),
}
OUTER = frozenset((1, 2, 12, 13, 14, 15))
CENTER_ORDER = {
    t: ((3, 0) if t in (8, 9) else (0, 3) if t in (4, 6) else (3,))
    for t in T if t != 0
}


@dataclass(frozen=True)
class Summary:
    """Exact K-local summary of a collection of equal-length pair words."""

    length: int
    factors: frozenset
    prefixes: frozenset
    suffixes: frozenset


def empty_summary(length):
    return Summary(length, frozenset(), frozenset(), frozenset())


def singleton_summary(seq):
    seq = tuple(seq)
    factors = {
        seq[j:j + q]
        for q in range(1, min(K, len(seq)) + 1)
        for j in range(len(seq) - q + 1)
    }
    cut = min(K, len(seq))
    return Summary(len(seq), frozenset(factors), frozenset((seq[:cut],)),
                   frozenset((seq[-cut:],)))


def union(summaries, length):
    summaries = tuple(s for s in summaries if s.factors)
    if not summaries:
        return empty_summary(length)
    assert all(s.length == length for s in summaries)
    return Summary(
        length,
        frozenset().union(*(s.factors for s in summaries)),
        frozenset().union(*(s.prefixes for s in summaries)),
        frozenset().union(*(s.suffixes for s in summaries)),
    )


def append_symbol(summary, symbol):
    """Append `symbol` to every word represented by an exact summary."""
    if not summary.factors:
        return empty_summary(summary.length + 1)
    factors = set(summary.factors)
    for suffix in summary.suffixes:
        for q in range(0, min(K - 1, len(suffix)) + 1):
            tail = suffix[len(suffix) - q:] if q else ()
            factors.add(tail + (symbol,))
    if summary.length >= K:
        prefixes = summary.prefixes
    else:
        prefixes = frozenset(p + (symbol,) for p in summary.prefixes)
    suffixes = frozenset((s + (symbol,))[-K:] for s in summary.suffixes)
    return Summary(summary.length + 1, frozenset(factors), prefixes, suffixes)


def base_words(side, t):
    if side == "left":
        return tuple((a,) for a in ORDER[t] if a in OUTER)
    if t == 0:
        return ((3,),)
    return tuple((a,) for a in CENTER_ORDER[t])


def adjacent_summary(words):
    relations = []
    for x, y in zip(words, words[1:]):
        relations.append(singleton_summary(tuple(zip(x, y))))
    return union(relations, 1)


def transition_ok(summary):
    """Check y=H(x), including both padded boundaries, from a K-summary."""
    n = summary.length
    if n < K:
        for relation in summary.factors:
            if len(relation) != n:
                continue
            x = tuple(z[0] for z in relation)
            y = tuple(z[1] for z in relation)
            padded = (0, 0) + x + (0, 0)
            assert tuple(local_rule(padded[q:q + 5]) for q in range(n)) == y
            spill = (0, 0, 0, 0) + x + (0, 0, 0, 0)
            assert tuple(local_rule(spill[q:q + 5])
                         for q in (0, 1, n + 2, n + 3)) == (0, 0, 0, 0)
        return
    for factor in summary.factors:
        if len(factor) == K:
            x = tuple(z[0] for z in factor)
            assert local_rule(x) == factor[K // 2][1]
    for prefix in summary.prefixes:
        x = tuple(z[0] for z in prefix)
        y = tuple(z[1] for z in prefix)
        assert local_rule((0, 0, x[0], x[1], x[2])) == y[0]
        assert local_rule((0, x[0], x[1], x[2], x[3])) == y[1]
        assert local_rule((0, 0, 0, 0, x[0])) == 0
        assert local_rule((0, 0, 0, x[0], x[1])) == 0
    for suffix in summary.suffixes:
        x = tuple(z[0] for z in suffix)
        y = tuple(z[1] for z in suffix)
        assert local_rule((x[-4], x[-3], x[-2], x[-1], 0)) == y[-2]
        assert local_rule((x[-3], x[-2], x[-1], 0, 0)) == y[-1]
        assert local_rule((x[-2], x[-1], 0, 0, 0)) == 0
        assert local_rule((x[-1], 0, 0, 0, 0)) == 0


def direct_small_check(words):
    for j, x in enumerate(words):
        y = words[(j + 1) % len(words)]
        padded = (0, 0) + x + (0, 0)
        got = tuple(local_rule(padded[q:q + 5]) for q in range(len(x)))
        assert got == y
        spill = (0, 0, 0, 0) + x + (0, 0, 0, 0)
        q = len(x)
        assert tuple(local_rule(spill[r:r + 5]) for r in (0, 1, q + 2, q + 3)) == (0, 0, 0, 0)


def state_signature(first, last, extreme_pairs, relations):
    """The exact finite data on which the next K-summary state depends."""
    def trunc(word):
        return word[:K], word[-K:]
    extrema = tuple((t, trunc(first[t]), trunc(last[t])) for t in T)
    aligned = tuple(
        (key, value.factors, value.prefixes, value.suffixes)
        for key, value in sorted(extreme_pairs.items())
    )
    rel = tuple((t, relations[t].factors, relations[t].prefixes,
                 relations[t].suffixes) for t in T)
    return extrema, aligned, rel


def certify(side, max_length=30):
    first = {t: base_words(side, t)[0] for t in T}
    last = {t: base_words(side, t)[-1] for t in T}
    extreme_words = {
        (kind, t): (first[t] if kind == "F" else last[t])
        for kind in ("F", "L") for t in T
    }
    extreme_pairs = {
        (e, f): singleton_summary(tuple(zip(extreme_words[e], extreme_words[f])))
        for e in extreme_words for f in extreme_words
    }
    relations = {t: adjacent_summary(base_words(side, t)) for t in T}
    full_words = base_words(side, 0)
    direct_small_check(full_words)
    previous_signature = None
    stabilization = None
    checked_records = 0

    for n in range(1, max_length + 1):
        wrap = extreme_pairs[(('L', 0), ('F', 0))]
        full = union((relations[0], wrap), n)
        transition_ok(full)
        checked_records += len(full.factors) + len(full.prefixes) + len(full.suffixes)

        signature = state_signature(first, last, extreme_pairs, relations)
        if signature == previous_signature:
            stabilization = n - 1
            break
        previous_signature = signature

        new_first = {}
        new_last = {}
        extreme_parent = {}
        extreme_append = {}
        for t in T:
            extreme_parent[("F", t)] = ("F", ORDER[t][0])
            extreme_append[("F", t)] = ORDER[t][0]
            extreme_parent[("L", t)] = ("L", ORDER[t][-1])
            extreme_append[("L", t)] = ORDER[t][-1]
        new_extreme_pairs = {
            (e, f): append_symbol(
                extreme_pairs[(extreme_parent[e], extreme_parent[f])],
                (extreme_append[e], extreme_append[f]),
            )
            for e in extreme_parent for f in extreme_parent
        }
        new_relations = {}
        for t in T:
            order = ORDER[t]
            new_first[t] = first[order[0]] + (order[0],)
            new_last[t] = last[order[-1]] + (order[-1],)
            pieces = [append_symbol(relations[a], (a, a)) for a in order]
            for a, b in zip(order, order[1:]):
                pieces.append(append_symbol(
                    extreme_pairs[(('L', a), ('F', b))], (a, b)
                ))
            new_relations[t] = union(pieces, n + 1)
        first, last = new_first, new_last
        extreme_pairs, relations = new_extreme_pairs, new_relations

    assert stabilization is not None
    # Equality of consecutive exact summary states, together with the displayed
    # deterministic recurrence, is the induction step for every later length.
    return stabilization, checked_records, previous_signature


if __name__ == "__main__":
    # Verify that each ORDER[t] is exactly the generic predecessor set read
    # from the path graph (the explicit sets are included to avoid importing
    # the statement being certified from another enumeration routine).
    predecessor_sets = {
        0: {1, 2, 6, 9, 13, 14, 15},
        1: {1, 2, 6, 9, 13, 14, 15},
        2: {1, 2, 6, 9, 13, 14, 15},
        4: {2, 4, 6, 8, 12, 14, 15},
        6: {2, 4, 6, 8, 12, 14, 15},
        8: {1, 4, 8, 9, 12, 13, 15},
        9: {1, 4, 8, 9, 12, 13, 15},
        12: {15}, 13: {15}, 14: {15}, 15: {15},
    }
    assert all(set(ORDER[t]) == predecessor_sets[t] for t in T)
    for side in ("left", "right"):
        stabilization, records, signature = certify(side)
        counts = tuple(len(part) if hasattr(part, "__len__") else 0 for part in signature)
        print(f"side={side} summary_fixed_from_length={stabilization} checked_summary_records={records}")
    print("certificate=PASS scope=all_lengths_H_equals_cyclic_colex_successor")
