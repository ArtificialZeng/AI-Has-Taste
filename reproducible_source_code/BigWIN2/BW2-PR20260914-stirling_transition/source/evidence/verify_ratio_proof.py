"""Exact error-detection checks for ratio-convexity-proof.md, not an infinite proof.

Run from the project directory: python3 evidence/verify_ratio_proof.py
Only Python's standard library and SymPy are used. No network or randomness.
"""
from fractions import Fraction as Q
from hashlib import sha256
from itertools import combinations, product
from math import factorial
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
JOB = "primary-20260914-stirling-transition-research-d94530e09967"


def digest(path):
    return sha256((ROOT / path).read_bytes()).hexdigest()


def elementary(xs):
    e = [Q(1)]
    for x in xs:
        e = [e[0]] + [e[j] + x*e[j-1] for j in range(1, len(e))] + [x*e[-1]]
    return e


def F(u, v, t):
    return u*(1+t*v)/(1+t*u)


def main():
    assert digest("source.md") == "4a37fe8a21f41aac0b72c9da83e28e1aff2ce19676fe24c5d93befb9e2d99594"
    u, v, t, w = sp.symbols("u v t w")
    f = lambda a, b: a*(1+t*b)/(1+t*a)
    lower = 2*t*t*(v-u)**3/((1+t*u)*(1+t*v)*(1+t*(2*v-u)))
    residuals = {
        "equal_step_identity": sp.factor(f(2*v-u, v)-2*f(v,u)+f(u,2*u-v)-lower),
        "first_argument_derivative": sp.factor(sp.diff(f(u,v),u)-(1+t*v)/(1+t*u)**2),
        "second_argument_derivative": sp.factor(sp.diff(f(u,v),v)-t*u/(1+t*u)),
        "upper_endpoint_limit": sp.factor(sp.limit(f(w,v), w, sp.oo)-(v+1/t)),
    }
    A, B, C, E, n = sp.symbols("A B C E n")
    H = B*B-A*C
    U = B*B*C-2*A*C*C+A*B*E
    Q1 = n*A+B
    Q2 = n*(n+1)*A+(2*n+1)*B+C
    raw = B*Q1*Q2-2*(n*B+C)*A*Q2+(n*(n+1)*B+(2*n+1)*C+E)*A*Q1
    positive_form = (n*A+B)*H+2*n*H*H/B+(1+n*A/B)*U
    residuals["positive_numerator_decomposition"] = sp.factor(raw-positive_form)
    residuals["U_ratio_identity"] = sp.factor(U/(A*B*C)-(B/A-2*C/B+E/C))
    assert all(x == 0 for x in residuals.values())

    # Adversarial rational four-ratio inputs, including u=0, flat slopes,
    # negative comparison value 2u-v, and the last-coefficient infinity limit.
    grid = [Q(0), Q(1,7), Q(1), Q(10)]
    lemma_count = endpoint_count = negative_comparison_count = 0
    for h,d,a,b in product(grid, repeat=4):
        u0 = h+d
        v0 = h+2*d+a
        w0 = h+3*d+2*a+b
        for t0 in [Q(1,9), Q(1), Q(7)]:
            rhs = 2*t0*t0*(v0-u0)**3/((1+t0*u0)*(1+t0*v0)*(1+t0*(2*v0-u0)))
            lhs = F(w0,v0,t0)-2*F(v0,u0,t0)+F(u0,h,t0)
            assert lhs >= rhs >= 0
            lemma_count += 1
            negative_comparison_count += (2*u0-v0 < 0)
            endpoint_lhs = v0+1/t0-2*F(v0,u0,t0)+F(u0,h,t0)
            assert endpoint_lhs >= rhs
            endpoint_count += 1

    # Generic symmetric-function families: equal, reciprocal, very separated,
    # a single large/small weight, and alternating extremes, in both orders.
    family_count = coefficient_centers = append_centers = 0
    for m in range(1,13):
        families = [
            [Q(1)]*m,
            [Q(1,j) for j in range(1,m+1)],
            [Q(10)**j for j in range(m)],
            [Q(10)**12]+[Q(1)]*(m-1),
            [Q(1,10**12)]+[Q(1)]*(m-1),
            [Q(10**8) if j%2 else Q(1,10**8) for j in range(m)],
        ]
        for xs in families:
            for ys in [xs, list(reversed(xs))]:
                e = elementary(ys)
                R = [Q(0)]+[e[j-1]/e[j] for j in range(1,m+1)]
                assert all(R[j]>R[j-1] for j in range(1,m+1))
                for j in range(1,m):
                    assert R[j+1]-2*R[j]+R[j-1] > 0
                    coefficient_centers += 1
                for t0 in [Q(1,10**9), Q(1), Q(10**9)]:
                    added = elementary(ys+[t0])
                    S = [Q(0)]+[added[j-1]/added[j] for j in range(1,m+2)]
                    assert S[-1] == R[-1]+1/t0
                    for j in range(1,m+1):
                        assert S[j] == F(R[j],R[j-1],t0)
                        assert S[j+1]-2*S[j]+S[j-1] > 0
                        append_centers += 1
                family_count += 1

    # Independent subset definition versus coefficient multiplication.
    subset_count = 0
    xs = [Q(1,2),Q(2,3),Q(3,5),Q(5,7),Q(7,11),Q(11,13),Q(13,17),Q(17,19),Q(19,23)]
    for m in range(10):
        e = elementary(xs[:m])
        for r in range(m+1):
            value = Q(0)
            for inds in combinations(range(m),r):
                term = Q(1)
                for i in inds: term *= xs[i]
                value += term
                subset_count += 1
            assert value == e[r]

    # Independent Stirling recurrence. Test the entire triangle through 160,
    # using two further rows for the q second differences.
    rows = [[1]]
    for nn in range(1,163):
        prev = rows[-1]
        row = [0]*(nn+1)
        for kk, value in enumerate(prev):
            row[kk] += (nn-1)*value
            row[kk+1] += value
        rows.append(row)
    def c(nn,kk):
        return rows[nn][kk] if 0<=kk<=nn else 0

    mapping_count = 0
    for nn in range(2,17):
        e = elementary([Q(1,j) for j in range(1,nn)])
        for kk in range(1,nn+1):
            assert c(nn,kk) == factorial(nn-1)*e[kk-1]
            mapping_count += 1

    q_count = d_count = d_identity_count = 0
    for kk in range(1,161):
        negative_seen = False
        for nn in range(1,161):
            D = c(nn,kk)**2-c(nn-1,kk)*c(nn+1,kk)
            if nn<kk: assert D==0
            if nn==kk: assert D==1
            if D<0: negative_seen = True
            if negative_seen: assert D<=0
            d_count += 1
            if nn>=kk+1:
                # Identity (7) with a common exact integer denominator.
                assert D == c(nn,kk)*c(nn-1,kk-1)-c(nn-1,kk)*c(nn,kk-1)-c(nn-1,kk)*c(nn,kk)
                d_identity_count += 1
            if nn<kk: continue
            aa,bb,cc,ee = [c(nn,kk-i) for i in range(4)]
            q1,q2 = c(nn+1,kk),c(nn+2,kk)
            raw_n = bb*q1*q2-2*c(nn+1,kk-1)*aa*q2+c(nn+2,kk-1)*aa*q1
            if kk==1:
                assert raw_n==0
            else:
                hh=bb*bb-aa*cc
                uu=bb*bb*cc-2*aa*cc*cc+aa*bb*ee
                assert hh>0 and uu>=0
                # Multiply by B to avoid rational evaluation of (5).
                assert bb*raw_n == bb*(nn*aa+bb)*hh+2*nn*hh*hh+(bb+nn*aa)*uu
                assert raw_n>0
            q_count += 1

    copied_sources = {}
    for file, expected in [
        ("2408.02782v1.html","6b4c97905f1fe95e002f603cb74c768b07180c9be9fa00bdba0414616b6e5a3b"),
        ("2607.04217v1.html","c2754444d71b8fb4bc3d6fc238a3bb42b65cc7008b39ceab8f82d8399394acb0"),
    ]:
        path = "evidence/external/"+file
        assert digest(path)==digest("literature/"+file)==expected
        copied_sources[path] = {"sha256":expected,"bytes":(ROOT/path).stat().st_size}
    result = {
        "job_id":JOB,
        "date":"2026-09-14",
        "source_sha256":digest("source.md"),
        "script_sha256":digest("evidence/verify_ratio_proof.py"),
        "proof_sha256":digest("evidence/ratio-convexity-proof.md"),
        "symbolic_residuals":{k:str(v) for k,v in residuals.items()},
        "sympy_version":sp.__version__,
        "rational_preservation_tests":{
            "finite_inputs":lemma_count,"infinite_endpoint_inputs":endpoint_count,
            "negative_comparison_value_inputs":negative_comparison_count,
            "grid":"h,d,a,b in {0,1/7,1,10}; t in {1/9,1,7}"},
        "elementary_symmetric_tests":{
            "families_including_reversals":family_count,"m_range":[1,12],
            "degree_convexity_centers":coefficient_centers,
            "appended_weight_centers":append_centers,
            "appended_weights":["1/10^9","1","10^9"],
            "independent_subsets":subset_count,"subset_dimension_range":[0,9]},
        "stirling_tests":{
            "q_range":"1<=k<=n<=160","q_count":q_count,
            "q_strict_for_k_at_least_2":True,
            "D_range":"1<=k<=160, 1<=n<=160","D_count":d_count,
            "D_ratio_identity_count":d_identity_count,
            "symmetric_coefficient_mapping_range":"2<=n<=16, 1<=k<=n",
            "symmetric_coefficient_mapping_count":mapping_count},
        "primary_source_copies":copied_sources,
        "all_assertions_passed":True,
        "limitations":"Exact finite error detection and symbolic identities. The infinite proof is the argument in ratio-convexity-proof.md. These checks are not a fresh referee pass or a novelty certificate."
    }
    target = ROOT/"evidence/verify_ratio_proof.json"
    tmp = target.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(result,indent=2)+"\n")
    tmp.replace(target)
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
