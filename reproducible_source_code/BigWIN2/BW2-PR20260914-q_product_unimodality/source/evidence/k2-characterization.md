# Exact two-factor criterion at arbitrary stretch

Proposer: `primary-20260914-q-product-unimodality-research-ba86ac9fff54`.
Date: 2026-09-14. Research proof submitted for a fresh mathematical referee;
no independent acceptance is asserted. This is a subsidiary theorem, and the
full original Conjecture 5.4 remains unresolved here.

## Statement

For every integer r >= 2 and all positive integers a, c, b, the polynomial
\[
P(q)=[a]_q[c]_q[b]_{q^r}
\]
is weakly unimodal, with every integer-indexed coefficient included, if and
only if
\[
r\mid a\quad\hbox{or}\quad r\mid c\quad\hbox{or}\quad
b\le 1+\lfloor a/r\rfloor+\lfloor c/r\rfloor. \tag{T}
\]
Here [a]_q = sum_{i=0}^{a-1} q^i. All factor-1 cases are included.

This proves precisely the k=2 restriction of the original statement. The
nearest source result is Proposition 4.5, which establishes r=2; its
interval-count method is the starting point below. The new step is a uniform
midpoint/floor estimate, with no restriction on r or the quotients. The
negative-difference witness was already derived in this project's triage and
is included here with its proof. No separate contribution is claimed for
that witness or for the known divisibility branch.

## Elementary facts and the divisibility branch

The product [u]_q[v]_q has symmetric trapezoidal coefficients, by counting
pairs (i,j) with i+j=n, 0 <= i < u, 0 <= j < v. Products of symmetric,
nonnegative, unimodal polynomials have the same properties. For completeness,
a symmetric unimodal polynomial F of degree E has the decomposition
\[
F(q)=\sum_{j=0}^{\lfloor E/2\rfloor}(f_j-f_{j-1})q^j[E-2j+1]_q,
\qquad f_{-1}=0.
\]
The coefficients in this sum are nonnegative. Expanding two such
decompositions expresses their product as a nonnegative sum of shifted
trapezoids, all symmetric about the same midpoint; hence the sum is
unimodal. The decomposition itself follows by telescoping the coefficients
up to the midpoint and using symmetry afterwards.

If a=rA with A >= 1, then
\[
[a]_q[b]_{q^r}=[r]_q\bigl([A]_x[b]_x\bigr)\big|_{x=q^r}.
\]
Its coefficient sequence repeats every coefficient of the symmetric
trapezoid [A]_x[b]_x exactly r times, so it is symmetric and unimodal.
Multiplication by [c]_q preserves these properties. The case r | c is the
same. This also supplies a self-contained proof of the known source branch
(Lemma 4.2 and Corollary 4.3).

## First differences

Assume a <= c, as permitted by commutativity, and write P=sum p_n q^n, with
p_n=0 outside [0,D], where D=a+c-2+r(b-1). Every factor is symmetric, so
unimodality is equivalent to p_n-p_{n-1} >= 0 for 1 <= n <= floor(D/2).

Put
\[
N(L,U)=\#\{j\in\mathbb Z:0\le j\le b-1,\ L\le rj\le U\}.
\]
The identity (1-q)[a]_q[c]_q=[a]_q-q^c[a]_q gives
\[
\Delta_n:=p_n-p_{n-1}
=N(n-a+1,n)-N(n-a-c+1,n-c). \tag{1}
\]
In particular Delta_n >= 0 for n < c, because the second count is zero.

## Sufficiency when neither factor is divisible by r

Write
\[
a=rA+s,\quad c=rC+t,\quad
A,C\ge0,\quad 1\le s,t\le r-1,\quad M=A+C,\quad B=b-1.
\]
Assume B <= M. Then D=r(M+B)+s+t-2. It remains to consider
c <= n <= floor(D/2). If this interval is nonempty then B >= 1: for B=0,
D/2=(a+c-2)/2 <= c-1.

