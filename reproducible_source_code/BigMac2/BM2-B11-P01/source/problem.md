# Precise reading: minimum dimension at restart length four

## Frozen input and provenance

The immutable statement is `source.md` (SHA-256
`5fcdf705252e8804eb53fdd3c5e490cbf2ddb4af6e976c28d00544df0a32de26`).
This file fixes its mathematical reading; it does not alter or silently weaken that
statement.  Triage job: `bigMac-00011-p01-triage-4a8182e33527`.

## Exact restarted-CG convention

Let \(n\geq 1\), let
\[
  A=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),\qquad \lambda_i>0,
\]
and choose \(x_0,b\in\mathbb R^n\) with nonzero initial residual
\(r_0=b-Ax_0\).  (Equivalently, one may prescribe any \(r_0\ne0\), take
\(x_0=0\), and set \(b=r_0\).)  Put \(x_*=A^{-1}b\).  For each restart-block
index \(k\geq0\), define
\[
 K_4(A,r_k)=\operatorname{span}\{r_k,Ar_k,A^2r_k,A^3r_k\},
\]
and let \(x_{k+1}\) be the unique minimizer of
\(\lVert x_*-z\rVert_A\) over \(z\in x_k+K_4(A,r_k)\), where
\(\lVert v\rVert_A^2=v^TAv\).  Then \(r_{k+1}=b-Ax_{k+1}\).

Thus **\(k\) counts completed four-step restart blocks**, not individual inner
CG steps.  Equivalently,
\[
 r_{k+1}=p_k(A)r_k,
 \quad p_k(t)=1+\sum_{\ell=1}^4c_{k,\ell}t^\ell,
 \quad r_{k+1}\perp K_4(A,r_k).
\]
For distinct active eigenvalues and normalized squared coordinates
\(w_{k,i}=r_{k,i}^2/\lVert r_k\rVert_2^2\), the Galerkin equations are
\[
  \sum_i w_{k,i}p_k(\lambda_i)\lambda_i^j=0
  \quad (j=0,1,2,3).
\]
All arithmetic and all convergence assertions are over the real numbers in exact
arithmetic.  Residual normalization and convergence use the Euclidean norm.

## Fully quantified target

For an instance as above, write \(y_k=r_k/\lVert r_k\rVert_2\) whenever
\(r_k\ne0\).  Define
\[
\begin{split}
 n_{\min}(4)=\min\{n\in\mathbb N:\;&\exists\lambda_1,\ldots,\lambda_n>0,
 \ \exists r_0\in\mathbb R^n\setminus\{0\}\text{ such that}\\
 & (\forall k\ge0,\ r_k\ne0)\ \land\
 \neg(\exists y\in S^{n-1},\ \lim_{j\to\infty}y_{2j}=y)\}.
\end{split}
\]
The minimum exists because the cited construction supplies an admissible
eight-dimensional instance.  “Never terminates” means \(r_k\ne0\) at every
restart point (equivalently, no inner block reaches the exact solution).
“The normalized even residual directions do not converge” means vector
nonconvergence of \((y_{2j})_{j\ge0}\), including signs—not merely
nonconvergence of squared spectral weights.

The active grade is the number of distinct eigenvalues whose eigenspace has a
nonzero component of \(r_0\), equivalently
\(\dim\operatorname{span}\{r_0,Ar_0,A^2r_0,\ldots\}\).  Restriction to this
cyclic subspace preserves termination and directional convergence.  Hence a
minimum-dimensional counterexample may, without loss, have distinct diagonal
entries and every coordinate of \(r_0\) nonzero; repeated eigenvalues and zero
coordinates remain included in the original quantifiers.

## Boundary and acceptable resolution scope

If the active grade is at most four, interpolation of \(1/t\) on the active
spectrum shows \(A^{-1}r_0\in K_4(A,r_0)\), so the first block terminates.
The primary paper gives an exact nonterminating, parity-nonconvergent construction
with eight active nodes.  The source therefore starts from
\(5\le n_{\min}(4)\le8\).  The elementary grade-five calculation recorded in
`checkpoint.md` sharpens the live range to
\[
  6\le n_{\min}(4)\le8.
\]

A complete answer must do one of the following:

1. give an exact counterexample first occurring in dimension six or seven and
   exactly exclude every lower undecided dimension; or
2. exactly exclude dimensions six and seven and combine this with the cited
   eight-dimensional construction.

For a smaller counterexample, a certificate must exactly specify the spectrum and
initial residual (explicitly or by unique isolating conditions), prove every
iterate is nonzero, and prove that the even normalized directions do not converge.
For an exclusion, the argument must cover all positive spectra and residuals,
including repeated eigenvalues, inactive coordinates, factor collisions, and
other boundary cases.  Floating-point plots or any finite orbit prefix are only
discovery evidence.

## Nearest primary result and source status

Colbrook, Stepaniants, and Townsend, *A Complete Resolution of Forsythe's
Conjecture for Restarted Conjugate Gradients*, arXiv:2609.04659v1 (submitted
2026-09-04), Theorem 1.1(ii), Theorem C.1.1, and Proposition C.1.2 prove the
eight-dimensional upper bound for \(s=4\).  Sections C.2--C.9 reconstruct the
diagonal SPD instance; Appendix C describes the exact rational/Sturm and interval
certificate.  The “Consequences and further questions” section explicitly asks
for the smallest counterexample dimension.  Primary record (retrieved
2026-09-07): <https://arxiv.org/abs/2609.04659>.  The inspected v1 PDF has
SHA-256 `a8eddb4d369949f3410bc711f657c06725fcbd4e6d8b20ff93a8ddced99244ee`.

The locator “Appendix B.4” in `source.md` is not the counterexample certificate
in v1: Section B.4 concerns the restart-three positive result.  The relevant
locator is **Appendix C**, together with Part C.  This bibliographic correction
does not change the frozen mathematical question.

As of the focused search on 2026-09-07, the minimum-dimension question is
`open-supported` by that primary paper.  No distinct primary source resolving
dimensions five through seven was found in the exact-phrase/equivalent-language
screen; this limited negative search is not a priority or novelty proof.
