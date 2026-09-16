# Binary reciprocal-subsum numerator log-concavity

## Frozen original and precise reading

The immutable `source.md` contains the original source statement:

> For n>=6, num_B(n,x) is log-concave.

Its SHA256 is `13e46a8af8569069d5eeadd7da3bb949452eccaa5e9472a43ebadec7f5231fdb`.
No correction to the original target is proposed.

For an integer n>=0, let B(n) be the finite set of multisets of powers of two
whose sum is n. The empty multiset is the sole partition of 0. For lambda in
B(n), let m_lambda(2^k) be the multiplicity of the part 2^k. For n>=1 define,
in the formal polynomial ring Z[x],

\[
 h_{n,\lambda}(x)=\prod_{k\ge0:\,2^k\le n}
 (1+x^{2^k})^{\lfloor n/2^k\rfloor-m_\lambda(2^k)},
 \qquad N_n(x)=\sum_{\lambda\in B(n)}h_{n,\lambda}(x).
\]

Every exponent is nonnegative. Set N_0(x)=1; the formula gives N_1(x)=1.
The common divisor G_B of the individual summands is 1 (BBFM Remark 6), so
this is exactly the journal's num_B, with no change of normalization. The
meaning of G_B must not be confused with the gcd of the summed numerator and
the denominator.

Let

\[
 d(n)=\deg N_n=\sum_{k\ge1}2^k\lfloor n/2^k\rfloor,
 \qquad c_{n,j}=[x^j]N_n(x),\quad 0\le j\le d(n).
\]

The full target is

\[
 \boxed{\ \forall n\in\mathbb Z,\ n\ge6,\quad
 \forall j\in\mathbb Z,\ 1\le j<d(n),\quad
 c_{n,j}^{\,2}\ge c_{n,j-1}c_{n,j+1}.\ }
\]

All consecutive integer degrees are included, without parity extraction,
coefficient normalization, omitted internal indices, or a strict inequality.
The variable x is formal; this is not a pointwise inequality for real x.

## Prior results, status, and boundary

