# Verification Report

**Mode:** Search verification; $citation-check-skill v2, advisory two-pass audit.
**Job:** `bigMac-00012-p02-release-436e003549d5`; **date:** 2026-09-08.
**Document:** `manuscript/main.pdf`; **verdict:** accept.

| Metric | Count |
|---|---:|
| Fixed claims extracted | 29 |
| Verified against primary sources, accepted mathematics or exact evidence | 26 |
| Accepted with user-record basis / limited methodological interpretation | 3 |
| Numerical errors / contradicted attributions / undefined citations | 0 |
| Records unverified for this workflow | 0 |

Pass 1 is saved in `audit/citation-claims.md`; this is the separate verification
pass. The user authorized this bounded autonomous job, so the advisory skill's
confirmation pause was not used. Repeated claims were grouped at extraction.

| Claim | Status | Evidence and scope |
|---|---|---|
| C01 | Verified: exact | Accepted claim and audit/math.md; fresh exact and referee verifier outputs reproduce all four factors. |
| C02 | Verified: exact | Each displayed residual has no indicated right descent; complete parabolic suffix enumeration confirms greatestness. |
| C03 | Verified: exact | Accepted Theorem 2 scope; the exact left-descent set is {b,d}; centrality identifies the image set. |
| C04 | Verified: paraphrase | Primary preprint Corollary 4.7, p.16, with Definitions 4.1–4.3, p.14; the manuscript checks regularity and fixedness. |
| C05 | Verified: exact | Displayed signed-permutation model, D4 graph and accepted certificate. |
| C06 | Verified: exact | Primary preprint Section 4.3, p.19: the even-Dr, i=1 conjecture has precisely this D4 specialization. |
| C07 | Verified: paraphrase | Primary Lemma 3.14, pp.13–14, assumes breadth at least 3. Here breadth is 4; the introductory comparison is within that setting. |
| C08 | Verified: mathematical scope | The usual braid-move consequence of Matsumoto is explicitly part of the accepted mathematical argument. No new theorem or page-specific attribution to Humphreys is asserted. |
| C09 | Verified: paraphrase | Publisher metadata/contents and original-book preview: Sections 1.6–1.10; Proposition 1.10(c), pp.19–20, gives unique length-additive parabolic decomposition. |
| C10 | Verified: mathematical scope | Lemma 1 is proved in the manuscript and accepted referee report. Proposition 1.10(c) supplies the standard Coxeter component; all four actual tails are separately exhaustively certified. |
| C11 | Verified: exact | Fresh exact output: 12 positive roots and the displayed integer reflection matrices. |
| C12 | Verified: exact | Primary preprint equation (4.9), Section 4.3, p.17; substitution r=4 gives bacbacdcbacd. |
| C13 | Verified: exact | Both implementations return longest element -I4, length 12, and the two reduced words. |
| C14 | Verified: exact | Fresh outputs give precisely the four table rows and counts 6,12,3,4; every rendered table value agrees. |
| C15 | Verified: exact | Fresh integer lengths give 12=9+3, 9=4+5, 4=2+2, 2=0+2 without rounding. |
| C16 | Verified: exact | All seven root images in the manuscript match the fresh exact-verifier vectors and are positive. |
| C17 | Verified: exact | Accepted left-descent calculation and fresh reconstruction give descents b,d only; displayed multiplication lengths agree. |
| C18 | Verified: exact | D4 adjacency and independent signed-permutation reconstruction give empty S1 perp and {b,d}. |
| C19 | Verified: exact | Longest element is -I4; primary preprint Proposition 2.6, p.5, also lists even D as central. |
| C20 | Verified: exact | Displayed covering is proper and both induced graphs connected. Primary Definitions 4.2–4.3, p.14, show centrality implies fixedness and regularity. |
| C21 | Verified: exact | Primary Corollary 4.7, p.16, applies at base exponent 1 and Definition 4.1, p.14, is exactly (3.1). |
| C22 | Verified: exact | Manuscript substitution m=pt and m=p preserves both universal quantifiers and endpoint cases; accepted referee scope unchanged. |
| C23 | Verified: exact | Fresh verifier outputs saved locally: group order 192, parabolic orders 6 and 24, exhaustive suffix counts 6,12,3,4. |
| C24 | Accepted from supplied record | User bibliography title and annotation directly support the finite-symmetric-group two-generation topic. External refresh unavailable. |
| C25 | Accepted: limited interpretation | literature/user_bibliography_check.md describes exact deductive finite-permutation-group classification with explicit generators. The comparison is expressly methodological, with no theorem borrowed; full-text refresh unavailable. |
| C26 | Verified: scope | The accepted frozen claim covers precisely D4 and all p,t>=1, with no Condition B, larger-r or ordering claim. |
| C27 | Verified: metadata | Current arXiv record confirms authors, record title and 4 September 2026 v1 submission. The local primary PDF has the different typeset title stated in source.md; the version identifier is unambiguous. |
| C28 | Verified: metadata | Cambridge publisher record confirms author/title, 1990 print publication and DOI; publisher frontmatter identifies the book and series; original title-page preview corroborates 1990. |
| C29 | Accepted from user record | metadata_basis=user_designated_workbook; authoritative worksheet 数学主表 row 45, transcribed in literature/user_bibliography_check.md. DOI and all supplied metadata retained; external refresh unavailable. |

