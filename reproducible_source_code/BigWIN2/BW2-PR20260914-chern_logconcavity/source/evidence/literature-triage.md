# Literature and scope triage

Job: primary-20260914-chern-logconcavity-triage-b02871487deb.
Retrieved/inspected 2026-09-14 (UTC), within this job.

## Inspected primary evidence

- Bérczi–Fehér, [arXiv HTML v1](https://arxiv.org/html/2605.25271v1),
  local full capture `literature/2605.25271v1.html`. Live HTML opened;
  local Sections 3 and 5 read, including their proofs. Definition 3.1
  and Conjecture 3.3 agree with the frozen statement. Theorem 3.7 covers
  j=0 log-concavity, Theorem 5.4 covers j=1; Theorem 5.2 covers j=2
  positivity. Section 1.2 and the discussion before Section 2 explicitly
  leave higher log-concavity modes unresolved. Equation (3.3) supplies
  the independent coefficient computation; Lemma 3.5 supplies the
  fixed-defect recurrence. Remark 3.8 rules out the general
  real-rootedness route already at k=2,j=1.
- [Current arXiv abstract](https://arxiv.org/abs/2605.25271), submission
  history inspected live: only v1, dated 24 May 2026, was listed.
- Primary Figure 1 was inspected directly in the captured SVG/HTML,
  now excerpted verbatim in `evidence/primary-figure1.html`. It labels
  GPT's log-concavity case j=1 and Co-Mathematician's j=2, whereas the
  formal statements/proofs and introduction assign j=0 and j=1.
  Thus the discrepancy is in the primary document itself. No j=2
  proof was found in the inspected primary sections. Do not use the
  figure alone to claim a theorem or dismiss its priority risk.
- Shivam Patel, [MathDB contribution](https://mathdb.com/p/374934/rank-two-binomial-positivity-conjecture-for-schur-coefficien),
  solution headed “Proof for every Schur index,” beneath the progress
  summary; author shown at the end. Full live contribution and the
  supplied `literature/prior-positivity-mathdb.html` were read. It claims
  all-j positivity and lower support bounds, using the all-index
  recurrence, the palindromic boundary A_{2j-1,j}=0, and multiplication
  in the Newton basis. It does not prove log-concavity. Its recurrence
  follows by extracting coefficients from E_d(T,u)=(T+d)E_{d-1}(T+u,u);
  the support argument is a prior proof claim, not a new contribution
  or an independent referee acceptance here. Live content confirms the
  handoff; stale search snippets incorrectly omit the posted solution.

## Current search and comparison

Queries included `"2605.25271" log concavity`, the author names with
`"binomial" "log-concavity"`, `"Rank-two binomial log-concavity"`,
`"Shivam Patel" "positivity" "B_{k"`,
`"binomial log-concavity" "Schur" proof`, and
`"2605.25271" "j=2" "log"`. Results led back to the primary paper,
mirrors/reviews, and MathDB. No later equivalent resolution of the
full conjecture was found in these searches on this date. This is
limited negative search evidence, not a priority guarantee.

The sole project-local handoff was enumerated and read:
`literature/outer-intake-handoff.md`. Its scope warning, positivity
claim and figure lead were independently checked as above. No registry
or dedup artifact is present inside this project; the handoff's 2,883
and 684 record counts and inaccessible-conversation comparison were
not reverified. Historical duplicate clearance remains incomplete.
The j=2 restriction is explicitly contained in the frozen all-j
conjecture and overlaps the paper's claimed open range; it is not a
separate reformulation of positivity or ordinary value log-concavity.

## Decision and verification route

Source status: **open-supported** for the higher-mode assertion, with
the documented primary-figure inconsistency. Suitability: **advance**
to one bounded method test, not mathematical acceptance. The natural
potential delta is all-k log-concavity for j=2 beyond Theorem 5.4.
Neither a new theorem nor a novelty claim is established in triage.

Exact product/Newton calculations agree with a separate implementation
of (3.3) at 19,363 integer evaluations. All 289 rows through k=32 have
interval support and nonnegative coefficients; all 6,088 strictly
interior minors are positive (`exact-triage.json`). This is a finite
observation only.

The cheapest direct certificate extension was also tested. Expressing
B_{k,2,r} in D(r+i,k-2), -4<=i<=1, agrees with 1,073 exact coefficients.
The unmodified trace/Abel-prefix sufficient condition fails: 499 of
12,378 active prefixes tested are negative. The first is k=4,r=4,
trace -1, pair (-1,0), prefix -946, multiplying a positive Abel
difference 6. Yet the actual minor is 212^2-27*660=27124>0.
This rejects that particular sufficient certificate, not the conjecture
or every permutation-based proof. Reproduction: run
`python3 evidence/exact_triage.py`, then
`python3 evidence/j2_prefix_probe.py`.

**One next test:** use one additional application of Lemma 3.5 to rewrite
the j=2 expansion with common defect k-3, and test all active trace/Abel
prefixes for 5<=k<=32 (k=4 already has its complete exact row). Any
negative active prefix rejects this revised certificate; a finite pass
would justify deriving the symbolic support-dependent coefficient
inequalities, but would not prove them.
