# Ordinary reciprocal-subsum denominator log-concavity

## Frozen statement and precise interpretation

The immutable `source.md` quotes BBFM, Conjecture 4:

> The sequence of coefficients of den(n,x) is log-concave except for n=3,5,6,7.

Here n is a positive integer and x is an indeterminate. A partition lambda of n is a finite nonincreasing list of positive integers summing to n; m_lambda(i) counts its parts equal to i. In Z[x], set

\[
\operatorname{sp}(\lambda,x)=\prod_{a\in\lambda}(1+x^a),\qquad
H_n(x)=\prod_{i=1}^n(1+x^i)^{\lfloor n/i\rfloor},
\]
\[
h_\lambda(x)=H_n(x)/\operatorname{sp}(\lambda,x),\quad
G_n(x)=\gcd_{\lambda\vdash n}h_\lambda(x),\quad
\operatorname{den}(n,x)=H_n(x)/G_n(x).
\]

The gcd is normalized to be monic. Each exponent in h_lambda is nonnegative. Proposition 3.8 identifies this polynomial exactly as

\[
D_n(x)=\prod_{i=1}^n(1+x^i)^{e_{n,i}},\qquad
 e_{n,i}=1+\lfloor\log_2(n/i)\rfloor
        =\#\{q\in\mathbb Z_{\ge0}:2^qi\le n\}.
\]

Write L_n=sum_(i=1)^n i e_(n,i) and D_n=sum_(j=0)^(L_n) d_(n,j)x^j. The exact target is

\[
\forall n\in\mathbb Z_{\ge1}\setminus\{3,5,6,7\},\quad
\forall j\in\mathbb Z,\ 1\le j<L_n:
\quad d_{n,j}^2\ge d_{n,j-1}d_{n,j+1}.
\]

All integer degrees count, including any zeros; no parity subsequence or rescaling of x is permitted. Weak inequalities are intended. For n=1 the internal-index condition is vacuous. The four excluded values are known failures, independently recalibrated in this job. No finite upper bound replaces the universal quantifier. No correction to the source statement is proposed.

## Primary status and nearest prior result

Source status: **open-supported**, checked 2026-09-13 +08 / 2026-09-12 UTC, within a bounded literature search. This is distinct from suitability and is not exhaustive novelty clearance.

