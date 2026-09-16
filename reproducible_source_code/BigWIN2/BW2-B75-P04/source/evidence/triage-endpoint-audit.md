# Endpoint triage evidence

Provenance: `win-00075-p04-triage-5c524cdfc050`.  Retrieval and audit
date: 2026-09-09.

## Primary-source and literature check

The official arXiv v1 abstract page is
<https://arxiv.org/abs/2609.04833>, and the checked full text is
<https://arxiv.org/html/2609.04833> / <https://arxiv.org/pdf/2609.04833>.
The official record lists five authors, submission date 2026-09-04, and
only version v1 as of the audit date.

Exact full-text positions are:

- Corollary 3.5 and (3.38): HTML lines 969--977; PDF extraction
  `P27`, lines 4962--4997 (viewer page 28).
- Theorem 3.4 and its quantifier: HTML lines 1003--1009; PDF extraction
  `P28`, lines 5215--5237 (viewer page 29).
- Simplification (3.41) and estimate (3.42): HTML lines 1012--1026;
  PDF extraction `P29`, lines 5304--5344 (viewer page 30).
- Intermediate-value assertion and final appeal to Corollary 3.5: HTML
  lines 1028--1038; PDF extraction `P29`, lines 5345--5386.
- The definition of \(p_\alpha\): HTML lines 306--316.

Searches for the exact displayed factors, the paper identifier together
with “correction/erratum/comment,” and equivalent endpoint wording found
the v1 paper but no independent primary correction or treatment.  This
is only a dated negative search result, not a priority claim.  There were
no files matching `literature/*handoff*.md`; the separately named recovery
note was treated as a lead and checked against the live arXiv text above.

## Exact simplification and limit

Put \(A=\alpha+2\) and \(p=A+h\).  Direct cancellation gives

\[
G(h)=\frac{2(Ab+(b+1)h)(2A+h)}
{(A+h)(A+2Ah+2h^2)}.
\]

The denominator tends to \(A^2>0\), so
\(\lim_{h\downarrow0}G(h)=4b\).  More explicitly,

\[
G(h)-4b=
-\frac{2hQ(A,b,h)}{(A+h)(A+2Ah+2h^2)},
\]
where

\[
Q=4A^2b+8Abh-Ab-2A+4bh^2-bh-h.
\]

These identities and the limit were independently recomputed by running
`python3 evidence/endpoint-audit.py`; all exact symbolic assertions pass.

## Explicit punctured-neighborhood estimate

For \(0<h\leq1\) and \(A\geq2,b\geq0\), the denominator above is at
least \(A^2\), and

\[
|Q|\leq M(A,b):=4A^2b+9Ab+2A+5b+1.
\]

Hence

\[
|G(h)-4b|\leq K(A,b)h,
\qquad K(A,b):=\frac{2M(A,b)}{A^2}.
\tag{1}
\]

Let \(b\in(C_\alpha/4,1)\) and \(\Delta=4b-C_\alpha>0\).  One explicit
choice is

\[
\varepsilon=min\left\{
\frac12,\ \frac{A(1-b)}{2b},\ \frac{\Delta}{2K(A,b)}
\right\}>0.
\tag{2}
\]

For \(0<h<\varepsilon\), (2) gives \(b<A/(A+h)\), while (1) yields

\[
G(A+h)>4b-\Delta/2=C_\alpha+\Delta/2>C_\alpha.
\]

Thus both the requested limit and its quantified local consequence hold.
Notice also that \(C_\alpha\leq\int_0^1(1-t)\,dt=1/2\), since
\(t^\alpha(1-t)^{1+\alpha/2}\leq1-t\); consequently the admissible
interval \((C_\alpha/4,1)\) is nonempty for every \(\alpha\geq0\).

## Exact condition (3.38) and proof-gap scope

Writing the left side of (3.38) as \(L(h)\), one obtains

\[
L(h)=\frac{Ab+(b+1)h}{h^2}\left(1-e^{-\Phi(h)}\right),
\]

\[
\Phi(h)=\log\Gamma(x)+\log\Gamma(1+2h)-\log\Gamma(x+2h),
\qquad x=\frac{A}{A+h}.
\]

Taylor's formula at \((x,h)=(1,0)\), using
\(\psi_1(1)=\pi^2/6\), gives

\[
\Phi(h)=\frac{\pi^2}{3A}h^2+o(h^2),
\qquad
\lim_{h\downarrow0}L(h)=\frac{\pi^2b}{3}.
\tag{3}
\]

The exact SymPy calculation in `evidence/endpoint-audit.py` independently
checks both limits in (3).  Therefore:

- if \(b>3C_\alpha/\pi^2\), then (3.38) itself is false throughout some
  punctured right neighborhood of \(A\);
- if \(b<3C_\alpha/\pi^2\), then (3.38) is true throughout some such
  neighborhood;
- equality at the threshold requires a higher-order term.

This proves a gap in the published derivation of Theorem 3.4: its stated
uniform-in-\(b\) neighborhood cannot follow from Corollary 3.5, because
the corollary's sufficient hypothesis fails near the endpoint for an
admissible nonempty range of \(b\).  It also exposes why invoking
\(f_\alpha(A)=0\) is insufficient: the prefactor
\([p(b+1)-A]/(p-A)\) is singular and their product has limit \(4b\), not
zero.  Neither (1) nor (3) is an operator-norm counterexample, because
(3.38) is sufficient, not necessary.
