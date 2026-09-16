# Fresh citation audit

## Method and frozen claim surface

I used the search mode of the citation checker in two non-interleaved passes.
Pass 1 extracted and froze eight claims in
`audit/citation-claim-ledger.json`.  After the only source edits (a corrected
arXiv class/DOI and PDF metadata), the same eight claims and line locations
were refrozen against manuscript digest
`aae6824c8f37b22a67011e318d360974074f43b469c386a9ecff430c7ad10cd7`;
no substantive claim changed.  Pass 2 verified those fixed claims in order,
with detailed source locations in `audit/citation-source-verification.json`.
The audit was performed serially because the job explicitly prohibited agents.

## Findings

All eight claims are verified.  The three cited records exist, their retained
author/title/year/version/venue fields agree with primary or institutional
records, and their cited passages support the nearby text:

* Sun, arXiv:2609.04176v1: local primary PDF pp.13--14, Lemma 6.6,
  (6.7)--(6.10) and (6.24).  These passages state the identity, finite ladder
  sorting, exact cell verification, and 178 merged cells.  No cell ledger or
  checker is supplied in the article.  The official arXiv record identifies
  `math.GM`, not the draft bibliography's `math.NT`; this was corrected and the
  arXiv-issued DOI was added.
* Embrechts--Hofert: Definition 2.1, Remark 2.2 and Proposition 3.1(2) in the
  published open-access PDF support the generalized-inverse/quantile convention
  and its atom-aware pushforward use.  ETH repository metadata confirms the DOI,
  journal, volume, issue, pages and year.
* Zeng, arXiv:2608.18179v1: Section 4, PDF p.4, explicitly states that exact
  cut-partition computations are diagnostic and not used in the proof.  This
  supports the manuscript's deliberately narrow methodological comparison.

Bibliography coverage is complete for the actual paper: it includes the problem
origin and closest result, the generalized-inverse method source, and the sole
active user-library item that directly supports a retained claim.  A second
library item would be irrelevant padding.  All three keys occur in ordinary
body flow and the canonical `manuscript/references.bib`; none is decorative,
undefined, duplicated, or unused.  The detailed audit is in
`audit/bibliography-audit.md`, and the attempt-bound library selection is in
`audit/user-bibliography-selection.json`.

Scope checked: both publication source files, all cite commands and BibTeX
entries, all eight extracted factual/attribution/numerical claims, exact nearby
passages, bibliography coverage, and the limitations of the current preprint
records.  The successful audit is not treated as mathematical proof.
