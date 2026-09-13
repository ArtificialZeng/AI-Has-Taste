# Fresh citation audit

Release job: `bigMac-00011-p02-release-8e7a7826a299`  
Search date: 2026-09-07  
Method: `citation-check-skill` v2, search mode, two separate passes.  
Bound PDF: SHA-256 `f1561ebd6cb8af5486dd854ca5544d1f49567b0214ba6d35f9a5509f06e9a8d6`.

## Scope and dependency completeness

Pass 1 is fixed in `audit/citation_claims.md`; it contains 18 extracted
attribution, existence, comparison, temporal, and numerical claims.  This
report is pass 2 and does not add or redefine claims.  I read both authored
dependencies listed by `publication.json`, checked the citation keys against
the final `.aux`, `.bbl`, `.blg`, compiler log, and extracted PDF, and checked
the complete six-page rendered PDF.  `main.tex` imports no authored TeX,
figure, style, or data file beyond `references.bib`, so the sorted dependency
scope is exactly:

1. `manuscript/main.tex`
2. `manuscript/references.bib`

All three cited keys resolve to three human-readable bibliography entries.
There are no undefined citations and no unused local publication dependency.

## Pass 2: claim-by-claim verification

| ID | Status | Verification |
|---|---|---|
| C01 | Verified (frozen mathematics) | It is the exact accepted `resolution-paper` scope in `claim.json`; `audit/math.md` audits all 32 labeled cases. The manuscript neither enlarges nor weakens it. |
| C02 | Verified (paraphrase) | Baek--Hwang--La--Yang v1, Definition 5.2, defines the additive level sort by starting prefix weight, increasing level, and scan-direction ties. |
| C03 | Verified (exact) | The displayed set has exactly 16 distinct admissible pairs; two tie labels give exactly 32 triples. |
| C04 | Verified (paraphrase) | Baek--Hwang--La--Yang v1, Definition 3.1, requires a partial ambient map to be defined and agree on every point of the specified domain while leaving behavior outside it unconstrained. |
| C05 | Verified (paraphrase) | The official arXiv record for Bojanczyk 2018 gives four machine/program characterizations of polyregular functions. The official arXiv and Dagstuhl records for Bojanczyk--Kiefer--Lhote 2019 state that string-to-string MSO interpretations are exactly polyregular functions. |
| C06 | Verified (frozen mathematics) | The identity is proved directly in Lemma 2 and accepted in `audit/math.md`; no external attribution is made. |
| C07 | Verified (frozen mathematics; exact count) | Lemma 3 gives the one-copy MSO order and the accepted audit checks its use in every zero-weight case; the table contains exactly 20 `PR` labels. |
| C08 | Verified (paraphrase) | Baek--Hwang--La--Yang v1, Theorem 3.8 gives regular inverse-image closure, Theorem 3.12 states the linear-growth collapse, and Proposition 5.6 applies exactly this chain on a regular two-parameter slice. |
| C09 | Verified (paraphrase) | Proposition 5.6 of the cited v1 paper is explicitly the two-pyramid regular-pullback criterion and has the same linear-growth proof pattern. |
| C10 | Verified (frozen mathematics) | The manuscript supplies the standard pumping witnesses; the accepted audit checks the direction of pumping and the fixed-lower-bound restriction. |
| C11 | Verified (frozen mathematics) | The accepted audit reconstructs both closed forms and probes. The exact-integer regression independently rechecked all 6,400 pairs. |
| C12 | Verified (frozen mathematics) | The accepted audit checks both thresholds; the exact-integer regression rechecked every pair with `1<=m,n<=160`. |
| C13 | Verified (frozen mathematics) | The accepted audit checks both thresholds and boundary regimes; the same exact regression rechecked the stated range. |
| C14 | Verified (frozen mathematics; exact count) | The accepted audit checks negation transport and counts the six representatives plus six transported cases. |
| C15 | Verified (paraphrase) | The cited v1 paper gives Definition 5.2, Proposition 5.6 and the right-to-left height-sweep lower bound, and Open Problem 11(4) asks which additive level sorts are polyregular while noting the `(1,1)` identity. |
| C16 | Verified (bounded comparison) | The cited source leaves precisely the broader classification open; the accepted audit verifies the bounded additions. The manuscript makes no priority claim and expressly excludes weights outside the finite family. |
| C17 | Verified (exact) | Fresh execution of `evidence/verify_mixed_sign.py` returned `height_formula_pairs=6400`, `suffix_probe_pairs=25600`, and `integer_sorting_only=True`. |
| C18 | Verified (exact metadata) | Official arXiv records confirm all three arXiv identifiers, author lists, titles, initial years, and primary classes; Dagstuhl independently confirms the 2019 ICALP paper and DOI `10.4230/LIPIcs.ICALP.2019.106`. |

No extracted claim is contradicted, numerically discrepant, misleading, or
unverified.  The mathematical statuses above mean consistency with the
accepted frozen mathematical audit and replayable exact evidence; citation
checking is not offered as a second proof review.

## Primary sources checked

- Baek, Hwang, La, and Yang, *A Computational Obstruction to Swapping Area
  and Dinv: An Automata-Theoretic View of the q,t-Catalan Symmetry*,
  arXiv:2609.05005v1, especially Definitions 3.1 and 5.2, Theorems 3.8 and
  3.12, Proposition 5.6, the height-sweep lower bound, and Open Problem 11(4):
  <https://arxiv.org/html/2609.05005v1>.
- Mikołaj Bojanczyk, *Polyregular Functions*, arXiv:1810.08760:
  <https://arxiv.org/abs/1810.08760>.
- Mikołaj Bojanczyk, Sandra Kiefer, and Nathan Lhote,
  *String-to-String Interpretations with Polynomial-Size Output*,
  arXiv:1905.13190 and ICALP 2019:
  <https://arxiv.org/abs/1905.13190> and
  <https://doi.org/10.4230/LIPIcs.ICALP.2019.106>.

## User bibliography check

I inspected `literature/user_bibliography_check.md`.  Its sole Excel-listed
item is Zijian Zeng's Rule 115 cellular-automaton preprint.  The check file
limits its possible use to a methodological comparison about finite-state
certificates and explicitly says that it supports neither polyregularity nor
an additive-level-sort lower bound.  The present paper makes no such
methodological comparison, so inserting that citation would be misleading;
it is therefore honestly omitted.  Direct SSRN/DOI pages were not reachable
through the bounded web endpoint, but that optional, uncited metadata access
limit does not affect any manuscript attribution or bibliography record.

## Verdict

**Accept.**  The citations exist, their metadata and nearby uses are
supported, the prior-work comparison is conservatively bounded, all keys are
defined, and the declared publication dependency scope is complete.

