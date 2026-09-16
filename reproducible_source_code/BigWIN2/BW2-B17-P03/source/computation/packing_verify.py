#!/usr/bin/env python3
"""Independent exact verifier using prime-support set packing, not gcd edges."""
import argparse, math, platform, sys, time

def support(n):
    out=[]; p=2
    while p*p<=n:
        if n%p==0:
            out.append(p)
            while n%p==0: n//=p
        p += 1 if p==2 else 2
    if n>1: out.append(n)
    return frozenset(out)

def bound_order(candidates, disjoint):
    # A proper greedy coloring of the disjointness graph bounds a packing.
    rem=candidates; order=[]; colors=[]; c=0
    while rem:
        c+=1; avail=rem
        while avail:
            b=avail & -avail; i=b.bit_length()-1
            order.append(i); colors.append(c); rem^=b; avail^=b
            avail &= ~disjoint[i]
    return order,colors

def has_packing(masks,target):
    disjoint=[0]*len(masks)
    for i in range(len(masks)):
        for j in range(i+1,len(masks)):
            if masks[i].isdisjoint(masks[j]): disjoint[i]|=1<<j; disjoint[j]|=1<<i
    chosen=[]; answer=[]; nodes=0
    def visit(candidates):
        nonlocal nodes,answer
        nodes+=1; order,colors=bound_order(candidates,disjoint)
        for k in range(len(order)-1,-1,-1):
            if len(chosen)+colors[k] < target: return False
            i=order[k]; bit=1<<i; chosen.append(i)
            if len(chosen)==target: answer=chosen.copy(); return True
            q=candidates & disjoint[i]
            if q and visit(q): return True
            chosen.pop(); candidates &= ~bit
        return False
    ok=visit((1<<len(masks))-1) if len(masks)>=target else False
    return ok,answer,nodes

def verify_witness(x,d,vs,target):
    nums=[z for v in vs for z in (v,v+d)]
    assert len(vs)==target and d>0 and all(2<=v<=x-d for v in vs)
    assert len(nums)==len(set(nums))
    assert all(math.gcd(nums[i],nums[j])==1 for i in range(len(nums)) for j in range(i+1,len(nums)))

def run(x,target,path):
    t=time.perf_counter(); overall=False
    prime_support=[support(n) for n in range(x+1)]
    with open(path,'w',encoding='ascii') as f:
        f.write('algorithm=exact_prime_support_set_packing_greedy_coloring_branch_and_bound\n')
        f.write(f'python={platform.python_version()} x={x} target={target}\n')
        for d in range(2,x-1,2):
            vals=[]; masks=[]
            for v in range(2,x-d+1):
                a,b=prime_support[v],prime_support[v+d]
                if a.isdisjoint(b): vals.append(v); masks.append(a|b)
            ok,ans,nodes=has_packing(masks,target)
            f.write(f'd={d} candidates={len(vals)} nodes={nodes} result={"SAT" if ok else "UNSAT"}\n')
            if ok:
                vs=[vals[i] for i in ans]; verify_witness(x,d,vs,target)
                f.write(f'witness_d={d}\nwitness_V={",".join(map(str,vs))}\n'); overall=True; break
        f.write(f'overall={"SAT" if overall else "UNSAT"} elapsed_seconds={time.perf_counter()-t:.9f}\n')
    print('SAT' if overall else 'UNSAT',x,target,time.perf_counter()-t)
    return overall

if __name__=='__main__':
    p=argparse.ArgumentParser(); p.add_argument('x',type=int); p.add_argument('target',type=int); p.add_argument('log')
    a=p.parse_args(); sys.exit(0 if run(a.x,a.target,a.log) else 1)
