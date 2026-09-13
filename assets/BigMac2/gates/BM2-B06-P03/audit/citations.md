# Verification report

Mode: Search plus user-designated bibliography authority.
Job: `bigMac-00006-p03-release-45c673bd9503`. Date: 2026-09-08.
Document: `manuscript/main.tex` and its three-page compiled PDF.
Method: explicitly invoked `$citation-check-skill`, used as an advisory audit.

## Summary

| Finding | Count |
|---|---:|
| Fixed extracted claims | 15 |
| Verified against accepted proof, exact recomputation, or primary text | 13 |
| Accepted within supplied workbook metadata/relevance scope | 2 |
| Numerical errors, contradictions, misleading attributions | 0 |
| Undefined citation keys | 0 |

Verdict: **accept**, under the user's bibliography authority rule. This is not
a statement that the unavailable Zeng full text was independently inspected.
The full citation scope and external-refresh limit remain disclosed below.

## Fixed claim-to-evidence mapping

Pass 1 was saved before verification in `audit/citation-extraction.md`. All
15 fixed claims were then checked, in this order. Grouped occurrences include
the abstract and later repetitions; no additional claims were introduced.

| ID | Result and evidence |
|---|---|
| C01 | Verified, exact. The accepted referee recurrence and fresh integer calculation both give b(5)=25056=5*5011+1. Both frozen Euler-product programs were executed again; see `evidence/release-coefficients.json`. |
| C02 | Verified, exact. The frozen quantifier is n>=1. At n=1 the value is nonzero modulo five, so it is the least admissible counterexample and a full disproof of this particular statement. |
| C03 | Verified, exact formula. The primary version-1 HTML equation (1.2) has the three exponents printed in manuscript equation (1). Positive integer color/tuple parameters cover the specializations actually used. |
| C04 | Verified, exact substitution: (3*4-2*4)*2=8, 2*4*2=16, (4-4)*2=0. |
| C05 | Verified from the formal-product construction: factors with first nonconstant degree exceeding N do not affect the coefficient of q^N; the constant-one denominator factors have integral inverses. |
| C06 | Verified, exact parameter. Version-1 Conjecture 7.1, fifth displayed congruence, is b-bar with r=s=k=4 and n>=1. The manuscript consistently keeps k=2 separate. |
| C07 | Verified against the accepted proof. Each logarithmic derivative contributes the displayed signed double sum; F has constant term one. |
| C08 | Verified against the accepted proof and coefficient comparison. The second double sum contributes only at even j, giving the stated divisor-sum correction. |
| C09 | Verified, exact. Fresh divisor-sum evaluation returns (16,32,64,64,96). |
| C10 | Verified, exact. Fresh recurrence and the two frozen product programs agree on (1,16,144,960,5264,25056). |
| C11 | Verified, exact. The displayed integer sum is 125280=5*25056. No numerical rounding or extrapolation occurs. |
| C12 | Verified, exact specialization of primary equation (1.2): k=4 gives f2^16/f1^32. The scope limitation agrees with `claim.json` and `audit/math.md`. |
| C13 | Accepted within supplied relevance scope, confidence: interpretation. `literature/user_bibliography_check.md` explicitly identifies generating-function coefficient analysis separated from independent exact finite diagnostics as the permissible comparison. The paragraph makes only this comparison and uses no cycle-length theorem. Full-text refresh was unavailable. |
| C14 | Verified, bibliographic. The arXiv search record and primary version-1 HTML header confirm both authors, title, version, math.NT class, and 3 September 2026 date. |
| C15 | Accepted from user record — external refresh unavailable. DOI, title, author, year, and publisher agree with the supplied workbook BibTeX extract, which is preserved verbatim. The threshold in the title is bibliographic text, not a theorem asserted here. |

The reproducible release calculations and source integrity checks are in
`audit/release-validation.py` and `evidence/release-validation.json`. They
support consistency review; the accepted mathematical audit remains the
mathematical acceptance record. The manuscript introduces no stronger result,
broader quantifier, or claim that the source's different conjecture is settled.

## Sources and access scope

- [Thejitha--Fathima, version-1 primary text](https://arxiv.org/html/2609.03926v1):
  header, equation (1.2), and Conjecture 7.1 were inspected directly. These are
  the only external mathematical attributions. No claim of exhaustive
  literature coverage, priority, or the current open status of k=4 is made.
- User-designated workbook record: `literature/user_bibliography_check.md`,
  identifying `Zijian_Zeng_数学论文_BibTeX最终表_49条.xlsx`,
  `数学主表!A40:F40`. **metadata_basis=user_designated_workbook**;
  **external refresh unavailable** for DOI 10.2139/ssrn.7380519 and its full
  text. The full workbook is not present locally; this audit uses the supplied
  extract and relevance assessment. Its reported prior Crossref match was
  not independently refreshed. The preserved article is genuinely relevant
  only for the narrow methods comparison C13. It supplies no partition claim.

The exact applicable search queries, primary URLs, endpoint outcomes, and
limits are recorded in `audit/release-web-check.md`. Optional access failures
have not been interpreted as nonexistence. No unnecessary citation was added
to reach a count; one relevant paper from the user's Excel list is present.

## Complete dependency and rendered-reference review

The exact sorted dependency list is:

1. `manuscript/main.bbl`
2. `manuscript/main.tex`
3. `manuscript/references.bib`

The whole TeX source, BibTeX database, and BBL were inspected. The TeX has no
local imported sections, figures, scripts, or custom styles; its sole explicit
bibliography input is `references.bib`, and biblatex loads `main.bbl`.
All other loaded classes, fonts, and packages in the actual log are system
TeX installations. Thus `publication.json` covers every local authored or
generated source dependency of this PDF. Generated aux/out/bcf files are
compiler intermediates, not additional authored inputs.

Both citation keys occur in the database and BBL, and both bibliography
entries appear on rendered page 3. The references in the text render as [1]
and [2], equation references resolve to (1)--(5), and Theorem 1 is resolved.
Neither text extraction nor direct page inspection found raw keys or question
marks. The user-supplied DOI appears correctly in the rendered bibliography.

No source, PDF, bibliography, mathematical evidence, or frozen snapshot was
modified in this release audit.
