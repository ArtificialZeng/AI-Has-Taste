# Precise problem statement

## Frozen claim and interpretation

The immutable claim in `source.md` is interpreted for the colored undirected cycle

\[
V=\mathbb Z/5\mathbb Z,\qquad
E=\{\{i,i+1\}:i\in\mathbb Z/5\mathbb Z\}.
\]

All vertices lie in one color class. Each of the five edges lies in its own color class. Distinct colors impose no numerical inequality: the five edge parameters are independent, but their realized values may coincide.

With indices modulo (5), the associated six-dimensional concentration space is

\[
L_{G_5}=\left\{K(a,b_0,\ldots,b_4):
K_{ii}=a,\ K_{i,i+1}=K_{i+1,i}=b_i,\ K_{ij}=0
\text{ otherwise}\right\}.
\]

Thus

\[
K(a,b)x=0
\quad\Longleftrightarrow\quad
a x_i+b_{i-1}x_{i-1}+b_i x_{i+1}=0
\quad(i\in\mathbb Z/5\mathbb Z).
\]

Here `PSD(5)` is the cone of real symmetric positive-semidefinite (5\times5) matrices, and `mlt` is Definition 2.13 of the cited primary paper: the least sample rank (n) for which the MLE exists with probability one for rank-(n) sample covariance matrices.

The exact assertion is

\[
\operatorname{mlt}(G_5)=1,
\]

equivalently

\[
\text{for Lebesgue-almost-every }x\in\mathbb R^5,
\quad
\{K\in L_{G_5}\cap\operatorname{PSD}(5):Kx=0\}=\{0\}.
\]

The measure is five-dimensional Lebesgue measure. The null vector (x=0) and other measure-zero strata cannot decide the assertion. Conversely, an open set of (x)'s carrying nonzero PSD kernel matrices disproves it. No normalization of (x) is part of the frozen statement; homogeneity would permit a sphere or affine-chart normalization only if the omitted strata are tracked explicitly.

## Source status and nearest result

The local PDF with SHA-256 `29727f7143ce6a7a92cf15dc80882e74590b7a3de66c42b50c31a4d94737e48d` is arXiv:2609.02382v1. Its actual title and authors are Roser Homs, Olga Kuznetsova, and Bernadette J. Stolz, *A computational approach to maximum likelihood thresholds for colored Gaussian graphical models* (dated 2026-09-03). The bibliographic title/authors written in immutable `source.md` are therefore incorrect, although its mathematical locators and statement agree with this PDF.

In that paper, Definition 2.2 gives (L_G), Definition 2.13 gives `mlt`, and Theorem 3.4(2) gives the PSD-kernel characterization. Proposition 3.25 proves only `wmlt(G)=1`. Proposition 3.26 proves `gcr(G)=2` for cycles with one vertex color and all edge colors distinct, and proves `mlt(G)=1` only for even cycle length. Conjecture 3.27 states the odd-cycle assertion. Therefore the source status at triage is `open-supported` as of the v1 paper, not a verified historical open problem.

Exact web searches on 2026-09-07 for the assertion, its conjecture number, and the paper title found the v1 paper and announcements/talks, but no separate primary proof or disproof. This bounded search is not a priority claim.

## Five-cycle baseline certificate

Put (x^*=(1,1,1,1,1)^T) and let

\[
K^*=K(2,-1,-1,-1,-1,-1).
\]

Then (K^*x^*=0) and

\[
y^T K^*y=\sum_{i\in\mathbb Z/5\mathbb Z}(y_i-y_{i+1})^2,
\]

so (K^*\succeq0), has rank (4), and is positive definite on ((x^*)^\perp).

For fixed (a=2), write the five kernel equations as

\[
B(x)b=-2x,
\]

where the columns of (B(x)) correspond to (b_0,\ldots,b_4). Exact expansion gives

\[
\det B(x)=2x_0x_1x_2x_3x_4,
\]

hence (det B(x^*)=2\ne0). Therefore (b(x)=-2B(x)^{-1}x) and (K(x)=K(2,b(x))) are continuous near (x^*), with (K(x)x=0). Since the four nonzero eigenvalues of (K^*) are positive, eigenvalue continuity makes (K(x)\succeq0), nonzero, and rank (4) throughout a sufficiently small open neighborhood of (x^*). This is the requested positive-measure obstruction. The exact open-box version is proved in `evidence/research_disproof.md` and is subsumed by the all-odd theorem below.

## Strengthened resolution candidate

For every fixed odd integer `m >= 3`, the same exact construction proves
`mlt(G_m)=2` for the cycle with one common vertex color and all edges in
distinct color classes. The kernel coefficient matrix has determinant

\[
\bigl(1+(-1)^{m-1}\bigr)\prod_i x_i=2\prod_i x_i.
\]

Its solution with diagonal parameter `a=2` therefore varies continuously from
`b=(-1,...,-1)` near `x=(1,...,1)`. On the nonempty open set where `x_i>0`
and `b_i<0`, the congruence `D K D=L_w` identifies `K` with a positive-weight
cycle Laplacian, up to invertible diagonal congruence. Thus a positive-measure
set of one-observation vectors has a rank-`m-1` PSD annihilator. Theorem 3.4(2),
Corollary 3.7, and Proposition 3.26 then give `mlt(G_m)=2`.

The case `m=5` completely disproves the frozen claim. Combining the new odd
case with Proposition 3.26 gives the full parity classification: threshold `1`
for even `m` and threshold `2` for odd `m`. Appendix Table 2 of the primary
source already gives `mlt=2` for `m=3` in this coloring, so `m=5` is the first
untreated odd length in that source, not the first odd length absolutely.

The complete argument and exact replay are in `evidence/research_all_odd.md`
and `evidence/research_all_odd.py`. Exact web searches on 2026-09-07 found no
separate primary resolution beyond arXiv:2609.02382v1; this is a bounded
comparison and not a claim of priority. The strengthened scope supersedes the
earlier `m=5`-only candidate and requires a fresh mathematical referee.
