# Verification Report

**PASS.** Job `newwin-00001-p08-release-467bc3c43b74`; reviewed 2026-09-12T09:48:39.283125+00:00.

**Mode:** fresh primary-source verification, using citation-check-skill and bib-reference-audit. The user prohibited subagents and interactive questions, so this worker performed the two passes sequentially. This is a fresh release review, not human peer review or a new mathematical referee decision.

| Metric | Count |
| --- | ---: |
| Extracted claim units | 24 |
| Verified claim units | 24 |
| Retained cited sources | 9 |
| Selected library sources | 1 |
| Natural non-library sources | 8 |
| Undefined, missing or unused bibliography keys | 0 |
| Unsupported, misleading or numerical-error findings | 0 |

## Fixed extraction and verification

Pass 1 read the full manuscript and froze the factual/attribution units, including the theorem, proof assertions, table and finite counts. Definitions were excluded. The ledger records each direct body citation and its exact line interval. The final extraction differs only in the equivalent literal UTF-8 Bézout spelling in C22; all assertions and keys match the initial extraction. Pass 2 then replayed the fixed 24 units in order against the locators below and the accepted evidence. No verification claim is inferred merely from a DOI, a successful build or an audit flag.

| Claim | Primary support / local basis | Finding |
| --- | --- | --- |
| C01 | S2, S3, S6 | The abstract formula, positive ordinary scalar and simple negative-root conclusion agree with the accepted claim and the complete printed proof. No quantifier or root assertion is strengthened. |
| C02 | Accepted scope and explicit manuscript proof / exact supplemental evidence | A maximal N-run ends in E for every nonempty excursion. Its final N creates exactly one NE, and its final two N letters create one NNE precisely when its length is at least two. These are noncyclic literal factors. |
| C03 | S2, S3 | Published Bóna Theorems 2 and 27 support enumeration and real-rootedness. Wang–Zhang published Theorems 1/2 reproduce them; its abstract supports confirmation of the interlacing conjectures. Author, year and theorem numbering match the cited versions. |
| C04 | S1 | The source explicitly asks for the Fuss extension in the rectangular family. The manuscript states its orientation and literal factor convention, matching immutable source.md and the accepted full scope. |
| C05 | Accepted scope and explicit manuscript proof / exact supplemental evidence | Theorem 1 is exactly the coefficient and root statement accepted in claim.json and audit/math.md: all m≥2,n≥1,1≤k≤n; degree k, simple zero at zero and k−1 distinct negative roots. |
| C06 | S2, S3 | Dividing the two coefficient formulas gives C(n−1,k−1)/C(mn+1,k−1). All j=1,…,k are in the ordinary formula domain at r=mn+1. The scalar is positive; no special-case exception remains. |
| C07 | S2, S4 | The generalized decomposition is explicitly in Zhang–Zhuang p. 5; its Lemma 12 marks augmented long ascents. Bóna Theorem 5 retains ordinary paths. The present comparison is limited to these inspected works and claims no exhaustive priority. |
| C08 | Accepted scope and explicit manuscript proof / exact supplemental evidence | The stated unique first-return split has the same components and marked return as the accepted lemma. Empty subexcursions are allowed and every component has the original step increments. |
| C09 | Accepted scope and explicit manuscript proof / exact supplemental evidence | The printed last-departure argument and inverse preserve the accepted proof, including skipped levels under a −m step. A descent below component base i would require a later upward departure from i−1. |
| C10 | Accepted scope and explicit manuscript proof / exact supplemental evidence | All six numerical table entries checked: P_m nonempty gives (0,0); only P_m empty gives (1,0); P_m=P_(m−1)=empty gives (1,1). The predecessor letters are E, EN, NN, respectively. m=2 is included. |
| C11 | Accepted scope and explicit manuscript proof / exact supplemental evidence | The three products are zF^m(F−1), zuF^(m−1)(F−1), zutF^(m−1). Their sum is the displayed F equation; substituting Y=F−1 gives the displayed φ. This matches the accepted formal derivation. |
| C12 | S5 | The exact formal inversion passage supports the displayed coefficient formula. n≥1 and Q(u,t) satisfy the field requirements. Coefficients lie in Q[u,t] by the recursion, allowing later u extraction; no analytic convergence is invoked. |
| C13 | Accepted scope and explicit manuscript proof / exact supplemental evidence | Choosing k u-factors yields v^(n−k)(1+v)^(mn−k)(v+t)^k. Subsequent extraction gives j−1 in the binomial coefficient. j=0 vanishes; mn−k≥k ensures degree k and positivity; the linear coefficient and k=1 case follow exactly. |
| C14 | Accepted scope and explicit manuscript proof / exact supplemental evidence | At t=1 the coefficient form becomes (1/n)C(n,k)[v^(k−1)](1+v)^(mn), giving the displayed Vandermonde specialization. No extra literature theorem is required for this elementary coefficient identity. |
| C15 | S2, S3 | Ordinary Theorem 1 of Wang–Zhang has the exact coefficient and exception. r=mn+1≥2k+1 satisfies all its hypotheses. The positive scalar identity transfers the Bóna Theorem 27 conclusion without a factor reversal. |
| C16 | S6 | DLMF 18.5.8, with index reversed, is the displayed J sum. Its Rodrigues table gives exactly the weight and factor (−1)^d/(2^d d!). The written product-rule expansion and leading-coefficient positivity agree termwise. |
| C17 | Accepted scope and explicit manuscript proof / exact supplemental evidence | With b≥1 the endpoint vanishing orders d+1 and d+b eliminate all integration-by-parts boundary terms. A polynomial formed from fewer than d sign-changing roots would give a nonzero one-signed weighted integral, contradicting orthogonality. d=0 is handled separately. |
| C18 | Accepted scope and explicit manuscript proof / exact supplemental evidence | The Möbius substitution clears denominators termwise. Each x in (−1,1) maps injectively to a negative t; these d roots exhaust the degree. The constant coefficient k and positive value at t=1 exclude missing exceptional roots. The accepted root conclusion is unchanged. |
| C19 | Accepted scope and explicit manuscript proof / exact supplemental evidence | At m=2,k=n, b=1 remains within the same weight range. For m=1 a nonempty component can begin NE, so crossing NNE factors can occur. The manuscript explicitly avoids applying the m≥2 functional equation outside its range. |
| C20 | Accepted scope and explicit manuscript proof / exact supplemental evidence | The final supplementary run checks all k at the displayed 40 grid pairs plus 9 additional distinct pairs. Exactly 49 pairs and sum(n)=303 polynomial rows result; all saved coefficient rows equal the accepted referee data. |
| C21 | S7 | Sturm Theorem 2.50 supports the signed-remainder root count with infinite endpoint. The verifier uses exact Fractions and positive rescalings; Q has nonzero constant coefficient. All 303 saved counts are k−1 and terminal gcd degrees zero, including the direct constant case. |
| C22 | S8 | The selected source Eq. (1) and Lemma 2.1 describe the normalized derivative Bézout formulation. The local exact gcd check supplies the rational coprimality assertion. Only this relationship is claimed, with no computational complexity bound or assertion that normalized pairs were produced. The UTF-8 spelling change is typographic only. |
| C23 | Accepted scope and explicit manuscript proof / exact supplemental evidence | The shipped script uses only the standard library, has the exact displayed pair list, stores coefficients/signs/root counts, and checks the eleven explicitly listed identity pairs. A fresh rerun reproduces all corresponding referee fields. The text correctly calls these finite observations rather than the infinite proof. |
| C24 | S9 | The authors’ primary software record supports the package citation. Local research-check.json specifies SymPy 1.14.0 and check-research.py uses its symbolic derivative and polynomial expansion routines. The separate model-review role is documented by the accepted audit; no external peer review or proof-assistant checking is asserted. |

