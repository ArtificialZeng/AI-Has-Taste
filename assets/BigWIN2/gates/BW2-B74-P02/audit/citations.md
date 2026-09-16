# Citation and bibliography audit

## Scope and method

This is the verification-only second pass for release job
win-00074-p02-release-7f6dbc4d0b34, citation attempt 5, launch
f11401bc-a968-4e56-966f-4ce52ef1dec7.  The extraction was frozen first in
audit/citation-claim-ledger.json.  It contains six substantive claim/citation
pairs and exactly the five ordinary body-flow citation keys in
manuscript/main.tex.  The parser-safe canonical sources retained the exact
fast-completion hashes and remained frozen at manuscript digest
6ed9ff1755f012c9785271f256a9d69591c9f0547f82722a78d431062077511a
and PDF digest
d1ec9591288c453846a60edbedbdcb266c67378a1638cfa3ecde69854870e3b2.

The fast-completion handoff predicates all remained exact: the canonical
source, bibliography, PDF, mathematical snapshot, citation set, and four-page
state matched.  I therefore freshly replayed every fixed claim against its
recorded exact source locator and the available local primary evidence.  The
preceding verified attempt had run all applicable academic search templates
on 2026-09-08 UTC (author/year/title words, exact title, author/year/venue, DOI,
and arXiv identifier where applicable); as the handoff requires, no web search
was repeated.  Exact passages, hypotheses, metadata, and nearby manuscript
scope were again checked separately from extraction.  The row-17 citation
context now records the live parser's masked cross-reference excerpt while
retaining the active body citation and literal nearby claim.  The user
expressly prohibited sub-agents, so the bibliography audit was performed
sequentially.

## Coverage decision

The bibliography is claim-driven and is not user-library-only.  The
Biswas--Mandal--Phukan preprint is the primary closest result and problem
source.  Cooper et al. is the primary source introducing the v-number in the
minimum-distance setting.  Herzog--Hibi supplies monomial-ideal background,
and Huneke--Swanson supplies the integral-closure background and the exact
ideal-closure fact invoked in the proof.  The selected active-library item,
Zeng's reconstruction preprint, supports only the narrow methodological
comparison about distinguishing an infinite proof from a bounded exact
implementation.  No retained citation is used as evidence for a stronger
claim than its source states, and no priority or exhaustive-literature claim
is made.

The active 49-entry first-sheet registry was screened.  Row 17 is the only
entry with a natural, independently verifiable nearby use in this manuscript.
Adding another entry would be padding.  The four non-library sources remain in
ordinary body flow and cover the natural origin, closest-result, background,
and proof-method dependencies.

## Claim-to-source verification

| Claim | Key | Exact source location inspected | Result |
|---|---|---|---|
| C01 | CooperEtAl2020 | Primary arXiv 1812.06529, introduction: lines 88--95 of the accessible HTML state that the authors introduce the v-number to study the minimum-distance function and relate minimum socle degree, v-number, and regularity; Elsevier's article record confirms the five authors, title, Advances in Applied Mathematics 112 (2020), article 101940, and DOI 10.1016/j.aam.2019.101940. | Verified, paraphrase |
| C02 | HerzogHibi2011 | Official Springer book record for DOI 10.1007/978-0-85729-106-6: overview identifies a special focus on monomial ideals, and the table of contents begins with the chapter Monomial Ideals, pages 3--22; authors, GTM 260, publisher, and 2011 copyright agree. | Verified, exact topic and metadata |
| C03 | HunekeSwanson2006 | Authors' official Purdue book page describes the work as a graduate textbook and research reference, lists Chapter 1 as What is integral closure of ideals?, and gives the LMS 336 / Cambridge 2006 citation; the author-hosted full book was inspected. | Verified, exact topic and metadata |
| C04 | BiswasMandalPhukan2026 | Supplied primary PDF evidence/external/2609.05044v1.pdf, printed page 6: Theorem 3.2 is for monomial ideals in K[x,y]; Example 3.3 uses (x^2,y^2,z^5,xyz), gives the displayed integral closure, and computes v-values 2 and 3.  The arXiv 2609.05044v1 record confirms title, authors, date, subject, and comparison scope. | Verified, exact |
| C05 | HunekeSwanson2006 | Author-hosted full book, Section 1.3 and Corollary 1.3.1, printed pages 6--7 (PDF pages 19--20): the integral closure of an ideal in a ring is an integrally closed ideal, with closure under addition proved immediately afterward. | Verified, exact |
| C06 | Zeng2026Multiplicity | Primary arXiv 2608.18179v1 abstract states both that the paper proves an infinite class of diameter-six trees and that it gives an exact cut-partition implementation intended for further work, while the unrestricted case remains open.  Title, author, date, DOI, and subject agree with registry row 17. | Verified, paraphrase |

All six fixed claims are verified.  There are no numerical errors, misleading
attributions, hallucinations, citation-not-found results, or unverified
claims.

## Authoritative sources

| Key | Record | Nearby use |
|---|---|---|
| BiswasMandalPhukan2026 | https://arxiv.org/abs/2609.05044 and the supplied v1 PDF | Closest prior result, two-variable theorem, and isolated c=5 example |
| CooperEtAl2020 | https://doi.org/10.1016/j.aam.2019.101940 and https://arxiv.org/abs/1812.06529 | Origin and minimum-distance/socle context of the v-number |
| HerzogHibi2011 | https://link.springer.com/book/10.1007/978-0-85729-106-6 | Monomial-ideal background |
| HunekeSwanson2006 | https://www.math.purdue.edu/~iswanso/book/index.html and https://www.math.purdue.edu/~iswanso/book/SwansonHuneke.pdf | Integral-closure background and Corollary 1.3.1 |
| Zeng2026Multiplicity | https://arxiv.org/abs/2608.18179 | Gate-selected methodological scope comparison |

## BibTeX audit

| Key | Current and official title | Official source | BibTeX replaced | Key changed | Uncertainty |
|---|---|---|---|---|---|
| BiswasMandalPhukan2026 | A Comparison of the v-Number of a Monomial Ideal and Its Integral Closure | arXiv 2609.05044v1 | No; fields agree | No | None |
| CooperEtAl2020 | Generalized Minimum Distance Functions and Algebraic Invariants of Geramita Ideals | Elsevier DOI record and arXiv 1812.06529 | No; fields agree | No | None |
| HerzogHibi2011 | Monomial Ideals | Springer DOI record | No; fields agree | No | None |
| HunekeSwanson2006 | Integral Closure of Ideals, Rings, and Modules | Author/Cambridge book record and full text | No; fields agree | No | None |
| Zeng2026Multiplicity | Multiplicity-Isolated Cores and Chromatic Symmetric Reconstruction of Trees | arXiv 2608.18179v1 | No; final entry agrees with the primary record | No | None |

The final bibliography checker found five cited keys and five BibTeX entries,
with no missing or unused entry and exact agreement with the five main.aux
bibcite keys.  The converged main.log and main.blg contain no undefined
citation/reference, missing database entry, repeated entry, BibTeX warning,
LaTeX error, fatal error, emergency stop, undefined control sequence, or
runaway argument.  No bibliography or citation-key change was required.
