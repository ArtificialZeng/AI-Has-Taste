# Citation and claim audit

Audit date: 2026-09-06.  Mode: search verification supplemented by the frozen
accepted computation for claims that are original to this manuscript.  The
audit used the two-pass procedure required by `citation-check-skill`: the claim
list below was frozen before any claim was classified.  Because the release job
explicitly prohibited agents and background workers, all seven reference checks
were performed serially in this release context.

## Pass 1: extracted claims

| ID | Claim | Type | Location |
|---|---|---|---|
| C01 | Gonzalez D'Leon and Wachs introduced the multiweighted-bond symmetric function `Psi_G` as a chromatic-polynomial analogue. | attribution/existence | abstract; lines 32--34, 53--57 |
| C02 | Their Conjecture 7.3 asserts Schur-log-concavity for every graph and degree. | attribution | lines 62--63 |
| C03 | They report exhaustive verification for connected graphs on at most seven vertices. | statistic/attribution | lines 34--35, 100 |
| C04 | The manuscript proves Schur positivity for every connected eight-vertex graph and every `d >= 1`. | existence | lines 35--46, 67--76 |
| C05 | There are 11,117 tested eight-vertex isomorphism classes. | statistic | lines 42, 189 |
| C06 | There are 294 tested Schur coordinates per graph in degrees 1 through 7. | statistic | lines 43, 209--218 |
| C07 | Exactly 3,268,398 coefficients were tested; all were positive and the global minimum was 1. | statistic | lines 44--45, 218--219 |
| C08 | For `d >= 8` the relevant differences vanish. | existence | lines 46, 75, 224--226 |
| C09 | The source proves alternating elementary positivity for chordal graphs, which does not by itself imply the quadratic Schur-positive assertion. | attribution/comparative | lines 78--82 |
| C10 | The chordal/nonchordal strata have respectively 1,614/9,503 classes, 474,516/2,793,882 coordinates, and the displayed per-degree minima. | statistic | Table 1, lines 86--98 |
| C11 | The closest identified prior result is the source computation through seven vertices. | ranking/attribution | lines 100--103 |
| C12 | A bounded search through 2026-09-06 located no separate primary paper settling the eight-vertex layer. | temporal/existence | lines 101--104 |
| C13 | Zeng's 2026 preprint uses selected chromatic-symmetric-function coefficients and an exact cut-partition implementation for tree reconstruction, but does not address this invariant or Schur-log-concavity. | attribution | lines 104--108 |
| C14 | Source formula (7.1)/Theorem 7.2 give the displayed bond-partition formula for each homogeneous piece. | attribution | lines 112--123 |
| C15 | Source Theorem 5.7, formula (5.3), gives the displayed recurrence for the Mobius symmetric function. | attribution | lines 133--149 |
| C16 | Macdonald Chapter I supplies the horizontal-strip Pieri conversion used for `h_mu` to Schur coefficients. | attribution | lines 152--161 |
| C17 | Direct calculation gives the displayed `P_3` values, while the two Schur coefficients are interchanged in source Example 7.4. | comparative/attribution | lines 163--173 |
| C18 | The Read--Wilson graph atlas, exposed in NetworkX, provides every seven-vertex isomorphism class; the seven-vertex slice has 1,044 representatives. | statistic/attribution | lines 175--181 |
| C19 | The extension loop has 127 neighborhoods, retains 119,980 connected labeled candidates, and deduplicates to 11,117 classes. | statistic | lines 180--189 |
| C20 | The exact NetworkX isomorphism routine used is based on the VF2 algorithm of Cordella et al. | attribution | lines 184--189 |
| C21 | The record contains one graph6 representative per line and replay regenerated all records byte-for-byte under Python 3.10.12 and NetworkX 3.4.2. | statistic/existence | lines 228--237 |
| C22 | The documented complete run took about 136 seconds. | statistic | lines 238--239 |
| C23 | Python, NetworkX, and Codex were used in the roles stated, but model output was not treated as mathematical evidence. | attribution/existence | lines 243--250 |

