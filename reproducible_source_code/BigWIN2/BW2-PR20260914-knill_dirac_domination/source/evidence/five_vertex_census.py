"""Exhaustive labeled complexes on <=5 vertices; numerical spectral screen.

Run from the project root:
  OPENBLAS_NUM_THREADS=1 python3 evidence/five_vertex_census.py

Each face is its vertex bitset; each complex is a bitset indexed by face-1.
Two different exhaustive generators (downsets and maximal-face antichains)
must give exactly the same set. No probabilistic symmetry reduction is used.
"""
import hashlib
import itertools
import json
import time
from collections import Counter
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent
JOB = 'primary-20260914-knill-dirac-domination-research-6e957123a5e9'


def downsets(m):
    faces = sorted(range(1, 1 << m), key=lambda f: (f.bit_count(), f))
    needs = {}
    for f in faces:
        needs[f] = sum(1 << ((f ^ (1 << v)) - 1)
                       for v in range(m) if f >> v & 1
                       if f ^ (1 << v))

    def visit(i, mask):
        if i == len(faces):
            yield mask
            return
        f = faces[i]
        yield from visit(i + 1, mask)
        if mask & needs[f] == needs[f]:
            yield from visit(i + 1, mask | (1 << (f - 1)))
    return visit(0, 0)


def antichain_closures(m):
    """Independently enumerate pairwise incomparable maximal-face families."""
    all_faces = list(range(1, 1 << m))
    closure = {f: sum(1 << (g - 1) for g in all_faces if g & f == g)
               for f in all_faces}

    def visit(available, mask):
        yield mask
        for i, f in enumerate(available):
            rest = [g for g in available[i + 1:]
                    if g & f != g and g & f != f]
            yield from visit(rest, mask | closure[f])
    return visit(all_faces, 0)


def face_list(mask, m):
    return [f for f in range(1, 1 << m) if mask >> (f - 1) & 1]


def matrices(mask, m):
    faces = face_list(mask, m)
    n = len(faces)
    pos = {f: i for i, f in enumerate(faces)}
    L = np.array([[int(bool(f & g)) for g in faces] for f in faces],
                 dtype=np.int64)
    d = np.zeros((n, n), dtype=np.int64)
    for i, f in enumerate(faces):
        if f.bit_count() == 1:
            continue
        vertices = [v for v in range(m) if f >> v & 1]
        for j, v in enumerate(vertices):
            d[i, pos[f ^ (1 << v)]] = (-1) ** j
    assert not np.any(d @ d)
    D = d + d.T
    assert np.all(np.abs(D) + np.eye(n, dtype=np.int64) <= L)
    return L, D


def permute_mask(mask, m, permutation):
    result = 0
    for f in face_list(mask, m):
        g = sum(1 << permutation[v] for v in range(m) if f >> v & 1)
        result |= 1 << (g - 1)
    return result


def main():
    start = time.monotonic()
    m = 5
    ds = list(downsets(m))
    ac = list(antichain_closures(m))
    assert len(ds) == len(set(ds)) == len(ac) == len(set(ac))
    assert set(ds) == set(ac)
    nonempty = sorted(x for x in ds if x)
    records = []
    by_dimension = Counter()
    for mask in nonempty:
        L, D = matrices(mask, m)
        le = np.linalg.eigvalsh(L)[::-1]
        de = np.linalg.eigvalsh(D)[::-1]
        gaps = np.cumsum(le - de)
        k = int(np.argmin(gaps)) + 1
        faces = face_list(mask, m)
        dim = max(f.bit_count() for f in faces) - 1
        by_dimension[dim] += 1
        records.append(dict(mask=mask, n=len(L), dimension=dim,
                            min_k=k, minimum_gap=float(gaps[k-1]),
                            gaps=gaps.tolist()))
    # Representatives by full permutation orbits; the exact tier may use these.
    unseen = set(nonempty)
    permutations = list(itertools.permutations(range(m)))
    reps = []
    while unseen:
        rep = min(unseen)
        orbit = {permute_mask(rep, m, p) for p in permutations}
        assert orbit <= set(nonempty)
        unseen.difference_update(orbit)
        reps.append(dict(mask=rep, orbit_size=len(orbit)))
    assert sum(r['orbit_size'] for r in reps) == len(nonempty)
    negatives = [r for r in records if r['minimum_gap'] < -1e-9]
    intermediate = [(r['gaps'][k-1], r['mask'], k)
                    for r in records for k in range(2, r['n'])]
    result = dict(job_id=JOB, arithmetic='float64 screening, not a proof',
                  numpy_version=np.__version__, universe_vertices=m,
                  complete_generators_agree=True,
                  empty_inclusive_count=len(ds), nonempty_count=len(nonempty),
                  mask_list_sha256=hashlib.sha256(
                      (','.join(map(str, nonempty))).encode()).hexdigest(),
                  by_dimension=dict(by_dimension), records=records,
                  isomorphism_representatives=reps,
                  summary=dict(nonempty_count=len(nonempty),
                      isomorphism_classes=len(reps),
                      matrix_size_range=[min(r['n'] for r in records),
                                         max(r['n'] for r in records)],
                      tested_partial_sums=sum(r['n'] for r in records),
                      minimum_gap=min(r['minimum_gap'] for r in records),
                      minimum_intermediate_gap=min(intermediate),
                      negative_candidates=len(negatives),
                      elapsed_seconds=time.monotonic()-start))
    (ROOT/'five-vertex-census.json').write_text(json.dumps(result, indent=2)+'\n')
    for i, r in enumerate(negatives):
        L, D = matrices(r['mask'], m)
        witness = dict(r, faces=face_list(r['mask'], m), L=L.tolist(), D=D.tolist())
        (ROOT/f'five-negative-{i}.json').write_text(json.dumps(witness, indent=2)+'\n')
    print(json.dumps(result['summary'], indent=2))


if __name__ == '__main__':
    main()
