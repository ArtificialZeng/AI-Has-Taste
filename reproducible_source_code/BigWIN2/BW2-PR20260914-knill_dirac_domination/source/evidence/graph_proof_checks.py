"""Adversarial checks after freezing graph-domination-proof.md.

Run: OPENBLAS_NUM_THREADS=1 python3 evidence/graph_proof_checks.py
Exact identities and finite characteristic-polynomial identities are separated
from float64 screens. None is a fresh referee or a proof of the infinite claim.
"""
import hashlib
import itertools
import json
import time
from collections import Counter
from pathlib import Path

import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent
JOB = 'primary-20260914-knill-dirac-domination-research-6e957123a5e9'


def graph_matrices(v, edges):
    edges = sorted(set(tuple(sorted(e)) for e in edges))
    faces = [(u,) for u in range(v)] + edges
    e = len(edges)
    B = np.zeros((v, e), dtype=np.int64)
    C = np.zeros((v, e), dtype=np.int64)
    for j, (a, b) in enumerate(edges):
        B[a, j] = B[b, j] = 1
        C[a, j], C[b, j] = -1, 1
    L = np.array([[int(bool(set(a) & set(b))) for b in faces] for a in faces])
    D = np.block([[np.zeros((v,v), dtype=np.int64), C],
                  [C.T, np.zeros((e,e), dtype=np.int64)]])
    block_L = np.block([[np.eye(v,dtype=np.int64), B],
                        [B.T, B.T@B-np.eye(e,dtype=np.int64)]])
    assert np.array_equal(L, block_L)
    Q, H = B@B.T, C@C.T
    deg = np.diag(Q)
    assert np.array_equal(Q+H, 2*np.diag(deg))
    assert np.all(np.abs(D)+np.eye(v+e,dtype=np.int64) <= L)
    adjacency = [[] for _ in range(v)]
    for a,b in edges:
        adjacency[a].append(b); adjacency[b].append(a)
    colors, components, bipartite = {}, 0, True
    for u in range(v):
        if u in colors:
            continue
        components += 1
        colors[u] = 1
        stack = [u]
        while stack:
            a = stack.pop()
            for b in adjacency[a]:
                if b not in colors:
                    colors[b] = -colors[a]; stack.append(b)
                elif colors[b] == colors[a]:
                    bipartite = False
    if bipartite:
        signs=np.array([colors[a] for a in range(v)])
        assert np.array_equal(signs[:,None]*H*signs[None,:],Q)
    return edges, L, D, Q, H, deg, components, bipartite


def screen(v, edges, name):
    edges,L,D,Q,H,deg,c,bip = graph_matrices(v,edges)
    e=len(edges); n=v+e
    le=np.linalg.eigvalsh(L)[::-1]
    de=np.linalg.eigvalsh(D)[::-1]
    q=np.maximum(np.linalg.eigvalsh(Q)[::-1],0)
    h=np.maximum(np.linalg.eigvalsh(H)[::-1],0)
    ds=np.sort(deg)[::-1]
    f=(q+np.sqrt(q*q+4))/2
    gap=np.cumsum(le-de)
    tol=1e-6
    assert np.max(np.abs(le[:v]-f))<tol
    assert all(x < 0 for x in le[v:])
    assert np.max(np.abs(np.cumsum(de)[:v]-np.cumsum(np.sqrt(h))))<tol
    assert all(h<=2*ds+tol)
    assert all(np.cumsum(q)>=np.cumsum(ds)-tol)
    rbound=(np.sqrt(q[0]**2+4)-2)/2
    detailed=rbound+np.cumsum((np.sqrt(ds)-np.sqrt(2))**2)/2
    assert all(gap[:v]>=detailed-tol)
    if bip:
        assert np.max(np.abs(q-h))<tol
        assert all(gap[:v]>=np.arange(1,v+1)/2-tol)
    else:
        assert q[0]>=4-tol
        assert all(gap[:v]>=np.sqrt(5)-1-tol)
    assert all(gap[v-1:] >= (v+c)/2-tol)
    assert min(gap)>=1-tol
    return dict(name=name,v=v,e=e,components=c,bipartite=bip,
                minimum_gap=float(min(gap)),min_k=int(np.argmin(gap))+1,
                q1=float(q[0]),initial_bound=float(rbound),tail_bound=(v+c)/2)


