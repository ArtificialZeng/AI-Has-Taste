#!/usr/bin/env python3
"""Exact finite checks of pruning-proof.md; no imports from the triage scripts.

Run from PROJECT_DIR: python3 evidence/verify_pruning.py
For a replay after freezing, append --output evidence/pruning-replay.json.
Uses Python 3 and NumPy. All output files are inside the project. This is a
proposer's computational crosscheck, not a separate mathematical review.
"""
from functools import lru_cache
from itertools import combinations
from math import comb
from pathlib import Path
import argparse
import hashlib
import json
import time

import numpy as np


JOB = 'newwin-00001-p02-research-0e4a4dc1b1e3'
OP = np.array([[0, 0, 0], [1, 1, 0], [1, 0, 1]], dtype=np.uint8)
DEST = Path('evidence/pruning-verification.json')


def save(data):
    temp = DEST.with_suffix('.json.tmp')
    temp.write_text(json.dumps(data, indent=2) + '\n')
    temp.replace(DEST)


@lru_cache(None)
def raw_trees(n, start=0):
    if n == 1:
        return (start,)
    return tuple((l, r) for k in range(1, n)
                 for l in raw_trees(k, start)
                 for r in raw_trees(n-k, start+k))


def prune(t):
    if isinstance(t, int):
        return t
    l, r = t
    if isinstance(l, tuple) and isinstance(r, tuple):
        return prune(l)
    return (prune(l), prune(r))


def leaves(t):
    if isinstance(t, int):
        return (t,)
    return leaves(t[0]) + leaves(t[1])


def shift(t):
    if isinstance(t, int):
        return t + 1
    return (shift(t[0]), shift(t[1]))


def evaluate(t, variables):
    if isinstance(t, int):
        return variables[t]
    return OP[evaluate(t[0], variables), evaluate(t[1], variables)]


def essential_support(table):
    return tuple(i for i in range(table.ndim)
                 if any(not np.array_equal(np.take(table, 0, axis=i),
                                           np.take(table, v, axis=i))
                        for v in (1, 2)))


def reconstruct(table, labels):
    """Recover the ordered comb using only its full truth table and labels."""
    k = len(labels)
    assert table.shape == (3,) * k
    if k == 1:
        assert np.array_equal(table, np.array([0, 1, 2], dtype=np.uint8))
        return labels[0]
    if k == 2:
        assert np.array_equal(table, OP)
        return tuple(labels)
    if np.all(np.take(table, 1, axis=0) == 1):
        child = 1 - np.take(table, 2, axis=0)
        return (labels[0], reconstruct(child, labels[1:]))
    child = np.take(table, 0, axis=k-1)
    return (reconstruct(child, labels[:-1]), labels[-1])


def recover_ambient(table):
    support = essential_support(table)
    reduced = table[tuple(slice(None) if i in support else 0
                          for i in range(table.ndim))]
    return reconstruct(reduced, support), support


@lru_cache(None)
def all_combs(labels):
    if len(labels) == 1:
        return (labels[0],)
    if len(labels) == 2:
        return (tuple(labels),)
    return (tuple((labels[0], t) for t in all_combs(labels[1:])) +
            tuple((t, labels[-1]) for t in all_combs(labels[:-1])))


