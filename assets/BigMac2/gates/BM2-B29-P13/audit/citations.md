# Fresh citation audit

Release job: `bigMac-00029-p13-release-2f9da8670649`  
Search and review date: 2026-09-09 (Asia/Shanghai)  
Method: `$citation-check-skill`, search mode, applied as a fixed extraction pass followed by a verification pass.

## Pass 1: fixed claim extraction

The externally sourced or bibliographic claims in the final manuscript were frozen before verification as follows.

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | Raso and Venturi introduced the survivor-set objects, an exact covering characterization, and a dynamic recurrence. | Attribution/existence | p. 1, section 1 |
| C02 | Their exact covering criterion has the domains and covering condition reproduced in Lemma 1. | Attribution | pp. 1--2 |
| C03 | Their pointwise witness condition is necessary but not sufficient because excluded points can require incompatible residue choices at one modulus. | Attribution | p. 2, Remark 34 comparison |
| C04 | The cited Raso--Venturi item is a recent first version, so the comparison is limited to that paper and no broader priority claim is made. | Temporal/scope | p. 2 |
| C05 | The user-designated Zeng record has the title *A Strict Certified Search Extension for Erdős Problem 647* and is cited only as a title-level, certification-oriented methodological comparison. | Bibliographic attribution | p. 2 |
| C06 | The Zeng item supplies no survivor-set definition or theorem and no result from it is used in the proof. | Scope/existence | p. 2 and citation-use audit |
| C07 | The two bibliography entries have the rendered author, title, year, and identifier metadata shown on p. 5. | Bibliographic | p. 5 |

The finite theorem, exhaustive counts, certificates, and replay statements are mathematical claims already accepted against the frozen evidence in `audit/math.md`; this release pass checked that the manuscript did not strengthen that accepted scope.

## Pass 2: verification

| ID | Status | Basis |
|---|---|---|
| C01 | Verified (paraphrase) | The primary arXiv abstract and full HTML state the model and that the paper establishes an exact structural recurrence, a residue-class covering criterion for extendibility, and a dynamic enumeration algorithm. |
| C02 | Verified (exact mathematical match) | arXiv v1, Definitions 28--29 and Theorem 30 give the same admissible-residue domains, covered blocks, hypotheses, and if-and-only-if covering condition used in Lemma 1. |
| C03 | Verified (paraphrase) | arXiv v1, Corollary 33 and Remark 34 state that the witness condition is necessary but not sufficient because distinct excluded points may require incompatible choices at the same modulus. |
| C04 | Verified/appropriately bounded | The primary record reports v1 submitted 8 September 2026. The manuscript makes no general novelty or priority assertion. |
| C05 | Accepted from user record — external refresh unavailable | Metadata basis is the authoritative workbook record transcribed in `literature/user_bibliography_check.md`. All required title/author/year/DOI searches were attempted; no paper-specific primary record was accessible in the bounded release context. The manuscript was narrowed to the title-level comparison actually supported by the designated record. |
| C06 | Verified internally | `Zeng2026SSRN7379599` occurs only in the expressly limited comparison; no definition, lemma, theorem, proof step, table, or certificate depends on it. |
| C07 | Verified | The final `.bbl`, extracted PDF text, and rendered p. 5 resolve both keys. Raso--Venturi metadata agrees with the primary arXiv record. Zeng metadata reproduces the authoritative workbook record without alteration. |

## Sources and search coverage

- Primary Raso--Venturi record: <https://arxiv.org/abs/2609.08528>, including title, authors, subjects, v1 identifier, and submission history.
- Primary Raso--Venturi full text: <https://arxiv.org/html/2609.08528v1>, especially Definitions 28--29, Theorem 30, Corollary 33, Remark 34, and Proposition 36.
- User-designated authoritative bibliography record: `literature/user_bibliography_check.md`, transcribed from workbook `Zijian_Zeng_数学论文_BibTeX最终表_49条.xlsx`, worksheet `数学主表!A7:F7`.
- Authored dependencies: `manuscript/main.tex` and `manuscript/references.bib`; these are exactly the sorted `publication.json` `source_files`. `main.fls` shows no additional authored TeX, bibliography, figure, or local style dependency. System TeX packages and generated `.aux`/`.bbl` files are not authored source dependencies.

For each academic item, the applicable author/year/title, full-title index, author/year/venue, identifier, and DOI/arXiv queries required by the advisory skill were attempted. The Raso--Venturi source and exact cited passages were accessible. The Zeng DOI/SSRN refresh was inaccessible; under the user's authority rule, this is recorded as `metadata_basis=user_designated_workbook` and `external refresh unavailable`, not as a nonexistent or unverified bibliography record.

The extracted and rendered PDF has citations `[1]` and `[2]`, no question-mark placeholders, no undefined keys, and no contradicted attribution. The accepted finite theorem remains exactly scoped to levels through 24; the asymptotic question and broad priority remain explicitly unresolved/unclaimed.

## Verdict

**ACCEPT.** Citation existence and claim support are adequate at the stated conservative scope. The workbook-authoritative Zeng record is preserved, its inaccessible external refresh is disclosed, and unsupported stronger prose was repaired before this audit.
