# Verification Report

**Mode:** Primary-source search verification, with a separate frozen extraction and verification pass.
**Document:** `manuscript/main.tex`, `manuscript/references.bib`, and the six-page `build/main.pdf`.
**Verified UTC date:** 2026-09-13.
**Release job:** `primary-20260914-grid-narayana-release-a978c20a048a`.
**Attempt / launch:** 1 / `e4d95c25-b291-4bd2-99e3-012a88d27040`.

| Metric | Count |
|---|---:|
| Substantive claim groups extracted | 26 |
| Verified claim groups | 26 |
| Distinct directly cited works | 5 |
| Citation-bearing claim groups | 6 |
| Non-library works in ordinary body flow | 4 |
| Selected active-library works | 1 |
| Numerical errors, unsupported claims, misleading attributions | 0 |
| Undefined citations or bibliography entries | 0 |

**Overall status: PASS.** This is a release and source-support audit. Mathematical acceptance remains the separate frozen report `audit/math.md`; it is not inferred from the build or from this report.

## Extraction and verification

The complete manuscript was read before extracting the fixed claims. The extraction is in `audit/citation-claim-ledger.json` and `audit/citation-extraction.md`; all 26 individual findings, precise source locations, and support explanations are in `audit/claim-verification.json`. Verification proceeded against that fixed list. Final digest/excerpt bindings incorporate only the metadata and presentation repairs described below. No substantive claim or citation key changed.

The ordinary-body parser masks comments, inert macros, opaque command arguments, literal text, and hidden conditionals. Its five active keys are exactly `AC26`, `Ath25`, `Flajolet80`, `Gessel16`, and `ZengEtAl26`, which also exactly equal the union of the ledger keys and the bibliography keys. There are no imported TeX files, custom citation macros, hidden citations, or `nocite` uses. `publication.json` correctly lists the two authored compilation dependencies. The LaTeX recorder and BibTeX log identify only standard installed TeX resources and generated auxiliary files beyond these inputs.

The requested audit was non-interactive. No agents, other Codex processes, or background workers were launched, because the user expressly prohibited delegation. The citation and bibliography skills were applied locally in this fresh context. The v4 release reference and the shared contract required by the supervisor handoff were read in full, separately, as were both citation skills. No unrelated phase reference was read.

## Claim-level source audit and coverage

