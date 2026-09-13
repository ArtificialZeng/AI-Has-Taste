# Fresh citation and claim-support audit

**Mode:** Search verification with user-designated bibliography authority
override  
**Document:** `manuscript/article.tex` / `manuscript/article.pdf`  
**Search date:** 2026-09-08  
**Advisory method:** `$citation-check-skill`, two-pass architecture

## Pass separation and scope

Pass 1 is frozen separately in `audit/citation-check-pass1.md` and contains
the 26 extracted attribution, existence, comparative, temporal, ranking, and
numerical claims.  This report is pass 2 only; no claims were added or
re-extracted during verification.  The external searches used all applicable
academic-citation templates (author/title, exact title with arXiv or Semantic
Scholar restriction, author/year/venue, and DOI or arXiv identifier).

The complete publication dependency list was checked against the TeX source,
the recorder file, the bibliography, and every evidence file named in
`publication.json`.  The exact sorted scope is:

- `evidence/exact_scan.py`
- `evidence/resolution_check.py`
- `evidence/resolution_check_results.json`
- `manuscript/article.tex`
- `manuscript/references.bib`
- `source.md`

There are no imported authored TeX fragments, figures, local styles, or other
local bibliography databases.  System TeX packages and generated build files
are not publication sources.  The dependency scope is complete.

## Citation verification

### Gil--Liang--Odetola--Weiner

The official arXiv abstract and HTML full text confirm the title, four authors,
submission date 1 September 2026, identifier `2609.01562v1`, and primary class
`math.CO`.  Section 7 contains Proposition 7.2 with the displayed definitions
of `D` and `G`, Lemma 7.3 with the cited adjacent-ratio identity, the exact
statement that `rho(n)<1` was verified for `496 <= n <= 2000`, and Conjecture
7.4 with the universal threshold and its equivalent grid-traffic formulation.
The source also directly supports the manuscript's short description of the
lattice-path obstruction setting.  Claims C01, C06--C08, and C24 are verified
as exact or meaning-preserving paraphrases.  Sources inspected:
`https://arxiv.org/abs/2609.01562` and
`https://arxiv.org/html/2609.01562v1`, especially Section 7.

### Robbins

The official JSTOR issue record confirms Herbert Robbins, *A Remark on
Stirling's Formula*, *The American Mathematical Monthly* 62(1) (1955), pages
26--29, DOI `10.2307/2308012`.  A page image/text scan of the original article
was inspected: its opening formulas state
`n! = sqrt(2*pi*n)(n/e)^n exp(r_n)` with
`1/(12n+1) < r_n < 1/(12n)`.  These strictly imply the manuscript's weaker
two-sided inequalities in equation (6).  Claims C20 and C25 are verified.
Sources inspected: `https://www.jstor.org/stable/i314852` and the original
article scan indexed at `https://heuklyd.github.io/papers/pdf/Robbins-1955.pdf`.

### Zeng workbook record

The DOI resolver, alternative resolver, SSRN record endpoint, exact-title
search, author/title search, author/year/venue search, and DOI search did not
return a refreshable record within this bounded audit.  Under the explicit
authority rule in `literature/user_bibliography_check.md`, the workbook
`Zijian_Zeng_数学论文_BibTeX最终表_49条.xlsx` (worksheet `数学主表`, row 40;
recorded SHA-256
`93cd3aa74e2deac375e7e54b3a640cb457c186b0a8e90fa2c0afe7024f59a427`)
controls the supplied title, author, year, publisher, DOI, and URL.  Status:
**Accepted from user record — external refresh unavailable**.
`metadata_basis=user_designated_workbook`.

The nearby prose makes only the permitted methodological comparison.  The
workbook abstract specifically describes a uniform analytic tail from degree
5000 onward joined to exact finite integer verification and outward-rounded
rational intervals, so it supports the comparison without being used for any
grid-traffic formula, threshold, theorem, or priority claim.  Claims C09 and
C26 are supported at their stated narrow scope.  This refresh limit is not an
unverified-citation defect under the designated-authority rule.

## Fixed-claim verification results

| Claims | Result | Evidence and precision check |
|---|---|---|
| C01, C06--C08, C24 | Verified (exact/paraphrase) | Official arXiv metadata and Section 7 text match the attribution, range endpoints, and formulas. |
| C09, C26 | Accepted/verified at narrow scope | Authoritative workbook record and abstract; external refresh unavailable. |
| C20, C25 | Verified (exact) | JSTOR metadata and original Robbins formula; the manuscript explicitly uses a weaker consequence. |
| C02, C10--C12, C19 | Verified against primary research evidence | Algebra in the frozen proof and the accepted referee reconstruction matches the manuscript, with no strengthening beyond the accepted claim. |
| C03--C05, C13--C18, C21--C22 | Verified (exact) | Every integer, endpoint, count, range, ranking, and arithmetic qualifier exactly matches `evidence/resolution_check_results.json`, the executable source, and the accepted referee replay. No rounding is used. |
| C23 | Verified | The assistance statement matches `audit/math.md` and is explicitly limited; it makes no peer-review claim. |

All 26 fixed claims are therefore supported at their actual scope.  There are
zero numerical errors, contradictions, misleading attributions, unsupported
novelty claims, hallucinations, or unresolved claim-support items.  The
manuscript makes no broad priority assertion.  All three BibTeX keys used in
the source occur in `references.bib`, appear in the built reference list, and
have resolved numeric citations in the extracted PDF.  No cited item is
unnecessary: the arXiv source establishes the original conjecture, Robbins
supplies the classical bound, and the single workbook paper supplies the
carefully limited methodological comparison requested for the generated PDF.

**Verdict: ACCEPT.**
