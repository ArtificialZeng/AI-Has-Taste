"""Sequential exact B2 falsification search; numba only compiles integer loops.

One RGS per relabeling class, all letters >=2, at least two letters exactly 2,
and no adjacent equal letters. Two separately expressed maps check every pass.
No randomness, parallelism, or floating point mathematical decisions.
"""
import sys
sys.dont_write_bytecode = True
import json
from hashlib import sha256
from pathlib import Path
from time import monotonic
import numpy as np
from numba import njit


@njit
def stack_map(w):
    n=len(w)
    stack=np.empty(n,np.int64)
    out=np.empty(n,np.int64)
    counts=np.zeros(n+1,np.int64)
    top=0
    done=0
    for x in w:
        while counts[x] and stack[top-1]!=x:
            top-=1
            y=stack[top]
            counts[y]-=1
            out[done]=y
            done+=1
        stack[top]=x
        top+=1
        counts[x]+=1
    while top:
        top-=1
        out[done]=stack[top]
        done+=1
    return out


@njit
def rec_slice(w,lo,hi,out,offset):
    if lo==hi:
        return offset
    a=w[lo]
    start=lo+1
    m=1
    for i in range(lo+1,hi):
        if w[i]==a:
            offset=rec_slice(w,start,i,out,offset)
            start=i+1
            m+=1
    offset=rec_slice(w,start,hi,out,offset)
    for _ in range(m):
        out[offset]=a
        offset+=1
    return offset


@njit
def recursive_map(w):
    out=np.empty(len(w),np.int64)
    assert rec_slice(w,0,len(w),out,0)==len(w)
    return out


@njit
def sorted_word(w):
    seen=0
    prev=-1
    for x in w:
        if x!=prev:
            if seen & (1<<x):
                return False
            seen |= 1<<x
            prev=x
    return True


@njit
def sorting_time(w,k):
    t=0
    while not sorted_word(w):
        s=stack_map(w)
        assert np.array_equal(s,recursive_map(w))
        w=s
        t+=1
        assert t<=k
    return t


@njit
def visit(w,counts,k,n,pos,used,need,over,hist,examples):
    left=n-pos
    if need>left or over>k-2:
        return
    if not left:
        a=sorting_time(w,k)
        marked=np.empty(n+1,np.int64)
        marked[:n]=w
        marked[n]=k
        b=sorting_time(marked,k)
        assert a<=b<=a+1
        if a==k-1 and b==k and hist[a,b]<len(examples):
            examples[hist[a,b],:]=w
        hist[a,b]+=1
        return
    for x in range(min(k,used+1)):
        if pos and w[pos-1]==x:
            continue
        old=counts[x]
        counts[x]+=1
        w[pos]=x
        visit(w,counts,k,n,pos+1,max(used,x+1),need-(old<2),
              over+(old==2),hist,examples)
        counts[x]-=1


def run(k,n):
    start=monotonic()
    hist=np.zeros((k+1,k+1),np.int64)
    examples=np.zeros((20,n),np.int64)
    visit(np.empty(n,np.int64),np.zeros(k,np.int64),k,n,0,0,2*k,0,hist,examples)
    failures=int(hist[k-1,k])
    result=dict(job_id='newwin-00001-p05-research-6c0e4e7ea54b',
        status='complete exact finite search; no infinite proof',r=k,n=n,
        enumerated=int(hist.sum()),b2_failures=failures,
        time_histogram=[[a,b,int(hist[a,b])] for a,b in zip(*np.nonzero(hist))],
        first_counterexamples=examples[:min(20,failures)].tolist(),
        validation='stack map equals first-letter recursive map on every visited iterate',
        script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=monotonic()-start)
    # numpy indices are converted explicitly; all recorded counts are exact.
    result['time_histogram']=[[int(a),int(b),c] for a,b,c in result['time_histogram']]
    path=Path(__file__).with_name(f'b2-r{k}-n{n}.json')
    tmp=path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(result,indent=2)+'\n')
    tmp.replace(path)
    print(json.dumps(result),flush=True)


if __name__=='__main__':
    r=int(sys.argv[1])
    assert 3<=r<62
    for n in map(int,sys.argv[2:]):
        assert n>=2*r
        run(r,n)