| Key | Verified primary record and exact support | Nearby use and retention decision |
|---|---|---|
| AC26 | Athanasiadis and Chapoton, *Polytopes and posets associated to preorders*, arXiv:2605.26916v1 (2026). [Primary text](https://arxiv.org/html/2605.26916v1): Section 9.3, final paragraph; Section 5, opening definition. | C01-C02, lines 71-74: origin of the exact maximum-deleted grid proposal and the nonzero-coordinate statistic. Needed for attribution and scope. The paper heading orders Athanasiadis before Chapoton; the repository abstract reverses them. The entry follows the cited paper heading. The served v1 identifier is retained; its internal August date is not treated as another version. |
| Ath25 | Athanasiadis, *Lattice point enumeration of polytopes associated to integer compositions*, arXiv:2510.23903, first submitted 2025, consulted v3 (2026). [Examples 2.3-2.4](https://arxiv.org/html/2510.23903v3) give the total-bound binomial-square coefficients and the chain-prefix Narayana coefficients. A [published record](https://link.springer.com/article/10.1007/s00026-026-00812-2) was also located. | C03, lines 74-79: closest separate-factor evaluations. The bibliography explicitly identifies the consulted preprint version for its locators. The conclusion that these single-family evaluations do not themselves separate the coupled grid inequalities is the manuscript's comparison of their hypotheses, not a quoted source theorem. |
| Flajolet80 | Flajolet, *Combinatorial aspects of continued fractions*, **Discrete Mathematics** 32(2) (1980), 125-161, DOI 10.1016/0012-365X(80)90050-3. [Author-hosted primary PDF](https://algo.inria.fr/flajolet/Publications/Flajolet80b.pdf): positive labelled paths on printed p. 127, Theorem 1 on p. 129, Motzkin specialization in Section 2.1 on p. 135. [Publisher record](https://www.sciencedirect.com/science/article/pii/0012365X80900503) supplies the journal metadata. | C04, lines 232-239: the formal weighted-path framework. Specializing rise, fall, and level weights to q, tq, and cq gives the claimed setting. The manuscript derives its own first-return equation. Needed method source; no analytic or positivity hypothesis is imported. |
| Gessel16 | Gessel, *Lagrange Inversion*, **Journal of Combinatorial Theory, Series A** 144 (2016), 212-249, DOI 10.1016/j.jcta.2016.06.018. [Primary record](https://arxiv.org/abs/1609.05988) confirms author, title, year, venue, pages, and DOI. [Theorem 2.1.1](https://arxiv.org/html/1609.05988), equation (2.1.1), is the needed coefficient identity; Section 4.1 treats the residue proof. | C05, lines 268-286: formal inversion with R(w)=w²+cw+t and phi(w)=w^k. The hypotheses hold over Q(c,t), with n positive and t invertible for the intermediate substitution. The manuscript proves the specialization and extends polynomially to t=0. Needed method source. |
| ZengEtAl26 | Zeng, Liu, Ratnavelu, and Ong Seng Huat, *Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes*, Preprints.org, v1 (posted 24 August 2026). [Primary Section 6](https://www.preprints.org/manuscript/202608.1658/v1) describes reconstruction of defining finite objects, a separate exact implementation, and integer/rational comparisons. The publisher's [Computational Mathematics index](https://www.preprints.org/subject/browse/computer-science-and-mathematics/computational-mathematics), corresponding entry, directly associates the same title and four authors with DOI 10.20944/preprints202608.1658.v1. | C06, lines 326-329: a concrete precedent for the separate exact-checker practice actually used here. This is a methods citation, not a claim about Narayana polynomials or an import of geometric theorems. Preprint status is explicit. Retained for this narrow, verified use. |

Primary passage locators and retrieved text are retained in `audit/source-passages.json`. Mathematical assertions C07-C24 were checked against the unchanged original statement and the corresponding sections of `evidence/research-proof.md`, including both boundary cutoffs, the trace sign, the polynomial specialization, n=1, and t=0. The all-n statement is unchanged. The code and complete saved exact output support C25-C26: the six ambient counts are 2, 20, 252, 3432, 48620, and 705432; the other ranges are exactly those printed in the article. The counts and stored coefficient vectors were recalculated from their integer formulas in this release pass. The exhaustive enumeration itself was not rerun or represented as a proof for all n.

The bibliography covers the problem origin, the closest factor evaluations, the two nontrivial standard methods, and the stated verification practice. It is neither library-only nor padded. Elementary binomial algebra and the newly proved finite trace identity are established in the text and do not need decorative references.

## Active library and source-access limits

The active registry and manifest were parsed at the exact supplied paths. All 49 first-sheet titles and abstracts were screened. The minimum selection is row 9, original registry key `202608.1658`, final key `ZengEtAl26`. The dynamic registry binding, UTC verification date, literal smallest citation-bearing sentence, and exact manuscript line interval are in `audit/user-bibliography-selection.json`. The hook-compatible `validate_selection` routine passed against the actual manuscript, bibliography, workbook, registry, and runner-issued attempt identity; its report is `audit/selection-validation.json`.

Row 34, concerning preorder support polynomials, is the closest topical library lead. The exact-title search here did not yield an inspectable primary record; the writing dossier also records failed primary-access routes. It was not used as mathematical evidence or inserted as an unverified citation. Other library subjects add no required source for this transfer proof. One well-supported methods reference is preferable to an unsupported extra entry.

The required literature-revision and handoff globs were enumerated before editing. There were no bibliography-revision files and no fast-completion handoff. The sole instruction-reading handoff's role, instruction-path, and accepted-snapshot predicates held. Both Crossref capture globs were enumerated before assessing access limitations and were empty; there was no saved authoritative Crossref response to discard. Direct DOI/Crossref/BibTeX-export requests for the library item failed in the web tool, and shell HTTP requests were denied by the network boundary. The live publisher's own full text and DOI-linked subject entry nevertheless establish the retained claim and metadata. A later direct Flajolet publisher fetch failed; its official publisher search record and author-hosted primary text supplied the required evidence. These access failures were not treated as mathematical outcomes.

No official exported BibTeX block was substituted or fabricated. Existing entries were retained after primary verification; only the missing, now independently verified DOI was added to `ZengEtAl26`. No citation key changed in this job. The pre-existing registry-to-manuscript key mapping is recorded above. `manuscript/main.tex` received only two presentation repairs: explicit link/cite/URL colors replaced `allcolors=blue`, and an explicit horizontal-space command before a telescoping equality was removed. The selection validator rejects those original constructs; the repairs preserve visible citation flow and every mathematical symbol.

The bounded fresh searches are recorded in `audit/citation-searches.json`. No equivalent resolution was located among the inspected results. This is not a global priority claim. The manuscript asserts only that its proof establishes the specific proposed factorization; it does not certify general preorder conjectures or external peer review.

## Final checks

The final clean LaTeX/BibTeX build converged with no warnings, unresolved references, missing keys, duplicate entries, or layout diagnostics. The bibliography checker reports five cited keys, five bibliography entries, and five matching auxiliary citation labels, with all missing/extra sets empty. All six final pages were actually viewed, including the five rendered reference entries and their ordinary-body citations. The build and visual observations are recorded separately in `audit/build.md` and `audit/visual.md` and bound to the same snapshot.

The runner-owned pre-publication hook was not invoked. No publication, submission, upload, or external communication was performed.
