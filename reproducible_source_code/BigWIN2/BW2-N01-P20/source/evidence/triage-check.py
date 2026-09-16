#!/usr/bin/env python3
"""Deterministic independent finite screen; numerical errors are not certificates."""
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import mpmath as mp

mp.mp.dps = 70
exact = {"symmetry": 0, "cdf_from_half": 0, "upper_ratio": 0, "center": 0}
for m in range(1, 65):
    n = 2*m-1
    c = [math.comb(n, i) for i in range(n+1)]
    for k in range(n+1):
        d = k-m
        assert c[k] == c[n-k]
        exact["symmetry"] += 1
        from_half = 2**(n-1)
        from_half += sum(c[m:k+1]) if d >= 0 else -sum(c[k+1:m])
        assert from_half == sum(c[:k+1])
        exact["cdf_from_half"] += 1
        if d >= 0:
            assert Fraction((d+1)*math.comb(2*m,k+1),c[k]) == Fraction(2*m*(d+1),k+1)
            exact["upper_ratio"] += 1
    lower = Fraction(sum(c[:m]), c[m-1])
    upper = Fraction(sum(c[:m-1])+math.comb(2*m,m+1),c[m])
    assert lower == Fraction(2**n,math.comb(2*m,m))
    assert upper-lower == Fraction(m-1,m+1)
    exact["center"] += 1

rows = []
sample_count = 0
for m in (25, 100, 400, 1600):
    n = 2*m-1
    root = math.isqrt(m)  # chosen m are squares: exact floor-cell inputs
    masses = [1]
    for i in range(1,n+1):
        masses.append(masses[-1]*(n-i+1)//i)
    for A in (1,2,4):
        maxima = {"local_scaled": mp.mpf(0), "cdf_scaled": mp.mpf(0),
                  "expectation_scaled": mp.mpf(0)}
        count = 0
        for d in range(-A*root,A*root+1):
            k = m+d
            if not 0 <= k <= n:
                continue
            p = mp.mpf(masses[k])/2**n
            u = mp.mpf(d)/root
            f = mp.exp(-u*u)/mp.sqrt(mp.pi)
            local = m*abs(p*root/f-(1-u/root))
            half = 2**(n-1)
            half += sum(masses[m:k+1]) if d >= 0 else -sum(masses[k+1:m])
            cdf = mp.mpf(half)/2**n
            cdf_res = m*abs(cdf-mp.erfc(-u)/2-f/root)
            maxima["local_scaled"] = max(maxima["local_scaled"],local)
            maxima["cdf_scaled"] = max(maxima["cdf_scaled"],cdf_res)
            if d < 0:
                E = mp.mpf(half)/masses[k]
            else:
                threshold = m-d-2
                num = 2**(n-1)-sum(masses[threshold+1:m])
                E = mp.mpf(num)/masses[k]+mp.mpf(2*m*(d+1))/(m+d+1)
            for theta in (Fraction(0),Fraction(1,10**8),Fraction(1,2),
                          Fraction(10**8-1,10**8)):
                x_exact = (d+theta)/root
                if abs(x_exact) > A:
                    continue
                assert math.floor(x_exact*root) == d
                x = mp.mpf(x_exact.numerator)/x_exact.denominator
                delta = -mp.mpf(theta.numerator)/theta.denominator
                H = mp.sqrt(mp.pi)*mp.exp(x*x)*mp.erfc(abs(x))/2
                F0 = H+(2*x if x>=0 else 0)
                F1 = (2*delta+1)*x*H+delta+1-(2*x*x if x>=0 else 0)
                residual = root*abs(E-root*F0-F1)
                maxima["expectation_scaled"] = max(maxima["expectation_scaled"],residual)
                count += 1
        sample_count += count
        rows.append({"m":m,"A":A,"samples":count,
                     **{key:mp.nstr(value,18) for key,value in maxima.items()}})
result = {
    "job_id":"newwin-00001-p20-triage-041b4cdafc30",
    "status":"exact finite identity checks and floating-point calibration only",
    "python":platform.python_version(),"mpmath":mp.__version__,"decimal_digits":mp.mp.dps,
    "exact_checks":exact,"sample_count":sample_count,"rows":rows,
    "local_scaled_definition":"m*abs(p*sqrt(m)/f(d/sqrt(m))-(1-d/m))",
    "cdf_scaled_definition":"m*abs(S-Phi(sqrt(2)*d/sqrt(m))-f(d/sqrt(m))/sqrt(m))",
    "expectation_scaled_definition":"sqrt(m)*abs(E-sqrt(m)*F0-F1)",
    "floor_offsets":["0","1/100000000","1/2","99999999/100000000"],
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "source_sha256":hashlib.sha256(Path("source.md").read_bytes()).hexdigest(),
    "limitations":"finite m and A only; no interval arithmetic and no universal remainder bound"
}
print(json.dumps(result,indent=2))
