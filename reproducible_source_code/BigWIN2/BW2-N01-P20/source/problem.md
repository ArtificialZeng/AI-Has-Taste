# Precise problem and submitted candidate scope

Research job `newwin-00001-p20-research-f42a5d965fef`; date 2026-09-12.
The exact original Chinese statement remains in immutable `source.md`,
SHA256 `b5dd0cb2ff5644a13c42b0b0e352a6a172be7c766f45a41ad37d89c83c4af495`.
No correction or weakening of its target is proposed.

## Definitions and quantified target

For integers \(m\ge1\) and \(0\le k\le2m-1\), define
\[
G_{m,k}=\begin{cases}
\displaystyle\sum_{i=0}^{k}\binom{2m-1}{i},&k<m,\\[4pt]
\displaystyle\sum_{i=0}^{2m-2-k}\binom{2m-1}{i}
 +(k-m+1)\binom{2m}{k+1},&k\ge m,
\end{cases}
\qquad E_{m,k}=\frac{G_{m,k}}{\binom{2m-1}{k}}.
\]
The sums are over integer indices, and a sum with negative upper endpoint
is zero. For \(0\le b\le a\), \(\binom ab=a!/[b!(a-b)!]\), with
\(0!=1\). Every binomial coefficient used in this definition has a valid
index. The denominator is positive.

In the cited model, \(E_{m,k}\) is the mean gap for uniformly sampled
arrival sequences of length \(2m-1\) with exactly \(k\) red cars and lane
capacity \(m\). The displayed finite formula is sufficient to define the
research problem; no probabilistic modeling assumptions are added.

For real \(x\), set
\[
k_m(x)=m+\lfloor x\sqrt m\rfloor,\qquad
\delta_m(x)=\lfloor x\sqrt m\rfloor-x\sqrt m\in(-1,0],
\]
where \(\lfloor t\rfloor\) is the greatest integer not exceeding \(t\).
Find explicit functions independent of \(m\),
\[
F_0:\mathbb R\to\mathbb R,\qquad
F_1:\mathbb R\times(-1,0]\to\mathbb R,
\]
and prove that for every real \(A>0\) there are a finite constant
\(C_A\ge0\) and an integer \(M_A\ge1\) such that for every integer
\(m\ge M_A\) and every real \(x\in[-A,A]\), the index \(k_m(x)\) is
admissible and
\[
\left|E_{m,k_m(x)}-\sqrt m\,F_0(x)
-F_1(x,\delta_m(x))\right|\le C_A m^{-1/2}.
\]
Admissibility alone holds, for example, for
\(m\ge\lceil(A+2)^2\rceil\); the error threshold may be larger.
The target includes every floor jump, \(x=0\), and sequences of real
\(x\) approaching either from either side as \(m\) changes. The branch
\(k_m(x)<m\) is exactly \(x<0\), including arbitrarily small negative
\(x\). The actual value of \(\delta_m(x)\) must be retained.
There is no requested uniformity for growing \(A\), no off-center regime,
and no assertion that these functions are uniquely determined outside
points sampled by the expansion.

## Nearest prior result, delta, and verification route

Insko, Johnson and Sullivan, *A Combinatorial Model for Lane Merging:
Limited Capacity Lanes*, ECA 6:2 (2026), S2R9,
DOI 10.54550/ECA2026V6S2R9,
[publisher PDF](https://ecajournal.haifa.ac.il/Volume2026/ECA2026_S2A9.pdf).
Corollary 7.2, printed p. 11, gives the exact expectation, outer bounds,
and an exact central value. Section 8, question 2, printed p. 12, asks
for an improved approximation when \(k\) is close to \(m\). The upper
branch matches the frozen formula since its subtraction
\(\binom{2m-1}{k}=\binom{2m-1}{2m-1-k}\) removes the last summand.
The two-term all-A uniform expansion with floor correction is the user's
precise refinement of that broader question.

Nearest prior result X: the foregoing exact formulas and bounds.
Proposed delta Y: explicit leading and constant terms throughout the
bounded central window with absolute \(O_A(m^{-1/2})\) error.
Verification route Z: exact symmetry at the odd binomial center, a
central Wallis-integral inequality, the finite-product logarithmic
estimate, and signed finite-interval trapezoidal bounds. The complete
proposer argument and explicit uniform constants are now in
`evidence/research-proof.md`. It fills the formerly conditional local
mass/CDF estimates and then handles division and the floor correction.
The coefficients are an output, not part of the frozen input.

Source status: **open-supported parent question; status-uncertain precise
refinement beyond the bounded literature screen**. The later Hiveley--
Zeilberger multi-lane result counts different objects/conditioning and
has no equivalent expansion in the inspected sections. No prior
resolution was located in the screened primary material; this is not
proof of novelty. General binomial approximation methods are classical,
and any useful contribution would be this specific near-center formula.
The earlier Bardenova et al. JIS 26 (2023), 23.5.3 was also newly inspected
online at Lemma 25/Corollary 26 and Open Problem 39. Its fixed-ratio
right-lane limit and separately posed capacity problem do not give this
expansion. See `evidence/research-literature.md` for exact source scope,
live queries, and access limits. The decisive original local primary PDF
is copied byte for byte into
`evidence/external/insko-johnson-sullivan-limited.pdf` for the claim snapshot.
The historical registry is not present in the project, so the supervisor's
broader deduplication report remains attributed, not independently verified.

## Submitted full-scope answer

With H(x)=sqrt(pi) exp(x^2) erfc(|x|)/2 and x_+=max(x,0), the candidate is
\[
F_0(x)=H(x)+2x_+,\qquad
F_1(x,\delta)=(2\delta+1)xH(x)+\delta+1-2x_+^2.
\]
Here erfc(t)=(2/sqrt(pi)) integral from t to infinity of exp(-u^2) du.
The proof establishes the original all-A/all-real-x quantifiers above,
with no growing-window claim. It gives explicit nonoptimized C_A and M_A.
The elementary methods are classical; the proposed contribution is their
specific application to the published near-center approximation gap.

Research decision: submit **candidate**, kind `resolution-paper`, original
status `proved` as the proposer's full-scope claim, pending a fresh referee.
No acceptance or manuscript is produced. `claim.json` states the exact
scope. `evidence/research-verification.md` separates analytic reasoning,
exact finite algebra, floating-point observations, and remaining review.
