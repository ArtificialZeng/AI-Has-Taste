"""Exact bounded triage: original interlacing and an explicit stronger method claim.

No randomized or floating-point root tests; no universal conclusion from search.
Run from the project: python3 evidence/triage-interlacing.py
"""
import itertools as it
import json
import time
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import sympy as sp

START = time.monotonic()
t = sp.Symbol('t')

def clean(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)

def poly(a):
    return sp.Poly.from_list(list(reversed(a)), t, domain=sp.QQ)

@lru_cache(None)
def rr(a):
    p = poly(a)
    return p.is_zero or sum(m for _, m in p.intervals()) == p.degree()

@lru_cache(None)
def interlaces(a, b):
    if not any(a) or not any(b):
        return True  # Explicit zero convention; no root claim for zero.
    f, g = poly(a), poly(b)
    if not rr(a) or not rr(b) or g.degree() - f.degree() not in (0, 1):
        return False
    h = sp.gcd(f, g)
    f, g = f.exquo(h), g.exquo(h)
    if f.degree() == 0 and g.degree() == 0:
        return True
    for precision in (4, 8, 16, 32, 64, 128):
        eps = sp.Rational(1, 10**precision)
        roots = [(lo, hi, tag, mult) for p, tag in ((f, 'f'), (g, 'g'))
                 for (lo, hi), mult in p.intervals(eps=eps)]
        roots.sort()
        if any(roots[z][1] >= roots[z+1][0] for z in range(len(roots)-1)):
            continue
        labels = [tag for lo, hi, tag, mult in roots for _ in range(mult)]
        expected = (['g'] if g.degree() == f.degree()+1 else []) + ['f', 'g'] * f.degree()
        return labels == expected
    raise RuntimeError('Root separation unresolved; no mathematical conclusion')

def data_for(lam, k):
    data = defaultdict(lambda: [[0]*len(lam) for _ in range(k)])
    for w in it.product(*(range(1, h+1) for h in lam)):
        alpha = tuple(w.count(i) for i in range(1, k+1))
        asc = sum(x < y for x, y in zip(w, w[1:]))
        data[alpha][w[0]-1][asc] += 1
    return {a: tuple(clean(x) for x in rows) for a, rows in data.items()}

def plus(a, b, q=1):
    return clean([(a[z] if z < len(a) else 0) + q*(b[z] if z < len(b) else 0)
                  for z in range(max(len(a), len(b)))])

def run():
    # Check the direction and multiplicity handling with explicit controls.
    assert interlaces((1,), (0, 1))
    assert not interlaces((0, 1), (1,))
    assert interlaces((0, 1), (0, 0, 1))
    assert not interlaces((0, 0, 1), (0, 1))
    assert not interlaces((1, 2, 1), (2, 3, 1))
    stats = dict(boards=0, content_cases=0, ordered_nonzero_pairs=0)
    failures = []
    obstruction = None
    for n in range(1, 8):
        for lam in it.combinations_with_replacement(range(1, 5), n):
            data = data_for(lam, 4)
            stats['boards'] += 1
            for alpha, rows in data.items():
                stats['content_cases'] += 1
                for hi in range(lam[0], 1, -1):
                    for lo in range(hi-1, 0, -1):
                        a, b = rows[hi-1], rows[lo-1]
                        if any(a) and any(b):
                            stats['ordered_nonzero_pairs'] += 1
                            if not interlaces(a, b):
                                failures.append(dict(lam=lam, alpha=alpha, hi=hi, lo=lo, f=a, g=b))
            # Stronger auxiliary claim C: all nonzero R_j(lam, beta-e_i)
            # across permitted prepended letters i form a compatible family.
            # A nonreal-rooted f+q*g disproves C, not Conjecture 28.
            if obstruction is None and n >= 2 and lam[0] >= 2 and lam[0] < lam[-1]:
                targets = set()
                for alpha in data:
                    for i in range(lam[0]):
                        beta = list(alpha); beta[i] += 1; targets.add(tuple(beta))
                for beta in sorted(targets):
                    family = []
                    for i in range(lam[0]):
                        if beta[i] == 0:
                            continue
                        a = list(beta); a[i] -= 1; a = tuple(a)
                        for j, f in enumerate(data.get(a, ()), 1):
                            if any(f):
                                family.append((i+1, j, a, f))
                    for left, right in it.combinations(family, 2):
                        if left[0] == right[0]:
                            continue
                        for q in (1, 2, 3, 5):
                            h = plus(left[3], right[3], q)
                            if not rr(h):
                                p = poly(h)
                                obstruction = dict(tail=lam, prepended_row=lam[0], beta=beta,
                                    left=dict(i=left[0], j=left[1], alpha=left[2], coeff=left[3]),
                                    right=dict(i=right[0], j=right[1], alpha=right[2], coeff=right[3]),
                                    q=q, sum_coeff=h, factorization=str(sp.factor(p.as_expr())),
                                    real_roots_with_multiplicity=sum(m for _,m in p.intervals()), degree=p.degree())
                                break
                        if obstruction:
                            break
                    if obstruction:
                        break
        print(json.dumps(dict(completed_n=n, stats=stats, failures=len(failures), obstruction=obstruction)), flush=True)
    result = dict(job_id='primary-20260913-multiset-rook-triage-cd5e7d22bd0b',
        scope='All nondecreasing boards in {1,2,3,4}^n, 1<=n<=7, all realized length-four contents; all ordered nonzero first-entry pairs.',
        verification='Integer word enumeration, QQ root isolation, exact polynomial gcd, rational disjoint root intervals; zero entries omitted.',
        stats=stats, original_interlacing_failures=failures, auxiliary_compatibility_obstruction=obstruction,
        elapsed_seconds=time.monotonic()-START, sympy=sp.__version__,
        limitation='Finite observations and one subsidiary-claim certificate; no resolution or independent referee.')
    out = Path(__file__).with_suffix('.json')
    out.write_text(json.dumps(result, indent=2)+'\n')
    return result

if __name__ == '__main__':
    print(json.dumps(run()))
