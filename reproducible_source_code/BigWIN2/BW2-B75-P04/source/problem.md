# Precise reading and triage target

## Frozen source

The immutable problem statement is `source.md` (SHA-256
`3ee9ccc12ddcd0cbb40f14d0a3444709b13b398ca02d9176d49d28788c4bc99e`).
The primary source is D. Li, S. Li, W. Pan, H. Wulan, and M. Zhou,
*Norm of the generalized Hilbert operator on weighted Bergman spaces*,
arXiv:2609.04833v1 (submitted 2026-09-04), Theorem 3.4 and (3.38),
(3.41)--(3.42), <https://arxiv.org/abs/2609.04833>.  The source was
retrieved and checked on 2026-09-09.

## Definitions and domain

Fix

\[
 \alpha\geq0,\qquad A=\alpha+2\;(\geq2),\qquad
 C_\alpha=B\!\left(1+\alpha,2+\frac\alpha2\right),
\]

where
\(B(x,y)=\int_0^1t^{x-1}(1-t)^{y-1}\,dt
=\Gamma(x)\Gamma(y)/\Gamma(x+y)\) for \(x,y>0\).  For \(p>A\), set
\(h=p-A>0\) and

\[
G_{\alpha,b}(p)=
 \frac{p(b+1)-A}{p-A}
 \frac{2[1-(A/p)^2]}{A/p+2(p-A)}.
\]

The parameter condition used by Theorem 3.4 is
\(0\leq b<A/p\).  Thus a right-hand limit with fixed \(b\) stays in
that domain precisely when \(0\leq b<1\) (and then it does so for all
sufficiently small \(h>0\)).  The nearby sufficient condition in
Corollary 3.5 additionally has \(p<p_\alpha\), where

\[
p_\alpha=\frac{3\alpha}{4}+2+
\frac14\sqrt{9\alpha^2+40\alpha+48} > A+\frac12.
\]

## Quantified endpoint claims

The unambiguous endpoint assertion is read as

\[
\forall\alpha\geq0\;\forall b\in[0,1):\quad
\lim_{\substack{p\downarrow A\\ b<A/p}}G_{\alpha,b}(p)=4b.
\tag{E}
\]

Its requested local consequence is

\[
\begin{split}
\forall\alpha\geq0\;\forall b\in(C_\alpha/4,1)\;\exists\varepsilon>0
\;\forall p:\quad &A<p<A+\varepsilon\\
&\Longrightarrow b<A/p\ \text{ and }\ G_{\alpha,b}(p)>C_\alpha.
\end{split}
\tag{N}
\]

We may, without loss, require \(\varepsilon\leq1/2\); then
\(p<p_\alpha\) and the point also lies in the small-\(p\) range used in
the proof of Theorem 3.4.

## The theorem-level quantifier under audit

Theorem 3.4 literally places \(p\) in the hypothesis before later saying
“for all” \(p\), so its displayed grammar is ill-scoped.  The natural
reading of “\(\beta_\alpha\) only depending on \(\alpha\)” is the uniform
statement

\[
\forall\alpha\geq0\;\exists\beta_\alpha\in(A,A+1/2]\;
\forall p\in(A,\beta_\alpha]\;\forall b\in[0,A/p):
\quad
\|\mathcal H_b\|_{A_\alpha^p\to A_\alpha^p}
=B\!\left(\frac Ap,b+1-\frac Ap\right).
\tag{T-uniform}
\]

A weaker possible repair would first fix \(b<1\) and permit a threshold
\(\beta_{\alpha,b}\).  That is a different statement and contradicts the
published phrase “only depending on \(\alpha\)”; it is therefore recorded
as a proposed correction, not silently substituted for the source.

## Nearest prior result, proposed delta, and scope

The nearest prior result is Corollary 3.5 of the same paper: for
\(A<p<p_\alpha\) and \(0\leq b<A/p\), the norm equality follows if the
left side \(L_{\alpha,b}(p)\) of (3.38) is at most \(C_\alpha\).  Theorem
3.4 explicitly says its proof relies on that corollary and bounds
\(L_{\alpha,b}(p)\) above by \(G_{\alpha,b}(p)\) in (3.41).

The proposed delta is a rigorous endpoint audit: prove (E) and (N),
quantify the resulting obstruction to (3.41), and determine the exact
endpoint behavior of (3.38).  The deterministic verifier is
`evidence/endpoint-audit.py`, with the analytic derivation and source
locators in `evidence/triage-endpoint-audit.md`.

This scope distinguishes three claims.  Failure of the estimate
\(G_{\alpha,b}(p)\leq C_\alpha\) is a failure of that proof route.  Failure
of the sufficient condition (3.38) still is not a failure of the norm
identity.  A counterexample to (T-uniform) would require an operator-level
witness or another necessary-condition argument; none is presently supplied.
