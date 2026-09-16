# Antiprism h-vector transformation: total nonnegativity

Primary source: Yanxin Liu and Jianxi Mao, Total positivity of transformation matrices for uniform subdivisions, arXiv:2607.01577v1 (2026-07-02).
https://arxiv.org/pdf/2607.01577v1
https://arxiv.org/html/2607.01577v1
The PDF calls the passage Remark 5.8, printed page 19; the HTML calls the same passage Remark 5.20. These are numbering differences, not different mathematical assertions. Full original captures are preserved separately.

The author's closing question is:
> It is natural to consider the interlacing property and total positivity of this transformation matrix.

Selected original target: determine whether the antiprism h-vector transformation matrix is totally nonnegative in every dimension. The other interlacing question is context, not a second task required for a full answer to the selected total-positivity question.

For every integer d>=1, define the (d+1)-by-(d+1) integer matrix H_d with row and column indices 0,...,d by the displayed primary formula, transcribed mathematically:
H_d(i,j) = sum_(r=0)^d sum_(s=0)^i binom(j,s) binom(d-j,d-r-s) binom(r,i-s)
            * sum_(ell>=0) (ell!)^2 S(i-s,ell) S(r-i+s,ell).
Here S(a,b) is a Stirling number of the second kind; S(0,0)=1 and out-of-range Stirling numbers and binomial coefficients are zero. Equivalently restrict every summand to its valid nonnegative indices. The sums are finite.

Is it true that, for every d>=1, every 1<=k<=d+1, and all strictly increasing row and column lists I,J of length k in {0,...,d}, det H_d[I,J]>=0?
Total positivity in these sources means NONNEGATIVITY of all minors, not strict positivity. This is the full finite-dimension matrix family, not the infinite Eulerian triangle and not its TP4 truncation. Zero boundary entries are intentional.

The matrix sends h(Delta) to h(sd_A(Delta)) for a (d-1)-dimensional simplicial complex. An independent combinatorial definition of antiprism subdivision and the transformation is in Athanasiadis, Brunink and Juhnke-Kubitzke, Combinatorics of antiprism triangulations, arXiv:2006.10789v2, Section 5.3, equations (19)--(21), Propositions 5.11--5.12 (printed pages 21--22).
https://arxiv.org/pdf/2006.10789v2

Primary earlier context: Mu and Welker, arXiv:2404.03500v2, the geometric-conditions question after the counterexample in Section 2 (its HTML numbering is broken as Question 2.0), explicitly reports small-dimensional antiprism total positivity. It does not prove all dimensions. The 2026 paper resolves barycentric and interval cases, not the selected antiprism family.
https://arxiv.org/html/2404.03500v2

Frozen on 2026-09-14 via authorized primary-literature fallback, not Chrome generation. No 大WIN batch number consumed. Source status is open-supported in the inspected current primary sources and bounded follow-up searches, not an absolute guarantee of worldwide priority. The full Excel corpus and local registry were screened; unavailable live conversation history is explicitly not claimed deduplicated. Operational guidance, source limitations, and nearest-neighbor comparisons are in literature/outer-intake-handoff.md and screen.md.
