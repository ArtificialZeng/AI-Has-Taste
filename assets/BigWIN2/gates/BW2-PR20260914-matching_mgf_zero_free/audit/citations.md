# Verification Report

**Mode:** Search verification, followed by exact internal-evidence checks.
**Document:** `manuscript/main.tex` and all six publication source files.
**Generated (UTC):** 2026-09-14T12:37:53.067693+00:00
**Release job:** `primary-20260914-matching-mgf-zero-free-release-1689b9e708f3`
**Overall status:** PASS for the current result-note manuscript; original problem unresolved.

| Metric | Count |
|---|---:|
| Claims extracted and verified | 25 |
| Citation-bearing claim groups | 7 |
| Distinct cited publications | 5 |
| Selected library publications | 1 |
| Natural non-library publications | 4 |
| Numerical errors / unverified / hallucinations / misleading claims | 0 / 0 / 0 / 0 |

## Protocol and scope

The full manuscript, coefficient matrices and printed program were read before the 25 claims were frozen in `audit/citation-claim-ledger.json`. Verification then worked through those fixed claims in C01–C25 order. Independent source collection was batched, but extraction and verification were separate passes. User instructions made this audit noninteractive and prohibited subagents; the primary worker performed the checks directly. All applicable academic search templates were issued, then actual primary passages were inspected. Prior writer/referee reports were indexes and accepted-scope evidence, not substitutes for primary citation verification.

The initial strict selection check rejected ordinary imported/formatting TeX. A bounded markup repair inlined the unchanged matrices and code, replaced spacing and matrix wrappers by supported equivalents, removed table rules, and moved citation locators outside optional citation arguments. Every retained key is now a literal ordinary-flow citation. This was a presentation repair, not a mathematical revision. `audit/release-source-repair.diff` records it. All fixed claims were rebound to their shifted lines, then sources were rebuilt, refrozen, and all seven rendered pages reviewed. The bibliography entries and citation keys were unchanged; five records needed no metadata replacement.

## Claim-to-source verification

