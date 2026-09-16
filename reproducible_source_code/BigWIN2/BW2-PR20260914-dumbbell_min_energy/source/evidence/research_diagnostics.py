"""Floating held-out diagnostics; not exact certificates or proofs.

Run: python3 evidence/research_diagnostics.py
Compares source-kernel quadrature, Hermitian eigenspaces, and one-sided finite
differences without using the symbolic matching verifier.
"""
from pathlib import Path
from functools import lru_cache
import json
import numpy as np
from numpy.polynomial import Polynomial as Poly
from scipy.integrate import quad

JOB = 'primary-20260914-dumbbell-min-energy-research-4c017c9f21aa'


def matrix(r, s, ell, alpha, beta, derivatives=False):
    n = r+s+ell-1
    A = np.zeros((n, n), complex)
    edges = [(j, (j+1) % r) for j in range(r)]
    edges += [(r+j, r+(j+1) % s) for j in range(s)]
    path = [0]+list(range(r+s, n))+[r]
    edges += list(zip(path, path[1:]))
    DD = []
    for j, (u, v) in enumerate(edges):
        gain = 1
        if j in (r-1, r+s-1):
            value, sign = ((alpha, (-1)**((r+1)//2)) if j == r-1
                           else (beta, (-1)**((s+1)//2)))
            raw = value*sign
            gain = raw+1j*np.sqrt(max(0, 1-raw*raw))
            if derivatives:
                D = np.zeros_like(A)
                D[u, v] = sign-1j*raw*sign/np.sqrt(1-raw*raw)
                D[v, u] = D[u, v].conjugate()
                DD.append(D)
        A[u, v], A[v, u] = gain, np.conj(gain)
    return A, DD


def energy(r, s, ell, a, b):
    A, _ = matrix(r, s, ell, a, b)
    return float(np.abs(np.linalg.eigvalsh(A)).sum())


def kernel_gradient(r, s, ell, alpha, beta):
    u = Poly([0, 1])
    @lru_cache(None)
    def f(k):
        if k == -1:
            return Poly([0])
        if k == 0:
            return Poly([1])
        return f(k-1)+u*f(k-2)
    def g(k):
        return f(k)+u*f(k-2)
    R = f(ell-1)*g(s)+u*f(ell-2)*f(s-1)
    S = f(ell-1)*g(r)+u*f(ell-2)*f(r-1)
    if ell == 1:
        M = g(r)*g(s)+u*f(r-1)*f(s-1)
    else:
        M = (f(ell-1)*g(r)*g(s)
             +u*f(ell-2)*(f(r-1)*g(s)+f(s-1)*g(r))
             +u*u*f(ell-3)*f(r-1)*f(s-1))
    def shift_even(poly, shift=0, scale=1):
        coef = np.zeros(shift+2*poly.degree()+1)
        coef[shift::2] = scale*poly.coef
        return Poly(coef)
    Z = shift_even(M)
    X, Y = shift_even(R, r, 2), shift_even(S, s, 2)
    W = shift_even(f(ell-1), r+s, 4)
    A, B = Z-W/4, alpha*X+beta*Y
    C = (A*A+B*B).trim()
    result = []
    errors = []
    for num in (-beta*W*A+X*B, -alpha*W*A+Y*B):
        num = num.trim()
        low, e1 = quad(lambda t: num(t)/(t*t*C(t)), 0, 1,
                       epsabs=2e-10, epsrel=2e-10)
        nr, cr = Poly(num.coef[::-1]), Poly(C.coef[::-1])
        exponent = C.degree()-num.degree()
        high, e2 = quad(lambda v: v**exponent*nr(v)/cr(v), 0, 1,
                        epsabs=2e-10, epsrel=2e-10)
        result.append(2*(low+high)/np.pi)
        errors.append(2*(e1+e2)/np.pi)
    return np.array(result), errors


cases = []
for r, s, ell, a in [(3, 7, 5, 2/5), (9, 5, 7, 3/4),
                      (7, 11, 3, -1/3), (13, 13, 9, 1/2),
                      (3, 3, 5, 1/2)]:
    b = 1/(4*a)
    A, DD = matrix(r, s, ell, a, b, True)
    ev, V = np.linalg.eigh(A)
    zero = np.argmin(abs(ev))
    assert abs(ev[zero]) < 5e-14
    signs = np.sign(ev)
    signs[zero] = 0
    signed_projection = (V*signs)@V.conj().T
    smooth = np.array([np.trace(signed_projection@D).real for D in DD])
    zero_grad = np.array([(V[:, zero].conj()@D@V[:, zero]).real for D in DD])
    H = (s+(ell-1)/2)*a+(r+(ell-1)/2)*b
    predicted_zero = -2*np.array([b, a])/H
    integral_grad, integration_errors = kernel_gradient(r, s, ell, a, b)
    assert np.max(abs(zero_grad-predicted_zero)) < 1e-11
    assert np.max(abs(smooth-integral_grad)) < 2e-8
    E0 = energy(r, s, ell, a, b)
    directions = []
    for h in [np.array([1., 0.]), np.array([0., 1.]),
              np.array([1., 1.]), np.array([-1., -1.]), np.array([a, -b])]:
        predicted = float(smooth@h+abs(predicted_zero@h))
        approx = []
        for step in (1e-4, 1e-5, 1e-6):
            val = (energy(r, s, ell, a+step*h[0], b+step*h[1])-E0)/step
            approx.append(float(val))
        assert abs(approx[-1]-predicted) < 3e-5
        directions.append({'h': h.tolist(), 'predicted': predicted,
                           'one_sided_steps': [1e-4, 1e-5, 1e-6],
                           'finite_differences': approx})
    cases.append({'triple': [r, s, ell], 'alpha': a, 'beta': b,
                  'smallest_absolute_eigenvalue': float(abs(ev[zero])),
                  'spectral_smooth_gradient': smooth.tolist(),
                  'kernel_integral_gradient': integral_grad.tolist(),
                  'quadrature_reported_absolute_errors': integration_errors,
                  'zero_root_gradient_error': float(max(abs(zero_grad-predicted_zero))),
                  'directions': directions})

# Equality in the sufficient length criterion: s+L=4(r+L).
r, s, ell = 3, 15, 3
p = 1/4
left = np.log(p)/2
offsets = [0, 0.01, 0.05, 0.1, 0.3, 0.6]
values = [energy(r, s, ell, np.sqrt(p)*np.exp(left+v),
                 np.sqrt(p)*np.exp(-left-v)) for v in offsets]
assert all(values[j+1] > values[j] for j in range(len(values)-1))
out = {'job_id': JOB, 'arithmetic': 'NumPy float64 / SciPy quadrature; non-certified',
       'interior_cases': cases,
       'boundary_case': {'triple': [r, s, ell], 'product': p,
                         'offsets_from_left_log_ratio_endpoint': offsets,
                         'energies': values},
       'all_diagnostic_tolerances_met': True,
       'scope': 'Five held-out directional cases and one boundary diagnostic. No global classification, interval certification, or novelty inference.',
       'independent_referee': False}
Path('evidence/research-diagnostics.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({'interior_cases': len(cases), 'boundary_case': out['boundary_case'],
                  'all_diagnostic_tolerances_met': True}, indent=2))