## Pass 2: verification results

| ID | Status | Confidence | Verification |
|---|---|---|---|
| C01 | Verified | paraphrase | arXiv:2608.08692v1, abstract and Section 7.1, identifies the new symmetric graph invariant as an analogue of the chromatic polynomial. |
| C02 | Verified | exact | arXiv:2608.08692v1, Conjecture 7.3 states that `Psi_G` is Schur-log-concave for any graph. |
| C03 | Verified | exact | Immediately before Conjecture 7.3, the source says the conjecture was computationally checked for every connected graph with at most seven vertices. |
| C04 | Verified | exact | This is the manuscript's accepted theorem, bound to mathematical snapshot `c5f1e62a...`; `audit/math.md` independently replayed and accepted its full scope. |
| C05 | Verified | exact | The frozen record has 11,117 lines/unique graph6 strings, independently re-parsed in `audit/math.md`. |
| C06 | Verified | exact | The exact partition-number sum is 294 and the accepted replay checks all seven degrees for all records. |
| C07 | Verified | exact | The accepted replay reports 3,268,398 coordinates, global minimum 1, and the same per-stratum totals. |
| C08 | Verified | exact | Source Section 5.2 makes `M_H` homogeneous of degree `|V(H)|-k`; the displayed bond-partition formula therefore limits an eight-vertex connected graph to degrees 0 through 7, as also audited mathematically. |
| C09 | Verified | paraphrase | Source Theorem 7.2 proves alternating elementary positivity for chordal graphs.  Its statement is linear in each homogeneous component and contains no quadratic Schur-log-concavity conclusion. |
| C10 | Verified | exact | Every displayed count and minimum agrees with the frozen exact summary and the referee's independent full-record parse. |
| C11 | Verified | interpretation | The exact nearest statement found is the source's own verification through seven vertices.  This is only a bounded closest-result comparison, not a priority theorem. |
| C12 | Verified | interpretation | Searches for the exact title/conjecture, `Psi_G` Schur-log-concavity, weighted-bond eight-vertex results, and the announced follow-up found the source and unrelated Schur-log-concavity papers, but no separate paper resolving this layer.  The manuscript correctly dates and limits the assertion. |
| C13 | Verified | paraphrase | arXiv:2608.18179 metadata/abstract and the supervisor capture support selected basis coefficients, tree reconstruction, a canonical partition model, and exact cut partitions.  The abstract is about the classical chromatic symmetric function of trees and gives no weighted-bond or Schur-log-concavity result. |
| C14 | Verified | paraphrase | Source equation (7.1) defines `Psi_G` as the sum over bond partitions; the proof of Theorem 7.2 explicitly groups partitions with `|pi|=n-d`, yielding the manuscript's formula.  The wording is compressed but mathematically faithful. |
| C15 | Verified | exact | Source Theorem 5.7, equation (5.3), is exactly the negative sum over nonmaximal bond partitions with factor `h_{|pi|-1}` and blockwise Mobius functions. |
| C16 | Verified | paraphrase | Macdonald, Chapter I, equation (5.16), is Pieri's formula: multiplying by `h_r` sums over partitions obtained by a horizontal `r`-strip.  Successive use gives the stated integer conversion. |
| C17 | Verified | exact | Source equation (7.2) gives the displayed `Psi_{P_3}`.  Its Example 7.4 prints `3s_(1,1)+2s_2`; the manuscript's independent definition-level regression yields `3s_2+2s_(1,1)`, exactly the reported swap. |
| C18 | Verified | exact | OUP verifies the Read--Wilson atlas metadata; official NetworkX `graph_atlas_g` documentation states that it returns all graphs with up to seven nodes.  The current atlas contains 1,253 graphs total and the exact seven-node slice has 1,044, as replayed locally. |
| C19 | Verified | exact | `2^7-1=127`; the frozen summary and referee replay independently reproduce 119,980 connected extensions and 11,117 retained classes. |
| C20 | Verified | paraphrase | Cordella et al. explicitly describe the VF2 exact graph/subgraph isomorphism algorithm; NetworkX's isomorphism documentation cites that paper for its VF2 implementation. |
| C21 | Verified | exact | The referee's fresh complete replay regenerated the 11,117-line record byte-for-byte under the stated versions and matched SHA-256 `08142d76...`. |
| C22 | Verified | exact | The manuscript says “about 136 seconds”; the frozen research replay records approximately 136 seconds, while the independent referee replay records 132.316 seconds.  The approximate statement is within the documented runs and does not claim an exact benchmark. |
| C23 | Verified | exact | This is a process disclosure consistent with the frozen project/job artifacts and the accepted referee report; it is not used as proof. |

