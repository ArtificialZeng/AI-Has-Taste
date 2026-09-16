"""Exhaustive quadratic residues for all labelled 4x4 boards.

Run: python3 evidence/research_n4.py
Uses the degree-justified orbit table from triage. All arithmetic is exact.
No matrix enumeration over F_3^(16) is attempted or claimed.
"""
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import permutations
from pathlib import Path
import json
import struct
import time

from triage_orbits import canonical, hit_weights, multiply

OUT = Path(__file__).resolve().parent
JOB = 'newwin-00001-p13-research-75edfb64efc5'
TABLE = json.loads((OUT/'connected_orbits.json').read_text())
LOOKUP = {(t['rows'], t['columns'], t['mask']):
          t['orbit_polynomials_in_x'] for t in TABLE}


@lru_cache(None)
def local_key(r, c, mask):
    return (r, c, canonical(r, c, [(i,j) for i in range(r)
                     for j in range(c) if mask >> (i*c+j) & 1]))


def bounded_components(n, mask):
    """None means a component has defect at least three at every rank."""
    parent = list(range(2*n))
    def root(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v
    edges = [(k//n,k%n) for k in range(n*n) if mask >> k & 1]
    for i,j in edges:
        parent[root(i)] = root(n+j)
    groups = {}
    for i,j in edges:
        groups.setdefault(root(i), []).append((i,j))
    ans = []
    for es in groups.values():
        rows, cols = sorted({i for i,j in es}), sorted({j for i,j in es})
        r, c = len(rows), len(cols)
        if max(r,c) > 3:
            return None
        lm = sum(1 << (rows.index(i)*c+cols.index(j)) for i,j in es)
        ans.append(local_key(r,c,lm))
    return ans


def support_residue(n, mask):
    comps = bounded_components(n,mask)
    if comps is None:
        return {}
    state = {0:[1,0,0]}
    for r,c,cmask in comps:
        nxt = {}
        for d,coeff in enumerate(LOOKUP[r,c,cmask]):
            e = r+c-d-1
            if e > 2 or not any(coeff):
                continue
            shifted = ([0]*e+coeff+[0]*3)[:3]
            for old,co in state.items():
                val = multiply(co,shifted,3)
                target = nxt.setdefault(old+d,[0,0,0])
                for z in range(3):
                    target[z] += val[z]
        state = {d:co for d,co in nxt.items() if any(co)}
    return state


def exhaustive(n):
    started = time.monotonic()
    total = 1 << (n*n)
    width = 3*(n+1)
    values = [[0]*width for _ in range(total)]
    nonzero_supports = 0
    for mask in range(total):
        state = support_residue(n,mask)
        nonzero_supports += bool(state)
        for d,co in state.items():
            values[mask][3*d:3*d+3] = co
    print('supports complete', n, nonzero_supports, flush=True)
    for bit in range(n*n):
        step = 1 << bit
        for base in range(0,total,2*step):
            for lo in range(base,base+step):
                a,b = values[lo+step],values[lo]
                for z in range(width):
                    a[z] += b[z]
    print('zeta complete',n,flush=True)
    weights = hit_weights(n)
    hist = [Counter() for _ in range(n+1)]
    hits = []
    negatives = []
    pms = [sum(1 << (i*n+j) for i,j in enumerate(p))
           for p in permutations(range(n))]
    digest = sha256()
    for mask,ms in enumerate(values):
        h = [[0,0,0] for _ in range(n+1)]
        for i in range(n+1):
            for d,w in enumerate(weights[i]):
                v = multiply(ms[3*i:3*i+3],w,3)
                for z in range(3):
                    h[d][z] += v[z]
        classical = [0]*(n+1)
        for pm in pms:
            classical[(pm&mask).bit_count()] += 1
        assert [v[0] for v in h] == classical, (n,mask)
        for d,v in enumerate(h):
            hist[d][v[2]] += 1
            digest.update(struct.pack('<3q',*v))
            if v[2] < 0:
                negatives.append({'mask':mask,'d':d,'H_residue':v,
                                  'M_residues':[ms[3*i:3*i+3] for i in range(n+1)]})
        hits.append(h)
    # H_d(B)=H_d(B^T), and invariance under row/column permutations.
    symmetry_checks = 0
    for mask,h in enumerate(hits):
        trans = sum(1 << (j*n+i) for i in range(n) for j in range(n)
                    if mask >> (i*n+j) & 1)
        row_swap = sum(1 << (((1-i) if n >= 2 and i < 2 else i)*n+j)
                       for i in range(n) for j in range(n) if mask >> (i*n+j)&1)
        assert h == hits[trans] == hits[row_swap]
        symmetry_checks += 2*(n+1)*3
    # Sum over hit indices is independent of the board.
    endpoint = hits[0][0]
    for h in hits:
        assert [sum(v[z] for v in h) for z in range(3)] == endpoint
    result = {'job_id':JOB,'n':n,'boards':total,'board_index_pairs':total*(n+1),
        'method':'exact orbit residue, all-support subset zeta transform, exact hit transform',
        'dependency':'Chen--Selover Remark 2.3 and orbit-polynomial degree bound in triage_reduction.md',
        'source_sha256':sha256((OUT.parent/'source.md').read_bytes()).hexdigest(),
        'orbit_table_sha256':sha256((OUT/'connected_orbits.json').read_bytes()).hexdigest(),
        'nonzero_exact_support_residues':nonzero_supports,
        'negative_quadratic_witnesses':negatives,
        'classical_constant_comparisons':total*(n+1),
        'symmetry_coefficient_comparisons':symmetry_checks,
        'total_hit_sum_comparisons':3*total,
        'quadratic_histograms_by_d':[dict(sorted(c.items())) for c in hist],
        'quadratic_range_by_d':[[min(c),max(c)] for c in hist],
        'empty_full_H_residues':{'empty':hits[0],'full':hits[-1]},
        'H_residue_stream_sha256':digest.hexdigest(),
        'stream_format':'mask increasing, d increasing; (c0,c1,c2) signed little-endian int64',
        'elapsed_seconds':round(time.monotonic()-started,3)}
    path = OUT/f'research_n{n}_results.json'
    tmp = path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(result,indent=2)+'\n')
    tmp.replace(path)
    # Small reusable full data archive, standard-library reader.
    import gzip
    data = b''.join(struct.pack('<3q',*v) for h in hits for v in h)
    assert sha256(data).hexdigest() == digest.hexdigest()
    with (OUT/f'research_n{n}_residues.bin.gz').open('wb') as f:
        with gzip.GzipFile(filename='',mode='wb',fileobj=f,mtime=0) as gz:
            gz.write(data)
    print(json.dumps({k:result[k] for k in ('n','boards','board_index_pairs',
            'negative_quadratic_witnesses','quadratic_range_by_d','elapsed_seconds')},indent=2))
    return hits


if __name__ == '__main__':
    exhaustive(4)
