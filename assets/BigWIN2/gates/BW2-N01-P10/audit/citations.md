# Verification Report

**Mode:** Primary-source search verification, plus frozen-proof and exact-evidence checks for the paper's own results.  
**Document:** manuscript/main.tex and all four publication source files.  
**Generated:** 2026-09-12T11:16:42.970901+00:00.  
**Release job:** newwin-00001-p10-release-44a34dd73dbb. Citation attempt 1; launch baa9248d-7d48-40a6-9f61-ee6532cd8df9.  
**Overall status:** PASS for the final scoped manuscript.

| Metric | Count |
| --- | ---: |
| Extracted claim records | 33 |
| Verified records | 33 |
| Citation-bearing records | 9 |
| Distinct cited references | 6 |
| Selected user-library records | 1 |
| Natural non-library references | 5 |
| Unverified, misleading, numerical-error or hallucinated claims | 0 |

The immutable original problem remains unresolved. The accepted result-note
proves the sufficient coefficient criterion, its infinite family of length
classes, and the fixed-sum boundary cases. This report does not certify global
priority, a complete solution, numerical stability or journal peer review.

## Two-stage procedure

The entire manuscript was read and its claim/citation pairs frozen in
`audit/citation-claim-ledger.json` before the fresh primary checks. After the
scope-preserving TeX parser repair, the extraction was repeated at the same
376 source lines, followed by a separate claim-by-claim source replay. A later
PDF-metadata-only update changed no claim or location. The final ledger binds
the exact source hashes and current manuscript digest.

The 29 applicable citation-search templates were executed; their queries and
responses are retained in `audit/release-searches.json`. Broad surname queries
returned unrelated namesakes, which were not used. The evidence is the original
arXiv full text/version records and the published Integers PDF, with precise
locators in the table below. `audit/release-primary-evidence.txt` and
`audit/release-primary-replay.txt` retain the retrieved passages. One versioned
Thomas--Tung abstract request failed; its live versioned full text and unversioned
abstract (which lists only v1) succeeded. No source is judged unavailable.

Both lead patterns and both Crossref-capture patterns were enumerated before
editing; each had zero matches. No historical handoff supplied an exemption.
The two-pass audit was non-interactive as requested. This worker used no agents,
other Codex processes or background workers because the user prohibited them.

## Citation claims and precise support

