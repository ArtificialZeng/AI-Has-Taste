"""Exact symbolic identities for runs of singleton profile entries."""
from pathlib import Path
import hashlib
import json
import sympy as sp
from schur_profiles import tensor

x,y,z = sp.symbols('x y z')
q,s,h2 = x*y,x+y,x*x+x*y+y*y
P = sp.Matrix([[1,0,0],[1,0,0],[0,0,1]])
Q = sp.Matrix([[0,1,1],[0,0,0],[0,1,0]])
R0 = sp.kronecker_product(P,P)
R = x*sp.kronecker_product(Q,P)+y*sp.kronecker_product(P,Q)
R2 = q*sp.kronecker_product(Q,Q)
zero = lambda M: all(sp.expand(a)==0 for a in M)
assert zero(R0**2-R0)
assert zero(R2**3)
assert zero(R2*R*R2)
assert zero(R**8-q*R**6-q*s*R**5-5*q*q*R**4
            -2*q*q*s*R**3-q*q*h2*R**2-q**3*s*R)
base = {}
for lead in (0,1):
    for tail in (0,1):
        rows=[]
        for r in range(8):
            h=tensor((0,)*lead+(1,)*r+(0,)*tail)
            sch=[h[j]-(h[j-1] if j else 0) for j in range(r//2+1)]
            assert all(a>=0 for a in sch)
            rows.append(sch)
        base[f'{lead},{tail}']=rows
# Independently verify the claimed scalar generating-function numerator by
# its first eight coefficients; the universal order-eight identity then
# determines the complete sequence.
D=1-q*z**2-q*s*z**3-5*q*q*z**4-2*q*q*s*z**5-q*q*h2*z**6-q**3*s*z**7
N=1+q*z**2+2*q*s*z**3+3*q*q*z**4+2*q*q*s*z**5+q*q*h2*z**6
u=sp.kronecker_product(sp.Matrix([0,1,1]),sp.Matrix([0,1,1]))
v=sp.kronecker_product(sp.Matrix([1,0,1]),sp.Matrix([1,0,1]))
terms=[];w=v
for r in range(8):
    terms.append((u.T*w)[0]);w=R*w
residual=sp.Poly(sp.expand(D*sum(a*z**j for j,a in enumerate(terms))-N),z)
assert all(sp.expand(residual.coeff_monomial(z**j))==0 for j in range(8))
profile=(1,0,1);w=R*R0*R*v
assert sp.expand(w[8])==x*x+y*y
assert sp.expand((u.T*w)[0])==2*h2
out={"job_id":"primary-20260914-bigdescent-logconcavity-research-6ff0786c2423",
    "arithmetic":"exact symbolic polynomials and Python integers",
    "matrix_identity":"R1^8 = xy R1^6 + xy(x+y)R1^5 + 5(xy)^2 R1^4 + 2(xy)^2(x+y)R1^3 + (xy)^2(x^2+xy+y^2)R1^2 + (xy)^3(x+y)R1",
    "identity_verified_entrywise":True,
    "vanishing_profile_blocks":[[2,2,2],[2,1,2]],
    "all_one_block_boundary_bases_Schur_coefficients":base,
    "all_one_generating_function":{"numerator":str(N),"denominator":str(D)},
    "diagonal_state_counterexample":{"profile":profile,"CC":"x^2+y^2",
        "CC_s_(1,1)_coefficient":-1,"accepted_scalar":"2(x^2+xy+y^2)"},
    "qualification":"Proves the contextual run reduction and all singleton-block boundary families at every run length. Does not prove arbitrary mixed profiles or original LC.",
    "source_sha256":hashlib.sha256(Path('source.md').read_bytes()).hexdigest(),
    "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='all_one_block_boundary_bases_Schur_coefficients'},indent=2))
