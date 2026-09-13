# Fresh citation and claim-support audit

## Scope and method

Audit date: 2026-09-09.  I read both authored dependencies listed in
`publication.json`, the extracted three-page PDF, the fixed pass-1 claim list
in `audit/citation-claims.md`, the accepted mathematical scope, the local
Neunhäuserer source PDF, and `literature/user_bibliography_check.md`.
`citation-check-skill` was explicitly applied in two passes: extraction was
completed and frozen before this verification pass.  Web checks used primary
publisher, institutional, author-hosted full-text, and arXiv records.  The two
Zeng records use the user's designated workbook as authoritative metadata:
`metadata_basis=user_designated_workbook`; external refresh was unavailable in
scope.

The complete authored dependency scope is exactly `manuscript/main.tex` and
`manuscript/references.bib`.  The final `.fls` and Biber log show no other
authored TeX, style, figure, or bibliography input.  All five citation keys are
defined and rendered in the extracted PDF.

## Claim-to-source results

| Claim | Result | Evidence and exact support |
|---|---|---|
| C01 | Verified (paraphrase) | Shannon's two-part 1948 article exists with the stated author, title, journal, volume, year, and pages.  The prose was repaired so that natural logarithms and `0 log 0 = 0` are explicitly this manuscript's conventions, while Shannon is cited only for Shannon entropy. |
| C02 | Verified (paraphrase) | Neunhäuserer, arXiv:2609.05546v1, abstract and pp. 1, 3, introduces the recursive overlap construction and states Conjecture 3.1 for every layer. |
| C03 | Verified (exact scope) | The same paper's abstract, Proposition 3.1 on pp. 3–4, and section 4 prove the binomial/non-overlap extremes and report symbolic computations for additional sequence families. |
| C04 | Verified (scope) | `claim.json`, the accepted `audit/math.md`, and the manuscript itself all state the full three-bit result and explicitly exclude larger layers and priority claims.  No strengthening beyond the accepted scope was found. |
| C05 | Verified (exact) | Shepp and Olkin's chapter proves concavity of the binomial entropy on `0 <= p <= 1` (multinomial discussion and Theorems 3–4).  Primary metadata show that the chapter is in *Contributions to Probability*, Academic Press, 1981, pp. 201–206, DOI `10.1016/B978-0-12-274460-0.50022-9`.  The erroneous 1972 Berkeley metadata inherited from the source paper were repaired before the final build. |
| C06 | Verified against accepted mathematics | The five-profile universal classification is identical to the frozen accepted claim and to the reconstruction in `audit/math.md`; no citation is asked to prove it. |
| C07 | Verified against accepted mathematics | The curvature and endpoint statements match the frozen claim and accepted referee report exactly; no citation is asked to prove them. |
| C08 | Verified (paraphrase) | Neunhäuserer Proposition 3.1 identifies the binomial and completely non-overlapping extremes.  Comparing those definitions with the manuscript's exhaustive table supports the bounded rows 1/5 versus rows 2–4 statement.  The manuscript makes no broader priority claim. |
| C09 | Verified (exact) | Fresh execution with the required interpreter returned exact zero for all five profile identities, both derivative identities, and all five second-derivative identities. |
| C10 | Verified (exact) | Fresh execution with the required interpreter matched five representatives and exactly all 10,000 integer pairs in `1 <= u,v <= 100`; the nearby sentence correctly labels this finite computation corroborative. |
| C11 | Verified within designated-record scope | Workbook row 21 supplies the displayed title, author, year, DOI, and abstract.  The abstract supports only the narrow analytic-proof/exact-symbolic-check comparison.  The manuscript expressly says it does not support the entropy theorem.  Accepted from user record — external refresh unavailable. |
| C12 | Verified within designated-record scope | Workbook row 40 supplies the displayed title, author, year, DOI, and abstract.  The abstract supports only the narrow analytic-proof/finite-exact-check comparison.  The manuscript expressly says it does not support the entropy theorem.  Accepted from user record — external refresh unavailable. |

## Sources and bounded literature check

- Jörg Neunhäuserer, arXiv:2609.05546v1: official arXiv record and the local
  six-page PDF with SHA-256
  `3e1709d9010041ee3060a0daba79286edabd268c782629f653e98991775314f8`;
  relevant locations were the abstract, Conjecture 3.1, Proposition 3.1, and
  section 4.
- Claude E. Shannon, *A Mathematical Theory of Communication*: Wiley's
  publisher records for volume 27 issues 3 and 4 confirm the 1948 two-part
  metadata and pages 379–423 and 623–656.
- Lawrence A. Shepp and Ingram Olkin, *Entropy of the Sum of Independent
  Bernoulli Random Variables and of the Multinomial Distribution*: the
  author-hosted full text and publisher/Stanford records confirm both the
  binomial concavity claim and the corrected 1981 chapter metadata.
- User-designated workbook records documented in
  `literature/user_bibliography_check.md`, rows 21 and 40.  Their supplied
  DOI/BibTeX metadata control for this workflow because external refresh was
  unavailable in scope.

Searches for the exact three-bit expression, “three-bit overlap Bernoulli,”
weighted Bernoulli-sum entropy concavity, and finite-overlap Bernoulli
convolutions found no source contradicting the manuscript's deliberately
bounded comparison.  This is not asserted as a priority proof.  No citation is
contradicted, no attribution is overextended, and no useful citation remains
unverified under the designated-record rule.

## Verdict

**Accept.**  Citation metadata and nearby prose are supported at their stated
scope, the one discovered Shepp–Olkin bibliographic error was repaired, the two
user-workbook citations are used only for genuine methodological comparisons,
and the final PDF has no undefined citations.

