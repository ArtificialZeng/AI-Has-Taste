"""Totally even subsets, pair feasibility and clique-based search for slitherlink signatures of multiplicity >= K.
usage: teven.py W H K"""
import sys, itertools, time
from pysat.solvers import Solver
from slither import Grid, deg_clauses, all_solutions

def kernel_basis(g):
    nE=len(g.edges)
    rows=[]
    for v,es in g.vedges.items(): rows.append(sum(1<<e for e in es))
    for c in g.cells: rows.append(sum(1<<e for e in g.cedges[c]))
    # Gaussian elimination over F2: find null space of matrix (rows x nE)
    piv={}  # pivot column -> row bitmask
    red=[]
    for r in rows:
        for pc,pr in piv.items():
            if r>>pc &1: r^=pr
        if r:
            pc=(r & -r).bit_length()-1
            for k in list(piv):
                if piv[k]>>pc &1: piv[k]^=r
            piv[pc]=r
    free=[e for e in range(nE) if e not in piv]
    basis=[]
    for f in free:
        vec=1<<f
        for pc,pr in piv.items():
            if pr>>f &1: vec|=1<<pc
        basis.append(vec)
    return basis

def edges_of(mask):
    out=[];e=0
    while mask:
        if mask&1: out.append(e)
        mask>>=1;e+=1
    return out

def model(g, Es, connect=False, maxit=100000, want_clues=False):
    """find C1 such that C1 xor E is a pseudocycle (or cycle if connect) with the same signature, for all E in Es (E=0 included implicitly)"""
    nE=len(g.edges); x={e:e+1 for e in range(nE)}
    s=Solver(name='cadical195')
    copies=[set()]+[set(edges_of(E)) for E in Es]
    for Eset in copies:
        lit={e:(-x[e] if e in Eset else x[e]) for e in range(nE)}
        for cl in deg_clauses(g,lit): s.add_clause(cl)
        s.add_clause([lit[e] for e in range(nE)])
        for c in g.cells:
            ce=[e for e in g.cedges[c] if e in Eset]
            if not ce: continue
            h=len(ce)//2
            for bits in itertools.product([0,1],repeat=len(ce)):
                if sum(bits)!=h: s.add_clause([(-x[e] if b else x[e]) for e,b in zip(ce,bits)])
    it=0
    while it<maxit:
        it+=1
        if not s.solve(): s.delete(); return None
        m=s.get_model(); C=set(e for e in range(nE) if m[e]>0)
        if not connect: s.delete(); return C
        bad=False
        for Eset in copies:
            comps=g.components(C ^ Eset)
            if len(comps)>1:
                bad=True
                for i,j in itertools.combinations(range(len(comps)),2):
                    for F in copies:  # forbid loops Li,Lj together in copy F: edges of copy F are x xor F
                        s.add_clause([(x[e] if e in F else -x[e]) for e in comps[i]]+[(x[e] if e in F else -x[e]) for e in comps[j]])
        if not bad: s.delete(); return C
    s.delete(); return 'limit'

if __name__=="__main__":
    W,H,K=int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])
    g=Grid(W,H); B=kernel_basis(g); k=len(B)
    print(f"{W}x{H}: dim T = {k}", flush=True)
    T=[]
    for bits in range(1,1<<k):
        E=0
        for i in range(k):
            if bits>>i&1: E^=B[i]
        T.append(E)
    t0=time.time()
    feas=[E for E in T if model(g,[E]) is not None]
    print(f"pseudo-feasible nonzero differences: {len(feas)} of {len(T)}  ({time.time()-t0:.0f}s)", flush=True)
    fs=set(feas)
    # compatibility: E,F both feasible and E^F feasible
    nb={E:set(F for F in feas if F!=E and (E^F) in fs) for E in feas}
    # cliques of size K-1 among feas (all pairwise compatible)
    found=0; tested=0
    def extend(cl, cand):
        global found, tested
        if len(cl)==K-1:
            tested+=1
            C=model(g,cl,connect=False)
            if C is None: return False
            C=model(g,cl,connect=True)
            if C=='limit': print('LIMIT on clique', [len(edges_of(E)) for E in cl], flush=True); return False
            if C is None: return False
            sig=g.signature(C)
            sols=all_solutions(g,sig,limit=1000)
            rows=[''.join(str(sig[g.cells.index((xx,yy))]) for xx in range(W-1)) for yy in range(H-2,-1,-1)]
            print(f"FOUND signature with multiplicity {len(sols)} ({time.time()-t0:.0f}s):", flush=True)
            print('\n'.join(rows), flush=True)
            found+=1
            return True
        for F in sorted(cand):
            if extend(cl+[F], set(G for G in cand if G>F and G in nb[F])): return True
        return False
    extend([], set(feas))
    print(f"done: {tested} cliques tested, found={found}, {time.time()-t0:.0f}s", flush=True)
