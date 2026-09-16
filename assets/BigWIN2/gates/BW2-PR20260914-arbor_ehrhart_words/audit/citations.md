# Verification Report

**Mode:** Search and preserved primary-source verification.
**Document:** manuscript/main.tex and manuscript/references.bib.
**Generated:** 2026-09-14 UTC.
**Job:** primary-20260914-arbor-ehrhart-words-release-df3b6d5a637c; attempt 1; launch 29ed2b81-e679-488f-914f-eff372f40c2d.

| Metric | Count |
|---|---:|
| Frozen substantive claims | 29 |
| Verified at stated scope | 29 |
| Citation keys and retained bibliography records | 6 |
| Selected library records | 1 |
| Natural non-library primary records | 5 |
| Undefined citations, numerical errors, unsupported claims | 0 |

**Overall status: PASS at the explicitly stated source/version scope.**

All three requested skills and the release contract were read in full before the
work they govern. Pass 1 read the complete manuscript and froze claims and direct
citation keys in audit/citation-claim-ledger.json. Pass 2 used that fixed list.
No agents were delegated because the user expressly prohibited them. The user
also required non-interactive verification, so no confirmation was requested.

The accepted mathematics is unchanged. The only source edit removes redundant
begingroup/endgroup wrappers around the final bibliography. This repaired the
active selection parser's rejection without changing claims or layout. All claim
excerpts and line intervals remained identical. New source/PDF bindings follow
a clean canonical rebuild and freeze. Both the initial and final PDFs were
rendered and every page was actually viewed; their rendered images agree byte
for byte (audit/release-render-comparison.json).

## Fixed claim verification

| ID | Located support | Verification |
|---|---|---|
| C01 | accepted proof and manuscript Sections 2-4 | The statement and all quantifiers match claim.json and the accepted argument; the manuscript carries the local identity through arbitrary subtree induction and the box inverse. |
| C02 | Chapoton, Section 1 preceding (1) | The definition has pairwise disjoint nonempty vertex labels covering the ground set, exactly a rooted partition tree. |
| C03 | Chapoton, Lemmas 1.1-1.2 | Cube inclusion and integral vertices are explicit. The root bound is a finite simplex bound, and cube inclusion implies dimension n. |
| C04 | manuscript definition of des, lines 64-69 | Every adjacent pair is either a strict descent or a weak rise. This includes equal letters. |
| C05 | claim.json; accepted proof; manuscript Theorem 1 and its completion | The same finite-content identity and the same n-1-des exponent are proved for every m>=0 and every rooted partition tree. |
| C06 | AXY Theorem 1.5 and Conjecture 5.2; AC Section 4.3 | The source conjecture is exact. AC also explicitly identifies the known case as a root of any size with singleton leaves, resolving the neighboring citation in this interval. |
| C07 | AC Conjecture 4.4 and Remark 7.3 | The displayed binomial sum is already stated as an equivalent formulation. With total content n, complementary filter upper bounds are the ideal lower bounds here. |
| C08 | Chapoton Proposition 2.1 equation (8); manuscript (9)-(12) | The source coefficient convolution is the upper truncation recurrence after renaming the root size. The manuscript supplies lower truncation and compatibility, and handles m=0 directly. |
| C09 | manuscript Lemma 2 and accepted local identity | Coefficient y^(b+j) equals the coefficient of z^(K-j) in (1-z)^(-b-j-1), hence binom(K+b,b+j). The remaining coefficients vanish on both sides. |
| C10 | manuscript Lemma 3 and accepted operator identity | For each monomial x^s, K=mN-s>=mb. Multiplying the local identity by y^(N-b) proves the claim linearly, with all exponents nonnegative. |
| C11 | rooted partition-tree definition | Child subtrees have disjoint vertices and disjoint blocks; adding the parent block covers its descendant set. Cardinalities therefore add. |
| C12 | manuscript upper-enumerator definition and recurrence | Independent child vectors multiply, unrestricted parent coordinates contribute (1-x)^(-b), and truncation imposes precisely the remaining parent bound. At m=0 only zero survives. |
| C13 | manuscript lower-enumerator definition and recurrence | Each coordinate contributes binomial weights from (1+y)^(m+1). Disjoint children multiply and lower truncation enforces exactly the parent inequality. |
| C14 | manuscript Proposition 4 and Lemma 3 | Child sizes sum to N-b; their transformations produce the input of Lemma 3. Empty child products establish the leaf base, proving the result at every vertex. |
| C15 | manuscript root coefficient extraction | Removing y^n and taking the constant term evaluates F_r at 1. Contents above m+1 have zero binomial weight, so extending the content domain adds nothing. |
| C16 | AXY Section 4, printed pp. 10-11; AC Remark 7.3 | Both passages display the same fixed-content binomial series and ordinary non-descent numerator. The manuscript credits prior use, not original discovery. |
| C17 | manuscript Lemma 5 and proof | The complete box/subset correspondence and stars-and-bars count prove this identity at fixed content independently of the cited prior uses. |
| C18 | manuscript lines 260-267 | Strictly decreasing boxes prohibit duplicate letters in one box. Keeping all bars records empty boxes and supplies the stated inverse. |
| C19 | manuscript lines 269-281 | Reserve one bar at each weak rise; exactly n+1 gaps remain available for the other bars. The coefficient is zero below d(w), and the binomial series gives the denominator. |
| C20 | manuscript completion and boundary paragraph | Admissible content classes partition the allowed words. At m=0, each letter must occur once in the unique strictly decreasing length-n word, so the constant term is one. |
| C21 | AC Conjecture 4.4; manuscript disjoint-subtree argument | Every ideal in the root-maximum arbor is a disjoint union of full subtrees at its maximal vertices. Summing inequalities gives the identification; arbitrary preorders are explicitly excluded. |
| C22 | Athanasiadis v3, immediately before Proposition 4.2 | The modified-ascent definition explicitly sets w_0=1. The result is for composition polytopes. |
| C23 | AC Proposition 4.5 and its preceding definition | The source requires a minimum vertex and places label 1 there. The paragraph refers to that qualified extension, not a general ordinary-descent theorem. |
| C24 | Yan v2 Section 5.3, Corollary 5.4 | R_tau is explicitly Q_tau+Delta_E-1. The auxiliary symbol is outside E and is smallest; its ascent statistic is different. |
| C25 | bounded primary-source inspection and audit/citation-searches.json | None of the inspected passages supplies the present all-arbor transformation. This verifies only the stated bounded comparison, without asserting exhaustive priority or worldwide open status. |
| C26 | AC Section 5 definition and Conjecture 5.3 | The h-polynomial there counts nonzero-coordinate support in the undilated polytope. Its real-rootedness conjecture is separate from the Ehrhart numerator. |
| C27 | dated Zeng author manuscript Proposition 3.1 and Theorem 4.2; AC Conjecture 5.3 | The cited body supports certification, not discovery priority. Fresh enumeration gives [1,17,106,303,427,303,106,17,1]; gamma substitution and Laguerre value -95/1024 certify non-real roots. Version identity with the online PDF is explicitly unverified. |
| C28 | both existing programs; audit/release-computation-replay.json | Read-only replay of both inspected implementations exactly matches their recorded outputs, including 153 arbors, 740 pairs and four larger examples. No computation is substituted for the infinite proof. |
| C29 | AC Section 4.3 after Conjecture 4.4; local test domains | The prior passage reports all preorders through size seven. The paper correctly describes its finite checks as convention/formula checks, not a larger census. |