Source status: **open-supported** as of 2026-09-13 Asia/Shanghai, with the bounded
literature limits recorded in `literature/triage-source-check.md`.
BBFM, *Reciprocals of subsum polynomials*, Ramanujan Journal 70:46 (2026),
DOI [10.1007/s11139-026-01419-0](https://link.springer.com/article/10.1007/s11139-026-01419-0),
Conjecture 7, p.21, states precisely n>=6. Proposition 4.1 gives d(n), positivity
of all coefficients, palindromicity, and N_(2m+1)=N_(2m). The weaker Conjecture 6
asks unimodality for n>=2. A proof only of unimodality is partial relative to
this frozen log-concavity target.

Theorem 4.7, pp.24–25, gives for every even n>=2

\[
 N_n=A_n+B_n,\qquad A_n=(1+x)^nN_{n/2}(x^2),\qquad
 B_n=\left(\prod_{i=1}^{v_2(n)}(1+x^{2^i})\right)N_{n-2}(x),
\]

where v_2(n) is the largest integer r such that 2^r divides n. Both summands
have degree d(n). These structural facts are prior work, not proposed contributions.

[Chen–Ono–Zhang v2](https://arxiv.org/html/2605.21718v2), section 1.2.2 remark,
p.4, explicitly retains the corrected log-concavity claim for n>5 as open.
The n=4,5 counterexamples in the older scope do not refute our source.
N4=N5=[4,10,18,18,20,18,18,10,4] has T_3=-36. In contrast, N6 has central
coefficients 100,100,100: the requested weak inequality allows this equality.

## Current research scope and evidence

The frozen original all-coefficient conjecture remains unresolved. Research
pass 2 proposes one **result-note candidate**, subject to fresh review.

**Main partial theorem.** For every real epsilon in (0,1), there is an integer
n_epsilon such that for every integer n>=n_epsilon, strict log-concavity holds
at every integer j with

    1<=j<=floor((1-epsilon)*sqrt(log_2(n)/2))

and at each reflected index d(n)-j. The proof is uniform in the growing j.
It supplies an explicit rational sufficient criterion at finite n; it does
not give a sharp threshold or settle the other internal positions.
`evidence/research-growing-boundary-proof.md` contains the complete argument.

The elementary mean-multiplicity bound is

    mu_n <= M_n := min_(0<=K<=floor(log_2 n))
                       (n+2^(K+1)-K-2)/(K+1),
    mu_n/n <= (1+o(1))/log_2 n.

It follows by grouping binary partition counts and summing expected part
weights. A union bound gives lower coefficient envelopes; the formal product
identity product_(k>=0)(1+x^(2^k))=(1-x)^(-1) gives upper envelopes. No
asymptotic enumeration theorem or floating-point decision is used.
The exact finite sufficient criterion is equation (G1) in the proof dossier.

**Uniform initial boundary theorem.** For every n>=6, strict log-concavity
holds at j=1,2,3 and d(n)-1,d(n)-2,d(n)-3. For even n>=6 the stronger
compensation inequalities T_j(N_n)>T_j(A_n)>0 hold at these positions,
where A_n=(1+x)^n N_(n/2)(x^2).

The first two positions were proved in `evidence/research-boundary-proof.md`.
The assigned third-position kernel is now proved: K3_m(l,t)>=0 for every
integer m>=5 and 0<=l<=t<=m, using its unchanged definition in that dossier's
equation (10). The complete new proof is `evidence/research-kernel3-proof.md`.
Its certificate uses 144 polynomial identities with 12325 nonnegative
monomials. A separate Fraction implementation verifies all identities and
complete infinite-domain coverage using 68 parity roots and 4119 clipped
vectors. Literal checks of 20790 entries for 5<=m<=48 calibrate the formulas;
they are not the infinite proof. Positivity of T3(A) is proved separately.

`evidence/research_growing_boundary.py` verifies the new mean and coefficient
bounds for n<=4096 using exact arithmetic, including 49085 coefficient
envelope checks. It independently builds low coefficients through degree 13;
it does not extend the earlier all-coefficient prefix. The rational criterion
also gives exact certificates at specified n=2^r up to r=1024 without computing
those huge polynomials. Coverage and limits are in its JSON output.

## Retained earlier evidence and failures

The sufficient all-index invariant T_j(N_n)>=T_j(A_n)>=0 for even n>=10 is
still unproved. Its finite survival through even n=512 is retained in
`evidence/research_recurrence.json`, including all 441984 internal indices of
the assigned earlier range 130<=n<=512. It is not a universal theorem.
The abstract carry-one induction cone still fails on the exact degree-eight
input in `evidence/research-boundary-proof.md`: A=[10,11,12,13,14,13,12,11,10],
B=2A yields an output T1=-304. This concerns abstract inputs, not the actual
binary numerator sequence. No original counterexample is known here.

## Candidate scope, sources, and one next test

`claim.json` binds only the partial boundary theorems and explicit criterion,
not the full original or the failed abstract induction. The kernel is a
supporting lemma for the uniform third position. No manuscript or acceptance
has been produced. These arguments have no known gaps in this research pass,
but fresh mathematical and novelty review is required.

Current bounded primary-source comparisons are recorded in
`literature/research-pass2-source-check.md`. The original BBFM journal PDF and
Chen–Ono–Zhang v2 PDF, with their full extracted texts, have been copied to
`evidence/external/` and included as decisive candidate inputs. No equivalent
of the proposed growing boundary theorem was found in these accessed sources;
this is not a priority certificate. No literature/*handoff*.md exists.

One next test: a fresh referee should try to invalidate the submitted boundary
claim by checking the mean bound, coefficientwise product domination, the
uniform-in-j limiting argument, and the exact kernel identities and complete
chamber coverage, then compare this precise partial scope with primary work.
The original source.md is unchanged; no correction or weakened reinterpretation
has been introduced. Historical deduplication limits remain those recorded in
`literature/triage-source-check.md`; no global registry rescan is claimed.