| ID | Source locator | Finding | Confidence |
|---|---|---|---|
| C01 | evidence/k4-proof.md, exact scope and stability-to-disk proof; audit/release-verification.json | Matches the accepted integer and real-parameter statements; exact transformed coefficients and determinants reproduced. | exact |
| C02 | claim.json; source.md; Wästlund Conjecture 11 | Unresolved is the original workflow scope: this paper proves only k=4 and does not claim a global resolution. | exact |
| C03 | wastlund2026, Conjecture 11, PDF page 25 | Same MGF, hypotheses and open radius mn/k. | paraphrase |
| C04 | claim.json; evidence/k4-proof.md; manuscript proof; audit/release-verification.json | All quantifiers, the reduced-numerator conclusion and the stronger algebraic domain agree with accepted scope. | exact |
| C05 | evidence/k4-proof.md, stability-to-disk proof; manuscript lines 238–253 | The (0,0) denominator factor vanishes at R and P(R)>0; nonintegral parameters are used only algebraically. | exact |
| C06 | wastlund2026, Section 4.3, Propositions 15–16, PDF pages 28–30 and 34 | The k<=3 result and finite-exception statement are explicit; final discussion explicitly supplies no cutoff. | paraphrase |
| C07 | C04 compared with C06; claim.json | Uniformity over every pair m,n>=4 eliminates every possible k=4 exception, without extending to k>=5. | interpretation |
| C08 | almsorkin2002, publisher abstract lines 469–473 | The same exponential matching model and Laplace-transform computations through k<=4 are explicitly described. | paraphrase |
| C09 | audit/source-search-wastlund2026.txt; audit/source-extra-search-and-methods.txt; precise primary statements in C06 and C08 | No equivalent theorem was identified in the sources actually inspected on this date; this is only a bounded search statement. | exact |
| C10 | evidence/k4-proof.md equations (1)–(3); manuscript/reconstruct.py; audit/release-verification.json | Generic rational equality, normalization, sextic coefficients and degree reproduced exactly. | exact |
| C11 | wastlund2026, equation (9) and separate d=0 rule, PDF page 8; Theorem 8, page 23 | Substitute k=i,d=i-j,n=n-4+i and clear denominators. The diagonal is separately handled, including m=i=4. | interpretation |
| C12 | evidence/k4-proof.md recursion and specialization paragraphs; audit/release-verification.json | There are 1+2+3+4+5=15 cells. Exact equality and degree checked; Ni>=1 and m-j>=1 justify every specialized off-diagonal division. | exact |
| C13 | evidence/research-k4-certificate.json; audit/release-verification.json | All seven literal matrices equal the direct shifted expansion of the displayed transformed sextic. | exact |
| C14 | evidence/research-k4-certificate.json; manuscript/hurwitz_certificate.py; audit/release-verification.json | Every full support rectangle and all positive integer coefficients compared, including constant terms. | exact |
| C15 | audit/release-verification.json; six literal table rows; frozen exact coefficient lists | All 24 numeric table entries and Delta6=h6 Delta5 match exactly; no rounding or numerical root approximation. | exact |
| C16 | holtz2003, Theorem 3 proof, PDF page 3; evidence/k4-proof.md convention paragraph | The ascending coefficient matrix has first minors h0,h0 Delta1,...,h0 Delta6. Its criterion and inversion yield precisely strict left-half-plane stability. | interpretation |
| C17 | zeng2026lens, Theorem 10, equations (8.25)–(8.27), HTML lines 1410–1455 | Rational Bernstein controls on the two-parameter box are explicit. The manuscript distinguishes the basis, domain and mathematical object of the present certificate. | paraphrase |
| C18 | evidence/k4-proof.md, stability-to-disk section; manuscript lines 225–236 | The displayed real-part identity covers the whole closed disk except -R, and h0>0 excludes the omitted point. | exact |
| C19 | evidence/k4-proof.md, denominator and cancellation argument; manuscript lines 238–253 | The factorwise positive inequalities give every rho>=R; A>0, the nonzero leading coefficient and P(R)>0 give cancellation and pole claims. | exact |
| C20 | evidence/k4-proof.md final proof paragraph; manuscript lines 255–268 | Counting matchings gives edge frequency 4/(mn); independence gives the displayed exponential bound. Domination on compact sets yields the asserted analytic identification. | exact |
| C21 | claim.json; manuscript lines 271–275; audit/release-verification.json | No larger-k or Gaussian claim appears. As a check on coefficient insufficiency, (z^2-z+1)(z+1)^4 has positive coefficients and two right-half-plane roots. | exact |
| C22 | meurer2017 official author README; evidence/k4-proof.md reproduction section; audit/release-verification.json | Software attribution matches the primary record; the actual local version is 1.14.0. The supplied exact integer determinant program was freshly run. | exact |
| C23 | evidence/k4-proof.md; accepted audit/math.md and runner role metadata; this job’s actual work | The identities certify an infinite domain. The stated AI assistance and separate AI review are disclosed without human peer-review or formalization claims. | exact |
| C24 | literal manuscript matrices; audit/release-verification.json; frozen 112 coefficients | Seven 4-by-4 matrices contain exactly 112 coefficients, each compared to the certificate. | exact |
| C25 | literal manuscript listing; manuscript/hurwitz_certificate.py; audit/release-verification.json | Printed code is byte-for-byte the indicated program section; execution reproduces supports, minima and final determinant identity. | exact |

## Bibliography correctness and coverage

