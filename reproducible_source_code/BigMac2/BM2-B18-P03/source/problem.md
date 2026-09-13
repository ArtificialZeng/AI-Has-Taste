# Precise reading of the problem

## Frozen source and provenance

The original Chinese statement is frozen verbatim in `source.md` (SHA-256
`65c11a0f7088c13b0ff6a2702bde0bc8b6b2c3c5b4626a06f291d5cedda3b646`).
This file only fixes its mathematical reading; it does not amend the source.

The cited local primary-source PDF was inspected on 2026-09-08 at
`../../batches/literature/bigMac-18/2609.01970v1.pdf`; its SHA-256 is
`9c6ac07445adeea52400085a68a9432f400552d31f1d56e162986add2ed73b68`,
matching `source.md`.

## Objects and quantifiers

Let \(H=L^2([-1,1],dp)\), over either the real or complex scalars, with Lebesgue
measure and its usual inner product. For every real \(u>0\), define

\[
 (S_u f)(p)=\int_{-1}^{1}
 \frac{e^{-(p-q)^2/(4u)}}{2\sqrt{\pi u}}f(q)\,dq,
 \qquad -1\le p\le 1.
\]

The continuous symmetric Gaussian kernel makes \(S_u\) Hilbert--Schmidt,
compact, and self-adjoint. It is also positive semidefinite and positivity
improving. Thus its largest algebraic eigenvalue

\[
 \lambda(u)=\max_{\|f\|_2=1}\langle f,S_u f\rangle
\]

is positive and simple. Set the *scalar* endpoint values \(\lambda(0)=1\) and
\(\Phi(0)=0\), and set \(\Phi(u)=\log\lambda(u)\) for \(u>0\). No compact
operator \(S_0\) is asserted: the endpoint is a continuous scalar extension.
For each \(u>0\), simplicity and standard compact-operator perturbation imply
that \(\lambda\) and \(\Phi\) are smooth locally in \(u\).

The cited paper proves (Eq. (59), with the direct argument in Appendix A.5,
especially Eq. (A53))

\[
 \lambda(u)=1-au+o(u),\qquad
 \Phi(u)=-au+o(u),\qquad a:=\frac{\pi^2}{4},
 \quad u\downarrow0.
\]

Consequently the already-established first right derivative is
\(\Phi'(0+)=-a\).

## Exact decision problem

The primary, classical reading of “finite right second derivative” is whether
there is an \(L\in\mathbb R\) such that

\[
 \Phi''(0+):=\lim_{u\downarrow0}
 \frac{\Phi'(u)-\Phi'(0+)}{u}
 =\lim_{u\downarrow0}\frac{\Phi'(u)+a}{u}=L.                 \tag{Q}
\]

Because endpoint terminology is not completely uniform, the associated
second Peano/Taylor quotient must also be tracked:

\[
 D^2_P\Phi(0+):=
 \lim_{u\downarrow0}\frac{2\,[\Phi(u)+au]}{u^2}.            \tag{P}
\]

Existence of the finite classical limit (Q) implies existence of (P) with the
same value (integrate the derivative estimate). The converse is not automatic.
Therefore:

- an affirmative resolution must prove (Q), not merely fit or prove a
  quadratic value expansion;
- failure or divergence of (P) already disproves a finite (Q);
- if only (P) is settled while (Q) is not, their statuses must be reported
  separately.

Write the first-order remainder as

\[
 R(u):=\Phi(u)+au.
\]

If (Q) has no finite value, the requested fallback is a rigorous all-small-
\(u\) lower bound on a nonquadratic scale for \(R(u)\), together with a
matching argument that identifies the correct power (and any logarithmic
factor). Any such lower bound must state whether it is signed or concerns
\(\lvert R(u)\rvert\). For example, a pure-power conclusion of order
\(\alpha\) requires constants \(u_0,c,C>0\), independent of \(u\), such that

\[
 c u^\alpha\le |R(u)|\le C u^\alpha\qquad(0<u<u_0),
\]

or an equally rigorous signed statement. A lower bound alone can obstruct an
\(O(u^2)\) remainder, but it does not determine the *correct* power without a
matching upper bound (or a sharper asymptotic). If an exact first nonanalytic
term is claimed, it must have a uniform remainder statement such as

\[
 R(u)=c u^\alpha+E(u),\qquad |E(u)|\le C\rho(u)
 \quad(0<u<u_0),\qquad \rho(u)=o(u^\alpha),
\]

with any preceding analytic terms and logarithmic factors written explicitly.
A floating-point fit or a finite list of numerical values is not such a bound.

## Scope and prior-result boundary

The question concerns the continuum principal eigenvalue above as
\(u\downarrow0\). It is not a claim about a fixed finite-dimensional truncation,
nor does it identify endpoint derivatives with separately optimized cumulants.
Equation (69) of the cited paper makes its higher-derivative interpretation
conditional, and the paragraph following it leaves higher-order analysis to
future work. Those statements support only the nearest-prior-result boundary:
the cited paper establishes the linear term but not the second-order endpoint
regularity. They do **not** by themselves establish that the question is open
in the full literature. Until a dedicated primary-literature search is done,
the source status is `status-uncertain`.

The proposed delta is to decide (Q), and in the negative case to certify the
first nonquadratic scale of \(R\). A cheap discriminating route is to evaluate
the Rayleigh quotient of the normalized Dirichlet ground state
\(f_1(p)=\cos(\pi p/2)\) using Appendix A.5's Fourier representation. Its
zero extension has an explicit algebraic Fourier tail, so an exact,
uniform small-\(u\) expansion can test whether a \(u^{3/2}\) correction already
forces the Peano quotient (P) to diverge. This is a proposed next test, not a
result recorded at triage.
