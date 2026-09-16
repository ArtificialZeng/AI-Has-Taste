#!/usr/bin/env python3
"""Independent subset-cardinality encoding for the sixteen order-16 examples.

No NetworkX, original encoder, IDPool, or cardinality library is used.
Exactly four vertices per color is enforced by at-most-four constraints;
the 16 exactly-once colored vertices force equality for all four colors.
"""
import hashlib
import itertools
import json
import subprocess
import time
from pathlib import Path
from pysat.solvers import Solver

ROOT=Path(__file__).resolve().parents[2]
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    started=time.monotonic();records=[]
    out=ROOT/'evidence/second_encoding';out.mkdir(exist_ok=True)
    candidates=[r for r in map(json.loads,(ROOT/'evidence/coloring_witnesses.jsonl').read_text().splitlines()) if r['classification']=='A_sat_E_unsat_observed']
    for row in candidates:
        code=row['graph6'];n=ord(code[0])-63;assert n==16
        bits=[(ord(c)-63)>>b&1 for c in code[1:] for b in range(5,-1,-1)]
        edges=[];k=0
        for v in range(n):
            for u in range(v):
                if bits[k]: edges.append((u,v))
                k+=1
        edges.sort();assert len(edges)==24
        elements=[frozenset([v]) for v in range(n)]+[frozenset(e) for e in edges]
        def x(a,c):return 4*a+c+1
        clauses=[]
        for a in range(len(elements)):
            clauses.append([x(a,c) for c in range(4)])
            clauses.extend([-x(a,c),-x(a,d)] for c,d in itertools.combinations(range(4),2))
        for a,b in itertools.combinations(range(len(elements)),2):
            conflict=(a<n and b<n and (a,b) in edges) or (bool(elements[a]&elements[b]) and b>=n)
            if conflict: clauses.extend([-x(a,c),-x(b,c)] for c in range(4))
        # Color names are interchangeable; no other symmetry constraints.
        clauses.append([x(0,0)])
        for c in range(4):
            clauses.extend([-x(v,c) for v in subset] for subset in itertools.combinations(range(n),5))
        stem=f'n16_i{row["index"]:04}'
        cnf=out/(stem+'.cnf');proof=out/(stem+'.drat');log=out/(stem+'.log')
        cnf.write_text(f'p cnf 160 {len(clauses)}\n'+''.join(' '.join(map(str,c))+' 0\n' for c in clauses))
        with Solver(name='glucose3',with_proof=True) as solver:
            solver.append_formula(clauses);assert not solver.solve()
            proof.write_text('\n'.join(solver.get_proof())+'\n')
        result=subprocess.run([str(ROOT/'tools/drat-trim'),str(cnf),str(proof)],capture_output=True,text=True)
        log.write_text(result.stdout+result.stderr)
        assert result.returncode==0 and 's VERIFIED' in result.stdout
        records.append(dict(n=n,index=row['index'],graph6=code,cnf=str(cnf.relative_to(ROOT)),
            proof=str(proof.relative_to(ROOT)),log=str(log.relative_to(ROOT)),
            cnf_sha256=sha(cnf),proof_sha256=sha(proof),log_sha256=sha(log),
            clauses=len(clauses),variables=160,status='VERIFIED'))
        print(stem+' VERIFIED',flush=True)
    report=dict(status='pass',script='evidence/scripts/second_encoding.py',records=records,
        count=len(records),seconds=time.monotonic()-started,
        solver='PySAT 1.8.dev24 glucose3 with_proof=True; default deterministic options; no randomization requested',
        checker_binary_sha256=sha(ROOT/'tools/drat-trim'),
        encoding='Proper total coloring plus every five vertices contain a vertex not colored c, for every color c; equivalent to equitable total coloring at order 16 by the local four-color star identity.')
    (ROOT/'evidence/second_encoding_verification.json').write_text(json.dumps(report,indent=2)+'\n')

if __name__=='__main__':main()
