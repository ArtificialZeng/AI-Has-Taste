# Verification Report

**Mode:** Primary-source search verification with local accepted-evidence checks.
**Document:** manuscript/main.tex and manuscript/references.bib; final seven-page build/main.pdf.
**Generated (UTC):** 2026-09-14T11:39:34.022643+00:00
**Release job:** primary-20260914-involution-orbit-basis-release-0d8839b8ec7d
**Overall status:** PASS within the explicitly stated source-access and mathematical-review scope.

| Metric | Count |
|---|---:|
| Fixed substantive claim groups | 40 |
| Verified groups | 40 |
| Distinct body-cited references | 7 |
| Selected library references | 1 |
| Natural non-library references | 6 |
| Numerical errors, unverified claims, misleading attributions | 0 |

The canonical claim ledger was extracted before verification and re-frozen after scope-neutral publication repairs. The second pass checked this fixed list in ID order; the detailed passage map and findings are in `audit/citation-source-verification.json`. This release review checks preservation of accepted mathematics and attribution; it does not replace `audit/math.md` or certify a new theorem. No subagents or other model workers were used because the user explicitly prohibited delegation. No interactive confirmation or runner hook was invoked.

## Bibliography audit

The full ordinary body-flow key set is `DaoNair, Knuth, LMRZ, SymPy, ZengWhiskered, ZhuPositive, ZhuRook`. It equals the ledger key union and the seven bibliography entries. The final auxiliary file resolves all seven keys. Comments, inert macros, conditionals, verbatim and nocite were not used as citation evidence. The active validator parsed the final manuscript successfully.

