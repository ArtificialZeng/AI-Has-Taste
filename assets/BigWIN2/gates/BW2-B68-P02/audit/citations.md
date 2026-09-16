# Citation and bibliography audit

## Scope and method

This is the second, verification-only pass for release job
`win-00068-p02-release-ad1c2e39c442`, citation attempt 7, launch
`19e4b0d4-8102-47fd-98db-15f8d58d6f9f`, over the claim extraction frozen in
`audit/citation-claim-ledger.json`.  The audited publication inputs are
`manuscript/main.tex` and `manuscript/references.bib`, bound to manuscript digest
`69e247a1f25611f7818daa501a600baa18cd74374eea5f2f4b2545f18b1ca737` and
PDF digest `1ce0b11ced22734c49a198b92d73f3652acde55382f314a00e61c8645898a671`.
Every fast-completion handoff predicate remained true, so this bounded recovery
did not repeat the attempt-6 web searches.  Instead, on 2026-09-08 I freshly
replayed all fifteen recorded claim/source locators against the unchanged audit
record and local evidence, directly reinspected the retained Adauto et al.
primary text, checked active-registry row 42 and its source BibTeX, and rechecked
the canonical BibTeX/AUX/log joins.  The attempt-6 authoritative source records
and exact locators remain unchanged; this report does not claim a new online
search.  The user expressly prohibited sub-agents, so the replay was performed
sequentially by this release worker.

## Coverage decision

The seven ordinary body-flow keys exactly equal the union of keys in the frozen
claim ledger.  The bibliography is not library-only: the primary problem source
and closest prior total-coloring result are cited, as are the natural sources for
the sequential-counter encoding, PySAT, DRAT checking, and nauty's
refinement--individualization framework.  The sole active user-library item is
used for a narrow method comparison and is explicitly said to concern an
unrelated algebraic property.  No other one of the 49 active first-sheet library
records naturally supports a manuscript claim; adding one would be padding.
No retained citation is decorative, and no substantive literature-dependent
claim lacks its natural source.

## Claim-to-source verification

| Claim | Key | Exact source location inspected | Status |
|---|---|---|---|
| C01 | `DantasEtAl2016` | Author-team prepublication text and the University of Modena IRIS publication record abstract: NP-completeness for bipartite cubic graphs and the first Type 1 cubic graphs with equitable total chromatic number 5.  Adauto et al., introduction lines 67--75 and Section 7 lines 792--814, explicitly attribute the order-20 graph R and the complexity result to this work. | Verified (paraphrase) |
| C02 | `DantasEtAl2016` | University of Modena IRIS and DBLP records for DOI `10.1016/j.dam.2015.10.013`: Discrete Applied Mathematics 209 (2016), 84--91; exact title and six-author list agree. | Verified (exact metadata) |
| C03 | `AdautoEtAl2026` | Primary arXiv v1, Section 7, Question 7.1 and following paragraph, PDF lines 791--814; retained text `evidence/external/2609.05259.txt`, lines 739--760. | Verified (exact) |
| C04 | `AdautoEtAl2026` | Primary arXiv v1, Lemma 3.1 and Corollary 3.2, PDF lines 159--226; retained text lines 172--229, including the vertex/edge class identity. | Verified (exact) |
| C05 | `AdautoEtAl2026` | arXiv record 2609.05259, submitted 2026-09-04, with the four listed authors and exact title. | Verified (exact metadata) |
| C06 | `Zeng2026Whiskered` | Primary SSRN record/PDF 7385138, abstract: 6,021 canonical graph isomorphism classes, graph6 representatives, and an independent short verifier reconstructing the matrices.  The manuscript limits the analogy to verification practice. | Verified (paraphrase) |
| C07 | `Zeng2026Whiskered` | SSRN primary record, posted 2026-09-03, Zijian Zeng, DOI `10.2139/ssrn.7385138`, exact title. | Verified (exact metadata) |
| C08 | `Sinz2005` | Author-hosted primary paper, Section 2, PDF pages 2--3, especially the sequential-counter construction and Theorem 1. | Verified (paraphrase) |
| C09 | `Sinz2005` | Springer DOI record and JKU publication record: CP 2005, LNCS 3709, pages 827--831, DOI `10.1007/11564751_73`. | Verified (exact metadata) |
| C10 | `IgnatievEtAl2018` | Author-hosted primary paper, abstract and Section 3.1, PDF pages 1--3: PySAT integrates cardinality encodings and explicitly lists sequential counters. | Verified (exact topic/paraphrase) |
| C11 | `IgnatievEtAl2018` | SAT 2018 proceedings and University of Lisbon record: LNCS 10929, pages 428--437, DOI `10.1007/978-3-319-94144-8_26`. | Verified (exact metadata) |
| C12 | `WetzlerEtAl2014` | Author-hosted primary paper, abstract and Sections 1 and 3, PDF pages 1--3: DRAT format and DRAT-trim validation of unsatisfiability derivations. | Verified (paraphrase) |
| C13 | `WetzlerEtAl2014` | Primary paper and authors' DRAT-trim page: SAT 2014, LNCS 8561, pages 422--429, DOI `10.1007/978-3-319-09284-3_31`. | Verified (exact metadata) |
| C14 | `McKayPiperno2014` | arXiv 1301.1493 abstract and author-hosted record: refinement--individualization principles and their implementation in nauty and Traces. | Verified (paraphrase) |
| C15 | `McKayPiperno2014` | Journal/arXiv/DBLP records: Journal of Symbolic Computation 60 (2014), 94--112, DOI `10.1016/j.jsc.2013.09.003`. | Verified (exact metadata) |

All 15 frozen claims survive the fresh recovery replay; there are no numerical errors,
hallucinations, misleading attributions, citation-not-found results, or
unverified claims.  No BibTeX key or entry needed replacement.

## Authoritative sources consulted

| Key | Primary or authoritative record | Why retained |
|---|---|---|
| `AdautoEtAl2026` | <https://arxiv.org/abs/2609.05259> and retained v1 PDF/text | Exact problem origin, Question 7.1, and decomposition lemma. |
| `DantasEtAl2016` | <https://www.sciencedirect.com/science/article/pii/S0166218X15005004> | Closest prior result and order-20 context. |
| `McKayPiperno2014` | <https://arxiv.org/abs/1301.1493> | Canonical graph generation/isomorphism method. |
| `Sinz2005` | <https://www.carstensinz.de/papers/CP-2005.pdf> | Sequential-counter cardinality encoding. |
| `IgnatievEtAl2018` | <https://alexeyignatiev.github.io/assets/pdf/imms-sat18-preprint.pdf> | PySAT and its cardinality encodings. |
| `WetzlerEtAl2014` | <https://www.cs.cmu.edu/~mheule/publications/drat-trim.pdf> | DRAT proof format and checker. |
| `Zeng2026Whiskered` | <https://papers.ssrn.com/sol3/Delivery.cfm/7385138.pdf?abstractid=7385138&mirid=1&type=2> | Gate-selected, genuinely relevant finite-verification comparison. |

## Mechanical consistency

On attempt 7 the bibliography checker found 7 cited keys, 7 BibTeX entries, no missing or
unused entries, and exact agreement with the 7 `\bibcite` keys in `main.aux`.
The converged `main.log` and `main.blg` contain no undefined citation/reference,
missing database entry, duplicate entry, BibTeX warning, LaTeX error, or fatal
diagnostic.  The citation audit therefore accepts the current manuscript.
