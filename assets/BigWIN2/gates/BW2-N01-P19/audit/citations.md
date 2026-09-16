# Verification report

**Overall status: PASS.** Three bibliography entries and all five ordinary body-flow citation occurrences support their nearby claims. All 25 extracted claim groups were checked; numerical errors, unsupported claims, misleading attributions and unresolved identity issues: zero.

Mode: primary-source search for external attributions, plus comparison with the accepted mathematical proof and exact arithmetic for the paper's own claims. This is a release audit, not external peer review or a replacement mathematical certificate.

Job: `newwin-00001-p19-release-825c1e67cb4c`.
Citation attempt: 1. Launch: `1965f721-de47-49fb-ba52-65cd75a10f0d`.
Verification UTC date: 2026-09-12.

## Two-pass protocol

Read the complete canonical manuscript and bibliography, then saved the extraction before fresh primary-source verification in `audit/citation-extraction-original.json`. The final extraction in `audit/citation-claim-ledger.json` has the same 25 claims, adjusted only for the subsequently corrected citation placement and line locations. It was frozen before replaying source support and completing the fresh build and visual audits. Definitions, acknowledgments and purely procedural AI disclosure were not promoted to external factual claims. Mathematical claims in proofs are grouped with their precise enclosing lemma/proof location rather than treated as unsourced general facts.

The fixed extraction is followed by one support decision for every claim in `audit/citation-verification-evidence.json`. The union of its direct keys equals the ordinary active body set exactly: `BaraskarVukusic2026`, `Shoup2009`, `ZengEtAl2026Certificates`. No comments, nocite, verbatim code, macros or hidden conditionals supply a required key. The selected library citation is an ordinary direct `\cite{ZengEtAl2026Certificates}`.

No agents, other Codex processes, background workers or interactive confirmations were used: the explicit worker instructions require serial, non-interactive verification. The configured pre-publication hook was not invoked.

## Bibliography correctness and nearby support

| Key | Verified record and source passage | Necessary nearby use | Action |
|---|---|---|---|
| BaraskarVukusic2026 | Omkar Baraskar and Ingrid Vukusic, *Bounds for Sets of Remainders*, JIS 29 (2026), Article 26.1.4, 18 pages; Theorem 1 p. 3, Theorem 3 p. 4, Problem 2 p. 16 | Problem origin, first-iterate convergence and closest general iterate bounds | Retained; no key change |
| Shoup2009 | Victor Shoup, *A Computational Introduction to Number Theory and Algebra*, second edition, Cambridge UP, 2009; Theorem 2.6 pp. 23-24 and Theorem 8.1 / proof (8.8) pp. 210-211 | Exact finite CRT product proportions and inclusion-exclusion verification | Retained; no key change |
| ZengEtAl2026Certificates | Zijian Zeng, Houde Liu, Kuru Ratnavelu, Ong Seng Huat, *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes*, Preprints.org v1, posted 24 August 2026; Section 6 | Explicit methodological comparison: reconstruct complete finite input and use a separate exact verifier | Completed missing DOI; retained preprint status and key |

