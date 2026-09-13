# Search log

Search date: 2026-08-30 (Asia/Shanghai).  Gate 1 was completed before the main
finite search.  URLs are recorded so the negative search can be scoped and
repeated; absence from these queries is not a universal nonexistence claim.

## Frozen questions

1. Does a primary source state the exact value of the largest cyclic
   \(3-(31,5,1)\) packing, equivalently the cardinality \(\Phi(31,5,2)\) with
   both correlation bounds equal to 2?
2. Are the stated \(9\le M\le13\), 145 resources, and 4761 internally valid
   block-orbit columns correct?
3. What is the publication status and latest version of the cited foundational
   and neighboring work?
4. Is there later literature or public code containing a size-10-or-larger
   construction or an exact upper-bound certificate?

## Queries and results

| Time/order | Service | Query or record | Result relevant to this project |
|---|---|---|---|
| 1 | TheoremDB | <https://www.theoremdb.org/statements/cyclic-315-packing-31/> | Snapshot dated 2026-07-25: status Open; retained interval 9--13; nine blocks; pair-incidence argument; 145/4761 enumeration report; no proof for sizes 10--13. |
| 2 | Web exact phrase | `"3-(31,5,1)" cyclic packing`, `cyclic 3-(v,5,1) packing 31` | No independent source settling the exact target was returned. |
| 3 | Web OOC notation | `"(31,5,2)" "optical orthogonal code"`, `"Phi(31,5,2)"`, variants with weight/correlation | No source stating the required cardinality was found.  Results with notation \((v,5,2,1)\) have cross-correlation 1 and are not the present problem. |
| 4 | IEEE/Crossref | DOI <https://doi.org/10.1109/18.30982> and Crossref API | Confirmed Chung, Salehi, Wei, *IEEE Trans. Inform. Theory* 35 (1989), 595--604.  This is the foundational OOC framework, not a parameter-specific solution. |
| 5 | Crossref/Elsevier | DOI <https://doi.org/10.1016/j.disc.2011.11.039> | Confirmed Bailey--Burgess, *Generalized packing designs*, *Discrete Math.* 313 (2013), 1167--1190. |
| 6 | ScienceDirect/Crossref | DOI <https://doi.org/10.1016/S0012-365X(03)00266-8> | Confirmed Chu--Colbourn, *Optimal (n,4,2)-OOC of small orders*, *Discrete Math.* 279 (2004), 163--172; weight 4, hence adjacent only. |
| 7 | arXiv export API | `all:"optical orthogonal code" AND all:"31" AND all:"weight 5"` | Zero records.  Searches for cyclic \(3\)-difference packings and recent OOC work returned no exact target. |
| 8 | zbMATH Open / public MathSciNet web search | exact parameter and relevant OOC titles | zbMATH returned weight-5 papers with unequal \((2,1)\) constraints; no exact \((31,5,2,2)\) record.  No public MathSciNet result settling the parameter was located. |
| 9 | OpenAlex API | exact target string and DOI metadata/citation records | Exact target query returned zero works.  DOI records confirmed later citation activity for the foundational papers but no title/abstract hit for this parameter. |
| 10 | Library and Archives Canada | L. Moura thesis PDF <https://www.collectionscanada.gc.ca/obj/s4/f2/dsk1/tape7/PQDD_0013/NQ41034.pdf> | Inspected Chapter 4 and cyclic-packing tables.  The tables cover related small instances but not \(3-(31,5,1)\). |
| 11 | GitHub and Zenodo web index | exact target, `Phi(31,5,2)`, OOC exact-search variants | No target-specific repository or certificate found.  Zenodo has large datasets for \((v,4,1)\), which are different parameters.  GitHub's unauthenticated code-search API itself returned HTTP 401, so the negative claim is limited to indexed web results. |
| 12 | TheoremDB related records | R184--R188 | The retained Python artifact is described but not exposed here as a trusted local dependency; all baseline counts and witnesses will be rebuilt independently. |

## Publication/version notes

- No arXiv version was found for the 1989 IEEE foundational article, the 2013
  Bailey--Burgess article, or the 2004 Chu--Colbourn article.  The DOI/publisher
  versions are therefore the versions used for metadata and scope.
- TheoremDB P2632 is a reviewed research-memory snapshot (CC0), not a formally
  published original theorem paper and not a proof certificate for the optimum.
- Crossref citation counts and OpenAlex `cited_by_count` are discovery aids only;
  they are not evidence that every citing work was read.  Exact-parameter and
  title/abstract searches were used to screen later work, with a second pass
  required if the computation produces a new endpoint.

## Gate transition

`NOVELTY_LOCK` entered after query 12.  The next permitted actions are exact
local reproduction of the baseline and structural reduction.  The lock will be
reopened for a second novelty search after a candidate exact value is certified.

## Gate 2 post-result pass

Search date: 2026-08-30, after the global target-13 verifier accepted all 162
fixed multiplier branches.

| Order | Service | Query or record | Post-result finding |
|---|---|---|---|
| G2-1 | TheoremDB | `cyclic-315-packing-31`, P2632 | Still `Open`; displayed certified interval remains 9--13. No 12-block construction or target-13 certificate is present. |
| G2-2 | arXiv export API | exact `all:"3-(31,5,1)"` | `opensearch:totalResults = 0`, feed updated 2026-08-30T08:09:14Z. |
| G2-3 | arXiv export API | exact `all:"Phi(31,5,2)"` | `opensearch:totalResults = 0`, feed updated 2026-08-30T08:09:23Z. |
| G2-4 | OpenAlex API | exact full-text searches for the two strings | `Phi(31,5,2)` returned zero. The sole `3-(31,5,1)` token hit was the unrelated 2024 paper *Sampling-Based Attack for Centrality Disruption in Complex Networks*. |
| G2-5 | Crossref API | exact bibliographic target string | Returned punctuation/number false positives, none in design theory or OOCs and none stating this result. |
| G2-6 | Later OOC literature | Baicheva--Topalova DOI `10.1007/s00200-013-0192-1`; Baicheva--Topalova DOI `10.55630/mem.2026.55.329-339` | The former classifies \((v,5,2,1)\) OOCs, whose cross-correlation limit is 1; the latter treats \((v,k,1)\) OOCs. Both are neighboring but different problems. |
| G2-7 | OpenAlex citation screening | works citing DOI `10.1109/18.30982`, targeted by `optical orthogonal`, `31`, and `weight 5` | Three returned works were unrelated to the equal-bound-2 exact parameter; no target solution appeared. The foundational record had 1,129 OpenAlex citations and update date 2026-08-27, so this was a targeted screen rather than a claim to have read every citing paper. |
| G2-8 | GitHub / indexed web | exact target strings; unauthenticated code-search API | Indexed web search returned no target repository. The GitHub code-search API again returned HTTP 401, so absence of private or unindexed code is not claimed. |
| G2-9 | Zenodo API | exact target-string query | Returned five punctuation/token false positives in unrelated biodiversity records, and no design/OOC artifact. |

Post-result conclusion: no checked primary publication, preprint, professional
database record, or public artifact settles the exact parameter or duplicates
the local witness/certificate. Novelty is therefore provisional within this
explicit scope.
