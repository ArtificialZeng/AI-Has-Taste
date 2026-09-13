# Verification Report

**Mode:** Search verification with frozen-primary fallback  
**Document:** `manuscript/main.pdf`  
**Generated:** 2026-09-07 (Asia/Shanghai)  
**Method:** `$citation-check-skill`, two separate passes

## Summary

| Metric | Count |
|---|---:|
| Total claims in fixed extraction | 14 |
| Verified | 14 |
| Numerical Error | 0 |
| Citation Not Found | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |

**Overall status:** PASS. The fixed pass-1 extraction is
`audit/citation_claims.md`; this report is the pass-2 verification and does not
add claims to that list.

## Claim-to-source verification

| ID | Status | Confidence | Verification |
|---|---|---|---|
| C01 | Verified | exact | The statement is identical in scope to `claim.json`; the current frozen evidence was accepted in `audit/math.md`. This citation audit does not substitute for that mathematical review. |
| C02 | Verified | exact | `evidence/verification.json` records 517 labelled ideals, split 64 and 453. |
| C03 | Verified | exact | `evidence/verification.json` records exact agreement of the primal and dual methods; `audit/referee_independent.json` records the third Fourier--Motzkin agreement. |
| C04 | Verified | paraphrase | The primary arXiv PDF defines the v-number on p. 1 and the monomial integral closure through its Newton polyhedron on pp. 1–2. The manuscript's minimal-generator formulation of the same Newton polyhedron is equivalent. |
| C05 | Verified | exact | The primary paper states the two-variable result as Theorem 3.2 (p. 6) and the three-variable equigenerated result as Theorem 3.12 (p. 9). The nearby manuscript text does not broaden either hypothesis. |
| C06 | Verified | exact | Example 3.3 (p. 6) gives `(x^2,y^2,z^5,xyz)` and the exact values 2 and 3. The manuscript's strict sign follows from those exact unequal values. |
| C07 | Verified | exact | The counts 64, 453 and 517 match `evidence/verification.json`; the displayed decomposition 372+27+54=453 is arithmetically exact. |
| C08 | Verified | exact | `evidence/verification.json` gives 31,922 expanded-grid points per method, 13,270 standard-box points per method, and 63,844 cross-method membership-bit equalities. |
| C09 | Verified | exact | The seven-bin distribution and zero violations match `evidence/verification.json` exactly and sum to 517. |
| C10 | Verified | exact | `audit/referee_independent.json` gives 1,034 socle lists, 3,552 socle exponents and 517 labelled ideals with exact agreement. |
| C11 | Verified | exact | Both frozen enumeration output and `audit/referee_independent.json` give `(2,3)` for the degree-five control; the external attribution is independently confirmed by Example 3.3. |
| C12 | Verified | paraphrase | The user bibliography row's abstract states characteristic zero, a structural reduction to 6,021 graph classes, exhaustive canonical enumeration, exact integer arithmetic, and an independently checkable verifier. The manuscript cites only this methodological analogy. |
| C13 | Verified | exact scope | The manuscript explicitly disclaims using the Zeng paper for integral closure, v-numbers, or the present boundary. Neither its title, abstract, nor keywords asserts one of those topics. |
| C14 | Verified | exact | `literature/user_bibliography_check.md` records a same-day check of the DOI content-negotiation metadata against workbook row 42: Zijian Zeng, exact title, 2026, Elsevier BV/SSRN, DOI `10.2139/ssrn.7385138`. |

## Sources consulted

1. Biswas, Mandal and Phukan, *A comparison of the v-number of a monomial
   ideal and its integral closure*, arXiv:2609.05044v1, 4 September 2026,
   14-page primary PDF. Author, title, date and version were read from the PDF;
   SHA-256 `e8ba90b5273578389918379df6e5b66fc899825ddb3b66dcb0f866f04e1561ab`
   matches `source.md`.
2. User bibliography workbook row `数学主表!A42:F42`, as transcribed and
   same-day metadata-checked in `literature/user_bibliography_check.md`.
   The narrow nearby sentence is supported by the row's abstract and does not
   use this paper for the theorem.
3. Frozen primary computation summaries `evidence/verification.json` and
   `audit/referee_independent.json`, plus the accepted mathematical report
   `audit/math.md`, for the paper's execution-record claims.

The mandatory academic search templates were attempted for both citations.
The web search surface returned no results, terminal DOI resolution failed,
and a single bounded Chrome DOI navigation timed out. This access limitation
does not leave a claim unsupported: the arXiv source was available as its
hash-matched primary PDF, while the user-list citation is limited to the
workbook abstract and the same-day DOI metadata record already preserved in
the project. No claim about the inaccessible paper's body is made.

## Citation and dependency scope

Both bibliography entries appear in `manuscript/main.bbl` and in the rendered
references on p. 4; all in-text citations resolve to `[1]` or `[2]`. There are
no undefined citations or references. Novelty language is bounded: the paper
does not attribute the new degree-four question to the cited authors and makes
no priority or journal-acceptance claim.

`publication.json` lists exactly `manuscript/main.tex` and
`manuscript/references.bib`. Inspection of `manuscript/main.fls` and all TeX
input commands found no authored imported TeX, local style, figure, or other
publication dependency. The source list is therefore complete.

