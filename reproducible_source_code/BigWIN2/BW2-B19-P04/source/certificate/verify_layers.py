#!/usr/bin/env python3
"""Independent verifier for the S(3,7) orbit-layer certificate."""
import argparse, hashlib, itertools, json, platform, sys
from pathlib import Path
import numba as nb
import numpy as np

FACETS=list(itertools.combinations(range(7),4))
VM=np.array([sum(1<<v for v in f) for f in FACETS],dtype=np.uint64)
INDEX={int(x):i for i,x in enumerate(VM)}
PERMS=np.empty((5040,35),dtype=np.uint8)
for q,p in enumerate(itertools.permutations(range(7))):
    for i,f in enumerate(FACETS): PERMS[q,i]=INDEX[sum(1<<p[v] for v in f)]

@nb.njit(cache=True)
def legal_by_maximal_intersections(state,j,vm):
    ints=np.zeros(35,np.uint64); count=0; f=vm[j]
    for i in range(35):
        if (state>>np.uint64(i))&np.uint64(1):
            h=f&vm[i]; seen=False
            for a in range(count): seen |= ints[a]==h
            if not seen: ints[count]=h; count+=1
    if count==0:return False
    for a in range(count):
        maximal=True
        for b in range(count):
            if a!=b and ints[a]!=ints[b] and (ints[a]&~ints[b])==0:
                maximal=False; break
        if maximal:
            x=ints[a]; pop=0
            while x: x&=x-np.uint64(1); pop+=1
            if pop!=3:return False
    return True

@nb.njit(cache=True)
def canonical(state,perms):
    best=np.uint64(0xffffffffffffffff)
    for q in range(perms.shape[0]):
        image=np.uint64(0)
        for i in range(35):
            if (state>>np.uint64(i))&np.uint64(1): image|=np.uint64(1)<<np.uint64(perms[q,i])
        if image<best:best=image
    return best

@nb.njit(cache=True)
def successors(layer,vm,perms):
    raw=np.empty(layer.size*35,np.uint64); used=0; dead=0
    for a in range(layer.size):
        state=layer[a]; moved=False
        for j in range(35):
            if not ((state>>np.uint64(j))&np.uint64(1)) and legal_by_maximal_intersections(state,j,vm):
                moved=True; raw[used]=canonical(state|(np.uint64(1)<<np.uint64(j)),perms); used+=1
        if not moved:dead+=1
    return raw[:used],dead

def small_crosscheck():
    # Exhaust all states for n=5 (five tetrahedral facets), using literal sets.
    n=5; facets=[frozenset(x) for x in itertools.combinations(range(n),4)]
    for state in range(1,1<<len(facets)):
        for j,f in enumerate(facets):
            if state>>j&1:continue
            ints={f&facets[i] for i in range(len(facets)) if state>>i&1}
            direct=bool(ints) and all(len(h)==3 for h in ints if not any(h<k for k in ints))
            ridges=[h for h in ints if len(h)==3]
            cover=bool(ridges) and all(any(h<=r for r in ridges) for h in ints)
            if direct!=cover:raise AssertionError(('small crosscheck',state,j))

def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('certificate_dir',type=Path); ap.add_argument('--output',type=Path); args=ap.parse_args()
    manifest=json.loads((args.certificate_dir/'layers_manifest.json').read_text())
    layers=[]
    for rec in manifest['files']:
        p=args.certificate_dir/rec['file']
        if p.stat().st_size!=rec['bytes'] or digest(p)!=rec['sha256']:raise SystemExit('manifest hash/size failure: '+p.name)
        x=np.fromfile(p,dtype='<u8')
        if x.size==0 or np.any(x[1:]<=x[:-1]):raise SystemExit('layer not strictly sorted unique: '+p.name)
        layers.append(x)
    if len(layers)!=35 or not np.array_equal(layers[0],np.array([1],dtype=np.uint64)):raise SystemExit('endpoint layer failure')
    small_crosscheck(); rows=[]
    for d in range(34):
        raw,dead=successors(layers[d],VM,PERMS); got=np.unique(raw)
        if dead:raise SystemExit(f'dead states at depth {d+1}: {dead}')
        if not np.array_equal(got,layers[d+1]):raise SystemExit(f'coverage mismatch from depth {d+1}')
        rows.append({'depth':d+1,'states':int(layers[d].size),'raw_successors':int(raw.size),'dead':int(dead)})
        print(json.dumps(rows[-1]),flush=True)
    full=(np.uint64(1)<<np.uint64(35))-np.uint64(1)
    if layers[-1].size!=1 or layers[-1][0]!=full:raise SystemExit('final state is not the full skeleton')
    result={'status':'PASS','theorem_endpoint':'Every partial shelling of S_{3,7} extends to a full shelling.','small_crosscheck':'all nonempty states for n=5','rows':rows,'manifest_sha256':digest(args.certificate_dir/'layers_manifest.json'),'verifier_sha256':digest(Path(__file__)),'python':sys.version,'numba':nb.__version__,'platform':platform.platform()}
    payload=json.dumps(result,indent=2)+'\n'
    if args.output:args.output.write_text(payload,encoding='utf-8')
    print(payload)

if __name__=='__main__':main()
