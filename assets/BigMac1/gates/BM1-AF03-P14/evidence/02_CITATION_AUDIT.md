# Citation and claim audit

Mode: search verification (strict academic precision)  
Document: `paper/main.tex`  
Cutoff: 2026-08-30 (release rerun)

## Pass 1: frozen extraction (no verification in this pass)

The following claim set was extracted from the complete manuscript before any
claim-by-claim citation verification.  Definitions, the manuscript's own
theorems, proof steps, methodology descriptions, and disclosure statements are
excluded under the skill's extraction rules.

| ID | Frozen claim | Type | Location |
|---|---|---|---|
| C01 | Ambrus and Gargyan conjectured that, for every `n>=2`, every locally extremal central section of `Q_n` is diagonal, as Conjecture 1.3. | attribution/existence | Introduction, first paragraph |
| C02 | Ambrus and Gargyan constructed non-diagonal critical central sections in every dimension at least four. | attribution/existence | Introduction, first paragraph |
| C03 | The selected Ambrus--Gargyan family consists of saddle points. | attribution | Introduction, first paragraph |
| C04 | Ambrus classified the critical directions of the four-cube; the sole non-diagonal orbit is `(1,1,2,2)/sqrt(10)`. | attribution/existence | Introduction, first paragraph; support section |
| C05 | For `3 <= k <= n-1`, the `k`-diagonal direction is not locally extremal. | attribution/existence | Introduction, second paragraph |
| C06 | Pournin's erratum corrects an omitted transverse term in the constrained-Hessian criterion for proper subdiagonals and leaves the main-diagonal conclusions unchanged. | attribution/existence | Introduction, second paragraph |
| C07 | Ball's sharp cube-slicing theorem makes `d_2` a global maximum. | attribution/existence | Introduction, second paragraph; support section |
| C08 | The five-dimensional case was previously unclassified. | temporal/existence | Introduction, before Theorem 1.1 |
| C09 | The release uses exact rational/algebraic certificates and no floating-point root as proof input. | existence | Introduction after Theorem 1.1; certificate section |
| C10 | The master audit runs the formula reconstruction, support/chamber verifiers, independent checks, and targeted corrupted-input tests. | existence | Certificate section |
| C11 | No Lean, Coq, Isabelle, or other interactive proof assistant was used. | existence | Computational disclosure |

Pass 2 is intentionally separated below and may not add new claims to this
frozen list.

## Pass 2: verification

Pass 2 used only the frozen IDs above.  External claims were checked against
the publisher/VOR or latest corrected preprint, DOI metadata, and the theorem
location itself.  Internal release claims were traced to the master log and
source tree.

### Summary

| Metric | Count |
|---|---:|
| Total frozen claims | 11 |
| Verified in the final manuscript | 11 |
| Numerical errors | 0 |
| Hallucinations | 0 |
| Misleading | 0 |
| Unverified | 0 |

Overall status: **PASS after one bounded-wording correction to C08**.

### Detailed findings

| ID | Status | Evidence and exact scope | Confidence/action |
|---|---|---|---|
| C01 | Verified | Ambrus--Gargyan 2024 VOR, pp. 2--3, definition (1.2) and Conjecture 1.3, including the quantifier `n>=2`. | exact; release wording now states the quantifier |
| C02 | Verified | Same VOR, p. 3, Theorem 1.2: for every `n>=4`, with all coordinates nonzero. | exact |
| C03 | Verified | Same VOR, Section 6, pp. 23--25: the selected `v_{n,2}(xi_n)` branch has increasing and decreasing directions. | paraphrase; manuscript deliberately says “selected family,” not all non-diagonal critical points |
| C04 | Verified | Ambrus 2022, Theorem 3: all `Q4` critical directions are diagonal or the signed-permutation orbit of `(1,1,2,2)/sqrt(10)`. | exact; latest arXiv v3 checked because older copies had Hessian errors |
| C05 | Verified | Ambrus--Gargyan 2025, Theorem 1.4 (VOR p. 3366): for every `n>=4` and `3<=k<=n-1`, the `k`-diagonal central section is not locally extremal. | exact |
| C06 | Verified | Pournin erratum, pp. 370--371: the constrained Hessian criterion omitted the transverse `-sqrt(n) V_{a_1}` term for proper subdiagonals; the paper explicitly says the main-diagonal results are unaffected. | exact; the full `3<=k<=n-1` conclusion remains attributed to Ambrus--Gargyan |
| C07 | Verified | Ball 1986, p. 465 abstract/theorem scope: every hyperplane section of the unit cube has volume at most `sqrt(2)`, sharply.  The `d2` section is a planar diagonal times a unit cube and has volume `sqrt(2)`. | exact |
| C08 | Verified after correction | Gate 2 searched the exact theorem wording, radical and minimal-polynomial fingerprints, arXiv math.MG corpus, DOI/citation indexes, author pages, public web, and GitHub.  No prior result was found, with recorded indexing and access limits. | Original categorical wording was replaced by the exact claim “the database-bounded search found no prior classification.” |
| C09 | Verified | Every decisive certificate in `audit/verification_log.json` is reconstructed with integer/rational or isolated quadratic-field arithmetic; discovery scripts are absent from the master command list. | exact internal trace |
| C10 | Verified | `audit/verification_log.json` has status `PASS`, 23 named checks, and no nonzero return code; it includes all support/chamber endpoints, independent audits, parser gates, and mutation suites. | exact internal trace; rechecked after the paper-only release delta |
| C11 | Verified | The release contains no `.lean`, `.v`, `.thy`, or `.agda` file; all proof reports consistently disclose exact CAS only. | exact repository trace |

### Authoritative sources

| Source | Official/primary URL | Used for |
|---|---|---|
| Ambrus, *Critical central sections of the cube* | https://doi.org/10.1090/proc/15955 ; https://arxiv.org/abs/2107.14778 | C04 |
| Ambrus--Gargyan, *Non-diagonal critical central sections of the cube* | https://doi.org/10.1016/j.aim.2024.109524 ; https://arxiv.org/abs/2307.03792 | C01--C03 |
| Ambrus--Gargyan, *Estimates on the decay of the Laplace--Polya integral* | https://doi.org/10.1112/blms.70157 ; https://arxiv.org/abs/2412.12835 | C05 |
| Pournin, erratum | https://doi.org/10.1007/s11854-025-0384-1 ; https://lipn.univ-paris13.fr/~pournin/LocalExtremaCorrigendum.pdf | C06 |
| Ball, *Cube slicing in R^n* | https://doi.org/10.1090/S0002-9939-1986-0840631-0 | C07 |
| Project Gate 2 and exact master audit | `literature/search_log.md`; `audit/verification_log.json` | C08--C11 |

No claim relies only on a search snippet or secondary source.  The DOI and
index searches were used for discovery and metadata reconciliation; the
mathematical scope was checked in the primary paper text.

## Release boundary

The release rerun did not turn C08 into an absolute priority claim.  It fixes
only a database-bounded not-found statement at the recorded cutoff; the exact
queries, index freshness, citation-graph omissions, and access limitations are
preserved in `literature/search_log.md`.  C09--C11 are release-internal claims,
so their evidence is the frozen source tree and exact audit logs rather than an
external publication.
