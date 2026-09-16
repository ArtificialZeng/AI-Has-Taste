"""Exact formula checks for a triage derivation; not an infinite-proof audit."""
import json
from fractions import Fraction as Q
from math import comb
from pathlib import Path


def coeffs(m):
    a = [0] * m
    a[-1] = 1
    for j in range(m - 2, -1, -1):
        a[j] = comb(m, j + 1) - 2 * a[j + 1]
    assert 2 * a[0] == 1 - (-1) ** m
    return a


def integral(j, k):
    return sum((Q(comb(k, ell) * 2**ell * (-1)**(k-ell), j+ell+1)
                for ell in range(k + 1)), Q(0))


def moment(p, k, r):
    return sum((Q(2 * comb(p, ell), k+r+ell+1)
                for ell in range(p + 1) if (k+r+ell) % 2 == 0), Q(0))


def hankel(p, k):
    u = [moment(p, k, r) for r in range(4)]
    return u[0] * u[2] - u[1]**2


checks = 0
top = []
for m in range(4, 21):
    a = coeffs(m)
    h = a.copy()
    h[0] += (-1)**m
    assert min(a) >= 0 and min(h) >= 0
    n = m - 1
    b = [Q(a[j], comb(n, j)) for j in range(m)]
    assert all(b[j] == m * integral(j, n-j) for j in range(m))
    for j in range(1, m - 1):
        minor = j*(n-j)*a[j]**2 - (j+1)*(m-j)*a[j-1]*a[j+1]
        turan = b[j-1]*b[j+1] - b[j]**2
        assert minor == -j*(n-j)*comb(n,j)**2*turan
        p, k = j-1, m-j-2
        assert turan == Q(m*m, 2**(2*j+2))*hankel(p,k)
        if j >= 2:
            assert minor == j*(n-j)*h[j]**2 - (j+1)*(m-j)*h[j-1]*h[j+1]
        if j >= 4:
            assert minor < 0
        if j == m-2:
            assert minor == -m
            top.append([m, j, minor])
        checks += 1

base_checks = recurrence_checks = 0
for k in range(1, 18, 2):
    assert hankel(3,k) == Q(64*(k+1), (k+2)**2*(k+4)**2*(k+6))
    base_checks += 1
    for p in range(1, 9):
        u = [moment(p,k,r) for r in range(4)]
        assert min(u) > 0
        e = u[1]*u[3] - u[2]**2
        assert e > 0
        rhs = (1+u[2]/u[1])*hankel(p,k) + (1+u[0]/u[1])*e
        assert hankel(p+1,k) == rhs
        recurrence_checks += 1

assert hankel(2,1) == Q(-16,225)
out = {
    "job_id": "primary-20260913-chen-ulc-failure-triage-085d5b98e601",
    "arithmetic": "exact Python integers and fractions.Fraction",
    "coefficient_m_range": [4,20],
    "internal_minor_identity_checks": checks,
    "base_case_odd_k_range": [1,17],
    "base_identity_checks": base_checks,
    "recurrence_p_range": [1,8],
    "recurrence_checks": recurrence_checks,
    "negative_control": {"p":2,"k":1,"H":"-16/225"},
    "top_endpoint_examples": top,
    "all_assertions_passed": True,
    "limitation": "Formula regression checks only; infinite sign proof and novelty require separate verification."
}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
