#!/usr/bin/env python3
"""Independent exact verifier for serialized equality candidates.

Unlike exact_census.py, this constructs A(L(G)) explicitly and obtains its
characteristic polynomial with SymPy, then counts real roots on (-oo,0) and
(0,oo) by exact polynomial root isolation.
"""
import argparse, hashlib, json
import networkx as nx
import sympy as sp

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('candidates')
    ap.add_argument('--output', required=True)
    args=ap.parse_args()
    out=[]
    for line in open(args.candidates):
        claimed=json.loads(line); raw=claimed['graph6'].encode('ascii')
        g=nx.from_graph6_bytes(raw); lg=nx.line_graph(g)
        nodes=list(lg); A=sp.zeros(len(nodes))
        pos={v:i for i,v in enumerate(nodes)}
        for u,v in lg.edges(): A[pos[u],pos[v]]=A[pos[v],pos[u]]=1
        x=sp.symbols('x'); poly=A.charpoly(x).as_poly()
        zero_mult=0
        while poly.eval(0)==0:
            poly=sp.div(poly,sp.Poly(x,x))[0]; zero_mult+=1
        # SymPy count_roots counts distinct roots, so restore multiplicities
        # from the exact square-free factorization.
        neg=positive=0
        for fac,mult in sp.factor_list(poly)[1]:
            neg += mult*int(fac.count_roots(-sp.oo,0))
            positive += mult*int(fac.count_roots(0,sp.oo))
        inertia=[positive,zero_mult,neg]
        signature=positive-neg; c=g.number_of_edges()-g.number_of_nodes()+1
        margin=c+1-2*signature
        assert inertia==claimed['line_inertia']
        assert margin==claimed['margin']==0
        out.append({'graph6':claimed['graph6'],'edges':sorted([sorted(e) for e in g.edges()]),
                    'line_charpoly':str(A.charpoly(x).as_expr()),
                    'line_inertia':inertia,'c':c,'signature':signature,'margin':margin})
    payload={'verifier':'explicit line graph + SymPy exact charpoly root isolation',
             'sympy_version':sp.__version__,'verified':len(out),'records':out,
             'input_sha256':hashlib.sha256(open(args.candidates,'rb').read()).hexdigest()}
    with open(args.output,'w') as f: json.dump(payload,f,indent=2,sort_keys=True)
    print(json.dumps({'VERIFIED':len(out),'input_sha256':payload['input_sha256']}))

if __name__=='__main__': main()
