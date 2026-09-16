"""Exact finite diagnostics for the analytic double-star proof.

No root solver, floating-point arithmetic, or prior triage code is used.
Run from the project root: python3 evidence/research-exact-check.py
The all-parameter theorem is in double-star-proof.md, not this finite test.
"""
from fractions import Fraction
from functools import reduce
from hashlib import sha256
from math import comb, gcd
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent


def q_coefficients(a, b):
    q = a + b
    co = [0] * (q + 2)
    co[0] = q
    for r in (a, b):
        for j in range(r + 1):
            co[j] += comb(r, j)
    for j in range(q + 1):
        co[j + 1] += comb(q, j)
    return co


def induced_counts(a, b):
    # A fresh bit-mask implementation: count edges, not traversal/reachability.
    # Every induced subgraph of a tree is a forest, so e=v-1 iff connected.
    n = a + b + 2
    edges = [(0, 1)] + [(0, i) for i in range(2, a + 2)]
    edges += [(1, i) for i in range(a + 2, n)]
    counts = [0] * (n + 1)
    for mask in range(1, 1 << n):
        vertices = mask.bit_count()
        edge_count = sum(((mask >> u) & 1) * ((mask >> v) & 1)
                         for u, v in edges)
        if edge_count == vertices - 1:
            counts[vertices] += 1
    return counts


