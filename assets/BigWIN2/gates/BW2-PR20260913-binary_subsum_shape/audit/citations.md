# Verification Report

**Mode:** primary-source search plus frozen-proof and exact-artifact verification.
**Document:** manuscript/main.tex and its complete publication inputs.
**Job:** primary-20260913-binary-subsum-shape-release-b63927b8723e
**Generated (UTC):** 2026-09-13T00:42:04.160819+00:00

| Metric | Count |
|---|---:|
| Fixed extracted claim groups | 33 |
| Verified within their stated scopes | 33 |
| Citation-bearing claim pairs | 11 |
| Unique retained references | 5 |
| Natural non-library references | 4 |
| Selected active-library records | 1 |
| Numerical errors, unsupported citations, misleading claims | 0 |
| Undefined citations or cross-references | 0 |

**Overall status: PASS for the current result-note release scope.** The original all-index conjecture remains unresolved. Mathematical acceptance belongs to the existing frozen referee audit; this report checks faithful presentation, source support and exact evidence, rather than certifying a new theorem.

## Extraction and independent verification

Pass 1 read the entire manuscript and froze 33 claim groups in `audit/citation-claim-ledger.json` before looking up source support. Repeated abstract statements map to M01-M03 and M21; definitions, reasoning steps and assistance acknowledgments are not separate external claims. Pass 2 worked through that fixed list and inspected the original primary passages and accepted proof artifacts. No new claims were introduced during verification. The user explicitly required a noninteractive single-worker audit, so no confirmation or delegation was used.

All four applicable academic-search templates were run for each reference (20 queries total), followed by direct primary-record access and three problem-specific novelty queries. Raw searches are retained in `audit/search-*.json` and `audit/release-novelty-search.json`. Searches are discovery evidence; secondary indexes were not accepted as source support. The unversioned COZ snippets still carry older wording; the actual v2 remark controls C04. All online checks took place on 2026-09-13 UTC. No supervisor bibliography-revision, handoff or Crossref capture files existed when enumerated before editing.

TeX-only repairs changed citation command variants to direct cites, expanded a coefficient-order alias, made link colors explicit, replaced one fixed-space indentation by ordinary math spacing, and removed a redundant final bibliography group. The supplementary checker had one stale equation-number comment replaced by its correct section locator. These changes preserve every mathematical statement, source key and bibliography entry. The fixed claim texts remained unchanged; their hashes/excerpts and three theorem-part line intervals were rebound and corrected. All affected build and visual checks were completed afresh; the final documentation-only supplement change did not alter the PDF.

## Retained bibliography and coverage

