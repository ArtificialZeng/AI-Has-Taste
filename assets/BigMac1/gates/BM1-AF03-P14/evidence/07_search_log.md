# Search log

Cutoff date: 2026-08-29.  Gate 1 is not locked until C01–C12 in the claim
ledger have evidence or an explicitly bounded “not found” result.

## Frozen protocol (before search)

Primary records to query: arXiv abstract/version history and source PDF;
Elsevier/ScienceDirect article record; Crossref DOI metadata; the authors'
public pages or repositories; Semantic Scholar/OpenAlex/Crossref citation
records only to enumerate later works, followed by verification in each later
work itself.  General web search is used for discovery, never as final support
for a mathematical statement.

Queries to record verbatim include the exact paper title, DOI, arXiv ID,
author/title plus `code`, exact title plus `cited by`, and combinations of
`Q_5`, `five-dimensional cube`, `local extrema`, `critical central sections`,
and the author names.  Searches in English and mathematical notation variants
are included.

## Search events

All events below were run on 2026-08-29 (Asia/Shanghai).

1. Web exact-title/metadata search: `"Non-diagonal critical central sections of the cube"`,
   DOI `10.1016/j.aim.2024.109524`, arXiv `2307.03792`, and exact title plus
   `code`.  Located the [arXiv record](https://arxiv.org/abs/2307.03792),
   [ScienceDirect record](https://www.sciencedirect.com/science/article/pii/S0001870824000392),
   and institutional copies.  No code link appeared.
2. Queried the arXiv export API for `2307.03792`.  It returned latest version
   `v4`, updated `2024-01-29T09:36:35Z`, DOI
   `10.1016/j.aim.2024.109524`, and comment “Final version, to appear in
   Advances in Mathematics.”
3. Queried Crossref by DOI and used DOI content negotiation.  The record gives
   authors Gergely Ambrus and Barnabás Gárgyán, *Advances in Mathematics* 441,
   article 109524, publication April 2024.  The publisher VOR was downloaded
   from the University of Szeged repository and hashed.
4. Read the VOR, especially pp. 2–3 (definition, Theorems 1.1–1.2,
   Conjecture 1.3), Section 5, and Section 6 (saddle proof).  Compared the same
   theorem/section endpoints with arXiv v4.  No theorem-level difference was
   found; a full character diff was not claimed.
5. Located and read G. Ambrus, *Critical central sections of the cube*,
   [arXiv:2107.14778v3](https://arxiv.org/abs/2107.14778), published in
   *Proceedings of the AMS* 150 (2022), DOI `10.1090/proc/15955`.  Theorem 3
   gives the \(n=4\) classification.  Its elimination step uses unnamed
   computer algebra; therefore it is literature evidence, not this project's
   independent exact certificate.
6. Novelty web queries: exact title plus years 2025/2026; `"all locally
   extremal central sections" cube`; `"Q_5" cube "central sections"
   critical`; `"critical central sections" "five-dimensional"`; and author
   names with local-extrema/Q5 variants.  No complete \(Q_5\) solution was
   found.
7. Queried arXiv API with `all:"critical central sections" AND all:cube`
   (100-result cap): total 2, namely arXiv:2107.14778 and 2307.03792.  The exact
   phrase query `all:"locally extremal central sections"` returned 0.  These
   phrase searches are not exhaustive of alternative terminology.
8. Citation enumeration: Crossref and OpenAlex each reported one citing work;
   OpenAlex's cited-by query returned Ambrus–Gárgyán, *Estimates on the decay
   of the Laplace–Pólya integral* (2025), DOI `10.1112/blms.70157`.  Semantic
   Scholar reported four: that paper, Pournin's *Deep sections of the
   hypercube* (arXiv:2407.04637), Brandenburg–Meroni's *Combinatorics of
   slices of cubes* (arXiv:2510.09265), and Fodor–González Merino's *Central
   diagonal sections of Gaussian cubes* (arXiv:2511.01504).  Primary
   abstracts/text were checked; none claims a full \(Q_5\) classification.
9. A crucial correction was found and read: Ambrus–Gárgyán 2025,
   [DOI 10.1112/blms.70157](https://doi.org/10.1112/blms.70157), Theorem 1.4,
   proves central \(k\)-diagonals with \(3\le k\le n-1\) are not locally
   extremal.  Pournin's [2025 erratum](https://doi.org/10.1007/s11854-025-0384-1)
   identifies the missing term in the earlier local-extremality criterion.
10. Public-code search: web queries `site:github.com` plus exact title/arXiv ID;
    GitHub repository API queries for exact title, arXiv ID, and
    `cube sections Ambrus Gargyan` all returned `total_count=0`.  GitHub's code
    search API returned HTTP 401 without authentication, so the conclusion is
    only “no code found by recorded public searches.”
11. Local primary-source archive and SHA-256 digests:
    `ambrus_gargyan_2024_vor.pdf`
    `2161c744f0a42f98191a62c155078e850a4976c5016a895fa7ee76c77fcc6ef2`;
    `ambrus_gargyan_2024_arxiv_v4.pdf`
    `f79129be94de37f18f12dae74555f9fcaced06f2e157b13b12fcdf7c0e53d3c7`;
    `ambrus_2022_arxiv.pdf`
    `5d236efcb7ea803dd7b7641b3d6f0f8fe5d8a2c9a6d0b2825c0becb5c7351611`;
    `ambrus_gargyan_2025_vor.pdf`
    `6ea1e597f64256fc31252c42537031141a0fb4501fe99e83a38064461553a496`.
12. An independent second researcher repeated the metadata, citation, version,
    code, and topic searches and checked the full texts of arXiv:2407.04637v2,
    2412.12835v3, 2510.09265v1, 2511.01504v3, and the newly located
    2603.25643v2.  The last is the closest 2026 chamber-method paper but stops
    at a four-cube formula catalogue and partial four-dimensional critical
    analysis.  The independent query list, version warnings, hashes, and
    bounded-negative qualifications are preserved in
    `literature/agent_novelty_report.md`; its primary archive is
    `literature/sources/novelty_agent/`.

## Gate 1 lock and boundary

`NOVELTY_LOCK = LOCKED_WITH_DATABASE_BOUND` at 2026-08-29.  “No solution
found” is limited to the arXiv, Crossref, OpenAlex, Semantic Scholar, publisher,
author/institutional pages, GitHub repository search, and general-web queries
listed above.  A second pass is mandatory if a rigorous new theorem emerges.

## Gate 2 — exact-result novelty search

Gate 2 was run on 2026-08-29 after the project had exact theorem endpoints.  The
searched statements, always modulo signed permutations and antipodes, were:

1. the full-support critical directions of \(Q_5\) are exactly \(d_5\) and
   \[
   v_\alpha=\frac{(\alpha,\alpha,1,1,1)}{\sqrt{2\alpha^2+3}},
   \qquad \alpha=\frac{24+\sqrt{69}}{13};
   \]
2. all locally extremal central sections of \(Q_5\) are exactly the diagonal
   types \(d_1,d_2,d_5\).

The first statement is deliberately restricted to **full support**; it is not
logged as a classification of every boundary-support critical direction.

### Gate 2 search events

13. **Exact wording and algebraic fingerprints.**  General-web searches used
    `"24+sqrt(69)" cube central section`, `"sqrt(69)" "central sections" cube`,
    `"(24+sqrt(69))/13"`, `"13r^2-48r+39" cube`,
    `"13 r^2 - 48 r + 39" section`, `"alpha,alpha,1,1,1" cube section`,
    `"five-dimensional cube" critical "central sections"`,
    `"Q_5" cube "local extrema" "central sections"`, and
    `"locally extremal central sections" cube classification`.  No result
    matching either endpoint was returned; radical-only hits were unrelated.
    Exact strings can miss alternative notation, so this is only one layer of
    the search.

14. **Current arXiv corpus and versions.**  The arXiv export API query
    [`all:"critical central sections" AND all:cube`](https://export.arxiv.org/api/query?search_query=all:%22critical%20central%20sections%22%20AND%20all:cube&start=0&max_results=100&sortBy=submittedDate&sortOrder=descending)
    returned only arXiv:2307.03792v4 and 2107.14778v3.  Exact phrase queries for
    `"local extrema"` with `"cube sections"`, and searches for
    `"five-dimensional cube"` with `section`, returned no matching paper.
    Broader `cat:math.MG AND all:cube AND all:section` (27 records),
    `cat:math.MG AND all:hypercube AND all:section` (6 records), and
    `all:"cube slicing" OR all:"cube sections"` (15 records) were screened by
    title and abstract, with plausible records checked in full text.  The
    relevant latest-version snapshot was: arXiv:2307.03792v4 (2024-01-29),
    2407.04637v2 (2025-03-04), 2412.12835v3 (2025-07-13),
    2510.09265v1 (2025-10-10), 2511.01504v3 (2026-06-04), and
    [2603.25643v2](https://arxiv.org/abs/2603.25643) (2026-07-01).
    Also screened were 2505.16247v3 (Vaaler's lower bound), 2607.28429v2
    (lattice coverings), and 2412.16054v1 (random sections); their endpoints
    are different.

15. **Primary-text scope check.**  The latest texts of the six plausible works
    above were searched for `Q5`, `five-dimensional`, `dimension 5`, `critical`,
    `local extrem`, the radical \(\sqrt{69}\), and complete-classification
    language, then the surrounding theorem statements were read.  AG24 retains
    the conjectural endpoint; arXiv:2407.04637 concerns deep/diagonal sections;
    2412.12835 proves the corrected status of diagonal types;
    2510.09265 classifies combinatorial slice types, not volume critical points;
    2511.01504 concerns Gaussian cubes; and 2603.25643v2 treats dimensions at
    most four and only a partial four-dimensional critical analysis.  None
    states either Gate 2 endpoint.

16. **Crossref.**  The current
    [DOI record](https://api.crossref.org/works/10.1016/j.aim.2024.109524)
    reports `is-referenced-by-count=1`.  Crossref bibliographic searches for
    `Q5 central cube sections local extrema`, `five-dimensional cube critical
    central sections`, `locally extremal central sections cube`, `critical
    directions cube section dimension 5`, and `all local extrema Q5 cube`
    returned the known 2022/2024/2025 cube-section papers among their relevant
    top results, but no exact endpoint.  A `references`-filter attempt returned
    HTTP 400, and exact-radical bibliographic search was dominated by unrelated
    records; Crossref was therefore used for metadata/discovery rather than as
    an exhaustive full-text search.

17. **Citation graph and index-lag audit.**  The
    [Semantic Scholar paper record](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1016/j.aim.2024.109524?fields=paperId,title,year,externalIds,citationCount,influentialCitationCount,authors)
    reported four citations and zero influential citations.  Its cited-by list
    comprised arXiv:2407.04637, 2412.12835, 2510.09265, and 2511.01504; all four
    latest primary texts were checked as in event 15.  Topic-search API calls
    later returned HTTP 429, a recorded coverage limitation.  The
    [OpenAlex DOI record](https://api.openalex.org/works/https://doi.org/10.1016/j.aim.2024.109524)
    (`W4392085021`, snapshot updated 2026-08-28) and its `cites:` query returned
    only the 2025 diagonal-extremality paper.  Direct inspection of
    arXiv:2603.25643v2 found that it cites AG24 although it was absent from both
    cited-by snapshots, demonstrating actual index lag; its scope is still
    dimensions \(\le4\).

18. **Google Scholar / Google-like scholarly search.**  An unauthenticated
    exact-title query for `"Non-diagonal critical central sections of the
    cube"` returned one work cluster, “Cited by 4,” whose cited-by page matched
    the four Semantic Scholar works.  Exact queries
    `"24+sqrt(69)" cube section`, `"13r^2-48r+39" cube`,
    `"five-dimensional cube" "critical central sections"`, and
    `"Q_5" "locally extremal central sections"` returned zero results.  Google
    Scholar coverage, deduplication, personalization and indexing delay are
    opaque; these zero-result observations are not treated as proof of absence.

19. **Authors and adjacent public material.**  Searches for Gergely Ambrus,
    Barnabás Gárgyán and Lionel Pournin with `cube sections`, `2026`, `Q5`, and
    `local extrema` found no complete \(Q_5\) result.  The 2025
    [Convexity conference booklet/poster](https://www.math.u-szeged.hu/convexity2025/Convexity25_Booklet.pdf)
    *Extremality of diagonal sections of the cube* records the diagonal status
    (in \(Q_5\): \(d_1,d_2,d_5\) extremal and \(d_3,d_4\) non-extremal) but does
    not classify non-diagonal critical directions or all \(Q_5\) local
    extrema.  Pournin's public publication page likewise led only to the known
    works already screened.

20. **Public code.**  GitHub repository-API and web searches used `2307.03792`,
    the exact AG24 title, `cube sections Ambrus Gargyan`,
    `"24+sqrt(69)" cube`, and `Q5 central cube sections`; each repository query
    returned zero relevant repositories.  Unauthenticated GitHub code search
    returned HTTP 401.  The separately located
    [repository for arXiv:2603.25643](https://github.com/RainCamel/slab_of_the_poly_norms)
    supports that paper's dimensions-at-most-four calculations and is not
    AG24 author code or a \(Q_5\) classification.

## Gate 2 lock and boundary

`NOVELTY_LOCK_GATE_2 = LOCKED_WITH_DATABASE_BOUND` at 2026-08-29.  Across the
recorded exact-signature searches, broad arXiv corpus screens, DOI/citation
graphs, Google Scholar, author/public pages, full-text version checks and public
repository searches, no public prior statement of either exact Gate 2 endpoint
was located.  The defensible conclusion is therefore “no prior public solution
was located within these databases, queries and cutoff,” not “no prior solution
exists.”  Unindexed, unpublished, inaccessible, newly posted after the cutoff,
or differently phrased work remains outside the lock.

## Release-phase novelty rerun — 2026-08-30

This is a second, release-date search after the mathematical endpoint and
hostile-referee PASS were frozen.  Search snippets were used only for
discovery; scope conclusions below were checked against primary arXiv,
publisher, DOI, or institutional records.

| Event | Query/endpoint | Result used | Boundary |
|---|---|---|---|
| R01 | `"complete classification" "Q_5" cube central sections local extrema` | No relevant result. | General-web indexing and phrasing are incomplete. |
| R02 | `"locally extremal central sections" cube 2026` | Original AG24 and diagonal-only AG25 results. | Exact phrase can miss equivalent terminology. |
| R03 | `site:arxiv.org cube central hyperplane sections Q5 critical directions 2026` | No \(Q_5\) classification. | Search-engine arXiv indexing is incomplete. |
| R04 | `"(24+sqrt(69))/13" cube section` and `"13 alpha^2-48 alpha+39" cube` | No mathematical hit. | Algebraic fingerprints can be formatted differently. |
| R05 | arXiv API `all:"central sections" AND all:cube`, response updated `2026-08-29T16:27:32Z` | Latest relevant hits were AG25 v3 and AG24 v4; no later \(Q_5\) result. | Literal API query misses papers using “slices.” |
| R06 | arXiv API `all:cube AND all:"critical points" AND all:slices`, response updated `2026-08-29T16:29:25Z` | Only arXiv:2603.25643v2; its primary abstract and paper stop at the four-cube catalogue/partial higher-dimensional critical analysis. | Does not search every synonym. |
| R07 | Crossref `query.title=central sections cube`, publication date from 2024 | AG24 was the only relevant mathematical record. | Crossref title search was noisy and excludes unpublished work. |
| R08 | OpenAlex record `W4392085021`, updated 2026-08-28 | One indexed citation to AG24. | Citation graph demonstrably lags. |
| R09 | Semantic Scholar Graph API for AG24 DOI | Four citations: arXiv:2407.04637, 2412.12835, 2510.09265, 2511.01504; none settles \(Q_5\). | It omitted the directly located 2026 paper. |
| R10 | Current Gergely Ambrus/Barnabás Gárgyán author and publication-page searches | No new cube-section classification; Ambrus's July 2026 arXiv work is unrelated. | Author identity and page freshness are bounded. |

The full text/scope checks from Gate 2 remain applicable to every indexed
citing work.  The only additional recent primary work found directly,
[arXiv:2603.25643v2](https://arxiv.org/abs/2603.25643), gives a complete family
of fourteen rational volume functions for slices/slabs of the four-cube and
only partial critical-point conclusions there.  It neither classifies the
five-cube nor produces a non-diagonal local extremum.

`NOVELTY_LOCK_RELEASE = LOCKED_WITH_DATABASE_BOUND` at 2026-08-30.  The
release may state only that no prior solution was located within the recorded
sources, queries, versions, and cutoff.
