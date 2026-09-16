# Citation and bibliography audit

Release job `lit-260905848-p01-release-5258dabb668e`, citation attempt 2, launch `5c5caafc-c0e9-4cf7-9fdd-55688689d609`.

## Verdict and method

**Accept.** The extraction stage froze seven substantive claim/citation pairs. Their key union is exactly the seven ordinary body-flow citation keys in `manuscript/main.tex`; there are no citations hidden in comments, `\nocite`, inert macros, verbatim material, or conditionals. The independent verification stage then replayed the required author/title, full-title, author/year/venue, DOI, and arXiv searches and checked each fixed claim against the exact primary-source passage recorded in `audit/source-locations.json`. The canonical key checker found seven cited keys, seven bibliography keys, no missing entry, no uncited entry, and all seven keys in the generated AUX file.

| Claim | Citation key | Manuscript location | Direct primary-source locator | Result |
|---|---|---:|---|---|
| CIT-01 | `FranklTokushige2016` | 63--70 | author PDF, p. 25, Conjecture 8.1 | verified paraphrase |
| CIT-02 | `LiLvWen2026` | 72--76 | arXiv v1 HTML, Theorem 1.1 | verified exactly |
| CIT-03 | `Tokushige2013` | 76--77 | author PDF, p. 2, Theorem 2 | verified exactly |
| CIT-04 | `ShimizuTokushige2026` | 77--80 | arXiv v1 HTML, paragraph after Theorem 3 | verified paraphrase |
| CIT-05 | `ZengEtAl2026` | 83--88 | publisher landing record, abstract and Sections 3--6 | verified paraphrase |
| CIT-06 | `BiereEtAl2024` | 238--239 | author PDF, p. 1, abstract and Section 1 | verified paraphrase |
| CIT-07 | `WetzlerHeuleHunt2014` | 240--243 | author PDF, p. 1, abstract and Section 1 | verified paraphrase |

No claim was numerically wrong, contradicted, misleadingly strengthened, or unsupported. Full canonical records, URLs, search replays, extracted-line locators, and support explanations are preserved in `audit/source-locations.json` and summarized independently in `audit/citation-verification.json`.

## Bibliographic correctness and coverage

Every retained reference exists. Authors, title, date, venue or repository version, DOI, and arXiv identifier in `manuscript/references.bib` agree with the checked primary records. The current attempt required no BibTeX replacement or key change. The rendered bibliography contains all seven records and no undefined citation.

Coverage is natural and not user-library-only. The paper cites the problem-origin survey, the closest 2026 vector-space results, the primary two-family theorem, the CaDiCaL system source, and the DRAT/checker source. The gate-bound library selection is the single genuinely nearby method paper `ZengEtAl2026`, directly cited in ordinary body flow. Its exact-predicate, symmetry-exhaustion, and independent-verifier practices support only the explicitly labeled methodological comparison. The other 48 active first-sheet library records would be padding rather than claim support, as documented in `audit/user-bibliography-selection.json`.

The local CNF sizes, archive byte counts, and checker step counts are intentionally not delegated to literature. They are archive-specific facts covered by the accepted mathematical evidence. The release text now states precisely that each binary stream contains a checked refutation prefix followed by disclosed trailing data including an incomplete final record; the method citations are not presented as certifying either local run.

## Limits

This audit verifies citation existence, metadata, nearby support, and coverage as of UTC 2026-09-10. It does not assert literature priority, peer review of the 2026 preprints, or correctness beyond the accepted mathematical audit. The job explicitly prohibited agents, so the two verification stages were performed sequentially and independently within the worker.
