"""Deterministic held-out tests; not used in the finite-base induction proof."""
import sys
sys.dont_write_bytecode=True
import json
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('basecheck',HERE/'clumped-marker-base.py')
c=module_from_spec(sp)
sp.loader.exec_module(c)
b=c.b


def time(w,r):
    t=0
    while not b.sorted_word(w):
        v=b.phi(w)
        assert v==b.recursive(w)==tuple(c.literal(np.array(w,dtype=np.int64)))
        w=v
        t+=1
        assert t<=r
    return t


def main():
    tests=[]
    for r in (4,5):
        for n in (2*r,2*r+1):
            total=0
            old=0
            for q in b.rgs_profiles(n,r):
                old+=1
                tq=time(q,r)
                # Whole, alternating, and internal-only gap sets; each new
                # letter's block has 1, 2 or 3 copies, and some gaps contain
                # two adjacent blocks of different new letters.
                masks=(range(n+1),range(0,n+1,2),range(1,n))
                for positions in masks:
                    positions=set(positions)
                    w=[]
                    marker=r
                    for gap in range(n+1):
                        if gap in positions:
                            w.extend([marker]*(1+gap%3))
                            marker+=1
                            if gap%3==0:
                                w.extend([marker]*2)
                                marker+=1
                        if gap<n:
                            w.append(q[gap])
                    tw=time(tuple(w),r)
                    assert (tw==r)==(tq==r),(q,w,tq,tw)
                    total+=1
            tests.append(dict(r=r,length=n,old_words=old,marked_cases=total,failures=0))
            print(tests[-1],flush=True)
    boundaries=[]
    for q,r in [((0,1,0,1),2),((0,1,0,2,1,0,2),3),((0,1,2,0,1,2,0,2),3)]:
        qo=b.orbit(q,r)
        mo=b.orbit(q+(r,),r)
        boundaries.append(dict(q=q,q_time=time(q,r),marked_time=time(q+(r,),r),
            q_orbit=qo,marked_orbit=mo))
    result=dict(job_id='newwin-00001-p05-research-6c0e4e7ea54b',
        status='held-out finite corroboration and boundary checks, not the proof',
        cases=tests,boundaries=boundaries,
        script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    b.atomic_json(HERE/'clumped-marker-heldout.json',result)


if __name__=='__main__':
    main()
