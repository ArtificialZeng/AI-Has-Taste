# Citation and bibliography release audit

## Scope and method

Search-mode verification was performed on 2026-09-07 using the required
two-pass procedure. Pass 1 is frozen in `audit/citation-claim-ledger.md` and
contains nine claim/citation pairs; pass 2 below verifies exactly those IDs
without re-extraction. The audit method was `citation-check-skill-v2 +
primary-source-manual`. Subagents were not used because this release job
explicitly forbids agents and parallel workers.

Before verification, I enumerated `literature/bibliography-revision-*.md` and
`literature/crossref-*.json`/`*.md`; none were present. Live primary publisher,
repository, and author-hosted records were therefore checked alongside the
local primary PDF. The canonical bibliography is
`manuscript/references.bib`; all eight entries are cited in ordinary body flow.

## Pass 2: fixed-claim verification

| ID | Status | Confidence | Exact source passage/location and conclusion |
|---|---|---|---|
| C01 | Verified | exact | Grunbaum, *Projection Constants*, Trans. AMS 95 (1960), pp. 451--465, title page and opening definition. The dated primary paper directly supports the conservative “go back at least” statement. Primary scan: `https://faculty.washington.edu/moishe/branko/BG18.ProjectionConstants.pdf`. |
| C02 | Verified | exact | Kumar et al., PDF p. 2, equations (1.2)--(1.3), state monotonicity and `sup_{n>=r} lambda(r,n)=lambda(r)`. Foucart--Skrzypek, PDF p. 1, equation (2) and the displayed definition immediately below, gives `lambda_K(m)=sup_{N>=m} lambda_K(m,N)`; Proposition 2(4a), PDF pp. 4--5, gives monotonicity. Primary sources: `https://arxiv.org/abs/2609.03200`, `https://foucart.github.io/publi/MaxProjCst_rev.pdf`. |
| C03 | Verified | paraphrase | Basso (2019), abstract and Theorem 1.4, claims existence of a finite-dimensional polyhedral maximizer, the claimed stabilization route. Basso's corrigendum, abstract and opening discussion, states Lemma 3.1(2) is false, the proof of Theorem 1.4 is incomplete, and the strategy no longer works. Publisher records: `https://www.sciencedirect.com/science/article/pii/S0022123619301752`, `https://www.sciencedirect.com/science/article/pii/S0022123624001794`. |
| C04 | Verified | exact | Kumar et al., PDF pp. 3--4, Theorem 1.3 gives `2^r binom(r+1,2)`; PDF pp. 8--10, Claim 2.5 partitions all `2^r` orthants and applies cloning; the paragraph following Theorem 1.3 says minor improvements may be possible. Full-text inspection found no statement of `2^(r-1) binom(r+1,2)`. |
| C05 | Verified | exact | Zeng--Liu--Ratnavelu, primary Preprints.org v1 record, abstract and Theorem 1, says equality holds when the five unoriented Gram lines form a regular pentagon up to permutation and sign switching; its formulas are permanental correlation-matrix inequalities. `https://www.preprints.org/manuscript/202608.1346`. |
| C06 | Verified | exact | Kumar et al., PDF p. 5, Theorem 2.1 displays both maxima and attributes them to Chalmers--Lewicki, with Foucart--Skrzypek Theorem 1 as comparison. Chalmers--Lewicki, official journal PDF pp. 106--107, Theorem 2.4, gives the absolute-Gram maximum; Foucart--Skrzypek, PDF p. 3, Theorem 1, equations (3)--(4), gives both the Gram and weighted-Seidel eigenvalue maxima. `https://www.impan.pl/shop/publication/transaction/download/product/89813`; `https://foucart.github.io/publi/MaxProjCst_rev.pdf`. |
| C07 | Verified | exact | Kumar et al., PDF pp. 5--8, Claims 2.1--2.4, contain respectively the Perron eigenvector, invariant subspace, quadratic identity, and cloning result used and re-proved in the manuscript. |
| C08 | Verified | exact | Schrijver, *Theory of Linear and Integer Programming*, Corollary 7.1i, p. 94, is the conic Caratheodory theorem: a vector in a cone in dimension `d` uses at most `d` generators. Bibliographic identity and 1986 Wiley edition are verified by the CWI author/institution record `https://ir.cwi.nl/pub/10206` and ISBN 0-471-90854-1. Kumar et al., PDF p. 8, independently quotes the same locator and statement. |
| C09 | Verified | exact | Kumar et al., PDF p. 3, Theorem 1.3 is the larger universal threshold; p. 4 explicitly leaves polynomial growth as Problem 1.4. The manuscript accurately limits its contribution and makes no priority claim. |

Summary: 9 verified; 0 numerical errors; 0 misleading claims; 0
hallucinations; 0 unverified claims. There are no quotations or cited visual
data. The theorem and proof internal to the manuscript remain governed by the
accepted mathematical audit rather than citation status.

## Bibliographic-record audit

All eight cited keys were checked against primary or authoritative records.
Author, title, year, venue/version, pagination where applicable, DOI/arXiv/ISBN,
and the nearby support all agree. No BibTeX replacement or key change is
needed.

| Key | Authoritative record | Nearby role | Action |
|---|---|---|---|
| `Grunbaum1960` | primary paper scan; Trans. AMS 95 (1960), 451--465 | historical origin | retain |
| `ChalmersLewicki2010` | IMPAN journal issue and official PDF; DOI 10.4064/sm200-2-1 | maximizing characterization | retain |
| `FoucartSkrzypek2017` | Elsevier article and author-hosted accepted PDF; DOI 10.1016/j.jmaa.2016.09.066 | supremum, monotonicity, two maxima | retain |
| `Basso2019` | Elsevier article; DOI 10.1016/j.jfa.2019.05.011 | exact historical stabilization claim | retain |
| `Basso2024` | Elsevier free corrigendum; DOI 10.1016/j.jfa.2024.110491 | correction of that claim | retain |
| `Schrijver1986` | CWI institutional record; ISBN 0-471-90854-1 | conic Caratheodory locator | retain |
| `KumarEtAl2026` | arXiv:2609.03200v1 and local SHA-256-bound PDF | definitions, closest theorem, methods | retain |
| `ZengLiuRatnavelu2026` | primary Preprints.org v1 record; DOI 10.20944/preprints202608.1346.v1 | narrowly delimited sign-switching comparison | retain |

The bibliography has normal primary coverage beyond the user library: problem
origin, closest prior theorem, the exact optimization formulas, the failed
stabilization claim and corrigendum, and conic Caratheodory are all sourced.
No reference is decorative. The one selected user-library item is bound in
`audit/user-bibliography-selection.json`; it has a direct body-flow
`\cite{ZengLiuRatnavelu2026}`. A second library item would be redundant or
irrelevant and was not added.

## Mechanical consistency

The bibliography checker found 8 cited keys, 8 bibliography entries, no
missing or unused keys, and exact agreement with the final `.aux`. The final
LaTeX/BibTeX logs contain no undefined citations, undefined references,
missing database entries, duplicates, or fatal diagnostics.

Verdict: **accept**.
