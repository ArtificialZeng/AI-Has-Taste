"""Independent exact inverse enumeration using the proved first-step length bound.

For fixed k, select all possible shortened outputs q by exhaustive enumeration
on k-1 letters and test q followed by a fresh marker. Then enumerate all exact
preimages by the first-letter recursion. This does not assume the disputed
marker-deletion bridge, and is not offered as an all-k structural solution.
"""
import sys
sys.dont_write_bytecode = True
import argparse
import json
from collections import Counter
from functools import lru_cache
from importlib.util import spec_from_file_location, module_from_spec
from itertools import combinations_with_replacement, product
from pathlib import Path
from time import monotonic
from hashlib import sha256

HERE = Path(__file__).resolve().parent
sp = spec_from_file_location('marker',HERE/'terminal-marker.py')
t = module_from_spec(sp)
sp.loader.exec_module(t)
b = t.b


def cuts(word, pieces):
    for positions in combinations_with_replacement(range(len(word)+1),pieces-1):
        bounds = (0,)+positions+(len(word),)
        yield tuple(word[bounds[i]:bounds[i+1]] for i in range(pieces))


@lru_cache(None)
def inverse(v):
    if not v:
        return ((),)
    # A run-free output can only come from a word with no repeated letters.
    if b.trunc(v) == v:
        return (v[::-1],) if len(set(v)) == len(v) else ()
    a = v[-1]
    m = 1
    while m<len(v) and v[-m-1] == a:
        m += 1
    prefix = v[:-m]
    if a in prefix:
        return ()
    found = []
    for segments in cuts(prefix,m):
        choices = tuple(inverse(s) for s in segments)
        if all(choices):
            for preimages in product(*choices):
                w = tuple(y for s in preimages for y in ((a,)+s))
                found.append(w)
    assert len(set(found)) == len(found)
    return tuple(found)


def expansions(q, extra):
    for positions in combinations_with_replacement(range(len(q)),extra):
        counts = Counter(positions)
        yield tuple(x for i,x in enumerate(q) for _ in range(1+counts[i]))


def census(k):
    start = monotonic()
    r = k-1
    qs = []
    qtotals = {}
    for n in (2*r,2*r+1):
        count = 0
        for q in t.words(n,r):
            count += 1
            z = q+(r,)
            for _ in range(r-1):
                z = b.phi(z)
            if not b.sorted_word(z):
                qs.append(q)
        qtotals[n] = count
    hits, multiplicities, cores = set(), Counter(), Counter()
    generated = 0
    for q in qs:
        for m in (2,3,4):
            extra = 2*k+2-m-len(q)
            if extra<0:
                continue
            for v in expansions(q,extra):
                for w in inverse(v+(r,)*m):
                    generated += 1
                    assert b.phi(w) == b.recursive(w) == v+(r,)*m
                    w = b.canon(w)
                    assert len(w)==2*k+2 and len(set(w))==k
                    assert min(Counter(w).values())>=2
                    assert w not in hits
                    hits.add(w)
                    multiplicities[w.count(0)] += 1
                    cores[len(b.trunc(w))] += 1
    prior = HERE/f'research-census-k{k}.json'
    compared = None
    if prior.exists():
        forward = {tuple(x['w']) for x in json.loads(prior.read_text())['hits']}
        assert hits == forward
        compared = prior.name
    result = dict(job_id='newwin-00001-p05-research-0171927ebd6e', k=k,
        status='exact finite inverse census; no all-k classification',
        q_domain_totals=qtotals, q_selected=len(qs), witnesses=len(hits),
        first_multiplicities=dict(multiplicities),core_lengths=dict(cores),
        forward_witness_set_compared=compared, duplicate_preimages=generated-len(hits),
        elapsed_seconds=monotonic()-start, cache=inverse.cache_info()._asdict(),
        witnesses_rgs=sorted(hits),
        source_sha256=sha256((HERE.parent/'source.md').read_bytes()).hexdigest(),
        script_sha256=sha256(Path(__file__).read_bytes()).hexdigest())
    b.atomic_json(HERE/f'inverse-census-k{k}.json',result)
    print(json.dumps({a:b for a,b in result.items() if a!='witnesses_rgs'},indent=2),flush=True)
    inverse.cache_clear()
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('k',type=int,nargs='+')
    args=parser.parse_args()
    for k in args.k:
        census(k)
