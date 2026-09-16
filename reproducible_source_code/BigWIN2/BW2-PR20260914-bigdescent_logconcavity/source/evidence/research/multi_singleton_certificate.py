"""Exact Schur coefficient test for separate alternating gap families.

All calculations use Python integers. A certificate position is a monomial
of degree two in each boundary/gap parameter group, including zero positions.
This file does not assume that the tested sufficient condition is true.
"""
from functools import lru_cache
from itertools import product, combinations_with_replacement
from pathlib import Path
import hashlib
import json
import time

from two_singleton_certificate import P, Q, I, OUT, IN, mul, scalar

JOB = "primary-20260914-bigdescent-logconcavity-research-5c6b908e3ed6"
PQ, QP = mul(P,Q), mul(Q,P)
FAMILIES = {"I": (I,), "P": (P,mul(PQ,P)), "Q": (Q,mul(QP,Q)),
            "PQ": (PQ,mul(PQ,PQ)), "QP": (QP,mul(QP,QP))}


@lru_cache(None)
def monomial_domain(sizes):
    """Ordered multilinear indices, quadratic indices, product lookup."""
    linear = tuple(product(*(range(s) for s in sizes)))
    quad = tuple(product(*(tuple(combinations_with_replacement(range(s),2))
                           for s in sizes)))
    lookup = {q: i for i,q in enumerate(quad)}
    prod = tuple(tuple(lookup[tuple(tuple(sorted((a,b))) for a,b in zip(p,q))]
                       for q in linear) for p in linear)
    return linear, quad, prod


def counts_table(names):
    m = len(names)+1
    bases = [FAMILIES[n] for n in names]
    sizes = (4,4)+tuple(map(len,bases))
    linear, quad, prod = monomial_domain(sizes)
    values = [[0]*len(linear) for _ in range(1<<m)]
    for t in range(1<<m):
        for p,(a,b,*cs) in enumerate(linear):
            M = (P,Q)[t&1]
            for i,c in enumerate(cs):
                M = mul(mul(M,bases[i][c]), (P,Q)[(t>>(i+1))&1])
            values[t][p] = scalar(OUT[a],M,IN[b])
    return sizes, values


def coefficient_rows(names):
    sizes, vals = counts_table(names)
    linear, quad, prod = monomial_domain(sizes)
    m = len(names)+1
    mask = (1<<m)-1
    h = [[0]*len(quad) for _ in range(m//2+1)]
    for t,vt in enumerate(vals):
        j = t.bit_count()
        if j>m//2:
            continue
        left = [(p,c) for p,c in enumerate(vt) if c]
        right = [(p,c) for p,c in enumerate(vals[mask^t]) if c]
        for p,a in left:
            keys = prod[p]
            for q,b in right:
                h[j][keys[q]] += a*b
    schur = [h[0]]+[[a-b for a,b in zip(h[j],h[j-1])]
                    for j in range(1,len(h))]
    return sizes,schur


def main():
    start = time.perf_counter()
    results = {}
    for m in (2,3,4):
        cases = {}
        first_negative = None
        total = negative = 0
        for names in product(FAMILIES,repeat=m-1):
            sizes, rows = coefficient_rows(names)
            quad = monomial_domain(sizes)[1]
            negs = [(j,i,c) for j,row in enumerate(rows)
                    for i,c in enumerate(row) if c<0]
            total += sum(map(len,rows))
            negative += len(negs)
            if negs and first_negative is None:
                j,i,c = negs[0]
                first_negative = {"gap_families":names,"Schur_index":j,
                    "quadratic_parameter_pairs":quad[i],"coefficient":c}
            cases[','.join(names)] = {
                "group_sizes":sizes,
                "coefficient_positions_per_Schur_row":len(quad),
                "negative_coefficients":len(negs),
                "minimum_by_Schur_index":[min(row) for row in rows],
                "positive_counts_by_Schur_index":[sum(c>0 for c in row)
                                                  for row in rows],
                "coefficients":rows}
        expected = (m//2+1)*100*13**(m-1)
        assert total==expected
        results[str(m)] = {"family_cases":len(cases),
            "coefficient_positions":total,"negative_coefficients":negative,
            "first_negative":first_negative,"families":cases}
        print(json.dumps({"m":m,"family_cases":len(cases),
            "coefficient_positions":total,"negative_coefficients":negative,
            "first_negative":first_negative,"seconds":time.perf_counter()-start}),
              flush=True)
        # Save completed cases after each m, with explicit coverage.
        out = {"job_id":JOB,"arithmetic":"exact Python integers",
            "definition":"A_T=l U_1 M_1 U_2 ... M_(m-1) U_m r, U_i=Q if i in T and P otherwise. H=sum_T A_T A_(complement T) x^|T| y^(m-|T|).",
            "boundary_rays":{"output":OUT,"input":IN},
            "gap_families":FAMILIES,
            "parameter_domain":"Each boundary and each gap is a nonnegative real combination of its own listed family. Distinct gap families are not mixed.",
            "coefficient_order":"Lexicographic Cartesian product of combinations_with_replacement(range(size),2) for groups [output,input,gap1,...]. Schur row j is h_j-h_(j-1), h_-1=0.",
            "completed_m":list(map(int,results)),"results":results,
            "qualification":"Exact parameter-polynomial test. Negative coefficients refute this sufficient proof premise; they need not be negative values at admissible matrix words.",
            "seconds":time.perf_counter()-start,
            "source_sha256":hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
        dest = Path(__file__).with_suffix('.json')
        temp = dest.with_suffix('.json.tmp')
        temp.write_text(json.dumps(out,separators=(',',':'))+'\n')
        temp.replace(dest)


if __name__=='__main__':
    main()
