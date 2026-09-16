#!/usr/bin/env python3
"""Check every census graph using independent exact C canonicalization.

Canonizer explores every individualized vertex, so its output is invariant
under isomorphism. Distinct outputs prove nonisomorphism. Deterministic
relabeling tests compare the complete 45,982-row census a second time.
"""
import hashlib
import json
import random
import subprocess
import time
from math import factorial
from pathlib import Path
import networkx as nx
from labeled_cubic_count import cubic_counts, realizations

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = {4:1,6:2,8:5,10:19,12:85,14:509,16:4060,18:41301}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def canon(raw):
    run = subprocess.run([str(ROOT/'tools/canonical_small')],input=raw,capture_output=True,check=True)
    rows=[line.split('\t') for line in run.stdout.decode('ascii').splitlines()]
    return [row[0] for row in rows],rows

def main():
    started=time.monotonic();reports=[];rng=random.Random(6802)
    all_labeled,connected_labeled=cubic_counts(18)
    for n,count in EXPECTED.items():
        raw=(ROOT/f'census/n{n:02}.g6').read_bytes()
        canonical,stats=canon(raw)
        assert len(canonical)==len(set(canonical))==count
        aut=[int(row[3]) for row in stats]
        assert all(a>0 and factorial(n)%a==0 for a in aut)
        labeled_sum=sum(factorial(n)//a for a in aut)
        assert labeled_sum==connected_labeled[n],(n,labeled_sum,connected_labeled[n])
        relabeled=[]
        for code in raw.splitlines():
            g=nx.from_graph6_bytes(code)
            assert len(g)==n and nx.is_connected(g) and all(d==3 for _,d in g.degree())
            p=list(range(n));rng.shuffle(p)
            h=nx.Graph();h.add_nodes_from(range(n));h.add_edges_from((p[u],p[v]) for u,v in g.edges())
            relabeled.append(nx.to_graph6_bytes(h,header=False))
        repeat,repeat_stats=canon(b''.join(relabeled))
        assert repeat==canonical
        assert [int(row[3]) for row in repeat_stats]==aut
        output=ROOT/f'evidence/canonical_n{n:02}.tsv'
        output.write_text(''.join('\t'.join(row)+'\n' for row in stats))
        reports.append(dict(n=n,count=count,unique_isomorphism_classes=len(set(canonical)),
            census_sha256=digest(raw),canonical_table=str(output.relative_to(ROOT)),
            canonical_table_sha256=digest(output.read_bytes()),
            orbit_weighted_labeled_count=labeled_sum,independent_connected_labeled_count=connected_labeled[n],
            independent_all_labeled_count=all_labeled[n],
            relabelings_checked=count,max_search_nodes=max(int(row[1]) for row in stats),
            max_leaves=max(int(row[2]) for row in stats)))
        print(json.dumps(reports[-1]),flush=True)
    # Independent small-universe check against NetworkX atlas and VF2.
    atlas=[g for g in nx.graph_atlas_g() if 1<=len(g)<=6]
    atlas_codes=[nx.to_graph6_bytes(g,header=False) for g in atlas]
    ac,_=canon(b''.join(atlas_codes))
    assert len(ac)==len(set(ac))==len(atlas)
    # Independently count automorphisms with VF2 on all atlas graphs <=6.
    _,astats=canon(b''.join(atlas_codes))
    for g,st in zip(atlas,astats):
        assert sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(g,g).isomorphisms_iter())==int(st[3])
    # Atlas orbit weights independently check the degree-sequence recurrence.
    for n in (4,6):
        total=sum(factorial(n)//int(st[3]) for g,st in zip(atlas,astats)
            if len(g)==n and all(d==3 for _,d in g.degree()))
        assert total==all_labeled[n]
    result=dict(status='pass',job_id='win-00068-p02-research-3d462c8286f0',
        script='evidence/scripts/independent_census.py',
        canonizer='evidence/scripts/canonical_small.c',
        canonizer_source_sha256=digest((ROOT/'evidence/scripts/canonical_small.c').read_bytes()),
        canonizer_binary_sha256=digest((ROOT/'tools/canonical_small').read_bytes()),
        networkx_version=nx.__version__,seed=6802,orders=reports,
        total=sum(x['count'] for x in reports),atlas_nonisomorphic_graphs_checked=len(atlas),
        seconds=time.monotonic()-started,
        degree_recurrence_states=realizations.cache_info().currsize,
        completeness_basis='For each order the pairwise nonisomorphic cubic census has sum(n!/|Aut(G)|) equal to an independently computed exact count of labeled connected simple cubic graphs; therefore no class is omitted. Published counts and geng provenance are additional cross-checks.')
    (ROOT/'evidence/independent_census.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__': main()
