"""Exact filtered-rank attack; independently generate Zhu's candidates forwards.

Run from project root, for example:
  python3 evidence/research_rank.py 7 1
  python3 evidence/research_rank.py 8 2
Each run writes research-n{n}a{a}-forward.json atomically, after every degree.
All ranks are over QQ (FLINT integer rank), never inferred from floats or a
rank deficiency modulo a prime. The saved inverse generator is used only for
comparison, not to generate the forward candidates or to calculate ranks.
"""
from itertools import combinations, permutations
from pathlib import Path
import hashlib
import json
import math
import platform
import sys
import time
import flint
from flint import fmpz_mat

JOB = 'primary-20260914-involution-orbit-basis-research-44e8d30db215'


def perfect(vertices):
    if not vertices:
        yield ()
        return
    u, *tail = vertices
    for v in tail:
        for rest in perfect([w for w in tail if w != v]):
            yield ((u, v),) + rest


def all_matchings(n, d):
    return sorted(m for support in combinations(range(1, n+1), 2*d)
                  for m in perfect(support))


def insert(tab, x):
    # Forward row insertion, coded without calling the inverse implementation.
    r = 0
    while r < len(tab):
        c = next((j for j, y in enumerate(tab[r]) if y > x), len(tab[r]))
        if c == len(tab[r]):
            tab[r].append(x)
            return r, c
        x, tab[r][c] = tab[r][c], x
        r += 1
    tab.append([x])
    return r, 0


def forward_label(n, m):
    partner = {u: v for e in m for u, v in [e, e[::-1]]}
    p, recording = [], []
    for i in sorted(partner):
        r, c = insert(p, partner[i])
        if r == len(recording):
            recording.append([])
        assert c == len(recording[r])
        recording[r].append(i)
    assert p == recording
    q = [[p[r][c] for r in range(len(p)) if len(p[r]) > c]
         for c in range(len(p[0]) if p else 0)]
    mu = tuple(map(len, q))
    assert all(t % 2 == 0 for t in mu)
    for i in range(1, n+1):
        if i not in partner:
            insert(q, i)
    lam = tuple(map(len, q))
    strip = [sum(t > c for t in lam)-sum(t > c for t in mu)
             for c in range(lam[0])]
    assert all(x in (0, 1) for x in strip)
    heights = [sum(2*x-1 for x in strip[:i]) for i in range(1, len(strip)+1)]
    return dict(lam=lam, mu=mu, tableau=tuple(map(tuple, q)), monomial=m,
                positive=all(h >= 0 for h in heights), heights=heights)


def columns_for(monomials, points):
    return [[int(frozenset(m) <= p) for p in points] for m in monomials]


def exact_rank(columns, row_count):
    # Rank is unchanged by transposition; store one function per matrix row.
    if not columns:
        return 0
    assert all(len(c) == row_count for c in columns)
    return fmpz_mat(columns).rank()


def atomic_json(path, data):
    tmp = path.with_suffix('.tmp')
    tmp.write_text(json.dumps(data, indent=2)+'\n')
    tmp.replace(path)


def run(n, a):
    assert 0 <= a <= n and n > 0 and (n-a) % 2 == 0
    from triage_rank import candidates
    start = time.monotonic()
    k = (n-a)//2
    point_tuples = all_matchings(n, k)
    points = [frozenset(m) for m in point_tuples]
    assert len(points) == math.factorial(n)//(math.factorial(a)*2**k*math.factorial(k))
    # Entire independent permutation census, practical through n=9.
    census = None
    if n <= 9:
        census = {tuple((i+1, p[i]+1) for i in range(n) if i < p[i])
                  for p in permutations(range(n))
                  if all(p[p[i]] == i for i in range(n)) and
                  sum(p[i] == i for i in range(n)) == a}
        assert census == set(point_tuples)
    output = dict(job_id=JOB, n=n, a=a, point_count=len(points), points=point_tuples,
                  arithmetic='exact QQ ranks via FLINT fmpz_mat.rank',
                  python=platform.python_version(), flint=flint.__version__,
                  source_sha256=hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
                  generator='independent forward RSK, transpose, then insert unused labels',
                  inverse_generator='evidence/triage_rank.py (comparison only)',
                  permutation_census_agrees=(census is not None),
                  complete=False, grades=[], candidate_data=[])
    path = Path(f'evidence/research-n{n}a{a}-forward.json')
    lower_cols, lower_rank, candidate_sets = [], 0, []
    for d in range(k+1):
        all_degree = all_matchings(n, d)
        labels = [forward_label(n, m) for m in all_degree]
        selected = [r for r in labels if r['positive'] and r['lam'][0] <= n-2*d+a]
        candidate = [r['monomial'] for r in selected]
        old, old_labels = candidates(n, a, d)
        assert set(candidate) == set(old)
        old_map = {tuple(r['monomial']):r for r in old_labels}
        assert all(all(r[key] == old_map[r['monomial']][key]
                       for key in ['lam','mu','tableau','monomial']) for r in selected)
        cols = columns_for(all_degree, points)
        new_cols = columns_for(candidate, points)
        augmented = exact_rank(lower_cols+new_cols, len(points))
        full = exact_rank(lower_cols+cols, len(points))
        # Independent degree-elevation check: for d<=k, all lower-degree
        # functions lie in the degree-d span; full_filtered rank must agree.
        degree_only = exact_rank(cols, len(points))
        assert full == degree_only
        grade = dict(degree=d, all_degree_count=len(all_degree),
                     candidate_count=len(candidate), lower_rank=lower_rank,
                     augmented_rank=augmented, full_filtered_rank=full,
                     degree_only_rank=degree_only, quotient_dimension=full-lower_rank,
                     candidate_increment=augmented-lower_rank,
                     basis_in_degree=(augmented-lower_rank == len(candidate) == full-lower_rank),
                     forward_inverse_labels_agree=True)
        output['grades'].append(grade)
        output['candidate_data'].extend(selected)
        output['elapsed_seconds'] = time.monotonic()-start
        atomic_json(path, output)
        print(json.dumps(dict(n=n,a=a,**grade)), flush=True)
        candidate_sets.append(set(candidate))
        lower_cols, lower_rank = lower_cols+cols, full
    assert lower_rank == len(points)
    failures = [(m, m[:i]+m[i+1:]) for d in range(1,k+1)
                for m in candidate_sets[d] for i in range(d)
                if m[:i]+m[i+1:] not in candidate_sets[d-1]]
    output.update(complete=True, all_pass=all(g['basis_in_degree'] for g in output['grades']),
                  divisor_closed=not failures, divisor_failures=failures[:10],
                  elapsed_seconds=time.monotonic()-start)
    atomic_json(path, output)
    print(json.dumps(dict(saved=str(path), elapsed_seconds=output['elapsed_seconds'],
                          all_pass=output['all_pass'])), flush=True)


if __name__ == '__main__':
    run(*map(int, sys.argv[1:]))
