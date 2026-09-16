# Precise reading of the frozen source

Provenance: AJQ, *Real-rootedness of rook-Eulerian polynomials*,
arXiv:2502.05939v1, Section 3.3, Conjecture 28; Definitions 8/9 and
(10)--(12), Lemma 27. The verbatim source/transliteration remains in
`source.md`; the complete original HTML remains in `literature/`. The
byte-identical primary text bound for candidate review is
`evidence/external/ajq-2502.05939v1.html`.

## Objects, quantifiers, and normalization

For every pair of integers n,k >= 1, every nondecreasing positive integer
sequence lambda=(lambda_1,...,lambda_n), and every content vector
alpha=(alpha_1,...,alpha_k) in Z_{>=0}^k with sum n, define

W(lambda,alpha) = {w in {1,...,k}^n : #{r:w_r=j}=alpha_j for each j,
                   and w_r <= lambda_r for every 1<=r<=n}.

The sequence lambda is a left-justified Ferrers board in the source's
first-row-shortest convention. Multiple rooks in a column are allowed.
There is no skew lower bound. In particular lambda_r >= r is NOT imposed
here: the source's own Example 26, lambda=22233, already violates that
restriction from the distinct-letter setting.

Let asc(w)=#{r:1<=r<n and w_r<w_(r+1)}. This is a strict adjacent ascent;
there is no sentinel. Define

R(lambda,alpha;t) = sum_{w in W(lambda,alpha)} t^asc(w),
R_j(lambda,alpha;t) = sum_{w in W(lambda,alpha), w_1=j} t^asc(w).

Set R_j=0 for unused/out-of-range letters; then R=sum_{j=1}^{lambda_1} R_j.
Capping lambda_r at k leaves all word sets unchanged. The source permits
zero content coordinates. All witness coordinates below are positive.

## Exact original conjunction

(A) For every such lambda,alpha, each nonzero R(lambda,alpha;t) has only
real zeros (necessarily nonpositive because its coefficients are nonnegative).

(B) For every such lambda,alpha, the descending sequence
(R_{lambda_1},R_{lambda_1-1},...,R_2,R_1) is interlacing.

Precisely, for nonzero f,g with positive leading coefficients, list their
roots with multiplicity in descending order a_1>=a_2>=... and b_1>=b_2>=....
Definition 8 requires deg(g)-deg(f) in {0,1}, with
... <= a_2 <= b_2 <= a_1 <= b_1 <= 0.
If deg(g)=deg(f)+1, the alternating chain starts on the left with the
extra root of g; if the degrees agree, it starts with a root of f.
Definition 9 requires f_i preceq f_j for EVERY 1<=i<j<=length of sequence,
not merely adjacent pairs. Repeated roots are allowed.

Zero convention, stated separately: omit zero entries when testing a
sequence; a wholly empty word set contributes the zero polynomial and is
bookkeeping rather than a substantive counterexample. Positive constants
have empty root lists. For optional n=0 normalization, R=1 with no first-entry
refinements; it is outside the quantified n>=1 target. No proposed correction
or weaker replacement of the original conjunction is being substituted.

## Nearest prior results and candidate contribution

The source's Theorem 12 proves the distinct-letter rook result. Its paragraph
after Conjecture 28 attributes rectangular content totals to Simion (1984),
Section 2, and rectangular refinement interlacing to Ma--Pan (2023),
Theorem 1.11. The older proofs are not independently audited in this research
job and are not dependencies of the counterexample. The frozen primary
source explicitly states the conjecture; current bounded searches did not
identify a prior primary resolution or this counterexample. This is not a
worldwide priority assertion. See `literature/research-screen-20260913.md`.

The newer source Yan, *Variations of colored multiset Eulerian polynomials
and applications*, arXiv:2608.15682v1, was checked through the definitions
and Theorems 1.4/1.5. Its literal statements concern unrestricted colored
words, endpoint conventions and total-polynomial interlacing as content
changes, rather than this row-flagged first-entry sequence. A copy of the
complete local primary text is `evidence/external/yan-2608.15682v1.html`.
This is a bounded nearby-source comparison, not a theorem of non-equivalence
under arbitrary transformations. The earlier statement that this local
source was absent is corrected by the current file listing.

Nearest prior result X: those rectangular and distinct-letter results.
Candidate delta Y: an exact failure of clause (B) on a nonrectangular board
with repeated positive content. Verification route Z: a complete 30-base,
two-insertion counting certificate, a separate 720-labeled-order domain
check, comparison of every inherited TSV row, and an exact root inequality.

For lambda=(3,3,3,3,4,4), alpha=(2,2,1,1), exact verification gives
R_3=t(t^2+8t+3), R_2=t(8t^2+15t+1), R_1=t^2(t+7)(2t+1).
Their smallest roots satisfy -4-sqrt(13)<-7, violating R_3 preceq R_1
because their degrees are 3 and 4. The complete proof and dependency/limit
statements are in `evidence/research-proof.md`; exact integer verification
is in `evidence/research-six-letter-audit.json`, reproducible with
`python3 evidence/research-verify-six-letter.py` using only the standard library.

The total is 2t(t^3+12t^2+15t+2). Its cubic has one root in each of
(-11,-10), (-2,-1), and (-1,0) by exact integer sign checks; degree three
exhausts its roots. Thus the total in this example is real-rooted. Clause
(A) remains undecided here. Since the immutable original is the conjunction
(A) AND (B), one valid failure of (B) disproves that exact conjunction.
The candidate is therefore resolution-paper/disproved, offered for fresh
referee review, with no claim that both clauses are false.

## Review test and exclusions

The research pass has completed the assigned independent recomputation and
source-definition check. The next test is a fresh referee's review of the
finite counting certificate, exact root direction and logical scope against
the archived primary text. No manuscript or referee acceptance exists.
Do not return to the prior proposed joint-content induction as the main test:
the direct failure of clause (B) supersedes that stronger method claim.

The earlier three-letter total check and four-letter interlacing census
remain background finite observations. Their completeness and counts are
not used in the fixed-witness proof and have not been reaudited in this pass.
No global minimality, new rectangular theorem, or failure of (A) is claimed.
Historical registry comparison is inherited only as a summary; the underlying
registry is absent in this assigned project. The Ma--Pan DOI and institutional
AJQ PDF opens failed; no mathematical conclusion is drawn from those access
limits. The full archived arXiv v1 HTML is the decisive source for the claim.
