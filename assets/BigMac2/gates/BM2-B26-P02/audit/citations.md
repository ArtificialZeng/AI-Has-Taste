# Fresh citation and dependency audit

**Mode:** Search verification with the advisory `citation-check-skill` and
primary-source manual checks  
**Document:** `manuscript/main.tex`, `manuscript/references.bib`, and the
rendered `manuscript/main.pdf`  
**Search date:** 2026-09-09

## Pass 1: fixed claim extraction

The manuscript was read in full before verification.  The following
attribution, existence, comparison, and numerical claims form the fixed
citation-audit input.  Definitions, proof steps, and explicitly delimited
method descriptions are outside the citation skill's extraction classes; the
accepted mathematical audit remains controlling for their correctness.

| ID | Extracted claim | Type | Location |
|---|---|---|---|
| C01 | Cover times are classical objects in random-walk theory. | Existence/attribution | p. 1, Statement and context |
| C02 | Si studies exact cover-time response to adding a nonedge and states universal fixed-start strict nonequality as Conjecture 6.2. | Attribution | p. 1 |
| C03 | Si's Theorem 6.4 excludes fixed-start equality through order seven and for trees of orders eight and nine. | Attribution | p. 1 |
| C04 | The present theorem is exactly the complementary connected non-tree order-eight fixed-start layer, without a broader priority claim. | Comparative/scope | p. 1 |
| C05 | The two cited Zeng papers use an explicitly finite, exhaustive, exact, independently checked certification style; they are not cited for cover-time claims. | Comparative/attribution | p. 1 |
| C06 | `geng` in nauty/Traces generated one representative for each connected order-eight graph with 8--28 edges. | Existence/attribution | p. 3 |
| C07 | The decisive census contains 11,094 graph representatives, 150,573 nonedges, and 1,204,584 marked instances. | Statistics | abstract, p. 3 |
| C08 | The two methods make 177,504 base cross-checks, solve 150,573 augmented graphs each, encounter zero singular systems, and find zero equality residues in 1,204,584 comparisons each. | Statistics | p. 3, Table 1 |
| C09 | A NetworkX decoder validates the 11,094 records; unrestricted generation gives 11,117 connected classes, split as 23 trees and 11,094 cyclic graphs. | Statistics/existence | p. 4, item 1 |
| C10 | Rooted canonicalization gives 72,374 rooted classes and zero equality residues; exact regression checks 42 order-seven values and four order-eight base/augmentation pairs. | Statistics | p. 4, items 2--3 |
| C11 | The clean reproduction and stated Apple clang, nauty, NetworkX, and Python versions are recorded properties of the computational supplement. | Temporal/existence | p. 4 |
| C12 | The theorem does not settle Si's unrestricted conjecture, and AI output is not used as mathematical evidence. | Scope/existence | pp. 4--5 |

No direct quotation appears.  The exact theorem and algebraic lemmas are
audited in `audit/math.md`; this release audit separately checked that the
authored prose does not strengthen that accepted scope.

## Pass 2: verification

