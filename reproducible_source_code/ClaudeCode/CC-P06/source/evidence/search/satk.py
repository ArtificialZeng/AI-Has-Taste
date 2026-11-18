"""Search for a fully clued slitherlink signature shared by >= K distinct single loops.
usage: satk.py W H K [maxiter]   (W x H vertices)"""
import sys, time, itertools
from pysat.solvers import Solver
from slither import Grid, deg_clauses, all_solutions
W,H,K=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]); maxit=int(sys.argv[4]) if len(sys.argv)>4 else 10**6
g=Grid(W,H); nE=len(g.edges)
top=[0]
def nv(): top[0]+=1; return top[0]
y=[[nv() for e in range(nE)] for t in range(K)]
z={c:[nv() for k in range(5)] for c in g.cells}
s=Solver(name='cadical195')
for t in range(K):
    for cl in deg_clauses(g,{e:y[t][e] for e in range(nE)}): s.add_clause(cl)
    s.add_clause([y[t][e] for e in range(nE)])           # nonempty
for c in g.cells:
    zs=z[c]; s.add_clause(zs)
    for a,b in itertools.combinations(zs,2): s.add_clause([-a,-b])
    es=g.cedges[c]
    for t in range(K):
        for bits in itertools.product([0,1],repeat=4):
            k=sum(bits)
            s.add_clause([(-y[t][e] if b else y[t][e]) for e,b in zip(es,bits)]+[zs[k]])
# pairwise distinct
for t,u in itertools.combinations(range(K),2):
    ds=[]
    for e in range(nE):
        d=nv(); ds.append(d)
        a,b=y[t][e],y[u][e]
        # d -> a xor b
        s.add_clause([-d,a,b]); s.add_clause([-d,-a,-b])
    s.add_clause(ds)
# symmetry breaking between copies: edge count of copy t <= ... (all equal by Theorem 1), so order by first edge
t0=time.time(); it=0; cuts=0
while True:
    it+=1
    if not s.solve():
        print(f"{W}x{H} K={K}: UNSAT after {it} iterations, {cuts} cuts, {time.time()-t0:.0f}s", flush=True); break
    m=set(l for l in s.get_model() if l>0)
    bad=False
    for t in range(K):
        E=[e for e in range(nE) if y[t][e] in m]
        comps=g.components(E)
        if len(comps)>1:
            bad=True
            for i in range(len(comps)):
                for j in range(i+1,len(comps)):
                    for u in range(K):
                        s.add_clause([-y[u][e] for e in comps[i]]+[-y[u][e] for e in comps[j]]); cuts+=1
    if not bad:
        clues=tuple(next(k for k in range(5) if z[c][k] in m) for c in g.cells)
        rows=[''.join(str(clues[g.cells.index((x,yy))]) for x in range(W-1)) for yy in range(H-2,-1,-1)]
        sols=all_solutions(g,clues,limit=1000)
        print(f"{W}x{H} K={K}: FOUND after {it} iterations, {time.time()-t0:.0f}s; exact multiplicity {len(sols)}", flush=True)
        print('\n'.join(rows), flush=True)
        break
    if it>=maxit: print("iteration limit"); break
    if it%200==0: print(f"  it {it} cuts {cuts} {time.time()-t0:.0f}s", flush=True)