## Source checks and limitations

The Fromentin–Godelle original PDF was copied into
`audit/source-material/2609.04757v1.pdf`; its SHA-256 is
`eac47298f884caf5150f75e3b5b6229d90d4cf58d79d8e9badce7ad4ab57daec`.
I read the actual passages in Definitions 4.1–4.3, Lemma 3.14, Corollary 4.7,
equation (4.9), Proposition 2.6 and the p.19 conjecture. The hypotheses and
source-relative comparison are preserved. The submission date differs from the
typeset PDF's internal date (September 7); the bibliography correctly identifies
the arXiv submission date. Its title follows the current arXiv record, while the
primary PDF's typeset title is “Alternating Decomposition of a Product in a
Spherical Type Artin-Tits Monoid.” No exhaustive novelty or priority is claimed.
[Current arXiv record](https://arxiv.org/abs/2609.04757).

Humphreys is a background citation. Publisher metadata and contents confirm the
record; the original-book preview supplies Proposition 1.10(c), pp.19–20:
unique minimum coset representatives and length additivity. The preview is an
OCR reproduction, so no exact quotation is made and it is not described as a
complete fresh review of the book. Lemma 1 and its four applications remain
supported by the accepted proof and independent exact certificate.
[Publisher record](https://www.cambridge.org/core/books/reflection-groups-and-coxeter-groups/2910C1E00877D33A04A512791B6EDD72/listing),
[original-book preview](https://www.scribd.com/document/577474129/Reflection-Groups-and-Coxeter-Groups-James-E-Humphreys).

The selected user-list paper is genuinely relevant to the stated narrow
comparison of exact finite-permutation-group work. It is cited once for that
purpose and is not a premise of the proof. The authoritative supplied record is
`Zijian_Zeng_数学论文_BibTeX最终表_49条.xlsx`, worksheet `数学主表`, row 45,
workbook SHA-256 `93cd3aa74e2deac375e7e54b3a640cb457c186b0a8e90fa2c0afe7024f59a427`,
as transcribed and annotated in `literature/user_bibliography_check.md`.
The workbook itself was not reopened in this job. The prior official API match
in that file is recorded evidence, not a new retrieval by this worker.
Fresh direct access and the four applicable title/author/venue/DOI searches did
not refresh the record. Its status is **Accepted from user record — external
refresh unavailable**, with `metadata_basis=user_designated_workbook`.
The DOI `10.5281/zenodo.22293146` and metadata remain unchanged. Available supplied
annotations support only the modest comparison used; no detailed theorem from
that paper is attributed or needed. This access limit does not invalidate its
workflow metadata or justify treating the record as nonexistent.

## Dependency and final PDF audit

The complete authored dependency list is exactly `manuscript/main.tex` and
`manuscript/references.bib`, sorted as in `publication.json`. I checked every
source directive, the recorder `main.fls`, the BibTeX log and generated BBL.
No local custom style, imported authored TeX or figure is missing. Generated
AUX/BBL/OUT files and system TeX packages are not authored dependencies.
All three citation keys have defined BibTeX entries and resolved numbered
references in the extracted and visually inspected final PDF. Lemma/theorem/
corollary and equation references also resolve. The table is an exact certificate,
with every count and word checked against the saved execution output; there are
no statistical charts. No source or mathematical-scope repair was necessary.

This audit concerns release consistency and citation support. The existing
fresh referee acceptance is the mathematical review; a passing audit or build
is not itself a proof.