| Key | Primary record and exact use | Status / changes |
|---|---|---|
| `wastlund2026` | [Moment generating functions in combinatorial optimization: Bipartite matching](https://arxiv.org/abs/2602.07563v1); Sections 2.1–2.3, equation (9), Theorem 8; Conjecture 11; Section 4.3, Propositions 15–16; PDF pages 7–8, 23, 25, 28–30, 34. Live HTML lines 149–159, 434–448, 488–490, 602–608, 710. Primary problem origin, closest zero-free predecessors, and the nontrivial probabilistic recursion used in the proof. | Verified; no BibTeX replacement or key change. |
| `almsorkin2002` | [Exact Expectations and Distributions for the Random Assignment Problem](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/exact-expectations-and-distributions-for-the-random-assignment-problem/9D846C840A833AEDA38A969A2E4D295C); Publisher abstract, lines 467–473; bibliographic information lines 437–456 and 480–485. Credits older four-edge transform computation and prevents its reconstruction being represented as the new contribution. | Verified; no BibTeX replacement or key change. |
| `holtz2003` | [Hermite-Biehler, Routh-Hurwitz, and total positivity](https://arxiv.org/abs/math/0512591); Author PDF page 3, Theorem 3 and its proof; extracted lines 223–287. Journal reference and related DOI on the primary arXiv record. An inspected primary proof of the classical stability criterion; its nontrivial role cannot be replaced by a generic citation about polynomial roots. | Verified; no BibTeX replacement or key change. |
| `zeng2026lens` | [Fixed Convex-Lens Spectral Constants: Möbius Reduction, Sharp Model Theorems, and Angle-Dependent Bounds](https://www.preprints.org/manuscript/202608.1272/v1); Theorem 10, asymmetric three-node patch, proof equations (8.25)–(8.27), live HTML lines 1410–1455. A substantive comparison between exact bivariate Bernstein certificates on a box and the present shifted monomial certificates on an unbounded quadrant. | Verified; no BibTeX replacement or key change. |
| `meurer2017` | [SymPy: symbolic computing in Python](https://github.com/sympy/sympy-paper); Authors’ official repository README, recommended citation and complete BibTeX, lines 0–5 of the raw web extraction. Attribution for the symbolic algebra software actually used, with the local version distinguished from the 2017 article. | Verified; no BibTeX replacement or key change. |

The primary problem paper supplies both the original conjecture and closest prior zero-free results. Alm–Sorkin supplies the older transform computation. Holtz supplies the exact classical criterion in the convention explicitly reconciled in the manuscript. Meurer et al. supplies actual software attribution. The single selected library preprint supplies a specific, limited bivariate positivity comparison. None is decorative, and the bibliography is neither library-only nor padded. The first four sources are not records in the active 49-entry library by title/DOI identity.

All 49 active library titles and the full metadata of the closest three leads were inspected. Row 13 was verified at its live full text, Theorem 10 and equations (8.25)–(8.27). It is explicitly a preprint. Its use is limited to Bernstein positivity on a two-parameter box; it is not a matching-cost dependency. The dynamic registry binding validates the actual workbook and registry hashes, first sheet, and 49-entry count. One relevant selection is justified in the selection JSON. Its exact compact citation sentence and nearby literal claim pass the unmodified hook-compatible validator. All five ordinary-flow keys exactly equal the ledger-key union.

Limits are explicit: Alm–Sorkin was checked at its publisher abstract, which directly supports the transform claim; no full-body novelty exclusion is asserted. Holtz’s 2003 journal article is distinguished from its 2005 author posting. The Meurer publisher requests failed, but the authors’ accessible primary repository gives the complete official citation and software abstract. SymPy version 1.14.0 and its actual use were verified locally, not attributed to a 2017 version claim. No saved Crossref captures were present. The library metadata was used only as a lead. Novelty language is bounded to the primary sources inspected on 14 September 2026; no exhaustive priority guarantee is given.

## Mathematical and computational scope

The title, abstract, theorem, proof and limitations agree with the accepted frozen claim. The unrestricted all-k original stays unresolved. The boundary at mn/4 is a pole, while the closed-disk assertion concerns the numerator. Real m,n occur only in the algebraic statement. The exact checks independently replayed the manuscript programs and compared 112 transformed and 951 determinant coefficients to frozen data, including all displayed matrices and all six table rows. The printed listing exactly matches the program. This verifies transcription and reproduction; it does not replace the accepted mathematical referee.

## Dependency, build and rendered-reference checks

The complete source list is the sorted `publication.json` list: main TeX, canonical bibliography, generated BBL, build program, and the two accompanying arithmetic programs. All were read. The final compiler recorder imports only main.tex, the generated BBL/aux/out, and installed system packages/fonts. The former matrices.tex remains an unused project file and is no longer a publication dependency because the exact matrices are now literal in main.tex. There are no additional authored inputs.

A clean pdfLaTeX/BibTeX/pdfLaTeX/pdfLaTeX build succeeded. The final logs contain no unresolved citation, reference, missing/duplicate database entry, compiler failure or overfull/underfull box. The skill checker reports five cited keys, five bibliography keys, and five AUX labels with no mismatch. Rendered pages 1–7 were actually viewed; all seven citations and all five references resolve. `audit/build.md`, `audit/visual.md`, `audit/bibliography-audit.json`, and `audit/citation-verification.json` supply detailed evidence. All final audits bind to the current snapshot and PDF. The runner-owned prepublication hook and publish step were not invoked.
