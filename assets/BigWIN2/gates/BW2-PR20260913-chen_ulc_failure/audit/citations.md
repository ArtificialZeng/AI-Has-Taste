# Verification Report

**Mode:** Search verification with local original-PDF verification and exact computational replay.
**Document:** manuscript/main.tex and the complete five-file publication source set.
**Generated:** 2026-09-12T22:57:21.251568+00:00
**Job:** primary-20260913-chen-ulc-failure-release-6faab700d5ab; citation attempt 2; launch efe2192d-0671-4b15-8b62-77098852a806.

| Metric | Count |
| --- | ---: |
| Frozen claim groups | 24 |
| Verified groups | 24 |
| Ordinary-body citation occurrences | 8 |
| Distinct cited works | 6 |
| Selected active-library works | 1 |
| Natural non-library cited works | 5 |
| Unsupported retained assertions / numerical errors / misleading citations | 0 |

**Overall status: PASS for the manuscript's bounded assertions.** The accepted mathematical scope is unchanged. Complete later-journal text and absolute priority remain unverified and explicitly outside the manuscript's claims.

## Two-stage procedure and instruction integrity

I read the entire live manuscript, canonical bibliography and reproduction inputs. Stage 1 regenerated and froze 24 claim groups and their current source excerpts in audit/citation-claim-ledger.json and audit/release-6faab700d5ab/extraction-frozen.json before independent source verification. Stage 2 checked that fixed list in order against primary passages and the accepted mathematical dossier. No claims were added during verification. The user's non-interactive instruction replaced the skill's confirmation step. No agents or other Codex workers were used because the user expressly prohibited delegation.

The math skill, release reference and both requested citation skills were each read in a separate complete top-level result before their workflows. No instruction read was truncated. An oversized later evidence batch was re-read in bounded outputs; registry screening used the complete 49-title/DOI/keyword listing and full abstracts of the five shortlisted rows. The supervisor instruction-receipt handoff's exact provenance digest was independently matched. No fast-completion or bibliography-revision handoff exists.

The applicable author/year/title, exact-title academic-index, author/year/venue and DOI/arXiv discovery templates were run for all six references; the source search outputs are search-0.json through search-5.json, with additional identifier and primary-record queries in locatorsB.json, novelty_liggett.json and chen-journal.json under audit/release-6faab700d5ab/. Unrelated results and secondary summaries were not used as support. Original source passages, rather than DOI existence, determine the findings below.

## Citation and bibliography coverage

