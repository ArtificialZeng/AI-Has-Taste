# Search log

Search cutoff: 2026-08-30 (Asia/Shanghai).  Search performed from the current
workspace.  Technical claims were checked against primary papers or official
metadata; search-result snippets were used only to locate them.

## Frozen claims before search

1. The journal metadata and exact scope of Lam--Leung.
2. The strongest proved endpoint and status of weights 17--21 in
   Christie--Dykema--Klep.
3. Whether `weight <= 19` is a published result or a computational artifact.
4. Whether weight 20 for distinct 105th roots is already resolved.
5. The latest arXiv revision, journal/DOI status, later citations, and public
   implementation state.

## Queries and records

| Date | Service | Query/record | Result used |
|---|---|---|---|
| 2026-08-30 | TheoremDB | `minimal-vanishing-105th-root-sums`, P2744 | Packet snapshot 2026-07-28; seven orbits through 19; R528 leaves weight 20 as next experiment. |
| 2026-08-30 | TheoremDB | R526 inline replay | Exact 48 by 105 matrix method, source/output digests, seven representatives, dependencies, and replay limits. |
| 2026-08-30 | arXiv | `2008.11268v2` | v2 dated 2025-12-16; proof through 16; 17--21 conjectural; preliminary floating-point implementation. |
| 2026-08-30 | arXiv | `math/9511209` | Lam--Leung preprint corresponding to the 2000 Journal of Algebra article. |
| 2026-08-30 | Elsevier/Crossref | DOI `10.1006/jabr.1999.8089` | Verified title, authors, journal, volume, issue, date, pages, DOI. |
| 2026-08-30 | DataCite | DOI `10.48550/arXiv.2008.11268` | Preprint metadata, version 2, revision timestamps; no related journal identifier. |
| 2026-08-30 | Crossref | title query `Classifying minimal vanishing sums of roots of unity` | No matching journal version of the Christie--Dykema--Klep preprint returned. |
| 2026-08-30 | OpenAlex | work W3080270668 and `cites:W3080270668` | Preprint record and two indexed citing works; neither resolves fixed conductor 105 at weight 20. |
| 2026-08-30 | GitHub | `lchristie/Sums-of-Roots-of-Unity` | Public repository README/files inspected; related type-generation code only. |
| 2026-08-30 | author page | Igor Klep preprints/publications | Work remains listed as a preprint; public code link located. |
| 2026-08-30 | web/arXiv | exact phrases combining `minimal vanishing`, `105`, `105th roots`, `conductor 105`, `weight 19`, `weight 20`, `distinct roots`, `affine`, `Galois` | No additional primary resolution located. |
| 2026-08-30 | zbMATH/MathSciNet web indices | exact title and keyword searches | No journal version or exact endpoint record located in accessible results. |

## Primary URLs

- https://doi.org/10.1006/jabr.1999.8089
- https://arxiv.org/abs/math/9511209
- https://arxiv.org/abs/2008.11268v2
- https://github.com/lchristie/Sums-of-Roots-of-Unity
- https://theoremdb.org/statements/P2744/
- https://theoremdb.org/records/minimal105-artifact-exhaustive-replay-through-nineteen/
- https://theoremdb.org/records/minimal105-attempt-extend-to-weight-twenty/

## Version trap and bounded conclusion

The 2020 v1 language treated the computed extension more strongly.  The current
v2 expressly demotes the implementation-dependent portion to experimental,
conjectural evidence because the implementation was not formally verified and
used floating-point vanishing tests.  All research below uses v2 as the current
source and does not promote its Appendix A table to a theorem.

No-result entries mean only “not found by these recorded services and queries by
the cutoff.”  A second novelty and citation pass is required after obtaining a
mathematical result.

## Result-aware second pass

Performed on 2026-08-30 after the independent verifier returned `VERIFIED`.

| Service | Query/record | Result used |
|---|---|---|
| General web index | Exact string `0,1,3,9,11,24,26,30,41,42,45,46,61,63,71,72,76,84,87,93` | No matching mathematical record for the first representative. |
| General web index | Exact string `0,1,3,11,12,16,24,33,41,42,45,46,54,63,71,75,76,84,86,87` | No matching mathematical record for the second representative. |
| arXiv/web | `minimal vanishing`, `105th roots`, `conductor 105`, `weight 20`, and the Christie--Dykema--Klep title with 2026/citation filters | No later arXiv resolution found; current arXiv record remains 2008.11268v2. |
| TheoremDB | P2744 and R528 | Live page still reports seven orbits through 19 and weight 20 open. |
| Crossref API | exact title query for `Classifying minimal vanishing sums of roots of unity` | No journal version of that preprint returned; nearby Lam--Leung and Sivek records were identified. |
| OpenAlex API | W3080270668 and `filter=cites:W3080270668` | `cited_by_count=2`, record updated 2026-08-26; the same two citing works do not resolve this fixed-conductor endpoint. |
| J-GLOBAL / zbMATH-linked metadata | exact preprint title | Still classified as an arXiv preprint, updated for the 2025 revision. |
| GitHub API | latest commit of `lchristie/Sums-of-Roots-of-Unity` | Head remains `b0563b270dc89ed7ca9e195535a107d5a81cc6dc`, dated 2020-07-28. |
| Publisher / primary PDF | Gary Sivek, DOI 10.1515/integ.2010.031 | Theorem 2 classifies possible cardinalities of vanishing distinct-root subsets, not minimal subsets or affine orbits. |

Release conclusion: within these recorded sources and this date, neither new
representative nor an equivalent complete weight-20 result was found.
