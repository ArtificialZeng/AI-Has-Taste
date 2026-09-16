# Precise problem interpretation

## Frozen claim

All spaces and operators are over the real scalar field. For each positive
integer \(n\), let \(\ell_\infty^n=(\mathbb R^n,\|\cdot\|_\infty)\). If
\(Y\) is a linear subspace of a normed space \(X\), a projection onto \(Y\)
is a linear map \(P:X\to Y\) with \(P^2=P\), and
\[
  \lambda(Y,X)=\inf\{\|P\|:P:X\to Y\text{ is a projection}\}.
\]
For a finite-dimensional real normed space \(Y\), set
\[
  \lambda(Y)=\sup\{\lambda(TY,X):X\text{ is a real normed space and }
  T:Y\to X\text{ is a linear isometry}\}.
\]
For positive integers \(n\ge r\), define
\[
  \lambda(r,n)=\sup_{\substack{Y\subseteq\ell_\infty^n\\\dim Y=r}}
  \lambda(Y,\ell_\infty^n),\qquad
  \lambda(r)=\sup_{\dim Y=r}\lambda(Y).
\]
The source establishes that these suprema are finite, that
\(\lambda(r,n)\) is nondecreasing in \(n\), and that
\(\lambda(r)=\sup_{n\ge r}\lambda(r,n)\).

The immutable assertion to prove or disprove is
\[
  (\forall r\in\mathbb Z_{\ge1})(\forall n\in\mathbb Z_{\ge r})
  \quad n\ge 2^{r-1}\binom{r+1}{2}
  \Longrightarrow \lambda(r,n)=\lambda(r).
\]
Here "real dimension" in `source.md` means integer dimension over the real
field; it does not quantify over nonintegral \(r\). The threshold is already
at least \(r\) for every \(r\ge1\).

## Equivalent optimization formulation and proof scope

For \(U\in\mathbb R^{n\times r}\), write \(x_i^T\) for its \(i\)-th row.
Theorem 2.1 of the primary source gives
\[
 \lambda(r,n)=\max\left\{
 \sigma(U,w):=\sum_{i,j=1}^n w_iw_j|\langle x_i,x_j\rangle|:
 U^TU=I_r,\ w\in\mathbb R_{\ge0}^n,\ \|w\|_2=1
 \right\}.
\]
Thus a proof of the frozen claim may show that every maximizing feasible pair
has an objective-equivalent representative with at most
\(2^{r-1}\binom{r+1}{2}\) nonzero rows, then use monotonicity and the displayed
supremum identity. It must also justify deletion of zero rows and, where
needed, padding to the stated ambient size. Counting sign cells without
preserving feasibility and the maximum is not sufficient.

A disproof must exhibit some admissible integers \(r,n\) at or above the
displayed threshold for which \(\lambda(r,n)<\lambda(r)\), with an exact
certificate or rigorous argument. Showing only that the threshold is not
minimal does not refute the claim.

## Source status and nearest result

The inspected primary source is Hitesh Kumar, Bojan Mohar, Seyed Ahmad
Mojallal, and Shivaramakrishna Pragada, *Stability of maximal relative
projection constants*, arXiv:2609.03200v1 (submitted 2026-09-02),
https://arxiv.org/abs/2609.03200, retrieved 2026-09-07. Equation (1.1) on PDF
p.2 gives the definitions above. Theorem 1.3 on pp.3--4 proves
\[
  \lambda(r,n)=\lambda(r)\quad\text{for all }
  n\ge 2^r\binom{r+1}{2}.
\]
Claim 2.4 (pp.7--8) is the cloning lemma, and Claim 2.5 (pp.9--10) partitions
the rows among all \(2^r\) coordinate orthants and applies conic
Caratheodory in the \(\binom{r+1}{2}\)-dimensional space of symmetric
\(r\times r\) matrices. The paper remarks only that minor improvements may be
possible; it does not state the frozen factor-two improvement.

A bounded search on 2026-09-07 for the exact threshold, equivalent stability
language, and maximal relative projection constants found the primary source
and older background papers, but no primary source stating this exact
factor-two bound. This is not proof of novelty or open status. The appropriate
source classification is **new-question, literature status uncertain**.

## Proposed delta and bounded verification route

Nearest prior result: the preceding \(2^r\binom{r+1}{2}\) theorem. Proposed
delta: halve the number of relevant orthants by independently replacing every
row \(x_i\) by \(-x_i\) when its first coordinate is negative. In matrix form,
with a diagonal sign matrix \(D\), this sends \(U\) to \(DU\), for which
\((DU)^T(DU)=U^TU\), while all absolute Gram entries and hence \(\sigma\)
are unchanged. With the paper's convention \(\operatorname{sgn}(0)=+1\), all
normalized rows lie in the \(2^{r-1}\) orthants having first sign \(+1\).

This is a plausible nontrivial target, not yet a proof. The decisive first
test is to turn the observation into a precise normalization lemma and replay
Claims 2.1--2.5 line by line, checking zero first coordinates, redefinition of
the signed graph, preservation under nonnegative cloning scalings, repeated
cloning, removal of zero rows, and the final monotonicity/supremum passage.

## Provenance

Triage job `win-00056-p01-triage-13821b47b83d`. The immutable source file had
SHA-256 `0b0f7e248a1c31a80ce40e673f7147cbae02d01773503528212de8cfd28dc660`
during this triage.
