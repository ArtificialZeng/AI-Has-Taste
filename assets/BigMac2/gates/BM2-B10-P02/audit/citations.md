# Fresh citation and dependency audit

Release job: `bigMac-00010-p02-release-93e775dd2753`  
Search date: 2026-09-07 (Asia/Shanghai)  
Method: `$citation-check-skill`, search-verification mode, with extraction and
verification performed as two separate passes.

## Pass 1: fixed extraction

The following are all externally sourced claims attached to the manuscript's
two citations.  The paper's new theorem and its proof are self-contained
mathematical claims already bound to the accepted mathematical audit, rather
than claims attributed to outside sources.

| ID | Extracted claim | Type | Location |
|---|---|---|---|
| C01 | Mossel's paper is *Consensus times for monotone aggregation dynamics*, by Elchanan Mossel, arXiv:2609.04468v1 (2026), math.PR. | existence / metadata | p. 1 and Reference 1 |
| C02 | Mossel studies the same discrete-time asynchronous model: one uniformly chosen updating agent and iid uniformly sampled inputs, with replacement. | attribution | p. 1 |
| C03 | Mossel's Theorem 1(iii), specialized to the displayed rule whose residual minterm has size two, gives worst-case order `Theta(N^(3/2))`. | attribution | p. 1 |
| C04 | Mossel's Proposition 13 and Sections 2.6--2.7 supply a finite birth--death Green-function/scale-function framework. | attribution | p. 1 |
| C05 | Zeng's distinct-cycle-length paper combines a uniform coefficient estimate with exact verification of a remaining finite range. | attribution / methodological comparison | p. 5 and Reference 2 |

No verification was mixed into this extraction pass, and this list was held
fixed for Pass 2.

## Pass 2: verification findings

| ID | Status | Evidence and scope |
|---|---|---|
| C01 | Verified (exact) | The primary arXiv record gives the exact title, author, category, identifier, v1 date (3 September 2026), and arXiv-issued DOI. |
| C02 | Verified (paraphrase) | The primary arXiv abstract and Section 1.1 specify the same update agent, iid uniform input indices, independence, and sampling with replacement. |
| C03 | Verified (paraphrase) | The primary text's Theorem 1(iii) and Theorem 22 state `Theta(N^(2-1/m))`; for `x1 OR (x2 AND x3)` the residual rule is `x2 AND x3`, so `m=2` and the exponent is `3/2`.  The manuscript does not attribute its sharp constant or profile to Mossel. |
| C04 | Verified (paraphrase) | Proposition 13 explicitly gives the killed-chain Green function and absorption-time sum; Sections 2.6--2.7 develop the potential and scale-function estimates. |
| C05 | Unverified because of bounded access | The local workbook check records an earlier Crossref comparison of exact title, author, year, DOI, and abstract and limits its permitted use correctly.  In this fresh release context, all required title/author/venue/DOI queries were attempted, but the new SSRN item was not indexed by the available search results, direct SSRN/DOI/Crossref pages were rejected by the web fetcher, and the shell had no DNS access.  The original text therefore could not be freshly inspected. |

Primary Mossel record inspected:
`https://arxiv.org/abs/2609.04468` and
`https://arxiv.org/html/2609.04468v1`, including Theorem 1(iii), Proposition
13, Sections 2.6--2.7, and Theorem 22.  For Zeng, the bounded searches included
the exact title, author/year/venue, DOI `10.2139/ssrn.7380519`, SSRN identifier,
and the required Semantic Scholar/arXiv variants.  No contrary record was
found; lack of fresh access is not treated as verification.

The Zeng citation is retained because the user-supplied bibliography check
identifies it as the relevant selected paper and the nearby sentence is
explicitly confined to a proof-architecture analogy.  It supports no claim
about consensus dynamics, the sharp constant, or priority.  This disclosed
text-access limitation warrants `accept_with_citation_limitations`; it does
not conceal an unsupported substantive or novelty claim.

## Resolution and dependency checks

- Both BibTeX keys used in `paper.tex` occur exactly once in
  `references.bib`, appear as References [1] and [2] in extracted and rendered
  PDF text, and produce no undefined-citation diagnostic.
- `publication.json` lists the complete authored dependency set:
  `manuscript/paper.tex` and `manuscript/references.bib`.  The recorder file
  shows no other project-local imported TeX, figure, style, or bibliography
  input.  Generated `.aux`, `.bbl`, log, and PDF files are not authored source
  dependencies.
- The manuscript's prior-result language is bounded: it calls Mossel the
  closest inspected result and expressly disclaims literature priority.
- The theorem statement matches the accepted frozen claim; no unsupported
  strengthening was found.

**Verdict:** accept with the single citation-access limitation above.
