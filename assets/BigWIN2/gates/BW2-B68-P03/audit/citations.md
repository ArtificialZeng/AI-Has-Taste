# Verification Report

**Mode:** Search, with a separate frozen extraction and verification pass.  
**Document:** manuscript/main.tex and manuscript/references.bib.  
**Date:** 2026-09-08. **Citation attempt:** 2.  
**Overall status:** PASS after correcting one source-description error.

| Metric | Count |
|---|---:|
| Final extracted claims | 19 |
| Verified within their stated scope | 19 |
| Ordinary body citation instances | 7 |
| Distinct cited references | 6 |
| Unresolved citation/coverage defects | 0 |
| Initially misleading claims, repaired | 1 |

The extraction was frozen before source verification. Inspection found that source equation (3.15) has 18 summands, whereas the manuscript called it a fourteen-summand formula. Its four multipliers divisible by 16 disappear in the frozen implementation. The manuscript now explicitly describes this reduction and numbers its 14 survivors. The revised extraction was frozen as round 2 and the affected statements were checked again against the original formula and frozen code. No mathematical input or accepted scope changed. The final ledger and verification JSON record all 19 claims individually.

| Claim | Direct keys | Exact support and result |
|---|---|---|
| CIT-001 | Andrews1984GFP | Official AMS record confirms the memoir; the original attribution/convention is explicitly reproduced in the cited Cui--Gu--Tang research manuscript, pp. 1-2. Verified paraphrase. |
| CIT-002 | CuiGuTang2024; CuiGuTang2025 | Publisher abstracts describe the constant-term and integral-coefficient constructions. Author-hosted originals corroborate this scope. Verified paraphrase. |
| CIT-003 | DasNathSarma2026 | Official versioned HTML, Theorems 1.2-1.3 and Conjecture 5.1; all moduli and affine progressions match. Verified exact attribution. |
| CIT-004 | Andrews1998Partitions | Original book scan/OCR, Chapter 2, displayed Theorem 2.8, equation (2.2.10), p. 21. NIST DLMF 17.8.1 supplies a clean equivalent formula. The manuscript specialization is an explicit algebraic inference. |
| CIT-005 | DasNathSarma2026 | Equation (3.15), all 18 source terms compared with the 14 retained modulo-16 tuples in the frozen code. Corrected and verified. |
| CIT-006 | ZengEtAl2026Finite | Version 1 abstract and Section 7 explicitly distinguish finite-library theorems from their ambient open problems. Only this methodological distinction is cited. |
| CIT-007 | DasNathSarma2026 | Equation (3.15), source positions 8, 10, 11, 15 have coefficients divisible by 16. The stated survivor ordering agrees with the frozen audit. |

The 12 additional scope, mathematical and computational claims are mapped individually in `audit/citation-verification.json`. The finite vectors and all 505 predicted section coefficients were replayed read-only; row-length minima were recomputed exactly. The accepted referee report, frozen dissection evidence and explicit elementary algebra support the remaining proved statements. Historical search/discovery statements are checked against the frozen record, not treated as proof of priority. Neither the stronger identity nor the original conjunction is proved here.

## Bibliographic correctness and coverage

Six entries were verified; `manuscript/references.bib` was left unchanged. No keys changed. The only authored edits were the equation-(3.15) description and a more precise Theorem 2.8 locator in `manuscript/main.tex`. All titles, authors, publication years/versions and identifiers agree with the inspected records. The older report's “Corollary 2.8” wording has been corrected: the displayed book statement is Theorem 2.8, even though its historical notes also call it a corollary.

The five non-library sources have distinct uses: Andrews's memoir supplies the origin and convention; his partition book supplies the classical identity; the two Cui--Gu--Tang papers supply the closest constant-term and integral-expression context; Das--Nath--Sarma supplies the original conjecture and exact computational formula. The single selected library paper supplies a narrow finite-verification scope comparison. It is not evidence for a partition congruence. All 49 active first-sheet titles were screened; a second library citation would add no distinct support. No decorative or uncited reference was added.

The complete publication dependencies are the two canonical sources listed above. There are no included TeX files, custom citation macros, hidden conditional citations, external figures, local styles or alternative bibliography databases. The union of the ledger's direct keys equals the ordinary body citation set exactly. No nocite, comments or verbatim material was counted.

## Sources and access limits

- [AMS memoir record](https://bookstore.ams.org/MEMO/49/301): original bibliographic record. Direct AMS full text could not be retrieved; the convention and Theorem 5.2 lattice expression were inspected in the explicit reproduction in the cited Cui--Gu--Tang primary research manuscript, pp. 1-2. This report does not claim direct inspection of the AMS chapters.
- [Cambridge book record](https://www.cambridge.org/core/books/theory-of-partitions/7BC70DD4C1A06AA6179CEDEAD2F0C2DC), author's publication list, and the [original book scan/OCR](https://www.scribd.com/document/364617376/George-E-Andrews-the-Theory-of-Partitions-BookZZ-org): the scan is hosted by a third party, but the checked content is the original theorem, not host commentary. [NIST DLMF 17.8.1](https://dlmf.nist.gov/17.8#E1) independently resolves the OCR's formula ambiguity.
- [2024 publisher record](https://www.sciencedirect.com/science/article/abs/pii/S009731652300105X) and [author-hosted manuscript](https://cfc.nankai.edu.cn/_upload/article/files/7c/59/537dfc2d4ccc940465b4bb926c83/8ce84fba-2d0e-457e-9b89-7c4c5688d8da.pdf): the deposited author copy predates publication and is identified as such.
- [2025 publisher record](https://link.springer.com/article/10.1007/s11139-025-01176-6): exact abstract-level support for the contextual claim; no inaccessible theorem is attributed to it.
- [Official arXiv version 1](https://arxiv.org/html/2609.05302v1): Theorems 1.2-1.3, equation (3.15), Conjecture 5.1.
- [Selected user-library preprint, version 1](https://www.preprints.org/manuscript/202608.1658): abstract and Section 7; publication remains explicitly non-peer-reviewed.

Applicable academic author/year/title, full-title, venue, DOI and arXiv search templates were run and saved in `audit/search-attempt2-*.json` and the subsequent source-access captures. No `literature/bibliography-revision-*.md` or `literature/crossref-*.json`/`.md` files exist in this project. Live WSL requests failed at the network boundary; browser access, including primary author copies, supplied the evidence. No missing request was converted into a mathematical conclusion.

The user prohibited agents and background workers; all semantic verification was performed serially in this release context. The two-pass procedure was non-interactive as expressly requested. Publication is a local audited conjecture note, not a proof, peer review or submission.

## Mechanical validation

The clean `latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex` build completed. The installed bibliography checker reports six cited keys, six bibliography keys, no missing/unused/duplicate keys and no auxiliary mismatch. The final `.log` and `.blg` contain no undefined citations/references, BibTeX warnings, fatal errors or overfull boxes. Four rendered pages were actually inspected; see the separate build and visual reports.

Final typography repair: the strict hook rejected standard pmod and substack commands. Equivalent explicit mod notation and a single-line product index replaced them. The mathematical claims, citations and line intervals did not change. All four pages were rebuilt, rerendered, and viewed again; the final displays remain legible and no warning was found. The final extraction is round 3.
