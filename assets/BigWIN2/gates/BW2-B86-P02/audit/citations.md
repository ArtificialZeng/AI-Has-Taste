# Citation and bibliography audit

Release job: `win-00086-p02-release-0b3f9cf5c11e`  
Citation attempt: 2  
Launch id: `43cdd192-fea6-4464-816e-6ccdb2051f0b`  
Verification date: 2026-09-09 UTC

## Scope and method

The audit used the requested two-stage, non-interactive protocol.  Stage 1
froze the eight citation-bearing claims and all six ordinary body-flow keys in
`audit/citation-claim-ledger.json`; its key union is exactly the body citation
set.  Stage 2 used the academic search templates from the citation-check skill
and inspected primary publisher, journal, arXiv, or preprint records and the
source passages identified below.  The BibTeX audit then compared author,
title, year, venue, volume/pages, DOI or arXiv identifier, and the nearby claim.

The publication inputs are exactly `manuscript/main.tex` and
`manuscript/references.bib`.  The six cited keys all occur in ordinary body
flow and in the canonical bibliography; there are no `\nocite`-only,
comment-only, hidden, missing, or unused entries.  The bibliography covers the
problem origin, the generalized graph definition, the closest conjecture and
its two preceding extreme cases, and the exact-verification comparison.  Five
of the six sources are natural non-library primary sources.  The single
user-library paper is the closest relevant method source; adding a second
library item would be padding.

## Frozen claims and source verification

| Claim | Key | Primary passage and result | Status |
|---|---|---|---|
| CIT-01 | `DayTripathi1992` | The publisher abstract calls the arrangement graph a new interconnection topology and a generalization of the star graph; the record gives Day and Tripathi, *Information Processing Letters* 42(5), 235--241 (1992), DOI 10.1016/0020-0190(92)90030-Y. | Verified, paraphrase |
| CIT-02 | `ChenGhorbaniWong2014` | The arXiv final version, Section 2, defines `A(n,k,r)` on the ordered `k`-permutations with adjacency at exactly `r` differing positions; the publisher record gives *Linear Algebra and its Applications* 444, 246--253 (2014), DOI 10.1016/j.laa.2013.11.035. | Verified, paraphrase |
| CIT-03 | `Pan2024` | The arXiv-v1 abstract and Theorem 1.2 treat `r=k` and `r=2,k=n`; Conjecture 3.1 gives the uniform symmetric-group Cayley formula. | Verified, paraphrase |
| CIT-04 | `DengZhang2011` | The official journal PDF, Theorem 1.1 on PDF p.2, states the full automorphism group of the derangement graph for `n>=3`. | Verified, paraphrase |
| CIT-05 | `Ganesan2015` | The arXiv abstract states the full automorphism group of the complete transposition graph; the same record supplies the 2015 journal reference and DOI. | Verified, paraphrase |
| CIT-06 | `Pan2024` | Conjecture 3.1 ranges over all `n>2` and `0<=k<=n-2`; `(4,1)` is therefore included.  The record lists only v1, submitted 29 July 2024. | Verified, exact logical instance |
| CIT-07 | `Pan2024` | Conjecture 3.1 explicitly displays `[R(S_n) semidirect Inn(S_n)] semidirect Z_2` with the same quantified range. | Verified, exact |
| CIT-08 | `ZengEtAl2026` | Version 1, Section 6, states that `verify_borsuk_ternary4.py` reconstructs all 81 points, all distances, all 15,056 maximal compatibility cliques, and the full symmetry action before accepting the certificate. | Verified, paraphrase |

No numerical discrepancy, omitted hypothesis, contradiction, misleading
strengthening, unverified citation, or unsupported novelty claim was found.
The manuscript expressly disclaims priority and makes no claim about the
inaccessible later journal text.

## Primary records inspected

| Key | Record or full text | Why retained |
|---|---|---|
| `DayTripathi1992` | https://www.sciencedirect.com/science/article/pii/002001909290030Y | Primary origin of arrangement graphs. |
| `ChenGhorbaniWong2014` | https://arxiv.org/html/1310.8078 and https://www.sciencedirect.com/science/article/pii/S0024379513007738 | Primary generalized-definition source and publication metadata. |
| `Pan2024` | https://arxiv.org/html/2407.19745v1 | Frozen source, extreme-family theorem, and exact conjecture. |
| `DengZhang2011` | https://www.combinatorics.org/ojs/index.php/eljc/article/download/v18i1p198/pdf | Official journal theorem for the complete derangement graph. |
| `Ganesan2015` | https://arxiv.org/abs/1404.7363 and https://doi.org/10.1007/s10801-015-0602-5 | Primary theorem plus journal/DOI metadata. |
| `ZengEtAl2026` | https://www.preprints.org/manuscript/202608.1658 | Primary version-1 method passage and DOI record. |

The mandatory searches were run for first-author/year/title words, exact
title with Semantic Scholar or arXiv restriction, author/year/venue, every
available DOI, and the supplied arXiv identifier.  DOI resolver failures were
not treated as evidence: the live primary pages above were inspected instead.
No `literature/crossref-*` supervisor capture exists in this project.

## Bibliography reconciliation

All six records exist and support their cited sentences.  Five BibTeX entries
already matched the verified publication records.  `Pan2024` incorrectly
listed the arXiv primary class as `math.CO`; the official record is `math.GR`,
and `manuscript/references.bib` was corrected.  No citation key changed and no
record remains blocked.  The canonical key checker reports six cited keys, six
BibTeX keys, no missing or unused key, and exact agreement with `main.aux`.

Overall status: **PASS** (8 of 8 frozen citation claims verified).
