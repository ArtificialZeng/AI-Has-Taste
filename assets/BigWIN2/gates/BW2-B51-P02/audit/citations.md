# Citation and bibliography release audit

## Method and frozen extraction

I used the requested two-stage non-interactive search-verification procedure.  Pass 1 froze seven claim/citation pairs in `audit/citation-claim-ledger.json` against manuscript snapshot `d938aadaf7f63c430817129e52e0abee8bef69bca6e3af898b70849cf986142c`; no verification result was added to that ledger.  Pass 2 checked those fixed claims in order against original publisher/arXiv/preprint text.  Exact source locations are serialized in `audit/citation-source-locations.json`.  The audit was performed serially because this release job explicitly prohibited subagents and other workers.

The source-tree enumeration found no `literature/bibliography-revision-*.md` and no `literature/crossref-*.json` or `literature/crossref-*.md` captures in this project.  Live primary records were therefore used together with the frozen Tian v1 PDF.  For each academic citation I ran the applicable author/year/title, full-title, author/venue, DOI, and arXiv searches; discovery snippets were not treated as source support.

## Claim-to-source findings

| Claim | Key | Nearby claim and exact support | Status |
|---|---|---|---|
| C01 | `Alon2024` | The arXiv primary manuscript abstract and Introduction define a connectivity code by connected spanning symmetric differences. | Verified (paraphrase) |
| C02 | `Alon2024` | The same abstract and Introduction state exactly `m(H) <= 2^{k'(H)} <= 2^{delta(H)}`. | Verified (exact) |
| C03 | `BaiEtAl2024` | Proposition 1.7 states the bound 16 for all toroidal grids with both parameters at least 3 and equality for the 3 by 3 case; its proof supplies the four-edge restriction argument. | Verified (exact) |
| C04 | `Tian2026` | The abstract and Theorem 1.2 construct infinitely many pairwise nonisomorphic extremal regular examples for every degree at least four. | Verified (paraphrase) |
| C05 | `Tian2026` | Section 6(d), PDF page 8, states that determining `m(C_m square C_n)` for all `m,n` remains open. | Verified (exact) |
| C06 | `Tian2026` | The manuscript expressly limits its own result to one fixed graph and disclaims absolute priority; this does not strengthen Tian's general open statement. | Verified (scope) |
| C07 | `ZengEtAl2026` | Preprints.org version 1, Sections 4 and 6, uses integer graph predicates, two separate exact maximum-clique implementations, and independent reconstruction of serialized finite objects. | Verified (paraphrase) |

All seven fixed claims are supported.  There are no numerical errors, hallucinations, misleading citations, citation-not-found results, or unresolved source-access blockers.

## Bibliographic identity and key audit

All four cited works exist and the author lists, titles, years/versions, venues, page ranges, and DOI/arXiv identities in `manuscript/references.bib` agree with authoritative records.  Tian's landing-page metadata uses a shorter updated title while the cited v1 PDF itself prints the longer title retained in the bibliography; the entry explicitly identifies v1 and the record identity is unambiguous.  No BibTeX replacement or key change was necessary.

The mechanical audit found four cited keys, four unique bibliography entries, no missing or unused entries, and exact agreement with the final `.aux`.  The final `.blg` has no missing database entry, repeated entry, or BibTeX warning.  The retained keys are `Alon2024`, `BaiEtAl2024`, `Tian2026`, and `ZengEtAl2026`.

## Coverage and user-library selection

The bibliography is not user-library-only.  It includes the natural primary source for the definition and general cut bound (Alon), the closest fixed-product result (Bai--Gao--Ma--Wu), and the immediate 2026 general connectivity-code paper that explicitly leaves products of cycles open (Tian).  Those three sources cover the problem origin and closest prior results.  The proof itself is self-contained; the CP-SAT solver is outside its trust boundary, so no external solver-correctness claim is used.

The active 49-record first-sheet user library was checksum-bound to its registry and source workbook in `audit/user-bibliography-selection.json`.  Row 9 is genuinely relevant to the one methodological comparison at manuscript lines 166--169 and is directly cited there as `\cite[Sections~4 and 6]{ZengEtAl2026}`.  No second library record supplies a distinct dependency; adding one would be decorative.  The one-reference rationale and exact primary passage are recorded in the bound selection file.

## Verdict

**Accept.**  Citation existence, metadata, nearby support, bibliography coverage, user-library relevance, source-file completeness, and TeX/BibTeX key consistency all pass.  The audit scope is the paper's seven literature-dependent statements; it makes no absolute novelty or journal-acceptance claim.
