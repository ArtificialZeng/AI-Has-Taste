#!/usr/bin/env python3
"""Exact target-clique decision for the two-row coprime grid (stdlib only)."""
import argparse, math, platform, sys, time

def color_sort(p, adj):
    order=[]; bounds=[]; color=0; rem=p
    while rem:
        color += 1; avail=rem
        while avail:
            bit=avail & -avail; v=bit.bit_length()-1
            order.append(v); bounds.append(color)
            rem ^= bit; avail ^= bit; avail &= ~adj[v]
    return order,bounds

def decide(adj,target):
    stack=[]; answer=[]; nodes=0
    sys.setrecursionlimit(5000)
    def expand(p):
        nonlocal nodes,answer
        nodes += 1; order,bounds=color_sort(p,adj)
        for i in range(len(order)-1,-1,-1):
            if len(stack)+bounds[i] < target: return False
            v=order[i]; bit=1<<v; stack.append(v)
            if len(stack)==target: answer=stack.copy(); return True
            q=p & adj[v]
            if q and expand(q): return True
            stack.pop(); p &= ~bit
        return False
    ok=expand((1<<len(adj))-1) if len(adj)>=target else False
    return ok,answer,nodes

def compatible(a,b,d):
    z=(a,a+d,b,b+d)
    return len(set(z))==4 and all(math.gcd(z[i],z[j])==1 for i in range(4) for j in range(i+1,4))

def run(x,target,path):
    t=time.perf_counter(); found=None
    with open(path,'w',encoding='ascii') as f:
        f.write('algorithm=exact_gcd_graph_greedy_coloring_branch_and_bound\n')
        f.write(f'python={platform.python_version()} x={x} target={target}\n')
        for d in range(2,x-1,2):
            vals=[v for v in range(2,x-d+1) if math.gcd(v,v+d)==1]
            adj=[0]*len(vals)
            for i,a in enumerate(vals):
                for j in range(i+1,len(vals)):
                    if compatible(a,vals[j],d): adj[i]|=1<<j; adj[j]|=1<<i
            ok,ans,nodes=decide(adj,target)
            f.write(f'd={d} vertices={len(vals)} nodes={nodes} result={"SAT" if ok else "UNSAT"}\n')
            if ok:
                found=(d,[vals[i] for i in ans]); break
        if found:
            f.write(f'witness_d={found[0]}\nwitness_V={",".join(map(str,found[1]))}\n')
        f.write(f'overall={"SAT" if found else "UNSAT"} elapsed_seconds={time.perf_counter()-t:.9f}\n')
    print('SAT' if found else 'UNSAT',x,target,found,time.perf_counter()-t,flush=True)
    return found

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('x',type=int); p.add_argument('target',type=int); p.add_argument('log')
    a=p.parse_args(); sys.exit(0 if run(a.x,a.target,a.log) else 1)
