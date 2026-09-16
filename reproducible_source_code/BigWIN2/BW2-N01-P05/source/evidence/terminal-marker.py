"""Adversarial exact tests of the terminal-marker bridge, independently of preimages."""
import sys
sys.dont_write_bytecode = True
import json
from collections import Counter
from hashlib import sha256
from importlib.util import spec_from_file_location, module_from_spec
from pathlib import Path

HERE = Path(__file__).resolve().parent
sp = spec_from_file_location('census', HERE/'research-pass1.py')
b = module_from_spec(sp)
sp.loader.exec_module(b)


def words(n, k):
    counts, prefix = [0]*k, []
    def visit(used, need):
        left = n-len(prefix)
        if need > left:
            return
        if not left:
            yield tuple(prefix)
            return
        for x in range(min(k,used+1)):
            if prefix and x == prefix[-1]:
                continue
            old = counts[x]
            counts[x] += 1
            prefix.append(x)
            yield from visit(max(used,x+1),need-(old<2))
            prefix.pop()
            counts[x] -= 1
    yield from visit(0,2*k)


def run(k, n):
    total = 0
    hits, examples = [], {}
    histogram = Counter()
    for q in words(n,k):
        total += 1
        a, c = q, q+(k,)
        ta = tc = 0
        while not b.sorted_word(a):
            ta += 1
            a = b.phi(a)
        while not b.sorted_word(c):
            tc += 1
            c = b.phi(c)
        histogram[str((ta,tc))] += 1
        if tc > ta:
            examples.setdefault(str((ta,tc)),q)
        if ta <= k-1 and tc == k:
            hits.append(q)
    result = dict(k=k,n=n,enumerated=total,time_histogram=dict(histogram),
                  delayed_examples=examples,maximal_delay_count=len(hits),
                  maximal_delay_examples=[dict(q=q,q_orbit=b.orbit(q,k),
                    marker_orbit=b.orbit(q+(k,),k)) for q in hits[:10]])
    print(json.dumps({a:b for a,b in result.items() if a!='maximal_delay_examples'}),flush=True)
    return result


if __name__ == '__main__':
    cases = []
    pairs = [(2,4)] + [(k,n) for k in (3,4,5) for n in range(2*k,2*k+4)]
    pairs += [(6,12),(6,13)]
    for k,n in pairs:
        cases.append(run(k,n))
        b.atomic_json(HERE/'terminal-marker.json',dict(
            job_id='newwin-00001-p05-research-0171927ebd6e',
            status='exact finite tests; no infinite theorem',
            domain='all run-free RGS with exactly k letters, each occurring at least twice',
            tested_statement='If 2k<=|q|<=2k+1 and k>=3, phi^(k-1)(q) sorted implies phi^(k-1)(q x) sorted for a new letter x',
            complete_cases=cases,
            script_sha256=sha256(Path(__file__).read_bytes()).hexdigest()))
