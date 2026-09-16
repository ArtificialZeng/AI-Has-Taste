"""Recompute a triage witness independently of the Cartesian-product search.

Uses a remaining-content recursion; never imports the search or its root test.
This is deterministic cross-checking, not a fresh mathematical referee.
"""
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
import sympy as sp

LAM = (3, 3, 3, 3, 4, 4)
ALPHA = (2, 2, 1, 1)
JOB = 'primary-20260913-multiset-rook-triage-cd5e7d22bd0b'

def visit(prefix, remaining):
    if not any(remaining):
        yield prefix
        return
    for j, count in enumerate(remaining, 1):
        if count and j <= LAM[len(prefix)]:
            rest = list(remaining)
            rest[j-1] -= 1
            yield from visit(prefix + (j,), tuple(rest))

def run():
    words = list(visit((), ALPHA))
    assert len(words) == len(set(words))
    counts = defaultdict(Counter)
    lines = ['word\tfirst_letter\tascents']
    for w in words:
        assert tuple(w.count(i) for i in range(1, 5)) == ALPHA
        assert all(j <= h for j, h in zip(w, LAM))
        d = sum(w[i] < w[i+1] for i in range(5))
        counts[w[0]][d] += 1
        lines.append(''.join(map(str, w)) + '\t' + str(w[0]) + '\t' + str(d))
    t = sp.Symbol('t')
    refinements = {j: sp.Poly(sum(c*t**d for d,c in counts[j].items()), t)
                   for j in range(1, 4)}
    assert refinements[3].as_expr() == t**3 + 8*t**2 + 3*t
    assert refinements[1].as_expr() == 2*t**4 + 15*t**3 + 7*t**2
    assert sp.expand(t**2*(t+7)*(2*t+1)) == refinements[1].as_expr()
    assert sp.expand(t*((t+4)**2-13)) == refinements[3].as_expr()
    # Root inequality is certified by 13 > 3^2, so -4-sqrt(13) < -7.
    assert 13 > 3**2
    total = sum(p.as_expr() for p in refinements.values())
    ptotal = sp.Poly(total, t)
    out = Path(__file__).parent
    (out/'six-letter-words.tsv').write_text('\n'.join(lines)+'\n')
    result = dict(job_id=JOB, lam=LAM, alpha=ALPHA,
        enumeration='Depth-first remaining-content recursion, bounded by each row flag; no search-script import.',
        legal_words=len(words), refined_counts={j:dict(sorted(counts[j].items())) for j in range(1,4)},
        refinements={j:str(p.as_expr()) for j,p in refinements.items()},
        factorizations={j:str(sp.factor(p.as_expr())) for j,p in refinements.items()},
        total=str(total), total_real_root_multiplicity=sum(m for _,m in ptotal.intervals()),
        total_degree=ptotal.degree(),
        exact_violation='deg(R1)=deg(R3)+1, but minroot(R3)=-4-sqrt(13)<-7=minroot(R1); hence R3 does not precede R1 in Definition 8.',
        source_sha256=hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
        word_list_sha256=hashlib.sha256((out/'six-letter-words.tsv').read_bytes()).hexdigest(),
        limitation='Triage cross-check only; total polynomial here is real-rooted; no independent referee or priority claim.')
    (out/'six-letter-verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__ == '__main__':
    run()
