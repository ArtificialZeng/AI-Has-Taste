# Fresh citation and bibliography audit

**Mode:** Search verification  
**Document:** `manuscript/main.tex`  
**Generated:** 2026-09-08 UTC

| Metric | Count |
|---|---:|
| Total frozen citation claims | 6 |
| Verified | 6 |
| Numerical Error | 0 |
| Unverified | 0 |
| Hallucination | 0 |
| Misleading | 0 |
| Citation Not Found | 0 |

**Overall status: PASS.**  This audit is bound to release job
`win-00073-p02-release-1f8a76d1e73a`, citation attempt 4, launch
`f4b94d83-db4e-4871-816c-adf7786ac115`, accepted evidence snapshot
`2a99216a023c7a9cfdc90150326d88f318af37372622653dccda563d6f4bf1c2`,
manuscript digest
`87e4a201ee7a53dcb0e9e88e27c3a6543d4249415b70c223e84e90588e584eaf`,
and PDF digest
`3da48aeeb45362f6198f6fce0d234affc709f83f76bd4afeca6e6ce22d918a19`.

## Two-stage method

Pass 1 extracted the ordinary body-flow claim/citation pairs from the complete
`manuscript/main.tex` and froze them in
`audit/citation-claim-ledger.json`.  Its six claims cover exactly the three body
citation keys `DumitruPrunescu2026`, `Hasse1936`, and
`ZengLiuRatnavelu2026`; comments, `\nocite`, inert text, and hidden
conditionals supply none of them.

Pass 2 treated that ledger as fixed and checked the cited primary records and
the exact nearby support.  On 2026-09-08 UTC I ran the prescribed author/year,
full-title, author/venue, DOI, and arXiv-identifier searches as applicable, then
inspected the primary arXiv HTML, the publisher and EuDML records for the Hasse
paper, and the versioned Preprints.org article.  The audit was performed
sequentially because this job expressly prohibited sub-agents.  Registry and
BibTeX metadata were used only as leads.

## Claim verification

| Claim | Status | Confidence | Direct source support |
|---|---|---|---|
| C01 | Verified | exact | Dumitru--Prunescu v1, Theorem 3, equations (4)--(5), arXiv HTML lines 233--240 in the 2026-09-08 retrieval. |
| C02 | Verified | exact | Theorem 3 assumes prime `p>=17`, counts affine pairs for every `A,B`, and explicitly includes repeated-root cubics; arXiv HTML lines 233--245, especially 235--242. |
| C03 | Verified | paraphrase | Hasse's 1936 primary article is the elliptic-function-field Riemann-hypothesis paper (pp. 193--208); the modern source states the resulting point-count bound as Hasse's theorem before using it. |
| C04 | Verified | exact scope check | Full-text inspection of Dumitru--Prunescu v1 finds the one-way `p>=17` theorem, not the manuscript's sharp biconditional or its four lower-prime witnesses; searches for the lower-prime witness language returned no such result. |
| C05 | Verified | paraphrase | Zeng--Liu--Ratnavelu v1 abstract and Introduction state that a strict prime-field boundary is closed and split the proof into above-half-rank and equality cases; Theorem 1.1 and its proof give the boundary and the structural equality-case route. |
| C06 | Verified | exact | Dumitru--Prunescu, Lemmas 4--6 and Theorem 3 proof, especially arXiv HTML lines 204--245, give the residue, bound, two lifts, and the `r^2<=4p` selector. |

No numerical citation claim was rounded or altered.  The four small-prime
tables are self-contained exact calculations backed by the frozen mathematical
evidence, not facts outsourced to a citation.

## Publication-record and BibTeX audit

| Key | Manuscript record | Authoritative record | Result |
|---|---|---|---|
| `DumitruPrunescu2026` | Bogdan Dumitru; Mihai Prunescu; 2026; arXiv:2609.05371v1 | arXiv abstract/submission history and v1 HTML: same title, authors, subject, identifier, and 4 September 2026 version date | Verified; no replacement or key change. |
| `Hasse1936` | Helmut Hasse; J. reine angew. Math. 175 (1936), 193--208; DOI 10.1515/crll.1936.175.193 | De Gruyter DOI record and EuDML article record: same author, title, journal, volume, year, and pages | Verified; no replacement or key change. |
| `ZengLiuRatnavelu2026` | Zijian Zeng; Houde Liu; Kuru Ratnavelu; Preprints v1, 18 August 2026; DOI 10.20944/preprints202608.1194.v1 | Version-1 Preprints.org page: same title, authors, version, posting date, and article content | Verified; no replacement or key change. |

Primary URLs inspected:

- https://arxiv.org/abs/2609.05371v1
- https://arxiv.org/html/2609.05371v1
- https://www.degruyterbrill.com/document/doi/10.1515/crll.1936.175.193/html
- https://geodesic.mathdoc.fr/item/JRAM_1936__175_149968/
- https://www.preprints.org/manuscript/202608.1194/v1

The Hasse publisher page restricts article-body access, but the Mathdoc record
replays the EuDML journal metadata and its original BibTeX export; the identity
and historical scope are also cross-checked by the modern primary source's
explicit invocation of Hasse's theorem.  No unsupported detailed quotation
from the restricted text is used.

## Coverage and mechanical consistency

The bibliography is not user-library-only.  `DumitruPrunescu2026` is the
natural non-library primary source for the problem formulas and closest upper
range theorem; `Hasse1936` is the natural historical method source for the
named bound.  Active-library row 8 is used once, in ordinary body flow, for its
narrow and verified boundary-completion comparison.  No second library entry
naturally supports another manuscript claim, so adding one would be padding.
The paper makes no priority claim and needs no decorative survey references.

The bibliography checker found 3 cited keys, 3 BibTeX entries, no missing or
unused entry, and exact agreement with the final `.aux`.  The final `.log` and
`.blg` contain no undefined citation/reference, missing database entry,
duplicate-entry, BibTeX warning, LaTeX error, fatal error, emergency stop,
undefined control sequence, or runaway argument.  Thus bibliography coverage,
claim support, metadata, and compilation consistency all pass.
