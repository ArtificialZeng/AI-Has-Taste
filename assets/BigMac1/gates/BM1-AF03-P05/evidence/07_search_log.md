# Search log

All dates are 2026-08-29 (Asia/Shanghai) unless an entry says otherwise.

## Pre-freeze reconnaissance

- Web queries: exact paper title; `e(overline G) n-3 q(G)=2`; exact title on
  arXiv; `sparse complement q(G)=2 graph`.
- Preliminary primary hits (not yet accepted into the ledger): ELA article
  landing/download record; arXiv:2411.12917.  A broad search also surfaced an
  August 2026 path-complement preprint, which is tracked by C10 and must not be
  treated as resolving (N9) without checking its endpoint.
- This reconnaissance occurred before the finite C01--C10 ledger was written;
  the systematic pass below is restricted to those frozen claims.

## Systematic Gate 1 pass

Completed on 2026-08-29.  The detailed raw query-by-query record is preserved
in `literature/agent_search_raw.md`, and the synthesized lock is in
`literature/agent_novelty_report.md`.

### Primary records checked

- Barrett--Fallat--Furst--Nasserasr--Rooney--Tait, ELA 42 (2026),
  pp. 146--161: publisher landing page/PDF, DOI/Crossref, arXiv:2411.12917v1
  abstract/API/source.  Verified definition, Conjecture 1.1, Theorems 2.3 and
  3.7, Observation 5.1, publication metadata, and that arXiv has only v1.
- Fallat--Mojallal, *Mathematics* 11 (2023), article 3595: publisher PDF,
  DOI/Crossref, arXiv:2307.09663 source.  Verified the first public
  formulation located, its 2022-personal-communication attribution,
  Theorems 22--23 for orders 7 and 8, and Problem 2 for orders at least 9.
- Levene--Oblak--Šmigoc, *Linear and Multilinear Algebra* 72 (2024),
  pp. 2054--2068, DOI 10.1080/03081087.2023.2232090: publisher full text/PDF
  record.  Verified Theorem 3.4, especially the connected \(k=1\) consequence
  for join factors whose orders differ by at most two.
- Fei--Luo, arXiv:2608.27227v1 (2026-08-27): checked the current source and
  theorem endpoint.  It cites the 2026 paper and corrects a nearby
  path-complement boundary aside, but does not address the present six-edge
  order-nine endpoint.

### Later-result and code searches

- Exact title, DOI, conjecture formula, “requires problem,” order-nine, and
  removed-edge searches on the general web and arXiv metadata/full records.
- Crossref and OpenAlex citation records; Google Scholar and Semantic Scholar
  were rate-limited and are recorded as coverage limitations.
- GitHub repository API searches for the exact title, arXiv ID, and relevant
  phrases; Zenodo exact-ID search; publisher/arXiv supplemental-file audit.
- No full order-nine solution or order-nine exact code/certificate was found.
  The very recent Fei--Luo citation demonstrates why zero index counts were
  not treated as proof of no citations.

### Gate 1 corrections to the supplied boundary

1. Attribution is now: the six-author conjecture, first published by
   Fallat--Mojallal (2023) from their 2022 communication, and restated by the
   six authors in 2026.
2. “Non-bipartite with at most six edges” is a valid search set but is not the
   minimal literature frontier.  Theorem 2.3, Theorem 3.7, Observation 5.1,
   and the order-eight baseline leave only non-bipartite six-edge complements.
3. The path-complement aside corrected by Fei--Luo is excluded from all proof
   dependencies here.

### Gate 1 outcome

`NOVELTY_LOCK = PASS_WITH_RECORDED_LIMITATIONS`.  A second current search is
mandatory immediately before a publishable release.

## Systematic Gate 6 pass (post-manuscript, pre-release)

Completed on 2026-08-29 (Asia/Shanghai), after the exact certificate,
verifier, and theorem endpoint had frozen.  This pass did not alter the
mathematical proof.

### Queries and records rechecked

- Exact and formula queries: `"q(G)=2" "n=9" complement graph distinct
  eigenvalues`; `"e(overline G)" "q(G)" graph conjecture`; `"sparse
  complement" "two distinct eigenvalues" graph`; and the exact 2026 paper
  title with `citing`, `order nine`, and `2608` variants.
- Current arXiv queries for the exact title, arXiv:2411.12917, recent
  `distinct eigenvalues`/complement records, and August 2026 records.
- Publisher/DOI queries for 10.13001/ela.2026.9443 and the ELA article record.
- Citation-validation queries for every bibliography item: author/year/title,
  exact title with arXiv where applicable, author/year/venue, and DOI (or
  ISBN/OUP record for the graph atlas).

### Results

- The publisher record and arXiv:2411.12917 still state the conjecture and the
  bipartite-complement result, with no newer arXiv version located.
- Fei--Luo, arXiv:2608.27227v1, remains the only new directly relevant citing
  preprint located.  Its endpoint is
  \(MB(\overline{P_n})=3\) for \(n\ge6\), not the present six-edge order-nine
  endpoint.
- Searches also returned other two-eigenvalue graph-family papers, but none
  claims an exhaustive resolution of all nine-vertex complements with at most
  six edges.
- No public exact order-nine certificate or verifier was located.

### Gate 6 outcome

`SECOND_NOVELTY_SEARCH = PASS_WITH_RECORDED_LIMITATIONS`.
The negative novelty claims remain bounded by this date, these queries, and
the Gate 1 databases.  Search-engine and index lag prevent any absolute claim
that no unpublished or unindexed solution exists.
