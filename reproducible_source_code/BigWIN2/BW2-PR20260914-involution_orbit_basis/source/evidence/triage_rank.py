"""Bounded exact graded-rank test of Zhu's EJC 2026 p.21 candidate.

Run: python3 evidence/triage_rank.py > evidence/triage-rank.json
Only the four listed cases are tested. No general theorem or novelty is claimed.
"""
from functools import lru_cache
from itertools import combinations
from fractions import Fraction
from math import factorial
import json
import platform


def partitions(n, bound=None):
    if n == 0:
        yield ()
        return
    for k in range(min(n, n if bound is None else bound), 0, -1):
        for tail in partitions(n-k, k):
            yield (k,) + tail


@lru_cache(None)
def tableaux(shape):
    if not shape:
        return ((),)
    result = []
    for i in range(len(shape)):
        if i+1 < len(shape) and shape[i] == shape[i+1]:
            continue
        smaller = list(shape)
        smaller[i] -= 1
        smaller = tuple(x for x in smaller if x)
        for t in tableaux(smaller):
            rows = [list(r) for r in t]
            if i == len(rows):
                rows.append([])
            rows[i].append(sum(shape))
            result.append(tuple(tuple(r) for r in rows))
    return tuple(result)


def row_insert(rows, value):
    for i, row in enumerate(rows):
        for j, old in enumerate(row):
            if old > value:
                row[j], value = value, old
                break
        else:
            row.append(value)
            return i, len(row)-1
    rows.append([value])
    return len(rows)-1, 0


def reverse_corner(rows, i):
    value = rows[i].pop()
    for j in range(i-1, -1, -1):
        k = max(k for k, old in enumerate(rows[j]) if old < value)
        rows[j][k], value = value, rows[j][k]
    while rows and not rows[-1]:
        rows.pop()
    return value


def reverse_strip(t, mu):
    rows = [list(r) for r in t]
    removed = []
    while sum(map(len, rows)) > sum(mu):
        corners = [i for i, r in enumerate(rows)
                   if len(r) > (mu[i] if i < len(mu) else 0)
                   and (i+1 == len(rows) or len(rows[i+1]) < len(r))]
        i = max(corners, key=lambda j: len(rows[j]))
        removed.append(reverse_corner(rows, i))
    assert tuple(map(len, rows)) == mu
    assert removed == sorted(removed, reverse=True)
    check = [r[:] for r in rows]
    for v in reversed(removed):
        row_insert(check, v)
    assert tuple(map(tuple, check)) == t
    return rows


def transpose(t):
    return [[r[c] for r in t if len(r) > c] for c in range(len(t[0]) if t else 0)]


def inverse_rsk_same(t):
    p, q = [r[:] for r in t], [r[:] for r in t]
    pairs = []
    while q:
        i = max(range(len(q)), key=lambda j: q[j][-1])
        label = q[i].pop()
        value = reverse_corner(p, i)
        while q and not q[-1]:
            q.pop()
        pairs.append((label, value))
    pairs.sort()
    check_p, check_q = [], []
    for label, value in pairs:
        i, j = row_insert(check_p, value)
        if i == len(check_q):
            check_q.append([])
        assert j == len(check_q[i])
        check_q[i].append(label)
    assert check_p == t and check_q == t
    mapping = dict(pairs)
    assert all(i != j and mapping[j] == i for i, j in pairs)
    return tuple((i, j) for i, j in pairs if i < j)


def positive_strip(lam, mu):
    if any(i >= len(lam) or x > lam[i] for i, x in enumerate(mu)):
        return False
    h = 0
    for c in range(1, lam[0]+1):
        count = sum(x >= c for x in lam) - sum(x >= c for x in mu)
        if count not in (0, 1):
            return False
        h += 1 if count else -1
        if h < 0:
            return False
    return True


def candidates(n, a, d):
    result = []
    labels = []
    for lam in partitions(n):
        if lam[0] > n-2*d+a:
            continue
        for mu in partitions(2*d):
            if any(x % 2 for x in mu) or not positive_strip(lam, mu):
                continue
            for t in tableaux(lam):
                m = inverse_rsk_same(transpose(reverse_strip(t, mu)))
                assert len(m) == d
                result.append(m)
                labels.append(dict(lam=lam, mu=mu, tableau=t, monomial=m))
    assert len(result) == len(set(result))
    return result, labels


def matchings(vertices, fixed):
    if not vertices:
        if fixed == 0:
            yield ()
        return
    i, *rest = vertices
    if fixed > 0:
        yield from matchings(rest, fixed-1)
    for j in rest:
        for tail in matchings([v for v in rest if v != j], fixed):
            yield ((i, j),) + tail


def add_vector(basis, vector):
    """Exact rational row echelon insertion; vectors are functions on the locus."""
    v = list(map(Fraction, vector))
    for pivot in sorted(basis):
        coefficient = v[pivot]
        if coefficient:
            v = [x-coefficient*y for x, y in zip(v, basis[pivot])]
    pivot = next((i for i, x in enumerate(v) if x), None)
    if pivot is not None:
        coefficient = v[pivot]
        basis[pivot] = tuple(x/coefficient for x in v)


def run(n, a):
    points = list(matchings(list(range(1, n+1)), a))
    k = (n-a)//2
    assert len(points) == factorial(n)//(factorial(a)*2**k*factorial(k))
    eval_m = lambda m: [int(set(m).issubset(point)) for point in points]
    full_basis, grades, all_labels = {}, [], []
    for d in range(k+1):
        candidate, labels = candidates(n, a, d)
        lower_rank = len(full_basis)
        augmented = full_basis.copy()
        for m in candidate:
            add_vector(augmented, eval_m(m))
        all_degree = list(matchings(list(range(1, n+1)), n-2*d))
        for m in all_degree:
            add_vector(full_basis, eval_m(m))
        increment = len(augmented)-lower_rank
        grades.append(dict(degree=d, candidate_count=len(candidate),
                           lower_rank=lower_rank, augmented_rank=len(augmented),
                           full_filtered_rank=len(full_basis),
                           quotient_dimension=len(full_basis)-lower_rank,
                           candidate_increment=increment,
                           basis_in_degree=(increment == len(candidate) == len(full_basis)-lower_rank)))
        all_labels.extend(labels)
    assert len(full_basis) == len(points)
    return dict(n=n, a=a, point_count=len(points), points=points,
                grades=grades, candidate_data=all_labels)


if __name__ == '__main__':
    cases = [run(n, a) for n, a in [(3, 1), (4, 0), (5, 1), (6, 2)]]
    print(json.dumps(dict(job_id='primary-20260914-involution-orbit-basis-triage-ea5e8d81bc2f',
                         python=platform.python_version(), domain='exact rational arithmetic',
                         randomness=None,
                         scope='Only (3,1),(4,0),(5,1),(6,2), all degrees 0 <= d <= (n-a)/2',
                         convention_checks='Every inverse Pieri and inverse RSK instance round-trips',
                         all_pass=all(g['basis_in_degree'] for c in cases for g in c['grades']),
                         cases=cases), indent=2))
