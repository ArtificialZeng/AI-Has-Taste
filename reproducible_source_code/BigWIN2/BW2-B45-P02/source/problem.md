# Precise problem reading

## Frozen claim and definitions

Fix (a\in\mathbb R) with (a>0).  Write the rising factorial as

\[
(a)_0=1,\qquad (a)_k=a(a+1)\cdots(a+k-1)\quad(k\geq1),
\]

and the falling factorial as (x^{\underline{k}}=x(x-1)\cdots(x-k+1)), with
(x^{\underline0}=1).  The polynomials

\[
e_k(x)=\frac{x^{\underline{k}}}{(a)_k}\qquad(k\geq0)
\]

form a basis of \(\mathbb R[x]\).  Define the degree-preserving real-linear
isomorphism \(L_a:\mathbb R[x]\to\mathbb R[x]\) by \(L_a(e_k)=x^k\).

The question is the following single universally quantified proposition:

\[
\forall a>0\;\forall P_1,P_2\in\mathbb R[x],\quad
\left.
\begin{array}{c}
\deg P_1=1,\ \deg P_2=2,\\
Z(L_a(P_1))\subseteq[-1,0],\\
Z(L_a(P_2))\subseteq[-1,0]
\end{array}
\right\}
\Longrightarrow Z(L_a(P_1P_2))\subseteq[-1,0].
\]

Here \(Z(Q)\) is the multiset of all complex zeros of the nonzero polynomial
\(Q\).  Thus containment in \([-1,0]\) asserts both real-rootedness and the
location of every zero, with multiplicity allowed.  The endpoint cases \(0\)
and \(-1\), repeated roots, and all \(a>0\) (without a compact lower or upper
bound) are included.

Multiplying either input by a nonzero real scalar does not affect any zero set,
and it only multiplies the output by the product of those scalars.  Hence the
claim is equivalent to the monic normalization

\[
L_a(P_1)=x+r,\qquad L_a(P_2)=(x+s)(x+t),
\quad a>0,\quad r,s,t\in[0,1].
\]

Under this normalization, the target is the cubic

\[
R_{a,r,s,t}(x)=c_0+c_1x+c_2x^2+c_3x^3,
\]

where

\[
\begin{aligned}
c_0&=rst,\\
c_1&=r(s+t)+st+\frac{s+t}{a},\\
c_2&=r+\frac{(a+1)(s+t)+2}{a},\\
c_3&=\frac{a+2}{a}>0.
\end{aligned}
\]

Thus the precise normalized assertion is

\[
\forall(a,r,s,t)\in(0,\infty)\times[0,1]^3,
\quad Z(R_{a,r,s,t})\subseteq[-1,0].
\]

## Exact reductions checked at triage

Direct symbolic expansion gives

\[
R_{a,r,s,t}(-1)=(r-1)(s-1)(t-1)
\]

and the reflection identity

\[
-R_{a,r,s,t}(-1-x)=R_{a,1-r,1-s,1-t}(x).
\]

All coefficients of every polynomial on the right are nonnegative and its
leading coefficient is positive.  Consequently \(R_{a,r,s,t}\) has no real
zero in \((0,\infty)\) and, by reflection, none in \(( -\infty,-1)\).
Therefore the original claim is exactly equivalent to proving that this cubic
is real-rooted throughout the parameter domain.  Equivalently, its cubic
discriminant must satisfy

\[
\operatorname{Disc}_x(R_{a,r,s,t})\geq0
\quad\text{for all }a>0,\ r,s,t\in[0,1].
\]

This equivalence includes discriminant-zero boundary cases.  A negative exact
discriminant at one admissible rational tuple would disprove the claim; a proof
requires a global nonnegativity certificate, not sampling.

## Scope and nearest prior result

The target is only the \((\deg P_1,\deg P_2)=(1,2)\) case; it does not assert
general multiplication closure.  In Anna Vishnyakova,
*Polynomially Deformed Normalized Pochhammer Sequences Having Generating
Functions With Only Real Non-positive Zeros*, arXiv:2608.03723v1 (submitted
2026-08-04), Definition 1.4 defines the same operator, Theorem D records
D. G. Wagner's multiplication-closure theorem for \(a=1\), and Open Problem
1.9 asks for the analogous statement for every \(a>0\).  Theorem 1.7 instead
imposes sufficient conditions on the zeros of one input polynomial and does
not settle this product-closure case.  The exact low-degree restriction above
was not found as a separately settled theorem in the limited searches recorded
in `evidence/triage.md`; this is a search report, not a priority claim.

Source status: **new-question nested in an open-supported problem**.  Suitability:
**advance**, because the claim reduces to explicit four-parameter polynomial
nonnegativity and admits exact CAD/discriminant or rational-counterexample tests.

