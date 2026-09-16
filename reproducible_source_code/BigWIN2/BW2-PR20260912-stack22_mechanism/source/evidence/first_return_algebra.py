"""Exact symbolic identity and independent coefficient recurrence checks."""
from pathlib import Path
import json
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def convolution(a, b, n):
    return sum(a[k]*b[n-k] for k in range(n+1))


def coefficients(N):
    # e_n = B_(n-1)+C_(n-1); d_n = 3B_(n-1)+C_(n-1)-[n=1].
    A, B, C, F, e, d = ([0]*(N+1) for _ in range(6))
    A[0] = C[0] = F[0] = 1
    for n in range(1, N+1):
        e[n] = B[n-1]+C[n-1]
        d[n] = 3*B[n-1]+C[n-1]-int(n == 1)
        A[n] = sum((e[k]+d[k])*A[n-k] for k in range(1, n+1))
        C[n] = sum(e[k]*C[n-k] for k in range(1, n+1))
        B[n] = sum(e[k]*B[n-k]+d[k]*A[n-k] for k in range(1, n+1))
        F[n] = sum(A[k-1]*F[n-k] for k in range(1, n+1))
    return A, B, C, F


def main():
    x, a, f = sp.symbols('x A F')
    R1 = f-1-x*a*f
    R2 = a-1-x*a*(4*a-2*f-1)
    P = 2*x*f**3-(2*x+3)*f**2-(x-7)*f-4
    multiplier = -4*x*a*f+2*x*f**2+x*f-3*f+4
    residual = sp.expand(P-x*f**2*R2-multiplier*R1)
    assert residual == 0
    A, B, C, F = coefficients(40)
    square = [convolution(F, F, n) for n in range(41)]
    cube = [convolution(square, F, n) for n in range(41)]
    cubic_residuals = [2*(cube[n-1] if n else 0)-2*(square[n-1] if n else 0)
                       -3*square[n]-(F[n-1] if n else 0)+7*F[n]-4*int(n == 0)
                       for n in range(41)]
    assert not any(cubic_residuals)
    assert all(A[n] == B[n]+C[n] and C[n] == F[n] for n in range(41))
    data = dict(job_id='primary-20260912-stack22-mechanism-research-897e72adb69b',
                arithmetic='exact polynomial expansion in SymPy; integer recursive coefficients',
                sympy_version=sp.__version__,
                identity='P = x F^2 R2 + (-4xAF+2xF^2+xF-3F+4) R1',
                polynomial_identity_residual=str(residual),
                formal_branch_derivative=int(sp.diff(P, f).subs({x: 0, f: 1})),
                coefficient_range=[0, 40], A=A, B=B, C=C, F=F,
                cubic_coefficient_residuals=cubic_residuals,
                limitation='The finite coefficient check is a verifier; the grammar proof supplies all-size validity.')
    dst = ROOT/'evidence/first_return_algebra.json'
    tmp = dst.with_suffix('.tmp')
    tmp.write_text(json.dumps(data, indent=2)+'\n')
    tmp.replace(dst)
    print(json.dumps({k:v for k,v in data.items() if k not in ['A','B','C','F','cubic_coefficient_residuals']}))
    print('F[0:13] =', F[:13])


if __name__ == '__main__':
    main()