- Ballantine–Beck–Feigon–Maurischat, *Reciprocals of subsum polynomials*, The Ramanujan Journal 70, article 46 (2026), [journal](https://doi.org/10.1007/s11139-026-01419-0). Definitions pp. 2–3; Proposition 3.8 and Proposition 3.9 p. 11; Proposition 3.10 p. 12; Conjecture 4 p. 18. Proposition 3.9 establishes palindromicity and unimodality, which are weaker than the target.
- Chen–Ono–Zhang, *Reciprocals of Partition Polynomials*, [arXiv:2605.21718v2](https://arxiv.org/html/2605.21718v2), revised 22 May 2026: Conjecture 4 p. 4 and Table 1 p. 6 explicitly retain this ordinary-denominator problem as open. Their binary-numerator counterexample concerns a different polynomial and does not settle this claim. Journal and preprint conjecture numbering differ elsewhere.

Both cached PDFs were hash-checked against the intake fingerprints; relevant extracted passages were read and compared with live primary HTML. See `evidence/triage.md` for search scope and provenance.

## Proposed delta and verification route

Nearest prior result X: the explicit product, symmetry/unimodality, and recurrence. Proposed delta Y: a uniform quantitative inequality for consecutive-coefficient minors along the recurrence, sufficient to prove the full target. Verification route Z: exact integer falsification first, then a uniform algebraic or coefficient-ratio proof; finite verification alone is insufficient.

Put r=v_2(n), o=n/2^r, and

\[
A_{n,k}(x)=D_{n-1}(x)\prod_{h=0}^{k-1}(1+x^{2^h o}),
\quad 0\le k\le r+1.
\]

Thus A_(n,0)=D_(n-1), A_(n,r+1)=D_n, and each next factor has shift s=2^k o. The full list of factors is required. Extend coefficients by zero outside their support and define T_j(A)=a_j^2-a_(j-1)a_(j+1).

The **unproved research target H** is

\[
2T_j(A_{n,k+1})\ \ge\ T_j(A_{n,k})+T_{j-s}(A_{n,k})
\tag{H}
\]

for every n>=9, every 0<=k<=v_2(n), and every integer j. Starting from the exactly checked D_8, H would propagate log-concavity through every stage and every n>=9; n=1,2,4 are separately finite checks. H is a stronger subsidiary claim, not a restatement accepted as proved. A failure of H alone would not disprove the original target.

Exact tests now cover 9<=n<=512 at all 60,553,416 stage/index pairs, covering all finite supports; outside them both sides vanish. Research pass 1 adds 52,893,866 checks in 257<=n<=512, with no failure of H or of any original or intermediate minor. The minimum ratio of the new minor to the sum of the old minors, where the denominator is positive, remains 5/9. This is finite evidence, not a uniform proof or mathematical acceptance.

## Research pass 1: restricted theorem and remaining kernel

The complete argument and exact certificates in `evidence/research.md`,
`evidence/research_edge_probe.py` and `.json` prove H for every n>=9 and
every stage at 0<=j<=32, together with the reflected indices. In particular,
the original minors are nonnegative for every positive n outside the four
exceptions when min(j,L_n-j)<=32. This restricted infinite-n result uses
561 polynomial templates, 24,497 nonnegative Newton coefficients and 968
earlier finite cases. `evidence/research_verify.py` and `.json` recompute
these certificates by a separate implementation. This is not a fresh referee
or novelty determination; no candidate is proposed from the fixed cutoff alone.

The reduction writes each stage adding s as n=s*2^t. Once n>=j+1, all
exponents affecting degree j+1 increase by exactly one when t increases by
one, making the H margin F_(s,j)(t) a polynomial of degree at most 2j.
Nonnegative Newton coefficients therefore certify infinitely many n.
Induction from D_8 handles the unaffected stages s>=j+2 without assuming
full log-concavity.

The next **unproved kernel K** asks: for every j>=0 and 1<=s<=j+1, put
t0=min{t>=0:s*2^t>=max(9,j+1)}. Are all forward differences
Delta^h F_(s,j)(t0) nonnegative for 0<=h<=2j? The exact definition of F,
bivariate coefficient identity, and design evidence through j=32 are in
`evidence/research.md` and `evidence/research_kernel_probe.json`. Uniform K
would cover n>=j+1, leaving the n<j+1 region; it is not asserted equivalent
to H or the original claim. A negative Newton coefficient could refute K
without refuting H.

An exact obstruction rules out a simpler qualitative route: a=(1+x)^16,
s=4 satisfies strict log-concavity, symmetry and the first-overlap bound,
and a(1+x^4) is log-concave, but H has margin -15,077,504 at j=10.
These are not actual recurrence-stage coefficients and do not disprove H
on the designated family.

## Scope and comparison limits

The local historical-comparison report and its six quoted nearest statements were reread. They concern other polynomial families and give no identified equivalence or direct implication. The original registry corpus and target conversation are unavailable inside this project, so the earlier corpus-wide result is retained as supplied evidence, not claimed as freshly rerun. No literal `literature/*handoff*.md` files were present; `literature/outer-intake.md` was read as the existing semantic handoff and its mathematical leads checked.

One next test: run `python3 evidence/research_kernel_probe.py --B 64` on
the frozen K, isolating previously untested 33<=j<=64, every s and every
Newton coefficient. Save any exact negative coefficient and evaluate its F
polynomial to distinguish failure of K from failure of H. If it survives,
seek a uniform proof from the recorded bivariate identity instead of another
full-n prefix extension.


## Research pass 2: current evidence and refined kernel

The assigned held-out K test through j=64 passes: 2,145 polynomials and
185,185 exact Newton coefficients, including 160,688 newly tested
coefficients at 33<=j<=64. A separate logarithmic-derivative implementation
reproduces every coefficient and all 3,068 earlier finite cases. The edge
theorem now covers min(j,L_n-j)<=64 for every n outside the four exceptions.
This does not settle the original universal claim. See `evidence/research2.md`
and its reproducible certificates. All pass-1 evidence remains preserved.

A proved auxiliary band gives positivity at h=2j-k whenever
j>=2k^2+k-1, uniformly in j and s. The low and middle Newton orders remain
unproved. The exact affine-exponent threshold improves from n>=j+1 to
2n>j+1. Freeze K_sharp_v1: for every j>=0 and 1<=s<=j+1, take the least
tau>=0 with s*2^tau>=9 and 2*s*2^tau>j+1; require all
Delta^h F_(s,j)(tau)>=0 for 0<=h<=2j. Its design range j<=64 passes, with
175,492 independently recomputed coefficients at 1,956 earlier starts.
This revised kernel has not yet had a held-out test. Even uniform K_sharp
would leave the separate j>=2n-1 region.

The affine threshold has a precise boundary obstruction: n=s=9,j=17 gives
F(0)=19668>0, but the polynomial tail extrapolates to 20795. Therefore its
actual 36th forward difference is -1127. This refutes polynomiality/global
Newton positivity from that excluded start, not K, K_sharp, H, or the
original target. Details are in `evidence/research2.md`.

Pass-2 next test, now completed in pass 3: freeze K_sharp_v1 and check
every s,h for 65<=j<=96 at its exact earlier start, independently verifying
the coefficients and distinguishing any failure from failure of H.

## Research pass 3: proposed conjecture-note scope

The original all-n, all-index claim remains unresolved. The proposed
candidate is the **explicitly unproved K_sharp_v1**, with its exact
quantifiers and full stage definition restated in `evidence/research3.md`.
No change was made to this kernel after its pass-2 freeze.

The held-out 65<=j<=96 test has 2,608 templates and 427,952 strictly
positive integer Newton coefficients. A separate logarithmic-derivative
implementation recomputes every coefficient and all 2,014 earlier
admissible margins, plus 5,216 evaluations outside the interpolation grids.
The inherited j<=64 sharp certificate is also fully recomputed in this
pass, including its 1,112 earlier cases. Together these prove the restricted
edge theorem with min(j,L_n-j)<=96 for every admissible n; the dossier
contains the complete finite-certificate reduction and induction.

A sparse second attack tests all Newton orders in 128 templates at the
listed degrees near 128,192,256,512, up to j=513. All 69,632 coefficients
are nonnegative. The precise shift/degree domain is in the dossier and
`evidence/research3_boundary_probe.json`; this is not exhaustive coverage
through 513. Separate verification checks five low orders, the top two
formulas and outside-grid values there; it does not independently
recompute every middle coefficient in this sparse range.

`evidence/research3_boundary_lemma.md` strengthens the previous isolated
obstruction: at j=2n-1, for every n>=9 and every actual stage adding s,
the discrepancy from the extrapolated polynomial tail is
-a_(2n-2)-2a_(2n-s-2)<0. Every even forward difference of order at least
4n is negative. This is an obstruction to extending the polynomial/
all-order Newton method through that boundary, not a disproof of K_sharp,
H, or the original problem.

Clarification of the kernel's payoff: it directly certifies H in 2n>j+1
for affected shifts s<=j+1. An unaffected shift reduces to an old minor,
which requires an induction or separate evidence. K_sharp alone is not
claimed to prove original log-concavity on an entire moving linear edge.
Its low/middle Newton orders and the original unbounded interior remain
unproved. The supporting high-order band and exact boundary obstruction
give the conjecture a structural basis; novelty and interest need fresh
review. Decisive primary PDFs are copied unchanged to evidence/external/.

One next test: independently attack K_sharp_v1 for j in {1022,1023,1024},
s in {1,2,3,511,512,513,j,j+1}, and every 0<=h<=2j at its prescribed tau.
Reproduce any negative coefficient by signed binomial sums and distinguish
it from an actual negative H margin.
