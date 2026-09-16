# Exact obstruction for every odd cycle length

## Theorem and relation to the frozen problem

For every fixed odd integer \(m\geq 3\), let \(G_m\) be the colored
\(m\)-cycle whose vertices have one common color and whose \(m\) edges have
pairwise distinct colors. Then

\[
\operatorname{mlt}(G_m)=2.
\]

Distinct edge colors mean that the edge parameters below are independent; they
need not take distinct numerical values.  The case \(m=5\) disproves the
immutable assertion in `source.md`.  Together with the even case of Proposition
3.26 in the primary source, the theorem gives the parity classification

\[
\operatorname{mlt}(G_m)=
\begin{cases}
1,&m\text{ even},\\
2,&m\text{ odd},
\end{cases}
\qquad (m\geq3).
\]

## Proof

Use indices in \(\mathbb Z/m\mathbb Z\).  The concentration space consists of
the symmetric cyclic tridiagonal matrices

\[
K(a,b)_{ii}=a,\qquad
K(a,b)_{i,i+1}=K(a,b)_{i+1,i}=b_i,
\]

with all other entries zero.  Fix \(a=2\).  For an observation
\(x=(x_0,\ldots,x_{m-1})^T\), the equations \(K(2,b)x=0\) are

\[
x_{i-1}b_{i-1}+x_{i+1}b_i=-2x_i.
\tag{1}
\]

Let \(B_m(x)\) be their coefficient matrix in
\(b=(b_0,\ldots,b_{m-1})^T\).  Row \(i\) has just two nonzero entries:
\(x_{i-1}\) in column \(i-1\) and \(x_{i+1}\) in column \(i\).  In the
Leibniz expansion of its determinant, a supported permutation must choose
column \(i-1\) or column \(i\) in every row.  If one row chooses the former,
bijectivity forces every row to do so by cyclic propagation; otherwise every
row chooses the latter.  Thus the only terms are the identity and the cyclic
shift.  Their coefficient products both equal \(\prod_i x_i\), while the
shift has sign \((-1)^{m-1}\).  Hence

\[
\det B_m(x)=\bigl(1+(-1)^{m-1}\bigr)\prod_{i=0}^{m-1}x_i.
\tag{2}
\]

Suppose now that \(m\) is odd.  Whenever every \(x_i\ne0\), equation (2)
makes (1) uniquely solvable, with

\[
b(x)=-2B_m(x)^{-1}x.
\]

This is a continuous rational map on each orthant.  At
\(\mathbf1=(1,\ldots,1)^T\), its unique value is
\(b_i(\mathbf1)=-1\) for every \(i\).  Therefore the set

\[
U_m=\{x\in(0,\infty)^m:b_i(x)<0\text{ for every }i\}
\tag{3}
\]

is open and contains \(\mathbf1\).  In particular, it is nonempty and has
positive \(m\)-dimensional Lebesgue measure.

For \(x\in U_m\), set

\[
w_i=-b_i(x)x_ix_{i+1}>0,
\qquad D=\operatorname{diag}(x_0,\ldots,x_{m-1}).
\]

Multiplying (1) by \(x_i\) gives

\[
2x_i^2=w_{i-1}+w_i.
\tag{4}
\]

It follows from the diagonal entries (4) and the off-diagonal entries that

\[
DK(2,b(x))D=L_w,
\tag{5}
\]

where \(L_w\) is the weighted Laplacian of the cycle, with positive edge
weights \(w_i\).  Equivalently, for every \(y\in\mathbb R^m\),

\[
y^TK(2,b(x))y
=\sum_{i=0}^{m-1}w_i
 \left(\frac{y_i}{x_i}-\frac{y_{i+1}}{x_{i+1}}\right)^2.
\tag{6}
\]

The cycle is connected and all weights are positive, so (6) proves
\(K(2,b(x))\succeq0\),
\(\ker K(2,b(x))=\mathbb Rx\), and
\(\operatorname{rank}K(2,b(x))=m-1\).  Thus every \(x\) in the
positive-measure set \(U_m\) is annihilated by a nonzero matrix in
\(L_{G_m}\cap\operatorname{PSD}(m)\).  Theorem 3.4(2) of the primary source
therefore gives \(\operatorname{mlt}(G_m)>1\).  Proposition 3.26 gives
\(\operatorname{gcr}(G_m)=2\), and Corollary 3.7 gives
\(\operatorname{mlt}(G_m)\leq\operatorname{gcr}(G_m)\).  Consequently
\(\operatorname{mlt}(G_m)=2\).  This proves the theorem.

## Boundary, source, and reproducibility checks

- The determinant vanishes identically for even \(m\), exactly where this
  construction no longer provides a unique continuation.  This is consistent
  with, but is not used to prove, the source's even result.
- The smallest odd boundary case \(m=3\) is included.  Table 2 of the primary
  source lists the concentration matrix with one common diagonal parameter and
  three independent edge parameters (the row labelled `3 vertices`) with
  `WMLT=1` and `MLT=2`, agreeing with the theorem.
- The proof is pointwise for every fixed odd \(m\); no neighborhood uniform in
  \(m\) is asserted.
- Theorem 3.4(2), Corollary 3.7, Proposition 3.25, Proposition 3.26, Conjecture
  3.27, and Appendix Table 2 were checked in
  `evidence/external/2609.02382.pdf` (arXiv:2609.02382v1, SHA-256
  `29727f7143ce6a7a92cf15dc80882e74590b7a3de66c42b50c31a4d94737e48d`).
  The PDF identifies the authors as Roser Homs, Olga Kuznetsova, and Bernadette
  J. Stolz and the title as *A computational approach to maximum likelihood
  thresholds for colored Gaussian graphical models*; this corrects only the
  bibliography in `problem.md`, not the immutable `source.md`.
- Exact web searches on 2026-09-07 for the paper title, Conjecture 3.27, and the
  all-distinct-edge odd-cycle MLT statement found the v1 primary paper and no
  separate primary resolution.  This bounded comparison is not a priority or
  exhaustive-literature claim.
- Run `python3 evidence/research_all_odd.py`.  It replays the support-permutation
  determinant argument, parity boundary, exact rational kernel systems,
  congruence, and rank checks in adversarial dimensions.  The infinite theorem
  follows from the displayed proof, not from the finite replay.
