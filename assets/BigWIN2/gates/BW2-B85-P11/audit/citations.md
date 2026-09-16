# Citation and bibliography audit

Verdict: **accept**.

This release audit used a two-stage, non-interactive procedure. In stage 1, the citation-bearing claims in `manuscript/main.tex` were frozen in `audit/citation-claim-ledger.json`; its citation-key union is exactly the ordinary body-flow key set. In stage 2, each claim was checked against a directly located passage in a primary record. The user prohibited sub-agents, so the independent second pass was performed sequentially after the ledger was frozen.

## Claim-level verification

| Claims | Key | Direct source and exact support | Result |
|---|---|---|---|
| C01--C02 | `KolountzakisRevesz2006` | The official Wiley DOI record confirms the authors, title, *Journal of the London Mathematical Society* 74(2), 475--496 (2006), and DOI `10.1112/S0024610706023234`. The authors' primary arXiv record, `math/0312218`, states in its abstract that the problem is studied on arbitrary locally compact abelian groups and on more general domains. | Supported |
| C03--C06 | `FuLiWangWang2026` | The primary arXiv record `2608.15643v1` confirms title, authors, version, year, and DOI `10.48550/arXiv.2608.15643`. In the primary PDF, Theorem 1.2 specializes at (p/q=5/2) to the manuscript's discrete set and factor (1/2); Section 4.1 gives the corresponding finite nonnegative trigonometric-polynomial formulation; Proposition 4.2 gives the displayed lower bound and explicitly disclaims optimality of that feasible polynomial; Lemma 5.1 gives the upper bound (9/4). | Supported |
| C07--C08 | `ZengLiuRatnavelu2026` | The official Preprints.org Version 1 record for manuscript `202608.1346` confirms authors, title, posting date, and DOI `10.20944/preprints202608.1346.v1`. Its abstract and Sections 4.1--4.2 exhibit the exact sum-of-squares identity and positive-semidefinite Gram matrices described by the nearby manuscript sentence. | Supported |

Primary records checked: `https://doi.org/10.1112/S0024610706023234`, `https://arxiv.org/abs/math/0312218`, `https://arxiv.org/abs/2608.15643`, `https://arxiv.org/pdf/2608.15643`, and `https://www.preprints.org/manuscript/202608.1346`. No quotation is needed in the manuscript; the ledger and the locators above record the narrower support actually used.

## Coverage and bibliography integrity

The bibliography contains exactly the three works cited in ordinary body flow. All three entries resolve in `main.aux`; there are no missing, undefined, duplicate, or unused bibliography keys. The two non-library primary sources naturally cover the general Turan framework, the problem-specific rational reduction, and the closest prior bounds. The one selected user-library paper is a natural methodological comparison, not a substitute for those sources. Adding a second library item would not support an existing nearby claim and would be padding.

The active 49-record first-sheet registry was checked and bound by digest in `audit/user-bibliography-selection.json`. Registry row 23 was then verified against the official primary record. The hook-compatible selection validator passed with the issued citation attempt and launch UUID. A fresh exact-title/value literature search found no additional primary source needed for a claim made by this manuscript; the manuscript deliberately makes no priority or formal open-problem-status assertion.

All publication inputs were inspected for citation dependencies: `manuscript/main.tex`, `manuscript/references.bib`, and `evidence/verify_exact_solution.py`. The verifier contains no bibliographic claims or citation dependencies. No `literature/bibliography-revision-*.md`, `literature/*handoff*.md`, or `literature/crossref-*` files exist in this project, so no supervisor lead or saved Crossref response was available or silently omitted.

