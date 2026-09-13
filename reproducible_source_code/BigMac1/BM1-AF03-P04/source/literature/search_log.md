# Search log

Search lock date: 2026-08-29 (Asia/Shanghai).  Claims C01--C12 were frozen
before the substantive proof route was accepted.

| ID | Query / database | Result retained |
|---|---|---|
| S01 | arXiv record `2602.02342` | v1 submitted 2026-02-02; latest v2 revised 2026-02-08; 75 pages; arXiv DOI only. |
| S02 | downloaded arXiv v1 PDF | SHA-256 `23b24f57991549b4c67ae0c5b3b0aee29fb71257bc7ae5a123e2c547598e3656`; Conjecture 1.4; general case described as checked for “small n”. |
| S03 | downloaded arXiv v2 PDF | SHA-256 `0300ba3ecb9d4d9a6fe648d8c2f1f20135e520f5a82675e6521ec0b3d7de0044`; same mathematical conjecture renumbered 1.5; explicit `n <= 4`. |
| S04 | downloaded arXiv v2 TeX source | Read formula (1.2), transitive-CYBE equation (1.5), Conjecture 1.5, \S2.1 conventions, and Proposition 3.14/Corollary 3.15. |
| S05 | Crossref REST: title `Monomial bialgebras`, author `Berenstein` | No matching journal work returned. |
| S06 | OpenAlex title/full-text search | Work W7127541625 is classified as an arXiv preprint, DOI null, cited-by count 0 at query time. |
| S07 | web exact query `"Monomial bialgebras" "Conjecture 1.4"` | Found only the source copies/index pages; no later proof. |
| S08 | web exact query `"The transitive-array conjecture" CYBE` | Found MathDB problem page reporting no posted solution; this is secondary evidence only. |
| S09 | web exact query `"2602.02342" citation` | No later mathematical citation or solution located. |
| S10 | web exact query `"Monomial bialgebras" Berenstein Greenstein Li 2026` | Found arXiv/source mirrors and unrelated works; no formal publication. |
| S11 | web query `arXiv 2602.02342 code GitHub` | No relevant public repository found. |
| S12 | arXiv References & Citations/code panels | No linked code; external citation tools exposed but no recorded citing paper. |
| S13 | Semantic Scholar API for ARXIV:2602.02342 | Rate-limited (HTTP 429); recorded as unavailable, not as negative evidence. |
| S14 | second pass: `"Monomial bialgebras" "Conjecture 1.5"` | Only the source/preprint copies and index pages were found; no proof or counterexample. |
| S15 | second pass: `"transitive array" "classical Yang-Baxter" proof` | The source and MathDB open-problem page were the only relevant results. |
| S16 | second pass: `"transitive CYBE" solution conjecture` and `"r(a)" "transitive CYBE"` | Source copies, reviews, and unrelated CYBE pages; no later solution located. |
| S17 | OpenAlex `filter=cites:W7127541625` | Exact result count 0 at query time. |
| S18 | Crossref bibliographic query for `2602.02342` | Returned unrelated identifier matches and no matching journal publication. |
| S19 | GitHub code API exact-ID query | HTTP 401 without authentication; not counted as negative evidence. Public web exact-ID/title search remained negative. |
| S20 | NASA ADS citation endpoint | HTTP 405; unavailable and not counted as negative evidence. |

Primary URLs:

- <https://arxiv.org/abs/2602.02342>
- <https://arxiv.org/pdf/2602.02342v1>
- <https://arxiv.org/pdf/2602.02342v2>
- <https://export.arxiv.org/e-print/2602.02342v2>

Scope warning: “not found” means only not found in the dated, recorded
databases and queries.  It is not a universal nonexistence claim.
