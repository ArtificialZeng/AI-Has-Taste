# Kernel discriminator and revised research target

Job: primary-20260913-inversion214-triage-cdf75c5e2abd, 2026-09-13.
These are triage derivations from the published equation, not an independently
audited result or a claim of novelty. The original algebraic-status question
is unresolved by this job.

Write V(x)=B(z,x,0) in Q[x][[z]], and

    T(x)=zx/(1-zx), H(x)=z(1+x)^2-x,
    S(x)=(1+x-zx)(1-z-zx)/(1-zx).

Multiply source equation (3.33) by y-x before substituting y=T(x).
This substitution is valid because coefficients of B are polynomials in
x,y and T is divisible by z. Cancellation of the common nonzero factors
in the resulting integral domain gives

    H(x)V(x) = V(T(x)) - S(x).                         (K)

All rational simplifications were checked symbolically, and (K) was checked
coefficientwise through z^16 using the published state rule. These finite
checks are corroboration; the substitution above supplies the argument.

Let c(z)=[x]V(x), d(z)=[x^2]V(x). There is no nonempty state with p=0,
so [x^0]V=1. Expanding (K) at x=0, using
S=1-z+(1-2z)x-sum_{k>=2}(zx)^k, yields

    z d = (1-z)c-z, hence F=1+c+d=c/z.                (E)

This identity is an elementary consequence of the inherited equation; it
is not advertised as a new enumeration theorem. It was also checked through
z^16, using c through z^17.

## Why unregularized iteration cannot discard its tail

For generic indeterminate x set t_j=T^j(x). Direct calculation gives

    t_j=z^j x / (1-x(z+...+z^j)), j>=1.

In Q(x)((z)), ord_z H(t_0)=0, ord_z H(t_1)=1 (leading coefficient 1-x),
and ord_z H(t_j)=1 for j>=2. After m iterations the tail is

    V(t_m) / product_{j=0}^{m-1} H(t_j).

Its order is 1-m, since V(t_m) has constant term 1. It does not tend to
zero. Even replacing V(t_m) by 1 leaves an error of order 2, since
c=z+O(z^2). This diagnoses this particular omitted-tail argument only.

## A specific repair worth one research pass

Set W(x)=V(x)-1-cx. Then W is divisible by z^2 x^2 and

    H(x)W(x)=W(T(x))+R0(x)+c R1(x),
    R0(x)=-z x^2(1-z-zx)/(1-zx),
    R1(x)=x^2(1-z-zx)^2/(1-zx).

The regularized tail at generic x has order at least m+3. Thus its
vanishing is compatible with formal iteration, unlike the preceding tail.

The small root X of H is

    X=(1-2z-sqrt(1-4z))/(2z)=z+2z^2+5z^3+...,

where the square root has constant term 1. Put q=T(X)=X^2/(1+2X), of
order 2. Substitution into (K) before dividing by H gives

    V(q)=S(X)=1+X^3/((1+X)(1+2X)).

This identifies a concrete boundary value. To turn it into a solved formula,
define t_0=q, t_{j+1}=T(t_j), D_j=product_{i=0}^j H(t_i), and test

    A=sum_{j>=0} R0(t_j)/D_j,
    L=q+sum_{j>=0} R1(t_j)/D_j,
    F ?= (S(X)-1-A)/(z L).                            (Q)

The orders of the A summands are j+4, those of the R1 summands are j+3,
and L has order 2 with leading coefficient 1. These give a precise route
to justify all infinite sums and the final Laurent division. The quotient
(Q) has not been independently implemented or audited here. Establishing
it rigorously with uniqueness and checking a held-out coefficient range is
the next discriminating test. Even a valid (Q) does not settle algebraicity;
an additional singularity or functional-identity argument is required.

Reproduce the completed checks from the project directory:

    python3 literature/inversion214-calibration.py
    python3 evidence/triage-kernel-check.py

The first reproduces definition/rule agreement for n=0..10. The second
uses exact integer arithmetic and SymPy rational simplification, with
explicit coverage in triage-kernel-check.json. No floating-point fitting,
algebraic degree search, or transcendence certificate was used.
