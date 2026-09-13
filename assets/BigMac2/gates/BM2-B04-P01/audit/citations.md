# Fresh citation and claim-support audit

Release job: `bigMac-00004-p01-release-4826a634131d`  
Search date: 2026-09-06  
Method: `$citation-check-skill` v2, search-verification mode, with separate
claim-extraction and verification passes.

## Bound material and scope

I read the complete authored dependency set in `publication.json`, the extracted
text and rendered references of the six-page PDF, the accepted mathematical
audit, and the cited primary records.  The bindings used here are research
snapshot `079e9113bb882a88ac5c2f62f841b0780dcb2f54f2d7ae330c8f4ced81548137`,
manuscript snapshot `9248dc0364747cfc845571c546dbc900d90f0ceaa6dd2800c697b5fa3a3325ce`,
and PDF SHA-256
`ca8b94bff18967835a2ea808ccbdd1b81166f640d1c001ec0b364116a4013e27`.

The complete authored source dependency list is exactly
`manuscript/main.tex` and `manuscript/references.bib`.  The TeX source imports no
local figures, styles, or subsidiary TeX files.  The bibliography database is
used and contains exactly the three rendered entries.  Generated auxiliary
files and system TeX packages are not authored dependencies.

## Pass 1: fixed claim extraction

The following list was fixed from the manuscript before source verification.
Definitions, proof steps proved in place, hypotheses, questions, and explicit
scope disclaimers were not treated as external factual claims.

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | Huang--Huh--Soskin--Wang identify reduced bounded ratios with the negative dual of the cut cone and conjecture the normalized bound 2. | Attribution/existence | PDF p. 1, context |
| C02 | Baldi--Kummer give a seven-point clique-web counterexample; for six points they record two additional hypermetric facet types and say their search found no counterexample there. | Attribution/existence | PDF p. 1, context |
| C03 | The fixed-locus supremum is exactly `8/(3 sqrt(3))`, geometric orbit averaging can leave the domain, and the target is outside the specified product cone. | Mathematical/existence | PDF pp. 1--5 |
| C04 | Every matrix in the stated domain has `p_ij >= 1`. | Mathematical/existence | PDF p. 4 |
| C05 | There are 60 triangular and 60 pentagonal lifts with the displayed exact histograms. | Statistic/mathematical | PDF p. 5 |
| C06 | The companion checker performs 120 exact integer evaluations and no theorem uses floating-point evidence. | Statistic/existence | PDF p. 5 |
| C07 | Zeng--Liu--Ratnavelu--Huat--Xiong use exact rational, algebraic, and Bernstein certificates on delimited regions in a different Hermitian scalar-gate problem. | Attribution/existence | PDF p. 5 |
| C08 | A language model assisted; the listed identities and enumeration were checked exactly; no formal proof assistant was used. | Method disclosure | PDF p. 5 |
| C09 | The Baldi--Kummer bibliography metadata (authors, title, year, arXiv ID, URL, DOI) is accurate. | Attribution/metadata | PDF p. 6 |
| C10 | The Huang--Huh--Soskin--Wang bibliography metadata is accurate. | Attribution/metadata | PDF p. 6 |
| C11 | The Zeng et al. bibliography metadata, SSRN posting date, URL, and DOI are accurate. | Attribution/metadata | PDF p. 6 |

## Pass 2: verification

| ID | Status | Evidence and exact support |
|---|---|---|
| C01 | Verified (paraphrase) | The official arXiv record and v2 PDF for `2510.25030`, Theorem B (printed p. 5) and Conjecture 1.9 (printed pp. 7--8), state the dual-cut-cone characterization and normalized bound by 2. Authors, title, v2 date (2025-11-08), and arXiv-issued DOI agree with the bibliography. |
| C02 | Verified (paraphrase) | The official arXiv record and retained v1 PDF `literature/Baldi-Kummer-2609.03934v1.pdf`, Section 3 (printed pp. 3--4), identify the seven-point non-hypermetric clique-web facet, state that two new hypermetric inequalities are needed for `Cut_6`, and explicitly say the authors were unable to produce a counterexample for them. The manuscript correctly warns that this is not a proof. |
| C03 | Verified at accepted scope | The exact three-part statement is identical in substance to `claim.json`; `audit/math.md` accepts that precise frozen statement and reconstructs each proof. The manuscript does not strengthen it to the unresolved full six-point problem. |
| C04 | Verified at accepted scope | The principal `2 x 2` interlacing argument appears in the accepted proof and is stated with the same hypotheses in the manuscript. |
| C05 | Verified (exact) | The accepted referee independently obtained the two histograms. A fresh execution of `evidence/check_typeII_product_dual.py` returned triangular counts `(-4:4,-2:46,0:10)`, pentagonal counts `(-6:12,-4:28,-2:16,0:4)`, and verified the separator over integers. |
| C06 | Verified (exact) | The two 60-element families total 120. The checker uses standard-library combinatorial generation and integer arithmetic; the proofs and accepted audit distinguish exact calculations from numerical evidence. |
| C07 | Verified (paraphrase) | The official SSRN record for abstract `7348478` lists the five authors in the manuscript order and describes exact rational certificates and exact Bernstein controls on explicit restricted regions. The manuscript explicitly limits the comparison to methodology and denies relevance to bounded ratios or cut cones. |
| C08 | Verified as disclosure | The statement is a bounded method disclosure, consistent with the accepted audit and the actual exact checker. It makes no claim of formal verification or independent peer review. |
| C09 | Verified (exact metadata) | Official arXiv record `2609.03934v1`: Lorenzo Baldi, Mario Kummer, *A note on bounded ratios*, submitted 2026-09-03, `math.CO`, arXiv-issued DOI `10.48550/arXiv.2609.03934`. The DOI was marked pending registration by arXiv on the search date; the authoritative arXiv record itself supplies it. |
| C10 | Verified (exact metadata) | Official arXiv record `2510.25030v2`: Daoji Huang, June Huh, Daniel Soskin, Botong Wang, *Bounded ratios for Lorentzian matrices*, v2 2025-11-08, arXiv-issued DOI `10.48550/arXiv.2510.25030`. |
| C11 | Verified (exact metadata/paraphrase) | The official SSRN indexed record gives the exact title and author order, date written 2026-08-25, 31 pages posted 2026-08-27, abstract ID `7348478`, and DOI `10.2139/ssrn.7348478`. |

The academic-citation searches used the prescribed author/year/title,
full-title repository, author/year/venue, DOI, and (where applicable) arXiv-ID
queries.  The directly opened SSRN page returned HTTP 403 after the official
indexed result had supplied the primary record and abstract; no claim relies on
an inaccessible passage.  The arXiv pages and PDFs were directly inspected.

## Result

All 11 extracted claims are verified at the scope stated.  There are no
undefined citations, missing bibliography entries, numerical errors,
misquotations, unsupported novelty assertions, or misleading upgrades of the
accepted partial result.  The closest-result comparison is appropriately
bounded to Huang et al. and Baldi--Kummer.  The user-bibliography paper is
genuinely relevant only as a methodological comparison and is cited only for
that supported point.

