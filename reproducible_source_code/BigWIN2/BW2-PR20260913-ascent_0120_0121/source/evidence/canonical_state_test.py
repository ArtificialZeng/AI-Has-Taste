"""Test the proposed bounded-width continuation automaton against literal words."""
from pathlib import Path
from itertools import combinations
from collections import defaultdict
import json

def asc(w): return sum(u<v for u,v in zip(w,w[1:]))
def valid(w):
 return not any(u<v<t and s in (u,v) for u,v,t,s in combinations(w,4))
def state(w):
 b={u for i,u in enumerate(w) if u>0 and any(u<v for v in w[i+1:])}|{0}
 eligible=[t for t in range(asc(w)+2) if t not in b]
 h=tuple(i for i,t in enumerate(eligible) if t in w)
 assert eligible[min(h)]==w[-1]
 return len(eligible),h

def children(s):
 k,h=s; h=set(h); last=min(h)
 out=[]
 for t in range(k):
  if t<=last:
   out.append((k,tuple(sorted(h|{t}))))
  else:
   removed=sum(u<t for u in h)
   out.append((k+1-removed,tuple(sorted({u-removed for u in h if u>=t}|{t-removed}))))
 return out

level=[(0,)]
checks=0
for n in range(1,10):
 for w in level:
  if max(w)<2: continue
  s=state(w)
  assert all(cs[0]<=s[0] for cs in children(s))
  actual=sorted(state(w+(t,)) for t in range(asc(w)+2) if valid(w+(t,)))
  assert sorted(children(s))==actual,(w,s,actual,children(s))
  checks+=1
 if n<9:
  level=[w+(t,) for w in level for t in range(asc(w)+2) if valid(w+(t,))]

# Mixed binary / bounded-width DP, with each concrete append counted once.
binary={(0,0):1}; post={}; counts=[1,1]; states=[0,0]
for n in range(1,16):
 nb=defaultdict(int); np=defaultdict(int)
 for (a,last),mult in binary.items():
  for t in (0,1): nb[(a+(last<t),t)]+=mult
  for t in range(2,a+2): np[(a+1,(t-2,))]+=mult
 for s,mult in post.items():
  for cs in children(s): np[cs]+=mult
 binary=nb; post=np
 counts.append(sum(binary.values())+sum(post.values())); states.append(len(post))
assert counts[:10]==[1,1,2,5,13,34,90,244,683,1980]
out={'job_id':'primary-20260913-ascent-0120-0121-triage-ccd00a55e176','literal_successor_multiset_checks_on_postbinary_prefixes_through_n9':checks,'successor_multisets_all_match':True,'canonical_counts_n0_to_n16':counts,'postbinary_states_n0_to_n16':states,'qualification':'All-length sufficiency is a proof target; beyond n=9 counts have only this automaton verification.'}
Path('evidence/canonical-state-results.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
