# Verification Report

**Mode:** Search verification with local primary-document replay  
**Document:** `manuscript/main.tex` and `manuscript/references.bib`  
**Generated:** 2026-09-08  
**Release job:** `win-00071-p01-release-74f5b2e2a4db`  
**Citation attempt / launch:** `6` / `d2e76aca-aec7-4e48-9724-bef8bdba4cfe`

## Summary

| Metric | Count |
|---|---:|
| Fixed citation claims | 5 |
| Ordinary body-flow citation keys | 4 |
| Verified claims | 5 |
| Numerical errors | 0 |
| Unverified claims | 0 |
| Hallucinations or misleading claims | 0 |

**Overall status: PASS.** The frozen ledger's key union exactly equals the
ordinary body-flow citation set. All retained citations have a real nearby use,
and all five claim pairs are supported by primary text or, for the bounded
search statement, by the primary source together with the frozen search record.

## Pass 1: fixed claim surface

`audit/citation-claim-ledger.json` was extracted before verification. It binds
five uniquely located claims to the canonical manuscript and bibliography, the
accepted mathematical snapshot, this release job, citation attempt 6, launch
UUID, and the current manuscript-snapshot digest. The four-key union is exactly:
`BrandtLickorishMillett1986`, `KoseleffPecker2010`, `Shoji2026`, and
`Zeng2026MultiplicityArxiv`. There is no `\\nocite`, custom citation macro,
verbatim citation, hidden conditional, or comment-only key.

## Pass 2: independent source verification

| Claim | Key | Primary source and exact locator | Status |
|---|---|---|---|
| CIT-01 | `BrandtLickorishMillett1986` | Springer version-of-record page for DOI `10.1007/BF01388747` confirms all metadata. Shoji's official v1 PDF, printed p.3, Section 2.1, reproduces the displayed normalization and Laurent-polynomial codomain while citing Brandt--Lickorish--Millett and Ho. | Verified (paraphrase) |
| CIT-02 | `KoseleffPecker2010` | Original *Fibonacci Quarterly* PDF, printed pp.137--138, Section 2, especially p.138 before Proposition 2.2, defines the all-one Conway family as Fibonacci knots or links and gives its Schubert fraction as `F_{j+1}/F_j`. | Verified (exact) |
| CIT-03 | `Shoji2026` | Official arXiv:2609.05200v1 PDF, Proposition 4.3 on printed pp.9--11 and Remark 4.5 on printed p.11, gives the even result and explicitly says the `2n+1` analogue has only small checks and no complete proof. | Verified (exact) |
| CIT-04 | `Shoji2026` | Official v1 PDF, Figure 5 and Proposition 4.3 on printed pp.9--11; `literature/triage.md` and `literature/research.md` preserve the bounded search. The manuscript explicitly disclaims exhaustive priority. | Verified (paraphrase) |
| CIT-05 | `Zeng2026MultiplicityArxiv` | Official arXiv:2608.18179v1 PDF, Section 4, printed p.4, final paragraph, says the exact edge-subset implementation and direct small-order checks are diagnostic only and not used in the proof; printed p.5 repeats that no computational output is a premise of Theorem 1.1. | Verified (exact) |

The machine-readable verification details are in
`audit/citation-source-verification.json`. The applicable first-author/year/title,
full-title, author/year/venue, DOI, and arXiv-ID query templates were freshly
replayed on 2026-09-08. The exact supporting passages were then checked against
the original *Fibonacci Quarterly* PDF, the two official arXiv v1 PDFs, and the
Springer version-of-record metadata. No conflicting primary record was found.

## User-library selection and bibliography coverage

The active checksum-bound first-sheet registry has 49 records. All records were
screened for actual claim-level relevance. Row 17,
*Multiplicity-Isolated Cores and Chromatic Symmetric Reconstruction of Trees*,
is selected in `audit/user-bibliography-selection.json` and cited directly in
the verification disclosure. Its official arXiv text supports the exact nearby
methodological comparison. Only one library record is retained because no second
record naturally supports another claim actually made by this manuscript; adding
one would be redundant or decorative.

The bibliography is not library-only. It naturally includes the non-library
primary source for the Q-polynomial, the original journal source for the
Fibonacci-link description, and Shoji's problem source and closest theorem.
The proof imports no further nontrivial external theorem: its transfer,
Chebyshev identity, sign grid, degree count, and cancellations are derived in
full. No retained reference is decorative.

## Bibliography and build diagnostics

The canonical BibTeX file contains exactly the four cited entries. Official
records confirm their authors, titles, years, venues or repository versions,
and identifiers; no key changed in this attempt. The bibliography checker found
four cited keys, four database keys, no missing or unused entries, and exact
agreement with `main.aux`. A clean attempt-6 rebuild converged to the four-page
PDF frozen in `audit/manuscript-snapshot.json`. The final `main.log` and
`main.blg` contain no
undefined citation/reference, missing database entry, repeated entry, BibTeX
warning, LaTeX error, fatal error, emergency stop, undefined control sequence,
or runaway argument. Subagents were not used because this bounded job expressly
forbade them.