def main():
    global DEST
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=DEST)
    args = parser.parse_args()
    DEST = args.output
    assert DEST.resolve().is_relative_to(Path.cwd().resolve())
    started = time.monotonic()
    source_hash = hashlib.sha256(Path('source.md').read_bytes()).hexdigest()
    assert source_hash == '8d79f1e102ca5ec8f683c484ddfafbedb7fdfd8ac753b334df41c95bd8a857c0'
    result = {
        'job_id': JOB,
        'arithmetic': 'exact uint8 operation lookup, complete truth-table equality',
        'role': 'proposer crosscheck, not an independent referee',
        'source_sha256': source_hash,
        'leaf_labels': 'zero-based in code, corresponding to x_(label+1)',
        'status': 'in progress',
        'raw_truth_table_checks': [],
    }
    save(result)

    # Exhaustive raw bracketings, independent truth-table reconstruction,
    # and preservation of every value on the full ambient input space.
    old_rows = {r['n']: r for r in json.loads(
        Path('evidence/exact-spectrum.json').read_text())['rows']}
    for n in range(1, 9):
        variables = np.indices((3,) * n, dtype=np.uint8)
        function_tables = set()
        for tree in raw_trees(n):
            table = evaluate(tree, variables)
            p = prune(tree)
            assert np.array_equal(table, evaluate(p, variables))
            recovered, support = recover_ambient(table)
            assert support == leaves(p)
            assert recovered == p
            function_tables.add(table.tobytes())
        assert len(raw_trees(n)) == comb(2*n-2, n-1) // n
        digest = hashlib.sha256(b''.join(sorted(function_tables))).hexdigest()
        assert digest == old_rows[n]['sorted_full_tables_sha256']
        result['raw_truth_table_checks'].append({
            'n': n, 'raw_bracketings': len(raw_trees(n)),
            'assignments_per_tree': 3**n,
            'function_count': len(function_tables),
            'full_function_set_sha256': digest,
            'pruning_preservation': True,
            'support_and_recursive_reconstruction': True,
            'matches_prior_full_set_digest': True,
        })
        save(result)

    # Adversarial domain: every ordered comb on every nonempty subset of an
    # eight-coordinate ambient set, including forms unattainable by pruning
    # B_8. This attacks the stronger separation lemma and arbitrary gaps.
    n = 8
    variables = np.indices((3,) * n, dtype=np.uint8)
    seen = {}
    count_by_support_size = {}
    for k in range(1, n+1):
        count = 0
        for labels in combinations(range(n), k):
            for tree in all_combs(labels):
                table = evaluate(tree, variables)
                recovered, support = recover_ambient(table)
                assert support == labels
                assert recovered == tree
                key = table.tobytes()
                assert key not in seen, ('collision', tree, seen.get(key))
                seen[key] = tree
                count += 1
        expected = comb(n, k) * (1 if k <= 2 else 2**(k-2))
        assert count == expected
        count_by_support_size[k] = count
    result['all_subset_comb_check'] = {
        'ambient_arity': n, 'assignments_per_tree': 3**n,
        'all_combs_on_all_nonempty_subsets': len(seen),
        'count_by_support_size': count_by_support_size,
        'collisions': 0,
        'support_and_recursive_reconstruction': True,
        'complete_domain': 'all increasing-label combs with labels in {0,...,7}',
    }
    save(result)

    # Separate purely syntactic DP, generated by all possible original root
    # splits, without using the conjectured numerical recurrence.
    S = {2: {(0, 1)}}
    C = {2: {(0, 1)}}
    structural_rows = []
    for n in range(2, 15):
        if n >= 3:
            S[n] = {(0, shift(t)) for t in S[n-1]}
            S[n].update((t, n-1) for t in S[n-1])
            for k in range(2, n-1):
                S[n].update(S[k])
            C[n] = {t for t in S[n] if max(leaves(t)) == n-1}
        decomposition = set(C[n])
        for m in range(2, n-1):
            assert decomposition.isdisjoint(C[m])
            decomposition.update(C[m])
        assert decomposition == S[n]
        if n >= 3:
            assert len(C[n]) == len(C[n-1]) + len(S[n-1])
        raw_set_checked = n <= 10
        if raw_set_checked:
            assert {prune(t) for t in raw_trees(n)} == S[n]
        if n >= 4:
            a = lambda k: 1 if k == 1 else len(S[k])
            assert a(n) == 3*a(n-1) - 2*a(n-2) + a(n-3)
        structural_rows.append({
            'n': n, 'forms': len(S[n]), 'last_variable_retained': len(C[n]),
            'terminal_interval_decomposition': True,
            'root_bijection_count': True,
            'raw_tree_set_crosscheck': raw_set_checked,
            'truth_tables_evaluated_in_this_section': False,
        })
    result['structural_checks'] = structural_rows
    result['status'] = 'all stated finite checks passed'
    result['scope_limit'] = ('Full ambient truth-table checks stop at arity 8; '
                             'syntactic set counts stop at arity 14. '
                             'The all-arity theorem is proved in pruning-proof.md.')
    result['elapsed_seconds'] = time.monotonic() - started
    assert hashlib.sha256(Path('source.md').read_bytes()).hexdigest() == source_hash
    save(result)
    print(json.dumps({
        'status': result['status'],
        'all_subset_combs': len(seen),
        'structural_counts_n2_through_n14': [r['forms'] for r in structural_rows],
        'elapsed_seconds': result['elapsed_seconds'],
        'output': str(DEST),
    }))


if __name__ == '__main__':
    main()
