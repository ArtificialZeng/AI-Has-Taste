# Verification report

**Mode:** two-pass primary-source verification, with exact local evidence for the
paper's own mathematical and numerical assertions. **Verdict: accept.**
**Document:** `manuscript/main.tex`, using only `manuscript/references.bib`.
**UTC verification date:** 2026-09-14.
**Job:** `primary-20260914-q-product-unimodality-release-a0a2d6a0e9ce`.
**Citation attempt:** 1.
**Launch:** `3b7d366e-0e77-4083-ae64-a46df0164b5b`.

| Metric | Count |
|---|---:|
| Frozen substantive claims | 28 |
| Claims with verified support | 28 |
| Source-linked claim groups | 6 |
| Ordinary body citation occurrences | 7 |
| Distinct cited references | 3 |
| Selected user-library records | 1 |
| Natural non-library references | 2 |
| Numerical errors, unsupported claims, unresolved citations | 0 |

The two explicitly requested citation skills were read completely before this
audit. The user required a non-interactive pass and prohibited agents; accordingly,
extraction was frozen locally and every reference was verified by this release
worker without delegation. No interactive confirmation, extra Codex process,
background worker, or configured pre-publication hook was used.

## Extraction and verification separation

`audit/citation-extraction.md` and `audit/citation-claim-ledger.json` fixed the
28 claims and their line intervals before fresh primary-passage verification.
Pass 2 evaluated that fixed list; `audit/citation-verification.json` records a
verdict and precise evidence for every claim. C04 contains two adjacent source
assertions and both citation occurrences were checked at their respective source
locators. The citation-key union is exactly `Andrews1975`, `CIMSY2026`, and
`ZengEtAl2026`. Definitions and the assistance disclosure were excluded from
external factual-claim extraction but were checked for scope and presentation.
There are no hidden citations, inert citation macros, `nocite` commands, or
conditional branches supplying a reference.

Three normalizations were necessary for the conservative citation parser:
the floor macro was expanded to its identical standard-TeX replacement; the
title uses literal mathematical q while retaining its explicit plain-text PDF
metadata; and the canonical `references` bibliography now prints in ordinary
body flow, with the same small type. The bibliography lookup is relative to the
manuscript directory. These changes preserved the claim text and all line
locations. The rebuilt PDF's text is byte-identical to the writer's extracted
PDF text. The full current sources were rechecked and the final snapshot and
ledger bindings were refreshed after rebuilding.

## Source identity and nearby support

