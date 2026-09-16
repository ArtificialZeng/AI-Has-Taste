#!/usr/bin/env python3
"""Exact bounded triage checks; no all-arity proof and no randomness.

Literal evaluation enumerates every ordered binary term, without using the
proposed equivalence to prune terms. The tree code is checked separately.
Run from the project directory: python3 evidence/triage-check.py
"""
import hashlib
import itertools as it
import json
import math
from pathlib import Path

TABLE = ((0, 0, 0), (1, 0, 1), (1, 1, 1))
JOB = "newwin-00001-p09-triage-d9fd6bb8283b"


def splits(support):
    for left in range(1, support):
        if left & support == left:
            yield left, support ^ left


def graft(left, right):
    root, first, others = left
    if first == ():
        return root, right, ()
    return root, first, tuple(sorted(others + (right,)))


def literal_tree_check(n=6):
    rows = list(it.product(range(3), repeat=n))
    terms = {1 << i: [(bytes(a[i] for a in rows), (i, (), ()))]
             for i in range(n)}
    outputs = []
    evaluations = 0
    all_supports_checked = 0
    for size in range(1, n + 1):
        for support in range(1, 1 << n):
            if support.bit_count() != size:
                continue
            if size > 1:
                terms[support] = []
                for left, right in splits(support):
                    for fv, fc in terms[left]:
                        for gv, gc in terms[right]:
                            value = bytes(TABLE[a][b] for a, b in zip(fv, gv))
                            terms[support].append((value, graft(fc, gc)))
                            evaluations += len(rows)
            code_to_value, value_to_code = {}, {}
            for value, code in terms[support]:
                assert code_to_value.setdefault(code, value) == value, (
                    "one tree code has two functions", size, support, code)
                assert value_to_code.setdefault(value, code) == code, (
                    "two tree codes have one function", size, support, code)
            raw_count = math.factorial(size) * math.comb(2 * size - 2, size - 1) // size
            assert len(terms[support]) == raw_count
            all_supports_checked += 1
            if support == (1 << size) - 1:
                # Recover truth tables on just these size coordinates, in lex order.
                stride = 3 ** (n - size)
                unique = {v[::stride] for v in value_to_code}
                masks = sorted(sum(1 << i for i, a in enumerate(v) if a == 1)
                               for v in unique)
                digest = hashlib.sha256(
                    ("\n".join(format(v, "x") for v in masks) + "\n").encode()
                ).hexdigest()
                outputs.append({"n": size, "raw_terms": raw_count,
                                "distinct_functions": len(unique),
                                "distinct_tree_codes": len(code_to_value),
                                "truth_set_sha256": digest})
    inherited = json.loads(Path("evidence/p09-intake-check.json").read_text())
    for row, old in zip(outputs, inherited["rows"]):
        assert row["distinct_functions"] == old["distinct_functions"]
        assert row["truth_set_sha256"] == old["truth_set_sha256"]
    return {"ambient_variables": n, "all_nonempty_supports_checked": all_supports_checked,
            "literal_product_assignment_cells": evaluations,
            "rows": outputs, "inherited_truth_sets_agree": True,
            "code_function_bijection_checked_on_every_support": True}


def partitions(items):
    if not items:
        yield ()
        return
    x, *rest = items
    for p in partitions(rest):
        yield ((x,),) + p
        for j, block in enumerate(p):
            yield p[:j] + ((x,) + block,) + p[j + 1:]


def normalize(p):
    return tuple(sorted(tuple(sorted(block)) for block in p))


def refinement_check(alphabets=(2, 2, 3)):
    rows = list(it.product(*(range(k) for k in alphabets)))
    ps = [normalize(p) for p in partitions(list(range(len(alphabets))))]
    pairs = 0
    for mask in range(1, 1 << len(rows)):
        relation = [a for i, a in enumerate(rows) if mask & (1 << i)]
        # R is contained in the product of its projections, so equal finite
        # cardinalities certify equality with that product.
        factors = set()
        for p in ps:
            size = math.prod(len({tuple(a[i] for i in b) for a in relation})
                             for b in p)
            if size == len(relation):
                factors.add(p)
        for p in factors:
            for q in factors:
                meet = normalize([set(b) & set(c) for b in p for c in q
                                  if set(b) & set(c)])
                assert meet in factors, (alphabets, mask, p, q)
                pairs += 1
    return {"alphabet_sizes": alphabets,
            "nonempty_relations_exhausted": (1 << len(rows)) - 1,
            "coordinate_partitions_per_relation": len(ps),
            "factorizing_partition_pairs_checked": pairs,
            "common_refinement_failures": 0}


def identities():
    four = list(it.product(range(3), repeat=4))
    assert all(TABLE[TABLE[TABLE[w][x]][y]][z] ==
               TABLE[TABLE[TABLE[w][x]][z]][y] for w, x, y, z in four)
    failures = []
    for x, y, z in it.product(range(3), repeat=3):
        lhs = TABLE[TABLE[x][y]][z]
        rhs = TABLE[TABLE[x][z]][y]
        if lhs != rhs:
            failures.append({"x": x, "y": y, "z": z, "lhs": lhs, "rhs": rhs})
    assert failures
    return {"four_variable_identity_assignments_checked": len(four),
            "stronger_three_variable_identity_counterexample": failures[0]}


def main():
    result = {"job_id": JOB, "arithmetic": "exact integers and literal table entries",
              "randomness": "none", "identities": identities(),
              "literal_tree_check": literal_tree_check(),
              "cartesian_common_refinement_check": refinement_check(),
              "scope": "Finite observations only. All-n tree injectivity remains a proof task.",
              "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    target = Path(__file__).with_name("triage-check.json")
    target.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
