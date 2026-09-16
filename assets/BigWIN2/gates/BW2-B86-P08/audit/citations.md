# Citation and bibliography audit

Release job: `win-00086-p08-release-c24024c4e62f`  
Citation attempt: 1  
Launch id: `260d920c-c4bb-4b61-947e-47841d4201b1`  
UTC verification date: 2026-09-10

## Scope and method

The audit used two recorded stages.  Stage 1 extracted the ordinary body-flow
citation surface from `manuscript/main.tex` and froze six substantive
claim/citation pairs in `audit/citation-claim-ledger.json`.  Its key union is
exactly

```
CroftFalconerGuy1991
Georgiou2026
Leech1950
ZengEtAl2026Certificates
```

Stage 2 treated that list as fixed and checked each source's existence,
identity, version or date, exact nearby passage, hypotheses, and support.
Searches used the academic-citation templates (author/year/title, full title,
author/year/venue, DOI, and arXiv id where applicable) and then inspected the
primary publisher or repository text.  Exact locators and the per-claim record
are in `audit/citation-verification.json`.  The user forbade subagents for this
bounded release job, so the release worker performed the checks sequentially.

## Claim-level results

| Claim | Keys | Status | Primary support |
|---|---|---|---|
| C01 | `CroftFalconerGuy1991` | Verified (paraphrase) | Springer confirms the 1991 book identity and DOI; the searchable book scan locates B22, “Polyhedra with congruent faces,” on p. 75; Georgiou Section 1 reproduces the triangular question and cites that page. |
| C02 | `Georgiou2026` | Verified (paraphrase) | arXiv:2608.01109v1, abstract and Theorems 1–2, explicitly settle universal realization and exact minimum face count when reflections are allowed. |
| C03 | `Georgiou2026` | Verified (paraphrase) | Remark 3 gives four direct and four mirror-image facets; Section 4 identifies right and obtuse scalene triangles as the remaining orientation-preserving case. |
| C04 | `Georgiou2026` | Verified (paraphrase) | Remark 3 uses cyclic side order relative to the outward normal and reversal to distinguish direct from mirror copies, exactly matching the manuscript convention for scalene facets. |
| C05 | `Leech1950`, `Georgiou2026` | Verified (paraphrase) | Georgiou's Lemma 5 gives the disphenoid coordinate identities and cites Leech; Cambridge's primary record and extract confirm Leech's equal-opposite-edge isosceles tetrahedron. |
| C06 | `ZengEtAl2026Certificates` | Verified (paraphrase) | Preprints.org v1, abstract and Section 6, documents exact finite enumerations in discrete geometry and replayable standard-library/independent exact verifiers. |

No claim was numerically rounded, contradicted, misleading, or unsupported.
The dated search for a later equivalent oriented-link result found none; that
bounded absence is expressly not a claim of priority.

## Bibliographic identity and coverage

All four bibliography records match the inspected primary records in title,
author identity, year/date, venue or repository, and DOI/arXiv identifier.
No BibTeX replacement or citation-key change was needed.  The canonical
bibliography has no missing or unused entry.

Coverage is appropriate to the manuscript's actual claims:

- Croft–Falconer–Guy is the problem origin.
- Georgiou is the closest primary result and the source of the precise open
  remainder, direct/mirror convention, and four-face comparison.
- Leech is the historical source for the equal-opposite-edge tetrahedron.
- Zeng–Liu–Ratnavelu–Huat is the one natural active user-library record for
  the ancillary exact-enumeration/replayable-verifier practice.

Thus the bibliography contains natural non-library primary sources in normal
body flow, is not Excel-only, and contains no decorative entry.  Screening all
49 active first-sheet library records found no honest second selection; adding
one would be padding.  The attempt-bound selection is recorded in
`audit/user-bibliography-selection.json`.

## Mechanical checks

The bibliography checker found four cited keys, four BibTeX entries, no missing
key, no unused entry, and exact agreement with the four `\bibcite` keys in the
final AUX file.  The converged LaTeX/BibTeX logs contain no undefined citation,
undefined reference, missing database entry, repeated entry, warning, fatal
error, overfull box, or underfull box.

Verdict: **accept**.
