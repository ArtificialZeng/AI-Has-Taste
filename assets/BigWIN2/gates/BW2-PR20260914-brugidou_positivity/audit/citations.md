# Verification Report

**Mode:** Search verification with direct primary passages and accepted local proof/receipt checks.
**Document:** manuscript/main.tex and manuscript/references.bib.
**Generated:** 2026-09-13T19:11:53.621208+00:00. **Job:** primary-20260914-brugidou-positivity-release-ee08f920b725.

| Metric | Count |
|---|---:|
| Frozen substantive claims | 31 |
| Verified after repair | 31 |
| Direct citation occurrences / distinct sources | 12 / 5 |
| Non-library sources / gate-selected library sources | 4 / 1 |
| Remaining numerical errors, misleading claims, unverified claims | 0 |

**Overall status: PASS for the current snapshot and the accepted result-note scope.**

The initial extraction is preserved separately. The sole substantive citation correction adds the non-column hypothesis to the terminal-block comparison. The theorem, proof scope and original problem are unchanged. The final extraction precedes this final ordered verification pass. No interactive confirmation or subagents were used because the user explicitly required a non-interactive single-worker job.

## Citation correctness and bibliography coverage

| Key | Record and exact source location | Retained use / action |
|---|---|---|
| BrugidouMonomial | [On a particular specialization of monomial symmetric functions](https://arxiv.org/html/2306.15300v7); Vincent Brugidou; arXiv:2306.15300v7; revised 4 June 2025. Corollary 3.5, (3.16)-(3.17); (3.22); Conjecture 4.1; Section 4 computation paragraph; Corollary 5.2 (HTML lines 189-213, 233-257, 383-385). | Problem origin, normalization, polynomiality, base case, and closest individual-partition comparison. Existing source entry retained; no key or metadata change. |
| BrugidouAnalog | [A q-analog of certain symmetric functions and one of its specializations](https://arxiv.org/html/2302.11221v6); Vincent Brugidou; arXiv:2302.11221v6; revised 7 May 2025. Definition (1.1), Theorem 6.3(i)-(ii), equations (6.4)-(6.5); HTML lines 445-458. Version history v6. | Original positive aggregate normalization and nontrivial row recurrence used in the proof. Existing source entry retained; no key or metadata change. |
| BrugidouTutte | [A recurrence for certain Tutte polynomials](https://arxiv.org/html/2509.20959v2); Vincent Brugidou; arXiv:2509.20959v2; revised 18 November 2025. Equations (1.1)-(1.2), Theorem 1.1 and Section 4, equation (4.1); HTML lines 38-58 and 209-214. | Closest later two-variable extension and connected-graph method for computing rows. Existing v2 entry retained; no key or metadata change. |
| MercaAugmented | [Augmented monomials in terms of power sums](https://link.springer.com/article/10.1186/s40064-015-1506-5); Mircea Merca; SpringerPlus 4, article 724; published 24 November 2015. Theorem 1 (HTML lines 145-151) and About this article (lines 466-476). | Original augmented-monomial subtraction method implemented by the second verifier. Correct DOI 10.1186/s40064-015-1506-5 retained; no replacement or key change. |
| ZengMultiplicity | [Multiplicity-Isolated Cores and Chromatic Symmetric Reconstruction of Trees](https://arxiv.org/html/2608.18179v1); Zijian Zeng; arXiv:2608.18179v1; 18 August 2026. Theorem 1.1 and following explanation; Definition 2.1; Lemma 2.2 and proof; proof of Theorem 1.1 (HTML lines 50-115). Abstract-record DOI at line 23. | Restricted methodological comparison about extracting useful information from a small coefficient layer of a symmetric-function invariant. Retained existing entry and key; added only the missing DOI 10.48550/arXiv.2608.18179, transcribed from the live primary record. No fabricated or wholesale exported BibTeX replacement. |

All five source identities and their nearby claims were checked. The four non-library references supply actual origin, prior-result and method obligations; this is not a library-only bibliography. Row 17 is retained for its precise coefficient-layer comparison, not as a theorem about the present specialization. One selected entry is enough for the supported comparison, and no unrelated second entry was added. The active 49-entry first sheet and dynamic checksum binding were validated.

The official arXiv abstract records establish the version dates. The v6 q-analog/q-analogue title spelling difference is recorded without treating it as a different paper. The v2 Tutte record supersedes the old longer search-result title. Merca's DOI is the publisher-confirmed 10.1186 prefix. The selected Zeng author is Zijian, not Xiaojian.

Machine BibTeX exports returned tool errors, so no wholesale official-BibTeX replacement is claimed or synthesized. Existing verified entries were retained. The only added field is Zeng's DOI, copied from the live arXiv primary record. This export limitation leaves no unverified title, author, date, identifier, or source-support premise. There were no saved Crossref captures to substitute. No online source is declared nonexistent or unavailable on the basis of the WSL request failure.

## Ordered claim verification

| ID | Status / confidence | Exact evidence | Check |
|---|---|---|---|
| C01 | Verified / exact | claim.json; audit/math.md, Exact statement checked | Abstract matches the accepted integral normalization, positive prefix and sufficient region; it explicitly preserves the unresolved original target. |
| C02 | Verified / exact | BrugidouMonomial: Corollary 3.5, (3.16)-(3.17) | Multiplicities, factorial normalization, order zero and degree agree after writing source n(lambda) as nu(lambda). |
| C03 | Verified / paraphrase | BrugidouMonomial: Conjecture 4.1 | The manuscript states the original positivity question, without converting it to log-concavity or restricting its quantifiers. |
| C04 | Verified / exact | claim.json; audit/math.md, Exact statement checked and proof reconstruction | All quantifiers, the endpoint min(d,2b+3), F(a), and the a<=6 consequence match the accepted result-note. |
| C05 | Verified / paraphrase | BrugidouAnalog: Theorem 6.3 | The cited theorem establishes the aggregate coefficient property and its recurrence. |
| C06 | Verified / paraphrase | BrugidouTutte: Theorem 1.1; (1.1)-(1.3) | The extension has two variables and concerns contracted-complete-graph aggregate polynomials; it does not supply individual-hook positivity. |
| C07 | Verified / exact | BrugidouMonomial: Corollary 5.2 and Section 4 | Final text now includes the non-column hypothesis. The source reports the terminal n-1 block and size 43. |
| C08 | Verified / interpretation | literature/research-pass1-screen.md; audit/math.md; source passages listed in this report | Retained only the bounded inspected-source comparison. Current title/author/id queries and direct primary passages found no equivalent hook-prefix statement. No exhaustive priority or worldwide open-status assertion. |
| C09 | Verified / paraphrase | ZengMultiplicity: Theorem 1.1; Definition 2.1; Lemma 2.2 and its proof | The leading partition determines weight multiplicities and the next layer determines endpoint-order edge data; the named isolation hypothesis permits reconstruction. |
| C10 | Verified / interpretation | ZengMultiplicity: Definition 2.1 and Theorem 1.1; manuscript Sections 2-3 | Chromatic reconstruction and the q-exponential monomial specialization are different invariants. The manuscript uses the comparison as context, with no imported positivity conclusion. |
| C11 | Verified / exact | audit/math.md, Reconstruction of the decisive argument; manuscript (3)-(4) | For a>=3 the distinguished variable has exponent at least two, so the product splits into the two monomials with multiplicity one; normalization gives the displayed factors. |
| C12 | Verified / exact | BrugidouMonomial: (3.22) | Substitution n=b+2 and division by b! gives the stated q-integer base case, including b=0. |
| C13 | Verified / exact | audit/math.md, base cases and constants; manuscript (4)-(7) | Known polynomiality plus integral prefixes gives integrality. Constants and the a=3 formula follow from the same recurrence, without assuming an unknown coefficient sign. |
| C14 | Verified / exact | BrugidouAnalog: Theorem 6.3(i), (6.4) | The n>=r>=1 domain, r!(n-r)! denominator, constant (n-r)! and positive integer coefficients match. |
| C15 | Verified / exact | BrugidouAnalog: Theorem 6.3(ii), (6.5) | Setting r=1 gives precisely the row sum with binom(m-1,j), shift binom(j,2), and J_(m-1)^(j). |
| C16 | Verified / exact | audit/math.md, row excess; manuscript Lemma 2 | After subtracting j=1, only j=2 contributes at degree one; its constant is (m-3)!, valid also at m=3. |
| C17 | Verified / exact | audit/math.md, double coefficient-prefix reconstruction | The binomial ratio is s+1; the accepted row excess gives Delta>=0 and Delta_1=(s+1)p_0/2. |
| C18 | Verified / exact | audit/math.md, identity (P); manuscript (11) | The shifted C term cannot enter for t<=s. Strictness uses (s-t)p_0 if t<s and Delta_1 at t=s. |
| C19 | Verified / exact | audit/math.md, identity (E); manuscript (12) | At 2s+1 the contribution is exactly C_0. The lower bound is positive even at s=1, and d>=3s ensures the index exists. |
| C20 | Verified / exact | audit/math.md, full-region tail induction; manuscript (13) | F is nondecreasing, so the recursive B lies within the induction domain. A(1)=B(1) yields a nonempty positive tail through degree d. |
| C21 | Verified / exact | audit/math.md, boundary D=2b+4; audit/release-verification.json | The ceiling condition closes the prefix-tail interval including equality. The five displayed F values and the row supplement agree. |
| C22 | Verified / exact | audit/release-verification.json, examples[0] | Both preserved pure implementations freshly reproduce all eleven displayed coefficients; 10(6+6+3)-20=130. |
| C23 | Verified / interpretation | evidence/triage/hook-route.md; audit/math.md; accepted F definition | The prior sufficient cutoff max(0,D-1) is compared to max(0,ceil((D-4)/2)); the manuscript does not claim the new bound is optimal. |
| C24 | Verified / exact | audit/release-verification.json, examples[1]; BrugidouMonomial: Corollary 5.2, Section 4 | Freshly checked n=45, d=481, F(14)=31 and 481-(45-2)=438. The example is a non-column partition and 45>43. |
| C25 | Verified / exact | BrugidouTutte: (1.2), (4.1) | At r=1 no edges are contracted. The complete-graph specialization agrees with the connected spanning-subgraph evaluation used by the checker. |
| C26 | Verified / exact | evidence/research/hook_prefix_check.json; audit/release-verification.json | Parsed all 177 records; verified the a-domain, 66 direct checks through size 12, and exactly 88 records in the sufficient region. |
| C27 | Verified / exact | manuscript (14) and generating-function derivation; audit/math.md | The formal logarithm of the elementary product expands coefficientwise as (-1)^(m-1)p_m/m. No analytic convergence premise is used. |
| C28 | Verified / exact | MercaAugmented: Theorem 1 | The source subtraction sum, power-sum factor and augmented multiplicities match; reordering preserves the monomial indexed by the partition. |
| C29 | Verified / exact | audit/referee-check.json; audit/release-verification.json | All 120 listed direct parameters equal the complete size-2-through-16 hook domain. The added set is exactly the stated 28 pairs, disjoint from the original 177. |
| C30 | Verified / exact | audit/referee-check.json; audit/release-verification.json | Read the 205-case receipt and its exact 3243 prefix and 37827 tail counts. These are reported finite validations, not replacements for the universal proof. |
| C31 | Verified / exact | claim.json and audit/math.md, Gaps, limits and decision | The sufficient-only threshold and exclusions match accepted scope. General hooks, non-hooks and log-concavity are not claimed solved. |

## Mechanical and scope checks

The complete ordinary body-flow citation set equals the union of the ledger keys. All five keys occur in canonical references.bib, final main.aux and main.bbl; there are no unused entries, missing keys, duplicate entries or undefined citations. No citation is supplied by nocite, comments, a hidden branch, an inert macro or a second bibliography. Publication inputs consist only of the canonical TeX and BibTeX sources plus installed standard TeX packages.

The hook-compatible selection validator passed with the current job's attempt 1 and launch UUID. It required removal of title-only negative vspace, equivalent partition-size notation in the aggregate sum, and removal of the redundant final bibliography group. These are source-preserving notation/layout repairs, not changes to the accepted result. All affected build and visual checks were repeated on the final PDF.

Fresh display-data recomputation reproduced K_(5,1) and the degree-481 example with both preserved implementations. The exact finite receipt domains and counts match the manuscript. The universal result remains justified by the accepted proof, not by these calculations or this audit. No global novelty certificate, optimal threshold, log-concavity theorem, or original-conjecture resolution is asserted.

Reproduction: python3 audit/release-verify.py; the final bibliography consistency and log diagnostics are recorded in audit/build.md. Source locations, hypotheses and per-claim support are also serialized in audit/citation-source-verification.json. The configured pre_publish_hook was not invoked.

Snapshot bindings: mathematical a7e3cb1a0da871d53fdebc1638fdbbcc611f8739bce3289b362822cd5d358427; manuscript 06882b81d33e7d8fbc23865c86b5df51927549014b55348e0eed9c14726e8940; PDF 0af683a236a0798007148e4fc2d3bb5d2027c23200211301f1717d6d0065d0a4.
