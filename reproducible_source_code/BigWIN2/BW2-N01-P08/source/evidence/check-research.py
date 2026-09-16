#!/usr/bin/env python3
"""Independent, bounded, exact corroboration of research-proof.md.

Run: python3 evidence/check-research.py
No imported project verifier, floats, randomness, workers, or network access.
Only writes evidence/research-check.json (atomic replacement).
"""
from collections import Counter, defaultdict
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import platform
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
JOB = 'newwin-00001-p08-research-23519ac79811'
SOURCE_HASH = 'e6b61e96d2298cfd85d301038ae9142fc908f4efaee7c7ab1638993c5cbf7696'


def block_counts(m, n):
    """Count D=N^a1 E ... N^an E by its n north-run slots.

    Every excursion ends E, so this representation is unique. In a north
    block the height increases; hence nonnegativity need only be checked
    just after each E. Slots of sizes 0, 1, and >=2 have different weights.
    """
    states = {(0, 0, 0): 1}  # total north steps used, peaks, NNE
    for east in range(n):
        nxt = defaultdict(int)
        for (north, peaks, nne), count in states.items():
            lower = max(0, m*(east+1)-north)
            for a in range(lower, m*n-north+1):
                nxt[north+a, peaks+int(a>0), nne+int(a>1)] += count
        states = nxt
    result = defaultdict(Counter)
    for (north, peaks, nne), count in states.items():
        assert north == m*n
        result[peaks][nne] += count
    return result


def formula(m, n, k):
    out = [0]
    for j in range(1, k+1):
        c = Fraction(comb(n,k)*comb(k,j)*comb(m*n-k,j-1), n)
        assert c.denominator == 1
        out.append(c.numerator)
    return out


def words(m, n):
    def generate(word, north, east):
        if east == n:
            assert north == m*n
            yield word
        else:
            if north < m*n:
                yield from generate(word+'N', north+1, east)
            if north >= m*(east+1):
                yield from generate(word+'E', north, east+1)
    yield from generate('',0,0)


def stats(word):
    return (sum(word[i:i+2]=='NE' for i in range(len(word)-1)),
            sum(word[i:i+3]=='NNE' for i in range(len(word)-2)))


def audit_word(word, m):
    heights = [0]
    for c in word:
        heights.append(heights[-1]+(1 if c=='N' else -m))
    assert min(heights) == heights[-1] == 0
    first_return = next(i for i in range(1,len(heights)) if heights[i]==0)
    root = first_return-1
    marked = [max(i for i in range(root) if heights[i]==h and word[i]=='N')
              for h in range(m)]
    assert marked == sorted(marked)
    ends = marked[1:]+[root]
    pieces = [word[a+1:b] for a,b in zip(marked,ends)]+[word[root+1:]]
    for piece in pieces:
        h = 0
        for c in piece:
            h += 1 if c=='N' else -m
            assert h>=0
        assert h == 0
        assert not piece or (piece.startswith('N'*m) and piece.endswith('E'))
    assert ''.join('N'+p for p in pieces[:m])+'E'+pieces[-1] == word
    extra = (int(not pieces[m-1]),int(not pieces[m-1] and not pieces[m-2]))
    internal = [stats(p) for p in pieces]
    assert stats(word) == tuple(sum(s[i] for s in internal)+extra[i] for i in (0,1))
    return str(extra)


def signs(values):
    s = [1 if v>0 else -1 for v in values if v!=0]
    return sum(a!=b for a,b in zip(s,s[1:]))


def sturm_negative_roots(poly):
    # All arithmetic is rational. The endpoints cannot be roots of poly.
    seq = [sp.Poly(q,poly.gen,domain=sp.QQ) for q in sp.sturm(poly.as_expr(),poly.gen)]
    left = [(-1)**p.degree()*p.LC() for p in seq]
    right = [p.eval(0) for p in seq]
    vl, vr = signs(left), signs(right)
    return vl-vr, vl, vr