## Source identity, nearby support and coverage

Each retained citation supports an ordinary body-flow use. The bibliography covers the origin, closest ordinary results, generalized decomposition comparison, formal inversion, Jacobi normalization, exact root counting, derivative coprimality and software actually used. No reference was added to meet a fixed total. The one library item is a minimum coverage selection, not a cap; none of the other screened library titles supports another necessary claim as directly. Renaming has not been used to manufacture a non-library citation.

### S1 — AlexanderssonCatalan

**Current and primary title:** Real-rooted polynomials: Catalan families.
Per Alexandersson; The Symmetric Functions Catalog; accessed 12 September 2026.

**Primary source:** [Real-rooted polynomials: Catalan families](https://www.symmetricfunctions.com/realRootedCatalan.htm).
**Exact locator:** NNE example and the following Alexandersson (2023) Fuss–Catalan conjecture; browser lines 40–48.
**Nearby support:** The maintained problem statement concerns the fixed-peak NNE distribution and asks for the n by nm Fuss extension. Our precise orientation and literal factor conventions are stated explicitly.
**Reason retained:** Problem origin and the exact conjectural extension being answered.
**Evidence:** audit/source-captures/source_open1.txt, audit/source-captures/source_open2.txt.

Metadata and nearby support: verified. Existing BibTeX retained; key unchanged.
### S2 — BonaEtAl2025

**Current and primary title:** A Combinatorial Proof of a Symmetry for a Refinement of the Narayana Numbers.
Miklós Bóna, Stoyan Dimitrov, Gilbert Labelle, Yifei Li, Joseph Pappe, Andrés R. Vindas-Meléndez, Yan Zhuang; EJC 32(2), P2.46 (2025); DOI 10.37236/12681. The publisher and PDF give 6 June 2025; a secondary search result with a different day was not adopted.

**Primary source:** [A Combinatorial Proof of a Symmetry for a Refinement of the Narayana Numbers](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i2p46/pdf/).
**Exact locator:** Published Theorem 2, p. 2; Theorem 5 and its preceding definition, p. 3; ordinary word conventions, pp. 4–5; Theorem 27, p. 18.
**Nearby support:** The joint coefficient is (1/k) C(r,k−1) C(r−k−1,j−1) C(k,j) when j>0 and k+j≤r; the exceptional constant case is r=k. Theorem 27 supplies ordinary real-rootedness. Theorem 5 still counts ordinary unit-step words. At r=mn+1≥2k+1 every j=1,…,k is allowed and the constant exception is absent.
**Reason retained:** Closest prior joint enumeration, underlying ordinary root theorem and the multi-pattern comparison.
**Evidence:** audit/source-captures/source_open2.txt, audit/source-captures/primary_specific.txt, audit/source-captures/publisher_metadata_final.txt.

Metadata and nearby support: verified. Existing BibTeX retained; key unchanged.
### S3 — WangZhang2024

**Current and primary title:** Interlacing Property of a Family of Generating Polynomials over Dyck Paths.
Bo Wang and Candice X. T. Zhang; EJC 31(1), P1.63 (2024); DOI 10.37236/12375.

**Primary source:** [Interlacing Property of a Family of Generating Polynomials over Dyck Paths](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v31i1p63/pdf/).
**Exact locator:** Published abstract, p. 1; Theorems 1 and 2, p. 2.
**Nearby support:** The paper reproduces the ordinary joint distribution and root theorem, with attribution to Bóna et al.; its abstract explicitly reports confirmation of the associated interlacing conjectures. The manuscript uses published Theorem 1, not the arXiv numbering 1.1.
**Reason retained:** Direct formula locator for the positive-scalar reduction and closest interlacing context.
**Evidence:** audit/source-captures/source_open2.txt, audit/source-captures/primary_specific.txt, audit/source-captures/publisher_metadata_final.txt.

Metadata and nearby support: verified. Existing BibTeX retained; key unchanged.
### S4 — ZhangZhuang2024

**Current and primary title:** A Subfamily of Skew Dyck Paths Related to k-ary Trees.
Yuxuan Zhang and Yan Zhuang; Journal of Integer Sequences 27 (2024), Article 24.2.4.

**Primary source:** [A Subfamily of Skew Dyck Paths Related to k-ary Trees](https://cs.uwaterloo.ca/journals/JIS/VOL27/Zhuang/zhuang2.pdf).
**Exact locator:** Generalized first-return decomposition and definition of augmentation, printed p. 5; long-ascent generating functions and Lemma 12, pp. 15–16.
**Nearby support:** The unique decomposition U μ1 … U μk D^(k) μ(k+1) is stated. Augmentation replaces each large down-step by U D^(k−1) L D. Lemma 12 marks long ascents of the augmented family, rather than the two unaugmented statistics considered here.
**Reason retained:** Attribution of the standard generalized decomposition and the precise nearby-statistic distinction.
**Evidence:** audit/source-captures/primary_specific.txt, audit/source-captures/support3.txt.

Metadata and nearby support: verified. Existing BibTeX retained; key unchanged.
### S5 — Gessel2016

**Current and primary title:** Lagrange inversion.
Ira M. Gessel; Journal of Combinatorial Theory, Series A 144 (2016), 212–249; DOI 10.1016/j.jcta.2016.06.018. The author-deposited arXiv record confirms journal, pages and DOI.

**Primary source:** [Lagrange inversion](https://arxiv.org/html/1609.05988).
**Exact locator:** Section 2.1, Theorem 2.1.1, Eq. (2.1.1); coefficient ring convention in Section 1.1.
**Nearby support:** Taking the outer series to be the identity in the formal inversion formula gives [z^n]Y=(1/n)[v^(n−1)]φ(v)^n. Here n≥1 and the coefficient field Q(u,t) has characteristic zero; φ(0)=ut is invertible.
**Reason retained:** Nontrivial formal coefficient-extraction method.
**Evidence:** audit/source-captures/primary_specific.txt, audit/source-captures/remaining_metadata.txt.

Metadata and nearby support: verified. Existing BibTeX retained; key unchanged.
### S6 — DLMFJacobi

**Current and primary title:** NIST Digital Library of Mathematical Functions, §18.5: Explicit Representations.
National Institute of Standards and Technology; current online section accessed 12 September 2026.

**Primary source:** [NIST Digital Library of Mathematical Functions, §18.5: Explicit Representations](https://dlmf.nist.gov/18.5).
**Exact locator:** Eq. 18.5.8; Eq. 18.5.5 and the Jacobi row of Table 18.5.1.
**Nearby support:** Reverse the finite-sum index in Eq. 18.5.8 and set degree d, α=1, β=b. The table gives w=(1−x)^α(1+x)^β, F=1−x², κ_d=(−2)^d d!, exactly yielding the manuscript normalization and Rodrigues identity. The manuscript proves the root conclusion itself.
**Reason retained:** Attribution and normalization of the classical Jacobi method.
**Evidence:** audit/source-captures/support3.txt, audit/source-captures/primary_specific.txt.

Metadata and nearby support: verified. Existing BibTeX retained; key unchanged.
### S7 — BasuPollackRoy2006

**Current and primary title:** Algorithms in Real Algebraic Geometry.
Saugata Basu, Richard Pollack and Marie-Françoise Roy; second edition; Algorithms and Computation in Mathematics 10; Springer, Berlin/Heidelberg, 2006; DOI 10.1007/3-540-33099-2.

**Primary source:** [Algorithms in Real Algebraic Geometry](https://www.cs.umd.edu/~gasarch/COURSES/752/S26/slides/AlgorithmsInRealAlgGeom.pdf).
**Exact locator:** Theorem 2.50 (Sturm), PDF page 60, printed p. 51; definitions of signed remainder sequences immediately preceding it.
**Nearby support:** The difference of endpoint sign variations for the signed remainder sequence of P and P-prime counts roots in (a,b), permitting infinite endpoints. Apply to Q=W/t on (−∞,0); Q(0)≠0. Positive primitive rescaling in the verifier preserves signs. The constant Q=1 case is separate.
**Reason retained:** Authoritative reference for exact finite root-count verification.
**Evidence:** audit/source-captures/metadata1.txt, audit/source-captures/support3.txt.

Metadata and nearby support: verified. Existing BibTeX retained; key unchanged.
### S8 — Zeng2026Bezout

**Current and primary title:** Generic Characteristic-Zero Equivalence Between Derivative Bézout Inversion and Multipoint Evaluation.
Zijian Zeng; Preprints.org, version 1, posted 31 August 2026; DOI 10.20944/preprints202608.2160.v1. This is a preprint, not a peer-reviewed article.

**Primary source:** [Generic Characteristic-Zero Equivalence Between Derivative Bézout Inversion and Multipoint Evaluation](https://www.preprints.org/manuscript/202608.2160).
**Exact locator:** Introduction Eq. (1), and Section 2.2, Lemma 2.1 and its proof; primary HTML lines 99–141. Publisher-indexed Analysis listing: matching title, sole author, posting date and exact DOI.
**Nearby support:** The source describes the normalized derivative Bézout pair for a polynomial with distinct roots. The manuscript cites only this formulation alongside its gcd test. Rational Euclidean division gives aQ+cQ-prime=1 when the rational polynomial is coprime to its derivative; a splitting field and normalization relate this to the source formulation. No pair is claimed as exported by the verifier and no generic complexity theorem is imported.
**Reason retained:** The actual derivative-coprimality interpretation in the finite verification discussion; selected library row 14.
**Evidence:** audit/source-captures/source_open1.txt, audit/source-captures/library_doi_final_search.txt.

Metadata and nearby support: verified. Existing BibTeX retained; key unchanged.
### S9 — MeurerEtAl2017

**Current and primary title:** SymPy: symbolic computing in Python.
Aaron Meurer and the coauthors listed in the authors’ official citation block; PeerJ Computer Science 3 (2017), e103; DOI 10.7717/peerj-cs.103. The existing BibTeX explicitly abbreviates the coauthors as “and others”, rendered et al.

**Primary source:** [SymPy: symbolic computing in Python](https://github.com/sympy/sympy-paper).
**Exact locator:** Official paper repository README, published citation and BibTeX block; software description in its abstract. Local evidence/check-research.py import and derivative/Poly calls; evidence/research-check.json sympy field.
**Nearby support:** The source identifies the symbolic-computation software. Actual version 1.14.0 and symbolic use are verified from local research evidence, not attributed to the 2017 paper.
**Reason retained:** Computational-assistance disclosure for software actually used.
**Evidence:** audit/source-captures/sympy_official_readme.txt, audit/source-captures/metadata0.txt.

Metadata and nearby support: verified. Existing BibTeX retained; key unchanged.

## Bibliography edits and exact library binding

Only the verified DOI field was restored in manuscript/references.bib, under Zeng2026Bezout. No source entry was wholesale replaced, no unrelated entry removed, and no key renamed. Existing bibliographic records were checked against primary records. The official SymPy citation explicitly lists the additional authors and agrees with the conventional “et al.” abbreviation retained in this bibliography. Unavailable export endpoints were not represented as fresh official BibTeX downloads.

Library row 14 was chosen after reading the active registry and all 49 first-sheet titles. The exact source article, version, author and Eq. (1)/Lemma 2.1 support were verified in its full primary HTML. The DOI is additionally displayed beside that exact title/author/date in the publisher’s indexed Analysis listing, preserved in audit/source-captures/library_doi_final_search.txt. The selected source is explicitly labeled a preprint. Its generic complexity equivalence is not invoked.

The selection binds the active registry and workbook hashes via build_registry_binding, citation attempt 1 and the runner-issued launch UUID. verified_at is the actual UTC date from date -u +%F. citation_context is the smallest literal citation-bearing sentence, with no unrelated equation-reference commands. The hook-compatible validate_selection call passed; its result is audit/selection-validation.json. The configured pre-publication hook was not invoked.

## Access, comparison and methodological limits

No bibliography-revision, literature handoff or Crossref capture files existed; those patterns were enumerated before editing or treating failed requests as limitations. WSL direct networking was denied. Browser primary records remained available. Some DOI/export/PDF variants failed; exact statements were checked in primary HTML or the published PDF text, and metadata was checked at the publisher or author-deposited record. The direct publisher Analysis listing open returned an older cached listing, while its indexed publisher excerpt contains the complete dated row used for DOI corroboration. This cache limitation is documented rather than disguised as a live resolver success. No inaccessible source or failed operation was converted into a mathematical claim.

All applicable academic search templates were run; queries and discovery outputs are preserved in audit/source-captures/search-records.json. Non-primary search results were not used as theorem evidence. The novelty comparison concerns the inspected Bóna, Wang–Zhang and Zhang–Zhuang results only; no worldwide priority or exhaustive open-status conclusion is asserted.

## Build, source dependencies and authored scope

All sorted publication source_files were checked: manuscript/README.md, manuscript/build.py, manuscript/main.tex, manuscript/references.bib, manuscript/verification.json, manuscript/verify.py. The compiler inventory includes only the canonical main.tex plus generated aux/bbl/out files within this project. BibTeX reads the explicitly declared references.bib. The supplementary script has no project-external code dependency. Standard installed TeX packages and fonts are toolchain dependencies.

The clean build and final key checker report nine cited/bibliographic/aux keys, with no missing, unused or undefined entry. The final LaTeX and BibTeX logs have no unresolved diagnostics or overfull/underfull boxes. The standalone verifier reproduced all 303 rows at 49 parameter pairs and all eleven identities; this corroboration is expressly finite. All six rendered final pages were actually viewed. Separate details are in audit/build.md and audit/visual.md.

Original source.md, checkpoint.md, claim.json, the accepted mathematical audit and every frozen mathematical snapshot file remain byte-for-byte unchanged. The final statement retains the full accepted quantifiers, coefficients and simple-root conclusion.

Mathematical snapshot: `c96c6b7b2814f0a2007caa6a6a99496edbecadac9ef9bc71fe55d3ecd76309f0`.
Manuscript snapshot: `4c76e5c2d8e61b75a85b57cf165889afc1b82282f4c36bfce8d9575114e62dd6`.
Final PDF: `9e7ebe7f07e45ddd1ff6e9e524e8cd63ce4060627680c871a96a8815807e76ff`.