## Bibliography audit and coverage

| Key | Primary record and inspected source | Necessary use | Action |
|---|---|---|---|
| Chapoton | [Chapoton](https://arxiv.org/html/2503.04247v2); Section 1, definition preceding (1), HTML lines 119-140; Lemmas 1.1-1.2, HTML lines 145-165; Section 2.1, Proposition 2.1, equation (8), HTML lines 293-313 | Rooted partition-tree definition, unit cube inclusion, lattice integrality, and upper height recurrence. The cited recurrence is stated for m>=1; the manuscript proves the m=0 boundary itself. | Retained; no key change or BibTeX replacement. |
| AXY | [AXY](https://arxiv.org/html/2603.11654v1); Theorem 1.5 and family definition in introduction; Section 4, printed pp. 10-11, fixed-content identity; Conjecture 5.2, printed p. 13, HTML lines 372-380 | Exact original all-arbor identity, root-block/singleton-leaf special case and the prior fixed-content generating function. | Retained; no key change or BibTeX replacement. |
| AC | [AC](https://arxiv.org/html/2605.26916v1); Section 4.3, Conjecture 4.4, Proposition 4.5, printed pp. 12-13; local text lines 566-600; Section 5 definition and Conjecture 5.3, printed pp. 15-16; local text lines 750-785; Remark 7.3, printed p. 19; HTML lines 607-620 | Broader preorder identity, known binomial reformulation and word identity, minimum-vertex modified-ascent result, size-seven tests, and the distinct support-real-rootedness conjecture. Arbor ideals reduce to descendant inequalities by disjoint union, as proved in the manuscript. | Retained; no key change or BibTeX replacement. |
| Athanasiadis | [Athanasiadis](https://arxiv.org/html/2510.23903v3); Section 4, definition immediately preceding Proposition 4.2, HTML lines 242-253; Publisher record: author and Cite this article, online publication 6 March 2026 | Composition-polytope modified ascents use w_0=1; the cited result is a special family with a different statistic. | Retained; no key change or BibTeX replacement. |
| Yan | [Yan](https://arxiv.org/html/2608.15682v2); Section 5.3 definitions and Corollary 5.4, HTML lines 482-510 | The polytope is R_tau=Q_tau+Delta_E-1 and words use an auxiliary smallest letter. The result does not assert the present formula for Q_tau. | Retained; no key change or BibTeX replacement. |
| ZengSupport | [ZengSupport](https://api.crossref.org/works/10.2139/ssrn.7385158); Saved Crossref deposited title/author/DOI/abstract and HTTP 200 headers; Author manuscript: witness in Section 2, Proposition 3.1 on p. 2 and Theorem 4.2 on p. 3; TeX lines 47-127 | Certification of an eight-element height-two support-polynomial counterexample. Fresh enumeration of all ideal inequalities and a rational Laguerre value corroborate the nearby comparison. | Retained; no key change or BibTeX replacement. |

The existing six titles, authors, dates and identifiers were checked individually
against the sources recorded in audit/citation-sources.json. The AC indexing page
reverses the authors relative to the actual primary PDF title page; the retained
entry follows the PDF. Chapoton's journal metadata confirms volume/issue/year/DOI;
pagination is corroborated in AXY's original bibliography. No purported official
BibTeX export was fabricated when export access failed. The version-specific
ZengSupport entry intentionally describes the inspected author manuscript, not
an uninspected hosted PDF. It was not overwritten with registry-only metadata.
No retained citation is decorative. The four non-library comparison/origin
papers plus Chapoton supply the natural primary literature for the actual claims.
The elementary binomial convolution and box inverse are proved in full; no
unproved triangulation, shellability, Sturm theorem or computer-algebra package
is invoked by this paper's proof. Its finite tests use standard-library integer
arithmetic, so there is no uncited external certification method dependency.

All 49 active first-sheet library titles/DOIs were screened and the complete row
34 was read. Row 34 is the direct subject match; the selection JSON gives the
reason for selecting one reference. Adding unrelated records would not improve
coverage. The five remaining identities are not library records, even under
alternate BibTeX keys. The active hook-compatible validator checks the exact
citation-bearing sentence, canonical bibliography, UTC date and dynamic registry
binding. It passes. The configured pre_publish_hook itself was never invoked.

## Exact recovery and limits

The exact supplied recovery handoff matches SHA-256
965952e968fa1db58beb4a2ffdd3119e73ddb0bbb907e120983cf907de43b677.
The four-field audit/write-recovery-release-evidence.json is bound to this job.
All four referenced live hashes and both byte counts match. The saved Crossref
JSON and headers were independently parsed: endpoint, HTTP 200, response date,
work status, DOI/title/author/publisher, license, primary URL and abstract agree
with the handoff. This is a fresh examination of a saved publisher-deposited
record, not a claim of a new successful retrieval. The abstract matches the local
TeX; the complete local body and PDF text were inspected, and PDF page 1 was
visually opened to check title, author and date.

The historical capture/copy operation was not observed. Browser opens of Crossref
and SSRN failed; no SSRN-hosted PDF was obtained. Matching metadata/abstract does
not establish hosted/local PDF byte equality. That limitation is explicit both
in the paper and in this audit. The dated author manuscript supports the limited
nearby counterexample-certification claim, independently corroborated in
audit/release-recovery-checks.json. It is not evidence for the separate arbor
theorem. Thus the handoff has sufficient scope for the actual citation and
waives none of the fresh release requirements.

The requested bibliography-revision and crossref-prefixed capture globs were
enumerated and were empty. Both literature handoffs were read. The row34-prefixed
Crossref capture specifically named by the exact handoff was inspected directly;
its valid saved scope was not discarded because live access failed. No
fast-completion handoff was present.

## Dependency and output checks

publication.json lists exactly manuscript/main.tex, manuscript/references.bib,
and manuscript/build/main.bbl. Inspection of TeX source and recorder inputs finds
only those relevant local sources, plus generated aux/out files; the bibliography
database is consumed by BibTeX. All other inputs are installed TeX packages/fonts.
There are no local custom styles, figures, or imported author sources omitted
from the publication dependency list. The generated bbl and extracted/rendered
references have all six entries, and all six keys occur in ordinary body flow.
There are no inert-macro, hidden-conditional, comment, nocite or verbatim-only
citations being counted. The ledger key union is exactly the active body key set.

The bib-reference-audit checker reports six cited keys, six bibliography keys,
six auxiliary bibliography labels, and no missing/unused/unresolved entries.
Final LaTeX and BibTeX logs have no relevant warnings or errors. The six-page PDF
has resolved numbered citations and cross-references, readable symbols and URLs,
and explicit computational/model-assistance disclosure. No formal certification,
journal peer review, external submission or exhaustive priority is claimed.

Only release_gate.py check remains before the ready handoff; the runner owns
post-worker validation and publish. This report is a citation/scope audit, not
an independent replacement of the accepted mathematical referee report.
