"""Fully clued slitherlink tools. Vertex grid W x H (W columns of vertices, H rows); cells (W-1) x (H-1)."""
import itertools
from pysat.solvers import Solver

class Grid:
    def __init__(self, W, H):
        self.W, self.H = W, H
        self.edges = []          # (v1, v2) with v=(x,y)
        self.eid = {}
        for y in range(H):
            for x in range(W-1):
                self._add((x,y),(x+1,y))
        for y in range(H-1):
            for x in range(W):
                self._add((x,y),(x,y+1))
        self.vedges = {(x,y):[] for x in range(W) for y in range(H)}
        for i,(a,b) in enumerate(self.edges):
            self.vedges[a].append(i); self.vedges[b].append(i)
        self.cells = [(x,y) for y in range(H-1) for x in range(W-1)]
        self.cedges = {}
        for (x,y) in self.cells:
            self.cedges[(x,y)] = [self.eid[((x,y),(x+1,y))], self.eid[((x,y+1),(x+1,y+1))],
                                  self.eid[((x,y),(x,y+1))], self.eid[((x+1,y),(x+1,y+1))]]
    def _add(self,a,b):
        self.eid[(a,b)] = len(self.edges); self.edges.append((a,b))
    def signature(self, E):
        S=set(E); return tuple(sum(e in S for e in self.cedges[c]) for c in self.cells)
    def components(self, E):
        """list of edge-sets of connected components of the edge set E"""
        adj={}
        for e in E:
            a,b=self.edges[e]; adj.setdefault(a,[]).append((b,e)); adj.setdefault(b,[]).append((a,e))
        seen=set(); comps=[]
        for v in adj:
            if v in seen: continue
            st=[v]; seen.add(v); ce=set()
            while st:
                u=st.pop()
                for w,e in adj[u]:
                    ce.add(e)
                    if w not in seen: seen.add(w); st.append(w)
            comps.append(ce)
        return comps
    def is_cycle(self, E):
        E=set(E)
        if not E: return False
        deg={}
        for e in E:
            for v in self.edges[e]: deg[v]=deg.get(v,0)+1
        if any(d!=2 for d in deg.values()): return False
        return len(self.components(E))==1

def deg_clauses(g, var):
    """each vertex has degree 0 or 2 among edges var[e]"""
    cl=[]
    for v,es in g.vedges.items():
        for e in es:
            cl.append([-var[e]]+[var[f] for f in es if f!=e])
        for a,b,c in itertools.combinations(es,3):
            cl.append([-var[a],-var[b],-var[c]])
    return cl

def count_patterns_clauses(g, var, cell, k):
    """clauses forcing exactly k of the 4 edges of cell to be true"""
    es=g.cedges[cell]; cl=[]
    for bits in itertools.product([0,1],repeat=4):
        if sum(bits)!=k:
            cl.append([(-var[e] if b else var[e]) for e,b in zip(es,bits)])
    return cl

def all_solutions(g, clues, limit=10**6, solver_name='cadical195'):
    """all single-loop solutions of a fully clued grid (clues: tuple over g.cells)"""
    var={e:e+1 for e in range(len(g.edges))}
    s=Solver(name=solver_name)
    for c in deg_clauses(g,var): s.add_clause(c)
    for cell,k in zip(g.cells,clues):
        for c in count_patterns_clauses(g,var,cell,k): s.add_clause(c)
    sols=[]
    while s.solve():
        m=s.get_model(); E=[e for e in range(len(g.edges)) if m[e]>0]
        comps=g.components(E)
        if len(comps)==1:
            sols.append(frozenset(E))
            s.add_clause([-var[e] if e in E else var[e] for e in range(len(g.edges))])
            if len(sols)>=limit: break
        else:
            # forbid each loop as a proper sub-loop: all edges of L present -> some edge outside L... use pairwise loop clauses
            for i in range(len(comps)):
                for j in range(i+1,len(comps)):
                    s.add_clause([-var[e] for e in comps[i]]+[-var[e] for e in comps[j]])
    s.delete()
    return sols

def parse(rows):
    """rows: list of strings top row first, each char a clue; returns (Grid, clues in g.cells order (y from bottom))"""
    Hc=len(rows); Wc=len(rows[0]); g=Grid(Wc+1,Hc+1)
    clues=tuple(int(rows[Hc-1-y][x]) for (x,y) in g.cells)
    return g,clues

if __name__=="__main__":
    tests={'knuth 6x6 (4 loops)':["322222","222232","222222","222222","232222","222223"],
           'knuth 5x5 a':["12221","21012","20002","21012","12221"],
           'knuth 5x5 b':["32223","21112","21012","21112","32223"],
           'knuth 5x5 c':["32223","23232","22022","23232","32223"],
           'beluhov fig10 (3)':["2222123","2322222","2222222","2222222","2222222","2222232","3212222"],
           '2x2':["32","23"]}
    for name,rows in tests.items():
        g,cl=parse(rows); print(name, len(all_solutions(g,cl)))
