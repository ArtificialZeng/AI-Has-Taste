# Search log

Search cutoff: **2026-08-30 Asia/Shanghai** (UTC data queried around
2026-08-29 23:45–23:55). Negative findings are limited to the listed sources
and literal/broadened queries.

## Pass 1 — frozen claims

Before browsing, claims C01–C14 in `claim_ledger.md` were fixed: definition,
29,212 census, 333/334 construction, 388 upper bound, current interval,
new-record threshold, exact local replay claims, latest versions, later work,
formal metadata, and public-code availability.

## Pass 2 — source and novelty checks

| Time/local | Source/database | Query/action | Result used |
|---|---|---|---|
| 2026-08-30 | TheoremDB | opened P2796 and records R497, R502–R506, R499/R500 | snapshot reviewed 2026-07-28: 334–388; exact public replay reports the unique direct extension, radius-five closure, and Singer cap; radius six was still only a proposed next experiment |
| 2026-08-30 | arXiv | opened 1708.06224 and version history | latest v5 dated 2019-03-22; Theorem 2 gives 333 planes; Appendix C gives 103 orbit representatives under \(G_{4,6}\) |
| 2026-08-30 | arXiv | opened 1809.09352 and version history | latest v2 dated 2020-10-30; Theorem 1.1 states \(A_2(7,4)\le388\); paper also reports an integer-only fallback 394 |
| 2026-08-30 | arXiv API | `all:"A_2(7,4)"`, 100 results, newest first | exactly one hit: arXiv:1809.09352v2 |
| 2026-08-30 | arXiv API | `all:"mixed dimension subspace codes"`, 100 results, newest first | three hits: 1808.03580v3, 1802.09793v1, 1512.06660v3; none changes this parameter |
| 2026-08-30 | web search | exact notation variants; `335 subspace code Fano plane`; `334-388 subspace code` | found no primary source claiming 335 or an upper bound below 388; current specialist table still shows 334–388 |
| 2026-08-30 | Subspace Codes, Bayreuth | binary mixed-dimension table, \(n=7,d=4\) | current displayed cell is 334–388 |
| 2026-08-30 | AIMS publisher | DOI 10.3934/amc.2019029 and DOI 10.3934/amc.2020034 | formal publication records and abstracts checked; upper-bound page explicitly states 388 |
| 2026-08-30 | Crossref API | both DOIs | journal metadata verified; citation counts treated only as database metadata |
| 2026-08-30 | zbMATH Open API | `doi:10.3934/amc.2019029` | record 7076474 / Zbl 1422.51004, reviewed journal article, metadata and mathematical summary verified |
| 2026-08-30 | zbMATH Open API | `doi:10.3934/amc.2020034` | API retry returned no payload; publisher/arXiv/Crossref independently verified metadata; logged as unavailable, not evidence |
| 2026-08-30 | public-code search | exact filename/hash of TheoremDB R497; GitHub queries | public replay provenance and hashes found on TheoremDB, but no directly downloadable primary-paper code repository found |
| 2026-08-30 | arXiv source | decompressed 1708.06224v5 in a temporary directory | exact \(G_{4,6}\) generators and all 9+26+68 Appendix C representatives inspected |

## Primary records

- https://arxiv.org/abs/1708.06224 (v5 used)
- https://doi.org/10.3934/amc.2019029
- https://arxiv.org/abs/1809.09352 (v2 used)
- https://doi.org/10.3934/amc.2020034
- https://doi.org/10.3934/amc.2016033
- https://subspacecodes.uni-bayreuth.de/table/2/
- https://api.zbmath.org/v1/document/_search?search_string=doi%3A10.3934%2Famc.2019029

## Search boundary

C12 means only “not found in these recorded searches by the cutoff.” A second
novelty pass is required if a strict new mathematical result emerges. No current
evidence justifies silently replacing 334–388.

## Pass 3 — post-result novelty check

Run after the exact radius-seven result was independently verified.  The search
was specifically aimed at the bounded claim, not merely the global parameter.

| Time/local | Source/database | Query/action | Result used |
|---|---|---|---|
| 2026-08-30 | web search | `"radius-seven" subspace code 333 exchange` | no matching mathematical publication or public certificate found |
| 2026-08-30 | web search | `"radius 7" "A_2(7,4)" subspace code` | no matching result found |
| 2026-08-30 | web search | `"deleting at most six" published planes subspace code` | no matching result found |
| 2026-08-30 | web search | `"blocker" "333" "subspace code"` | no matching radius-six/seven completion found |
| 2026-08-30 | TheoremDB P2796/R500/R504 | rechecked local-exchange records | R504 reports closure only through radius five; R500 lists radius six as a future experiment |

Within this recorded search boundary, the certified closure through radius
seven is new.  This is not a proof that no unindexed or private computation
exists, and it does not change the global interval.
