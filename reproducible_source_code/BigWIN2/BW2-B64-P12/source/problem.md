# Precise problem statement

## Frozen source and object under audit

The immutable lead is `source.md` (local SHA-256
`a8a2bea37103f33d1c0cc6892ce1f7b6b07587e0f628a550727c99f0e1933534`).
The cited primary source is Alicia Cordero and Juan R. Torregrosa,
“Improving the efficiency of a Hyperpower method for approximating inverse
matrices,” arXiv:2609.04433v1 (submitted 3 September 2026), Section 2,
PDF Theorem 2.1 and equations (2.1)–(2.7) (HTML Theorem 1 and equations
(4)–(11)). The arXiv abstract and v1 HTML were
inspected on 2026-09-07 at
<https://arxiv.org/abs/2609.04433> and
<https://arxiv.org/html/2609.04433v1>. During the research pass the local
primary PDF identified in `source.md` was located, copied to
`evidence/external/2609.04433.pdf`, and independently verified to have SHA-256
`0b2d8edbed7c6b69ef0f9edd7e106e919c7a2f5976f845e16b3758528a32fe2c`.

## Definitions and quantifiers

Let \(n\geq 1\), let \(A\in\mathbb C^{n\times n}\) be nonsingular, and let
\(X_k\in\mathbb C^{n\times n}\). For a submultiplicative matrix norm define

\[
R_k=I-AX_k,\qquad
Y_k=X_k(2I-AX_k),\qquad R_k^Y=I-AY_k=R_k^2,
\]

and, whenever \(R_k\ne0\),

\[
\nu_k=\frac{\|R_k^Y\|^2}{\|R_k\|^2}
     =\frac{\|R_k^2\|^2}{\|R_k\|^2},\qquad
X_{k+1}=Y_k\big((2+\nu_k)I-(1+\nu_k)AY_k\big).
\]

At \(R_k=0\) the algorithm has already found \(A^{-1}\), so it terminates;
the displayed quotient itself is undefined there. Direct algebra, without a
change of residual convention, gives the exact residual update

\[
R_{k+1}=-\nu_kR_k^2+(1+\nu_k)R_k^4. \tag{*}
\]

The source theorem quantifies over every nonsingular complex matrix and an
initial estimate satisfying \(\|I-AX_0\|\leq\sigma<1\), and asserts
convergence to \(A^{-1}\) with order six. Its proof later imposes the stronger
\(\sigma<3^{-1/3}\), an additional scope discrepancy to keep separate from
the order claim.

For this audit, “local order six” means at least the standard uniform local
estimate \(\|R_{+}\|\le C\|R\|^6\) for all sufficiently small residuals (and
the equivalent error formulation for fixed nonsingular \(A\)). “Actual
asymptotic order \(p\)” on a specified orbit means Q-order:
\(0<\lim_{k\to\infty}\|R_{k+1}\|/\|R_k\|^p<\infty\), if that limit exists.
Any alternative order notion used in a final claim must be stated explicitly.

## Exact discriminating test

Take \(A=I_3\), the Frobenius norm,
\(D=\operatorname{diag}(1,2,3)\), \(R=tD\), and \(X=I-R\), with
\(0<|t|<1/\sqrt{14}\). Then

\[
\nu=\frac{t^4(1+16+81)}{t^2(1+4+9)}=7t^2,
\]

and substitution in (*) yields exactly

\[
R_+=t^4\operatorname{diag}(-6,-12,18)
     +7t^6\operatorname{diag}(1,16,81).
\]

Consequently \(\|R_+\|_F/\|R\|_F^6\to\infty\) as \(t\to0\), since the
quartic coefficient is nonzero. Thus the asserted uniform general-matrix
sixth-order estimate fails under the paper's own update and residual
convention. This one-step fact alone does not establish the Q-order of the
entire orbit.

## Research target and scope

Source status: **new-question** (audit of a four-day-old v1 preprint). Searches
on 2026-09-07 for the exact title, the phrase “scalar norm-type accelerators,”
and norm-accelerated matrix-inverse iterations found the cited v1 but no
primary correction or prior audit. This is a limited search, not a priority
claim.

Nearest prior result: the standard order-four Hyperpower residual map is
\(R_+=R^4\); arXiv:2609.04433v1 proposes the scalar norm correction and claims
order six. Proposed delta: prove an exact counterexample to that general order
claim, prove that the diagonal orbit from \(t(1,2,3)\) has a definite actual
asymptotic order on an explicit nonzero interval, and isolate the invalid
quantifier step in the source proof. Verification route: use the exact
three-coordinate recurrence

\[
\nu(r)=\frac{\sum_i r_i^4}{\sum_i r_i^2},\qquad
r_i^+=-\nu(r)r_i^2+(1+\nu(r))r_i^4,
\]

then establish a rational cone/interval invariant and matching upper and lower
quartic bounds. The final scope, if proved, is a refutation of the stated
general theorem plus an analysis of this explicit diagonal family, not a claim
about every CTM orbit.
