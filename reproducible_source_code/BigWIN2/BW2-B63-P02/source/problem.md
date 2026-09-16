# Precise problem statement

## Frozen family and notation

For each integer `r >= 2`, set

\[
n=4r+2,\qquad k=2r,\qquad s=r.
\]

The generalized Johnson graph `J(4r+2,2r,r)` is the finite simple graph with
vertex set \(\binom{[4r+2]}{2r}\). Distinct vertices \(A,B\) are adjacent
exactly when \(|A\cap B|=r\). Equivalently this is the distance-\(r\)
relation of the Johnson scheme on the \(2r\)-subsets.

Use the binomial convention \(\binom ab=0\) when \(b<0\) or \(b>a\). For
each index \(j\in\{0,1,\ldots,2r\}\), define the integer

\[
E_r(j)=\sum_{\ell=0}^{r}(-1)^\ell
 \binom{j}{\ell}\binom{2r-j}{r-\ell}
 \binom{2r+2-j}{r-\ell}.
\]

These are exactly the adjacency eigenvalues, with multiplicity
\(m_j=\binom{4r+2}{j}-\binom{4r+2}{j-1}\). Thus the set of minimizing
indices is

\[
I(r)=\{j\in\{0,\ldots,2r\}:E_r(j)=\min_{0\leq i\leq2r}E_r(i)\}.
\]

## Quantified target

Determine the least integer \(r_0\geq2\) such that

\[
\forall r\in\mathbb Z,\quad r\geq r_0\Longrightarrow 2\in I(r),
\]

and, for every integer \(r\) with \(2\leq r<r_0\), determine the full set
\(I(r)\). The requested proof must compare exact integers (or exact rational
normalizations) and cover every \(r\geq r_0\), not merely a computed range.
If an eigenvalue is repeated at different Johnson-scheme indices, all indices
attaining the minimum must be reported.

The constraint \(r_0\geq2\) makes explicit the source's natural domain; without
it, a literal search for a least threshold would quantify over undefined family
members below `r=2`.

## Nearest prior result and proposed delta

Luo--Cao--Li--Li, arXiv:2609.04677v1 (submitted 2026-09-04), equation (2.1)
gives the Eberlein formula above. Proposition 12 proves that for positive
integers \(r,t\) satisfying \(t^2-t<4r-2\), \(E_r(2)\) is the smallest
eigenvalue of \(J(4r+t,2r,r)\) for all sufficiently large \(r\). Specializing
to \(t=2\) proves only the eventual assertion, with no explicit threshold or
classification of the remaining cases.

The proposed contribution is to replace “sufficiently large” by the sharp
threshold for `t=2` and classify every smaller `r`. A bounded verification route
is available: use Proposition 12's explicit comparisons for indices `0,1,3`,
make its trace/multiplicity estimate effective for all indices `j>=4`, and check
the finitely many residual values directly from the integer formula.

Primary source inspected 2026-09-07:
<https://arxiv.org/html/2609.04677v1>, especially equation (2.1), Proposition
12, and Theorem 13. The frozen source also records PDF SHA-256
`de3b37a3c87eeeef297382da835922996e804e6b2ab44d1a2e763cc4fa9881f3`;
the PDF itself was not re-downloaded during this triage.