def primitive(co):
    assert co[-1] != 0
    content = reduce(gcd, (abs(x) for x in co))
    sign = 1 if co[-1] > 0 else -1
    return [sign * x // content for x in co]


def schur_certificate(co):
    """Integer Schur recursion, coefficients in ascending order.

    For degree d and real coefficients with leading A and constant B,
    |B|<|A| and Schur stability of (A P-B P*)/x imply Schur stability
    of P. Conversely this condition is necessary. Only the sufficient
    direction is needed here. Every recorded margin A^2-B^2 is exact.
    """
    co = primitive(co)
    initial = list(co)
    steps = []
    while len(co) > 1:
        degree = len(co) - 1
        leading, constant = co[-1], co[0]
        margin = leading * leading - constant * constant
        assert margin > 0, (degree, leading, constant)
        # Keep the certificate small: its initial polynomial and the recursion
        # reproduce every integer; intermediate coefficients can be enormous.
        payload = bytearray()
        for value in co:
            encoded = abs(value).to_bytes((abs(value).bit_length()+7)//8, 'big')
            payload.extend(b'-' if value < 0 else b'+')
            payload.extend(len(encoded).to_bytes(8, 'big'))
            payload.extend(encoded)
        steps.append({'degree': degree, 'margin_positive': margin > 0,
                      'leading_bits': leading.bit_length(),
                      'constant_bits': abs(constant).bit_length(),
                      'margin_bits': margin.bit_length(),
                      'coefficient_binary_sha256': sha256(payload).hexdigest()})
        reduced = [leading * co[j] - constant * co[degree-j]
                   for j in range(1, degree + 1)]
        assert reduced[-1] == margin
        co = primitive(reduced)
    assert co == [1]
    return {'initial_coefficients': [str(v) for v in initial],
            'steps': steps, 'final_constant': 1}


def rational_below_c(q, denominator=10000):
    # Largest numerator with (numerator/denominator)^(q+1)<q+1.
    lo, hi = denominator, 2 * denominator
    target = (q+1) * denominator ** (q+1)
    assert lo ** (q+1) < target < hi ** (q+1)
    while hi-lo > 1:
        middle = (lo+hi)//2
        if middle ** (q+1) < target:
            lo = middle
        else:
            hi = middle
    return Fraction(lo, denominator)


def inner_reciprocal(co):
    # (2u)^d Q((1-u)/(2u)); roots u=1/(2z+1).
    d = len(co)-1
    out = [0]*(d+1)
    for j, value in enumerate(co):
        for k in range(j+1):
            out[d-j+k] += value * 2**(d-j) * comb(j,k) * (-1)**k
    assert out[0] == co[-1]
    return out


def outer_scaled(co, c0):
    # R=c0+1/2=U/V, so V^d Q(R*x-1/2) has integral coefficients
    # when V is even. This is harmless scaling of the target polynomial.
    radius = c0 + Fraction(1,2)
    U, V = radius.numerator, radius.denominator
    if V % 2:
        U, V = 2*U, 2*V
    d = len(co)-1
    out = [0]*(d+1)
    for j, value in enumerate(co):
        for k in range(j+1):
            out[k] += value*comb(j,k)*U**k*(-V//2)**(j-k)*V**(d-j)
    return radius, out


def main():
    controls = []
    for co, expected in [([-1,2],True), ([1,0,4],True),
                         ([-2,1],False), ([-1,1],False),
                         ([1,0,1],False), ([1,-8,4],False)]:
        try:
            schur_certificate(co)
            result = True
        except AssertionError:
            result = False
        assert result == expected
        controls.append({'coefficients':co, 'expected_stable':expected,
                         'returned_stable':result})

    enumeration = []
    for q in range(2, 11):
        for a in range(1, q//2+1):
            b = q-a
            cc = induced_counts(a,b)
            assert cc[0] == 0 and cc[1:] == q_coefficients(a,b)
            enumeration.append({'a':a, 'b':b, 'counts':cc})

    certificates = []
    for q in range(2, 25):
        c0 = rational_below_c(q)
        assert c0 > 1 and c0**(q+1) < q+1
        for a in range(1, q//2+1):
            b = q-a
            co = q_coefficients(a,b)
            inner = schur_certificate(inner_reciprocal(co))
            radius, outer_co = outer_scaled(co,c0)
            outer = schur_certificate(outer_co)
            certificates.append({'a':a, 'b':b, 'q':q, 'n':q+2,
                                 'outer_radius':str(radius),
                                 'rational_c_below_target':str(c0),
                                 'inner':inner, 'outer':outer})

    # An independent symbolic construction checks both substitution maps,
    # including high degree, balanced and unbalanced cases.
    import sympy as sp
    z, u = sp.symbols('z u')
    transform_checks = []
    for a,b in [(1,1),(1,2),(1,7),(4,4),(1,23),(12,12)]:
        q = a+b
        d = q+1
        Q = q+(1+z)**a+(1+z)**b+z*(1+z)**q
        co = q_coefficients(a,b)
        pin = sum(value*u**j for j,value in enumerate(inner_reciprocal(co)))
        assert sp.cancel(pin-(2*u)**d*Q.subs(z,(1-u)/(2*u))) == 0
        radius, poc = outer_scaled(co,rational_below_c(q))
        R = sp.Rational(radius.numerator,radius.denominator)
        V = radius.denominator
        if V % 2:
            V *= 2
        pout = sum(value*u**j for j,value in enumerate(poc))
        assert sp.expand(pout-V**d*Q.subs(z,R*u-sp.Rational(1,2))) == 0
        transform_checks.append({'a':a,'b':b,'inner_identity':True,
                                 'outer_identity':True})

    # Exact endpoint-margin identities on algebraic c: clear denominators
    # and reduce c^(q+1)-(q+1), without assuming the analytic inequality.
    identities = []
    for q in range(2, 65):
        # Cross-multiplied identity, checked by integer polynomial reduction:
        # [(c+1)c^q-c-c^(q-1)-q]*c(c+1)(q+1)
        #          - (c-1)(q+1-c^2)*(c+1)c^q.
        c = sp.Symbol('c')
        numerator = ((c+1)*c**q-c-c**(q-1)-q)*c*(c+1)*(q+1)
        numerator -= (c-1)*(q+1-c**2)*(c+1)*c**q
        remainder = sp.rem(numerator, c**(q+1)-(q+1), c)
        assert remainder == 0
        identities.append({'q':q, 'remainder':0})

    report = {
        'status':'exact finite certificates; the infinite theorem is analytic',
        'job_id':'primary-20260913-subtree-annulus-research-bac30ce160a8',
        'arithmetic':'integer and rational only; SymPy polynomial remainders',
        'schur_controls':controls,
        'independent_symbolic_transform_checks':transform_checks,
        'coefficient_coverage':'q=2..10, a=1..floor(q/2), b=q-a',
        'coefficient_case_count':len(enumeration),
        'coefficient_checks':enumeration,
        'root_coverage':'q=2..24, a=1..floor(q/2), b=q-a; all roots per polynomial',
        'root_case_count':len(certificates),
        'root_certificate_method':'exact Schur recursion on reciprocal inner and scaled outer polynomials',
        'root_certificates':certificates,
        'endpoint_algebra_coverage':'q=2..64; polynomial identity modulo c^(q+1)-(q+1)',
        'endpoint_remainders':identities,
        'source_sha256':sha256((OUT.parent/'source.md').read_bytes()).hexdigest(),
        'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    target = OUT/'research-exact-checks.json'
    target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({'coefficient_cases':len(enumeration),
                      'root_cases':len(certificates),
                      'schur_recursions':2*len(certificates),
                      'endpoint_identities':len(identities),
                      'output':str(target.relative_to(OUT.parent)),
                      'all_passed':True}))


if __name__ == '__main__':
    main()
