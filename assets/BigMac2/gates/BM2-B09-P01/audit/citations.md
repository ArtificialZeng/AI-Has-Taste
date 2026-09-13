# Fresh citation and authored-claim audit

Audit date: 2026-09-07 (Asia/Shanghai)  
Method: `$citation-check-skill`, search-verification mode, with separate
extraction and verification passes  
Release job: `bigMac-00009-p01-release-0c119e668365`

This report is bound to evidence snapshot
`f9c68aabbc292cf2fd8e90b5635b9baef672e7c87ad17d46d177e0d4d622b153`,
manuscript digest
`e492c66ba6b9df7334af2f520131d3a5d6f0676fe4ab45df1ddab17a80709752`,
and PDF digest
`fdcdba76cfab26dd9d05844b0c1a9cc033a655303cd090e0ee0b1a92f8110d84`.

## Pass 1: fixed claim extraction

The following inventory was fixed before source verification. Definitions,
hypotheticals, proof exposition, and the assistance-method description were
not extracted under the skill's exclusion rules. Mathematical assertions and
all contextualized numerical assertions were retained so that the manuscript's
scope could be compared with the accepted mathematical report.

| ID | Extracted claim | Type | Location |
|---|---|---|---|
| C01 | An explicit connected simple cubic graph on 16 vertices has a proper 4-total coloring and no equitable proper 4-total coloring. | existence + statistic | abstract; Theorem 1 |
| C02 | The displayed coloring covers all 40 vertex and edge objects. | statistic | abstract; Sections 2--3 |
| C03 | The equitable-coloring CNF has 3,040 variables and 9,408 clauses. | statistic | abstract; Section 3 |
| C04 | The retained proof has 2,498 RUP additions, 3,459 deletion instructions, no RAT-only additions, and ends with the empty clause. | statistic + existence | abstract; Section 3 |
| C05 | The graph therefore has total chromatic number four and disproves the below-order-20 universal existence assertion. | existence | abstract; Theorem 1 |
| C06 | Adauto, de Figueiredo, Sasaki, and Schneider ask whether every Type-1 cubic graph of order below 20 has an equitable proper 4-total coloring. | attribution | Section 1 |
| C07 | The graph6 record shown in the paper encodes the graph defined by the displayed 24-edge list. | existence + statistic | Sections 1--2 |
| C08 | The displayed edge list is loop-free and repetition-free, is cubic, and contains the displayed 15-edge spanning tree. | existence + statistic | Section 2 |
| C09 | The displayed vertex and edge assignment is a proper total coloring with vertex counts (4,6,2,4), edge counts (6,5,7,6), and total class sizes (10,11,9,10). | statistic + existence | Section 2 |
| C10 | Four colors are necessary at each cubic vertex, so the witness proves `chi''(G)=4`. | existence | Section 2 |
| C11 | There are 40 colored objects, so an equitable four-coloring has class sizes (10,10,10,10). | statistic | Section 3 |
| C12 | The symmetry units remove no proper four-total coloring up to a global palette permutation. | existence | Section 3 |
| C13 | The threshold recurrence and final units impose exactly ten objects of each color. | existence + statistic | Section 3 |
| C14 | The expanded formula is satisfiable exactly when the graph has an equitable proper 4-total coloring. | existence | Lemma 2 |
| C15 | RUP additions are entailed by the active formula; the checked empty-clause derivation proves the CNF unsatisfiable. | existence | Section 3 |
| C16 | Wetzler, Heule, and Hunt provide background on the DRAT clausal proof format and its checking. | attribution | Section 3 |
| C17 | The retained verifier reconstructs and compares the CNF, checks 2,498 additions and 3,459 deletions, and confirms the empty clause. | statistic + existence | Section 4 |
| C18 | Zeng's whiskered-graph paper uses canonical finite graph data, exact per-instance certificates, and a short independent verifier. | attribution | Section 4 |
| C19 | Zeng's cited work is only a reproducibility-method comparison and supplies no total-coloring theorem used here. | attribution/scope | Section 4 |
| C20 | The three bibliography records have the authors, titles, years, venues/descriptions, pagination or identifiers printed in the PDF. | attribution/existence | References |

## Pass 2: verification of the fixed inventory

