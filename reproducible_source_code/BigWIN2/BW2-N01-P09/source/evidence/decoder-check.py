#!/usr/bin/env python3
"""Exact adversarial checks of the SC229 decoder; no all-arity inference.

Run from the project directory: python3 evidence/decoder-check.py
Only the Python standard library is used. The decoder receives a truth set
and labelled support, never a syntactic term or its proposed tree code.
All coordinate partitions are checked to find the finest AND factorization.
"""
from functools import lru_cache
from itertools import product
from pathlib import Path
from fractions import Fraction
from math import comb, factorial, prod
import hashlib
import json
import time

JOB = "newwin-00001-p09-research-6b8b4cffaffd"
TABLE = ((0, 0, 0), (1, 0, 1), (1, 1, 1))
STATS = {"decoder_calls": 0, "coordinate_partitions_tested": 0,
         "factors_checked": 0, "singleton_decodes": 0,
         "essential_coordinate_checks": 0}


@lru_cache(None)
def universe(n):
    return tuple(product(range(3), repeat=n))


@lru_cache(None)
def partitions(n):
    if n == 0:
        return ((),)
    out = []
    for p in partitions(n - 1):
        out.append(p + ((n - 1,),))
        for j, b in enumerate(p):
            out.append(p[:j] + (b + (n - 1,),) + p[j + 1:])
    return tuple(out)


def projection(relation, indices):
    return frozenset(tuple(a[i] for i in indices) for a in relation)


def finest_factors(labels, relation):
    """Find all factorizing partitions, without assuming the decoder lemma."""
    assert relation
    candidates = []
    for p in partitions(len(labels)):
        STATS["coordinate_partitions_tested"] += 1
        factors = tuple(projection(relation, b) for b in p)
        # The relation is contained in the product of projections. Equal
        # cardinalities therefore certify exact Cartesian factorization.
        if prod(map(len, factors)) == len(relation):
            candidates.append((p, factors))
    max_blocks = max(len(p) for p, _ in candidates)
    finest = [(p, f) for p, f in candidates if len(p) == max_blocks]
    assert len(finest) == 1, ("nonunique finest factorization", labels)
    p, fs = finest[0]
    return tuple((tuple(labels[i] for i in b), f) for b, f in zip(p, fs))


def check_essential(labels, relation):
    assert 0 < len(relation) < 3 ** len(labels)
    for i in range(len(labels)):
        STATS["essential_coordinate_checks"] += 1
        slices = [frozenset(a[:i] + a[i+1:] for a in relation if a[i] == v)
                  for v in range(3)]
        assert len(set(slices)) > 1, ("inessential variable", labels, i)


def decode(labels, relation):
    STATS["decoder_calls"] += 1
    check_essential(labels, relation)
    assert (0,) * len(labels) not in relation
    if len(labels) == 1:
        STATS["singleton_decodes"] += 1
        assert relation == frozenset({(1,)})
        return (labels[0], (), ())
    fs = finest_factors(labels, relation)
    matches = []
    for z, (block, f) in enumerate(fs):
        STATS["factors_checked"] += 1
        check_essential(block, f)
        for j in range(len(block)):
            if not any(a[j] == 0 for a in f):
                matches.append((z, j))
    assert len(matches) == 1, ("root-factor recognition failed", labels, matches)
    z, root_pos = matches[0]
    root_block, h = fs[z]
    root = root_block[root_pos]
    child_labels = root_block[:root_pos] + root_block[root_pos+1:]
    assert child_labels
    assert sum(a[root_pos] == 2 for a in h) == 3 ** len(child_labels)
    h_root1 = frozenset(a[:root_pos] + a[root_pos+1:]
                       for a in h if a[root_pos] == 1)
    first = decode(child_labels, frozenset(universe(len(child_labels))) - h_root1)
    others = []
    for k, (block, f) in enumerate(fs):
        if k != z:
            assert (0,) * len(block) in f
            others.append(decode(block, frozenset(universe(len(block))) - f))
    return (root, first, tuple(sorted(others)))


def graft(left, right):
    root, first, others = left
    if first == ():
        return root, right, ()
    return root, first, tuple(sorted(others + (right,)))


@lru_cache(None)
def literal_terms(labels):
    """Every syntax tree, using the table, with no equivalence pruning."""
    if len(labels) == 1:
        return ((bytes(range(3)), (labels[0], (), ())),)
    rows = universe(len(labels))
    outputs = []
    for mask in range(1, (1 << len(labels)) - 1):
        li = tuple(i for i in range(len(labels)) if mask & (1 << i))
        ri = tuple(i for i in range(len(labels)) if not mask & (1 << i))
        left_labels = tuple(labels[i] for i in li)
        right_labels = tuple(labels[i] for i in ri)
        left_index = [sum(a[j] * 3 ** (len(li)-1-k) for k, j in enumerate(li))
                      for a in rows]
        right_index = [sum(a[j] * 3 ** (len(ri)-1-k) for k, j in enumerate(ri))
                       for a in rows]
        for lv, lc in literal_terms(left_labels):
            for rv, rc in literal_terms(right_labels):
                value = bytes(TABLE[lv[i]][rv[j]] for i, j in zip(left_index, right_index))
                outputs.append((value, graft(lc, rc)))
    expected = factorial(len(labels)) * comb(2*len(labels)-2, len(labels)-1) // len(labels)
    assert len(outputs) == expected
    return tuple(outputs)


