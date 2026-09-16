# Fresh citation and claim verification report

Mode: search verification  
Document: `manuscript/main.tex` and `manuscript/references.bib`  
Checked: 2026-09-07  
Method: two-pass `$citation-check-skill` protocol plus primary-source manual
inspection and `$bib-reference-audit` consistency checks. The user prohibited
subagents, so all six keys were independently checked in this release context.

## Summary

The pass-1 set of 19 claims was frozen in
`audit/citation-claim-ledger.md` before verification. A later metadata-only TeX
edit added PDF title/author/subject/keywords and did not alter that claim set.
All 19 claims are verified; there are no numerical errors, missing citations,
misquotations, hallucinations, misleading claims, or unverified retained
claims. All six cited works exist and support their nearby statements. The
bibliography is neither user-library-only nor padded.

## Claim decisions

| Claims | Status | Evidence |
|---|---|---|
| C01, C02, C08--C10, C12--C16 | Verified (exact) | Direct displayed derivations and the two freshly rerun exact programs reproduce the 32/8 dimensions, both characteristic polynomials, eigenvalue ordering, and `4-2*sqrt(2)` gaps. |
| C03--C07, C19 | Verified (paraphrase/exact where numerical) | Greaves--Zhu, Conjecture 2, and Blanco v2, Example 4.7 and Section 5; Blanco's pp. 23--24 give the strict `(6,2)` value and Conjecture 5.1. Full-text search confirms no stated exact `(4,2)` evaluation. |
| C11 | Verified (paraphrase) | Terras, Part I contents explicitly include the DFT on `Z/nZ` and adjacency spectra of graphs over it. |
| C17 | Verified (exact attribution) | PeerJ title page/abstract identifies SymPy as a Python computer algebra system; bibliographic metadata match. |
| C18 | Verified (exact) | The SSRN primary abstract states the exact-rational/algebraic sign decisions and independent definition-level programs verbatim in substance. |

Detailed primary locations and URLs are recorded in
`audit/citation-source-locations.md`.

## Bibliographic-record audit

Six cited keys and six BibTeX entries were checked. Author, title, year,
venue/version, and DOI data match the primary records. The source-registry key
`Zeng2026SSRN7348478` is deliberately represented by the unique final key
`ZengEtAl2026`; no TeX key is missing. No replacement or key edit was necessary.

The mechanical audit reported one bibliography file, six cited keys, six
BibTeX keys, no missing or unused keys, and exact agreement with the final AUX
file. The final LOG/BLG scan found no undefined citations or references,
missing database entry, repeated entry, BibTeX warning, LaTeX error, fatal
error, emergency stop, undefined control sequence, or runaway argument.

## Coverage and limitations

The three natural primary sources for the generalized-pancake problem and its
closest conjectures are cited in ordinary prose. The elementary Fourier method
and the only software dependency have appropriate standard sources. The one
selected user-library work is relevant only to the carefully limited
verification-method comparison; the manuscript expressly says its programs
are corroborative. No novelty or priority claim is made. The SSRN item is a
preprint, and that status is shown in the bibliography. No source supports a
stronger result than the manuscript states.

