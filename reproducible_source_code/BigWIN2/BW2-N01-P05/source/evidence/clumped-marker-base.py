"""Exhaustive finite base for the clumped-marker theorem, r=3.

Every RGS of profiles (2,2,2), (3,2,2), with each subset of gaps occupied
by one distinct singleton. The proof reduces arbitrary clumped marker blocks
to this finite domain. Three algorithms agree on both passes in every case.
The literal forbidden-triple implementation does not use the run-stack rule
or first-letter recursion. numba compiles its exact integer loops only.
"""
import sys
sys.dont_write_bytecode=True
import json
from collections import Counter
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from math import factorial
from pathlib import Path
import numpy as np
from numba import njit

HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('baseline',HERE/'research-pass1.py')
b=module_from_spec(sp)
sp.loader.exec_module(b)


@njit
def literal(w):
    n=len(w)
    s=np.empty(n,np.int64)
    out=np.empty(n,np.int64)
    top=0
    done=0
    for x in w:
        while True:
            s[top]=x
            forbidden=False
            for i in range(top+1):
                for j in range(i+1,top+1):
                    for k in range(j+1,top+1):
                        if s[i]==s[k] and s[i]!=s[j]:
                            forbidden=True
            if not forbidden:
                top+=1
                break
            top-=1
            out[done]=s[top]
            done+=1
    while top:
        top-=1
        out[done]=s[top]
        done+=1
    return out


def after_two(w):
    for _ in range(2):
        a=b.phi(w)
        assert a==b.recursive(w)==tuple(literal(np.array(w,dtype=np.int64)))
        w=a
    return b.sorted_word(w)


def main():
    cases=[]
    totals=[]
    for n in (6,7):
        count=0
        for q in b.rgs_profiles(n,3):
            assert sorted(Counter(q).values())==([2,2,2] if n==6 else [2,2,3])
            count+=1
            q_sorted=after_two(q)
            marked_hard=0
            for mask in range(1<<(n+1)):
                w=[]
                marker=3
                for gap in range(n+1):
                    if mask & (1<<gap):
                        w.append(marker)
                        marker+=1
                    if gap<n:
                        w.append(q[gap])
                marked_sorted=after_two(tuple(w))
                assert marked_sorted==q_sorted,(q,mask,w)
                marked_hard+=not marked_sorted
            cases.append(dict(q=q,length=n,gap_masks=1<<(n+1),
                q_sorted_after_two=q_sorted,marked_unsorted_after_two=marked_hard))
        expected=factorial(6)//(2**3*factorial(3)) if n==6 else factorial(7)//(factorial(3)*2**2*factorial(2))
        assert count==expected
        totals.append(dict(length=n,q_count=count,expected_q_count=expected,
            marked_cases=count*(1<<(n+1))))
    result=dict(job_id='newwin-00001-p05-research-6c0e4e7ea54b',
        status='complete exact finite base certificate; infinite reduction is in clumped-marker-theorem.md',
        assertion='For profiles (2,2,2) and (3,2,2), insertion of distinct singleton markers in any subset of gaps preserves whether two passes suffice',
        totals=totals,marked_cases=sum(t['marked_cases'] for t in totals),
        q_cases=len(cases),failed_cases=0,
        methods=['literal forbidden-triple stack','run-stack','first-letter recursion'],
        cases=cases,script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),
        baseline_script_sha256=sha256((HERE/'research-pass1.py').read_bytes()).hexdigest())
    b.atomic_json(HERE/'clumped-marker-base.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='cases'},indent=2))


if __name__=='__main__':
    main()
