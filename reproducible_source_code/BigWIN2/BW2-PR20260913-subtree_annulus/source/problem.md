# Precise original problem and result-note candidate scope

Research job: primary-20260913-subtree-annulus-research-bac30ce160a8.
Date: 2026-09-13 +08. The admitted double-star target is unchanged.
The original `source.md` is immutable; its SHA256 is
`780c2b23b0b5c8ff23910d73403f7abbeb0f811ea709caaf64323eefbab29f94`.

For every integer n>=2 and every finite simple connected acyclic graph T=(V,E)
with |V|=n, define s_k(T) to count vertex subsets S of cardinality k for which
T[S] is connected. Subsets are counted once, not up to isomorphism; the empty
set is excluded. Set Phi_T(z)=sum_{k=1}^n s_k(T) z^k.
For every z in C, the target is

    Phi_T(z)=0  ==>  1/2 <= |z+1/2| <= 1/2+(n-1)^(1/(n-1)).

Both inequalities are closed. All complex zeros, including the simple zero
z=0 (since s_1=n), belong to the target. No multiplicity exception is made.
Neither an origin-centred estimate nor a subclass result resolves this target.
There is no material ambiguity in the supplied reading.

Source status: **open-supported**, not exhaustively certified open. Brown–Mol,
[arXiv:1810.08655v1](https://arxiv.org/pdf/1810.08655v1), physical pp.1–3
and 14, gives the definitions/recursions and Conjecture 4.2; the authors report
verification through order 18. This is prior computational evidence only.
Jin–Ma–Wang v1 Theorem 1.3 proves the radial upper bound. Live inspection also
found **v2, 14 August 2026**, titled *Proof of a Brown-Mol conjecture on subtree
roots*: [latest primary version](https://arxiv.org/html/2608.07898v2).
Its Theorem 1.3 adds radial equality classification; Section 5, Conjecture 5.1
still states the entire shifted annulus. This updates the intake's v1 boundary,
without altering the frozen original. The research pass rechecked this live
version and its actual statements. Current comparison and limits are in
`evidence/research-literature.md`. The original local Brown-Mol PDF and JMW
v1 HTML are copied unchanged into `evidence/external/`; current v2 primary
text is captured in `evidence/external/jmw-v2-front-research-live-web.txt`
and `evidence/external/jmw-v2-research-live-web.txt`.

Nearest prior result X: the universal radial bound and its equality cases,
together with the established path/star formulas. Candidate delta Y is the
following partial theorem, submitted for fresh review:

For every pair of integers a,b>=1, let D(a,b) consist of an edge uv with a
additional leaves at u and b additional leaves at v, of order n=a+b+2.
Every nonzero zero z of Phi_D satisfies

    1/2 < |z+1/2| < 1/2+(n-1)^(1/(n-1)).

The zero z=0 is simple. Consequently the original closed annulus holds for
every tree of diameter at most three and order n>=2. Within this class the
only inner-boundary root is zero, and an outer-boundary root occurs exactly
for even-order stars, uniquely at -1-(n-1)^(1/(n-1)). The star calculation is
prior elementary material; the proposed contribution is the uniform
two-parameter double-star theorem. No equivalent was found in the bounded
primary-source screen, which does not certify priority. The arbitrary-tree
original remains unresolved. No mathematical acceptance has occurred.

Verification route Z: the exact identity

    Phi_D(z)/z = q+(1+z)^a+(1+z)^b+z(1+z)^q,  q=a+b,

reduces outer-circle exclusion to a one-variable convexity estimate and
Rouche's theorem. The complete proof, quantitative positive margin, closed
inner-disk exclusion, and all boundary cases are in
`evidence/double-star-proof.md`. The q=2 P4 case has a direct modulus bound,
so no Hurwitz theorem is needed. Researcher checks and the independent exact
finite verification method are in `evidence/research-verification.md`.
The finite checks cover all unordered double-star parameters with a+b<=24;
they are supplementary to the infinite analytic proof and not a tree census.

The half-plane reformulation is also exact: with Q_T=Phi_T/z and

    H_T(x)=(x+1)^(n-1) Q_T(-1/(x+1)),

the inner inequality for nonzero roots is equivalent to all zeros of H_T
having Re x<=0. Indeed x=-1-1/z and
|z+1/2|^2-1/4=|z|^2 Re(1+1/z). H_T(-1)=(-1)^(n-1), so clearing
denominators introduces no root at the pole; z=0 maps to infinity and is
handled separately. This reformulation alone is not a new theorem.

Disposition: result-note candidate requesting a fresh referee on the exact
family scope above. No manuscript or PDF has been prepared. The research
pass's gap list identifies no mathematical gap in this family proof, while
correctness, novelty and value remain subject to review.