| Key | Current BibTeX title | Verified primary title | Primary record | Action; key change |
|---|---|---|---|---|
| LMRZ | Involution matrix loci and orbit harmonics | Involution matrix loci and orbit harmonics | [Primary record](https://link.springer.com/article/10.1007/s00209-025-03736-4) | Retained verified entry. No key change. |
| ZhuPositive | Positive combinatorial formulae for involution matrix loci and orbit harmonics | Positive Combinatorial Formulae for Involution Matrix Loci and Orbit Harmonics | [Primary record](https://www.combinatorics.org/ojs/index.php/eljc/article/view/v33i2p54) | Retained verified entry. No key change. |
| ZhuRook | Rook placements and orbit harmonics | Rook placements and orbit harmonics | [Primary record](https://link.springer.com/article/10.1007/s00209-026-04090-9) | Retained verified entry. No key change. |
| DaoNair | On the {Lefschetz} property for quotients by monomial ideals containing squares of variables | On the Lefschetz property for quotients by monomial ideals containing squares of variables | [Primary record](https://arxiv.org/abs/2112.09434) | Retained verified entry. No key change. |
| Knuth | Permutations, matrices, and generalized {Young} tableaux | Permutations, matrices, and generalized Young tableaux | [Primary record](https://msp.org/pjm/1970/34-3/pjm-v34-n3-p09-p.pdf) | Retained verified entry. No key change. |
| SymPy | {SymPy}: symbolic computing in {Python} | SymPy: symbolic computing in Python | [Primary record](https://peerj.com/articles/cs-103.pdf) | Retained verified entry. No key change. |
| ZengWhiskered | The whiskered-graph weak {Lefschetz} conjecture for graphs on eight vertices | The Whiskered-Graph Weak Lefschetz Conjecture for Graphs on Eight Vertices | [Primary record](https://papers.ssrn.com/sol3/Delivery.cfm/7385138.pdf?abstractid=7385138&mirid=1&type=2) | Retained verified entry; added explicit DOI field from primary SSRN record. No key change. |

All titles, authors, years, venues and retained page/article identifiers were verified against the cited primary records. Title-case and BibTeX protection braces do not change identities. The published first-author form Jasper M. Liu is retained; primary v1 uses Moxuan (Jasper) Liu. The SymPy author list is conventionally abbreviated as et al. No bibliography block was replaced or falsely labelled an official export. The only metadata repair was adding the explicit, independently verified DOI field to the existing ZengWhiskered entry. A live Crossref BibTeX export attempt failed; enumeration found no `literature/crossref-*.json` or `.md` captures. This access failure does not invalidate the accessible primary SSRN abstract or its DOI. No unverified field was invented.

## Exact source support and coverage

### LMRZ
**Use:** Closest prior orbit-harmonics bases and characters.
**Claims:** C03, C09. **Locator:** Theorem 3.3 (S3.Thmtheorem3); Theorem 5.21 (S5.Thmtheorem21); Section 2.1; Lemma 5.10.
Theorem 3.3 gives the matching-monomial basis for all involutions; Theorem 5.21 gives fixed-class graded characters. Published author name Jasper M. Liu is used; the v1 spells the first author Moxuan (Jasper) Liu.
**Access scope:** Publisher metadata verified; exact theorem content checked in primary v1, not the inaccessible full version of record.

### ZhuPositive
**Use:** Problem origin, literal candidate and required algebraic/character conventions.
**Claims:** C04, C06, C09, C12, C25, C26, C27, C32. **Locator:** Proposition 2, printed page 4; Proposition 3, printed page 5; Section 2.5, printed page 6; Definition 5, printed page 7; equation (4), printed page 9; Proposition 17, printed page 12; Corollary 24 and proof, printed pages 18-19; Problem 29 and following construction, printed page 21.
The journal problem asks for a general monomial basis; its candidate uses positive horizontal strips, inverse insertion and transposed RSK. The cited propositions support the exact conventions, ideal, dimension count and automatic first-row restriction at d<=a.
**Access scope:** Full journal PDF inspected at all cited passages; fresh text extraction equals the frozen source bytes. No full solution or priority is inferred from the search.

### ZhuRook
**Use:** Primary proof of the ideal presentation and degree cutoff.
**Claims:** C09, C12, C33. **Locator:** Appendix A, generator list before Lemma A.2 (browser lines 158-178); Lemma A.3 (lines 185-191); Proposition A.7 (lines 242-280).
The displayed generators and Proposition A.7 identify the homogeneous ideal, with high-degree matching monomials; Lemma A.3 gives vanishing above (n-a)/2. The paper correctly distinguishes the equivalent all-monomial formulation in the EJC source.
**Access scope:** Relevant publisher appendix and publication 17 July 2026 inspected; subscription main text is not claimed read.

### DaoNair
**Use:** Nontrivial incidence/Lefschetz method and closest-method comparison.
**Claims:** C10, C14. **Locator:** Section 2: characteristic-zero hypotheses and multiplication by sum of variables; Proposition 3.1 (browser lines 150-154); Lemma 3.2 (lines 157-166); Theorem 3.3 (lines 167-195).
The incidence matrix has rank n minus the number of bipartite components in characteristic zero. Its transpose is degree-one multiplication. The WLP criterion is explicitly prior work, not this note's new result.
**Access scope:** Primary arXiv v4 statements and author-submitted journal/DOI fields checked; the exact graph specialization is also proved in the manuscript.

### Knuth
**Use:** Primary source for the RSK insertion method.
**Claims:** C24. **Locator:** Sections 2-3, printed pages 711-715, INSERT/DELETE and Construction A; Introduction to Section 4, printed page 711; publisher author index for full page range.
INSERT chooses the first strictly larger row entry and propagates the displaced entry. Section 3 uses INSERT in the matrix/tableau correspondence. This supports the conventional row insertion cited in the note.
**Access scope:** Only the ordinary correspondence is used; no result about the alternate zero-one dual correspondence is imported.

### SymPy
**Use:** Software actually used for rational-rank checks.
**Claims:** C36. **Locator:** Publisher PDF first page: title, author list, abstract, date and recommended citation; Local installed sympy.__version__; audit/referee_verify.py DomainMatrix/QQ operations.
The primary publisher PDF extraction identifies the software paper and all metadata. The local runtime is 1.14.0 and the replay verifies all reported QQ ranks. The 2017 article is not being cited for a 2026 computation or for the current version number.
**Access scope:** Publisher landing-page access returned 403; primary PDF first-page text was available in search. No inaccessible algorithmic theorem is invoked.

### ZengWhiskered
**Use:** Relevant library comparison for reconstructible exact multiplication-matrix certificates.
**Claims:** C38. **Locator:** Primary SSRN abstract, final two sentences; keywords Monomial Algebra and Exact Combinatorial Verification.
The abstract describes exact integer kernel vectors for a multiplication map and a short verifier reconstructing its matrices from graph6 representatives. This directly supports the manuscript's limited methodological comparison.
**Access scope:** Direct full-paper access failed; no theorem, proof or certificate from that work is used or certified here. Registry metadata alone was not accepted as verification.

The bibliography covers the problem origin, nearest earlier bases and characters, primary ideal presentation, incidence/Lefschetz method, insertion correspondence, and exact-rank software. Each retained source has a direct nearby use. The row-42 library comparison concerns the same graph-monomial multiplication-map and certificate setting; no theorem about whiskered graphs is used. Its one-item selection is a minimum coverage choice, not a cap on the six other natural references. The rank/nullity step for standard monomials is proved directly, so adding a decorative textbook citation is unnecessary.

The exact active 49-entry registry and workbook were checked through the dynamic registry binding. All titles/identifiers were screened; the full closer records at rows 8, 14, 25 and 42 were read. Row 42 is selected with an exact three-line, smallest-sentence direct citation context, actual UTC date, attempt 1 and launch UUID `b6d603ca-1ffc-4550-84e8-a6cbbe896850`. `bigwin_user_bibliography.validate_selection` passed; its result is recorded in `audit/user-bibliography-validation.json`. This did not run the configured pre-publication hook.

## Fixed-claim second pass

| Claim | Manuscript lines | Status | Exact verification |
|---|---|---|---|
| C01 | 32-43 | Verified | Abstract is no stronger than accepted claim.json: all admissibility restrictions, degrees and two-transposition family are retained. |
| C02 | 62-65 | Verified | The homogeneous ideal generators in Zhu Section 2.5 have rational coefficients; degree-preserving linear elimination is displayed in the manuscript and accepted proof. |
| C03 | 67-69 | Verified | LMRZ primary Theorems 3.3 and 5.21; published metadata checked separately. |
| C04 | 70-75 | Verified | Zhu Proposition 17 and Problem 29 with its following construction; journal printed pages 12 and 21. |
| C05 | 83-95 | Verified | Manuscript equations (1), (6), (7); accepted quadratic-proof.md shows surjectivity and disjointness. |
| C06 | 97-118 | Verified | All clauses of Theorem 1 match frozen claim.json and accepted math.md; Zhu Problem 29 identifies the candidate rather than proving the new result. |
| C07 | 120-123 | Verified | For 1<=i<j<=n, ij<=n(n-1), so n^2-ij>=n. Off-diagonal domain is explicitly stated. |
| C08 | 125-134 | Verified | Accepted two-transposition corollary; k=2 and degree cutoff give the displayed Hilbert polynomial. |
| C09 | 136-137 | Verified | LMRZ Theorem 5.21, Zhu Proposition 17 and Rook Appendix A supply the attributed prior inputs. |
| C10 | 137-140 | Verified | Dao-Nair Proposition 3.1, Lemma 3.2 and Theorem 3.3, under characteristic-zero hypotheses. |
| C11 | 140-144 | Verified | Bounded assessment checked against frozen research-screen.md, current primary comparisons and fresh narrow queries. It is expressly not a universal absence or priority claim. |
| C12 | 148-155 | Verified | EJC Section 2.5 and Rook Appendix A generator list/Proposition A.7 agree; matching high-degree generators suffice, as explicitly stated. |
| C13 | 162-179 | Verified | Manuscript elimination is homogeneous and rational; a+1>=3 and k+1>=3 give the exact accepted degree-2 quotient. |
| C14 | 181-189 | Verified | Dao-Nair Lemma 3.2 gives the transposed matrix of multiplication; the manuscript uses vertex-by-edge signless incidence and its rows for relations. |
| C15 | 191-196 | Verified | Accepted graph argument and fresh release-verification.json graph_checks: square invertible D_T, determinant absolute value 2; displayed quotient system fixes the matrix orientation. |
| C16 | 198-214 | Verified | Three star families partition the vertices, the final edges give the specified five-cycle, and the displayed binomial count equals |E|. The manuscript proves the odd-cycle kernel argument. |
| C17 | 216-222 | Verified | The invertible T-coordinate block identifies the relation space with those coordinates, so its complement is a basis; accepted proof section 2. |
| C18 | 231-242 | Verified | Uniform odd-walk argument and the three following cases match accepted math.md sections 3 and 5. Finite replay is supplementary only. |
| C19 | 247-258 | Verified | Each of the five walk scores recomputes as displayed; the minimum r+2s=13 at (5,4) is an excluded edge. |
| C20 | 260-271 | Verified | Displayed walk has scores r+6,11,17,14,st+2; disjointness and excluded equality give the three exact lower bounds and r=3 case. |
| C21 | 273-280 | Verified | Accepted exhaustive types give lower bounds 26,23,22,24 and 38. Equality 22 is exactly the excluded edge 25--34. |
| C22 | 282-292 | Verified | The T_5 core has ten vertices and maximum score 22; the three attachment neighbors have products 6,3,2. Connected oddness supplies full incidence rank. |
| C23 | 295-312 | Verified | Homogeneity, uniqueness and the strict score inequality imply the leading terms for every weight refinement; degree-by-degree row reduction gives the exact quotient dimension. |
| C24 | 316-320 | Verified | Knuth INSERT on printed page 712 and Construction A on page 715 explicitly use the stated insertion. |
| C25 | 322-329 | Verified | Zhu Definition 5 and equation (4): only the first lambda_1 steps must remain weakly above the axis; even-row inner partitions and the first-row bound match Proposition 17. |
| C26 | 331-342 | Verified | Zhu Proposition 2 relates symmetry to equal tableaux and trace to odd column lengths; the transpose converts even rows of Q to even columns. |
| C27 | 344-349 | Verified | Zhu Proposition 3 is the increasing-insertion tableau Pieri bijection; the source Problem 29 uses its inverse. |
| C28 | 351-354 | Verified | Accepted tableau classification; final manuscript preserves all cases and the degree-one/zero restrictions. |
| C29 | 356-380 | Verified | Displayed three tableaux and the s2=2/s3=3 failures coincide with accepted uniform proof; literal inverse tableau replay covers n=6..10. |
| C30 | 382-391 | Verified | The manuscript includes its greedy exchange argument; the strip is positive exactly when its second-row length is at least 2. |
| C31 | 393-407 | Verified | Unused-label counts below s3 and s4 are s3-3 and s4-4; necessity, sufficiency and the remaining supports match the accepted proof. |
| C32 | 409-415 | Verified | Zhu Corollary 24 proof shows every positive strip automatically obeys the first-row restriction when d<=a; source pages 18-19. |
| C33 | 418-424 | Verified | Rook Lemma A.3 proves the required cutoff; exactly 3*binomial(n,4) two-edge matchings and binomial(n,2) exclusions give the stated counts. |
| C34 | 428-439 | Verified | Frozen quadratic-verification.json covers every n=6..14. Fresh accepted-code replay covers all eight stated graph values, each margin 1, and all five tableau values. These are finite observations. |
| C35 | 441-449 | Verified | The filtered-evaluation description follows the associated-graded definition and LMRZ Section 2.1; the manuscript rank identity checks independence modulo all lower degrees. |
| C36 | 450-454 | Verified | Pointwise involution relations give the displayed degree-preserving reduction. SymPy identity is primary-source verified; local version 1.14.0 and QQ operations were checked. |
| C37 | 455-473 | Verified | Fresh release-verification.json filtered_checks exactly matches all fifteen displayed row entries, the three degree-zero dimensions, and candidate-augmented ranks; no rounding. |
| C38 | 476-482 | Verified | Primary SSRN abstract final two sentences directly support the comparison. It asserts a reporting/methodological fact, not correctness of an uninspected theorem. |
| C39 | 484-489 | Verified | Frozen original asks for all fixed classes. The stated restrictions and omitted all-degree assertion leave that original problem unresolved by this note. |
| C40 | 491-497 | Verified | Research/referee/writing provenance and inspected exact-arithmetic verifier corroborate the disclosure. Separate model passes are not described as external review, and no formal proof certificate is claimed. |

## Finite values and visual data

The final table was read in the rendered PDF and compared value by value with a fresh execution of the accepted verifier. Its rows are `(6,2): 45,15,45,30`, `(7,3): 105,21,105,84`, and `(8,2): 420,28,210,182`; all degree-zero dimensions are 1. Every candidate-augmented rank equals the stated filtered degree-two rank. All eight graph replay cases retain minimum strict score margin 1, and all five tableau cases pass. Earlier n=6..14 coverage was checked directly in the frozen original data. This replay reuses accepted code and is not a new independent mathematical method. No table entry is rounded or extrapolated. The source-to-tableau display and the two displayed odd walks were also inspected for correct labels. There are no statistical plots, axes, legends, or error bars.

## Dependency, build and scope check

`publication.json` lists exactly `manuscript/main.tex` and `manuscript/references.bib`. The TeX recorder adds only generated aux/bbl/out files and installed system packages. The .bbl was generated from the canonical bibliography; there are no authored imported TeX files, figures, local styles or generated numeric inputs missing from the dependency list. Build/reproduction scripts are accompanying materials, not compiler inputs. `check_bib_keys.py manuscript/main.tex --aux build/main.aux` reports seven keys, no missing or unused entries, and no auxiliary mismatch. The final compiler and bibliography logs contain no undefined citations/references, fatal errors or layout warnings. All seven PDF pages and their resolved references were visually inspected.

No mathematical statement was widened. The note remains restricted to admissible a>=2, k>=2 and degrees 0,1,2, with the complete a=n-4 family for n>=6; the original general construction remains unresolved by the result. The bounded novelty sentence only reports the inspected primary screen, never universal absence or priority. Local audit readiness is not peer review, journal acceptance, public posting or submission.

## Publication repairs

- Added the primary-record DOI field to ZengWhiskered and used a direct `\cite{ZengWhiskered}` in the same supporting sentence.
- Replaced the partition relation symbol with the equivalent words “a partition ... of ...”, because the active citation parser does not support `\vdash`.
- Removed a redundant zero-width tableau strut because the parser does not support `\rule`; the rebuilt tableau was inspected and remains legible.
- Rebuilt from clean products, regenerated the manuscript snapshot, and repeated all affected checks. No key was renamed, no source was added for quota padding, and no frozen mathematical input was edited.
