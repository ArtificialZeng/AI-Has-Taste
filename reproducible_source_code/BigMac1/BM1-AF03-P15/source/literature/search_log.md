# Search log — Gate 1 `NOVELTY_LOCK`

Search date: 2026-08-29 (Asia/Shanghai). Searcher: Codex. Searches were
performed before mathematical discovery work. URLs below are recorded so that
the lock can be reproduced or refreshed.

## 1. Source identity, version, and statement

### 1.1 Publisher and DOI

- Opened the [Algebraic Combinatorics landing
  page](https://alco.centre-mersenne.org/articles/10.5802/alco.114/) and the
  [version-of-record
  PDF](https://alco.centre-mersenne.org/item/10.5802/alco.114.pdf).
- Resolved DOI [10.5802/alco.114](https://doi.org/10.5802/alco.114).
- Queried Crossref:
  [`https://api.crossref.org/works/10.5802/alco.114`](https://api.crossref.org/works/10.5802/alco.114).
- Result: title, authors, journal, volume 3, issue 3, pages 791–800, and
  publication date 2020-06-02 all agree. The journal page additionally gives
  received/revised/accepted dates and MR 4113607.
- Inspected Conjecture 1.3(a) (p. 792), normalized-flow definition and Theorem
  2.4 (p. 794), Proposition 3.6 (p. 797), and Section 5/Proposition 5.1/final
  verification sentence (pp. 798–799).

### 1.2 Latest arXiv version

- Opened [`https://arxiv.org/abs/1903.02033`](https://arxiv.org/abs/1903.02033)
  and queried the official Atom API:
  [`https://export.arxiv.org/api/query?id_list=1903.02033`](https://export.arxiv.org/api/query?id_list=1903.02033).
- Result: latest version is `1903.02033v2`, updated 2020-10-31; arXiv says
  “v2: minor edits and journal reference” and records DOI 10.5802/alco.114.
- Downloaded the v2 source archive. Its complete top-level file list is
  `main.tex`, `main.bbl`. The TeX statement and the sentence “verified ... up
  to \(n=8\)” agree with the version of record.

### 1.3 Public artifacts linked by the source records

- Enumerated every `href` on the journal landing page. Relevant downloadable
  objects are the PDF, article TeX, and citation exports; there is no
  supplementary-material, code, or data link.
- Inspected the arXiv source archive as above; no Sage/Python/notebook/data
  file or flow certificate is included.
- Conclusion limited to these records: the published \(n\le8\) report has no
  attached reproducible certificate.

## 2. Frozen exact text checks

The following source locations were checked directly rather than inferred from
an abstract or secondary summary.

| Item | Location | Audit result |
|---|---|---|
| Type-\(D\) conjecture | Gaetz–Gao, Conjecture 1.3(a), p. 792 | `Abs(W)` for type \(D_n\) has a normalized flow with \(\nu\equiv1\). |
| Type-\(D\) range and model | Section 5 opening, p. 798 | \(n\ge4\) and \(D_n=G(2,2,n)\). |
| Flow equations | Section 2.4, p. 794 | Nonnegative cover-edge weights with normalized row/column sums on each adjacent-rank bipartite graph. |
| Orbit quotient | Proposition 3.6, p. 797 | Equivalence between unit-weight flow on \(P\) and orbit-size-weighted flow on \(P/G\). |
| Failed claw route | Proposition 5.1, pp. 798–799 | The product-of-claws subposet route is impossible for \(D_n\), \(n\ge4\). |
| Reported finite verification | Last paragraph of Section 5, p. 799 | Author report: computer search through \(n=8\). No details/certificate are supplied there. |

## 3. Citation-index search

### 3.1 OpenAlex

- Work lookup:
  [`https://api.openalex.org/works/https://doi.org/10.5802/alco.114`](https://api.openalex.org/works/https://doi.org/10.5802/alco.114).
- Reverse-citation query:
  [`https://api.openalex.org/works?filter=cites:W2921670843&per-page=200`](https://api.openalex.org/works?filter=cites:W2921670843&per-page=200).
- Result on the lock date: `cited_by_count = 2`; returned:
  1. Angela Carnevale, Matthew Dyer, Paolo Sentinelli, *The intermediate
     orders of a Coxeter group*, DOI
     [10.1090/proc/16199](https://doi.org/10.1090/proc/16199).
  2. Ke Ou, *Absolute length for some modular finite reflection groups*, DOI
     [10.1142/S021949882550118X](https://doi.org/10.1142/S021949882550118X).

### 3.2 Semantic Scholar

- Queried the public Graph API by DOI:
  [`https://api.semanticscholar.org/graph/v1/paper/DOI:10.5802/alco.114`](https://api.semanticscholar.org/graph/v1/paper/DOI:10.5802/alco.114)
  with citation fields.
- Result on the lock date: three records. Besides the Carnevale–Dyer–Sentinelli
  paper, the list included the earlier/contemporaneous Harper–Kim–Livesay
  preprint/paper and Fritz Reece's 2019 University of Chicago REU expository
  paper *Normalized Flow and Sperner Theory of Coxeter Groups*. No post-2020
  \(D_n\) solution record was returned. Semantic Scholar did not return Ke Ou
  in this query, illustrating why more than one index was used.

### 3.3 Publisher/Numdam cited-by list

- Opened the journal/Numdam record:
  [`https://www.numdam.org/articles/10.5802/alco.114/`](https://www.numdam.org/articles/10.5802/alco.114/).
- Result: the same two later formal citations as OpenAlex were displayed.

Citation indexes are discovery tools, not primary evidence for mathematical
content. Both later papers were therefore inspected separately.

## 4. Inspection of later citing papers

### 4.0 Contemporaneous expository record returned by the index

- Opened Fritz Reece, *Normalized Flow and Sperner Theory of Coxeter Groups*,
  [University of Chicago REU 2019
  PDF](https://math.uchicago.edu/~may/REU2019/REUPapers/Reece.pdf).
- This is an expository REU paper, not an independent proof or a later
  resolution. On PDF p. 11 it says that whether \(D_n\) is Sperner/has NFP is
  still open and repeats Gaetz–Gao's \(n\le8\) report.

### 4.1 Carnevale–Dyer–Sentinelli

- Opened official arXiv record
  [`2203.00405v2`](https://arxiv.org/abs/2203.00405v2), official API
  [`id_list=2203.00405`](https://export.arxiv.org/api/query?id_list=2203.00405),
  and PDF; publication metadata is DOI
  [10.1090/proc/16199](https://doi.org/10.1090/proc/16199), *Proc. Amer. Math.
  Soc.* **151** (2023), 1433–1443.
- Searched full text for `Sperner`, `normalized flow`, `type D`, `absolute
  order`, and `Gaetz`.
- Relevant location: Section 4, arXiv PDF pp. 10–11. The authors state that the
  strong Sperner result was given for finite Coxeter groups except type \(D_n\)
  and pose Problem 4.4 on Sperner properties of their broader
  \(k\)-absolute orders. They do not claim a normalized flow for \(D_n\), a
  \(D_9\) result, or a larger verified range.

### 4.2 Ou

- Opened DOI
  [10.1142/S021949882550118X](https://doi.org/10.1142/S021949882550118X)
  and inspected the publisher-visible title, abstract, and citation context.
- Publication: *Journal of Algebra and Its Applications* **24** (2025),
  2550118; received 2023-09-07, accepted 2023-10-16, first published
  2023-11-23.
- Full-text/search terms inspected where publicly visible: `Gaetz`, `Sperner`,
  `normalized flow`, `type D`.
- Result: the paper studies the absolute-length function for certain modular
  finite reflection subgroups of \(GL_n(\mathbb F_q)\). No result about
  normalized flows on the real Coxeter group \(D_n\) was located.

## 5. Broad literature and status searches

### 5.1 Web queries

Searches used exact phrases and combinations, including:

```text
"On the Sperner property for the absolute order on complex reflection groups"
"absolute order" "normalized flow" D_n
"Abs(D_n)" "normalized flow"
"type D" "normalized flow" Coxeter group Sperner
"verified this conjecture" "n = 8" absolute order
"Conjecture 1.3" Gaetz Gao
"Normalized-flow conjecture for the absolute order of type D"
```

The searches were repeated with year terms 2020 through 2026 and with targeted
domains `arxiv.org`, publisher sites, `github.com`, `zenodo.org`, `osf.io`, and
`figshare.com`.

- No later proof/disproof, \(D_9\) exact certificate, or extended verification
  range was located.
- Exact-phrase results overwhelmingly returned the original paper.
- A current secondary entry, [MathDB problem
  342030](https://mathdb.com/p/342030/normalized-flow-conjecture-for-the-absolute-order-of-type-d),
  labels the conjecture open and repeats the \(n\le8\) report. Because it is a
  secondary/automated tracker, it is used only as a freshness signal.

### 5.2 arXiv API topic queries

Queried the official arXiv API, newest first, with up to 100 results for:

```text
all:"normalized flow" AND all:"absolute order"
all:"absolute order" AND all:Sperner
all:"type D" AND all:"normalized flow"
```

The `absolute order` + `Sperner` search returned the 2019 Gaetz–Gao paper and
the related 2019 Harper–Kim–Livesay paper on types \(A\) and \(B\); it returned
no later type-\(D\) resolution. The two normalized-flow exact-combination
queries returned no additional relevant arXiv record.

### 5.3 Authors' visible publication records

- Checked Christian Gaetz's [research
  page](https://sites.google.com/berkeley.edu/gaetz/research) and current arXiv
  author search results.
- Searched for a matching Yibo Gao publication/code page, taking care not to
  conflate same-name researchers.
- No follow-up paper or code artifact resolving the conjecture was located.

## 6. Public-code and data search

### 6.1 GitHub

Used both GitHub repository search and authenticated code search (read-only)
for:

```text
1903.02033
"On the Sperner property for the absolute order on complex reflection groups"
"Gaetz" "Gao" "absolute order"
"computer search up to n = 8"
"computer search up to n=8"
"type Dn admits a normalized flow"
"normalized flow" language:Sage
"Abs(W)" "SageMath"
```

Also ran web-engine domain searches combining GitHub with the title, DOI,
authors, `SageMath`, `Coxeter`, and `normalized flow`. Result: no relevant
repository, code file, issue, or exact flow certificate was found.

### 6.2 Research repositories

Ran exact-title and topic searches against Zenodo, OSF, and Figshare via web
search and available public endpoints. No relevant dataset, software deposit,
or certificate was found.

The negative result is scoped to indexed public artifacts under the searched
identifiers and phrases. It does not establish universal nonexistence.

## 7. `NOVELTY_LOCK` decision

**Lock outcome: proceed with the \(D_9\) exact finite problem.** No public
resolution was located, and the source boundary requires only one wording
refinement:

- Safe: “\(D_9\) is the first case beyond Gaetz–Gao's published computer
  verification through \(n=8\), and no resolution was located in the dated
  search.”
- Too strong without additional evidence: “\(D_9\) has never been checked by
  anyone” or “this will be the first computation.”

The required second, independently phrased novelty search is recorded in
Section 8 below.

## 8. Second-pass post-result novelty audit

Date: 2026-08-29 (Asia/Shanghai). Trigger: an exact \(D_9\) candidate had been
produced, so the contractual post-result novelty check was run before any
release claim. This pass deliberately changed both vocabulary and discovery
paths. In place of the first pass's title/DOI/paper-language searches, it
emphasized `G(2,2,9)`, `D9`/`D_9`, even signed permutations, orbit flows,
Farkas certificates, \(n\ge9\), and a general type-\(D\) solution. The cutoff
was 2020--2026. Access failures are isolated in Section 8.6 and were not
counted as negative search evidence.

### 8.1 Reverse citations and bibliographic indexes

#### zbMATH Open

- The DOI lookup
  [`https://zbmath.org/?q=doi%3A10.5802%2Falco.114`](https://zbmath.org/?q=doi%3A10.5802%2Falco.114)
  identifies Zbl 1528.20057 / internal record 7207838 and displays “Cited in 4
  Documents.” The reverse query
  [`https://zbmath.org/?q=rf%3A7207838`](https://zbmath.org/?q=rf%3A7207838)
  returns:
  1. Ou's 2025 modular absolute-length paper (already audited in Section 4.2);
  2. Carnevale--Dyer--Sentinelli's 2023 intermediate-orders paper (already
     audited in Section 4.1);
  3. Christian Gaetz and Yibo Gao, *The hull metric on Coxeter groups*, DOI
     [10.5070/C62257870](https://doi.org/10.5070/C62257870), arXiv
     [`2012.06841`](https://arxiv.org/abs/2012.06841);
  4. Harper--Kim--Livesay's contemporaneous type-\(A\)/\(B\) paper, DOI
     [10.37236/8874](https://doi.org/10.37236/8874), arXiv
     [`1902.08334`](https://arxiv.org/abs/1902.08334).
- The third item is the one relevant record missed by the first-pass
  OpenAlex list. Its full text was checked. It studies the (simple-reflection)
  Cayley graph's hull/strong-hull property. The remark after Corollary 4.11,
  arXiv PDF pp. 9--10, says only that the signed-permutation framework there
  does not deduce the strong hull property in type \(D\). It neither studies
  normalized flows on the absolute order nor gives a \(D_9\), \(n\ge9\), or
  general \(D_n\) result.
- New 2020--2026 topic queries included `"normalized matching" "type D"`,
  `Sperner "type D" "absolute order"`, `"even signed permutations"
  Sperner`, `"G(2,2,n)" Sperner`, `D9 Coxeter Sperner`, and `"absolute
  order" flow certificate`. Focused queries returned no document. Broader
  searches for `"absolute order" Coxeter`, `Sperner Coxeter`, and `"type D"
  Coxeter poset` were title-screened; the original paper, the records above,
  and unrelated absolute/noncrossing/Bruhat-order papers were found, but no
  resolution of the target.

#### OpenAlex, OpenCitations, and Crossref

- Repeated the OpenAlex DOI lookup
  [`W2921670843`](https://api.openalex.org/works/https://doi.org/10.5802/alco.114)
  and a [2020--2026 topic
  query](https://api.openalex.org/works?search=type%20D%20Coxeter%20absolute%20order%20Sperner&filter=from_publication_date%3A2020-01-01%2Cto_publication_date%3A2026-12-31&per-page=100).
  The work record still reports two indexed citations, and the topic results
  returned the original paper, the type-\(A\)/\(B\) paper, the intermediate-
  orders paper, and unrelated records; no \(D_9\) or general-\(D_n\) solution
  was present. An exact `G(2,2,9) Sperner flow` search returned zero works.
- Queried OpenCitations COCI through both the
  [v1 endpoint](https://opencitations.net/index/coci/api/v1/citations/10.5802/alco.114)
  and the [v2 endpoint](https://opencitations.net/index/api/v2/citations/doi:10.5802/alco.114).
  They list the same two DOI-indexed later citations as OpenAlex: Ou and
  Carnevale--Dyer--Sentinelli. The difference from zbMATH's four records is
  an index-coverage difference, not mathematical evidence.
- Crossref bibliographic queries for
  [`type D Coxeter absolute order
  Sperner`](https://api.crossref.org/works?query.bibliographic=type%20D%20Coxeter%20absolute%20order%20Sperner&filter=from-pub-date%3A2020-01-01%2Cuntil-pub-date%3A2026-12-31&rows=100),
  `D9 absolute order Coxeter normalized flow`, `G(2,2,9) Sperner`, and the
  authors plus `normalized flow` returned the already known records or noisy
  false positives, but no competing result. Crossref is a metadata index, not
  a theorem/full-text index, so this is supporting coverage only.

#### MathSciNet and Semantic Scholar

- The public identifier MR 4113607 was rechecked from the journal/Numdam
  metadata. Direct
  [`mathscinet-getitem?mr=4113607`](https://mathscinet.ams.org/mathscinet-getitem?mr=4113607)
  access redirected to an institutional/authentication route, so no
  MathSciNet reverse-citation conclusion was drawn.
- The second-pass Semantic Scholar topic endpoint returned HTTP 429. The
  successful first-pass DOI citation response remains recorded in Section
  3.2, but the rate-limited second attempt contributes no negative evidence.

### 8.2 arXiv and current author records

- New exact arXiv API topic searches, newest first, were run for

  ```text
  all:"even signed permutations" AND all:Sperner
  all:"G(2,2,9)"
  all:"D_9" AND all:"absolute order"
  all:"Farkas certificate" AND all:Coxeter
  ```

  Each returned zero records. As a positive-control author query,
  `au:"Christian Gaetz" AND all:Sperner` returned four records, including the
  original paper and three papers on other orders; none was a type-\(D\)
  normalized-flow resolution. Thus the exact zeroes above were not caused by
  a generally nonfunctional API route.
- Inspected Yibo Gao's authoritative [BICMR publication
  page](http://faculty.bicmr.pku.edu.cn/~gaoyibo/research.html), which lists
  papers through 2026. It lists the original article and repeats its
  “except possibly type \(D_n\)” abstract, but lists no normalized-flow,
  \(D_9\), or later absolute-order solution.
- Inspected Christian Gaetz's current [UC Berkeley faculty
  page](https://vcresearch.berkeley.edu/faculty/christian-gaetz), which links
  ORCID [0000-0002-3748-4008](https://orcid.org/0000-0002-3748-4008), and
  queried the [public ORCID works
  endpoint](https://pub.orcid.org/v3.0/0000-0002-3748-4008/works). Among the
  29 returned titles are the original paper and *The hull metric on Coxeter
  groups*; no title or identifier indicates a \(D_9\), \(n\ge9\), or general
  type-\(D\) flow result.
- OpenAlex's author entity attached to Yibo Gao in the original work is
  visibly conflated with same-name medical publications/institutions.
  Therefore no negative inference was made from that author entity; the
  BICMR page above was used instead.

### 8.3 Public code and research-object repositories

#### GitHub

Authenticated GitHub code search returned zero results for each focused query:

```text
"G(2,2,9)"
"D9" "Sperner"
"D_9" "Sperner"
"even signed permutations" "normalized flow"
"type D" "absolute order" language:Sage
"Farkas" "absolute order"
"orbit flow" "Coxeter"
```

Repository search likewise returned zero for `G(2,2,9) Sperner`, `D9
normalized flow Coxeter`, `even signed permutation poset flow`, `type D
absolute order`, and `Coxeter normalized matching poset`. A deliberately
broad code query for `"type D" "absolute order" language:Python` returned
100 mostly generic text-fragment matches; manual screening found them
irrelevant, and that capped broad count was not used as absence evidence.

#### Zenodo and OSF

- The Zenodo public records API returned total zero for exact-phrase queries
  `"D9 normalized flow"`, `"G(2,2,9)"`, `"type D absolute order"`, and the
  exact Gaetz--Gao paper title. A loose type-\(D\) search found Zenodo record
  [14497933](https://zenodo.org/records/14497933), *type-D-bruhat: v1.0.0*.
  Its metadata describes a Sage program for a type-\(D\) **Bruhat** graph and
  a spanning cubical subgraph, not the absolute-order normalized-flow
  problem; it is a false positive, not a competing certificate.
- The OSF public API's exact title-filter endpoints for
  [`nodes`](https://api.osf.io/v2/nodes/?filter%5Btitle%5D=G%282%2C2%2C9%29),
  [`registrations`](https://api.osf.io/v2/registrations/?filter%5Btitle%5D=G%282%2C2%2C9%29),
  and
  [`preprints`](https://api.osf.io/v2/preprints/?filter%5Btitle%5D=G%282%2C2%2C9%29)
  returned total zero for each of `D9 normalized flow`, `G(2,2,9)`, `type D
  absolute order`, and `normalized flow Coxeter`. The generic `/v2/search/`
  route returned HTTP 404, so the conclusion is limited to these accessible
  object-type endpoints.

### 8.4 Primary reflection-length dependency

The classical rank dependency was checked against a primary source rather
than left implicit:

- R. W. Carter, *Conjugacy classes in the Weyl group*, *Compositio
  Mathematica* **25** (1972), no. 1, 1--59,
  [Numdam](https://www.numdam.org/item/CM_1972__25_1_1_0/).
- Section 2, Lemma 2, journal p. 3 states that the reflection length \(l(w)\)
  equals the number of eigenvalues of \(w\) on \(V\) that are unequal to 1.
  For the finite orthogonal reflection representation this is
  \(\operatorname{codim}\operatorname{Fix}(w)\).
- The archived primary PDF
  [`sources/carter-1972.pdf`](sources/carter-1972.pdf) has SHA-256
  `9906164332f45299f337c5e95f8681c8ec02356a6b34d72aada16e7be0a3eaf5`.

### 8.5 Result of the post-result audit

No public proof/disproof, exact \(D_9\) orbit flow, \(n\ge9\) verification,
general \(D_n\) normalized-flow construction, or relevant public code deposit
was located in the accessible second-pass sources. The only new formal citing
paper missed by the first-pass two-citation indexes was *The hull metric on
Coxeter groups*, and full-text inspection showed that it addresses a
different Cayley-graph property.

Accordingly, the Gate 1 boundary does not need correction. The safe claim
remains:

> \(D_9\) is the first case beyond Gaetz--Gao's published computer report
> through \(n=8\), and neither of the two dated public searches located a
> later resolution.

This is not a claim that no private, unpublished, or unindexed computation
exists.

### 8.6 Access and index limitations (not used as negative evidence)

- MathSciNet article/citation access required an institutional/authenticated
  route; only the public MR identifier supplied by the publisher was checked.
- Direct Google Scholar exact-title access timed out, and the linked author
  profile returned HTTP 403. zbMATH, OpenAlex, OpenCitations, Crossref, arXiv,
  ORCID, and the authors' accessible institutional pages were used as public
  alternatives; none is represented as a complete substitute for Scholar.
- The second Semantic Scholar API call was rate-limited with HTTP 429.
- Figshare's public article-search API returned HTTP 403 for the focused
  queries. Therefore Figshare supplies no positive or negative evidence in
  this pass.
- Christian Gaetz's Google Sites research page timed out from this
  environment. His accessible current Berkeley page and public ORCID work
  record were used; the timeout itself was not treated as an absence result.
- The OSF generic search route returned HTTP 404, although exact title-filter
  endpoints for nodes, registrations, and preprints were accessible and are
  reported separately above.
