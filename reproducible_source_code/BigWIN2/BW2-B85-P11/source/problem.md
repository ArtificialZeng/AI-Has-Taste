# Precise problem reading

## Frozen target

The immutable statement is `source.md` (SHA-256
`c3d26bd50db550877a991b263ebec998946948438739646d7f9a07f5a3647350`).  At
the fixed parameter \(\lambda=5/2\), put
\[
\Omega:=\Omega_{5/2}=(-1,1)\cup(3/2,7/2)\cup(-7/2,-3/2).
\]
For a continuous function \(f:\mathbb R\to\mathbb C\), positive definite means
that for every \(m\geq1\), every \(x_1,\ldots,x_m\in\mathbb R\), and every
\(z_1,\ldots,z_m\in\mathbb C\),
\[
  \sum_{j,k=1}^m z_j\overline{z_k}\,f(x_j-x_k)\geq0.
\]
Here \(\operatorname{supp}f\) is the closed support.  Define
\[
T_{\mathbb R}(\Omega)=\sup\left\{\int_{\mathbb R}f(x)\,dx:
 f\in C(\mathbb R),\ f\text{ positive definite},\ f(0)=1,
 \operatorname{supp}f\subset\Omega\right\}.
\]
The primary task is to determine this number exactly.  Classification of all
extremizers is explicitly secondary and is not part of the success condition
for the exact-value task.

## Equivalent finite optimization

Let
\[
A=\{-6,-5,-4,-1,0,1,4,5,6\}.
\]
For \(c=(c_1,c_4,c_5,c_6)\in\mathbb R^4\), set
\[
p_c(t)=1+2c_1\cos t+2c_4\cos4t+2c_5\cos5t+2c_6\cos6t.
\]
The precise finite problem is
\[
M=\max\left\{1+2(c_1+c_4+c_5+c_6):
 p_c(t)\geq0\quad\text{for every }t\in\mathbb R\right\},
\qquad T_{\mathbb R}(\Omega)=\frac M2.
\]
Equivalently, with \(x=\cos t\) and \(T_k\) the Chebyshev polynomial,
\(1+2c_1T_1(x)+2c_4T_4(x)+2c_5T_5(x)+2c_6T_6(x)\geq0\) for every
\(x\in[-1,1]\).  The word “maximum” is justified: nonnegative normalized
trigonometric polynomials have bounded Fourier coefficients, and the feasible
set is closed.  There are no unstated sign restrictions on the four
coefficients.

## Prior result and scope

Fu--Li--Wang--Wang, arXiv:2608.15643v1, Theorem 1.2, applied to \((p,q)=(5,2)\),
gives the finite equivalence above.  Proposition 4.2 and Lemma 5.1 give only
\[
\frac{559+80\sqrt{42}}{506}\leq T_{\mathbb R}(\Omega)\leq\frac94.
\]
Thus neither a floating optimum nor a one-sided certificate answers the frozen
target.  An exact answer requires a feasible exact nonnegative polynomial and
a matching exact dual/moment upper certificate.  A strict exact improvement of
one published endpoint is a possible subsidiary result, but must be labelled
as leaving the primary exact-value question unresolved.

Literature status as of 2026-09-11 is **status-uncertain**: the cited paper is
the nearest verified primary result and does not state the fixed exact-value
question as a formal open problem; targeted searches found no later primary
resolution, which is not proof of openness or priority.  Search details are in
`evidence/triage.md`.

## Research-pass resolution candidate

The exact primal--dual certificate in `evidence/exact_solution.md` proposes the
full-scope value
\[
 T_{\mathbb R}(\Omega)=
 \frac{(2u+1)^2(4u^2-6u+1)^2}{128u^6-20u^2+5},
\]
where \(u\) is the unique root in \([533/1000,267/500]\) of
\[
 256u^7+256u^6-96u^5-80u^4+40u^3+30u^2-15u-5=0.
\]
This is \(2.1353071788763974322\ldots\).  The lower certificate is a normalized
square of a cubic; the matching upper certificate is an exact positive
three-atomic moment functional supported at that cubic's three roots.  All
symbolic identities and rational sign enclosures are reproduced by
`evidence/verify_exact_solution.py`.  This is a researcher-submitted candidate,
not yet an independent mathematical acceptance, and it makes no extremizer
classification or priority claim.
