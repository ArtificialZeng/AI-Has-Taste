"""Exact row-move enumeration and clique search, independent of source formulas.

Run from the project root: python3 evidence/triage_check.py
"""
from collections import Counter
from pathlib import Path
import json


def partitions(n, largest=None):
    if n == 0:
        yield ()
        return
    for k in range(min(n, largest or n), 0, -1):
        for tail in partitions(n-k, k):
            yield (k,) + tail


def neighbors(lam):
    result = set()
    for i in range(len(lam)):
        for j in range(len(lam)+1):
            if i == j:
                continue
            rows = list(lam) + [0]
            rows[i] -= 1
            rows[j] += 1
            mu = tuple(sorted((x for x in rows if x), reverse=True))
            if mu != lam:
                result.add(mu)
    return result


def formulas(lam):
    counts = Counter(lam)
    sizes = sorted(counts, reverse=True)
    r = len(sizes)
    alpha = [int(counts[s] == 1) for s in sizes]
    beta = [int(s-t == 1) for s,t in zip(sizes, sizes[1:]+[0])]
    degree = r*(r+1)-sum(alpha)-sum(beta)
    delta = max([r+1-a-b for a,b in zip(alpha,beta)] +
                [r-a-b for a,b in zip(alpha+[0],[0]+beta)])
    return degree, delta


def clique_number(vertices, adjacency):
    best = 0
    def visit(size, candidates):
        nonlocal best
        best = max(best, size)
        while candidates:
            if size + len(candidates) <= best:
                return
            v = candidates.pop()
            visit(size+1, candidates & adjacency[v])
    visit(0, set(vertices))
    return best


def run(max_n=20):
    output = {'range': [2,max_n], 'arithmetic': 'exact integers and sets',
              'degree_formula_mismatches': [], 'dimension_formula_mismatches': [],
              'rows': []}
    for n in range(2,max_n+1):
        verts = list(partitions(n))
        adj = {v:neighbors(v) for v in verts}
        all_v = set(verts)
        assert all(adj[v] <= all_v and v not in adj[v] for v in verts)
        assert all(v in adj[w] for v in verts for w in adj[v])
        degrees = {v:len(adj[v]) for v in verts}
        dims = {v:clique_number(adj[v],adj) for v in verts}
        for v in verts:
            fd,fc = formulas(v)
            if degrees[v] != fd:
                output['degree_formula_mismatches'].append([v,degrees[v],fd])
            if dims[v] != fc:
                output['dimension_formula_mismatches'].append([v,dims[v],fc])
        edges = [(v,w) for v in verts for w in sorted(adj[v]) if v<w]
        ed = max(edges,key=lambda e:abs(degrees[e[0]]-degrees[e[1]]))
        ec = max(edges,key=lambda e:abs(dims[e[0]]-dims[e[1]]))
        output['rows'].append({'n':n,'vertices':len(verts),'edges':len(edges),
            'D_d':abs(degrees[ed[0]]-degrees[ed[1]]),
            'D_delta':abs(dims[ec[0]]-dims[ec[1]]),
            'degree_witness':ed,'dimension_witness':ec})
    Path('evidence/triage_check.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output))


if __name__ == '__main__':
    run()
