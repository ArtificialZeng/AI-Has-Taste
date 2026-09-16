"""Exact bounded definition calibration only; not a proof or new coverage result."""
from itertools import product
from math import comb
import json, platform, time

def weak(total, length):
    if length == 1:
        yield (total,)
    else:
        for a in range(total + 1):
            for tail in weak(total-a, length-1):
                yield (a,) + tail

def run(blocks, parent):
    n=sum(map(len,blocks))
    descendants=[]
    for v in range(len(blocks)):
        included=[]
        for u in range(len(blocks)):
            j=u
            while j != -1 and j != v:
                j=parent[j]
            if j == v:
                included.extend(blocks[u])
        descendants.append(tuple(included))
    ehr=[]
    for m in range(n+1):
        count=0
        for total in range(m*n+1):
            for x in weak(total,n):
                if all(sum(x[i] for i in ds)<=m*len(ds) for ds in descendants):
                    count+=1
        ehr.append(count)
    hstar=[sum((-1)**j*comb(n+1,j)*ehr[k-j] for j in range(k+1)) for k in range(n+1)]
    words=[0]*(n+1)
    for w in product(range(n),repeat=n):
        if all(sum(c in ds for c in w)>=len(ds) for ds in descendants):
            des=sum(w[i]>w[i+1] for i in range(n-1))
            words[n-1-des]+=1
    return dict(blocks=blocks,parent=parent,n=n,descendants=descendants,ehrhart_samples=ehr,hstar=hstar,word_polynomial=words,equal=hstar==words)

if __name__=='__main__':
    start=time.perf_counter()
    cases=[([[0]],[-1]),([[2,3],[0],[1]],[-1,0,0]),([[2,3],[0,1]],[-1,0]),([[4],[0,1],[2,3]],[-1,0,0]),([[4],[2,3],[0,1]],[-1,0,1]),([[4],[0],[3],[1,2]],[-1,0,0,2]),([[0],[1,2],[3,4]],[-1,0,0])]
    result=dict(python=platform.python_version(),domain='exact integers',seed=None,cases=[run(*c) for c in cases],runtime_seconds=time.perf_counter()-start,qualification='Seven finite convention checks only; no general proof or novelty claim.')
    print(json.dumps(result,ensure_ascii=False,indent=2))
