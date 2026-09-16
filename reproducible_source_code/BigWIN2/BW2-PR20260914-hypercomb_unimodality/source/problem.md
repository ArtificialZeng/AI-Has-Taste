# Frozen interpretation: uniform linear hypercomb unimodality

The original wording is preserved verbatim in `source.md`, SHA-256
`66bd66f1a94163be3cb7f8929629c0f122d7f7490759017615c0d690a842773c`.
This interpretation fixes no upper cutoff on either parameter.

For every pair of integers n >= 1 and ell >= 3, take a linear ell-uniform
hyperpath with spine edges e_1,...,e_n. Consecutive edges meet in one vertex;
nonconsecutive edges are disjoint. Select attachment vertices w_0,...,w_n:
w_i = e_i intersect e_(i+1) for 1 <= i < n, and private vertices w_0 in e_1
and w_n in e_n. For n=1 the two selected vertices must be distinct. At each
w_i attach an ell-element edge consisting of w_i and ell-1 fresh vertices,
all fresh vertex sets disjoint. No other vertices or edges are present.
Call the resulting hypergraph C_(n,ell).

A strong independent set is a subset S of its vertices such that
|S intersect e| <= 1 for every hyperedge e. Define
c_(n,ell,k) = #{S: S is strong independent and |S|=k}, and
C_(n,ell)(x) = sum_k c_(n,ell,k) x^k.
There are 2n+1 edges and (2n+1)(ell-1)+1 vertices. The maximum independent
set size is 2n+1: every edge has a private vertex, so the upper bound from
at most one selected vertex per edge is attained. Thus the degree and the
index range below are exact.

**Target.** For every n >= 1 and ell >= 3 there exists an integer
m in {0,...,2n+1} such that
c_(n,ell,0) <= ... <= c_(n,ell,m) >= ... >= c_(n,ell,2n+1).
Equalities and multiple adjacent modes are allowed. Weak hypergraph
independence, arbitrary linear hypertrees, and ell=2 are outside this target.
Log-concavity is a strictly stronger possible route; its failure would not
disprove the target. A smaller central gap or an eventual theorem is partial.

The exact recurrence in Galvin--Sharpe, Theorem 1.7, is

    C_0 = 1 + ell*x,
    C_1 = 1 + (3ell-2)x + 3(ell-1)^2 x^2 + (ell-1)^2(ell-2)x^3,
    C_n = (1+(ell-1)x) ((1+(ell-2)x) C_(n-1) + x C_(n-2)), n >= 2.

C_0 is only an auxiliary initial polynomial. The simplified x^2 coefficient
above equals the unsimplified coefficient frozen in `source.md`.

**Nearest prior result and status.** David Galvin and Courtney Sharpe,
*Independent set sequence of some linear hypertrees*, Australasian Journal
of Combinatorics 94(1) (2026), 93--121; arXiv:2409.15555v5 (30 January 2026).
Theorem 1.7 is on journal p.99, Corollary 1.8 and Note 1.9 on p.100;
Section 2.5 supplies the recurrence and a sum of two log-concave polynomials.
For each fixed ell, Corollary 1.8 leaves a possible O(sqrt(n)) band, and
Question 1.10(4) asks to shorten or eliminate it. Note 1.9 withdraws the
earlier all-parameter log-concavity proof because of a proof error, without
giving a counterexample. The authors report finite unimodality checks for
n <= 500 and ell <= 12. Current source status is `open-supported` under the
bounded literature screen, not a worldwide priority assertion.

Primary sources inspected on 2026-09-14:
- https://arxiv.org/abs/2409.15555 (current version history)
- https://academicweb.nd.edu/~dgalvin1/pdf/journal/linear-hyperpaths_J.pdf

**Subsequent literature correction.** The live triage additionally found
*Eventual Strict Log-Concavity of Weighted Linear Hypercombs*, aiXiv
aixiv.260910.000002v1.0 (10 September 2026), attributed to OpenAI Codex
GPT-6-Astra. Its Theorem 1 and Corollary 2 on p.2 assert eventual strict
log-concavity for each fixed positive weight pair; s=ell-2,t=ell-1 gives
our recurrence exactly. Its Section 9 retains the all-length question.
The full proof and claimed Lean verification were not audited in triage.
The statement was inspected in the primary PDF, not inferred from a snippet:
https://aixiv.science/pdf/aixiv.260910.000002v1.0.pdf . See
`literature/triage-live-screen.md`. This corrects the supplied handoff's
limited later-literature screen and updates the nearest overlapping result;
`source.md` remains unchanged.

**Research-pass candidate, strictly partial.** The original full-unimodality
target above is unchanged. A proposed proof now gives, for every n>=2 and
ell>=3, W_n <=_lr x^2 Y_n and Y_n <=_lr x W_n, where
W_n=C_1 F_n, Y_n=C_0 b F_(n-1), F_0=0,F_1=1 and
F_n=a F_(n-1)+b F_(n-2). The order P <=_lr Q means
p_i q_j >= p_j q_i for all integers i<j, with zero-extended coefficients.
Consequently the smallest modes satisfy
m(Y_n)-1 <= m(W_n) <= m(Y_n)+2. The sum is nondecreasing up to the smaller
mode and nonincreasing from the larger; these endpoints differ by at most
two index steps. The separation two is attained at n=3,ell=5 for these
summands. This does not assert nonunimodality of that example or settle the
possible intermediate valley for the full family. The center of the new
interval is specified by the summand modes, not an explicit affine formula.

The proposed contribution is this all-length, all-uniformity constant
bound, distinct from the journal O(sqrt(n)) interval and the later preprint's
fixed-parameter eventual statement. The complete argument and its scope
are in `evidence/two-step-mode-proof.md`; exact implementation checks are
in `evidence/two_step_checks.py` and `evidence/two-step-checks.json`.
No independent acceptance is claimed. The fresh primary-source comparison
is `literature/research-mode-bound-screen.md`. Decisive supplied primary
PDFs are preserved byte-identically as
`evidence/external/linear-hyperpaths-author-journal.pdf` and
`evidence/external/2409.15555v5.pdf`; their capture record is alongside them.
