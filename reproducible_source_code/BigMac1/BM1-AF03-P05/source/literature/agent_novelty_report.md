# Gate 1 agent report: source and novelty lock

Audit date: **2026-08-29** (Asia/Shanghai)  
Scope: the order-nine instance of the sparse-complement conjecture for the
minimum number of distinct eigenvalues of a graph.  This is an agent-local
report for later merger; it does not modify `claim_ledger.md` or
`search_log.md`.

## Outcome

**NOVELTY_LOCK passes, with two important scope refinements.**  I found no
public proof or counterexample for the full conjecture at order $9$, nor a
public result certifying all nine-vertex complements with at most six edges.
The published record still identifies orders through $8$ as verified and
order $9$ as the first order not covered in full.

However:

1. The public provenance is more nuanced than attributing the first public
   formulation solely to Barrett--Fallat--Furst--Nasserasr--Rooney--Tait.
   Fallat--Mojallal published the conjecture as Conjecture 1 in 2023, explicitly
   saying it was based on a 2022 personal communication from those six authors.
   Thus a careful attribution is: **the Barrett--Fallat--Furst--Nasserasr--
   Rooney--Tait conjecture, first published by Fallat--Mojallal (2023) from
   their 2022 communication**, and restated as Conjecture 1.1 by the six
   authors in 2026.
2. For $n=9$, the genuinely unresolved finite frontier is narrower than
   “all non-bipartite complements with at most six edges”: after combining
   Theorems 2.3 and 3.7 and Observation 5.1 of the 2026 paper with the verified
   $n\leq 8$ baseline, **only non-bipartite complements with exactly six
   edges remain outside those general reductions**.  The derivation is given
   below.

One very recent citing preprint was found: Fei--Luo,
arXiv:2608.27227v1 (submitted 2026-08-27).  It studies the different problem
$MB(\overline{P_n})$, not the sparse-complement conjecture.  It does not
settle the present $n=9$ problem: for $G=\overline{P_9}$, the removed graph
is $P_9$, which has eight edges, outside the present six-edge threshold.

## Frozen claim list and dispositions

The list below was frozen before the targeted searches recorded in
`agent_search_raw.md`.  “Exact” means directly stated in a primary source;
“inference” means a consequence assembled here from exact source statements;
“not found” is limited to the recorded sources and queries.

