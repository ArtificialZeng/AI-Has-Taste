#!/usr/bin/env python3
"""Adversarial algebra and numerical checks; the universal proof is separate.

Run from PROJECT_DIR: python3 evidence/research-check.py
No randomness, network requests, background workers, or interval certificates.
"""
from fractions import Fraction as F
from hashlib import sha256
from math import comb, floor, isqrt
from pathlib import Path
import json
import platform
import mpmath as mp

mp.mp.dps = 90
exact = {"source_reflection": 0, "signed_polynomial_quadrature": 0,
         "rational_remainder": 0, "reciprocal_remainder": 0,
         "central_jump": 0, "floor_cell": 0}


def binomial_row(n):
    row, cumulative = [1], [1]
    for k in range(1, n+1):
        row.append(row[-1]*(n-k+1)//k)
        cumulative.append(cumulative[-1]+row[-1])
    return row, cumulative


def source_value(m, k, row, cumulative):
    if k < m:
        numerator = cumulative[k]
    else:
        u = 2*m-2-k
        numerator = (cumulative[u] if u >= 0 else 0)
        numerator += (k-m+1)*comb(2*m, k+1)
    return F(numerator, row[k])


for m in range(1, 49):
    n = 2*m-1
    row, cumulative = binomial_row(n)
    for k in range(n+1):
        d = k-m
        reflected = (F(cumulative[k], row[k]) if d < 0 else
                     F(2**n-cumulative[k], row[k]) + F(2*m*(d+1), m+d+1))
        assert source_value(m, k, row, cumulative) == reflected
        exact["source_reflection"] += 1
        if d >= 0:
            remainder = F(2*m*(d+1), m+d+1) - (2*d+2-F(2*d*d, m))
            displayed = -F(4*d+2, m)+F(2*(d+1)**3, m*(m+d+1))
            assert remainder == displayed
            exact["rational_remainder"] += 1
    assert (source_value(m, m, row, cumulative)-source_value(m, m-1, row, cumulative)
            == F(m-1, m+1))
    exact["central_jump"] += 1

# Both orientations, d=-1 (empty sum), d=0, and nonconstant monomials.
for q in range(1, 8):
    h = F(1, q)
    for d in range(-20, 21):
        y = d*h
        for power in range(4):
            def g(t):
                return t**power
            t_sum = (h*sum(g(j*h) for j in range(d+1)) if d >= 0 else
                     -h*sum(g(j*h) for j in range(d+1, 0)))
            err = t_sum-y**(power+1)/F(power+1)-h*(g(F(0))+g(y))/2
            predicted = (F(0) if power <= 1 else
                         y*h*h/6 if power == 2 else y*y*h*h/4)
            assert err == predicted
            exact["signed_polynomial_quadrature"] += 1

for y in (F(-3), F(-1), F(0), F(1), F(3)):
    for h in (F(1, 10), F(1, 30)):
        for rho in (F(-1, 1000), F(0), F(1, 1000)):
            z = 1-y*h+rho
            assert 1/z-1-y*h == (y*y*h*h-rho*(1+y*h))/z
            exact["reciprocal_remainder"] += 1


def as_mp(x):
    return mp.mpf(x.numerator)/x.denominator


def constants(A):
    B = A+1
    K = F(1, 4)+F(5, 6)*B*B+B**4/3
    M = -((-max(F(4), 4*B*B, K).numerator)//max(F(4), 4*B*B, K).denominator)
    B, K = as_mp(B), as_mp(K)
    c = 1/mp.sqrt(mp.pi)
    L = mp.mpf('1.5')*mp.e*K
    D = c*((B+1)*L+B*(2+4*B*B)/12+B/2+B*(6*B+4*B**3)/12)
    J = 2*mp.e*(B*B+mp.mpf('1.5')*L)
    a = c*mp.exp(-B*B)
    Q = (J+2*mp.e*D)/a+B+J
    T = 4*B+2+2*(B+1)**3
    b = mp.sqrt(mp.pi)/2
    U, W = (2+4*B*B)*b+2*B, (1+2*B*B)*b+5*B
    return M, L, D, Q+T+U/2+W


theta_values = (F(0), F(1, 10**20), F(1, 3), 1-F(1, 10**20))
numeric_rows = []
total, eligible = 0, 0
for m in (17, 127, 509, 2039):
    row, cumulative = binomial_row(2*m-1)
    h = 1/mp.sqrt(m)
    for A in (F(1, 8), F(1), F(3), F(6)):
        # The endpoint index is found exactly: r^2 <= A^2*m < (r+1)^2.
        r = isqrt((A*A*m).numerator//(A*A*m).denominator)
        ds = sorted({-r-1, -r, -r+1, -(r//2), -2, -1, 0, 1, 2,
                     r//2, r-1, r})
        M, L, D, C = constants(A)
        maxima = dict(local_scaled=mp.mpf(0), cdf_scaled=mp.mpf(0),
                      expectation_scaled=mp.mpf(0))
        count = 0
        for d in ds:
            k = m+d
            if not 0 <= k < 2*m:
                continue
            y = d*h
            f = mp.exp(-y*y)/mp.sqrt(mp.pi)
            p = mp.mpf(row[k])/2**(2*m-1)
            S = mp.mpf(cumulative[k])/2**(2*m-1)
            E = as_mp(source_value(m, k, row, cumulative))
            for theta in theta_values:
                u = d+theta
                # x=u/sqrt(m), so the window and floor are certified rationally.
                if u*u > A*A*m:
                    continue
                assert floor(u) == d and -1 < -theta <= 0
                exact["floor_cell"] += 1
                x, delta = as_mp(u)*h, -as_mp(theta)
                H = mp.sqrt(mp.pi)/2*mp.exp(x*x)*mp.erfc(abs(x))
                F0 = H+2*max(x, 0)
                F1 = (2*delta+1)*x*H+delta+1-2*max(x, 0)**2
                values = {
                    "local_scaled": m*abs(p/(h*f)-(1-y*h)),
                    "cdf_scaled": m*abs(S-mp.erfc(-y)/2-h*f),
                    "expectation_scaled": abs(E-F0/h-F1)/h,
                }
                for key, value in values.items():
                    maxima[key] = max(maxima[key], value)
                if m >= M:
                    assert values["local_scaled"] <= L
                    assert values["cdf_scaled"] <= D
                    assert values["expectation_scaled"] <= C
                    eligible += 1
                count += 1
        total += count
        numeric_rows.append({
            "m": m, "A": str(A), "samples": count, "M_A": M,
            "within_proved_m_threshold": m >= M,
            **{key: mp.nstr(value, 20) for key, value in maxima.items()},
            "proved_C_A_nonoptimized": mp.nstr(C, 12),
        })

result = {
    "job_id": "newwin-00001-p20-research-f42a5d965fef",
    "status": "exact finite algebra checks and finite floating-point consistency checks passed",
    "python": platform.python_version(), "mpmath": mp.__version__,
    "decimal_digits": mp.mp.dps, "exact_checks": exact,
    "exact_coverage": {
        "source_reflection_and_central_jump": "m=1..48, all admissible k",
        "rational_remainder": "m=1..48, 0<=d<=m-1",
        "quadrature": "h=1/q, q=1..7; d=-20..20; monomials 1,t,t^2,t^3",
        "reciprocal": "5 rational y, 2 rational h, 3 rational rho",
    },
    "numeric_samples": total, "samples_within_proved_m_threshold": eligible,
    "theta_values": [str(t) for t in theta_values], "rows": numeric_rows,
    "numeric_definitions": {
        "local_scaled": "m*abs(p/(h*f(y))-(1-y*h))",
        "cdf_scaled": "m*abs(S-P(y)-h*f(y))",
        "expectation_scaled": "sqrt(m)*abs(E-sqrt(m)*F0-F1)",
    },
    "source_sha256": sha256(Path('source.md').read_bytes()).hexdigest(),
    "proof_sha256": sha256(Path('evidence/research-proof.md').read_bytes()).hexdigest(),
    "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
    "limitations": "Finite nonexhaustive numerical samples at nonsquare m, not interval arithmetic. Exact algebra/floor checks cover only the displayed finite ranges. The infinite uniform result depends on the analytic proof; this run is not independent mathematical review."
}
print(json.dumps(result, indent=2))
