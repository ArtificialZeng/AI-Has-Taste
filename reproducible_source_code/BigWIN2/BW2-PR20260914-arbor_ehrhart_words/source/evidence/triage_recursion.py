"""Exact triage check of two independently defined subtree recurrences.
No external dependencies; no randomness. Does not certify an infinite theorem.
"""
from math import comb
import json
from pathlib import Path
from desk_calibration import run


def convolution(a, b):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def compute(blocks, parent, m):
    children = [[] for _ in blocks]
    for v, p in enumerate(parent):
        if p >= 0:
            children[p].append(v)
    audit = []
    def visit(v):
        b = len(blocks[v])
        data = [visit(c) for c in children[v]]
        N = b + sum(t[0] for t in data)
        F = [comb(q+b-1, b-1) for q in range(m*N+1)]
        G = [comb((m+1)*b, q) for q in range((m+1)*b+1)]
        for _, fc, gc in data:
            F = convolution(F, fc)[:m*N+1]
            G = convolution(G, gc)
        G[:N] = [0]*N
        transform = [0]*((m+1)*N+1)
        for s, count in enumerate(F):
            for j in range(m*N-s+1):
                transform[N+j] += count*comb(m*N-s, j)
        assert G == transform, (blocks, parent, v, m)
        audit.append(dict(vertex=v, size=N, coefficient_identity=True))
        return N, F, G
    root = parent.index(-1)
    N, F, G = visit(root)
    return dict(m=m, ehrhart=sum(F), binomial_sum=G[N], subtrees=audit)


def main():
    supplied = json.loads(Path('evidence/desk_calibration.json').read_text())['cases']
    extra = [
        dict(blocks=[[0,1],[2,3],[4,5],[6,7]], parent=[-1,0,0,1]),
        dict(blocks=[[0],[1,2],[3,4,5],[6],[7,8]], parent=[-1,0,0,1,1]),
    ]
    cases = []
    for index, case in enumerate(supplied+extra):
        blocks, parent = case['blocks'], case['parent']
        n = sum(map(len, blocks))
        checks = [compute(blocks,parent,m) for m in range(n+1)]
        assert all(t['ehrhart'] == t['binomial_sum'] for t in checks)
        hstar = [sum((-1)**j*comb(n+1,j)*checks[k-j]['ehrhart'] for j in range(k+1)) for k in range(n+1)]
        record = dict(blocks=blocks,parent=parent,n=n,checks=checks,hstar=hstar)
        if index < len(supplied):
            direct = run(blocks,parent)
            assert direct['ehrhart_samples'] == [t['ehrhart'] for t in checks]
            assert direct['word_polynomial'] == hstar
            record['fresh_direct_lattice_and_word_check'] = True
        cases.append(record)
    print(json.dumps(dict(job_id='primary-20260914-arbor-ehrhart-words-triage-5bfaab9809a5',
                         arithmetic='exact integers', seed=None, cases=cases,
                         qualification='Seven fresh brute-force convention checks; two additional recurrence checks. Not a completeness or novelty claim.'),indent=2))

if __name__ == '__main__':
    main()
