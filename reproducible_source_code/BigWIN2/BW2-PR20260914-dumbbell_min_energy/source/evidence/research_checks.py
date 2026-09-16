"""Reproduce the finite checks for the uniform singular-branch argument.

Run from the project root: python3 evidence/research_checks.py
Exact assertions and floating diagnostic observations are recorded separately.
No registry access, other processes, or external writes are performed.
"""
from functools import lru_cache
from pathlib import Path
import hashlib
import json
import sympy as S

JOB = 'primary-20260914-dumbbell-min-energy-research-4c017c9f21aa'
x, alpha, beta, t = S.symbols('x alpha beta t', real=True)


def graph(r, s, ell):
    n = r+s+ell-1
    edges = [(j, (j+1) % r) for j in range(r)]
    edges += [(r+j, r+(j+1) % s) for j in range(s)]
    path = [0] + list(range(r+s, n)) + [r]
    return n, edges + list(zip(path, path[1:]))


def matching_coefficients(n, edges, removed=()):
    adj = [0]*n
    for u, v in edges:
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    @lru_cache(None)
    def count(mask):
        if mask == 0:
            return (1,)
        v = (mask & -mask).bit_length()-1
        rest = mask ^ (1 << v)
        answer = list(count(rest)) + [0]
        neighbors = adj[v] & rest
        while neighbors:
            bit = neighbors & -neighbors
            neighbors ^= bit
            for k, value in enumerate(count(rest ^ bit)):
                answer[k+1] += value
        while len(answer) > 1 and answer[-1] == 0:
            answer.pop()
        return tuple(answer)

    mask = (1 << n)-1
    for v in removed:
        mask &= ~(1 << v)
    order = mask.bit_count()
    return {order-2*k: (-1)**k*v for k, v in enumerate(count(mask))}


