# Citation audit

## Verification report

**Mode:** search verification with locally archived primary PDFs  
**Document:** `paper/main.tex` / `paper/main.pdf`  
**Generated:** 2026-08-29 (Asia/Shanghai)  
**Overall status:** **PASS with bounded negative-search limitations**

| Metric | Count |
|---|---:|
| Frozen claims checked | 14 |
| Verified as stated and scoped | 14 |
| Numerical errors | 0 |
| Hallucinations/misquotations | 0 |
| Unverified absolute novelty claims | 0 |
| Bibliography entries cited/available | 5/5 |

The audit used the required two-pass architecture.  Pass 1 was the frozen
C01--C10 claim list in `literature/claim_ledger.md`; C11--C14 retained the new
IDs assigned when Gate 1 found scope corrections.  Pass 2 did not re-extract,
renumber, or silently alter those claims.

## Detailed findings

| ID | Short claim | Status | Primary location | Confidence |
|---|---|---|---|---|
| C01 | ELA title, six authors, volume 42, pages 146--161, DOI | verified | ELA article/PDF front matter | exact |
| C02 | Exact-support definition of \(S(G)\) and definition of \(q(G)\) | verified | Barrett et al., p. 146 | exact |
| C03 | \(e(\overline G)\le n-3\Rightarrow q(G)=2\) conjecture | verified | Barrett et al., Conj. 1.1, p. 147 | exact |
| C04 | Bipartite complements satisfy the threshold | verified | Barrett et al., Thm. 3.7, p. 153 | exact |
| C05 | Complete \(n=7,8\) baselines | verified | Fallat--Mojallal, Thms. 22--23 | exact |
| C06 | No full public \(n=9\) resolution found through the search date | verified as a bounded search result | Gate 1 and Gate 6 logs | interpretation |
| C07 | No public exact \(n=9\) certificate/code found | verified as a bounded search result | Gate 1 code search and Gate 6 repeat | interpretation |
| C08 | Two-eigenvalue/involution normalization | verified | direct proof in formal statement and manuscript | exact |
| C09 | Connected balanced joins have \(q=2\) | verified | Levene--Oblak--Šmigoc, Thm. 3.4, \(k=1\) | paraphrase |
| C10 | Fei--Luo has a different path-complement endpoint | verified | arXiv:2608.27227v1 main theorem | exact |
| C11 | First public formulation/provenance refinement | verified | Fallat--Mojallal, Conj. 1 and ref. 37 | exact |
| C12 | arXiv:2411.12917 has only v1; journal version is later | verified | arXiv history and ELA record | exact |
| C13 | Literature-only frontier can be reduced to nonbipartite six-edge complements | verified | stated-source synthesis plus elementary vertex count | interpretation |
| C14 | The nearby \(n=5\) path-complement aside is corrected but unused | verified | Fei--Luo boundary discussion | paraphrase |

C06 and C07 do not claim metaphysical absence.  Their wording is limited to
the documented databases, queries, date, and index-lag caveat; that scoped
wording is what was verified.

## Manuscript bibliography audit

| Key | Existence/metadata | Claim binding | Result |
|---|---|---|---|
| `BarrettEtAl2026` | ELA publisher and DOI 10.13001/ela.2026.9443 | Conj. 1.1 and Thm. 3.7 checked in publisher PDF | pass |
| `FallatMojallal2023` | MDPI and DOI 10.3390/math11163595 | Conj. 1/ref. 37 and Thms. 22--23 checked in publisher PDF | pass |
| `LeveneOblakSmigoc2024` | publisher/open repository and DOI 10.1080/03081087.2023.2232090 | Thm. 3.4 hypotheses and \(k=1\) consequence checked | pass |
| `McKayPiperno2014` | arXiv:1301.1493 and DOI 10.1016/j.jsc.2013.09.003 | `geng`/nauty discovery provenance only, not verifier completeness | pass |
| `ReadWilson1998` | OUP DOI 10.1093/oso/9780198532897.001.0001, ISBN 9780198532897 | atlas provenance; official NetworkX docs confirm all graphs through seven nodes | pass |

The LaTeX citation audit printed `cited=5 bib=5 missing=0 unused=0`.

## Sources consulted

- ELA publisher article/PDF: <https://journals.uwyo.edu/index.php/ela/article/view/9443>
- arXiv:2411.12917: <https://arxiv.org/abs/2411.12917>
- Fallat--Mojallal publisher record: <https://www.mdpi.com/2227-7390/11/16/3595>
- arXiv:2307.09663: <https://arxiv.org/abs/2307.09663>
- Levene--Oblak--Šmigoc publisher full text: <https://doi.org/10.1080/03081087.2023.2232090>
- Fei--Luo: <https://arxiv.org/abs/2608.27227>
- McKay--Piperno: <https://arxiv.org/abs/1301.1493>
- OUP graph atlas record: <https://academic.oup.com/book/54439>
- NetworkX `graph_atlas_g` documentation: <https://networkx.org/documentation/stable/reference/generated/networkx.generators.atlas.graph_atlas_g.html>
