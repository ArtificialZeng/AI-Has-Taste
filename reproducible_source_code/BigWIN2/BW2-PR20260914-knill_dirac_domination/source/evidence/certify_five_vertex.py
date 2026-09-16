"""Exact rational-root certificates for every five-vertex isomorphism class.

The integer matrix builder is independent of the numerical screen's builder.
Run: OPENBLAS_NUM_THREADS=1 python3 evidence/certify_five_vertex.py
"""
import itertools
import json
import time
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parent
JOB = 'primary-20260914-knill-dirac-domination-research-6e957123a5e9'


def matrices(mask):
    faces = [tuple(v for v in range(5) if f >> v & 1)
             for f in range(1, 32) if mask >> (f - 1) & 1]
    n = len(faces)
    pos = {f: i for i, f in enumerate(faces)}
    assert all(y in pos for f in faces for size in range(1, len(f))
               for y in itertools.combinations(f, size))
    L = sp.Matrix(n, n, lambda i, j: int(bool(set(faces[i]) & set(faces[j]))))
    d = sp.zeros(n)
    for f in faces:
        if len(f) > 1:
            for j in range(len(f)):
                d[pos[f], pos[f[:j]+f[j+1:]]] = (-1)**j
    assert d*d == sp.zeros(n)
    return faces, L, d+d.T


def root_intervals(A):
    poly = A.charpoly().as_poly()
    grouped = poly.intervals(eps=sp.Rational(1, 10**9))
    roots = []
    for (a, b), mult in reversed(grouped):
        roots.extend([(a, b)]*mult)
    assert len(roots) == A.rows
    return list(map(int, poly.all_coeffs())), roots


def certificate(mask):
    faces, L, D = matrices(mask)
    pl, li = root_intervals(L)
    pd, di = root_intervals(D)
    lower = []
    total = sp.Rational(0)
    for (a, _), (_, d) in zip(li, di):
        total += a-d
        lower.append(total)
    return dict(mask=mask, faces=faces, n=len(faces),
                L=L.tolist(), D=D.tolist(),
                charpoly_L_coefficients=pl, charpoly_D_coefficients=pd,
                L_intervals=[[str(a), str(b)] for a, b in li],
                D_intervals=[[str(a), str(b)] for a, b in di],
                partial_sum_gap_lower_bounds=list(map(str, lower)),
                every_k_strictly_positive=all(t > 0 for t in lower))


def main():
    start = time.monotonic()
    census = json.loads((ROOT/'five-vertex-census.json').read_text())
    reps = census['isomorphism_representatives']
    certs = []
    for i, r in enumerate(reps):
        certs.append(dict(certificate(r['mask']), orbit_size=r['orbit_size']))
        if (i+1) % 25 == 0:
            print(json.dumps({'certified_so_far':i+1,
                              'elapsed_seconds':time.monotonic()-start}), flush=True)
    result = dict(job_id=JOB, arithmetic='exact integer polynomials and rational intervals',
                  sympy_version=sp.__version__, certificates=certs,
                  summary=dict(isomorphism_classes=len(certs),
                    represented_labeled_complexes=sum(r['orbit_size'] for r in certs),
                    all_k_certified=all(r['every_k_strictly_positive'] for r in certs),
                    minimum_certified_gap=str(min(sp.Rational(t) for r in certs
                                                  for t in r['partial_sum_gap_lower_bounds'])),
                    elapsed_seconds=time.monotonic()-start))
    (ROOT/'five-vertex-exact.json').write_text(json.dumps(result, indent=2, default=int)+'\n')
    print(json.dumps(result['summary'], indent=2))


if __name__ == '__main__':
    main()
