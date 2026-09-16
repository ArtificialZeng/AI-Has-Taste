# Precise reading and triage record

## Mathematical statement

For each fixed integer
\[
p\in\{1,2,3,4,5\},\qquad \gamma_D:=5p(p+1),
\]
let \(\mathbb P_p\) be the real univariate polynomials of degree at most
\(p\).  For \(0<\kappa<1\), \(\gamma>0\), and
\((u,q)\in\mathbb P_p\times\mathbb P_p\), interpret the two-cell form in
the frozen question as the dimensionless one-dimensional reduction (60) of
Appendix B of arXiv:2609.04067v1:
\[
\begin{aligned}
a^{(2)}_{\kappa,\gamma}(u,q)
={}&\int_{-1}^{0}(u'(x))^2\,dx
 +\int_{0}^{\kappa}(q'(x))^2\,dx
 -2q'(\kappa)q(\kappa)+\gamma_Dq(\kappa)^2\\
&+\gamma\sum_{k=1}^{p}
 \frac{(q^{(k)}(0)-u^{(k)}(0))^2}{(k!)^2}.
\end{aligned}
\]
Here \(u\) is the polynomial on the uncut neighbour \((-1,0)\), \(q\) is
the polynomial on the cut cell \((0,1)\), and the physical part of the cut
cell is \((0,\kappa)\).  The common trace condition at the ghost face causes
no additional restriction in this reduction: the form is unchanged on
shifting the otherwise unused constant coefficient of \(u\), so every pair
can be represented with \(u(0)=q(0)\).  Appendix B proves that positive
semidefiniteness of the full tensor-product two-cell form is equivalent to
positive semidefiniteness of this form on all of
\(\mathbb P_p\times\mathbb P_p\).

Define, with the paper's convention \(\inf\varnothing=+\infty\),
\[
\tau_p(\kappa):=
\inf\{\gamma>0:\ a^{(2)}_{\kappa,\gamma}(u,q)\geq0
\text{ for every }(u,q)\in\mathbb P_p^2\}.
\]
The requested number is
\[
\Gamma_p:=\sup_{0<\kappa<1}\tau_p(\kappa).
\]
For every one of the five values of \(p\), determine \(\Gamma_p\) exactly
and give the complete maximizer information: every interior
\(\kappa\in(0,1)\) with \(\tau_p(\kappa)=\Gamma_p\), and either endpoint
\(\kappa=0,1\) for which the corresponding one-sided limit realizes the
supremum.  A numerical plot or floating-point eigenvalue list does not answer
the problem.  The answer must be rational or algebraic and accompanied by an
exact certificate, for example rational matrix reduction plus resultants and
Sturm sign counts.

In monomial coordinates, the unused coefficient \(u_0\) may be factored out.
On
\[
z=(u_1,\ldots,u_p,q_0,\ldots,q_p),
\]
the form has a symmetric matrix
\(H_p(\kappa,\gamma)=A_p(\kappa)+\gamma G_p\) with entries in
\(\mathbb Q[\kappa,\gamma]\); at the ghost face the final sum is simply
\(\gamma\sum_{k=1}^p(q_k-u_k)^2\).  This is the finite exact object to be
certified.  PSD must include all null directions; a determinant root alone is
not a PSD certificate.

## Boundary cases and known lower bound

The domain in the supremum is open, so an endpoint can realize the supremum
only as a one-sided limiting maximizer.  Proposition 5 proves that at
\(\kappa=0\)
\[
\min\{\gamma>0:a^{(2)}_{0,\gamma}\succeq0\}
=\frac1{\gamma_D-p^2}
=\frac1{p(4p+5)}.
\]
It also proves
\(\Gamma_p\geq1/[p(4p+5)]\).  The five lower-bound values are
\(1/9,1/26,1/51,1/84,1/125\).  The unresolved issue is the matching global
upper bound, or an exact interior counterexample to it.

## Source status and nearest literature (checked 2026-09-07)

Status: **open-supported for this precise finite-dimensional question**.
The primary paper was submitted on 2026-09-03.  Proposition 5 and the final
paragraph of Appendix B explicitly say that equality of the cut-uniform
threshold with \(1/(\gamma_D-p^2)\) remains unproved; Table 6 reports only
sampled generalized-eigenvalue support.  The local PDF hash agrees with the
frozen locator:
`cbe004fd2b861aa6342b9b2d8d2ba065319ae039be5cb2cda4721780e534fac3`.

- Primary source: <https://arxiv.org/abs/2609.04067v1>, especially
  Proposition 4, Table 6, equation (60), Proposition 5, and the final
  paragraph of Appendix B (PDF pp. 30--39; relevant exact reduction and open
  statement on pp. 37--39).
- Exact-assertion and equivalent-language searches found no separate source
  settling this newly posed \(p\leq5\) classification.  This is a limited
  screen, not a priority proof.
- The nearest general stabilization result inspected was Burman--Hansbo--Larson,
  *On the design of locking free ghost penalty stabilization and the relation
  to CutFEM with discrete extension*, Numerische Mathematik 158 (2026),
  <https://doi.org/10.1007/s00211-025-01502-6>.  It gives parameter-scale
  coercivity results (including ghost weight proportional to inverse Nitsche
  weight) but not this exact aligned two-cell threshold or its maximizers.

## Triage target

Nearest prior result: the exact vanishing-cut threshold and global lower bound
above.  Proposed delta: certify \(\Gamma_p\) and all maximizers for each
\(p=1,\ldots,5\).  Verification route: construct \(H_p\) over
\(\mathbb Q[\kappa,\gamma]\), eliminate harmless/null directions, determine
the exact threshold branches, isolate every branch intersection and stationary
point in \([0,1]\) using resultants and Sturm sequences, and certify PSD on
every resulting interval with exact signs or an exact congruence/Schur
complement.
