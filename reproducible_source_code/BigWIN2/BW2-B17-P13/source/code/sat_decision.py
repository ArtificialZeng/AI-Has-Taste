#!/usr/bin/env python3
"""Generate/solve the exact decision CNF |A+A| >= target.

Lingeling proof output is discovery provenance until checked independently.
"""
import argparse, json, platform, time
from pysat.card import CardEnc, EncType
from pysat.formula import CNF, IDPool
from pysat.solvers import Solver
import pysat

def build(n,k,target):
    pool=IDPool(); cnf=CNF(); x={i:pool.id(f'x_{i}') for i in range(1,n+1)}
    cnf.extend(CardEnc.equals(list(x.values()),bound=k,vpool=pool,encoding=EncType.seqcounter).clauses)
    cnf.append([x[1]])
    reps={s:[] for s in range(2,2*n+1)}
    for i in range(1,n+1):
      for j in range(i,n+1):
        if i==j: z=x[i]
        else:
          z=pool.id(f'z_{i}_{j}')
          cnf.extend([[-z,x[i]],[-z,x[j]],[-x[i],-x[j],z]])
        reps[i+j].append(z)
    ys=[]
    for s,zs in reps.items():
      y=pool.id(f'y_{s}'); ys.append(y)
      cnf.extend([[-z,y] for z in zs]); cnf.append([-y,*zs])
    if target > len(ys):
      cnf.append([])
    elif target > 0:
      cnf.extend(CardEnc.atleast(ys,bound=target,vpool=pool,encoding=EncType.seqcounter).clauses)
    return cnf,pool,x,ys

def main():
 p=argparse.ArgumentParser(); p.add_argument('--n',type=int,default=38); p.add_argument('--k',type=int,default=12)
 p.add_argument('--target',type=int,required=True); p.add_argument('--cnf',required=True); p.add_argument('--result',required=True)
 p.add_argument('--proof'); p.add_argument('--solver',default='lingeling'); a=p.parse_args()
 cnf,pool,x,ys=build(a.n,a.k,a.target); cnf.to_file(a.cnf)
 t=time.time()
 with Solver(name=a.solver,bootstrap_with=cnf.clauses,with_proof=bool(a.proof)) as s:
  sat=s.solve(); model=s.get_model() if sat else None; proof=s.get_proof() if (not sat and a.proof) else None
  stats=s.accum_stats()
 if proof is not None:
  with open(a.proof,'w') as f: f.write('\n'.join(proof)); f.write('\n')
 chosen=[i for i,v in x.items() if model and model[v-1]>0] if sat else None
 out={'purpose':'exact decision; UNSAT requires independent proof checking','python':platform.python_version(),
      'pysat':pysat.__version__,'parameters':vars(a),'variables':pool.top,'clauses':len(cnf.clauses),
      'satisfiable':sat,'set':chosen,'elapsed_seconds':time.time()-t,'solver_stats':stats,
      'proof_lines':len(proof) if proof is not None else None}
 with open(a.result,'w') as f: json.dump(out,f,indent=2,sort_keys=True); f.write('\n')
 print(json.dumps(out,indent=2,sort_keys=True))
if __name__=='__main__': main()