def exhaustive_decoder(nmax=5):
    result = []
    for n in range(1, nmax+1):
        labels = tuple(range(n))
        value_codes, code_values = {}, {}
        raw = literal_terms(labels)
        for value, code in raw:
            assert value_codes.setdefault(value, code) == code
            assert code_values.setdefault(code, value) == value
        for value, code in value_codes.items():
            relation = frozenset(a for a, v in zip(universe(n), value) if v == 1)
            assert decode(labels, relation) == code, ("decoded tree differs", n, code)
        result.append({"n": n, "raw_full_linear_terms": len(raw),
                       "distinct_functions_decoded": len(value_codes),
                       "assignments_per_function": 3**n})
    return result


def left_comb(labels):
    t = labels[0]
    for x in labels[1:]:
        t = (t, x)
    return t


def right_comb(labels):
    t = labels[-1]
    for x in reversed(labels[:-1]):
        t = (x, t)
    return t


def balanced(labels):
    if len(labels) == 1:
        return labels[0]
    mid = len(labels)//2
    return (balanced(labels[:mid]), balanced(labels[mid:]))


def syntax_code(t):
    if isinstance(t, int):
        return (t, (), ())
    return graft(syntax_code(t[0]), syntax_code(t[1]))


def evaluate(t, assignment):
    if isinstance(t, int):
        return assignment[t]
    return TABLE[evaluate(t[0], assignment)][evaluate(t[1], assignment)]


def structured_attacks():
    # Chosen after the written decoder statement: large root degree, deep
    # recursion, a large distinguished child, non-singleton ordinary children,
    # and label permutations. This is a bounded list, not an arity census.
    out = []
    for n in (6, 7):
        ls = tuple(range(n))
        families = {
            "left_comb": left_comb(ls),
            "right_comb": right_comb(ls),
            "balanced": balanced(ls),
            "deep_distinguished_child": (0, left_comb(ls[1:])),
            "compound_ordinary_child": ((0, 1), right_comb(ls[2:])),
            "reversed_left_comb": left_comb(ls[::-1]),
            "reversed_right_comb": right_comb(ls[::-1]),
            "reversed_balanced": balanced(ls[::-1]),
        }
        for name, term in families.items():
            relation = frozenset(a for a in universe(n) if evaluate(term, a) == 1)
            assert decode(ls, relation) == syntax_code(term)
            out.append({"n": n, "family": name, "syntax": term,
                        "assignments": 3**n, "truth_set_size": len(relation)})
    return out


def counting_check(nmax=12):
    c, b = [0] * (nmax+1), [0] * (nmax+1)
    c[1], b[0] = 1, 1
    result = []
    for n in range(1, nmax+1):
        if n > 1:
            c[n] = n * sum(comb(n-1, k)*c[k]*b[n-1-k] for k in range(1, n))
        b[n] = sum(comb(n-1, j-1)*c[j]*b[n-j] for j in range(1, n+1))
        explicit = factorial(n-1) * sum(
            (Fraction(comb(n, k) * k**(n-1-k), factorial(n-1-k))
             for k in range(n)), Fraction())
        assert explicit.denominator == 1 and explicit == c[n]
        result.append({"n": n, "recurrence_count": c[n], "explicit_sum": int(explicit),
                       "meaning": "proved-model count; not a new function census"})
    prior = json.loads(Path("evidence/triage-check.json").read_text())
    for row in prior["literal_tree_check"]["rows"]:
        assert c[row["n"]] == row["distinct_functions"]
    return result


def main():
    started = time.monotonic()
    result = {"job_id": JOB, "arithmetic": "exact finite sets, integers and fractions",
              "randomness": "none", "decoder_inputs": "labelled support and truth set only",
              "exhaustive_decoding": exhaustive_decoder(),
              "structured_attacks": structured_attacks(),
              "counting_check": counting_check(), "stats": STATS,
              "scope": "Finite tests of a separately written all-arity proof; no mathematical audit.",
              "source_sha256": hashlib.sha256(Path("source.md").read_bytes()).hexdigest(),
              "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "elapsed_seconds": round(time.monotonic()-started, 3)}
    target = Path(__file__).with_suffix(".json")
    temporary = target.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(result, indent=2) + "\n")
    temporary.replace(target)
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
