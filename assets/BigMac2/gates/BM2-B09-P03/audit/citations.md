# Fresh citation and claim audit

Release job: `bigMac-00009-p03-release-5e52c78d86fd`  
Search date: 2026-09-07 (Asia/Shanghai)  
Method: `$citation-check-skill` v2, search mode, followed by primary-source
manual inspection and frozen-evidence traceability.

## Scope and fixed pass-one extraction

I read the complete authored dependency set (`manuscript/main.tex` and
`manuscript/references.bib`) and the complete four-page PDF before doing any
verification.  The following claim list was then frozen for pass two; no
claims were added while checking it.

| ID | Extracted claim | Type | Location |
|---|---|---|---|
| C01 | The paper studies the full union of four order-four almost-Sarymsakov levels under one common ordering. | Existence | Abstract; pp. 1--2 |
| C02 | The exact uniform scrambling horizon is 11, uniformly for arbitrary positive compatible stochastic weights. | Statistic + existence | Abstract; Theorem 1, p. 2 |
| C03 | There are exactly \(15^4=50{,}625\) row-nonempty supports; the nonscrambling frontier has 120 states at length 10 and none at length 11. | Statistics | Abstract; pp. 3--4 |
| C04 | The definitions used are Hsu's Definition 3, including the nested GR/GE and lower-left access conditions. | Attribution | p. 1 |
| C05 | Hsu's Theorem 5 gives \((4-1)(4-1)!=18\), and Remark 5 proves sharpness only for order three. | Attribution + statistics | p. 2 |
| C06 | Nonnegative support multiplication is Boolean multiplication, admission depends only on support, and every row-nonempty support has a positive stochastic realization. | Existence + causal | Lemma 2, p. 2 |
| C07 | Scrambling is preserved by left multiplication with a row-allowable support. | Existence | Lemma 3, p. 2 |
| C08 | The four level counts are 4096, 15806, 25462, and 35347, with a union of 37,833 supports. | Statistics | p. 3 |
| C09 | Recurrence (1) gives every and only nonscrambling product state at each exact depth. | Existence | Proposition 4, p. 3 |
| C10 | The displayed frontier sequence is \(1,19946,13532,9802,6258,3332,1720,988,566,316,120,0\). | Statistics | table, p. 3 |
| C11 | The independent checker scans all \(2^{16}\) Boolean relations and compares 37,833 alphabet and 56,581 frontier entries using exact integer operations. | Statistics + existence | p. 3 |
| C12 | Zeng's cited cellular-automaton work also separates an exact finite-state model, theorem, and independent exact computations. | Attribution + comparative | p. 3 |
| C13 | The ten displayed supports are legal and multiply cumulatively to `17ef`, whose second and fourth row masks are disjoint. | Statistics + existence | table and text, p. 4 |
| C14 | The bibliography identifies Hsu's 2026 arXiv v1 paper by author, title, identifier, subject record, and arXiv-issued DOI. | Citation | reference [1], p. 4 |
| C15 | The bibliography identifies Zeng's 2026 SSRN preprint by author, title, and DOI. | Citation | reference [2], p. 4 |

Definitions, proof steps, explicitly bounded limitations, and the assistance
disclosure were not extracted as external factual claims under the skill's
exclusion rules for definitions and methodology descriptions.

## Pass-two verification

| ID(s) | Status | Source and exact check |
|---|---|---|
| C01, C04, C05, C14 | Verified (exact) | The primary arXiv record `https://arxiv.org/abs/2609.05050` gives Shun-Pin Hsu, the exact title, submission date 4 September 2026, `math.DS`, identifier `2609.05050v1`, and the arXiv-issued DOI (noted there as pending registration).  I also inspected the primary eight-page PDF with SHA-256 `30a7f91e362d4a6375b743950618c94454219cce064c11d027ae108c9abc257f`.  Definition 3 on p. 5 is exactly the union of accessible nested-expansion levels; Theorem 5 on p. 6 states \(L_n=(n-1)(n-1)!\); Remark 5 on p. 6 says the bound is not generally claimed sharp but is sharp for \(n=3\).  Substitution \(n=4\) gives 18 exactly. |
| C02, C03, C06--C11, C13 | Verified (exact) | These mathematical and numerical claims agree without strengthening with `claim.json`, the accepted report `audit/math.md`, and its snapshot-bound exact certificate checks.  Counts, witness factors, factor levels, cumulative products, final masks, and the 11-step empty frontier all match exactly.  The release audit treats that accepted mathematical audit as the correctness authority and separately checked that the manuscript's scope is identical. |
| C12 | Unverified in the fresh release context | `literature/user_bibliography_check.md` records a same-day Crossref check of DOI `10.2139/ssrn.7379379` and reports an abstract supporting precisely this finite-state/checking comparison.  I ran the applicable author/title, exact-title/index, venue, DOI, and SSRN-record searches.  The fresh Crossref/SSRN record and original text did not resolve within the bounded audit window.  The sentence is deliberately narrow, supplies no stochastic-matrix result, and is retained only to satisfy the user's bibliography requirement. |
| C15 | Verified from the recorded same-day metadata check, with fresh-access limitation | Author, title, year, and DOI agree exactly between the BibTeX entry and `literature/user_bibliography_check.md`; direct fresh primary-record resolution was unavailable as described for C12. |

There are no numerical mismatches, contradicted attributions, misleading
scope changes, or unsupported novelty claims.  The manuscript expressly says
that its comparison is only with Hsu's cited version and makes no worldwide
priority claim.

## Search record and source mapping

For Hsu I ran all applicable templates: author/year/title prefix, exact title
restricted to Semantic Scholar or arXiv, author/year/venue, DOI, and arXiv-ID
queries.  The authoritative arXiv landing record and the primary PDF supplied
the metadata and cited passages.  For Zeng I ran the author/year/title prefix,
exact-title/index, author/year/SSRN, DOI, and SSRN identifier queries; the
fresh metadata/full-text endpoints remained unresolved, so no stronger claim
is made from them.

The citation-to-claim mapping is: `Hsu2026` supports only C01, C04, C05, and
C14; `Zeng2026Rule115` supports only the methodological C12 and its own C15
metadata.  Neither citation is used as evidence for horizon 11 or for any
certificate count.

## Dependency and rendered-reference audit

`publication.json` lists exactly the complete authored dependency set,
sorted as `manuscript/main.tex`, `manuscript/references.bib`.  The TeX source
has no local `input`, `include`, graphics, or custom-style dependency.  The
recorder file contains only the authored `main.tex` plus generated local
`main.aux`, `main.bbl`, and `main.out`; BibTeX's log identifies
`references.bib` as its sole database.  Both source files were read.

The three citation occurrences have matching bibliography keys; `main.aux`
contains both `bibcite` records; the final log has no undefined citation or
reference diagnostic.  Text extraction and the inspected rendering show two
resolved, readable references on p. 4.  Thus dependency scope is complete and
`undefined_citations=false`.

## Verdict

**Accept with citation limitations.**  Hsu's substantive citation is fully
verified against the primary record and text.  The nonessential Zeng
methodological comparison is conservatively disclosed as fresh-record/text
unverified; this is solely a temporary metadata/text-access limitation, not a
contradiction or support for the mathematical result.