| ID; manuscript lines | Key and primary source | Exact source locator | Support and limitation |
| --- | --- | --- | --- |
| C01; 62–64 | [HadelynEtAl2026](https://arxiv.org/html/2606.00420v1) | Section 5, especially lines 540-550, Question 5.3 | The source defines the Schur tableau-value partition map with multiplicities and asks which shapes give injectivity. The manuscript only says that the maps and broader question appear there; it does not claim the fixed-sum two-row refinement originates there. Confidence: paraphrase. |
| C02; 65–67 | [ThomasTung2026](https://arxiv.org/html/2606.19796v1) | Conjecture 6.3, lines 721-725; Convention 2.1 and Definition 2.17 | The quantified conjecture concerns every two-row shape on partitions of each prescribed integer, restricted to the domain where the map is defined. Shape (2,2) requires at least two parts. Confidence: paraphrase. |
| C03; 110–113 | [ThomasTung2026](https://arxiv.org/html/2606.19796v1) | Theorem 1.7, lines 83-86; Theorem 5.7, lines 667-674 | The (2,1) result and recovery from equal first k-1 parts hold for the stated partition setting. Theorem 5.7 assumes equal lengths; our output cardinality supplies that condition, and the comparison takes place in the fixed-sum problem. The positive-real extension is proved in our manuscript, not attributed to Thomas--Tung. Confidence: paraphrase. |
| C04; 114–115 | [Fomin2019](https://arxiv.org/pdf/1903.04062v1) | Printed p. 3, equation (1), and p. 4, Theorem 2.1; web PDF lines 77-112 and 127-168 | Equation (1) separates the highest input power sum from a polynomial in lower power sums. Theorem 2.1 develops the coefficients through exponential generating functions. This supports the established moment-method attribution, without asserting that Fomin proved the present Schur result. Confidence: paraphrase. |
| C05; 116–122 | [DAndreaEtAl2025](https://arxiv.org/html/2508.03568v2) | Example 4.7, coefficient of s_(2,2), lines 615-626; Definition A.1 and Example A.2, lines 702-715 | The displayed s_(2,2) derivation is s_(2,1)+(s_2-s_(1,1))*2^s-s_1*3^s. Rank evaluation and s=j-1 give exactly c_j(n). The manuscript labels its novelty as an application and arithmetic criterion. Confidence: interpretation. |
| C06; 125–130 | [Zeng2026MultiplicityArxiv](https://arxiv.org/html/2608.18179v1) | Theorem 1.1, lines 50-54; Definition 2.1, lines 65-71; Lemmas 2.2 and 3.1 and proof, lines 74-115 | The proper-tree hypothesis, unique nonleaf core weights and unrestricted repeated leaf weights are all explicit. The manuscript accurately limits the tree statement and compares multiplicity handling; it neither imports a tree argument nor asserts unrestricted tree reconstruction. Confidence: paraphrase. |
| C07; 204–215 | [DAndreaEtAl2025](https://arxiv.org/html/2508.03568v2) | Definition 3.2, lines 433-437; Example 4.7; Appendix A, Definition A.1 and Remark A.8, lines 702-715 and 764-769 | The operator is sum r^(s+1) d/du_r. Applying it to the displayed Schur polynomial and setting u_r=n yields the claimed scalar. Chern shadows exist at every order; the full scalar discriminant identity is stated in the source only in degrees 1,2,3. The manuscript retains all lower moments and explicitly avoids extending that identity. Confidence: interpretation. |
| C08; 251–253 | [HadelynEtAl2026](https://arxiv.org/html/2606.00420v1) | Theorem 5.1 and proof, lines 520-532 | The source recovers the largest entry from its jth power and then divides the maximum residual by the known largest entry to power j-1. At j=2 this is exactly the extremal algorithm printed here, whose positive-real domain is justified by the manuscript proof. Confidence: interpretation. |
| C09; 312–316 | [Li2026](https://math.colgate.edu/~integers/aa16/aa16.pdf) | Printed p. 2, Theorem 1 and following paragraph, PDF lines 33-39 | The theorem reconstructs partitions from distinct-index pair products and a fixed sum. The next paragraph explicitly allows finite positive-real sequences with the same sum. This supports the alternative final boundary recovery after E_2 is obtained. Confidence: paraphrase. |

## Bibliographic identities and retained-source coverage

All six current titles match their primary records, allowing ordinary title-case
and BibTeX brace normalization. No entry or citation key was replaced, renamed,
added or deleted. `manuscript/references.bib` is byte-identical to the writer's
version. The existing version-specific entries are verified records; no unofficial
BibTeX block was represented as a verbatim official export.

| Key | Verified title and author/year | Primary identity and reason retained |
| --- | --- | --- |
| ThomasTung2026 | Injectivity of symmetric polynomial maps on partitions; Rohith Thomas and Katherine Tung, 2026 | [arXiv:2606.19796v1](https://arxiv.org/abs/2606.19796): origin of the precise two-row question and closest known-prefix result. Preprint numbering is used; journal numbering from source.md is not asserted. |
| HadelynEtAl2026 | Counterexamples regarding elementary symmetric partitions; Vixail Hadelyn, Harper Niergarth, Weiyou Li and Wenhui Li, 2026 | [arXiv:2606.00420v1](https://arxiv.org/abs/2606.00420v1): Schur partition-map context and the actual extremal complete-homogeneous recovery method. |
| Fomin2019 | Moser Polynomials and Eulerian Numbers; Dmitri V. Fomin, 2019 | [arXiv:1903.04062v1](https://arxiv.org/abs/1903.04062v1): triangular moment reconstruction and coefficient calculation. The PDF byline includes the middle initial omitted by the abstract's abbreviated author record. |
| DAndreaEtAl2025 | A plethystic chain rule; Alessandro D'Andrea, Enrico Fatighenti and Claudio Onorati, 2025 | [arXiv:2508.03568v2](https://arxiv.org/abs/2508.03568v2), dated 8 October 2025: the necessary Appendix A and explicit shape-(2,2) derivation. The later version is not silently substituted. |
| Li2026 | A note on multiset reconstruction from pairwise products and total sum; Stella Jiahui Li, 2026 | [Integers 26, A16](https://math.colgate.edu/~integers/aa16/aa16.pdf), 3 pages, published 19 January 2026; DOI 10.5281/zenodo.18304958: closest fixed-sum pair-product recovery theorem. |
| Zeng2026MultiplicityArxiv | Multiplicity-Isolated Cores and Chromatic Symmetric Reconstruction of Trees; Zijian Zeng, 2026 | [arXiv:2608.18179v1](https://arxiv.org/abs/2608.18179v1), 18 August 2026: precise comparison of repeated-value recovery from symmetric invariants. This is the one selected library item, not a mathematical premise for the Schur theorem. |

The bibliography is neither library-only nor decorative. The five non-library
sources cover the question, closest results, and the nontrivial methods. The
library comparison states a concrete theorem with its properness and multiplicity
hypotheses. All 49 active titles were screened; the selected row 17 is the closest
actual reconstruction result. The less direct certificate, generic squarefree
inversion and Chebyshev-moment papers do not warrant padding. The literal
citation-bearing sentence, source support, UTC verification date and dynamic
registry binding are in `audit/user-bibliography-selection.json`.

The manuscript displays and checks its tableau content identities, Newton
recurrence, congruences and integer square certificate. These elementary steps
need no extra speculative citation. No Möbius-method or numerical-solver theorem
is silently used by the printed proof. The related tree theorem is not transferred
to the Schur setting. The Chern-shadow source's low-degree scalar identity is
not extended to higher degrees; the manuscript keeps the lower-moment polynomial.

The bounded primary comparison found no equivalent reconstruction result in the
inspected material on 2026-09-12. That supports only the explicit comparison,
not comprehensive priority. Secondary discovery hits were not evidence.

## Other substantive claims

These entries were verified against the actual frozen proof and exact records,
not by treating mathematical-acceptance JSON as a proof. Full extracted text and
source-specific support are in the ledger and `audit/citation-source-verification.json`.

| ID; manuscript lines | Decisive evidence | Check |
| --- | --- | --- |
| M01; 29–41 | evidence/research-moment-proof.md: Theorems A--C; sections 2,4,5 | Abstract retains the exact positive-real criterion, admitted residues, fixed-sum boundaries and unresolved scope. |
| M02; 56–59 | evidence/research-moment-proof.md: Section 1 | Indexed tableaux add numerical multiplicities; support or scalar sum omits data. |
| M03; 73–74 | evidence/research-moment-proof.md: Exact statement and Section 6 | The theorem only treats the admitted lengths and does not claim a complete resolution. |
| M04; 84–90 | evidence/research-moment-proof.md: Theorem A; Section 2 | First n nonzero linear coefficients recover n input power sums and the root polynomial, including repeated roots. |
| M05; 92–97 | evidence/research-moment-proof.md: Theorem B; Section 4 | The modular proof establishes nonvanishing at every order for the stated sufficient length classes. |
| M06; 99–104 | evidence/research-moment-proof.md: Corollary C; Sections 1 and 5 | Strict cardinality growth gives equal lengths; the two boundary lengths require the fixed positive sum. |
| M07; 106–108 | evidence/research-moment-proof.md: Exact statement; Section 6 | Necessary arithmetic residue restrictions and a stopped division do not establish an output collision. |
| M08; 135–143 | evidence/research-moment-proof.md: Section 1 | The printed tableau lists give coefficients 1,1,2 for the three allowable content types. |
| M09; 144–151 | evidence/research-moment-proof.md: Section 1 | The binomial count equals n^2(n^2-1)/12 and is strictly increasing for n>=2. |
| M10; 153–161 | evidence/research-moment-proof.md: Section 1, equation (1) | The five displayed exponent-type coefficient vectors combine to 0,0,1,1,2. |
| M11; 163–185 | evidence/research-moment-proof.md: Section 2, equations (2)--(3) | At total order j only one positive-degree factor can contain p_j; the remaining terms use lower moments. |
| M12; 187–202 | evidence/research-moment-proof.md: Section 2, Newton recurrence | The recurrence produces the input log root polynomial. Positivity ensures logs and injective exponentiation; repetitions remain root multiplicities. |
| M13; 219–241 | evidence/research-moment-proof.md: Section 4 | Even j>=4 gives nonsquare residue 2 mod 8. Odd j>=5 forces n=2 mod4 and units congruent to +/-1 mod3 and mod5, giving precisely the four residues. |
| M14; 255–261 | evidence/research-moment-proof.md: Section 5, equation (6) | Coincident, intersecting and disjoint index-pairs give the same multiset identity. Dotted union is explicitly defined to add multiplicities. |
| M15; 263–277 | evidence/research-moment-proof.md: Section 5 | All residual pairs contain an unrecovered factor bounded by b_(r+1), while b_1*b_(r+1) occurs. Repeated values are deleted with multiplicities. |
| M16; 279–282 | evidence/research-moment-proof.md: Section 5 | Positive fixed sum and observed data determine the degree-two or degree-four root polynomial. |
| M17; 284–310 | evidence/research-moment-proof.md: Section 5 | D(4)=20, total degree 80 and symmetry give product A^20. The scalar identity determines e_3 after e_1 and e_2 are known. |
| M18; 318–322 | evidence/research-moment-proof.md: Corollary C; Section 5 | The boundary lemmas and the coefficient/arithmetic theorem together cover exactly the corollary. |
| M19; 324–329 | evidence/research-moment-check.json: unequal_sum_boundary_witnesses | Both full integer output multisets and their unequal sums were replayed independently in audit/release-numerical-checks.json. |
| M20; 333–337 | evidence/research-verification.md: Executed coverage | Logarithms to base 2 identify the exponent lists exactly; changing base multiplies jth moments by a fixed jth power. |
| M21; 338–342 | evidence/research-moment-check.json: counts, grid_results, heldout_samples | 1281 grid inputs plus 60 heldout inputs equals 1341, split into 1252 complete recoveries and 89 predicted stops; boundary count 85. |
| M22; 343–345 | audit/referee-checks.json: counts; fresh_log_alphabet; rational_boundary_alphabet | The second implementation records 1281 fresh lists and 85 rational boundary recoveries. No claim of exhaustive real-domain coverage is made. |
| M23; 347–357 | audit/release-coefficient-certificate.json: All 26 rows and coefficient_zeros_n_j | The stdout-only certificate was rerun. The only admitted square pairs below length 10^6 are (2,2),(4,3),(14,5), and A_26=2541765165034. Strict monotonicity proves stopping. |
| M24; 359–363 | evidence/research-moment-proof.md: Section 6; coefficient formula | Substitution n=14,j=5 gives zero. This stops the displayed recurrence at p_5 without implying noninjectivity. |

The 26-row coefficient certificate was rerun with the source-package stdout-only
program. Counts were reconciled directly to the serialized research/referee
records, and both unequal-sum negative controls were recomputed from content
multiplicities; see `audit/release-numerical-checks.json`. The full output-writing
research/referee programs were not rerun in the frozen archive. Finite checks
remain supplementary; they are not promoted to an unbounded result.

## Complete publication and citation dependency audit

The publication source list is exactly the sorted set of
`manuscript/README.md`, `manuscript/check-coefficient-certificate.py`,
`manuscript/main.tex`, and `manuscript/references.bib`.
All four were read. README ranges agree with the source records; the standalone
certificate uses only the Python standard library and reproduces its stated
bounded result. The TeX recorder shows only main.tex and generated aux/bbl/out
files locally, plus installed TeX resources. The bibliography is the canonical
references.bib and the bbl is generated by BibTeX. There are no unlisted local
figures, included TeX files, fonts or data dependencies.

The active-body citation parser, final aux file and BibTeX database give exactly
six matching keys. All nine active direct cite commands are covered by the ledger.
Comments, nocite, inert macros, verbatim and conditional text contribute no keys.
The library selection validator passed against the exact runner-issued attempt
and launch; the read-only validation result is retained. The runner-owned
pre_publish_hook was not invoked.

`manuscript/main.tex` received only notation/parser compatibility changes and
literal PDF metadata. The changes and live parser failure are documented in
`audit/release-notation-repair.json`. No frozen mathematical input, source.md,
checkpoint.md, claim.json or accepted mathematical audit was modified. The final
build converged with zero unresolved citations, references or warning diagnostics.
The separate build and all-page visual reports are `audit/build.md` and
`audit/visual.md`. There are no remaining citation blockers.