| ID | Frozen claim | Class | Disposition and primary evidence |
|---|---|---|---|
| G1-01 | The paper's $S(G)$ consists of real symmetric matrices whose off-diagonal nonzeros occur exactly at edges, and $q(G)=\min_{A\in S(G)}q(A)$. | exact | Verified in Barrett et al. (2026), printed p. 146, Introduction; also in arXiv source lines 175--176. |
| G1-02 | The conjecture is: for every simple graph $G$ of order $n\geq3$, $e(\overline G)\leq n-3\Rightarrow q(G)=2$. | exact | Verified as Barrett et al. (2026), Conjecture 1.1, printed p. 147; arXiv source lines 182--184.  Endpoint $n\geq3$, weak inequality, and complement are all explicit. |
| G1-03 | The conjecture is attributable to the six 2026 authors. | provenance | Substantively supported but needs nuance: Fallat--Mojallal (2023), Conjecture 1, is the first public formulation located; its text says it is based on Barrett--Fallat--Furst--Nasserasr--Rooney--Tait, Personal Communication, 2022 (reference 37). |
| G1-04 | The 2026 paper is formally published in ELA 42, 146--161 with DOI 10.13001/ela.2026.9443. | exact metadata | Verified on the ELA landing page/PDF and Crossref.  ELA and Crossref give publication date 2026-03-04; the PDF says received 2025-03-15 and accepted 2026-02-13. |
| G1-05 | arXiv:2411.12917 is the corresponding preprint and the latest arXiv version. | exact metadata | Verified.  arXiv lists only v1, submitted 2024-11-19 23:05:43 UTC; no v2 is present as of the audit date.  Because the journal paper is later, the published version is the authoritative version for citation. |
| G1-06 | All graphs with $e(\overline G)\leq\lfloor n/2\rfloor-1$ have $q(G)=2$. | exact theorem | Verified as Barrett et al. (2026), Theorem 2.3, printed p. 149. |
| G1-07 | The conjecture holds whenever $\overline G$ is bipartite. | exact theorem | Verified as Barrett et al. (2026), Theorem 3.7, printed p. 153: $n\geq3$, $\overline G$ bipartite, $e(\overline G)\leq n-3$. |
| G1-08 | Orders $n=7$ and $n=8$ were verified. | exact theorems | Verified in Fallat--Mojallal (2023): Theorem 22 (up to four deletions from $K_7$, PDF p. 18) and Theorem 23 (up to five deletions from $K_8$, PDF p. 24).  Barrett et al. (2026), printed pp. 147 and 157, expressly cite this baseline. |
| G1-09 | $n=9$ is the first order not known in full. | inference/novelty | Supported by G1-08 and Fallat--Mojallal's explicit Problem 2 (prove the conjecture for graphs of order at least nine, PDF p. 25), plus the negative later-solution searches below.  No public full $n=9$ resolution was found. |
| G1-10 | At $n=9$, the threshold is $e(\overline G)\leq6$. | exact arithmetic consequence | Verified from Conjecture 1.1: $n-3=6$. |
| G1-11 | It suffices to enumerate all non-bipartite $H=\overline G$ with at most six edges. | valid but nonminimal reduction | Bipartite $H$ are excluded by Theorem 3.7.  Yet Theorem 2.3 already covers $e(H)\leq3$, and Observation 5.1 plus the $n\leq8$ baseline covers every non-bipartite $H$ with four or five edges.  The minimal residual frontier has $e(H)=6$. |
| G1-12 | A later public paper has solved or disproved the full order-nine case. | novelty | Not found.  Crossref and OpenAlex both reported zero indexed citations to DOI 10.13001/ela.2026.9443 at query time, but the newer arXiv preprint 2608.27227 directly cites it and is too recent to be reflected by those counts.  That preprint solves a different path-complement multiplicity question. |
| G1-13 | Public discovery/certification code exists for the 2026 paper or the $n=9$ finite problem. | code | Not found.  The arXiv v1 source archive contains only `BipartiteComplement.tex` and `.bbl`; exact-title/arXiv-ID GitHub repository searches and an exact-ID Zenodo search returned zero.  Fallat--Mojallal cite a general external Sage SSP/SAP/SMP tester, but no archived instance scripts or $n=9$ enumeration/certificates were located. |
| G1-14 | No correction affects the conjecture statement or its $n\leq8$ baseline. | exact/negative search | No corrigendum or erratum to the 2026 paper was found.  Fei--Luo (2026), however, correct a *nearby aside* after Porism 5.4: the printed example range $\overline{P_n}$, $n>4$, $3\nmid n$, wrongly includes $n=5$, for which $q(\overline{P_5})=3$.  They use the statement only for $n\geq6$.  This does not affect Conjecture 1.1, Theorem 2.3, Theorem 3.7, or the present six-edge $n=9$ endpoint. |

## Primary-source details

### Barrett--Fallat--Furst--Nasserasr--Rooney--Tait (2026)

- Publisher landing page:
  <https://journals.uwyo.edu/index.php/ela/article/view/9443>
- Publisher PDF:
  <https://journals.uwyo.edu/index.php/ela/article/download/9443/7389/28681>
- DOI: <https://doi.org/10.13001/ela.2026.9443>
- Crossref record:
  <https://api.crossref.org/works/10.13001%2Fela.2026.9443>
- arXiv abstract/source: <https://arxiv.org/abs/2411.12917>,
  <https://export.arxiv.org/e-print/2411.12917v1>
- Metadata: Wayne Barrett, Shaun Fallat, Veronika Furst, Shahla Nasserasr,
  Brendan Rooney, Michael Tait; *Electronic Journal of Linear Algebra* 42
  (2026), 146--161; published 2026-03-04; DOI
  `10.13001/ela.2026.9443`.
- Relevant locations in the printed paper:
  - definition and abstract: p. 146;
  - Conjecture 1.1 and the statement that $n=7,8$ had been verified: p. 147;
  - Theorem 2.3: p. 149;
  - Theorem 3.7: p. 153;
  - statement that the conjecture is verified for $n\leq8$ and Observation
    5.1: p. 157;
  - Theorem 5.3, a non-bipartite odd-cycle deletion family: p. 159;
  - discussion following Porism 5.4 (including the $\overline{P_n}$ aside
    corrected by Fei--Luo): p. 160.

The publisher PDF SHA-256 retrieved during this audit was
`c1adfc9bfcc3882c15cd53395d78de73032ac943b3f14ae7a4cf1350262e3962`.
The arXiv v1 PDF SHA-256 was
`5f0b0d0243e6691b43d7d0c4377584400a8ed849aa217b490737ad48348870ba`;
the arXiv v1 source archive SHA-256 was
`14e2236aedd3dcfe52f0f0246498c20ce8aaa4fa07be7dd2d741d682142e2bd1`.