No Numerical Error, Hallucination, Misleading, Citation Not Found, or
Unverified classification remains.  Overall result: PASS.

## Citation-by-citation audit and coverage

| Key | Current / official title | Primary or official source | Nearby claim supported | Action |
|---|---|---|---|---|
| `gonzalez-wachs2026` | *Weighted bond posets and a new chromatic symmetric function* | https://arxiv.org/abs/2608.08692v1 and full HTML text | Definition of `Psi_G`, equations (5.3), (7.1), Theorem 7.2, Conjecture 7.3, seven-vertex verification, and Example 7.4 | Metadata and scope verified; retain. |
| `huh2012` | *Milnor numbers of projective hypersurfaces and the chromatic polynomial of graphs* | https://doi.org/10.1090/S0894-0347-2012-00731-0; author manuscript at Princeton | Log-concavity of absolute chromatic-polynomial coefficients | Metadata and claim verified; retain. |
| `macdonald1995` | *Symmetric Functions and Hall Polynomials*, second edition | https://doi.org/10.1093/oso/9780198534891.001.0001; Chapter I (5.16) | Horizontal-strip Pieri rule and resulting basis conversion | Metadata and passage verified; retain. |
| `read-wilson1998` | *An Atlas of Graphs* | https://doi.org/10.1093/oso/9780198532897.001.0001 | Primary atlas underlying the complete up-to-seven graph list | Metadata and need verified; retain. |
| `hagberg-schult-swart2008` | *Exploring network structure, dynamics, and function using NetworkX* | https://networkx.org/documentation/stable/release/citing.html and author-deposited paper | Identifies/cites the NetworkX package used to expose the atlas and run graph algorithms | Metadata verified; retain. |
| `cordella-et-al2004` | *A (sub)graph isomorphism algorithm for matching large graphs* | https://doi.org/10.1109/TPAMI.2004.75 | VF2 algorithm underlying the exact isomorphism routine | Metadata and passage verified; retain. |
| `zeng2026` | *Multiplicity-Isolated Cores and Chromatic Symmetric Reconstruction of Trees* | https://arxiv.org/abs/2608.18179 and `literature/arxiv-row17-2026-09-06.json` | Narrow related-work comparison using selected coefficients and exact cut partitions, with explicit scope disclaimer | Metadata and scope verified; retain. |

All seven bibliography entries are used and necessary for an actual nearby
claim; there are no decorative references and no uncited entries.  The
bibliography is not Excel-only: the single required user-library item is a
narrow comparison, while the source paper and the primary sources for scalar
log-concavity, Pieri conversion, graph-atlas enumeration, NetworkX, and VF2 are
all present.  No reference key or BibTeX field required correction.

The selected user-library item `zeng2026` has an ordinary body-flow direct
`\cite{zeng2026}` at manuscript line 104.  It uses the canonical
`manuscript/references.bib`; no alternate bibliography is present.

No `literature/crossref-*.json` or `literature/crossref-*.md` capture existed at
audit time.  No conclusion here rests on a failed WSL request; all retained
works were verified through the listed primary/official records.  Search date:
2026-09-06.
