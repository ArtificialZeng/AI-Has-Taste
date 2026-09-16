#!/usr/bin/env python3
"""Discovery-scale orbit BFS under S_7; not by itself a certificate."""
import argparse, hashlib, itertools, json, platform, sys, time
from pathlib import Path
import numba as nb
import numpy as np

FACETS=list(itertools.combinations(range(7),4))
VM=np.array([sum(1<<v for v in f) for f in FACETS],dtype=np.uint64)
INDEX={int(x):i for i,x in enumerate(VM)}
ACTIONS=np.empty((5040,35),dtype=np.uint8)
for q,p in enumerate(itertools.permutations(range(7))):
    for i,f in enumerate(FACETS): ACTIONS[q,i]=INDEX[sum(1<<p[v] for v in f)]

@nb.njit(cache=True)
def pc(x):
    n=0
    while x:
        x &= x-np.uint64(1); n+=1
    return n

@nb.njit(cache=True)
def appendable(s,j,vm):
    ridges=np.zeros(4,np.uint64); nr=0; f=vm[j]
    for i in range(35):
        if (s>>np.uint64(i))&np.uint64(1):
            h=f&vm[i]
            if pc(h)==3:
                seen=False
                for q in range(nr): seen |= ridges[q]==h
                if not seen: ridges[nr]=h; nr+=1
    if nr==0:return False
    for i in range(35):
        if (s>>np.uint64(i))&np.uint64(1):
            h=f&vm[i]; covered=False
            for q in range(nr): covered |= (h & ~ridges[q])==0
            if not covered:return False
    return True

@nb.njit(cache=True)
def canon(s,actions):
    best=np.uint64(0xffffffffffffffff)
    for q in range(actions.shape[0]):
        t=np.uint64(0)
        for i in range(35):
            if (s>>np.uint64(i))&np.uint64(1): t |= np.uint64(1)<<np.uint64(actions[q,i])
        if t<best:best=t
    return best

@nb.njit(cache=True)
def expand(layer,vm,actions):
    out=np.empty(layer.size*35,np.uint64); k=0; dead=0
    for z in range(layer.size):
        s=layer[z]; anymove=False
        for j in range(35):
            if not ((s>>np.uint64(j))&np.uint64(1)) and appendable(s,j,vm):
                anymove=True; out[k]=canon(s|(np.uint64(1)<<np.uint64(j)),actions); k+=1
        if not anymove:dead+=1
    return out[:k],dead

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--max-depth',type=int,default=12)
    ap.add_argument('--output',type=Path); ap.add_argument('--certificate-dir',type=Path); args=ap.parse_args()
    if args.certificate_dir: args.certificate_dir.mkdir(parents=True,exist_ok=True)
    layer=np.array([1],dtype=np.uint64); rows=[]
    for depth in range(1,args.max_depth+1):
        if args.certificate_dir:
            layer.tofile(args.certificate_dir/f'layer_{depth:02d}.u64le')
        start=time.time(); out,dead=expand(layer,VM,ACTIONS) if depth<35 else (np.empty(0,np.uint64),0)
        rows.append({'depth':depth,'orbits':int(layer.size),'transitions':int(out.size),'dead':int(dead),'seconds':time.time()-start})
        print(json.dumps(rows[-1]),flush=True)
        if dead or depth==args.max_depth:break
        layer=np.unique(out)
    result={'discovery_only':not bool(args.certificate_dir),'rows':rows,'python':sys.version,'platform':platform.platform(),'numba':nb.__version__}
    if args.certificate_dir:
        files=[]
        for p in sorted(args.certificate_dir.glob('layer_*.u64le')):
            files.append({'file':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
        (args.certificate_dir/'layers_manifest.json').write_text(json.dumps({'format':'sorted unique uint64 little-endian states; facet bits use lexicographic 4-subsets of vertices 0..6','files':files},indent=2)+'\n')
    if args.output:args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    if rows[-1]['dead']:raise SystemExit(2)

if __name__=='__main__':main()
