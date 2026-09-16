#!/usr/bin/env python3
"""Independent verifier: no FLINT/SymPy; checks sparse integer kernel equations."""
import argparse, hashlib, json
import networkx as nx

def adj_masks(g):
 a=[0]*len(g)
 for u,v in g.edges(): a[u]|=1<<v; a[v]|=1<<u
 return a
def indep(m,a):
 for i in range(len(a)):
  if (m>>i)&1 and a[i]&m: return False
 return True
def layers(g):
 n=len(g); a=adj_masks(g); L=[[] for _ in range(n+1)]
 for x in range(1<<n):
  if not indep(x,a): continue
  y=((1<<n)-1)^x
  while True:
   m=x|(y<<n); L[m.bit_count()].append(m)
   if not y: break
   y=(y-1)&(((1<<n)-1)^x)
 return L
def alpha(g):
 a=adj_masks(g); return max(m.bit_count() for m in range(1<<len(g)) if indep(m,a))
def verify(r):
 g=nx.from_graph6_bytes(r["graph6"].encode()); assert len(g)==8 and alpha(g)==3
 L=layers(g); h=list(map(len,L)); assert h==r["hilbert"]
 d=r["degree"]; assert (d,r["side"]) in ((4,"right"),(5,"left"))
 v=[0]*r["vector_length"]
 for i,x in r["vector_sparse"]: assert 0<=i<len(v) and v[i]==0 and x; v[i]=x
 assert any(v)
 if r["side"]=="right":
  assert h[d]<=h[d+1] and len(v)==h[d]; up={m:i for i,m in enumerate(L[d+1])}; sums=[0]*h[d+1]
  for j,m in enumerate(L[d]):
   if not v[j]: continue
   for b in range(16):
    i=up.get(m|(1<<b)) if not ((m>>b)&1) else None
    if i is not None: sums[i]+=v[j]
 else:
  assert h[d]>=h[d+1] and len(v)==h[d+1]; up={m:i for i,m in enumerate(L[d+1])}; sums=[]
  for m in L[d]: sums.append(sum(v[up[m|(1<<b)]] for b in range(16) if not ((m>>b)&1) and (m|(1<<b)) in up))
 assert all(x==0 for x in sums)
def main():
 p=argparse.ArgumentParser(); p.add_argument("certificate"); a=p.parse_args(); num=0
 with open(a.certificate) as f:
  for line in f: verify(json.loads(line)); num+=1
 print(json.dumps({"verified":num,"input_sha256":hashlib.sha256(open(a.certificate,"rb").read()).hexdigest(),"status":"OK"},sort_keys=True))
if __name__=="__main__": main()