### Fallat--Mojallal (2023), public origin and $n=7,8$ baseline

- Publisher page:
  <https://www.mdpi.com/2227-7390/11/16/3595>
- Publisher PDF:
  <https://mdpi-res.com/d_attachment/mathematics/mathematics-11-03595/article_deploy/mathematics-11-03595-v2.pdf>
- DOI: <https://doi.org/10.3390/math11163595>
- arXiv: <https://arxiv.org/abs/2307.09663>
- Metadata: Shaun Fallat and Seyed Ahmad Mojallal, *Mathematics* 11(16)
  (2023), article 3595, published 2023-08-19, DOI
  `10.3390/math11163595`.
- Primary statements:
  - Conjecture 1, PDF p. 17: removing at most $n-3$ edges from $K_n$
    leaves $q=2$.
  - Reference 37: Barrett, Fallat, Furst, Nasserasr, Rooney, Tait,
    Personal Communication, 2022.
  - Theorem 22, PDF p. 18: order $7$, at most four removed edges.
  - Theorem 23, PDF p. 24: order $8$, at most five removed edges.
  - Problem 2, PDF p. 25: prove Conjecture 1 for graphs of order at least
    nine.

The MDPI v2 PDF SHA-256 retrieved during this audit was
`45158aa30bd2f938e70c0a60948bdc6bbc353fe75a3714f70e8d1f231d1bde8a`.

### Fei--Luo (2026), subsequent citation but different endpoint

- arXiv: <https://arxiv.org/abs/2608.27227>
- Jintao Fei and Jiangying Luo, *Rank-Three Projections and Minimal
  Multiplicity Bipartitions of Path Complements*, arXiv:2608.27227v1,
  submitted 2026-08-27.
- Exact endpoint: $MB(\overline{P_n})=3$ for $n\geq6$, with small-order
  exceptions stated separately.  The paper cites Barrett et al. (2026) at
  its discussion of Porism 5.4 and Lemma 5.2.
- Relevance here: it is a genuine later citation and reveals the $n=5$
  boundary error in the 2026 paper's path-complement aside, but it neither
  proves nor disproves the six-edge order-nine conjecture.

## Exact order-nine frontier implied by the literature

Let $H=\overline G$ have nine vertices and $e(H)\leq6$.

1. If $H$ is bipartite, Theorem 3.7 gives $q(G)=2$.
2. If $e(H)\leq3$, Theorem 2.3 gives $q(G)=2$, regardless of
   bipartiteness.
3. Suppose $H$ is non-bipartite and $e(H)\leq5$.  Then $H$ contains an
   odd cycle.  With at most five total edges, that cycle has length $3$ or
   $5$.  A triangle plus at most two remaining edges meets at most seven
   vertices, while a 5-cycle meets only five.  Hence $H$ has at least two
   isolated vertices.  Delete two isolated vertices and regard the remainder
   as a graph on $n-2=7$ vertices.  Since $e(H)\leq n-4=5$ and the main
   conjecture is known through order $8$, Observation 5.1 of Barrett et al.
   applies and gives $q(K_9-E(H))=2$.

Therefore the literature-backed residual class is precisely

\[
  |V(H)|=9,\qquad e(H)=6,\qquad H\text{ non-bipartite}.
\]

This is an **inference** from published theorems, not a theorem stated verbatim
in the papers.  Some six-edge members may also fall into other published
special families; the assertion here is only that the three general reductions
above leave no graphs with fewer than six edges.

## Novelty-search conclusion and limitations

The following searches produced no full $n=9$ solution: exact-title and
exact-DOI web searches; arXiv full-metadata queries for “minimum number of
distinct eigenvalues” with “complement,” “bipartite complement,” the
“requires problem,” and removed edges; Crossref and OpenAlex citation records;
exact-title/arXiv-ID GitHub repository searches; and an exact-ID Zenodo search.
Google Scholar and Semantic Scholar endpoints returned rate-limit errors, so a
claim of *absolute* absence would be unjustified.  The very recent Fei--Luo
preprint was found by broader current-arXiv searching and checked from its
source package, mitigating (but not eliminating) indexing lag.

No proof assistant result (Lean/Coq/Isabelle) relevant to this claim was found
in the audited sources.  Gate 1 does not independently certify the published
$n=7,8$ proofs; the user's contract correctly requires reproducing that last
known baseline with an exact, fail-closed verifier in later gates.
