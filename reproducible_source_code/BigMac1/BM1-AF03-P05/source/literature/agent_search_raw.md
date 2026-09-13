# Gate 1 raw search record

Audit date: 2026-08-29  
Agent scope: primary-source and novelty searches only.  Results here are raw
provenance for merger into the project search log; third-party snippets were
not used to establish mathematical claims.

## Frozen claims before targeted search

1. Exact definition of (S(G)) and (q(G)).
2. Exact conjecture, including $n\geq3$, complement notation, weak threshold
   $e(\overline G)\leq n-3$, and equality $q(G)=2$.
3. Attribution and first public formulation.
4. Journal/DOI metadata and publication status.
5. Latest arXiv version.
6. General theorem $e(\overline G)\leq\lfloor n/2\rfloor-1$.
7. Bipartite-complement theorem.
8. Exact status of orders (7) and (8).
9. Whether order (9) is still the first unverified order.
10. Whether subsequent work solves or refutes order (9).
11. Whether public code/certificates exist.
12. Whether an erratum/correction changes the endpoint.

## Publisher, DOI, and arXiv checks

### 2026 paper

- ELA landing page opened:
  <https://journals.uwyo.edu/index.php/ela/article/view/9443>
  - displayed title, all six authors, publication date 2026-03-04, DOI
    10.13001/ela.2026.9443, volume 42;
  - abstract displayed exact complement threshold and bipartite-complement
    claim.
- ELA PDF opened/read:
  <https://journals.uwyo.edu/index.php/ela/article/download/9443/7389/28681>
  - 16 pages, printed pp. 146--161;
  - p. 146: definition/abstract and received/accepted metadata;
  - p. 147: Conjecture 1.1; (n=7,8) statement;
  - p. 149: Theorem 2.3;
  - p. 153: Theorem 3.7;
  - p. 157: $n\leq8$ statement and Observation 5.1;
  - p. 159: Theorem 5.3;
  - p. 160: path-complement example after Porism 5.4.
- Crossref queried:
  <https://api.crossref.org/works/10.13001%2Fela.2026.9443>
  - status `ok`;
  - DOI `10.13001/ela.2026.9443`;
  - publisher `University of Wyoming Libraries`;
  - container `The Electronic Journal of Linear Algebra`;
  - published date 2026-03-04, volume 42, pages 146--161;
  - `is-referenced-by-count: 0` at query time.
- arXiv abstract page opened: <https://arxiv.org/abs/2411.12917>
  - only `[v1] Tue, 19 Nov 2024 23:05:43 UTC` in submission history;
  - no v2/v3.
- Official arXiv API queried:
  <https://export.arxiv.org/api/query?id_list=2411.12917>
  - entry ID ended in `2411.12917v1`;
  - updated and published fields both 2024-11-19T23:05:43Z.
- arXiv source downloaded from
  <https://export.arxiv.org/e-print/2411.12917v1>.
  Archive listing contained only:
  - `BipartiteComplement.tex`
  - `BipartiteComplement.bbl`
  No program, notebook, serialized enumeration, or certificate was present.

### 2023 source/baseline paper

- MDPI publisher page found:
  <https://www.mdpi.com/2227-7390/11/16/3595>
- Stable publisher PDF read:
  <https://mdpi-res.com/d_attachment/mathematics/mathematics-11-03595/article_deploy/mathematics-11-03595-v2.pdf>
  - PDF p. 17: Conjecture 1 and attribution to personal communication;
  - PDF p. 18: Theorem 22, (K_7) minus at most four edges;
  - PDF p. 24: Theorem 23, (K_8) minus at most five edges;
  - PDF p. 25: Problem 2, orders at least nine.
- Crossref queried:
  <https://api.crossref.org/works/10.3390%2Fmath11163595>
  - status `ok`, DOI `10.3390/math11163595`, published 2023-08-19,
    volume 11, issue 16.
- arXiv source downloaded:
  <https://export.arxiv.org/e-print/2307.09663v1>
  - source lines 970--973 state the conjecture;
  - lines 975 and 1036--1040 state/prove the (n=7) endpoint;
  - lines 1305--1309 state the (n=8) endpoint;
  - line 1343 states the order-at-least-nine problem;
  - bibliography lines 1367--1368 identify the six-author 2022 personal
    communication.
- The MDPI paper's reference 38 points to an external general
  “SAP/SSP/SMP Tester--SAGE” at
  <https://sage.math.iastate.edu/home/pub/79/>.  A direct retrieval attempt
  timed out (HTTP code 000 after 10 seconds) on the audit date.  This is a
  general tester citation, not an archived (n=9) computation/certificate.

## Web search queries

The web search engine was queried with the following strings (quotation marks
were included where shown):

1. `"Graphs with Bipartite Complement that Admit Two Distinct Eigenvalues"`
2. `"Graphs with Bipartite Complement" q(G) 2 Barrett Fallat Furst Nasserasr Rooney Tait arXiv`
3. `site:doi.org "Graphs with Bipartite Complement that Admit Two Distinct Eigenvalues"`
4. `site:github.com "Graphs with Bipartite Complement that Admit Two Distinct Eigenvalues"`
5. `"Graphs with bipartite complement that admit two distinct eigenvalues" -site:journals.uwyo.edu -site:arxiv.org -site:researchgate.net`
6. `"e(\\overline{G})" "n-3" "q(G)=2"`
7. `"Conjecture 1.1" "bipartite complement" "q(G)"`
8. `"q(G)=2" "n = 9" complement graph distinct eigenvalues`
9. `"Spectral Applications of Vertex-Clique Incidence Matrices Associated with a Graph" DOI`
10. `site:mdpi.com "Spectral Applications of Vertex-Clique Incidence Matrices"`
11. `"Conjecture 1" "Spectral applications" "n-3" q(G)`
12. `"verified for n = 7" "q(G)" graph`
13. `"2411.12917" code OR github OR SageMath`
14. `"10.13001/ela.2026.9443" code OR github OR data`
15. `github "e(\\overline{G})" "n-3" eigenvalues graph`
16. `github "q(K_9" eigenvalues graph`
17. `"q = 2 requires problem" graph`
18. `"requires problem" "two distinct eigenvalues" graph`
19. `"Removing up to" "edges from K_n" "q" graph eigenvalues`
20. `"order at least 9" "minimum number of distinct eigenvalues" graph`
21. `"10.13001/ela.2026.9443" correction OR corrigendum OR erratum OR retraction`
22. `"Graphs with bipartite complement that admit two distinct eigenvalues" correction OR corrigendum OR erratum`
23. `"2411.12917" correction OR erratum OR comment`
24. `site:journals.uwyo.edu/index.php/ela "9443" corrigendum`

