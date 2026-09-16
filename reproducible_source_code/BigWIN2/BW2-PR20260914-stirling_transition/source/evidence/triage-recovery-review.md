# Recovery triage decision and verification

Job: `primary-20260914-stirling-transition-triage-65861bc877d9`.
Date: 2026-09-14. Decision: **advance** one bounded research pass.
Workflow: candidate_kind=none; original_status=unresolved.

The supervisor's recovery note reports that the preceding triage was interrupted
before its structured result was committed. Its proposed decision is not treated
as acceptance. The present decision follows the checks below. No manuscript or
mathematical candidate is produced.

## Inputs and source checks

Enumerated `literature/*handoff*.md`: the only match was
`literature/outer-intake-handoff.md`; read it in full. Also read the specifically
relevant `literature/triage-operational-recovery-20260914T1120.md`, `screen.md`,
and all five match statements in `dedup.json`. They concern 3D pattern
avoidance, graph cycle covers, or Johnson graph spectra, not the present
fixed-column counts. External corpus completeness and conversation dedup were
not rerun. No global novelty or duplicate-exclusion claim follows.

The frozen source hash, both HTML capture hashes, and the retained reduction,
script and output hashes match the supplied receipts; see the fresh JSON.
No predecessor evidence file was rewritten. `source.md` remains byte-for-byte
unchanged.

Live primary reinspection on 2026-09-14:

- [Liang–Sagan published PDF](https://users.math.msu.edu/users/bsagan/Papers/Old/lclc%20-%20pub.pdf),
  printed p.31, Section 8.2, Conjecture 8.8 (PDF page index 30, extracted
  lines 1288–1294): the same fixed-k sign transition and reported tests through
  100. Printed p.23, Theorem 7.2 (index 22, lines 853–856) concerns the
  second-kind numbers S(n,k), not this first-kind assertion.
- [arXiv version history](https://arxiv.org/abs/2408.02782), submission-history
  lines 24–27: only v1, dated 5 August 2024, is listed. The retained authentic
  [v1 HTML](https://arxiv.org/html/2408.02782v1) was inspected at Conjecture 8.9
  and agrees with the published assertion.
- The retained authentic [Salas v1 HTML](https://arxiv.org/html/2607.04217v1)
  was inspected at Theorems 1.4 and 1.5, equations (1.14) and (1.16).
  These compare fixed rows and whole row-polynomial products, respectively.
  A coefficient of a product is a convolution, so direct coefficient extraction
  does not give the individual D_k. This rejects that immediate deduction,
  without ruling out every possible transformation.

The earlier survey and its access limits are retained in
`literature/triage-review.md`. This job additionally searched
`"Stirling" "Liang" "Sagan" "conjecture" transition` and
`"elementary symmetric" "ratio" "supermodular"`; snippets were only leads.
No inspected resolution was found. Source status remains **open-supported in
the inspected literature**; the ratio lemma's novelty is unverified. A complete
literature resurvey was not needed for this recovery decision.

## Conditional reduction checked directly

Write q(n)=c(n,k-1)/c(n,k) for n>=k>=1. Positive support makes every
denominator positive. The recurrence gives

    c(n+1,k)/c(n,k) = n+q(n),
    D_k(n)/(c(n-1,k)c(n,k)) = q(n-1)-q(n)-1  (n>=k+1).

Assume L: q(n)-2q(n+1)+q(n+2)>=0 for every n>=k.
Then d_n=q(n)-q(n+1) is nonincreasing. The set
J={j>=k: d_j<1} is nonempty: otherwise telescoping would yield
q(k+t)<=q(k)-t<0 for a sufficiently large integer t, whereas q is
nonnegative. Let j0=min J and N_k=j0+1. For k+1<=n<N_k,
d_(n-1)>=1, so D_k(n)>=0. For n>=N_k, monotonicity gives
d_(n-1)<=d_j0<1, so D_k(n)<0. Finally D_k(n)=0 for n<k
and D_k(k)=1. Thus L implies the entire frozen assertion, including a
negative tail and correct treatment of equality. The k=1 case also satisfies
this argument, with q=0.

Only this implication is established. No converse or necessity result is
claimed; in particular, a counterexample to L alone would not refute the source
assertion. This is the precise interpretation of the corresponding caution in
the archived reduction.

With A=c(n,k), B=c(n,k-1), C=c(n,k-2), E=c(n,k-3), the cleared numerator
in equation (2) of `evidence/ratio-reduction.md` is exactly correct: a fresh
symbolic expansion leaves residual zero. This verifies an identity, not its
sign. Row log-concavity gives B^2-AC>=0; it does not by itself justify all
remaining cubic terms.

## Exact checks and limits

Run `python3 evidence/triage_recovery_check.py`.
The fresh output `evidence/triage_recovery_check.json` records:

- Consistency of all 150 retained sign words and their summary fields; their
  complete large rectangle was not recomputed in this job.
- Fresh exact recurrence replay: 1600 D values, 1<=k<=20 and 1<=n<=80,
  match the retained data; 1370 ratio second differences, k<=n<=78 in these
  columns, are nonnegative; 1390 exact rational checks confirm the D identity.
- Independent enumeration of every permutation for 0<=n<=7 (5914 total)
  reproduces the small rows. This is a combinatorial check, not a fresh referee.
- Symbolic numerator expansion agrees identically, using SymPy 1.14.0.

The previous 150000 D checks and 138525 ratio checks remain attributed to the
previous job. None of the finite checks proves any infinite threshold.
An optional HTML parser import failed because `bs4` is absent; standard-library
text extraction sufficed. This is a tooling fact, not a mathematical obstacle.

## Admission rationale and one next test

Nearest prior result X: a published transition conjecture with finite tests,
alongside different row and second-kind column theorems. Proposed delta Y:
a uniform sign-persistence theorem obtained from L, or an exact contrary sign
reversal for the source. Verification route Z: the checked conditional
reduction, exact arithmetic, and a universal symmetric-function inequality.
The delta is substantial if proved; neither small-k calculations nor a larger
finite table alone would qualify.

One next test: prove or refute nonnegativity of the explicit numerator (2)
for A=c(n,k), B=c(n,k-1), C=c(n,k-2), E=c(n,k-3), all n>=k>=1,
using applicable Newton/Toeplitz inequalities. A proof establishes L and hence
the source assertion; an exact negative instance rejects only this stronger
route. The test is admitted for one bounded research pass, not certified.
