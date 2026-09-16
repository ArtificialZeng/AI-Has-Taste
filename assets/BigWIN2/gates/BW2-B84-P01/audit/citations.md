# Citation and bibliography audit

Release job: `win-00084-p01-release-fe275ec7f516`  
Citation attempt: 2  
Launch ID: `3027e6fd-e76c-4cf1-822d-09fd1137b793`  
Search/verification date (UTC): 2026-09-09  
Mode: search verification, followed by a LaTeX/BibTeX consistency audit

## Two-stage protocol

Pass 1 read the complete canonical manuscript and bibliography and froze twelve
claim/citation pairs in `audit/citation-claim-ledger.json` before any verification
conclusion was recorded.  Its five-key union is exactly the ordinary body-flow
citation set.  Pass 2 then checked the claims in identifier order against primary
text and authoritative publication records.  The user prohibited sub-agents, so
the per-reference checks were performed sequentially by this release worker.

## Claim-level findings

| Claim | Key | Status | Primary evidence and exact locator |
|---|---|---|---|
| C01 | `CarrDevadoss2006` | Verified (paraphrase) | Carr--Devadoss arXiv `math/0407229v2`, abstract and Section 2, especially Theorem 2.6; the publisher record at `https://www.sciencedirect.com/science/article/pii/S016686410500249X` says the constructed graph-associahedron has face poset based on connected subgraphs. |
| C02 | `CarrDevadoss2006` | Verified (exact metadata) | The same ScienceDirect record gives title, authors, *Topology and its Applications* 153(12), 2155--2168 (2006), and DOI `10.1016/j.topol.2005.08.010`. |
| C03 | `CardinalPourninValenciaPabon2022` | Verified (paraphrase) | Frozen primary PDF `evidence/external/2106.16130v2.pdf`, PDF pp. 2--3, Sections 1.1--1.3: maximal tubings are vertices, search trees are in bijection with them, and flips are rotations. |
| C04 | `CardinalPourninValenciaPabon2022` | Verified (exact specialization) | Frozen PDF pp. 4--5, Theorems 2 and 8, and p. 18, Question 2.  With `p=q=3`, Theorem 8 gives `9+floor(3/2)+3=13`; because `K_{3,3}` is a subgraph of `SPK_{3,3}`, Theorem 2 gives the stated upper bound. |
| C05 | `CardinalPourninValenciaPabon2022` | Verified (exact topic) | Frozen PDF p. 2, Section 1.2: a vertex and its descendants form a subtree and those subtree vertex sets are exactly the tubes in the corresponding maximal tubing. |
| C06 | `CardinalPourninValenciaPabon2022` | Verified (exact metadata) | Official arXiv record `https://arxiv.org/abs/2106.16130` gives the authors, v2 date, journal reference *Annals of Combinatorics* 26(4), 873--902 (2022), and related DOI `10.1007/s00026-022-00598-z`. |
| C07 | `GargantiniPastineTorres2024` | Verified (exact specialization) | Frozen primary PDF `evidence/external/2406.06317v2.pdf`, PDF p. 28, Theorem 4.7, and p. 29, Corollary 4.8.  Taking the three true twins of `SPK_{3,3}` yields `13-binomial(3,2)=10`; Corollary 4.8 yields the same lower bound and contains no upper bound. |
| C08 | `GargantiniPastineTorres2024` | Verified (exact metadata) | Title page of the frozen PDF and official arXiv record `https://arxiv.org/abs/2406.06317` give all three authors, title, identifier, subject, and v2 date 10 October 2024; the bibliography accurately identifies it as an arXiv preprint. |
| C09 | `BronKerbosch1973` | Verified (exact topic) | Official ACM record `https://dl.acm.org/doi/10.1145/362342.362367` and the article's algorithm statement identify Algorithm 457 as the enumeration procedure for maximal complete subgraphs (cliques). |
| C10 | `BronKerbosch1973` | Verified (exact metadata) | The ACM record gives Coen Bron and Joep Kerbosch, *Communications of the ACM* 16(9), 575--577, 1 September 1973, DOI `10.1145/362342.362367`. |
| C11 | `ZengEtAl2026Certificates` | Verified (paraphrase) | Primary Preprints.org article `https://www.preprints.org/manuscript/202608.1658`, Proposition 1 and Section 6: integer predicates, an independently reconstructing standard-library verifier, a separate list-based exact implementation, and the explicit sentence that ancillary files separate discovery from certification. |
| C12 | `ZengEtAl2026Certificates` | Verified (exact metadata) | The same primary record gives the exact title, four authors, version 1, and posting date 24 August 2026; the publisher DOI is `10.20944/preprints202608.1658.v1`. |

No numerical mismatch, unsupported strengthening, misleading omission, missing
citation, decorative reference, or failed claim was found.  The bounded statement
about not locating another determination remains explicitly non-priority language.

## Coverage and bibliography integrity

The bibliography is not library-only.  Four natural non-library sources cover the
origin/definition (`CarrDevadoss2006`), closest diameter results and search-tree
encoding (`CardinalPourninValenciaPabon2022`), the improved lower bound
(`GargantiniPastineTorres2024`), and the nontrivial maximal-clique method
(`BronKerbosch1973`).  The one selected active-library paper supports only the
stated methodological comparison.  All five entries are used in ordinary body
flow, and no key is supplied by `nocite`, comments, inert macros, or hidden text.

The bibliography checker found 5 cited keys, 5 BibTeX entries, no missing or unused
entry, and an exact match with the converged AUX set.  Final logs contain no
undefined citation/reference, missing database entry, repeated entry, BibTeX
warning, or TeX fatal error.  Author, title, year, venue/version, pages, DOI/arXiv
identifier, and nearby support all agree with the checked records.  No BibTeX or
key replacement was necessary.

The required `literature/crossref-*.json` and `.md` supervisor captures were
enumerated and none existed.  Fresh official arXiv, ACM, ScienceDirect, and
Preprints records plus the two frozen primary PDFs supplied the needed metadata
and exact passages; no Crossref-only inference was used.

Overall status: **PASS** (12/12 frozen claims verified; 0 failed).