The following endpoint bounds justify every clipping in (1):
\[
n\le a+c-2,
\qquad
0\le n-c\le\frac{a-c-2+rB}{2}\le\frac{rB-2}{2}<rB.
\]
The first follows from D <= 2(a+c-2), using B <= M and s+t >= 2.
Also n-a >= 0. Consequently the negative count starts at j=0 and is not
upper-clipped; the positive count has its lower endpoint above j=0. Thus
\[
\Delta_n=
\max\{0,\min(B,\lfloor n/r\rfloor)-\lfloor(n-a)/r\rfloor\}
-\bigl(\lfloor(n-c)/r\rfloor+1\bigr). \tag{2}
\]
It is enough to prove, with
\[
F=\lfloor(n-a)/r\rfloor+\lfloor(n-c)/r\rfloor+1,
\qquad h=\lfloor n/r\rfloor,
\]
that F <= B and F <= h. These are exactly the two bounds required by
inequality (2) of `triage-interval-reduction.md`.

For the first bound, floor subadditivity and 2n <= D give
\[
F\le\left\lfloor\frac{2n-a-c}{r}\right\rfloor+1
\le\left\lfloor\frac{rB-2}{r}\right\rfloor+1=B. \tag{3}
\]
The last equality holds for every integer r >= 2.

For the second, write n=rh+v, 0 <= v < r, and set
\[
e=\mathbf1_{v<s}+\mathbf1_{v<t}.
\]
Then
\[
F=2h-M+1-e. \tag{4}
\]
The midpoint bound implies
\[
n\le D/2\le rM+(s+t-2)/2<r(M+1),
\]
so h <= M. If h <= M-1, (4) immediately gives F <= h.
If h=M, the same midpoint bound gives 2v <= s+t-2, hence
v < max(s,t) and e >= 1; (4) again gives F <= h.
This exhausts the quotient and residue possibilities, including s=t.

Combining (3) and (4) yields F <= min(B,h). Since
floor((n-c)/r)+1 >= 1 in the interval under consideration, the expression
inside the maximum in (2) is positive and is at least the subtracted
negative count. Thus Delta_n >= 0. Symmetry proves sufficiency.

## Necessity and an exact negative witness

Retain the nondivisible residue notation, and assume B >= M+1, i.e.,
b >= M+2. Let u=max(s,t) and n_*=rM+u.

In the positive count in (1), the lower endpoint is
rC+u-s+1, strictly between rC and r(C+1), while the upper endpoint is
rM+u. The permitted j are C+1,...,M, exactly A choices (zero if A=0).
No upper clipping occurs because B >= M+1.

In the negative count, the lower endpoint is
u-s-t+1=1-min(s,t) <= 0, and the upper endpoint is rA+u-t, with
0 <= u-t < r. Thus the permitted j are 0,...,A, exactly A+1 choices.
There is again no upper clipping. Therefore
\[
p_{n_*}-p_{n_*-1}=-1. \tag{5}
\]
Moreover n_* >= 1 and
\[
D-2n_*=r(B-M)-|s-t|-2
\ge r-(r-2)-2=0.
\]
So this drop occurs within the first half of a symmetric polynomial and
rules out unimodality. Together with sufficiency and the divisibility
branch, this proves (T).

## Dependencies, scope, and review status

The argument above is self-contained: finite polynomial identities,
symmetry, elementary interval counts, floor subadditivity, and the proved
closure fact are its only mathematical dependencies. It does not assume
the source conjecture or infer any infinite statement from experiments.
Known boundary results and the candidate's precise delta are checked in
`literature/research-k2-comparison.md` against the retained primary source.

Known proof gaps: none identified by the proposer. A fresh referee has not
yet checked the argument or its contribution. In particular, this dossier
does not assert that the all-k sufficient direction or the remaining
necessary-direction ranges are settled, and does not prove priority.

Computational/AI assistance: this proof was developed and checked in one
model context, building on the saved triage reduction. The separate exact
integer verifier is a reproducible consistency test, not an independent
model review, a formal proof assistant certificate, or a universal proof.