def main():
    assert sha256((ROOT/'source.md').read_bytes()).hexdigest() == SOURCE_HASH
    x,t = sp.symbols('x t')
    # These pairs were not in the inherited m=2..4,n<=8 coefficient table.
    pairs = [(2,9),(2,14),(3,10),(4,10),(5,8),(7,7),(17,5),(100,3)]
    rows = []
    for m,n in pairs:
        counts = block_counts(m,n)
        assert sum(map(lambda c:sum(c.values()),counts.values())) == comb((m+1)*n,n)//(m*n+1)
        for k in range(1,n+1):
            coeff = [counts[k][j] for j in range(k+1)]
            assert coeff == formula(m,n,k), (m,n,k,'block enumeration')
            assert sum(coeff) == Fraction(comb(n,k)*comb(m*n,k-1),n)
            p = sp.Poly(sum(coeff[j+1]*t**j for j in range(k)),t,domain=sp.ZZ)
            assert p.degree()==k-1 and p.eval(0)>0
            assert sp.gcd(p,p.diff()).degree()==0
            nr, vl, vr = sturm_negative_roots(p)
            assert nr == k-1, (m,n,k,'negative roots')
            d, A, b = k-1, m*n-k, m*n-2*k+1
            # SymPy's Jacobi implementation and the Rodrigues derivative are
            # checked against each other, independently of the path counts.
            jac = sp.Poly(sp.jacobi(d,1,b,x),x,domain=sp.QQ)
            rod_numerator = sp.Poly((-1)**d*sp.diff((1-x)**(d+1)*(1+x)**(d+b),x,d),x)
            rod_denominator = sp.Poly(2**d*sp.factorial(d)*(1-x)*(1+x)**b,x)
            rod, remainder = sp.div(rod_numerator,rod_denominator)
            assert remainder.is_zero and rod.set_domain(sp.QQ) == jac
            # Clear denominators monomial by monomial, without numerical substitution.
            transformed = sp.Poly(sum(c*(1+t)**i*(1-t)**(d-i)
                for (i,),c in jac.terms()),t,domain=sp.QQ)
            expected = sp.Poly(sum(comb(k,l+1)*comb(A,l)*t**l for l in range(k)),t,domain=sp.QQ)
            assert transformed == expected
            assert p.set_domain(sp.QQ) == transformed.mul_ground(sp.Rational(comb(n,k),n))
            ordinary_scalar = Fraction(comb(n-1,k-1),comb(m*n+1,k-1))
            ordinary = [0]+[Fraction(comb(m*n+1,k-1)*comb(k,j)*comb(A,j-1),k)
                           for j in range(1,k+1)]
            assert [ordinary_scalar*c for c in ordinary] == coeff
            rows.append(dict(m=m,n=n,k=k,coefficients_ascending=coeff,
                negative_roots_of_W_over_t=nr,sturm_variations=[vl,vr],
                squarefree_W_over_t=True,jacobi_beta=b,
                jacobi_rodrigues_and_transformation_match=True,
                ordinary_scalar=str(ordinary_scalar)))

    decomposition_pairs = [(2,5),(2,6),(3,5),(5,4)]
    cases=Counter();word_counts=[]
    for m,n in decomposition_pairs:
        total=0;direct=defaultdict(Counter)
        for word in words(m,n):
            total+=1
            cases[audit_word(word,m)]+=1
            k,j=stats(word);direct[k][j]+=1
        assert total==comb((m+1)*n,n)//(m*n+1)
        for k in range(1,n+1):
            assert [direct[k][j] for j in range(k+1)]==formula(m,n,k)
        word_counts.append(dict(m=m,n=n,words=total))

    result=dict(job_id=JOB,python=platform.python_version(),sympy=sp.__version__,
        source_sha256=SOURCE_HASH,domain='exact integers and rationals',
        randomness='none',independent_algorithm='north-run slots before each east step',
        coefficient_pairs=pairs,tested_polynomials=len(rows),
        checks=['block enumeration vs closed formula','Fuss total and peak totals',
                'exact negative-root Sturm count','squarefreeness',
                'Jacobi vs Rodrigues','polynomial Mobius transform','ordinary positive scalar'],
        decomposition_word_counts=word_counts,decomposition_words=sum(w['words'] for w in word_counts),
        boundary_cases=dict(cases),failures=[],rows=rows,
        conclusion='Finite corroboration, not the all-parameter proof or independent referee acceptance.')
    target=ROOT/'evidence/research-check.json'
    tmp=target.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(result,indent=2)+'\n')
    tmp.replace(target)
    print(json.dumps({k:result[k] for k in ['tested_polynomials','decomposition_words','boundary_cases','failures']}))


if __name__=='__main__':
    main()
