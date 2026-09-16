# Citation and bibliography audit: accept

Job: `win-00060-p02-release-7052b390769a`  
Evidence snapshot: `7f73e26f61f0bec41577a20ec5776d6c794c8616fb5f1344d69f7e609da0748d`  
Manuscript snapshot: `e1bba527f76bb2541d0fd5c4b584da42bd61c7e98e07bea6fc4e38ab896fc096`  
PDF: `9d359be47e9a78c487e3f3a916b1336218589bdf57a12955d4d7d1ea634932c8`

## Method and result

I used the required non-interactive two-pass procedure. The first pass froze
seven externally sourced claim/citation pairs in
`audit/citation-claim-ledger.json`; the second pass used only that ledger and
recorded claim-level source passages in `audit/citation-verification.json`.
All seven claims are verified (two exact, five faithful paraphrases). There
are no numerical errors, hallucinations, misleading claims, missing sources,
or unverifiable retained citations. Subagents were not used because this job
explicitly prohibited agents and other workers.

## Per-reference audit

| Key | Primary record and source location | Nearby support | Action |
|---|---|---|---|
| `Burman2010` | Erik Burman, *Ghost penalty*, publisher PDF, p. 1217 (abstract and Introduction), https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2010.10.006.pdf | Introduces the penalty for robustness independent of how the boundary cuts the mesh. | Metadata and DOI verified; retained unchanged. |
| `BurmanEtAl2015` | Wiley publisher page, Summary and Sections 2--4, https://onlinelibrary.wiley.com/doi/10.1002/nme.4823 | Provides the stated broad CutFEM context. Wiley's “How to cite” record confirms all five authors, 2015, volume 104, and pages 472--501. | Retained unchanged. |
| `BurmanHansboLarson2026` | Springer publisher page, Abstract and Introduction, https://link.springer.com/article/10.1007/s00211-025-01502-6 | Explicitly relates generalized stabilization kernels to finite-element spaces defined by discrete extensions. The publisher record confirms volume 158 (2026), pp. 249--280. | Retained unchanged. |
| `Wichrowski2026` | arXiv:2609.04067v1 and the checksum-bound local PDF. Printed p. 31, Eq. (57) and following paragraph; Appendix B, Eq. (60) and Proposition 5, printed pp. 36--38. https://arxiv.org/abs/2609.04067 | Eq. (60) matches the displayed form term-by-term. Proposition 5 proves the vanishing-cut lower bound; p. 31 explicitly leaves global sharpness open. | Retained unchanged; this is the closest prior result and problem-origin source. |
| `ZengEtAl2026` | Official SSRN record and Abstract, https://papers.ssrn.com/sol3/papers.cfm?abstract_id=7348478 | Supports only the nearby methods comparison: exact rational sign/Bernstein certificates in a parameterized Hermitian positivity problem. | Retained and changed to a direct body-flow `\cite{ZengEtAl2026}`; no bibliographic key change. |

No official record conflicted with the retained title, author, year, venue,
pagination, or DOI data, so no speculative BibTeX replacement was made.
There were no old-to-new key mappings.

## Coverage and user-library gate

The bibliography is not library-only. It includes the original ghost-penalty
paper, a primary CutFEM overview, a primary discrete-extension/stabilization
article, the exact problem-origin and closest-prior source, and one relevant
user-library methods comparison. The mathematical proof is self-contained:
its Gram identity, Schur complements, leading-minor signs, endpoint kernel
identity, and rank-one downdate are all derived in the manuscript, so no
uncited nontrivial external theorem is being imported. The bibliography is
therefore complete for the paper's actual dependencies without padding.

The active 49-row first-sheet registry and workbook hashes were checked.
Row 29 is the sole library entry directly sharing parameterized Hermitian
positivity and exact rational sign certification. A second library item would
not support another natural claim in this paper. The attempt-bound decision is
recorded in `audit/user-bibliography-selection.json` with citation attempt 1
and launch ID `3533dc6d-497a-403a-9656-efc519cff554`.

## Mechanical citation checks

The canonical bibliography is `manuscript/references.bib`. The skill checker
found five cited keys, five BibTeX keys, no missing or unused entries, and exact
agreement with the final `.aux`. The final log and `.blg` contain no undefined
citation, missing database entry, duplicate entry, or BibTeX warning.

Verdict: **accept**.