- **BBFM**: *Reciprocals of subsum polynomials*, The Ramanujan Journal 70, article 46 (2026). [Primary record](https://link.springer.com/article/10.1007/s11139-026-01419-0). Journal PDF pp. 18-19, Remark 6 and Proposition 4.1; p. 21, Conjecture 7 and Corollary 4.2; p. 23, Corollary 4.5; p. 24, Remark 8 and Theorem 4.7. Problem origin, normalization, structural dependencies, initial coefficient identities and recurrence.
- **COZ**: *Reciprocals of Partition Polynomials*, arXiv:2605.21718v2, 22 May 2026. [Primary record](https://arxiv.org/html/2605.21718v2). Section 1.2.2, remark on p. 4; live HTML lines 191-197. Closest correction of the small-parameter formulation; v2 preserves the corrected n>5 question.
- **Neidinger**: *Multivariate Polynomial Interpolation in Newton Forms*, SIAM Review 61(2), 361-381 (2019). [Primary record](https://epubs.siam.org/doi/10.1137/17M1124188). Publisher abstract, HTML lines 66-70, specifically lower sets and triangular/corner nodes at line 68; bibliographic information on publisher record. General lower-set Newton interpolation context. The precise integer-simplex special case is independently proved in the manuscript. No uninspected source theorem number is claimed.
- **SymPy**: *SymPy: symbolic computing in Python*, PeerJ Computer Science 3:e103 (2017). [Primary record](https://docs.sympy.org/latest/citing.html). Official Citing SymPy record, lines 326-355; actual use in evidence/research_kernel3.py:11 and separate Fraction checker evidence/research_kernel3_verify.py:10. Software attribution for original symbolic expansion; not a dependency of the standalone release checker.
- **ZengChollet**: *Sharp Self-Chollet Inequalities for Rank-Two Correlation Matrices of Order Five*, Preprints.org version 1, posted 19 August 2026; explicitly not peer reviewed. [Primary record](https://www.preprints.org/manuscript/202608.1346/v1). Version and authors at live HTML lines 15-44; Section 7 at lines 447-456, exact SOS/LDL-transpose/Gram checks at 453 and integer/rational arithmetic at 456. Method comparison between exact SOS/PSD Gram certificates and this note’s nonnegative monomial identities on unbounded chambers. No transfer of a matrix theorem or novelty claim.

The primary records agree with the existing titles, authors, years, venues and version identities. All 27 SymPy authors were compared against the official project citation/BibTeX record. No `.bib` entry was replaced and no citation key changed. No retained metadata or nearby source claim remains unverified. The five-entry bibliography is driven by the actual origin, closest scope clarification, nontrivial verification method, software, and relevant exact-positivity comparison; its size was not a target. The elementary union bound, binary-expansion product and Chebyshev inequality are proved directly in the body, and no asymptotic enumeration theorem is invoked. The bounded source comparison supplies no exhaustive priority certificate.

The active 49-row first-sheet registry and manifest were parsed. Row 23 is the single minimum selection, with a substantive method comparison in ordinary text. Its actual v1 Section 7 was inspected; registry metadata alone was not used as evidence. The one-record explanation and exact current UTC date are in the selection JSON. The installed hook-compatible selection validator passes on the actual final source. No runner-owned pre-publication hook was invoked.

## Fixed claim-by-claim findings

| Claim | Source locator | Result and scope |
|---|---|---|
| C01 | BBFM Remark 6, pp. 18-19; local source lines 1115-1160 | Verified: The common summand gcd is one; no alternate normalization was substituted. |
| C02 | BBFM Proposition 4.1(a),(b),(d),(e), p. 19 | Verified: Degree, positivity, symmetry and even/odd equality match exactly. |
| C03 | BBFM Conjecture 7, p. 21 | Verified: The journal conjecture explicitly starts at n=6; the n=4,5 cases do not refute it. |
| C04 | COZ v2 Section 1.2.2, p. 4; HTML lines 191-197 | Verified: The original-language remark excludes n=4,5 and leaves n>5 open. Unversioned stale search snippets were not used as contrary evidence. |
| C05 | BBFM Theorem 4.7, p. 24; HTML lines 983-991 | Verified: Substituting the manuscript even index for the source’s 2n gives the identical recurrence and carry product. |
| C06 | BBFM Section 4 and COZ v2 compared with frozen claim.json and the bounded live queries | Verified: No equivalent was found in the inspected primary records. This is only the stated bounded assessment, not exhaustive priority or universal open-status certification. |
| C07 | BBFM Corollary 4.5, p. 23, and Remark 8, p. 24 | Verified: The sums for c1 and c2, and B(2m)=sum B(k) for c0, are explicitly present. |
| C08 | BBFM Corollary 4.2, pp. 21-22 | Verified: The source identity for positive k matches; k=0 is the trivial empty-sum base already defined. |
| C09 | Neidinger publisher abstract, HTML 66-70; manuscript Section 4 finite-difference argument | Verified: The source supports the cited general lower-set principle. The precise degree-D integer-simplex proof is written out locally, and no unseen detailed source result is needed. |
| C10 | Official SymPy citation lines 326-355, generator import and separate rational verifier | Verified: The authors and paper metadata match; the retained generator actually imports SymPy, while the second verifier uses Fraction polynomial algebra. |
| C11 | Zeng et al. v1 Section 7, HTML 447-456 | Verified: Exact SOS and LDL-transpose/Gram checks and symbolic integer/rational arithmetic are expressly described; the manuscript compares methods only. |
| M01 | claim.json assertion (1); growing-boundary proof exact statement and Section 3 | Verified: All quantifiers, epsilon range, floor, constant and reflected indices agree with the accepted scope. |
| M02 | claim.json assertion (2); boundary proof Sections 3-4 and kernel3 proof statement/strictness | Verified: The same n>=6, first-three and reflected indices, with stronger comparison only for even n, are retained. |
| M03 | claim.json assertion (3); growing-boundary proof G1 | Verified: Admissible integer K, internal 1<=j<=n, positive lower bound, and exact binomial indices match; the condition is sufficient only. |
| M04 | Growing-boundary proof Section 1, G2-G4 | Verified: The deletion identity, monotone block estimate and admissible choice K=floor(L-log2 L) match the manuscript proof. |
| M05 | Growing-boundary proof Section 2, G5-G8 | Verified: Both lower envelopes and the upper envelope preserve the same ranges and signs; squaring is done only under positivity. |
| M06 | Growing-boundary proof G7 | Verified: The binary-expansion product is a formal series identity; fixed coefficients require finitely many factors. |
| M07 | Growing-boundary proof Section 3, G9-G11 | Verified: The uniform bounds and fixed cutoff for smaller indices are all retained, with no pointwise-to-uniform strengthening. |
| M08 | Boundary proof equations (1)-(3) and the recurrence extraction | Verified: The cubic and A coefficients and positive T1/T2 formulas match the accepted derivation. |
| M09 | Boundary proof first-position section, equations (4)-(5) | Verified: Chebyshev is proved in the body; no additional unproved external inequality is being used. |
| M10 | Boundary proof second-position section, equations (6)-(7), all four cases | Verified: The four substitutions match the proof and packaged checker, with 105 monomials and exact positive K(0,0). |
| M11 | Kernel3 proof closed tails, together with frozen formal kernel definition | Verified: The quartic carry terms and polarized kernel preserve the formal extension accepted by the referee. |
| M12 | Kernel3 proof K1-K2 and complete certificate domain | Verified: The exact tails, active/inactive branches and positivity match; all 144 identities were replayed. |
| M13 | Kernel3 proof chamber table and inverse-gap formulas | Verified: Every symbolic entry in manuscript Table 2 was checked against the accepted table and inverse formulas. |
| M14 | Packaged verifier kernel3_certificate and accepted referee coverage argument | Verified: Fresh output gives 68 roots, 144 leaves, 12325 monomials and 8059 clipped vectors at height four; the infinite coverage argument is stated separately. |
| M15 | Kernel3 proof strictness and K4 | Verified: The positive e0 term and separate A comparison preserve m>=5 and m>=4 thresholds respectively. |
| M16 | Direct partition-sum reconstruction at n=6,8 | Verified: All twelve displayed coefficients and four Turan values match exactly; no rounding or sampled extrapolation. |
| M17 | Standalone source imports and degree arguments; accepted math report exact verification section | Verified: Only standard-library modules are imported. Degree bounds match the displayed tail formulas; no claim that software alone proves the analytic degree bounds. |
| M18 | Fresh packaged exact certificate checker output | Verified: Counts match exactly: 144/12720, 4/126, 6/42. |
| M19 | Fresh criterion.py output using exact fractions | Verified: All eight exponent/range pairs match the table; no huge numerator or partition counts were constructed. |
| M20 | Frozen research_growing_boundary.json scope and retained computational source | Verified: The recorded calibration has mean n=2..4096 and coefficient degree 13. This is historical finite calibration, not a new infinite theorem or claimed fresh rerun of all calibration. |
| M21 | Frozen original statement and accepted claim scope, plus manuscript proofs | Verified: No proof controls the central coefficient range here; the limitations and absence of optimality claims are accurate. |
| M22 | Literal TeX appendix comparison and exact strictness checker | Verified: All 42 coefficients in six arrays agree exactly; positivity and degree/evaluation counts were replayed. |

## Dependency and build coverage

Every publication input was read or, for the large certificate arrays, parsed and independently checked against its defining sums. All supplementary mathematical data match the accepted scope. Both source PDFs were freshly extracted and matched the frozen text byte for byte (`audit/source-passage-replay.json`). The standalone checker was run against the final supplement. The small numerical table was separately reconstructed directly from partition sums; the appendix arrays were compared literally.

The citation-key checker reports five cited keys, five BibTeX keys and five auxiliary bibliography keys, with no missing, extra or unused entries. The installed active-TeX parser finds exactly the same five ordinary body-flow keys as the ledger union. There are no citations supplied only by comments, inert macros, conditionals, verbatim material or nocite. Publication sources checked:

- `manuscript/README.md`
- `manuscript/build/main.bbl`
- `manuscript/main.tex`
- `manuscript/references.bib`
- `manuscript/supplement/README.md`
- `manuscript/supplement/criterion.py`
- `manuscript/supplement/kernel2.json`
- `manuscript/supplement/kernel3.json`
- `manuscript/supplement/strictness.json`
- `manuscript/supplement/verify.py`

See `audit/build.md` and `audit/visual.md` for the clean nine-page build and actual all-page visual inspection.
