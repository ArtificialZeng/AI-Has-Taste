# Verification Report

**Mode:** Search verification with preserved primary documents and exact local evidence.  
**Document:** `manuscript/main.tex`, `manuscript/references.bib`, and the declared companion `manuscript/verify.py`.  
**Generated:** 2026-09-14 UTC.  
**Release job:** `primary-20260914-antiprism-total-positivity-release-0c9af236c4d2`.  
**Attempt / launch:** 1 / `d1366461-59b3-4b04-9c69-d2799db3a774`.

| Metric | Count |
|---|---:|
| Substantive claims extracted and checked | 31 |
| Direct citation pairs / distinct cited works | 6 / 6 |
| Verified claims at their stated scope | 31 |
| Numerical errors, unsupported attributions, misleading claims | 0 |
| Selected library works / other primary or method works | 1 / 5 |

**Overall status: PASS for the accepted result-note scope.** The original total-nonnegativity question remains unresolved. This release audit is not new mathematical certification or external peer review. Its bindings are in `audit/citations.json` and `audit/manuscript-snapshot.json`.

## Extraction and verification

The entire manuscript and bibliography were read before source verification. Pass 1 fixed 31 claims, including all six citation pairs, in `audit/citation-extraction-pass1.json`. After a two-line citation-format repair, the final extraction was saved in `audit/citation-extraction-final.json`; no mathematical assertion or citation identity changed. The final ledger is `audit/citation-claim-ledger.json`, bound to the canonical source paths and current source/snapshot hashes. Verification then compared those fixed claims with the primary passages and local proof/evidence. No claim was silently dropped or strengthened.

The requested skills were read completely. Their default delegation and interactive confirmation steps were superseded by the user's explicit single-worker, non-interactive instructions. No agent, additional Codex process, or background worker was spawned. The configured pre-publication hook was not invoked.

For all six works, the applicable author/year/title, full-title database, author/year/venue, DOI, and arXiv search templates were executed. Search captures and primary passage locations are under `audit/release-sources/`; the readable source map is `audit/citation-source-index.json`. Search results were discovery leads. Mathematical support comes from the actual primary passages described below, not generated summaries. No bibliography-revision or fast-completion handoff existed. The sole intake handoff was read and checked only for relevant source leads.

## Citation findings and bibliography coverage

All retained titles, authors, years, venue/version fields and identifiers are consistent with the inspected primary evidence. Existing BibTeX entries were retained; no official export was fabricated or substituted. `manuscript/references.bib` is byte-for-byte unchanged, and no key changed. The only manuscript edit replaces the accented, optional-note citation sentence with a literal direct `\cite{Zeng2026}` and places Lemma 2.1 in ordinary text. This preserves its substantive assertion and permits exact selection validation.