The author/title/date/venue and claim-level checks are distinct. The primary [JIS record](https://cs.uwaterloo.ca/journals/JIS/VOL29/Vukusic/vukusic2.html) confirms its journal metadata; the [full publisher paper](https://cs.uwaterloo.ca/journals/JIS/VOL29/Vukusic/vukusic2.pdf) confirms the definitions, theorems and problem. Substituting j=2 into Theorem 3 gives exactly 1/24 and 1/4; this is a documented specialization, not an asserted quotation of a strict separation.

The [author's book page](https://shoup.net/ntb/) identifies its downloadable Version 2 (2008) as corresponding to the second print edition. The [author's full PDF](https://shoup.net/ntb/ntb-v2.pdf) was inspected at its exact CRT and finite inclusion-exclusion statements and proofs. The [publisher copyright leaf](https://assets.cambridge.org/97805215/16440/copyright/9780521516440_copyright_info.pdf), returned as primary indexed text, confirms the 2009 print year and ISBN 978-0-521-51644-0. The direct copyright-leaf open later timed out; the substantive theorem text was directly accessible.

The [selected preprint's full primary HTML](https://www.preprints.org/manuscript/202608.1658/v1) identifies v1 and its four authors and posting date, and explicitly states that it is not peer reviewed. Section 6, HTML lines 207-218, describes complete integer-input reconstruction, a separate exact implementation, and integer/rational decisive comparisons. Section 4 Proposition 1 supplies a further example of independent graph reconstruction. These support the narrow method comparison; no geometric theorem is cited as an arithmetic premise. The [publisher's Computational Mathematics listing](https://www.preprints.org/subject/browse/computer-science-and-mathematics/computational-mathematics) binds the same exact title and authors to DOI `10.20944/preprints202608.1658.v1` and the August 24 posting date.

Crossref/DOI resolver and BibTeX export requests failed in this environment. Before assessing access limits, `literature/crossref-*.json` and `literature/crossref-*.md` were enumerated; neither exists. No source was declared nonexistent. Official exported BibTeX was not recovered, so the existing verified entries were retained. Only the selected preprint's missing DOI field was completed from verified primary metadata; no raw-export replacement or new key is claimed. All retained bibliographic identities and all cited claims have primary support.

## Coverage and user library

The active registry and manifest were read, and all 49 first-sheet titles were screened. The abstracts for the strongest leads, rows 7, 9 and 44, were considered. Row 9 is selected for the concrete verification comparison whose full source passage was inspected. Rows 7 and 44 concern different arithmetic problems and are not necessary premises of this manuscript. Adding them without an additional needed claim would not improve coverage.

This is a normal claim-driven bibliography, not an Excel-only bibliography: the non-library problem paper covers the original question and nearest bounds, and the non-library book covers both nontrivial standard methods. Elementary division and prime-divisor existence are proved or used in their elementary form; no analytic prime estimate, Pierce-expansion theorem or geometric optimization algorithm is invoked as a premise. There is no fixed reference quota and no decorative reference. The gate-bound one-item selection is in `audit/user-bibliography-selection.json`, with its dynamic active registry binding, exact current attempt/launch identity, UTC date and smallest literal citation-bearing sentence. The hook-compatible `bigwin_user_bibliography.validate_selection` actually passed; see `audit/release-selection-validation.json`.

## Claim decisions

| ID | Type | Manuscript lines | Direct keys | Status / support locator |
|---|---|---|---|---|
| C01 | Existence + Statistic | 25-35 | (own result) | Verified (exact): audit/release-arithmetic-checks.json and audit/math.md |
| C02 | Existence | 47-48 | (own result) | Verified (exact): source.md and manuscript equation (1) |
| C03 | Attribution + Statistic | 50-58 | BaraskarVukusic2026 | Verified (interpretation): BaraskarVukusic2026, Theorems 1 and 3, pp. 3-4 |
| C04 | Attribution | 59-60 | BaraskarVukusic2026 | Verified (paraphrase): BaraskarVukusic2026, Section 7 Problem 2, p. 16 |
| C05 | Comparative | 61-63 | (own result) | Verified (interpretation): audit/math.md, Source comparison; BaraskarVukusic2026, Theorem 3 |
| C06 | Statistic | 69-80 | (own result) | Verified (exact): audit/release-arithmetic.json; claim.json |
| C07 | Existence | 82-95 | (own result) | Verified (exact): claim.json; audit/math.md, Exact separation |
| C08 | Attribution | 97-102 | Shoup2009 | Verified (paraphrase): Shoup2009, Theorem 2.6 and residue-bijection restatement, pp. 23-24 |
| C09 | Existence | 106-135 | (own result) | Verified (exact): evidence/research-proof.md, Section 1; audit/math.md, Positive membership |
| C10 | Existence | 137-146 | (own result) | Verified (exact): evidence/research-proof.md, Section 2, equation (2) |
| C11 | Existence | 159-191 | (own result) | Verified (exact): audit/math.md, Fixed cutoff and a uniform count |
| C12 | Statistic | 197-225 | (own result) | Verified (exact): audit/release-arithmetic-checks.json |
| C13 | Statistic | 226-232 | (own result) | Verified (exact): audit/release-arithmetic.json, beta |
| C14 | Existence | 236-253 | (own result) | Verified (exact): audit/math.md, Coefficients and prime-power cases |
| C15 | Existence | 260-265 | (own result) | Verified (exact): evidence/research-proof.md, zero-class density derivation; Shoup2009 CRT |
| C16 | Existence | 267-290 | (own result) | Verified (exact): audit/math.md, Coefficients and prime-power cases; audit/release-arithmetic.json |
| C17 | Statistic | 292-321 | (own result) | Verified (exact): audit/release-arithmetic-checks.json, zero_class_table |
| C18 | Causal | 325-335 | (own result) | Verified (exact): claim.json; audit/math.md, Exact separation |
| C19 | Existence + Statistic | 337-352 | (own result) | Verified (exact): audit/release-arithmetic.json, certified_gap_at_203; claim.json |
| C20 | Statistic | 354-357 | (own result) | Verified (exact): manuscript/certificate.py, final gap assertions; audit/release-arithmetic.json |
| C21 | Existence | 359-366 | (own result) | Verified (exact): manuscript/certificate.py and audit/release-arithmetic.json |
| C22 | Attribution | 368-377 | Shoup2009 | Verified (interpretation): Shoup2009, Theorem 8.1 proof, equation (8.8), pp. 210-211 |
| C23 | Statistic | 377-379 | (own result) | Verified (exact): audit/referee_verify.py lines 181-185; audit/referee-verification.json |
| C24 | Attribution + Comparative | 381-384 | ZengEtAl2026Certificates | Verified (interpretation): ZengEtAl2026Certificates, Section 6, HTML lines 207-218 |
| C25 | Existence | 384-387 | (own result) | Verified (exact): accepted proof and manuscript Lemmas 2-3 |

The detailed claim text, hypothesis checks and inference explanations are in the JSON ledger and verification evidence. All eight residue counts and all 18 zero-class table densities were extracted from the final TeX and compared value-by-value with the full publication certificate and accepted referee evidence. The displayed constants and both gaps agree exactly. The abstract's decimal statement is a strict lower inequality: the exact rational gap exceeds 49/5000, not a rounded claim of equality. The assertion about testing through 768 is supported by the separate referee verifier and its output; that finite range is not used to justify arbitrary n.

## Bounded literature comparison

All applicable academic search templates were run for each source: first author/year/first title words, exact title with arXiv or Semantic Scholar discovery filters, first author/year/venue, DOI for the selected preprint, and arXiv:2508.20853 for the origin paper. Additional queries were `"Bounds for Sets of Remainders" "nonconvergence"` and `"iterated remainder sets" nonconvergence proof`. The relevant primary results were the original JIS paper and its arXiv preprint. No equivalent two-progression separation was found in this bounded search on 2026-09-12. This does not certify exhaustive priority or the global current status of higher iterates. Search-result snippets from secondary sources were not used as support.

Web retrieval and query evidence is retained under `audit/release-sources/`; the frozen original publisher PDF is under `evidence/external/`. This pass read the primary passages, rather than accepting the writer's confidence or relying solely on DOI existence.

## Scope, changes and final consistency

The abstract, main theorem, lemmas, constants, proof and sufficient threshold preserve exactly the accepted j=2 scope. The original `source.md`, `checkpoint.md`, `claim.json` and all mathematical snapshot inputs remain byte-for-byte unchanged. No result about j>=3, exact global extrema, or minimal threshold was added.

Edits are limited to `manuscript/main.tex` and `manuscript/references.bib`: simplified the email link's unsupported nested TeX command, moved the origin citation into ordinary body prose, made the library citation direct and kept its Section 6 locator in prose, and completed its verified DOI. No mathematical expression or claim was changed. No citation keys changed.

A genuinely clean latexmk build, the final TeX and BibTeX logs, canonical key-to-bibliography/aux consistency, complete source dependencies, PDF metadata and embedded fonts were checked. All six rendered pages were actually viewed. Build and visual findings have separate reports. `audit/build.log` is the completed final log; `audit/release-build-transcript.log` also retains normal intermediate compilation messages.

The citation audit is bound to these final digests:

- Accepted mathematical snapshot: `f6e26cd2153e23fdfbc5be1822272e0031a1a19a7c9717f8d44555b03e6c3e02`.
- Manuscript snapshot: `4c489d65f1189161766c2f6e9fe675a23006759b4dfe905baef9862b73262627`.
- Final PDF: `65180f3d38bed38a49108150ab3c8efe277ebc78f4ec7d5b1ffbe5c901766bb3`.
