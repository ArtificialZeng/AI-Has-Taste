# Verification Report

**Mode:** Search verification with primary documents, followed by replay of saved primary passages against the final frozen extraction.
**Document:** manuscript/main.tex and the complete publication dependency set.
**Generated:** 2026-09-13T21:13:24.450260+00:00
**Release job:** `primary-20260914-comb-inverse-release-63c10542e86d`; citation attempt 1; launch `15749e31-318e-4f6b-a910-e79b44450e32`.

| Metric | Count |
| --- | ---: |
| Extracted claims | 25 |
| Verified within the stated scope | 25 |
| Retained references | 5 |
| Ordinary body citation occurrences | 7 |
| Selected library records | 1 |
| Natural non-library primary references | 4 |
| Numerical errors / misleading claims / unsupported retained citations | 0 |

**Overall status: PASS.** This is release verification, not a new mathematical proof or external peer review.

## Citation support and bibliographic accuracy

- **AC** — [Polytopes and posets associated to preorders](https://arxiv.org/html/2605.26916v1). Introduction, equation (2); Section 5 opening definition and Conjecture 5.4; Section 9.6, final unnumbered proposal (HTML lines 846–869). Defines all-ideal polytopes and the raw support statistic; the recursive comb and proposed Laurent-series coefficients agree exactly. General duality is a distinct conjecture. Original HTML author order is Athanasiadis then Chapoton. The official arXiv BibTeX/abstract metadata reverses that order; the existing bibliography retains the primary manuscript order. No export block was substituted.
- **Chapoton** — [On posets and polytopes attached to arbors](https://arxiv.org/html/2503.04247v2). Equation (16), Propositions 2.8 and 2.9 (HTML lines 446–484). The exponents count nonzero coordinates and height. The two propositions recursively compute these coefficients from the root and subtrees. Retained the specifically inspected arXiv v2 citation. The publisher also confirms a journal version in Mathematica Scandinavica 131(3), 2025, DOI 10.7146/math.scand.a-159563. No assertion that the work remains unpublished is made.
- **Wang** — [Counting Lattice Points in Minkowski Sums of Cross Polytopes](https://arxiv.org/html/2608.16037v1). Title/authors and Theorem 1.3 with following paragraph (HTML lines 33–36 and 97–104). The theorem is support-enumerator duality for every bipartite graph. Its immediately following paragraph explicitly applies it to preorder Conjecture 5.4. All five authors, title, 2026 and v1 agree with the original record. This theorem is contextual, not invoked in the comb proof.
- **BF** — [Basic analytic combinatorics of directed lattice paths](https://lipn.fr/~banderier/Papers/tcs_banderier_flajolet_2002.pdf). Title page and printed page 52 (PDF page 16), Example 3, equation (24) and following Lagrange-inversion formula. Displays the rooted-tree equation and its inversion. Its degree set is finite and its code is preorder. The present proof supplies postorder reconstruction and coefficientwise finiteness for its own unbounded degree set. Title, both authors, journal, volume, page range and year are directly confirmed. No finite-step analytic theorem is imported.
- **ZengChecks** — [Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes](https://www.preprints.org/manuscript/202608.1658/v1). Section 4, Proposition 1 certificate proof (HTML lines 187–195), and Section 6 (lines 207–218). DOI: publisher Computational Mathematics subject listing, record at lines 298–323. Integer adjacency predicates feed separate bitset and list implementations that reconstruct the same graph. Section 6 describes independent reconstruction and integer/rational decisions. This supports the expressly limited comparison of verification practice. Primary title, four authors, posting date and version checked. The publisher subject listing independently supplies the DOI and its DOI link opens this full text. Added only that verified DOI field; retained the existing bibliographic entry and key. No geometric endpoint is cited as a comb result.

The detailed title/author/year/version audit and per-key action list are in `audit/bibliography-audit.json`. No key changed and no official BibTeX export block was fabricated or substituted. The ZengChecks entry received one independently verified DOI field. The publisher listing (record headed “Exact Finite Certificates,” posted 24 August 2026) displays the DOI and links to the verified full text. Direct Crossref/DOI access failures alone were not used to deny this primary evidence. The project contains no `literature/crossref-*.json` or `.md` capture. Exporter limitations are recorded separately from citation correctness; retained citation identities and nearby claims have primary support.

The arXiv AC export orders Chapoton first, while the actual primary manuscript title page orders Athanasiadis first. The bibliography follows the actual cited document. Chapoton's arXiv v2 is deliberately retained as the version at which the proposition locators were checked; a journal version was also verified on its publisher's page. These are explicit version choices, without assertions that the works are unpublished or externally certified.

## Complete claim traceability

| ID | Type | Verification basis |
| --- | --- | --- |
| C01 | Attribution | Defines all-ideal polytopes and the raw support statistic; the recursive comb and proposed Laurent-series coefficients agree exactly. General duality is a distinct conjecture. |
| C02 | Attribution | Defines all-ideal polytopes and the raw support statistic; the recursive comb and proposed Laurent-series coefficients agree exactly. General duality is a distinct conjecture. |
| C03 | Attribution | The exponents count nonzero coordinates and height. The two propositions recursively compute these coefficients from the root and subtrees. |
| C04 | Attribution | The theorem is support-enumerator duality for every bipartite graph. Its immediately following paragraph explicitly applies it to preorder Conjecture 5.4. Defines all-ideal polytopes and the raw support statistic; the recursive comb and proposed Laurent-series coefficients agree exactly. General duality is a distinct conjecture. |
| C05 | Attribution | Displays the rooted-tree equation and its inversion. Its degree set is finite and its code is preorder. The present proof supplies postorder reconstruction and coefficientwise finiteness for its own unbounded degree set. |
| C06 | Temporal | The recorded title/author/year/identifier searches and inspected primary passages locate no equivalent full comb inverse resolution. Liu–Tang 2605.08968 concerns singleton-root stars and four other invariant series, as its locally inspected introduction states. This is only a report of bounded searches through the manuscript date in Asia/Shanghai; no global priority certification. |
| C07 | Existence | The final Theorem 1 retains the accepted all-n Q(t)[[x]] statement and both compositions. Sections 2–3 reproduce the accepted proof without a new hypothesis. |
| C08 | Existence | Induction in the accepted proof gives two vertices per recursion and exactly the displayed spine and leaf covers. |
| C09 | Existence | Every nonempty ideal is a spine prefix plus any subset of its pendant leaves. Maximizing its inequality over that subset gives the positive-part prefix costs in both directions. |
| C10 | Existence | At cost zero, (0,0),(0,1) contribute 1+t. At positive c there are two support-one pairs and c support-two pairs; product weights preserve support. |
| C11 | Existence | Summing the constant, geometric and differentiated-geometric local weights gives the displayed rational W; algebra matches the accepted proof. |
| C12 | Existence | The stack has i minus the previous total cost completed trees before c_i. The prefix bound is exactly stack legality. Postorder processing reconstructs each component uniquely. |
| C13 | Existence | Root decomposition and all nonempty ordered forest sequences yield the two series equations. The uniquely first postorder leaf gives exactly qz; n=0 and coefficientwise finiteness are stated. |
| C14 | Existence | Substituting U=qF/(t+qF) in W gives q(1+F)(1+qF). Finite-diagonal summation of the original R gives its rational denominator. Both linear terms are one, so the right inverse is also the left inverse. |
| C15 | Existence | Setting x=tz in the accepted elimination yields the cubic in Z[t][[z]]; coefficient recursion fixes its constant-one solution. |
| C16 | Existence | The displayed h_1,h_2 agree with fresh exact coefficient data. The polynomial cubic specializes to H=1/(1+z) at t=-1 and H=1/(1-z) at t=0; the Laurent F is not specialized at zero. |
| C17 | Attribution | Integer adjacency predicates feed separate bitset and list implementations that reconstruct the same graph. Section 6 describes independent reconstruction and integer/rational decisions. This supports the expressly limited comparison of verification practice. |
| C18 | Statistic | Fresh execution of the supplementary mathematical functions reproduces exactly n=0,...,5; 198627 ambient lattice vectors. Checked against the final table and manuscript JSON; no tolerance or rounding. |
| C19 | Statistic | Fresh execution of the supplementary mathematical functions reproduces exactly n=0,...,8; 6917 forests. Checked against the final table and manuscript JSON; no tolerance or rounding. |
| C20 | Statistic | Fresh execution of the supplementary mathematical functions reproduces exactly n=0,...,8 canonical-leaf normalization. Checked against the final table and manuscript JSON; no tolerance or rounding. |
| C21 | Statistic | Fresh execution of the supplementary mathematical functions reproduces exactly c=0,...,25. Checked against the final table and manuscript JSON; no tolerance or rounding. |
| C22 | Statistic | Fresh execution of the supplementary mathematical functions reproduces exactly both compositions through degree 13 over integer Laurent polynomials. Checked against the final table and manuscript JSON; no tolerance or rounding. |
| C23 | Statistic | Fresh execution of the supplementary mathematical functions reproduces exactly 17577 ambient cost words for n=0,...,8; direct lattice enumeration only to n=5. Checked against the final table and manuscript JSON; no tolerance or rounding. |
| C24 | Existence | All non-main function ASTs match the separately written referee checker. Standard-library imports and wrapper were inspected; fresh execution reproduces the JSON-normalized output without rewriting any source output. The adaptation is not counted as another independent implementation. |
| C25 | Existence | The abstract accurately condenses C07 and C09–C14; it adds no claim beyond the accepted proof. |

## Coverage, relevance, and limits

The five retained references have separate natural uses: original problem and definitions, nearest general support/height recursion, relevant existing duality theorem, classical tree equation/inversion context, and exact finite verification practice. The proof supplies its own forest bijection and formal calculations. It imports neither Banderier–Flajolet's finite-step analytic conclusions nor the library paper's geometric endpoints. No extra bibliography item is required solely to achieve a numerical quota.

The active registry has 49 records on its first sheet. All titles were screened and relevant leads were inspected. Row 9 naturally supports the existing separate-implementation paragraph and is selected with a dynamic registry binding. Row 34 is more directly about preorder support polynomials but concerns a separate real-rootedness counterexample, for which no usable primary text was retrieved here; its registry abstract is not treated as verified evidence. Other tree and exact-enumeration library leads provide no closer verified support for an actual manuscript claim. One selection is therefore justified without inserting a second decorative citation. The current manuscript contains four natural non-library primary references in ordinary body flow.

All applicable academic search templates (author/year/title, full title with scholarly domains, author/year/venue, and supplied DOI or arXiv identifier) were run and saved in `audit/citation-web-*.json`. Primary passages, not secondary snippets, support the retained citations. The finite lookup and source comparisons do not exclude unindexed or older equivalent work. The manuscript preserves this bounded novelty language. The related Liu–Tang four-generating-series paper was checked from its local primary introduction: its family is a singleton-root star, and its invariants are zeta, M-triangle, Ehrhart and volume series. No assertion about that paper is introduced into the manuscript.

The full accepted all-degree claim remains intact. Counts 198,627, 6,917 and 17,577 and every displayed range were checked against fresh exact executions and the rendered table. Formal-series checks through degree 13 are distinguished from direct lattice enumeration only through n=5. The source, checkpoint, claim and all mathematical snapshot files are unchanged.

## Two-pass protocol, dependency scope, and repairs

The initial 25-claim extraction preceded source verification. After citation/typographic repairs, the same claims were frozen with final literal excerpts and corrected locators, then the saved exact primary passages were replayed. The union of ledger citation keys equals all five ordinary body-flow keys. There are no citations supplied only by comments, nocite, inert macro definitions or hidden conditionals. Every retained citation is now an unadorned direct cite with its section locator in visible prose, so the conservative hook parser also recognizes it.

The hook-compatible selection validator passed with the exact runner job/attempt/launch data and the actual UTC date 2026-09-13. Its scope is structural validation, not claim truth. The runner-owned pre_publish_hook was not invoked. The user expressly prohibited agents and interactive confirmation, so all per-reference verification was performed sequentially in this fresh release context.

Publication dependencies are exactly the sorted five source_files in publication.json: main.tex, references.bib, the supplementary checker, its JSON and README. The TeX recorder uses only main.tex, generated auxiliary/bibliography files and system packages/configuration; BibTeX reads the canonical references.bib. No authored dependency is omitted. Generated and rendered references resolve to all five entries; the key checker reports no missing, duplicate, unused or aux-only key.

Only manuscript/main.tex and manuscript/references.bib changed: a verified DOI was added, optional citation notes were moved into visible prose, unsupported bold-vector/indicator font commands were replaced by ordinary vector-letter/upright-indicator notation, the coverage table uses a bold header without special rule macros, and the terminal bibliography is printed directly without a group wrapper. These scope-preserving adjustments avoid unsupported commands in the conservative citation parser and preserve every mathematical statement and table value. The complete clean build and all-page visual checks were repeated afterward.
