#!/usr/bin/env python3
"""Cross-check census evaluator against explicit line-graph characteristic polynomials."""
import argparse, json
import networkx as nx
import sympy as sp
from exact_census import graph_record

def charpoly_inertia(g):
    L=nx.line_graph(g); nodes=list(L); A=sp.zeros(len(nodes)); ix={v:i for i,v in enumerate(nodes)}
    for u,v in L.edges(): A[ix[u],ix[v]]=A[ix[v],ix[u]]=1
    x=sp.symbols('x'); p=A.charpoly(x).as_poly(); z=0
    while p.eval(0)==0: p=sp.div(p,sp.Poly(x,x))[0]; z+=1
    neg=pos=0
    for f,m in sp.factor_list(p)[1]:
        neg += m*int(f.count_roots(-sp.oo,0)); pos += m*int(f.count_roots(0,sp.oo))
    return [pos,z,neg]

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input'); ap.add_argument('--stride',type=int,default=2500)
    ap.add_argument('--output',required=True); a=ap.parse_args(); checked=[]
    for i,line in enumerate(open(a.input,'rb')):
        if i%a.stride: continue
        raw=line.strip(); rec=graph_record(raw); direct=charpoly_inertia(nx.from_graph6_bytes(raw))
        assert rec['line_inertia']==direct, (i,rec,direct)
        checked.append({'index0':i,'graph6':rec['graph6'],'inertia':direct})
    with open(a.output,'w') as f: json.dump({'stride':a.stride,'checked':len(checked),'records':checked},f,indent=2)
    print('CROSSCHECK_OK',len(checked))
if __name__=='__main__': main()
