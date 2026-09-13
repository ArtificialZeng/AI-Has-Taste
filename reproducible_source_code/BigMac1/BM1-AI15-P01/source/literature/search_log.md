# Search log

All searches were run on 2026-08-29 (Asia/Shanghai).  Search-result absence
is not treated as proof of novelty.

## Pass 1: frozen claims and primary source

- 09:55 CST — arXiv ID/title queries: `arXiv 2508.14901 Computational
  Resolution of Hadamard Product Factorization for 4x4 Matrices`, exact title,
  and title plus `real Rivin`.  The only directly relevant mathematical result
  was the [arXiv record](https://arxiv.org/abs/2508.14901).
- 09:56 CST — arXiv abstract/history opened.  It lists only v1, submitted
  2025-07-31, and gives the DataCite DOI
  [10.48550/arXiv.2508.14901](https://doi.org/10.48550/arXiv.2508.14901).
- 09:58 CST — downloaded the v1 PDF directly from arXiv to
  `literature/rivin_2508.14901v1.pdf`.  SHA-256:
  `2e4de59df9c31feb8f8d96a3a87f239c6b1277ebb9bf5de39a0911ee6a239d34`.
  PDF text was checked at Theorem 4, Example 5, Theorem 6, §4.3, and Open
  Problem 7.1(4).  Example 5 matches the prompt entry for entry.

## Pass 2: post-result novelty audit

- 10:02 CST — exact-title and targeted web queries:
  `"The simplest counterexample" "Hadamard" Rivin factorization`,
  `"2508.14901" decomposition rational counterexample`, a quoted row-pattern
  query, and exact title plus `correction OR comment OR response`.  No relevant
  correction, response, or exact factorization was found.
- 10:03 CST — Semantic Scholar Graph API query for `arXiv:2508.14901` returned
  paper ID `a572c6111dcc26ff351c67a58394523ebedf576d`, venue `arXiv.org`, and
  citation count 0.  Endpoint:
  `https://api.semanticscholar.org/graph/v1/paper/arXiv:2508.14901`.
- 10:03 CST — OpenAlex DOI lookup returned work
  `https://openalex.org/W4416050143`, type `preprint`, submitted version,
  `is_published=false`, and cited-by count 0.  Endpoint:
  `https://api.openalex.org/works/https://doi.org/10.48550/arxiv.2508.14901`.
- 10:03 CST — Crossref bibliographic title query produced unrelated fuzzy
  matches and no record for the exact paper.  This is consistent with, but
  does not prove, lack of journal publication.

## NOVELTY_LOCK conclusion

The verifiable source frontier is Rivin's unchanged arXiv v1, which explicitly
stops at numerical evidence over \(\mathbb R\).  Within the recorded sources
and queries, no prior exact rational factorization of Example 5 was found.
Accordingly the project may describe its formula as “not found in the audited
literature as of 2026-08-29,” but may not claim priority as an established
fact until wider human bibliographic review.

## Final continuation recheck

- 10:20 CST — after the release-portability issue was reported, repeated four
  targeted searches: the arXiv ID plus exact title, ID plus
  `correction OR erratum OR factorization`, exact title plus `rational`, and
  the four quoted binary rows plus `Hadamard factorization`.
- Result: the only directly relevant mathematical record remained
  [arXiv:2508.14901](https://arxiv.org/abs/2508.14901).  No correction,
  replacement version, indexed response, or prior explicit factorization was
  located.  Unrelated Hadamard-matrix/code hits were discarded.
- Consequence: C06 and the bounded `NOVELTY_LOCK` language are unchanged.  The
  project still makes no absolute first/priority claim.
