"""Exact certificate for the sharp conditional two-event odds bound.

The mathematical reduction to five matrix families is in
two-singleton-theorem.md. This program certifies their finite polynomial
inequalities, then recomputes them with a separate symbolic implementation.
"""
from itertools import product, combinations_with_replacement as cwr
from pathlib import Path
import hashlib
import json
import time

JOB = "primary-20260914-bigdescent-logconcavity-research-6ff0786c2423"
P = ((1,0,0),(1,0,0),(0,0,1))
Q = ((0,1,1),(0,0,0),(0,1,0))
I = ((1,0,0),(0,1,0),(0,0,1))
OUT = ((1,0,0),(0,1,0),(1,0,1),(0,1,1))
IN = ((1,0,0),(1,1,0),(1,0,1),(1,1,1))

def mul(a,b):
    return tuple(tuple(sum(a[i][k]*b[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))

def scalar(l,m,r):
    return sum(l[i]*m[i][j]*r[j] for i in range(3) for j in range(3))

def add(a,b):
    return tuple(tuple(a[i][j]+b[i][j] for j in range(3)) for i in range(3))

def main():
    start = time.perf_counter()
    PQ, QP = mul(P,Q), mul(Q,P)
    PQP, QPQ = mul(PQ,P), mul(QP,Q)
    assert mul(P,P) == P
    assert mul(mul(Q,Q),Q) == ((0,0,0),)*3
    assert mul(PQP,QP) == add(PQP,P)
    assert mul(QPQ,PQ) == add(QPQ,Q)
    assert mul(mul(PQ,PQ),PQ) == add(mul(PQ,PQ),PQ)
    assert mul(mul(QP,QP),QP) == add(mul(QP,QP),QP)
    families = {"I":(I,), "P":(P,PQP), "Q":(Q,QPQ),
                "PQ":(PQ,mul(PQ,PQ)), "QP":(QP,mul(QP,QP))}
    reports = {}
    # Each listed tuple gives the expansion of the image in the ray basis.
    out_images = (
        ((1,0,0,0),(1,0,0,0),(0,0,1,0),(0,0,1,0)),
        ((0,0,0,1),(0,0,0,0),(0,1,0,1),(0,1,0,0)))
    in_images = (
        ((0,1,0,0),(0,1,0,0),(0,0,0,1),(0,0,0,1)),
        ((0,0,0,0),(0,0,1,0),(1,0,0,0),(1,0,1,0)))
    for t,T in enumerate((P,Q)):
        for i in range(4):
            assert tuple(sum(OUT[i][k]*T[k][j] for k in range(3))
                         for j in range(3)) == tuple(
                sum(out_images[t][i][k]*OUT[k][j] for k in range(4))
                for j in range(3))
            assert tuple(sum(T[j][k]*IN[i][k] for k in range(3))
                         for j in range(3)) == tuple(
                sum(in_images[t][i][k]*IN[k][j] for k in range(4))
                for j in range(3))

    import sympy as sp
    ls = sp.symbols('l0:4'); rs = sp.symbols('r0:4'); ms = sp.symbols('m0:2')
    sl = sp.Matrix([[sum(ls[k]*OUT[k][j] for k in range(4)) for j in range(3)]])
    sr = sp.Matrix([sum(rs[k]*IN[k][j] for k in range(4)) for j in range(3)])
    sP, sQ = sp.Matrix(P), sp.Matrix(Q)
    for name, base in families.items():
        values = {}
        for a,l in enumerate(OUT):
            for b,r in enumerate(IN):
                for c,M in enumerate(base):
                    values[a,b,c] = tuple(scalar(l,mul(mul(U,M),V),r)
                        for U,V in ((P,P),(Q,P),(P,Q),(Q,Q)))
        # Independent symbolic expansion, without polarization or integer
        # scalar tables. All missing monomials are explicitly checked as zero.
        sM = sp.zeros(3)
        for c,M in enumerate(base):
            sM += ms[c]*sp.Matrix(M)
        A,B,C,D = [(sl*U*sM*V*sr)[0]
                   for U,V in ((sP,sP),(sQ,sP),(sP,sQ),(sQ,sQ))]
        variables = ls+rs+ms[:len(base)]
        poly = sp.Poly(sp.expand(2*B*C-A*D), *variables)
        coefficients = []
        for aa,bb,cc in product(cwr(range(4),2),cwr(range(4),2),
                                cwr(range(len(base)),2)):
            choices = [((a,b),) if a==b else ((a,b),(b,a))
                       for a,b in (aa,bb,cc)]
            coefficient = 0
            for a,b,c in product(*choices):
                A,B,C,D = values[a[0],b[0],c[0]]
                AA,BB,CC,DD = values[a[1],b[1],c[1]]
                coefficient += 2*B*CC-A*DD
            powers = [0]*len(variables)
            for a in aa: powers[a] += 1
            for b in bb: powers[4+b] += 1
            for c in cc: powers[8+c] += 1
            assert coefficient == poly.coeff_monomial(tuple(powers))
            assert coefficient >= 0, (name,aa,bb,cc,coefficient)
            coefficients.append(coefficient)
        assert sum(c != 0 for c in coefficients) == len(poly.terms())
        reports[name] = {"basis_matrices":base,
            "coefficient_count":len(coefficients),
            "positive_coefficients":sum(c>0 for c in coefficients),
            "minimum_coefficient":min(coefficients),
            "coefficients":coefficients}
    # Sharpness for the actual word model, n=4, event sites 2 and 4,
    # conditioned on absence of an event at site 3.
    l,r,M = OUT[3],IN[2],P
    A,B,C,D = [scalar(l,mul(mul(U,M),V),r)
               for U,V in ((P,P),(Q,P),(P,Q),(Q,Q))]
    assert (A,B,C,D) == (2,1,1,1)
    result = {"job_id":JOB,"arithmetic":"exact integer arithmetic and SymPy",
        "statement":"For l in cone(OUT), r in cone(IN), and every product M of P,Q, define A=l P M P r, B=l Q M P r, C=l P M Q r, D=l Q M Q r. Then A D <= 2 B C.",
        "ray_cones_preserved":True,"alternating_word_identities_verified":True,
        "rank_one_reduction":"If M has rank at most one, AD=BC. Every word containing QQ has this rank. Compress PP; every remaining nonempty word is alternating and belongs to one of the four two-generator families.",
        "family_coefficient_order":"Lexicographic product of unordered pairs of output-ray indices, input-ray indices, and matrix-basis indices, each obtained using combinations_with_replacement.",
        "families":reports,"polynomial_coefficients_checked":sum(
            v['coefficient_count'] for v in reports.values()),
        "independent_symbolic_expansion_matches":True,
        "sharp_actual_example":{"n":4,"single_event_sites":[2,4],
            "fixed_absent_sites":[3],"A":A,"B":B,"C":C,"D":D,
            "ratio_AD_over_BC":2},
        "qualification":"A finite exact certificate for the stated matrix inequalities, with an explicit infinite-word reduction. Same-worker cross-check, not a fresh referee or a novelty claim.",
        "seconds":time.perf_counter()-start,
        "source_sha256":hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='families'},indent=2))

if __name__ == '__main__':
    main()
