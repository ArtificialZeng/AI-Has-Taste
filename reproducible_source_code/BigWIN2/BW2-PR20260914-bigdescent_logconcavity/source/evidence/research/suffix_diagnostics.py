"""Exact witnesses and recurrence checks for the attempted suffix induction."""
from pathlib import Path
import json, hashlib

def at(p,k):return p[k] if 0<=k<len(p) else 0
def add(*ps):return [sum(at(p,k) for p in ps) for k in range(max(map(len,ps)))]
def t(p):return [0]+p
def T(s):
 a,b,c=s
 return add(a,t(b),t(c)),a,add(t(b),c)
def L(p,k):return at(p,k)**2-at(p,k-1)*at(p,k+1)
def M(p,q,k):return 2*at(p,k)*at(q,k)-at(p,k-1)*at(q,k+1)-at(p,k+1)*at(q,k-1)
def invariants(s,k):
 a,b,c=s
 return dict(LA=L(a,k),LB=L(b,k),LC=L(c,k),U=M(a,b,k),V=M(a,c,k),W=M(b,c,k),H=M(a,t(b),k),I=M(a,t(c),k),J=M(c,t(b),k))
state=([1],[0],[1]);first_bad=None;strong=None;rr_checks=0
for n in range(1,301):
 a,b,c=state;new=T(state)
 for k in range(n+2):
  x=invariants(state,k);xm=invariants(state,k-1);y=invariants(new,k)
  predicted=dict(
   LA=x['LA']+xm['LB']+xm['LC']+x['H']+x['I']+xm['W'],
   LB=x['LA'],LC=xm['LB']+x['LC']+x['J'],
   U=2*x['LA']+x['H']+x['I'],
   V=x['H']+x['V']+2*xm['LB']+x['J']+xm['W']+M(c,t(c),k),
   W=x['H']+x['V'],H=M(a,t(a),k)+xm['U']+xm['V'],
   I=M(a,t(t(b)),k)+x['I']+M(b,t(b),k-1)+xm['W']+xm['J']+2*xm['LC'],
   J=xm['U']+M(c,t(a),k))
  assert y==predicted,(n,k,y,predicted)
  rr_checks+=9
  for name,v in x.items():
   if v<0 and first_bad is None:first_bad=dict(n=n,k=k,name=name,value=v)
  v=at(c,k)*at(b,k-1)-at(c,k-1)*at(b,k)
  if v<0 and strong is None:strong=dict(n=n,k=k,value=v,B=b,C=c,mixed=M(c,t(b),k))
 state=new
scaled=([1,5],[1],[1]);first=T(scaled);second=T(first)
assert second[2]==[1,2,5] and L(second[2],1)==-1
assert invariants(scaled,1)['J']==0 and invariants(first,1)['J']==-3
out=dict(job_id='primary-20260914-bigdescent-logconcavity-research-ff87ce2dd87c',arithmetic='exact Python integers',actual_states_n_max=300,nine_invariants_first_failure=first_bad,determinant_recurrence_scalar_checks=rr_checks,strong_C_tB_first_failure=strong,scale_obstruction=dict(scale=5,input=scaled,after_one=first,after_two=second,C_L1=L(second[2],1),J_after_one=M(first[2],t(first[1]),1)),qualification='The scale witness is outside the actual orbit and refutes only the stated invariant-cone method. Actual-state tests are finite.',script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