| IDs | Status | Confidence | Decisive check |
|---|---|---|---|
| C01--C05, C07--C15, C17 | Verified | exact | These statements match the accepted frozen claim and the fresh referee's explicit graph, coloring, CNF, and RUP checks in `audit/math.md`. The manuscript adds no minimum-order or priority conclusion. The research snapshot remained unchanged. |
| C06 | Verified | exact | The supplied primary PDF `2609.05259v1`, SHA-256 `18d8c8381368c740103ac445be4c2150929239677f0f76098fcd7c277da760d6`, has the stated authors/title and asks exactly this existence question as Question 7.1 on pp. 13--14. |
| C16 | Verified | paraphrase | The authors' DRAT-trim page and linked system-description text identify the tool as a SAT proof checker, explain DRAT/RUP/RAT and deletion instructions, and give the exact SAT 2014 metadata. The nearby manuscript language is limited to background on format and checking. |
| C18 | Verified | paraphrase | The official SSRN record and abstract for DOI `10.2139/ssrn.7385138` state an exhaustive canonical enumeration of 6,021 graph isomorphism classes, exact integer certificates/kernel vectors for every class, and a short independent verifier reconstructing matrices from graph6 representatives. |
| C19 | Verified | exact | The cited title and abstract concern a weak-Lefschetz graph-algebra problem, not total coloring. The manuscript expressly limits the comparison and draws no mathematical inference from it. |
| C20 | Verified | exact | The Adauto metadata match the supplied arXiv PDF; the Wetzler metadata match the author page/paper and DOI `10.1007/978-3-319-09284-3_31`; the Zeng metadata match the official SSRN record and the Crossref comparison already documented in `literature/user_bibliography_check.md`. |

No extracted claim had a numerical error, contradiction, misleading omission,
or unverified citation. The accepted mathematical audit, not citation lookup,
is the basis for the theorem.

## Citation-to-claim mapping and primary sources

1. `AdautoEtAl2026` supports only C06. The primary cached PDF was inspected at
   Question 7.1, pp. 13--14. Searches run were author/year/title terms, the full
   title restricted to arXiv, author/year/subject, and `arxiv:2609.05259`.
2. `WetzlerHeuleHunt2014` supports only C16. The author-maintained page
   <https://www.cs.utexas.edu/~marijn/drat-trim/> and the linked paper text were
   inspected. Searches run were author/year/title terms, the full title with
   primary repositories, author/year/venue, and the DOI query.
3. `Zeng2026WhiskeredGraphs` supports only C18--C19. The official SSRN record
   <https://ssrn.com/abstract=7385138> and abstract were inspected, together
   with the Crossref metadata check recorded in
   `literature/user_bibliography_check.md`. Searches run were author/year/title
   terms, the full title restricted to SSRN/DOI, author/year/venue, and the DOI
   query. This is a genuinely relevant paper from the user's Excel list, used
   narrowly for its certificate-first verification pattern.

The arXiv abstract endpoint was not returned by the web cache and the SSRN PDF
delivery endpoint returned HTTP 403 during this bounded audit. These endpoint
limits did not leave either citation unverified: the exact supplied arXiv PDF
was locally available, and the official SSRN record/abstract contains every
fact used in the manuscript. No optional endpoint was pursued further.

## Dependency and rendered-reference audit

`publication.json` lists exactly these sorted authored inputs:

- `manuscript/main.tex`
- `manuscript/references.bib`

`main.tex` has no local `input`, `include`, graphics, custom class, or custom
style dependency. The remaining TeX packages are system packages. BibTeX uses
only `references.bib`. Thus the publication dependency scope is complete.

The three citation keys in `main.aux` are defined exactly once in
`references.bib`; `main.bbl` contains all three entries; and the extracted PDF
shows resolved citations `[1]`, `[2]`, `[3]` and all three bibliography entries.
There are no undefined citations. Each citation is material at its stated
scope; none is misleading or merely count-filling. In particular, the user-list
paper is accompanied by an explicit disclaimer against using it as support for
the total-coloring result.

## Verdict

**Accept.** Citation existence, metadata, nearby support, numerical precision,
authored-claim scope, bibliography resolution, and publication dependencies all
pass. There is no unsupported novelty or minimum-order claim.
