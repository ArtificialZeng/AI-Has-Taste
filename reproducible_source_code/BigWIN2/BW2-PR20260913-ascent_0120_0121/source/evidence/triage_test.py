"""Exact triage tests; run with python3 evidence/triage_test.py."""
from itertools import combinations
from collections import defaultdict
from pathlib import Path
import json, hashlib

N=9
EXPECTED=[1,1,2,5,13,34,90,244,683,1980]
PATTERNS={(0,1,2,0),(0,1,2,1)}
def asc(w): return sum(a<b for a,b in zip(w,w[1:]))
def red(w):
 d={v:i for i,v in enumerate(sorted(set(w)))}
 return tuple(d[v] for v in w)
def valid(w):
 return all(red(q) not in PATTERNS for q in combinations(w,4))
def children(w):
 return tuple(t for t in range(asc(w)+2) if valid(w+(t,)))
def forbidden(w):
 b=set()
 for u,v,t in combinations(w,3):
  if u<v<t: b.update((u,v))
 return frozenset(b)
def simplified_forbidden(w):
 b={u for i,u in enumerate(w) if u>0 and any(u<v for v in w[i+1:])}
 if max(w)>=2: b.add(0)
 return frozenset(b)
def compact_state(w):
 return (asc(w),w[-1],max(w),len(set(w)),len(forbidden(w)))

# Baseline: all ascent sequences, unpruned by avoidance; full quadruple reduction.
levels={1:[(0,)]}; counts=[1]; totals=[1]
for n in range(1,N+1):
 if n>1:
  levels[n]=[w+(t,) for w in levels[n-1] for t in range(asc(w)+2)]
 good=[w for w in levels[n] if valid(w)]
 counts.append(len(good)); totals.append(len(levels[n]))
 levels[n]=levels[n] # Keep unpruned level for next iteration.
 if n==1: goodlevels={}
 goodlevels[n]=good
assert counts==EXPECTED,counts
# Independently count states by updating endpoints of all increasing pairs.
# No quadruple reduction is used in this recurrence.
state_counts={(0,0,frozenset({0}),frozenset(),frozenset()):1}
rec_counts=[1,1]
for n in range(1,N):
 nxt=defaultdict(int)
 for (a,last,seen,pairs,banned),mult in state_counts.items():
  for t in range(a+2):
   if t in banned: continue
   b=set(banned)
   for u,v in pairs:
    if v<t: b.update((u,v))
   ps=pairs | frozenset((u,t) for u in seen if u<t)
   key=(a+(last<t),t,seen|{t},ps,frozenset(b))
   nxt[key]+=mult
 state_counts=nxt
 rec_counts.append(sum(nxt.values()))
assert rec_counts==counts
collision=None
for n,words in goodlevels.items():
 groups={}
 for w in words:
  assert forbidden(w)==simplified_forbidden(w),(w,forbidden(w),simplified_forbidden(w))
  key=compact_state(w); ch=children(w)
  if key in groups and groups[key][1]!=ch and collision is None:
   v,cv=groups[key]
   collision={'length':n,'state_fields':['asc','last','max','distinct_count','banned_count'],'state':key,'prefix_1':v,'prefix_2':w,'children_1':cv,'children_2':ch,'banned_1':sorted(forbidden(v)),'banned_2':sorted(forbidden(w))}
  else: groups[key]=(w,ch)
non_rgf=next(w for words in goodlevels.values() for w in words if any(w[i]>max(w[:i])+1 for i in range(1,len(w))))
contains0132=next(w for words in goodlevels.values() for w in words if any(red(q)==(0,1,3,2) for q in combinations(w,4)))
out={'job_id':'primary-20260913-ascent-0120-0121-triage-ccd00a55e176','max_length':N,'counts_n0_to_n9':counts,'all_ascent_totals_n0_to_n9':totals,'independent_state_counts':rec_counts,'full_reduction_and_state_counts_agree':True,'simplified_forbidden_matches_all_avoiders_through_n9':True,'compact_state_collision':collision,'smallest_non_RGF':non_rgf,'smallest_0132_containing_avoider':contains0132,'source_sha256':hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),'limitation':'Finite exact observations; no all-length enumeration or novelty claim.'}
Path('evidence/triage-test-results.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