| ID / key | Exact supporting source location | Verified nearby use and reason retained |
|---|---|---|
| C01 / ABJ2022 | [Published record](https://link.springer.com/article/10.1007/s00454-021-00356-7); [preprint v2](https://arxiv.org/pdf/2006.10789v2), printed pp. 19–23, Proposition 5.7(b), Section 5.3, equation (20), Proposition 5.12 and its proof | The antiprism h-vector transformation and local Stirling normalization. Substitution of the local formula reproduces the displayed matrix with the required index order. This is the original transformation source. |
| C02 / MW2026 | [Published record](https://link.springer.com/article/10.1007/s00026-024-00727-w); [primary v2 HTML](https://arxiv.org/html/2404.03500v2), final paragraph of Section 2 | Small-dimensional antiprism positivity experiments, with no unsupported numerical dimension bound. Issue year 2026 is correct; online publication was in 2024. This is the closest earlier experimental context. |
| C03 / LM2026 | [Primary v1 record](https://arxiv.org/abs/2607.01577v1), abstract; [primary HTML](https://arxiv.org/html/2607.01577v1), Remark 5.20; frozen PDF p. 19, Remark 5.8 | Established barycentric and interval results and the open antiprism question. The displayed formula agrees with the manuscript. The PDF/HTML numbering distinction is real. This is the immediate problem source, not a source for the internal coefficient hypothesis. |
| C04 / BT2004 | [Author-hosted original paper](https://people.maths.ox.ac.uk/trefethen/barycentric.pdf), equation (2.1), p. 502; Section 9.3, equations (9.3)–(9.6), pp. 512–513; [publisher record](https://epubs.siam.org/doi/10.1137/S0036144502417715) | Lagrange cardinal polynomials and their nodal differentiation matrix. Distinct rational nodes meet the hypotheses; the Laurent-basis adjustment is derived locally. This is the natural interpolation method source. |
| C05 / Zeng2026 | [Primary version 1](https://www.preprints.org/manuscript/202608.2160/v1), Section 2.2, Lemma 2.1 and equation (2), including its proof | Reciprocal root derivatives are the node values of the canonical inverse of the derivative modulo the root polynomial. This identifies the same weight normalization used in the proof. Only this elementary identity is used, with no complexity claim. The preprint author is Zijian Zeng, distinct from the manuscript byline Xiaojian Zeng. |
| C06 / Bareiss1968 | [Indexed original AMS paper](https://www.ams.org/mcom/1968-22-103/S0025-5718-1968-0226829-0/S0025-5718-1968-0226829-0.pdf), opening p. 565, abstract and Section I; implementation in `manuscript/verify.py` | Integer-preserving elimination for determinant evaluation. The implementation's previous-pivot divisions, pivot swaps, sign handling and remainder assertions were inspected and exercised. This is the natural exact determinant method source. No speed or stability assertion is imported. |

For C06, direct AMS downloads/record requests and live Crossref requests failed; JSTOR exposed no article text. Before treating these retrievals as unavailable, `literature/crossref-*.json` and `literature/crossref-*.md` were enumerated: neither existed. The accessible indexed AMS opening passage is original paper text and supports the narrow method attribution. The issue/page metadata are also corroborated in the original [OSTI-hosted report](https://www.osti.gov/servlets/purl/6122085), bibliography entry (1), printed p. 21. No complete AMS PDF download or official BibTeX export is claimed. The failed requests do not invalidate the accessible primary passage, and no broader claim relies on inaccessible text.

The bibliography is not library-only: the five non-library sources independently cover origin, closest prior results, interpolation and exact elimination. Each has a substantive ordinary body use. Adding other library papers on unrelated conjectures would pad the bibliography. The active 49-entry first-sheet registry and manifest were parsed and their titles screened; row 14 is the direct interpolation match. The one-entry selection, exact sentence locator, actual UTC verification date and dynamic registry binding passed `validate_selection`; evidence is `audit/selection-validation.json`. This is a minimum relevant library selection, not a ceiling on references.

## Uncited mathematical and finite-observation claims

The detailed per-claim dispositions are in `audit/citation-claim-verification.json`. The following groups identify their decisive support; all claims remain present in the ledger.

| Claims | Verification and scope |
|---|---|
| M01, M04–M06, M25 | Compared with frozen `claim.json` and accepted `audit/math.md`: same determinant, coefficient formulas, quantifiers, signs and unresolved original status. Neither a negative matrix minor nor a minimal negative order is asserted. |
| M02 | The original Liu–Mao introduction explicitly defines TP by nonnegative minors. The manuscript's terminology distinction is correct. |
| M03, M08–M15 | Compared the formal definitions, generating series, specialization, row-degree extraction, Vandermonde determinant, trace identity, interpolation weights, harmonic cancellation and selected-monomial argument with the accepted reconstruction. The distinctness/invertibility conditions hold; the rational-function identity is extended only after clearing denominators. |
| M07 | The frozen coefficient hypothesis is expressly project-generated. The frozen literature comparison and current bounded searches found no equivalent formula; they provide no exhaustive priority or worldwide open-status certificate. The manuscript states that limitation. |
| M16–M20 | Rechecked the signed Stirling and forward-substitution formulas. The companion reproduced every displayed five-row entry, every Table 1 fraction, the quartic, its positive shift and the exact order-22 sum with rational arithmetic. |
| M21–M22 | Inspected the direct alternating-power-sum extraction, forced row support and integer determinant summation. The companion's separate direct extraction agrees at (k,m) = (1,1), (5,5), (6,3), (22,9). |
| M23 | Replayed the stated family over all 2 ≤ k ≤ 32 and 1 ≤ m ≤ k. The first negative pair is (22,9); no other coefficient shapes or n powers are claimed covered. |
| M24 | Parsed all entries of the frozen order-five and order-six coefficient arrays: respectively 5,712 and 33,396 positive nonzero coefficients. This audit did not reconstruct those full expansions. They remain disclosed finite observations, not premises of the theorem. |

`python3 manuscript/verify.py > audit/release-verification.json` succeeded; every assertion passed. `audit/release-finite-observations.json` records the separate full-array count/sign checks. These computations check transfer and reproducibility and do not replace the accepted all-order derivation. The AI/process disclosure agrees with the actual recorded workflow and is not presented as independent external peer review.

## Dependencies, rendered references and decision

The declaration in `publication.json` includes all authored dependencies: main TeX, canonical bibliography and the companion source. The TeX recorder contains only the main TeX, generated build files and system packages. The BBL is generated from the declared bibliography with system `plain.bst`; no imported TeX, authored figure or local style is missing. The companion is declared because the paper describes and distributes it.

The final clean build has six cited keys, six BibTeX entries and six resolved AUX bibliography labels, without missing or unused entries. All six references and the citation numbers were inspected in the extracted PDF and the rendered pages. The compiler/BibTeX logs contain no unresolved citations or references, failures or layout warnings. See `audit/build.md` and `audit/visual.md` for the actual build and page inspections.

No source or unsupported-claim blocker remains for the stated narrow citation uses. Mathematical input hashes and the accepted audit are unchanged. The final release gate is a structural/provenance check; its success must not be interpreted as proof, novelty certification, journal acceptance or publication to the public.