def exact_case(v,edges,name):
    edges,L,D,Q,H,deg,c,bip=graph_matrices(v,edges)
    x=sp.Symbol('x'); e=len(edges)
    actual=sp.Matrix(L).charpoly(x).as_expr()
    transformed=sp.cancel((x+1)**(e-v)*
                         ((x*x-1)*sp.eye(v)-x*sp.Matrix(Q)).det())
    assert sp.expand(actual-transformed)==0
    return dict(name=name,v=v,edges=edges,L=L.tolist(),D=D.tolist(),
                charpoly_L=str(actual),charpoly_D=str(sp.Matrix(D).charpoly(x).as_expr()),
                charpoly_Q=str(sp.Matrix(Q).charpoly(x).as_expr()),
                exact_spectral_transform_identity=True)


def main():
    start=time.monotonic()
    proof_hash=hashlib.sha256((ROOT/'graph-domination-proof.md').read_bytes()).hexdigest()
    counts=Counter(); minima={}; totals=Counter()
    for v in range(1,7):
        possible=list(itertools.combinations(range(v),2))
        best=None
        for mask in range(1<<len(possible)):
            edges=[edge for i,edge in enumerate(possible) if mask>>i&1]
            r=screen(v,edges,f'labeled-{v}-{mask}')
            counts[v]+=1; totals['bipartite' if r['bipartite'] else 'nonbipartite']+=1
            totals['partial_sums']+=v+len(edges)
            if best is None or r['minimum_gap']<best['minimum_gap']:
                best=dict(r,edges=edges)
        minima[v]=best
        print(json.dumps({'completed_vertex_order':v,'graphs':counts[v]}),flush=True)
    held=[]
    for v in [7,8,15,16,31,32]:
        held.append(screen(v,[(i,i+1) for i in range(v-1)],f'path-{v}'))
        held.append(screen(v,[(i,(i+1)%v) for i in range(v)],f'cycle-{v}'))
        held.append(screen(v,[(0,i) for i in range(1,v)],f'star-{v}'))
        held.append(screen(v,[(i,i+1) for i in range(0,v-1,2)],f'matching-{v}'))
    for v in [7,10,16]:
        held.append(screen(v,list(itertools.combinations(range(v),2)),f'complete-{v}'))
    for a,b in [(2,9),(3,8),(8,8),(16,16)]:
        held.append(screen(a+b,[(i,a+j) for i in range(a) for j in range(b)],
                           f'complete-bipartite-{a}-{b}'))
    held.append(screen(13,[(0,1),(1,2),(0,2),(3,4),(4,5),(5,6),(7,8)],
                       'odd-cycle-path-edge-four-isolates'))
    examples=[(1,[],'singleton'),(2,[(0,1)],'single-edge'),
              (3,[(0,1),(1,2)],'path-3'),
              (3,[(0,1),(1,2),(0,2)],'unfilled-triangle'),
              (4,[(0,1),(1,2),(2,3),(0,3)],'cycle-4'),
              (4,[(0,1),(1,2),(0,2),(2,3)],'triangle-pendant'),
              (6,[(0,1),(2,3)],'matching-two-isolates')]
    exact=[exact_case(*args) for args in examples]
    result=dict(job_id=JOB,proof_sha256_before_tests=proof_hash,
                numpy_version=np.__version__,sympy_version=sp.__version__,
                arithmetic={'matrix_identities':'exact int64; entries and sizes prevent overflow',
                            'spectral_screens':'float64; tolerance 1e-6; not proof certificates',
                            'symbolic_examples':'exact SymPy integer polynomial identities'},
                exhaustive_counts=dict(counts),exhaustive_minima=minima,
                held_out_cases=held,exact_examples=exact,
                summary=dict(exhaustive_labeled_graphs=sum(counts.values()),
                             exhaustive_partial_sums=totals['partial_sums'],
                             bipartite=totals['bipartite'],nonbipartite=totals['nonbipartite'],
                             held_out_cases=len(held),exact_examples=len(exact),
                             all_assertions_passed=True,
                             elapsed_seconds=time.monotonic()-start))
    (ROOT/'graph-proof-checks.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['summary'],indent=2))


if __name__=='__main__':
    main()
