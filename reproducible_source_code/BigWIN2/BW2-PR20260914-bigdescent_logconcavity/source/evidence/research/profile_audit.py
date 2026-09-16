"""Different implementation: explicit word pairs versus matrix profiles."""
from itertools import product
from collections import Counter, defaultdict
from pathlib import Path
from math import comb
import json, hashlib, time
START=time.perf_counter()
P=((1,0,0),(1,0,0),(0,0,1))
Q=((0,1,1),(0,0,0),(0,1,0))

def tensor_edges(e):
 out=[]
 for a,b,c,d in product(range(3),repeat=4):
  if e==0:
   v=P[c][a]*P[d][b]
   if v:out.append((3*a+b,3*c+d,0,v))
  elif e==2:
   v=Q[c][a]*Q[d][b]
   if v:out.append((3*a+b,3*c+d,1,v))
  else:
   for shift,v in ((1,Q[c][a]*P[d][b]),(0,P[c][a]*Q[d][b])):
    if v:out.append((3*a+b,3*c+d,shift,v))
 return out
ED=[tensor_edges(e) for e in range(3)]
def tensor(profile):
 rows=[{} for _ in range(9)]
 for i in (0,2,6,8):rows[i][0]=1
 for e in profile:
  rr=[{} for _ in range(9)]
  for old,new,shift,m in ED[e]:
   for d,v in rows[old].items():rr[new][d+shift]=rr[new].get(d+shift,0)+m*v
  rows=rr
 out=Counter()
 for i in (4,5,7,8):out.update(rows[i])
 return +out

def encode(e):return sum(v*3**j for j,v in enumerate(e))
def decode(code,length):
 out=[]
 for j in range(length):out.append(code%3);code//=3
 return tuple(out)
def compress(e):
 out=[]
 for a in e:
  if a or not out or out[-1]:out.append(a)
 return tuple(out)
def shape_failure(h,total):
 for j in range(total+1):
  assert h[j]==h[total-j],('asymmetry',total,j,h)
 for j in range(1,total//2+1):
  if h[j]<h[j-1]:return {"j":j,"h_j":h[j],"h_previous":h[j-1]}
 return None

# A direct scan of every binary word; no suffix recurrence is used here.
direct={};word_counts=[]
for n in range(1,10):
 words=Counter()
 for prefix in product((0,1),repeat=n-1):
  w=prefix+(1,);e=[]
  for i in range(1,n):
   e.append(int(w[i-1:i+1]==(1,0) or i>=2 and w[i-2:i+1]==(0,1,1)))
  words[encode(e),sum(e)]+=1
 h=defaultdict(Counter)
 for (m,k),a in words.items():
  for (mm,kk),b in words.items():h[m+mm][k]+=a*b
 direct[n]=h;word_counts.append(2**(n-1))
profiles_checked=0;scalar_coefficients=0
for n in range(1,10):
 for code in range(3**(n-1)):
  e=decode(code,n-1);expected=direct[n].get(code,Counter());got=tensor(e)
  assert got==expected,(n,e,got,expected)
  ee=compress(e)
  assert expected==direct[len(ee)+1].get(encode(ee),Counter()),('compression',e)
  assert shape_failure(got,sum(e)) is None,(e,got)
  profiles_checked+=1;scalar_coefficients+=sum(e)+1

# Held-out attack: all periodic motifs of length <=4, repeated 8,16,32
# times, with either choice at each boundary. Test beyond degree 14.
held=set()
for length in range(1,5):
 for motif in product((0,1,2),repeat=length):
  for repeat in (8,16,32):
   for lead,tail in product((False,True),repeat=2):
    e=compress(((0,) if lead else ())+motif*repeat+((0,) if tail else ()))
    if sum(e)>=16:held.add(e)
first_bad=None;zero=0;nonzero=0;max_degree=0;max_length=0
for e in sorted(held,key=lambda e:(len(e),e)):
 h=tensor(e);bad=shape_failure(h,sum(e))
 if bad and first_bad is None:first_bad={"profile":e,**bad}
 zero+=not bool(h);nonzero+=bool(h)
 max_degree=max(max_degree,sum(e));max_length=max(max_length,len(e))

reported=json.loads(Path('evidence/research/profile_test.json').read_text())
expected_counts=[0]+[sum(comb(l,2*k-l)*2**(l+1) for l in range(k,2*k+1)) for k in range(1,reported['degree_k_max']+1)]
assert reported['profile_counts_by_k']==expected_counts
assert reported['first_negative_coefficient'] is None
out={"job_id":"primary-20260914-bigdescent-logconcavity-research-ff87ce2dd87c",
 "arithmetic":"exact Python integers","fresh_model_audit":False,
 "direct_word_enumeration_n_max":9,"direct_words":sum(word_counts),
 "all_ternary_profiles_compared":profiles_checked,"scalar_coefficients_compared":scalar_coefficients,
 "tensor_agrees_with_direct_word_pairs":True,"compression_agrees_with_direct_word_pairs":True,
 "independent_profile_count_formula_matches":True,
 "periodic_attack":"All motifs in {0,1,2} of length 1..4, repeated 8,16,32 times; independently optional leading/trailing zero; compress zeros; retain total degree >=16; deduplicate.",
 "periodic_profiles":len(held),"periodic_zero_profiles":zero,"periodic_nonzero_profiles":nonzero,
 "periodic_max_total_degree":max_degree,"periodic_max_compressed_length":max_length,
 "periodic_first_Schur_failure":first_bad,
 "qualification":"Same worker, independent deterministic implementation. The periodic suite is not exhaustive outside its specified family and proves no all-degree claim.",
 "seconds":time.perf_counter()-START,
 "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
