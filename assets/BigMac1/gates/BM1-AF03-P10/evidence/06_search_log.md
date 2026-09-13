# Search log

Search lock date: 2026-08-29 (Asia/Shanghai).  “No result” below means only
no result in the named service and query, not proof of nonexistence.

## Frozen questions (before pass-2 searching)

1. What exact generic object and equivalence relation does the paper use?
2. Is the DOI and journal publication real, and what is its publication date?
3. What is the latest arXiv version and did its statement change?
4. Does the source really report verification exactly for \(n<9\)?
5. Has a later primary source proved or disproved Conjecture 12 or checked
   \(n=9\)?
6. Is the original computation/data/code public?

## Pass 2 searches and records

| Date | Service | Query / endpoint | Result used |
|---|---|---|---|
| 2026-08-29 | Springer | DOI landing page `10.1007/s10884-025-10446-2` | Version of record, open access, published 2025-07-10; abstract and Conjecture 12 verified. |
| 2026-08-29 | Crossref REST | `/works/10.1007/s10884-025-10446-2` | DOI/title/journal/date verified; indexed cited-by count 0; raw snapshot stored. |
| 2026-08-29 | OpenAlex REST | `/works/https://doi.org/10.1007/s10884-025-10446-2` | Work `W4412159887`, OA version, cited-by count 0; raw snapshot stored. |
| 2026-08-29 | arXiv API | `id_list=2411.18264` | Latest is v4, updated 2025-06-09; version-history comment records the general-class/special-subclass clarification. |
| 2026-08-29 | arXiv e-print | `2411.18264` | v4 source saved and inspected; Conjecture 12 and definitions verified. |
| 2026-08-29 | arXiv API/e-print | `id_list=2303.00229` | Foundational tree-system construction and edge-DP formula inspected. |
| 2026-08-29 | Web search | exact paper title; exact DOI; `Peter H van der Kamp Lotka Volterra tree systems conjecture n<9` | Located publisher, arXiv, foundational papers, and one subsequent citation. |
| 2026-08-29 | Web search | `"Nonisomorphic trees are not LV-equivalent"`; `"LV-equivalent" trees Lotka Volterra`; `"2411.18264" citing OR citation` | No later resolution located; found only restatements and related material. |
| 2026-08-29 | Web search | exact title/DOI excluding Springer/arXiv | Located van der Kamp--McLaren--Quispel (2026), which cites the paper but does not discuss or resolve Conjecture 12. |
| 2026-08-29 | GitHub-indexed web search | exact title; `LV-equivalent`; `2411.18264`; author plus `tree-system` | No relevant public repository located. |
| 2026-08-29 | Article Data Availability | inspected version of record | Order 5--8 equivalent-hypergraph sets are available only upon request. |

## Gate-1 conclusion

The prompt's historical boundary is correct as an author-reported frontier:
the 2025 version of record verifies \(n<9\), and no recorded later primary
source resolves \(n=9\).  The necessary correction is semantic: the conjecture
is about generic/general parametric classes, excluding special subclasses.
This lock authorizes independent baseline reproduction and order-nine work; it
does not claim that every database or private communication was searched.

## Pass 3: theorem-specific novelty recheck after proof discovery

Run on 2026-08-29 after the cone-incidence/three-circuit proof was written.

| Service | Query / endpoint | Result |
|---|---|---|
| Web search | `"cone over a tree" "cycle matroid" determines tree` | No matching theorem or LV application located. |
| Web search | `"cone of a tree" matroid isomorphism tree reconstruction` | No matching theorem or LV application located. |
| Web search | `graphic matroid cone tree reconstruction triangles` | Located only standard graphic-matroid representation material, not the target theorem. |
| Web search | `"linear Darboux polynomials" tree "projective" matroid` | No source connecting generic tree-system DPs to cone graphic matroids located. |
| Semantic Scholar API | DOI `10.1007/s10884-025-10446-2`, citations field | Exactly one indexed citation: arXiv `2604.01743` / DOI `10.46298/ocnmp.18125`; it does not address Conjecture 12. Raw snapshot stored. |
| OpenAlex API | `filter=cites:W4412159887` | Zero results (known incomplete relative to Semantic Scholar and the publisher). Raw snapshot stored. |
| arXiv API | `all:"LV-equivalent"`, 100 results | One irrelevant electronics-design false positive; no mathematical resolution located. Raw snapshot stored. |
| GitHub repository API | repository query `"LV-equivalent"` | Zero repositories. Raw snapshot stored. |

Pass-3 conclusion: no public antecedent of the exact general theorem or its
cone-matroid proof was found.  This is a bounded novelty search, not a legal or
absolute priority determination.
