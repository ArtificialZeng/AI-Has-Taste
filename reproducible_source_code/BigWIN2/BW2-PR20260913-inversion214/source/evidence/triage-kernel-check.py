#!/usr/bin/env python3
"""Exact finite and symbolic checks for triage, not a transcendence proof."""
from collections import Counter
from math import comb
from pathlib import Path
import json
import platform
import sympy as sp

N = 16
states = Counter({(0, 0): 1})
V = Counter()
counts, linear = [], []
for n in range(N + 2):
    counts.append(sum(m for (p, s), m in states.items() if s == 0 and p <= 2))
    linear.append(states[1, 0])
    if n <= N:
        for (p, s), m in states.items():
            if s == 0:
                V[n, p] += m
    nxt = Counter()
    for (p, s), m in states.items():
        nxt[p + 1, s] += m
        if s:
            nxt[p + 1, s - 1] += m
        else:
            for ell in range(p):
                nxt[p - ell, ell] += m
            for ell in range(p - 1):
                nxt[p - ell - 1, ell] += m
    states = nxt

# Coefficients indexed by (z degree, x degree). Verify H V - V(T) + S.
residual = Counter()
for (n, p), m in V.items():
    for dz, dx, a in [(1, 0, 1), (1, 1, 2), (1, 2, 1), (0, 1, -1)]:
        if n + dz <= N:
            residual[n + dz, p + dx] += a * m
    if p == 0:
        residual[n, 0] -= m
    else:
        # T^p=(zx)^p/(1-zx)^p.
        for r in range(p, N - n + 1):
            residual[n + r, r] -= m * comb(r - 1, p - 1)
residual[0, 0] += 1
residual[1, 0] -= 1
residual[0, 1] += 1
residual[1, 1] -= 2
for k in range(2, N + 1):
    residual[k, k] -= 1
nonzero = {str(k): v for k, v in residual.items() if v}
assert not nonzero
assert linear[1:] == counts[:-1]

z, x, c = sp.symbols('z x c')
T = z * x / (1 - z * x)
H = z * (1 + x)**2 - x
S = (1 + x - z*x) * (1 - z - z*x) / (1 - z*x)
R0 = -z*x*x*(1-z-z*x)/(1-z*x)
R1 = x*x*(1-z-z*x)**2/(1-z*x)
checks = {
    'H_from_cleared_equation': sp.factor((T+2*x*T-x*x)/(x*(1+T))-H),
    'S_from_cleared_equation': sp.factor(-(T+z)*(T-x)/(x*z*(1+T))-S),
    'constant_regularization': sp.factor(1-S-H-R0),
    'linear_regularization': sp.factor(T-H*x-R1),
    'small_root_specialization': sp.factor(S.subs(z,x/(1+x)**2)-1-x**3/((1+x)*(1+2*x))),
}
assert all(value == 0 for value in checks.values())
out = {
    'job_id': 'primary-20260913-inversion214-triage-cdf75c5e2abd',
    'python': platform.python_version(), 'sympy': sp.__version__,
    'arithmetic': 'exact integers and symbolic rational functions',
    'boundary_identity_z_degrees': [0, N],
    'boundary_nonzero_residuals': nonzero,
    'F_equals_linear_over_z_degrees': [0, N],
    'counts': counts[:N+1],
    'symbolic_residuals': {k: str(v) for k,v in checks.items()},
    'scope': 'Finite identity checks and exact rational simplifications; no solved F or algebraic-status proof.',
}
Path('evidence/triage-kernel-check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
