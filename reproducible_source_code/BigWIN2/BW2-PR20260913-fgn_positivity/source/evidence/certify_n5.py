"""Exact rational certificate for the n=5 one-sided fGn predictor.

Run: python3 evidence/certify_n5.py
Uses only the Python standard library. No floating-point operations enter
the certificate. The accompanying proof is evidence/n5-proof.md.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import comb, factorial
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
JOB = "primary-20260913-fgn-positivity-research-1f1ccfebc1c5"


def const(n, c):
    return {(0,) * n: c} if c else {}


def var(n, j):
    return {tuple(int(i == j) for i in range(n)): 1}


def add(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, 0) + c
    return {e: c for e, c in out.items() if c}


def scale(p, c):
    return {e: a * c for e, a in p.items() if a * c}


def mul(p, q):
    out = {}
    for e, a in p.items():
        for f, b in q.items():
            g = tuple(i + j for i, j in zip(e, f))
            out[g] = out.get(g, 0) + a * b
    return {e: c for e, c in out.items() if c}


def power(p, k, n):
    out = const(n, 1)
    for _ in range(k):
        out = mul(out, p)
    return out


def det(A):
    n = len(A)
    nd = len(next(iter(A[0][0])))
    out = {}
    for perm in permutations(range(n)):
        inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
        term = const(nd, (-1) ** inversions)
        for i in range(n):
            term = mul(term, A[i][perm[i]])
        out = add(out, term)
    return out


def cofactor_numerator(rs, n, k):
    A = [[rs[abs(i-j)] for j in range(n-1)] for i in range(n-1)]
    for i in range(n-1):
        A[i][k-2] = rs[i+1]
    return det(A)


def algebra():
    # Generic covariance variables: independent of the triage SymPy code.
    one = const(4, 1)
    r1, r2, r3, r4 = [var(4, j) for j in range(4)]
    q = add(r2, mul(r2, r2), scale(mul(r1, r1), -1), scale(mul(r1, r3), -1))
    K = add(mul(add(one, scale(r2, -1)), add(one, scale(r4, -1))),
            scale(power(add(r1, scale(r3, -1)), 2, 4), -1))
    rs = [one, r1, r2, r3, r4]
    assert cofactor_numerator(rs, 4, 3) == mul(add(one, scale(r2, -1)), q)
    assert cofactor_numerator(rs, 5, 3) == mul(q, K)

    # Entries 2*rho_j, with a=2^t, b=3^t, c=5^t. Their 4x4
    # column-3 Cramer determinant is exactly 16*N_54, without division.
    a, b, c = [var(3, j) for j in range(3)]
    R1 = add(a, const(3, -2))
    R2 = add(b, scale(a, -2), const(3, 1))
    R3 = add(mul(a, a), scale(b, -2), a)
    R4 = add(c, scale(mul(a, a), -2), b)
    four_q = add(scale(R2, 2), mul(R2, R2), scale(mul(R1, R1), -1),
                 scale(mul(R1, R3), -1))
    F = [(1, -1), (2, -2), (4, 4), (6, -2), (8, -1), (9, 1)]
    flatten = lambda p: sorted((2**i * 3**j * 5**k, v) for (i, j, k), v in p.items())
    assert flatten(four_q) == F
    assert add(scale(R2, 2), scale(mul(R1, R1), -1)) == add(R1, scale(R3, -1))
    P = cofactor_numerator([const(3, 2), R1, R2, R3, R4], 5, 4)
    terms = flatten(P)
    old = json.loads((ROOT / "evidence/triage-algebra.json").read_text())
    assert terms == [tuple(v) for v in old["n5"]["P_exponential_terms_base_coefficient"]]

    def derivative_at(t, order):
        out = {}
        for (i, j, k), coefficient in P.items():
            linear = add(scale(var(3, 0), i), scale(var(3, 1), j), scale(var(3, 2), k))
            out = add(out, scale(power(linear, order, 3), coefficient * (2**i * 3**j * 5**k)**t))
        return out

    assert not derivative_at(1, 0)
    assert all(not derivative_at(2, j) for j in range(3))
    assert derivative_at(1, 1) == add(scale(var(3, 0), 80), scale(var(3, 1), -48))
    return terms


def floor_scaled(x, scale_):
    return (x.numerator * scale_) // x.denominator


def ceil_scaled(x, scale_):
    return -floor_scaled(-x, scale_)


def log_interval(p, M=120, scale_=10**30):
    # log(p) = 2*sum_{j>=0} z^(2j+1)/(2j+1), z=(p-1)/(p+1).
    z = Q(p-1, p+1)
    lower = 2 * sum((z**(2*j+1) / (2*j+1) for j in range(M)), Q(0))
    tail = 2 * z**(2*M+1) / ((2*M+1) * (1-z*z))
    lo, hi = floor_scaled(lower, scale_), ceil_scaled(lower + tail, scale_)
    assert Q(lo, scale_) <= lower < lower + tail <= Q(hi, scale_)
    return lo, hi


def main():
    terms = algebra()
    N = 26
    log_scale, a_scale, beta_scale = 10**30, 10**12, 10**6
    prime_logs = {p: log_interval(p) for p in (2, 3, 5)}
    base_logs = {}
    for base, _ in terms:
        n, lo, hi = base, 0, 0
        for p in (2, 3, 5):
            while n % p == 0:
                n //= p
                lo += prime_logs[p][0]
                hi += prime_logs[p][1]
        assert n == 1
        base_logs[base] = (Q(lo, log_scale), Q(hi, log_scale))
        assert 0 <= lo <= hi < 5*log_scale

    # A_k = (-1)^k P^(k)(2)/k!, enclosed using rational log bounds.
    A = {}
    for k in range(3, N+1):
        lo, hi = Q(0), Q(0)
        for base, coefficient in terms:
            l, u = base_logs[base]
            v = Q((-1)**k * coefficient * base**2, factorial(k))
            if v >= 0:
                lo, hi = lo + v*l**k, hi + v*u**k
            else:
                lo, hi = lo + v*u**k, hi + v*l**k
        A[k] = (floor_scaled(lo, a_scale), ceil_scaled(hi, a_scale))
        assert Q(A[k][0], a_scale) <= lo <= hi <= Q(A[k][1], a_scale)
    assert A[3][0] > 0  # Also certifies the continued value at t=2.

    # G(x)=P(2-x)/x^3. G(1)=0. Approximate
    # G(x)/(1-x) by (G_N(x)-G_N(1))/(1-x).
    degree = N-4
    power_bounds = []
    for j in range(degree+1):
        lo = -sum(A[k][1] for k in range(j+4, N+1))
        hi = -sum(A[k][0] for k in range(j+4, N+1))
        power_bounds.append((Q(lo, a_scale), Q(hi, a_scale)))

    bernstein_lowers = []
    for i in range(degree+1):
        lo = sum((Q(comb(i, j), comb(degree, j)) * power_bounds[j][0]
                  for j in range(i+1)), Q(0))
        rounded = floor_scaled(lo, beta_scale)
        assert Q(rounded, beta_scale) > Q(271, 100)
        bernstein_lowers.append(rounded)

    S = sum(abs(c) * base**2 for base, c in terms)
    assert S == 212096
    # Ratio of (k-3)*5^k/k! to its predecessor, for k>=N+2,
    # is at most 5/(N-2). This bounds the whole omitted series.
    B = Q(S * (N-2) * 5**(N+1), factorial(N+1)) / (1-Q(5, N-2))
    assert B < Q(1, 200)
    assert Q(271, 100) - Q(1, 200) > Q(27, 10)
    result = {
        "job_id": JOB,
        "evidence_type": "exact rational all-interval certificate; not a fresh referee audit",
        "source_sha256": hashlib.sha256((ROOT / "source.md").read_bytes()).hexdigest(),
        "statement": "P(t)/((t-1)*(2-t)^3)>27/10 for 1<t<2, also for its analytic continuation at 1 and 2",
        "independently_recomputed_algebra": [
            "N43=(1-rho2)*q", "N53=q*K", "4*q=F(t)",
            "rho2-rho1^2=(rho1-rho3)/2", "P(t)=16*N54(t)",
            "P(1)=P(2)=P'(2)=P''(2)=0", "P'(1)=80*log(2)-48*log(3)"
        ],
        "P_exponential_terms_base_coefficient": terms,
        "log_series_terms": 120,
        "log_scale": log_scale,
        "prime_log_bounds_scaled": prime_logs,
        "N": N,
        "A_definition": "A_k=(-1)^k*P^(k)(2)/k!",
        "A_scale": a_scale,
        "A_bounds_scaled": A,
        "approximating_polynomial_degree": degree,
        "bernstein_lower_scale": beta_scale,
        "bernstein_lower_bounds_scaled": bernstein_lowers,
        "all_bernstein_coefficients_strictly_greater_than": "271/100",
        "absolute_exponential_weight_sum_S": S,
        "uniform_tail_bound_exact": str(B),
        "uniform_tail_bound_strictly_less_than": "1/200",
        "certified_uniform_lower_bound": "27/10"
    }
    output = ROOT / "evidence/n5-certificate.json"
    serialized = json.dumps(result, indent=2) + "\n"
    output.write_text(serialized)
    print(json.dumps({"certificate": str(output.relative_to(ROOT)),
                      "exact_algebra_checks": "passed",
                      "bernstein_coefficients": len(bernstein_lowers),
                      "minimum_bernstein_lower_bound": str(Q(min(bernstein_lowers), beta_scale)),
                      "tail_bound": str(B),
                      "uniform_lower_bound": "27/10"}))


if __name__ == "__main__":
    main()
