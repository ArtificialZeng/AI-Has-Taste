# Fresh citation and bibliography audit

Job: `win-00056-p02-release-8bf7998fc25c`  
Search date: 2026-09-07  
Method: two-pass search verification using primary records and direct source text;
serial review was required by the explicit no-agent job constraint.

## Result

**Accept.** The extraction-only ledger is
`audit/citation-claim-ledger.md`; the independent fixed-ledger verification and
exact locators are in `audit/citation-source-verification.md`. All three cited
keys are defined, used in ordinary body flow, present in the final `.aux`, and
supported by their nearby claims.

| Key | Current and official title | Primary source and locator | Support | Action |
|---|---|---|---|---|
| `FasiHashemi2026` | *Conditioning of solutions to the Sylvester equation* | arXiv record `2609.04050v1`; local hash-bound PDF, Example 6 and Figure 3, printed pp. 21--22 | exact: same four matrices, 30 values, and empirical orders; no exact constants or remainder bounds there | verified; retained |
| `Zeng2026ConvexLens` | *Fixed Convex-Lens Spectral Constants: Möbius Reduction, Sharp Model Theorems, and Angle-Dependent Bounds* | Preprints.org primary page, abstract and Section 1/Theorems 1--7 | paraphrase: a distinct spectral-set problem uses exact constants and finite-dimensional exact certificates | verified; retained; selected library row 13 |
| `StewartSun1990` | *Matrix Perturbation Theory* | Academic Press, 1990, Theorem IV.4.11 | exact singular-value perturbation inequality used in the proof | locator sharpened; entry retained |

Metadata differences requiring replacement: none. Citation-key changes: none.
`manuscript/references.bib` contains exactly the three cited entries; none is
unused, missing, duplicated, decorative, or unverifiable. The bibliography is
not library-only: it contains the primary problem paper, the natural matrix-
perturbation reference, and one directly relevant library analogue.

The active 49-record first-sheet registry and source snapshot were hash checked.
`audit/user-bibliography-selection.json` validates against the supplied schema
and is bound to citation attempt 1 and launch ID
`4a11079a-5f8a-4f41-980f-559569c9ffff`. Row 13 is the only retained library
item because a second entry would be less direct and would pad the bibliography.
The selected final key appears in an ordinary direct `\cite{Zeng2026ConvexLens}`.

The mechanical BibTeX check reports three cited keys, three `.bib` keys, no
missing or unused entries, and exact agreement with the final `.aux`. The final
build log and `.blg` contain no undefined citations/references, missing database
entries, duplicate entries, BibTeX warnings, LaTeX errors, or fatal diagnostics.
No source-access or claim-support blocker remains.