| Key | Primary source and precise locator | Nearby support and retained purpose |
| --- | --- | --- |
| AMQ2023 | [Motives of melonic graphs](https://ems.press/journals/aihpd/articles/8843881); Publisher PDF pp.523–524, Proposition 3.2, Section 3.5 and Corollary 3.4; web lines 767–827. | Proposition 3.2 supplies the recursive class formula; Corollary 3.4 gives nonnegative integer coefficients in S, identified just above as the three-punctured projective-line class. This supports the opening context sentence. |
| Chen2025 | [Log-Concavity of the Grothendieck Classes of Banana Graphs and Clasped Necklaces](https://arxiv.org/abs/2503.16296v2); Printed p.3 Theorem 1.1; pp.8–9 Definition 2.4 and (2.14)–(2.18); p.10 (3.1),(3.3); p.16 Proposition 3.8, computation through m=100, Conjecture 3.9; p.18 Proposition 3.10. | The inspected version defines the identical polynomial families and actual-degree normalization, proves ordinary log-concavity and non-ULC existence, and poses the uniform higher-index claim. Its order-m proposition is a different assertion. The manuscript consistently identifies this version. |
| Liggett1997 | [Ultra logconcave sequences and negative dependence](https://www.sciencedirect.com/science/article/pii/S0097316597927904); Publisher original abstract, first sentence; author bibliography item [70], abstract and BibTeX. Chen p.9 supplies the finite-order convention and no-internal-zeros qualification. | The publisher abstract directly states convolution closure for ultra-log-concave sequences, exactly the brief background attribution. No unread proof or additional negative-dependence result is invoked. |
| WangZhu2016 | [Log-convex and Stieltjes moment sequences](https://www.sciencedirect.com/science/article/pii/S0196885816300525); Original preprint pp.1–5, Sections 1–2, Hankel matrix discussion, moment representation (1), and Theorem 2.3 at p.5; web lines 91–124,170–210. | The source connects Hankel minors and moment log-convexity, then establishes infinite log-convexity for Stieltjes moment sequences. The manuscript attributes only this background and explicitly separates its signed density from the positive-measure setting. |
| Meurer2017 | [SymPy: symbolic computing in Python](https://docs.sympy.org/latest/citing.html); Official citation page lines 328–355, complete citation and exported BibTeX; authors' paper repository abstract. | Identifies the symbolic algebra software actually used by the supplied verifier. Fresh execution reproduced the four reported symbolic identities. The citation is software attribution, not proof certification. |
| ZengLiuRatnavelu2026 | [A Counterexample to the Tang–Zhang Schatten Norm Conjecture and Sharp Positive Results](https://www.preprints.org/manuscript/202608.1067/v1); Primary header lines 15–44 and 54–68; Section 2, equations (11)–(15), (17),(18), lines 222–279; concluding C<q<R. | The cited method example uses precisely seven positive rational residuals to separate the attained norm ratio from the proposed constant. All seven were freshly recomputed. Equation (16) defines a cubic and is not counted. Only this certification method is used as a comparison. |

Each current title, author list, year/version, venue, pages and DOI agrees with its primary record at the supported scope. Detailed metadata and access qualifications are in audit/citation-source-verification.json. The AMQ citation uses the publisher's 2023 issue year, distinct from its online date in December 2022. The Chen entry identifies arXiv v2 rather than silently substituting later journal numbering. The library record is correctly marked as a preprint. SymPy's complete 27-author list was compared with its official BibTeX.

Six entries were verified; no .tex, .bib or citation-key edits were necessary. No BibTeX replacement was performed and there is no old-to-new key mapping. Existing accurate local entries were retained. The bibliography supplies problem origin and closest prior results (AMQ and Chen), ULC context (Liggett), moment methods (Wang–Zhu), symbolic software (Meurer et al.), and a specific exact-sign-certificate comparison (Zeng et al.). None is retained merely to inflate a reference count. Elementary Cauchy–Schwarz and finite binomial algebra are proved or justified in place and do not require additional specialist sources.

The selected library DOI was additionally checked in the [official Preprints.org Analysis index](https://www.preprints.org/subject/browse/computer-science-and-mathematics/analysis), which associates the exact title, three authors and 17 August 2026 posting date with DOI 10.20944/preprints202608.1067.v1. This primary identity record is saved in library-official-index.json. Direct DOI/API/download opens and raw WSL HTTP failed; those access failures do not remove the available official primary support.

The selected library row 2 is a method example in ordinary body flow, not a source for the Chen theorem. Primary equations (11)–(15),(17),(18) give seven strictly positive rational residuals; all seven were freshly reproduced in library-residuals.json. Equation (16) is a definition. Other screened rows 29,34,38,47 do not supply an additional needed theorem for this argument. The dynamic registry/workbook binding covers the active first-sheet 49-entry library. The exact three-line selected sentence contains its direct citation and excludes unrelated masked commands. verified_at is the actual UTC date 2026-09-12. The installed standalone selection validator passed with attempt 2 and the runner-issued launch UUID; the runner-owned pre_publish_hook was not invoked.

## Fixed claim findings

| ID | Status | Source locator and finding |
| --- | --- | --- |
| C01 | Verified | audit/math.md; Chen v2 pp.3,16; manuscript proof Sections 2–3: The abstract stays inside the accepted all-parameter statement and accurately describes the signed-moment proof and endpoint. |
| C02 | Verified | AMQ2023, publisher PDF pp.523–524, Proposition 3.2 and Corollary 3.4: The original recursion and nonnegative coefficient conclusion support the opening attribution. |
| C03 | Verified | Chen2025, p.3 Theorem 1.1; p.10 (3.1),(3.3): Both displayed families and their ordinary log-concavity match the original text. |
| C04 | Verified | Chen2025, pp.8–9 Definition 2.4, (2.14)–(2.15): The denominator is the binomial coefficient for actual degree, not order m. |
| C05 | Verified | Liggett1997 original publisher abstract; Chen2025 p.9 (2.17): Convolution closure is stated in the original abstract; interval support is explicitly retained in the finite-order convention. |
| C06 | Verified | audit/math.md, exact scope and reconstruction; manuscript Theorem 1: Theorem 1 matches the frozen accepted claim for both families and all m>=4, including the empty higher-index cases. |
| C07 | Verified | Chen2025 p.16, Proposition 3.8 and Conjecture 3.9: Existence is credited as prior work; the inspected computation extends through m=100, and the uniform range is the source conjecture. |
| C08 | Verified | Chen2025 p.18, Proposition 3.10 and heading: That proposition uses order m; it does not establish the required degree-(m-1) minors. |
| C09 | Verified | audit/release-6faab700d5ab/chen-journal.json: The publisher preview records the DOI. Complete journal text was not inspected; no global or relative priority is asserted. |
| C10 | Verified | WangZhu2016 original preprint pp.2–5, especially Theorem 2.3; manuscript Lemma 2: The attributed Stieltjes result is present. Its nonnegative-measure hypotheses are not extended to the signed density. |
| C11 | Verified | audit/math.md, uniform positivity; manuscript Lemma 2: Even k gives a nonnegative density positive on an interval, so strict Cauchy–Schwarz has the required nonproportionality. |
| C12 | Verified | audit/math.md, uniform positivity; manuscript (6),(7): Reflection proves positivity for odd exponents, and E is obtained from the nonnegative auxiliary density. This stays within the accepted proof. |
| C13 | Verified | manuscript (8); audit/release-6faab700d5ab/exact-checks.json: The rational base formula was symbolically reproduced. Its numerator identity follows by substituting t=k+2 in the accepted numerator calculation. |
| C14 | Verified | manuscript (9),(10); audit/math.md; exact-checks.json symbolic_checks: Multiplication by 1+x and the exact determinant identity preserve positivity; B>0 justifies division. The recurrence residual is zero. |
| C15 | Verified | audit/math.md, polynomial facts; exact-checks.json polynomial_checks: The geometric sums establish the polynomial properties, and h-f=(-1)^m leaves every relevant positive-degree coefficient unchanged. |
| C16 | Verified | audit/math.md, endpoint; exact-checks.json endpoint_checks and symbolic_checks: The stated three coefficients yield -m exactly; both families and m=4,5 are included. |
| C17 | Verified | audit/math.md, normalization and extraction; manuscript (16)–(18): Binomial ratios and finite expansion produce the formulas. Polynomial identity includes s=-2 without an invalid division at that point. |
| C18 | Verified | audit/math.md, parameter bijection; exact-checks.json reduction and cancellation checks: The parameter map covers precisely p>=3,k>=0. The positive prefactor gives the required strict reverse minor; no range is enlarged. |
| C19 | Verified | audit/release-6faab700d5ab/exact-checks.json, boundary_examples and controls: The exact differences -4,-5 and D_6,3=6, with H(2,1)=-16/225, match the manuscript; these are finite observations. |
| C20 | Verified | ZengLiuRatnavelu2026 Section 2 (11)–(15),(17),(18); library-residuals.json: Seven positive rational residuals were checked against the source values. The claimed count excludes the cubic definition (16). |
| C21 | Verified | manuscript (21); audit/math.md; manuscript/verification.py moment(): Substitution and finite binomial expansion prove the rational sum; exact Fraction evaluation implements it. |
| C22 | Verified | audit/release-6faab700d5ab/exact-checks.json: Fresh execution gives exactly 1018 divisions,257556 target differences,1018 endpoints,703 reductions,920 moment pairs and460 odd-k induction checks over the stated ranges. |
| C23 | Verified | Meurer2017 official citation; manuscript/verification.py symbolic_checks(); exact-checks.json: The script actually uses SymPy and freshly returns the four asserted symbolic checks. The manuscript separates finite tests from the proof. |
| C24 | Verified | audit/math.md; manuscript/verification.py; manuscript/README.md: Scope and disclosure agree with the accepted dossier and inspected code. This release is not a new mathematical referee pass or external peer review. |

## Scope, primary access, and reproducibility

The fresh publisher preview confirms the later Chen DOI, the same families and the known existence classification, with changed internal numbering. Its full text was not retrieved; the direct open returned HTTP 403. No literature/crossref-*.json or literature/crossref-*.md captures exist here, as enumerated before any access conclusion. The source-conjecture theorem is not weakened or replaced by that access outcome. No equivalent uniform proof was located in the bounded queries used here; that statement is not a claim of global priority or present openness.

The theorem, lemma, parity split, strictness, degree-(m-1) normalization and small cases match audit/math.md and the frozen claim. The fresh verifier reproduced every numerical count and the negative boundary control. Infinite validity comes from the already accepted proof; this release audit only checked manuscript fidelity and reproduced the finite evidence. All original source, claim, checkpoint and accepted evidence bytes remain unchanged.

The canonical bibliography is the sole .bib input. No custom citation macros, hidden conditionals, inert text, comments or nocite commands supply body keys. The hook-compatible active-body key set equals the ledger union exactly. The complete authored dependency set is the sorted publication.source_files; TeX system packages and generated auxiliaries are build dependencies, not omitted authored content. The inspected portable verifier imports only standard-library modules and optional SymPy.

Clean build: bash manuscript/build.sh, exit 0. Exact replay: python3 manuscript/verification.py --symbolic, exit 0. Library replay: python3 audit/verify-library-certificates.py, exit 0. The installed check_bib_keys.py reports six cited keys, six bibliography keys, no missing/unused keys and complete final .aux agreement. Final .log/.blg contain no unresolved citations, references, duplicate entries, fatal errors or overfull/underfull boxes. All five rendered pages were actually viewed in this release context; see audit/visual.md. The build and visual reports are bound to the same current PDF.

Bindings: mathematical snapshot 4556257bb02194676513831cafeed05699982a8fd956a67820a92eda025f8ae5; manuscript 3ceea70d8cc6150305a1e7803d7c68e99dca884218ce450049e222720edc65fc; PDF 5a8c9b3de7676d91dac6e3836d8d4b43d2fe8301c99567a45480fbc9af995028. These operational identifiers remain outside the scholarly manuscript.
