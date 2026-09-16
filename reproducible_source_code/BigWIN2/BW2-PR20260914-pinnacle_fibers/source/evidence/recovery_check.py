#!/usr/bin/env python3
"""Recheck retained triage certificates without modifying prior artifacts."""
from collections import defaultdict
from itertools import permutations, product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
JOB = 'primary-20260914-pinnacle-fibers-triage-e0fe653b2140'
SOURCE_HASH = '1df3a7b5d04986a7f3a816b6fd50b53b6a27d5b95b005273f1d100fe5f5bcba7'

def digest(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()

def pins(p):
    return tuple(p[i] for i in range(1, len(p)-1) if p[i-1] < p[i] > p[i+1])

def inversion(p):
    pos = {v: i for i, v in enumerate(p)}
    return tuple(sum(pos[u] > pos[v] for u in range(1, v))
                 for v in range(1, len(p)+1))

def le(a, b):
    return all(x <= y for x, y in zip(a, b))

def operations(rows):
    size = len(rows)
    order = [[le(inversion(a), inversion(b)) for b in rows] for a in rows]
    joins, meets = {}, {}
    for a, b in product(range(size), repeat=2):
        upper = [u for u in range(size) if order[a][u] and order[b][u]]
        lower = [u for u in range(size) if order[u][a] and order[u][b]]
        least = [u for u in upper if all(order[u][v] for v in upper)]
        greatest = [u for u in lower if all(order[v][u] for v in lower)]
        assert len(least) == len(greatest) == 1
        joins[a, b], meets[a, b] = least[0], greatest[0]
    return order, joins, meets

def main():
    retained = ['source.md', 'evidence/n5_obstruction.md',
                'evidence/triage_exact.py', 'evidence/verify_triage.py',
                'evidence/triage_exact_results.json',
                'evidence/triage_obstruction.json', 'evidence/triage_verification.json']
    before = {p: digest(p) for p in retained}
    assert before['source.md'] == SOURCE_HASH
    cert = json.loads((ROOT / retained[-2]).read_text())
    previous = json.loads((ROOT / retained[-1]).read_text())
    assert previous['discovery_certificate_sha256'] == before[retained[-2]]
    small = []
    for n in range(5):
        groups = defaultdict(list)
        for p in permutations(range(1, n+1)):
            groups[pins(p)].append(p)
        for rows in groups.values():
            _, joins, meets = operations(rows)
            for a, b, c in product(range(len(rows)), repeat=3):
                assert meets[a, joins[b, c]] == joins[meets[a, b], meets[a, c]]
        small.append({'n': n, 'fibers': len(groups), 'all_triples_distributive': True})
    assert small == previous['small_cases']
    assert cert['n'] == 5 and cert['sigma'] == [5]
    rows = [p for p in permutations(range(1, 6)) if pins(p) == (5,)]
    supplied = [(tuple(r['permutation']), tuple(r['iota'])) for r in cert['fiber']]
    assert len(supplied) == len(set(supplied)) == len(rows) == 56
    assert set(supplied) == {(p, inversion(p)) for p in rows}
    order, joins, meets = operations(rows)
    named = {'e': (1,2,3,5,4), 'b': (1,2,5,3,4), 'a': (1,3,5,2,4),
             'c': (1,3,4,5,2), 'd': (1,3,5,4,2)}
    ids = {name: rows.index(p) for name, p in named.items()}
    reverse = {i: name for name, i in ids.items()}
    for name, p in named.items():
        assert previous['witness'][name] == {'permutation': list(p), 'iota': list(inversion(p))}
    assert len(previous['five_element_sublattice_bounds']) == 25
    checked_pairs = set()
    for record in previous['five_element_sublattice_bounds']:
        x, y = record['pair']
        checked_pairs.add((x, y))
        a, b = ids[x], ids[y]
        assert reverse[joins[a, b]] == record['join']
        assert reverse[meets[a, b]] == record['meet']
        upper = {rows[u] for u in range(56) if order[a][u] and order[b][u]}
        lower = {rows[u] for u in range(56) if order[u][a] and order[u][b]}
        assert upper == set(map(tuple, record['all_upper_bounds']))
        assert lower == set(map(tuple, record['all_lower_bounds']))
        assert len(upper) == len(record['all_upper_bounds'])
        assert len(lower) == len(record['all_lower_bounds'])
    assert checked_pairs == set(product(named, repeat=2))
    a, b, c = (ids[name] for name in ('a', 'b', 'c'))
    assert meets[a, joins[b, c]] == a != b == joins[meets[a, b], meets[a, c]]
    failure = cert['failure']
    assert [supplied[i][0] for i in failure['triple']] == [named[x] for x in ('a','b','c')]
    assert supplied[failure['lhs']][0] == named['a']
    assert supplied[failure['rhs']][0] == named['b']
    lower_box = [{'permutation': list(p), 'iota': list(inversion(p)), 'pinnacles': list(pins(p))}
                 for p in permutations(range(1, 6)) if le(inversion(p), (0,0,1,0,1))]
    assert len(lower_box) == 4
    assert lower_box == previous['ambient_lower_box_for_a_c']
    assert [r['permutation'] for r in lower_box if r['pinnacles'] == [5]] == [list(named['e'])]
    assert before == {p: digest(p) for p in retained}
    result = {'job_id': JOB, 'verification_completed': True,
              'role': 'triage', 'fresh_mathematical_referee': False,
              'method': 'direct permutations; universal bounds; saved bound-set comparison',
              'small_cases': small, 'complete_fiber_size': 56,
              'all_pairs_have_internal_join_and_meet': True,
              'all_25_saved_bound_records_match': True,
              'distributivity': {'triple': ['a','b','c'], 'lhs': 'a', 'rhs': 'b', 'equal': False},
              'ambient_lower_box_for_a_c': lower_box,
              'retained_files_unchanged_sha256': before}
    target = ROOT / 'evidence/recovery_check.json'
    temporary = target.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(result, indent=2) + '\n')
    temporary.replace(target)
    print(json.dumps({k: v for k, v in result.items() if k != 'retained_files_unchanged_sha256'}))

if __name__ == '__main__':
    main()
