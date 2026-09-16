#!/usr/bin/env python3
"""Exact order-n census for 2 s(L(G)) <= c(G)+1.

Input is one graph6 graph per line (as emitted by nauty geng -cq n).
All inertia computations use fractions.Fraction and congruence operations.
"""
import argparse, collections, hashlib, json, sys, time
from fractions import Fraction
import networkx as nx


def exact_inertia_symmetric(a):
    """Return (positive, zero, negative) inertia using exact congruences."""
    a = [[Fraction(x) for x in row] for row in a]
    p = z = neg = 0
    while a:
        n = len(a)
        k = next((i for i in range(n) if a[i][i]), None)
        if k is None:
            edge = next(((i,j) for i in range(n) for j in range(i+1,n)
                         if a[i][j]), None)
            if edge is None:
                z += n
                break
            # Congruence e_i <- e_i+e_j creates a nonzero diagonal 2*a_ij.
            i,j = edge
            old_ii, old_ij, old_jj = a[i][i], a[i][j], a[j][j]
            for q in range(n):
                if q != i:
                    a[i][q] += a[j][q]
                    a[q][i] = a[i][q]
            a[i][i] = old_ii + 2*old_ij + old_jj
            k = i
        if k:
            a[0], a[k] = a[k], a[0]
            for row in a:
                row[0], row[k] = row[k], row[0]
        pivot = a[0][0]
        if pivot > 0: p += 1
        else: neg += 1
        a = [[a[i][j] - a[i][0]*a[0][j]/pivot
              for j in range(1,n)] for i in range(1,n)]
    return p,z,neg


def graph_record(raw):
    raw = raw.strip()
    g = nx.from_graph6_bytes(raw)
    n, m = g.number_of_nodes(), g.number_of_edges()
    q2 = [[0]*n for _ in range(n)]
    for i in range(n): q2[i][i] = g.degree(i)-2
    for i,j in g.edges(): q2[i][j]=q2[j][i]=1
    above, equal, below = exact_inertia_symmetric(q2)
    b0 = 1 if nx.is_bipartite(g) else 0  # nullity of signless Laplacian, connected case
    # Delete b0 zero eigenvalues of Q (not present among nonzero eigenvalues
    # of B^T B), then add nullity(B)=m-n+b0 copies of -2: net m-n.
    lp, lz, ln = above, equal, below + m - n
    s = lp-ln
    c = m-n+1
    margin = c+1-2*s
    return dict(graph6=raw.decode('ascii'), n=n, m=m, c=c,
                q_minus_2_inertia=[above,equal,below],
                line_inertia=[lp,lz,ln], signature=s, margin=margin,
                bipartite=bool(b0))


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--summary', required=True)
    ap.add_argument('--candidates', required=True)
    ap.add_argument('--limit', type=int)
    args=ap.parse_args()
    counts=collections.Counter(); minmargin=None; mins=[]; total=0
    h=hashlib.sha256(); t=time.time()
    with open(args.input,'rb') as f:
      for raw in f:
        raw=raw.strip()
        if not raw: continue
        h.update(raw+b'\n'); rec=graph_record(raw); total+=1
        counts[str(rec['margin'])]+=1
        if minmargin is None or rec['margin']<minmargin: minmargin=rec['margin']; mins=[rec]
        elif rec['margin']==minmargin: mins.append(rec)
        if args.limit and total>=args.limit: break
    with open(args.candidates,'w') as f:
      for r in mins: f.write(json.dumps(r,sort_keys=True)+'\n')
    summary={'graphs':total,'input_sha256_prefix_scope':h.hexdigest(),
             'minimum_margin':minmargin,'minimum_count':len(mins),
             'margin_histogram':dict(sorted(counts.items(),key=lambda x:int(x[0]))),
             'elapsed_seconds':time.time()-t,
             'convention':'signature = positive adjacency eigenvalues minus negative adjacency eigenvalues'}
    with open(args.summary,'w') as f: json.dump(summary,f,indent=2,sort_keys=True)
    print(json.dumps(summary,sort_keys=True))

if __name__=='__main__': main()