def polynomial(r, s, ell):
    n, edges = graph(r, s, ell)
    def mp(removed=()):
        return S.Add(*(c*x**j for j, c in
                       matching_coefficients(n, edges, removed).items()))
    a = (-1)**((r+1)//2)*alpha
    b = (-1)**((s+1)//2)*beta
    return S.expand(mp()-2*a*mp(range(r))-2*b*mp(range(r, r+s))
                    +4*a*b*mp(range(r+s)))


triples = []
for r in (3, 5, 7, 9, 11):
    for s in (3, 5, 7, 9, 11):
        for ell in (1, 3, 5, 7, 9):
            n, edges = graph(r, s, ell)
            L = (ell-1)//2
            eps = (-1)**(n//2)
            full = matching_coefficients(n, edges)
            rem_r = matching_coefficients(n, edges, range(r))
            rem_s = matching_coefficients(n, edges, range(r, r+s))
            rem_both = matching_coefficients(n, edges, range(r+s))
            assert full[0] == eps
            assert rem_both[0] == (-1)**L
            assert rem_r[1] == (-1)**((n-r-1)//2)*(s+L)
            assert rem_s[1] == (-1)**((n-s-1)//2)*(r+L)
            p0 = full[0]+4*(-1)**((r+s+2)//2)*alpha*beta*rem_both[0]
            px0 = (-2*(-1)**((r+1)//2)*alpha*rem_r[1]
                   -2*(-1)**((s+1)//2)*beta*rem_s[1])
            H = (s+L)*alpha+(r+L)*beta
            assert S.expand(p0-eps*(1-4*alpha*beta)) == 0
            assert S.expand(px0+2*eps*H) == 0
            triples.append([r, s, ell])

# Check the characteristic formula directly with algebraic Hermitian matrices
# on singular points, including both normalization residues and both signs.
matrix_cases = []
for r, s, ell, av in [(3, 3, 1, S.Rational(1, 2)),
                      (3, 5, 1, S.Rational(1, 3)),
                      (5, 3, 3, -S.Rational(3, 4))]:
    bv = 1/(4*av)
    a = (-1)**((r+1)//2)*av
    b = (-1)**((s+1)//2)*bv
    z, w = a+S.I*S.sqrt(1-a*a), b+S.I*S.sqrt(1-b*b)
    n, edges = graph(r, s, ell)
    A = S.zeros(n)
    for u, v in edges:
        gain = z if (u, v) == (r-1, 0) else w if (u, v) == (r+s-1, r) else S.Integer(1)
        A[u, v], A[v, u] = gain, S.conjugate(gain)
    cp = A.charpoly().as_expr()
    cp = cp.subs(next(iter(cp.free_symbols)), x)
    pp = polynomial(r, s, ell).subs({alpha: av, beta: bv})
    assert S.simplify(S.expand(cp-pp)) == 0
    assert pp.subs(x, 0) == 0
    assert S.diff(pp, x).subs(x, 0) != 0
    matrix_cases.append({'triple': [r, s, ell], 'alpha': str(av), 'beta': str(bv)})

# Generic exact differential identities, with no numerical approximation.
u, d, z, w = S.symbols('u d z w', positive=True)
K = d+z*S.exp(2*u)+w*S.exp(-2*u)
assert S.simplify(S.diff(S.log(K), u, 2).subs(u, 0)
                  -4*(d*(z+w)+4*z*w)/(d+z+w)**2) == 0

p331 = polynomial(3, 3, 1)
half = p331.subs({alpha: S.Rational(1, 2), beta: S.Rational(1, 2)})
assert S.expand(half-x*(x+2)*(x*x-x-3)*(x*x-x-1)) == 0
c = S.symbols('c', real=True)
diagonal = p331.subs({alpha: c, beta: c})
assert S.expand(diagonal-(x**3-x*x-3*x+1-2*c)*(x**3+x*x-3*x-1-2*c)) == 0
slope = -S.diff(diagonal, c).subs({x: 0, c: S.Rational(1, 2)}) / S.diff(diagonal, x).subs({x: 0, c: S.Rational(1, 2)})
assert slope == -S.Rational(2, 3)
U, v, w = (S.sqrt(13)-1)/2, (1+S.sqrt(5))/2, (1+S.sqrt(13))/2
left = 4*(1/(5*v)-1/(6-U))
right = 4*(1/(6+w)+1/(5*v))
G = -S.Rational(2, 5)-2*S.sqrt(13)/39+2*S.sqrt(5)/5
assert S.simplify(left-(G-S.Rational(2, 3))) == 0
assert S.simplify(right-(G+S.Rational(2, 3))) == 0
# 11/5 < sqrt(5) < 9/4, 18/5 < sqrt(13) < 37/10.
assert S.Rational(11, 5)**2 < 5 < S.Rational(9, 4)**2
assert S.Rational(18, 5)**2 < 13 < S.Rational(37, 10)**2
Glow = -S.Rational(2, 5)-2*S.Rational(37, 10)/39+2*S.Rational(11, 5)/5
Ghigh = -S.Rational(2, 5)-2*S.Rational(18, 5)/39+2*S.Rational(9, 4)/5
assert 0 < Glow < Ghigh < S.Rational(2, 3)
Z, X, W = 1+7*t*t+11*t**4+t**6, 2*t**3*(1+3*t*t), 4*t**6
A0, B0 = Z-W/4, X
numerator = S.factor(-W*A0/2+X*B0)
assert S.expand(numerator-2*t**6*(1+5*t*t+7*t**4)) == 0

# Held-out exact test: D335 has a simple zero at the half diagonal, but the
# normal first-order condition fails.  Isolate every root and use rational
# interval arithmetic for the signed nonzero-root derivative sum.
p335 = polynomial(3, 3, 5).subs({alpha: c, beta: c})
q335 = S.Poly(p335.subs(c, S.Rational(1, 2)), x)
assert S.expand(q335.as_expr()-x*(x+2)*(x**4-x**3-5*x*x+3*x+5)*(x**4-x**3-3*x*x+x+1)) == 0
pc335 = S.Poly(S.diff(p335, c).subs(c, S.Rational(1, 2)), x)
assert S.expand(pc335.as_expr()+4*(x**7-7*x**5-x**4+13*x**3+3*x*x-5*x-1)) == 0
px335 = q335.diff()
assert S.gcd(q335, px335).degree() == 0
root_intervals335 = q335.intervals(eps=S.Rational(1, 10**13))
assert len(root_intervals335) == 10 and all(m == 1 for _, m in root_intervals335)


def interval_add(a, b):
    return (a[0]+b[0], a[1]+b[1])


def interval_multiply(a, b):
    vals = [aa*bb for aa in a for bb in b]
    return min(vals), max(vals)


def interval_poly(poly, interval):
    answer = (S.Integer(0), S.Integer(0))
    for cc in poly.all_coeffs():
        answer = interval_add(interval_multiply(answer, interval), (cc, cc))
    return answer


G335 = (S.Integer(0), S.Integer(0))
root_receipts335 = []
for interval, multiplicity in root_intervals335:
    lo, hi = interval
    assert multiplicity == 1 and (lo == hi or q335.count_roots(lo, hi) == 1)
    if lo == hi == 0:
        continue
    assert lo > 0 or hi < 0
    denominator = interval_poly(px335, interval)
    assert denominator[0]*denominator[1] > 0
    reciprocal = (1/denominator[1], 1/denominator[0])
    fraction = interval_multiply(interval_poly(pc335, interval), reciprocal)
    # sign(lambda)*lambda' = -sign(lambda)*P_c/P_x.
    factor = -1 if lo > 0 else 1
    signed = interval_multiply(fraction, (factor, factor))
    G335 = interval_add(G335, signed)
    root_receipts335.append({'root_interval': [str(lo), str(hi)],
                            'signed_derivative_interval': [str(vv) for vv in signed]})
assert S.Rational(407, 1000) < G335[0] <= G335[1] < S.Rational(408, 1000)
assert -pc335.eval(0)/px335.eval(0) == -S.Rational(2, 5)

# Supplement the all-length hyperbolic proof by exact rational-polynomial
# comparisons for r<s and ell in a finite independent range.  With v=exp(eta),
# t=v/(v^2-1), all hyperbolic expressions are rational.
v = S.symbols('v', positive=True)
sh = lambda k: (v**k-v**(-k))/2
ch = lambda k: (v**k+v**(-k))/2
ratio_cases = []
for r, s, ell in [(3, 5, 1), (3, 13, 1), (5, 9, 3), (7, 15, 5), (3, 15, 3)]:
    L = (ell-1)//2
    ceta = sh(ell-1)/(2*ch(ell)*ch(1))
    ratio = (sh(s)+ceta*ch(s))/(sh(r)+ceta*ch(r))
    # Exact positive coefficients after v=1+y verify the strict lower bound
    # for these cases, as an independent finite check of the analytic proof.
    y = S.symbols('y', positive=True)
    numerator, denominator = S.fraction(S.cancel(ratio-S.Rational(s+L, r+L)))
    pn = S.Poly(S.expand(numerator.subs(v, 1+y)), y)
    pd = S.Poly(S.expand(denominator.subs(v, 1+y)), y)
    assert all(cc >= 0 for cc in pn.all_coeffs()) and any(cc > 0 for cc in pn.all_coeffs())
    assert all(cc >= 0 for cc in pd.all_coeffs()) and any(cc > 0 for cc in pd.all_coeffs())
    ratio_cases.append([r, s, ell])

source_hash = hashlib.sha256(Path('source.md').read_bytes()).hexdigest()
assert source_hash == 'ec7265dcc8f807c129c4343be3ebf171d3c8a7b56c87316810172368a8e016fa'
out = {
    'job_id': JOB,
    'source_sha256': source_hash,
    'sympy_version': S.__version__,
    'coefficient_check_triples': triples,
    'coefficient_check_count': len(triples),
    'singular_matrix_characteristic_checks': matrix_cases,
    'generic_log_kernel_second_derivative_identity': '4*(d*(z+w)+4*z*w)/(d+z+w)^2',
    'D331_simple_zero_diagonal_slope': str(slope),
    'D331_smooth_diagonal_derivative': str(G),
    'D331_smooth_derivative_rational_bounds': [str(Glow), str(Ghigh)],
    'D331_derivative_jump': '4/3',
    'D331_stationarity_numerator': str(S.factor(-W*A0/2+X*B0)),
    'D335_polynomial_at_half': str(S.factor(q335.as_expr())),
    'D335_diagonal_polynomial_derivative_at_half': str(pc335.as_expr()),
    'D335_exact_nonzero_root_derivative_intervals': root_receipts335,
    'D335_smooth_diagonal_derivative_outer_bounds': ['407/1000', '408/1000'],
    'D335_zero_root_diagonal_derivative': '-2/5',
    'D335_directional_energy_derivative_along_minus_diagonal_bounds': ['-8/1000', '-7/1000'],
    'exact_kernel_ratio_check_triples': ratio_cases,
    'all_exact_assertions_passed': True,
    'scope': 'Finite exact checks supplement the complete arguments in singular-branch.md; no infinite claim follows from the tested range alone.',
    'independent_referee': False,
}
Path('evidence/research-checks.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k: out[k] for k in ['job_id', 'coefficient_check_count', 'singular_matrix_characteristic_checks', 'all_exact_assertions_passed']}, indent=2))
