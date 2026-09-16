"""Exact event-profile tests. Finite degree coverage; no all-degree claim."""
from collections import defaultdict
from pathlib import Path
import json, hashlib, time
JOB = "primary-20260914-bigdescent-logconcavity-research-ff87ce2dd87c"
START = time.perf_counter()
# Edges indexed by old suffix state (A,B,C), each (new state,event).
EDGES = (((0,0),(1,0)), ((0,1),(2,1)), ((0,1),(2,0)))
PAIR = [[] for _ in range(3)]
for a in range(3):
 for b in range(3):
  for aa,x in EDGES[a]:
   for bb,y in EDGES[b]: PAIR[x+y].append((3*a+b,3*aa+bb,x))
def step(v,e):
 out={}
 for (s,d),value in v.items():
  for old,new,inc in PAIR[e]:
   if old==s: out[new,d+inc]=out.get((new,d+inc),0)+value
 return out
ACCEPT=(4,5,7,8)
def value(v,k):return sum(v.get((s,k),0) for s in ACCEPT)
K=7
counts=[0]*(K+1)
first_bad=None
min_positive=[None]*(K+1)
initial={(s,0):1 for s in (0,2,6,8)}
def visit(v,total,profile):
 global first_bad
 if total and total%2==0:
  k=total//2
  for tail in (False,True):
   vv=step(v,0) if tail else v
   p=profile+(0,) if tail else profile
   counts[k]+=1
   d=value(vv,k)-value(vv,k-1)
   if d<0 and first_bad is None:
    first_bad={"k":k,"profile":p,"central":value(vv,k),"adjacent":value(vv,k-1),"difference":d}
   if d>0 and (min_positive[k] is None or d<min_positive[k]):min_positive[k]=d
 if total>=2*K:return
 for zero in (False,True):
  vv=step(v,0) if zero else v
  pp=profile+(0,) if zero else profile
  for e in (1,2):
   if total+e<=2*K:visit(step(vv,e),total+e,pp+(e,))
# Leading zero optional; subsequent optional zeros are handled before each event.
# Start with the first event here to avoid double-counting leading zeros.
for lead in (False,True):
 v=step(initial,0) if lead else initial
 p=(0,) if lead else ()
 for e in (1,2):visit(step(v,e),e,p+(e,))
out={"job_id":JOB,"arithmetic":"exact Python integers","degree_k_max":K,
 "profile_counts_by_k":counts,"first_negative_coefficient":first_bad,
 "smallest_positive_difference_by_k":min_positive,
 "coverage":"All profiles in {0,1,2} of total degree 2k, after replacing each nonempty zero run by one zero; 1<=k<=K. Includes zero-count and boundary profiles.",
 "compression":"No-event transfer P is idempotent, hence P tensor P is idempotent. Every coefficient profile compresses to length <=4k+1, independent of n.",
 "qualification":"Together with the proved transfer and compression, this verifies coefficientwise LC at these fixed k for all n. It does not prove all k, a fresh audit, or novelty.",
 "seconds":time.perf_counter()-START,
 "source_sha256":hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
 "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
