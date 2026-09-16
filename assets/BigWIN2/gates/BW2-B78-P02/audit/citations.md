# Citation and bibliography audit

Release job: `win-00078-p02-release-382a564d0f4a`  
Citation attempt: 1  
Launch id: `28bf2997-5c23-4066-9624-adc0e8425577`  
UTC verification date: 2026-09-10

## Scope and method

The audit used two separate stages. Stage 1 extracted the ordinary body-flow
citation surface from `manuscript/main.tex` and froze four substantive
claim/citation pairs in `audit/citation-claim-ledger.json`. Its key union is
exactly

```
brehm-fiedler-2018
kuhrs-telek-vassena-2026
mochizuki-fiedler-2015
zeng-liu-ratnavelu-ong-2026
```

Stage 2 treated those claims as fixed and checked each source's existence,
identity, date or version, exact nearby passage, hypotheses, and support.
All applicable academic search templates were run: author/year/title,
full-title, author/year/venue, DOI, and arXiv identifier. Verification then
used the primary publisher, arXiv, or Preprints record and inspected full text.
The per-claim locators and bibliographic identity record are frozen in
`audit/citation-verification.json`. The user explicitly prohibited subagents
for this bounded release job, so the release worker performed the checks
sequentially.

## Claim-level results

| Claim | Keys | Status | Primary support |
|---|---|---|---|
| C01 | `mochizuki-fiedler-2015`, `brehm-fiedler-2018` | Verified (paraphrase) | The ScienceDirect paper introduces structural sensitivity analysis and identifies its mathematical formulation with the augmented A-matrix of Eq. (8). The Wiley paper extends the same stoichiometry-based steady-state sensitivity program to regular multimolecular systems. Kuhrs--Telek--Vassena Eq. (25) also expressly attributes the introduction of this matrix to these two works. |
| C02 | `kuhrs-telek-vassena-2026` | Verified (paraphrase) | arXiv:2609.05100v1 treats `A=[R|C]` as the associated layered mixed matrix; Theorem 3.23 characterizes a nonzero inverse sensitivity by reachability in the influence graph. |
| C03 | `kuhrs-telek-vassena-2026` | Verified (paraphrase) | Remark 3.6 expressly says classical mass action is not parameter-rich and therefore imposes additional algebraic constraints on the equilibrium Jacobian requiring further analysis. |
| C04 | `zeng-liu-ratnavelu-ong-2026` | Verified (paraphrase) | Preprints.org version 1, Sections 3 and 6, records symmetry-orbit reduction, JSON certificates, from-scratch reconstruction of the finite objects and symmetry action, and a separate independent exact implementation. |

No frozen citation claim was contradicted, misleading, numerically rounded, or
unsupported. The manuscript makes no literature-priority or open-status claim
for its newly frozen finite census.

## Bibliographic identity and coverage

All four bibliography records match the inspected primary records in title,
author identity, year or version date, venue or repository, pagination where
applicable, and DOI or arXiv identifier. No BibTeX replacement and no citation
key change was needed.

Coverage follows the manuscript's actual dependencies:

- Mochizuki--Fiedler and Brehm--Fiedler are the primary structural-sensitivity
  sources for the augmented-matrix program.
- Kuhrs--Telek--Vassena is the problem source and closest result: the
  independent-symbol inverse pattern and the explicit mass-action limitation.
- Zeng--Liu--Ratnavelu--Ong is the one natural active user-library paper for the
  ancillary exact-enumeration and independent-reconstruction comparison.

Thus natural non-library primary literature appears in ordinary body flow; the
bibliography is neither user-library-only nor padded. All 49 active first-sheet
library records were screened. Row 9 is the strongest complete match for the
single ancillary methodology sentence, while a second library citation would
not support a distinct premise. The exact attempt-bound selection is recorded
in `audit/user-bibliography-selection.json`.

## Mechanical checks

The bibliography checker found four cited keys and four BibTeX entries, with no
missing or unused entry and exact agreement with the final AUX file. The
converged LaTeX/BibTeX logs contain no undefined citation or reference, missing
database entry, repeated entry, warning, fatal error, overfull box, or underfull
box. The union of direct keys in the claim ledger exactly equals the ordinary
body-flow citation-key set.

Verdict: **accept**.
