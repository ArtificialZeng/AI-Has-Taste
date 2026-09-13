# Fresh citation and claim verification report

**Mode:** Search verification, two passes  
**Document:** `manuscript/article.tex` and rendered `manuscript/article.pdf`  
**Search date:** 2026-09-07 (Asia/Shanghai)  
**Method:** Explicit application of `citation-check-skill`; the fixed extraction
is `audit/citation-claims.md`.

## Summary

The three curvature-flow references and every nearby claim made from them are
supported by primary arXiv or publisher text. The exact reproducibility counts
also match a fresh execution of the enumerated checker. One newly deposited
SSRN item selected from the user's bibliography remains a disclosed metadata
and text-access limitation: the local bibliography check records a same-day
Crossref verification, but fresh DOI, Crossref, SSRN, exact-title, author/title,
and exact-DOI requests in this release context returned either no indexed result
or an inaccessible endpoint. No curvature, transport, or priority claim is
assigned to that item, and the manuscript expressly limits it to a
methodological analogy.

**Verdict: accept with citation limitations.** There are no contradicted
citations, undefined keys, unsupported novelty claims, or misleading uses.

## Fixed-claim results

| ID | Status | Verification |
|---|---|---|
| C01 | Verified (paraphrase) | The arXiv record for Bai--Hua gives the displayed title, authors, 2026 date, version 1, and math.CO classification. The primary PDF abstract and Theorems 1.1--1.3 establish curvature diffusion/convergence and the convex-potential gradient description for finite trees; its introduction states that behavior on graphs with cycles remains open. |
| C02 | Verified (paraphrase) | The arXiv record and Johns Hopkins/AJM preprint give all five authors and the journal metadata `146 (2024), 1723--1747`. Definition 3 uses the shortest-path distance in the curvature denominator, and equation (4) is exactly the normalized continuous flow used in the manuscript. |
| C03 | Verified (paraphrase plus stated inference) | The arXiv record gives Bai, title, 2026, and v1. The primary PDF defines the lazy mass as uniform over neighbours and treats the short cycles, including `C_3`, in Section 6. Comparing that displayed kernel with the manuscript's inverse-weight kernel shows equality on the triangle only when all three incident-length pairs, hence all three lengths, are equal. The manuscript correctly says this adjacent calculation does not determine its inverse-weight fixed set. |
| C04 | Unverified in this fresh context (access limitation) | `literature/user_bibliography_check.md` records the user-workbook entry and a same-day Crossref check for Zijian Zeng, the displayed title, 2026, and DOI `10.2139/ssrn.7379198`, together with a narrowly permitted methodological use. Fresh mandatory author/title, full-title, venue, DOI, Crossref, and SSRN searches did not expose the record or text. The citation is retained only for the explicitly disclaimed methodological analogy; it supports no mathematical claim of this note. |
| C05 | Verified (exact) | Fresh execution of `python evidence/check_curvature.py` printed `exact checks passed: 13824 positive integer triples; 456 fixed triples`; the source loop is exactly `range(1,25)^3` and separately asserts the `(4,1,1)` curvature vector. Thus `24^3=13,824`, `456`, and the stated separate check match exactly. |
| C06 | Verified except for the disclosed C04 record | The compiled bibliography resolves all four keys. Primary records verify the exact metadata for Bai--Hua, Bai--Lin--Lu--Wang--Yau, and Bai; the Zeng record has the bounded access limitation above. |

## Primary sources inspected

- Bai and Hua, [arXiv:2609.04671v1](https://arxiv.org/abs/2609.04671),
  record and 12-page primary PDF: abstract, Introduction, Theorems 1.1--1.3,
  and Section 2.
- Bai, Lin, Lu, Wang, and Yau,
  [arXiv:2010.01802](https://arxiv.org/abs/2010.01802) and the
  [AJM author/publisher preprint](https://preprint.press.jhu.edu/ajm/sites/default/files/AJM-bai-lin-lu-et-al.pdf):
  Definition 3, equation (4), and publication metadata.
- Bai, [arXiv:2607.14748v1](https://arxiv.org/abs/2607.14748),
  record and 32-page primary PDF: Section 2 kernel definition and Section 6
  short-cycle treatment.
- `literature/user_bibliography_check.md` for the selected user-workbook record
  and its permitted narrow use; the fresh endpoint limitation is stated above.

## Dependency, resolution, and scope checks

`publication.json` enumerates the complete authored dependency set:
`evidence/check_curvature.py`, `manuscript/article.tex`, and
`manuscript/references.bib`. The TeX recorder file shows no imported authored
TeX, figure, or local style beyond these; `.aux`, `.bbl`, and `.out` are generated
build products. The extracted PDF contains four numbered, legible references,
and the BibTeX log reports four used entries and zero warnings. Every `\cite`
key occurs in the database and rendered references, so there are no undefined
citations. The accepted mathematical scope and the manuscript agree: this is a
partial result-note and makes no claim about nonstationary omega limits,
boundary dynamics, or absolute novelty.