| ID | Status | Source and exact support |
|---|---|---|
| C01 | Verified (paraphrase) | Aleliunas et al. (1979) studies the expected number of random-walk edge traversals needed to visit a graph, and Matthews (1988) studies covering problems for Markov chains.  Author/title/year/pages/DOIs match the bibliography. |
| C02 | Verified (exact) | Si, arXiv:2608.27474v1, abstract and Conjecture 6.2: the paper studies the exact response to inserting a nonedge, and the conjecture quantifies over every connected finite simple graph, genuine nonedge, and start. |
| C03 | Verified (exact) | Si, Theorem 6.4, states no fixed-start or worst-start equality through order seven and no equality among trees of orders eight and nine. |
| C04 | Verified (interpretation) | The excluded domain in Si's Theorem 6.4, the immutable `source.md`, and accepted Theorem 1 leave exactly the connected cyclic order-eight fixed-start layer.  The manuscript explicitly disclaims broader priority. |
| C05 | Verified (paraphrase) | The official Preprints.org abstract for DOI `10.20944/preprints202608.1658.v1` describes exact predicates, exhaustive symmetry-reduced enumeration, and two exact clique computations.  The second record's user-workbook abstract describes an exhaustive order-nine graph census, exact rational congruence, and an independent integer/Sturm verification.  The sentence makes only this methodological comparison. |
| C06 | Verified (paraphrase plus local record) | McKay--Piperno describes nauty and Traces; the current official nauty/Traces site identifies the software family.  `evidence/run-metadata.json` records the exact `geng -cq 8 8:28` command, and the accepted audit independently regenerated the inventory. |
| C07 | Verified (exact) | `evidence/census-modular-result.json`, `evidence/run-metadata.json`, and `evidence/rooted-streams-metadata.json` give exactly 11,094, 150,573, and 1,204,584. |
| C08 | Verified (exact) | `evidence/census-modular-result.json` gives 177,504 cross-method comparisons, 150,573 augmented solves, 1,204,584 comparisons per method, zero singular principal systems, and direct zero counts `[0,0]`. |
| C09 | Verified (exact) | `evidence/graph6-crosscheck.json` gives 11,094 connected codec round trips; `audit/math.md` records the independently regenerated 11,117-class total and 23/11,094 split.  Hagberg--Schult--Swart metadata and primary PDF match the NetworkX citation. |
| C10 | Verified (exact) | `evidence/census-modular-result.json` gives 72,374 rooted isomorphism classes and zero canonical-lookup residues.  `evidence/exact-regression.json` contains three order-seven cases with seven base and seven augmented start values each (42 total); `audit/referee-checks.json` records the four order-eight pairs. |
| C11 | Verified (exact) | `evidence/run-metadata.json` records Apple clang 21.0.0, nauty 2.9.3, Python 3.12.14, and the authoritative Python path; `evidence/graph6-crosscheck.json` records NetworkX 3.6.1.  `evidence/reproduction-result.json` has status `pass`. |
| C12 | Verified (exact scope) | Si labels the unit-conductance equality questions open and states Conjecture 6.2; `claim.json` and `audit/math.md` accept only the order-eight layer.  The assistance disclosure makes no evidentiary claim for AI output. |

There are no numerical mismatches, contradicted attributions, misleading
comparisons, or unsupported novelty claims.

## Bibliographic and rendered-reference checks

All mandatory applicable title/author/venue/identifier searches were run.  The
following primary or authoritative records were consulted:

1. R. Aleliunas et al., Berkeley archive and DOI
   `10.1109/SFCS.1979.34`:
   <https://www2.eecs.berkeley.edu/Pubs/TechRpts/1979/29132.html>.
2. P. Matthews, Project Euclid/Annals record and DOI
   `10.1214/aop/1176991686`:
   <https://projecteuclid.org/euclid.aop/1176991686>.
3. I. M. Si, arXiv:2608.27474v1 full HTML, especially Conjecture 6.2 and
   Theorem 6.4: <https://arxiv.org/html/2608.27474v1>.
4. B. D. McKay and A. Piperno, arXiv:1301.1493 and DOI
   `10.1016/j.jsc.2013.09.003`: <https://arxiv.org/abs/1301.1493>.
5. A. A. Hagberg, D. A. Schult, and P. J. Swart, author-hosted primary PDF:
   <https://aric.hagberg.org/papers/hagberg-2008-exploring.pdf>.
6. Z. Zeng et al., official Preprints.org record:
   <https://www.preprints.org/manuscript/202608.1658>.
7. Z. Zeng, *Exact Verification of the Line-Graph Signature Inequality at
   Order Nine*: metadata basis is the user-designated workbook documented in
   `literature/user_bibliography_check.md`; status is **Accepted from user
   record -- external refresh unavailable** for DOI
   `10.2139/ssrn.7386040`.  The workbook-supplied abstract, not an unavailable
   external page, supports the narrow methodological sentence.

Thus `metadata_basis=user_designated_workbook` applies to the second workbook
record.  The first workbook record was also checked successfully against its
official current page.  This access limitation leaves no unsupported nearby
prose and does not require `accept_with_citation_limitations` under the
user-designated-authority rule.

The extracted PDF contains seven fully resolved bibliography entries.  Every
citation key used by `main.tex` appears in `references.bib` and in the rendered
reference list; the uncited `ReadWilson1998` database entry is not rendered.
There are no undefined citations.

## Publication dependency scope

The sorted authored dependency list is exactly:

1. `manuscript/main.tex`
2. `manuscript/references.bib`

The TeX source has no `\input`, `\include`, local figure, or local style
dependency.  Its sole local bibliography dependency is `references.bib`;
`main.bbl` and the auxiliary files are generated build products, and all other
recorder inputs are system TeX files.  Accordingly, `publication.json`
enumerates the complete authored dependency scope.

**Verdict: accept.**
