"""Exhaustive variant of teven.py: enumerate all (K-1)-cliques, several C1 per clique, record every signature with
multiplicity >= K and its exact multiplicity.  usage: teven2.py W H K [perclique]"""
import sys, itertools, time
from pysat.solvers import Solver
from slither import Grid, deg_clauses, all_solutions
from teven import kernel_basis, edges_of, model
W,H,K=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]); per=int(sys.argv[4]) if len(sys.argv)>4 else 20
g=Grid(W,H); B=kernel_basis(g); k=len(B)
T=[]
for bits in range(1,1<<k):
    E=0
    for i in range(k):
        if bits>>i&1: E^=B[i]
    T.append(E)
t0=time.time()
feas=[E for E in T if model(g,[E]) is not None]
fs=set(feas); nb={E:set(F for F in feas if F!=E and (E^F) in fs) for E in feas}
print(f"{W}x{H}: dim T={k}, feasible {len(feas)} ({time.time()-t0:.0f}s)",flush=True)
def sig_rows(sig): return tuple(''.join(str(sig[g.cells.index((xx,yy))]) for xx in range(W-1)) for yy in range(H-2,-1,-1))
def canon(rows):
    vs=[rows]
    r=rows
    def rot(r): return tuple(''.join(r[len(r)-1-j][i] for j in range(len(r))) for i in range(len(r[0])))
    def flip(r): return tuple(x[::-1] for x in r)
    cands=[]
    for f in (False,True):
        r=flip(rows) if f else rows
        for _ in range(4):
            cands.append(r); r=rot(r)
    if W!=H: cands=[c for c in cands if len(c)==len(rows)]
    return min(cands)
seen={}; tested=0; hist={}
def joint_solutions(cl, limit):
    """enumerate up to `limit` cycles C1 with all C1^E cycles of the same signature"""
    nE=len(g.edges); x={e:e+1 for e in range(nE)}
    s=Solver(name='cadical195')
    copies=[set()]+[set(edges_of(E)) for E in cl]
    for Eset in copies:
        lit={e:(-x[e] if e in Eset else x[e]) for e in range(nE)}
        for c in deg_clauses(g,lit): s.add_clause(c)
        s.add_clause([lit[e] for e in range(nE)])
        for c in g.cells:
            ce=[e for e in g.cedges[c] if e in Eset]
            if not ce: continue
            h=len(ce)//2
            for bits in itertools.product([0,1],repeat=len(ce)):
                if sum(bits)!=h: s.add_clause([(-x[e] if b else x[e]) for e,b in zip(ce,bits)])
    out=[]; it=0
    while len(out)<limit and it<20000:
        it+=1
        if not s.solve(): break
        m=s.get_model(); C=set(e for e in range(nE) if m[e]>0)
        bad=False
        for Eset in copies:
            comps=g.components(C^Eset)
            if len(comps)>1:
                bad=True
                for i,j in itertools.combinations(range(len(comps)),2):
                    for F in copies:
                        s.add_clause([(x[e] if e in F else -x[e]) for e in comps[i]]+[(x[e] if e in F else -x[e]) for e in comps[j]])
        if not bad:
            out.append(C)
            s.add_clause([(-x[e] if e in C else x[e]) for e in range(nE)])
    if it>=20000: print("LIMIT", flush=True)
    s.delete(); return out
def extend(cl, cand):
    global tested
    if len(cl)==K-1:
        tested+=1
        if model(g,cl) is None: return
        for C in joint_solutions(cl, per):
            sig=g.signature(C); rows=sig_rows(sig); key=canon(rows)
            if key in seen: continue
            mult=len(all_solutions(g,sig,limit=1000)); seen[key]=mult; hist[mult]=hist.get(mult,0)+1
            print(f"multiplicity {mult} ({time.time()-t0:.0f}s, {tested} cliques):"+(" *** FIVE ***" if mult==5 else ""),flush=True)
            print('\n'.join(rows),flush=True)
        return
    for F in sorted(cand):
        extend(cl+[F], set(G for G in cand if G>F and G in nb[F]))
extend([], set(feas))
print(f"done: {tested} cliques, distinct signatures by multiplicity: {hist}  ({time.time()-t0:.0f}s)",flush=True)
