"""Deterministic triage only: exhaustive complexes on a four-vertex universe.

Run: OPENBLAS_NUM_THREADS=1 python3 evidence/tiny_complexes.py
Every nonempty downset of the nonempty Boolean lattice is visited once.
Exact verification on the three-vertex universe uses rational root isolation;
four-vertex results are explicitly floating-point observations.
"""
import itertools
import json
from pathlib import Path
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent
JOB = "primary-20260914-knill-dirac-domination-triage-809fb2a0f8af"

def complexes(m):
    faces = [tuple(c) for k in range(1, m + 1)
             for c in itertools.combinations(range(m), k)]
    requirements = []
    for x in faces:
        requirements.append(sum(1 << j for j, y in enumerate(faces)
                                if set(y) <= set(x)))
    for mask in range(1, 1 << len(faces)):
        if all(not (mask >> j & 1) or mask & need == need
               for j, need in enumerate(requirements)):
            yield [x for j, x in enumerate(faces) if mask >> j & 1]

def matrices(faces):
    n = len(faces)
    pos = {x: i for i, x in enumerate(faces)}
    L = np.array([[int(bool(set(x) & set(y))) for y in faces]
                  for x in faces], dtype=np.int64)
    d = np.zeros((n, n), dtype=np.int64)
    for i, x in enumerate(faces):
        if len(x) > 1:
            for j in range(len(x)):
                d[i, pos[x[:j] + x[j+1:]]] = (-1) ** j
    D = d + d.T
    assert not np.any(d @ d)
    assert np.all(np.diag(L) == 1) and np.all(np.diag(D) == 0)
    assert np.all(np.abs(D) + np.eye(n, dtype=np.int64) <= L)
    grading = np.array([(-1)**(len(x)-1) for x in faces])
    assert np.array_equal(grading[:, None] * D * grading[None, :], -D)
    orientation = np.array([(-1)**i for i in range(n)])
    assert sp.Matrix(D).charpoly().as_expr() == sp.Matrix(
        orientation[:, None] * D * orientation[None, :]).charpoly().as_expr()
    return L, D

def roots(A):
    p = sp.Matrix(A).charpoly().as_poly()
    intervals = p.intervals(eps=sp.Rational(1, 10**12))
    ordered = []
    for (a, b), mult in reversed(intervals):
        ordered.extend([(a, b)] * mult)
    assert len(ordered) == len(A)
    assert all(ordered[i][0] >= ordered[i+1][1]
               for i in range(len(A)-1)
               if ordered[i] != ordered[i+1])
    return p, ordered

def exact_record(faces):
    L, D = matrices(faces)
    p, li = roots(L)
    q, di = roots(D)
    lower = [sum(t[0] for t in li[:k]) - sum(t[1] for t in di[:k])
             for k in range(1, len(faces)+1)]
    return dict(faces=faces, L=L.tolist(), D=D.tolist(),
                charpoly_L=str(p.as_expr()), charpoly_D=str(q.as_expr()),
                L_intervals=[[str(a), str(b)] for a, b in li],
                D_intervals=[[str(a), str(b)] for a, b in di],
                partial_sum_gap_lower_bounds=list(map(str, lower)),
                every_k_certified=all(x > 0 for x in lower))

def numerical_record(faces, name=None):
    L, D = matrices(faces)
    le = np.linalg.eigvalsh(L)[::-1]
    de = np.linalg.eigvalsh(D)[::-1]
    gaps = np.cumsum(le - de)
    k = int(np.argmin(gaps)) + 1
    return dict(name=name, faces=faces, n=len(faces), min_k=k,
                minimum_gap=float(gaps[k-1]), gaps=gaps.tolist())

def closure(facets):
    return sorted({tuple(y) for x in facets for k in range(1,len(x)+1)
                   for y in itertools.combinations(sorted(x), k)},
                  key=lambda x:(len(x),x))

def main():
    exact = [exact_record(f) for f in complexes(3)]
    numerical = [numerical_record(f) for f in complexes(4)]
    structured = []
    for m in range(3, 7):
        for dimension in range(1, min(m-1, 3)+1):
            structured.append(numerical_record(
                closure(itertools.combinations(range(m), dimension+1)),
                f"{dimension}-skeleton on {m} vertices"))
    for m in range(3, 9):
        for name, edges in [
            ("path",[(i,i+1) for i in range(m-1)]),
            ("cycle",[(i,(i+1)%m) for i in range(m)]),
            ("star",[(0,i) for i in range(1,m)])]:
            structured.append(numerical_record(closure(edges),f"{name}-{m}"))
    result = dict(job_id=JOB, numpy_version=np.__version__, sympy_version=sp.__version__,
                  exact_three_vertex_universe=exact,
                  floating_four_vertex_universe=numerical,
                  floating_structured=structured,
                  summary=dict(exact_nonempty_complexes=len(exact),
                    all_exact_certified=all(r['every_k_certified'] for r in exact),
                    numerical_nonempty_complexes=len(numerical),
                    structured_cases=len(structured),
                    numerical_min_gap=min(r['minimum_gap'] for r in numerical+structured),
                    negative_numerical_candidates=sum(r['minimum_gap'] < -1e-9
                                                       for r in numerical+structured)))
    (ROOT/'tiny-complexes.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['summary'],indent=2))

if __name__ == '__main__':
    main()
