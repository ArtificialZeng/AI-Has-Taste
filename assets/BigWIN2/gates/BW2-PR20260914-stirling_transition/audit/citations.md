# Verification report

Mode: fresh primary-source verification with exact local evidence. Overall status: **PASS at the manuscript's stated scope**.

Job: `primary-20260914-stirling-transition-release-4805c41c0f1c`. UTC date: 2026-09-14. Citation attempt 1; launch `4fd11a90-a336-4609-ac46-6327c73d377e`.

| Metric | Count |
|---|---:|
| Extracted substantive claims and disclosures | 22 |
| Verified at stated scope | 22 |
| Body citation keys / bibliography entries | 5 / 5 |
| Selected library references / non-library references | 1 / 4 |
| Numerical errors, unsupported attributions, unresolved citations | 0 |

The two requested citation skills were read in full and used. Pass 1 froze the claim list before primary-source verification. Pass 2 checked those fixed claims against original source passages, the accepted mathematical scope, and exact replay. The initial extraction is preserved in `audit/citation-extraction-stage1.json`; the final ledger retains the same claims and updates only source-format excerpts and snapshot bindings. No agents were used because the user explicitly prohibited delegation. No interactive confirmation was requested, as instructed.

## Citation correctness and source locations

| Key | Primary record and nearby support | Decision |
|---|---|---|
| LiangSagan2026 | [Published author-hosted PDF](https://users.math.msu.edu/users/bsagan/Papers/Old/lclc%20-%20pub.pdf), cover and p.31, Conjecture 8.8 and preceding finite-test range. Local arXiv v1 `S8.Thmthm9` is Conjecture 8.9. | Verified; origin and version comparison. |
| Salas2026 | [arXiv v1](https://arxiv.org/abs/2607.04217v1), actual Theorems 1.4 and 1.5, equations (1.14) and (1.16), read in the frozen primary HTML. | Verified; fixed rows and whole row polynomials, with coefficientwise parameter order. |
| FanWang2026 | [Publisher abstract](https://www.sciencedirect.com/science/article/pii/S0196885826000643), opening two sentences plus author/title/volume/date record. | Verified only for the explicitly abstract-level attribution. |
| ZengLiuRatnavelu2026 | [Primary version 1](https://www.preprints.org/manuscript/202608.1346/v1), byline/date, Section 3 equations (10)-(15), Section 4.1 equation (18), Section 7. | Verified; symmetric-function reduction and exact positivity decomposition, with different variable domain explicitly acknowledged. |
| MeurerEtAl2017 | [Authors' paper repository](https://github.com/sympy/sympy-paper), recommended citation, complete BibTeX and abstract. | Verified software attribution; exact used version is independently recorded in frozen local evidence. |

Titles, author names, years, venue/version and DOI identities match the primary records. The full five-row metadata/support table, access limits and evidence locations are in `audit/citation-source-map.json`. The existing `manuscript/references.bib` needed no replacement, no key changes and no deletions. The authors' recommended SymPy BibTeX was compared with the current entry; differences are optional fields and formatting, not identity. Both preprints remain identified as preprints. Search discovery and primary text receipts are saved separately; registry metadata alone was never accepted as support.

Fan--Wang's direct full text remains inaccessible. The accessible publisher-indexed abstract supports exactly the manuscript sentence; neither its complete ratio theorem nor possible Stirling applications is excluded. Crossref capture patterns were enumerated before reporting this limit and no such captures exist in this project. PeerJ direct opening also failed, but the authors' primary source repository supplied the needed publication record. These access limits do not become mathematical claims. The bounded searches found no equivalent fixed-column resolution in the inspected texts and do not certify worldwide novelty.

## Claim verification and coverage

`audit/citation-verification.json` records a separate substantive basis for every C01-C22. The manuscript's theorem, lemmas, endpoint conventions, positive numerator decomposition and finite-threshold proof match the accepted frozen claim. No new mathematical assertion was inserted. The convolution observation is direct coefficient multiplication, not an unsupported attribution to Salas. The ordinary body union is exactly the five ledger keys; comments, inert macros and hidden citations supply none of the coverage.

The publication verifier was copied byte for byte into `audit/release-replay/` and executed there, preserving the original supplement. Its result equals `manuscript/verification.json`: both polynomial residuals vanish; 72,000 determinant tests, 52,100 second differences, 791 weight multisets and the cycle-type coverage through n=22 agree exactly. The source version field confirms SymPy 1.14.0. These are finite error-detection checks; the infinite proof remains the accepted deductive argument.

The active 49-record first-sheet registry was read, all titles screened, and closest object/method abstracts examined. Row 23 supports a concrete algebraic comparison: elementary-symmetric reduction followed by exact positivity certificates. It is not used as a Stirling theorem or solely as an exact-arithmetic citation. One natural library record is sufficient here; related but unneeded matrix, probability and graph results were not added. The four non-library papers cover the problem origin, closest inspected row results, relevant general ratio work and software. The recurrence/product formula is derived from permutation insertion, and the nontrivial ratio lemmas and verification identities are proved in full, so no omitted external theorem is doing hidden work. No decorative references or fixed reference-count quota were used.

The dependency inventory is complete: `manuscript/main.tex`, `manuscript/references.bib`, `manuscript/verify.py`, and `manuscript/verification.json`. The last two are bound supplementary evidence rather than TeX imports. Compiler recorder inputs use only main.tex, generated aux/out/bbl files, and installed system packages/fonts; BibTeX uses references.bib and system plainnat.bst. There is no additional authored input, figure, database or local style. Canonical bibliography syntax and the exact active library binding passed the installed selection validator. The runner-owned pre-publication hook was not invoked.

## Final build and rendered citations

The release made scope-preserving TeX changes: direct cite syntax for all five references, source locators retained in visible prose, explicit blue link colors, removal of one equation spacer, and accurate PDF title/author metadata. Initial selection-validator syntax failures are recorded in `audit/selection-validation.json` together with the repairs. Final sources were rebuilt from a clean output directory, refrozen, and all five rendered pages were actually viewed again. All references [1]-[5], source numbers, equations and numerical coverage resolve. Final mechanical BibTeX checks report five source keys, five database keys, five aux keys, and no missing, unused or unmatched entries. Detailed build and page observations are in the separate reports.