| Key | Current and verified title | Primary record and exact support | Action |
|---|---|---|---|
| CIMSY2026 | Unimodality of q-Fibonomial coefficients for small cases | [arXiv version 1](https://arxiv.org/abs/2605.12822v1), [primary HTML](https://arxiv.org/html/2605.12822v1). Conjecture 5.4, PDF p.14; Lemma 4.2 and Corollary 4.3, pp.9–10; Proposition 4.5 and its interval-count proof, pp.11–12; Proposition 5.3, pp.13–14. | Verified; retained. |
| Andrews1975 | A theorem on reciprocal polynomials with applications to permutations and compositions | [JSTOR record and indexed original abstract](https://www.jstor.org/stable/2319803), [publisher's original abstract](https://www.tandfonline.com/doi/abs/10.1080/00029890.1975.11993950), [author bibliography, item 62](https://georgeandrews1.github.io/publications.html). The abstract explicitly states product closure for nonnegative reciprocal unimodal polynomials. | Verified at the narrow abstract scope; retained. |
| ZengEtAl2026 | Exact finite certificates for the four-dimensional ternary Borsuk problem and five-dimensional ternary kissing codes | [Preprints.org version 1](https://www.preprints.org/manuscript/202608.1658/v1), Section 4, Proposition 1 certificate proof, HTML lines 192–195, and Section 6, lines 207–218. These describe integer predicates, reconstruction, and a separate exact implementation. | Verified; retained. |

All author lists match the primary records. The first reference is by Brendan B.
Connelly, Ezekiel Ito, Thomas C. Martinez, Olha Shevchenko, and Kacey Yang;
its arXiv record identifies v1 submitted 12 May 2026. The retained PDF and HTML
have different printed dates; this is not treated as a new version. Andrews's
article is in *The American Mathematical Monthly* 82(8), 830–833 (1975).
The 2018 publisher online date is not substituted for its original year.
Both the JSTOR DOI used in the bibliography and the modern publisher DOI
identify that article. The library preprint's four authors are Zijian Zeng,
Houde Liu, Kuru Ratnavelu, and Ong Seng Huat; version 1 was posted 24 August
2026. Its status is represented as a preprint, not a refereed journal article.
Zijian Zeng is not silently identified with manuscript author Xiaojian Zeng.

No BibTeX entry needed replacement and no citation key changed. The existing
entries were checked field-by-field against primary records; they are not
represented as byte-for-byte official exports. The final `.bbl` and rendered
references preserve the checked authors, titles, years, versions, pages, and
identifiers. The reference audit repaired only TeX lookup/execution syntax.

### Source-access scope

The mandatory author/year/title, full-title database, author/year/venue and
identifier searches were run for all three references; the arXiv-identifier
template applied to CIMSY2026 and the DOI template to the other two. The
verifier followed primary records and did not use secondary search summaries
as mathematical evidence. Fresh results and passages are retained under
`audit/release-sources/`. In addition, the decisive retained CIMSY PDF text was
read directly at the locators above and agreed with the fresh primary HTML.

For Andrews, direct full-article retrieval did not supply inspectable full
text. Fresh searches returned the original abstract on both JSTOR and the
publisher site. The exact closure sentence is supported by that abstract;
no source proof or uninspected theorem number is claimed. The manuscript also
proves the closure property itself. Thus this limited access leaves no gap in
the actual nearby attribution. Before recording this limit, the release
worker enumerated `literature/crossref-*.json` and `literature/crossref-*.md`;
neither pattern had any saved capture. No valid saved Crossref response was
discarded. Source failure is not treated as a mathematical result.

## Claim-level decisions

| Claims | Verification and decisive locator | Result |
|---|---|---|
| C01–C03 | Abstract and Theorem 1 match the accepted two-factor statement in `claim.json`; Conjecture 5.4 supplies the exact broader parent quantifiers. | Verified, exact mathematical scope. |
| C04 | Lemma 4.2 / Corollary 4.3 establish divisibility; Proposition 5.3 establishes the single ordinary factor. | Verified, paraphrase. |
| C05 | Proposition 4.5 gives stretch 2. Relabel its ordinary lengths as a,c and stretched length as b. For odd a,c, the stated inequality equals the manuscript floor-sum bound. The proof explicitly compares positive and negative interval counts. | Verified, paraphrase and elementary specialization. |
| C06 | Andrews's original abstract asserts the stated nonnegative symmetric/unimodal product closure. | Verified, paraphrase. |
| C07–C19 | The centered expansion, divisibility, symmetry, clipped counts, both floor bounds, and the negative witness reproduce the accepted proof in `evidence/k2-characterization.md`, with detailed referee checks in `audit/math.md`. Boundary factors 1, zero quotients, odd degree, empty midpoint range, and upper clipping are retained. | Verified against accepted argument; no strengthening. |
| C20 | Direct integer multiplication reproduces all 13 displayed coefficients, including the two equal terminal values 13. | Verified, exact. |
| C21 | Proposition 5.3 fails for lengths 7 and 9 at stretch 5 and b=3: neither length is divisible by 5, and each is below 10. Both drops were also recomputed. | Verified, exact specialization. |
| C22–C25 | `audit/release-verifier.py` replays every ordered grid tuple and regenerated draw using the inspected referee routines. It confirms 81,648 grid tuples, 600 draws, 82,248 total tests, 54,281 negative witnesses, and 597,941 coefficient comparisons. The complete dense signature equals the referee's. | Verified, exact finite coverage. |
| C26 | Preprints.org Sections 4 and 6 explicitly reconstruct finite objects and use separate exact implementations. The citation compares verification design only; no geometric conclusion is imported. | Verified, paraphrase. |
| C27–C28 | Finite tests are explicitly separated from the symbolic proof. The integer criterion and explicit witness give the asserted decision; the remaining parent parameter ranges are left unresolved here. | Verified within accepted scope. |

The individual record for each of C01–C28, rather than only the grouped table,
is in `audit/citation-verification.json`. Replaying accepted routines is a release
consistency check; it is not an additional independent mathematical review.

## Coverage, library selection, and dependencies

The active registry and manifest at the user-specified paths were parsed and
checked. All 49 first-sheet titles/DOIs/keywords were screened; full lead records
9, 14, 16, 34, and 42 were read. Row 9 has the direct methodological use described
above. Other screened polynomial or finite-verification papers concern results
not used here; adding them would not improve support. The selected reference's
actual primary text, rather than registry metadata, supports its nearby sentence.
`audit/user-bibliography-selection.json` binds this single minimum selection
to the dynamic 49-record registry, actual UTC date, and current attempt/launch.
The context is the smallest citation-bearing sentence at lines 243–246.

The bibliography is not library-only. CIMSY2026 is required for the question,
closest prior theorem, and reused interval reduction; Andrews1975 is the natural
classical source for product closure. The library source supports the exact
verification design actually reported. Each reference has a substantive body
use, with no fixed-count padding. No Gaussian/Fibonomial theorem, algorithmic
complexity bound, or geometric theorem requiring additional literature is used.
No worldwide-priority or exhaustive-search claim is made.

`publication.json` completely enumerates the authored build inputs:
`manuscript/main.tex` and `manuscript/references.bib`. There are no imported
authored fragments, local styles, figures, or omitted databases. The generated
`.bbl` derives from the canonical bibliography using system `plain.bst`.
The `.fls` dependency check found only the main source and generated aux/bbl/out
files locally. Captured literature and audit scripts are not TeX dependencies.

The final bibliography-key check reports 3 source keys, 3 database keys, and
3 resolved auxiliary citations, with no missing or unused key. All seven body
citations resolve in the extracted and visually inspected PDF. The installed
hook-compatible `validate_selection` passes, and its masked-body key set equals
the ledger union. See `audit/selection-validation.json`, `audit/bib-key-check.txt`,
and `audit/release-preflight.json`. The runner-owned hook remains uninvoked.

All frozen source, checkpoint, claim, evidence, and mathematical-audit files
remain byte-identical; `audit/release-integrity-final.json` records this check.
This acceptance concerns the bound manuscript's citations and scope, not
external peer review or a resolution beyond the accepted two-factor theorem.
