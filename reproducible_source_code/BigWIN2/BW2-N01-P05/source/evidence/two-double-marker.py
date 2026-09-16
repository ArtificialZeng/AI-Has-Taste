"""Falsification test of a strengthening; no all-k assertion is proved here."""
import sys
sys.dont_write_bytecode=True
from importlib.util import spec_from_file_location,module_from_spec
from pathlib import Path
from hashlib import sha256

HERE=Path(__file__).resolve().parent
sp=spec_from_file_location('t',HERE/'terminal-marker.py')
t=module_from_spec(sp)
sp.loader.exec_module(t)


def main():
    results=[]
    pairs=[(k,n) for k in (3,4) for n in range(2*k,17 if k==3 else 14)]
    pairs += [(5,14)]
    for k,n in pairs:
        total=0
        examples=[]
        for q in t.words(n,k):
            if sum(q.count(x)==2 for x in range(k))<2:
                continue
            total+=1
            a=q
            c=q+(k,)
            for _ in range(k-1):
                a=t.b.phi(a)
                c=t.b.phi(c)
            if t.b.sorted_word(a) and not t.b.sorted_word(c):
                examples.append(dict(q=q,q_orbit=t.b.orbit(q,k),
                    marker_orbit=t.b.orbit(q+(k,),k)))
        item=dict(k=k,n=n,enumerated=total,failures=examples)
        results.append(item)
        print(k,n,total,len(examples),examples[:1],flush=True)
        t.b.atomic_json(HERE/'two-double-marker.json',dict(
            job_id='newwin-00001-p05-research-0171927ebd6e',
            status='exact finite test of an unproved strengthening',
            statement='For run-free q with k>=3 letters, every letter at least twice and at least two letters exactly twice, phi^(k-1)(q) sorted implies phi^(k-1)(q x) sorted for a new letter x',
            script_sha256=sha256(Path(__file__).read_bytes()).hexdigest(),cases=results))


if __name__=='__main__':
    main()