Relevant outcomes:

- The ELA publisher record/PDF, arXiv v1, the 2023 MDPI paper, author research
  pages, and bibliographic portals were returned.
- No result claimed a proof/counterexample of all order-nine six-edge cases.
- No erratum/corrigendum/retraction for DOI 10.13001/ela.2026.9443 was
  returned.
- The most important new hit from broader current searches was
  arXiv:2608.27227, checked separately from its primary source.

## arXiv metadata searches

Official arXiv API queries (up to 100 records, descending submission date)
included:

- `all:"minimum number of distinct eigenvalues" AND all:complement`
  - returned arXiv:2411.12917 and the older Nordhaus--Gaddum paper
    arXiv:1807.06436;
  - no later full sparse-complement solution.
- `all:"bipartite complement" AND all:eigenvalues`
  - returned arXiv:2411.12917 and an unrelated 2012 line-graph paper;
  - no later full solution.
- `all:"two distinct eigenvalues" AND all:"removed edges"`
  - no relevant later solution returned.

Because arXiv metadata search does not search every formula in full text, this
was supplemented by exact-title/phrase web search and by checking the recent
path-complement preprint's source.

## Subsequent citations and correction check

### Citation indices

- Crossref DOI record: `is-referenced-by-count = 0`.
- OpenAlex work record:
  <https://api.openalex.org/works/https://doi.org/10.13001/ela.2026.9443>
  - work ID `W7133568905`;
  - publication date 2026-03-04;
  - `cited_by_count = 0` at query time.
- Google Scholar link from arXiv returned HTTP 429.
- Semantic Scholar API returned HTTP 429.
- Therefore zero index counts were treated as lag-sensitive, not as proof of
  no citations.

### Directly found citing preprint

- arXiv page: <https://arxiv.org/abs/2608.27227>
- Source: <https://export.arxiv.org/e-print/2608.27227v1>
- Submitted 2026-08-27; title *Rank-Three Projections and Minimal Multiplicity
  Bipartitions of Path Complements*; authors Jintao Fei, Jiangying Luo.
- Source hits:
  - main text lines 119--145 cite Barrett et al. (2026), Porism 5.4 and Lemma
    5.2;
  - lines 574--583 explain that the printed $n>4$, $3\nmid n$ range in
    the discussion after Porism 5.4 includes the exceptional $n=5$, so the
    later paper uses it only for $n\geq6$;
  - bibliography includes DOI 10.13001/ela.2026.9443 and arXiv:2411.12917.
- Its theorem $MB(\overline{P_n})=3$ for $n\geq6$ is outside the current
  six-edge endpoint.  Its mention of “orders $n\geq9$ divisible by three”
  refers to the multiplicity-bipartition question for path complements, not
  to Conjecture 1.1.

## Public code/data searches

- GitHub repository API exact search for `"2411.12917"`: `total_count = 0`.
- GitHub repository API exact-title search: `total_count = 0`.
- GitHub repository API search for `"Spectral Applications of Vertex-Clique
  Incidence Matrices"`: `total_count = 0`.
- GitHub repository API search for `"q=2" "bipartite complement" graph`:
  `total_count = 0`.
- Zenodo API exact search for `"2411.12917"`: `hits.total = 0`.
- CatalyzeX direct retrieval returned HTTP 403; no code link was established.
- ELA PDF full-text searches for `SageMath`, `code`, `Data Availability`, and
  `Supplementary` returned no matches.
- The 2026 arXiv source package contains only TeX and BBL files.
- Fei--Luo's arXiv source includes an exact-arithmetic verification script,
  but that script certifies their path-complement result and is not code for
  the current order-nine sparse-complement enumeration.

Conclusion: no public code/certificate specifically associated with the 2026
paper or the full (n=9), six-edge problem was located.

## File hashes recorded during retrieval

- ELA publisher PDF:
  `c1adfc9bfcc3882c15cd53395d78de73032ac943b3f14ae7a4cf1350262e3962`
- arXiv:2411.12917v1 PDF:
  `5f0b0d0243e6691b43d7d0c4377584400a8ed849aa217b490737ad48348870ba`
- arXiv:2411.12917v1 source archive:
  `14e2236aedd3dcfe52f0f0246498c20ce8aaa4fa07be7dd2d741d682142e2bd1`
- Fallat--Mojallal MDPI v2 PDF:
  `45158aa30bd2f938e70c0a60948bdc6bbc353fe75a3714f70e8d1f231d1bde8a`

## Negative-result limitation

“Not found” in this record means not found in the publisher/DOI/arXiv records,
the specified web and API queries, and the checked public repositories as of
2026-08-29.  Google Scholar and Semantic Scholar were rate-limited, and very
recent material can evade citation indexing.  A second novelty pass remains
mandatory before any publication claim.
