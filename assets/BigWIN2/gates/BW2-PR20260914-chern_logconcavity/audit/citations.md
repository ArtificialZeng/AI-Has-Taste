# Verification Report

**Mode:** primary-source search verification, with frozen local mathematical evidence for the note's own results.
**Document:** manuscript/main.tex and all publication dependencies.
**Generated:** 2026-09-14T03:02:31.626173+00:00
**Release job:** primary-20260914-chern-logconcavity-release-7e11daba3cdd

| Metric | Count |
|---|---:|
| Frozen claims | 30 |
| Verified at the stated scope | 30 |
| Bibliography entries / active body keys | 5 / 5 |
| Selected library entries | 1 |
| Natural non-library body keys | 4 |
| Unsupported or misleading claims found | 0 |
| Unresolved citations / missing bibliography keys | 0 |

**Overall status: PASS at the exact accepted result-note scope.** The original problem remains unresolved. This is a release audit, not a replacement for the accepted mathematical review.

## Two-stage method and bindings

All manuscript claims were extracted before fresh source verification. The initial extraction is preserved in audit/citation-claim-ledger-initial.json. A deterministic selection-parser failure required flattening the table and moving PDF attachment insertion from TeX into the build process. The same 30 claims were frozen again with final locations before the final verification pass; no claim was added or strengthened. Verification below follows their fixed order. The final ledger contains the union of every active body citation key exactly. Commands, comments, verbatim text and metadata do not contribute citations.

All three requested skills were read completely, together with the release reference and release contract. The user expressly prohibited agents and interactive confirmation, so this worker performed the two passes serially. The required academic search templates were issued for all five entries (no DOI/arXiv query where none exists). Search results were used as leads; actual primary passages supplied claim support. The saved web results and source locators are audit/citation-search-evidence.json, audit/citation-primary-passages.json, and audit/citation-identifier-evidence.json.

The actual UTC date was obtained from date -u +%F. The selection uses runner-issued attempt 1 and launch 8ccb394d-4239-404a-9135-9292a8877c43, and a dynamically rebuilt binding to the active 49-row first-sheet registry. The hook-compatible validate_selection function passed on the final source. The configured pre_publish_hook was not invoked.

## Bibliography correctness and coverage

| Final key | Primary publication identity and precise use | Decision |
|---|---|---|
| BercziFeher2026 | Gergely Bérczi and László M. Fehér, *Positivity in classical enumerative geometry: a case study in synchronized AI-assisted mathematics*, arXiv:2605.25271v1, 24 May 2026. Theorem 2.4; Section 3; equations (5.1)-(5.2); Lemma 5.3; Theorem 5.4 and Appendix A. | Retain: problem origin, definitions, closest results, recurrence and proof method. |
| Branden2014 | Petter Brändén, *Unimodality, log-concavity, real-rootedness and beyond*, arXiv:1410.6601v1, 24 October 2014. Lemma 1.1, pp. 2-3, including its proof. | Retain: an inspected author-written proof of the classical coefficient inequality under the exact needed hypotheses; no claim of originating Newton's inequalities. |
| Meurer2017 | Aaron Meurer and 26 coauthors, *SymPy: symbolic computing in Python*, PeerJ Computer Science 3 (2017), e103, DOI 10.7717/peerj-cs.103. Authors' repository README and official BibTeX. | Retain: identifies the system actually used for initial symbolic generation; the final verifier is separately specified. |
| Patel2026 | Shivam Patel, *Proof for every Schur index*, actual reader contribution to the MathDB positivity problem, posted in 2026; equations (1)-(2) through the conclusion and displayed author attribution. | Retain: accurately acknowledges a nearby all-index positivity claim while preserving its unverified status. |
| Zeng2026Lens | Zijian Zeng, *Fixed Convex-Lens Spectral Constants: Möbius Reduction, Sharp Model Theorems, and Angle-Dependent Bounds*, Preprints.org v1, 19 August 2026. Theorem 10 proof, equations (8.25)-(8.27). | Retain: concrete exact positive-basis certificate comparison at the step where its relevance is explained. No Chern-class theorem or spectral conclusion is imported. |

Primary records: [Bérczi–Fehér](https://arxiv.org/abs/2605.25271v1), [primary full text](https://arxiv.org/html/2605.25271v1), [Brändén record](https://arxiv.org/abs/1410.6601v1), [Brändén original PDF](https://arxiv.org/pdf/1410.6601v1), [SymPy authors' paper repository](https://github.com/sympy/sympy-paper), [Patel's actual contribution](https://mathdb.com/p/374934/rank-two-binomial-positivity-conjecture-for-schur-coefficien), and [Zeng's primary v1 full text](https://www.preprints.org/manuscript/202608.1272/v1).

All retained BibTeX author/title/year/version/venue fields agree with the inspected records. The 27 SymPy authors were checked individually against the authors' supplied BibTeX. Existing BibTeX entries were retained without replacement or key renaming; missing optional fields were not invented. The only citation-source edit changed Zeng's optional citation note into adjacent ordinary text with a literal direct cite. The final bibliography remains canonical manuscript/references.bib, with all five entries used. The library is a minimum coverage condition: four genuine non-library citations cover the actual scholarly dependencies. No general Chern geometry or unrelated graph/operator theorem is invoked that would need padding references. Elementary support and interpolation steps are proved in the text.

All 49 active registry title/abstract records were screened. Row 13 was selected for its exact basis-positivity verification technique. The registry was not treated as primary support: the actual Theorem 10 proof was read. Row 29 overlaps that comparison, while other entries have different mathematical objects or verification tasks. No second entry adds a necessary claim. The selected sentence is literal, compact, contains the direct citation, and excludes unrelated eqref/label commands.

## Source access and comparison limits

The primary Zeng version page supplies the actual title, author, posted date, version and full proof. Its DOI identifier 10.20944/preprints202608.1272.v1 is additionally corroborated by the independently retrieved [bibliographic record](https://www.researchgate.net/publication/412697332_Fixed_Convex-Lens_Spectral_Constants_Mobius_Reduction_Sharp_Model_Theorems_and_Angle-Dependent_Bounds); this secondary metadata is not used for mathematical support. The DOI resolver, Crossref endpoint and PDF download attempts returned web-tool errors. The shell fetch returned Operation not permitted. No successful direct Crossref or PDF response is claimed. Both literature/crossref-*.json and literature/crossref-*.md were enumerated and had no matches. Source availability is established by the actual primary HTML; the narrower endpoint failures do not erase it. Similarly, the PeerJ PDF endpoint returned 403, but the authors' own repository supplies the published record and full official BibTeX, which were inspected. These access limits leave no unsupported nearby claim in the manuscript.

Fresh focused queries for the arXiv ID, authors, residual, forcing polynomial, lower modes and log-concavity found no equivalent explicit R_k theorem among inspected sources. The source's Figure 1 label was independently read from the frozen primary SVG and compared with its formal Theorem 5.4. The paper correctly follows the formal mode-one statement. No worldwide priority, complete spreadsheet-history search, or inaccessible conversation-history search is claimed. Both supplied handoffs were read and their named frozen local captures/receipts exist. No bibliography-revision or fast-completion handoff existed.

## Claim-by-claim decisions

### C01 — Verified (exact)

The note proves all-k residual support and log-concavity with a 41-prefix exact certificate; the original conjecture and second-mode restriction remain unresolved by it.

Location: manuscript/main.tex:28-39. Direct keys: none; original argument/evidence. Source: claim.json; audit/math.md, accepted scope; audit/release-certificate-output.txt. The abstract preserves k>=4, the precise support, 41-prefix certificate and unresolved original status. The attached replay actually succeeds.

### C02 — Verified (paraphrase)

The Schur coefficient functions A are rational polynomials with the stated finite-difference Newton expansion.

Location: manuscript/main.tex:53-59. Direct keys: BercziFeher2026. Source: BercziFeher2026, Theorem 2.4 and Section 3; primary HTML S2.Thmtheorem4 and S3. The polynomiality theorem applies at n=2, and the finite triangular Schur conversion preserves rational polynomiality. The Newton expansion is the stated finite-difference basis.

### C03 — Verified (exact)

Chern-root power sums, Newton identities and triangular Schur conversion give polynomiality of degree at most 2k.

Location: manuscript/main.tex:62-65. Direct keys: none; original argument/evidence. Source: manuscript/main.tex, equations (1)-(3); accepted evidence/auxiliary-proof.md. The root power sum of order h has degree at most h+1 in d. Newton identities give degree at most 2k; the fixed triangular basis change does not increase it.

### C04 — Verified (paraphrase)

Conjecture 3.3 asks for binomial log-concavity; formal Theorems 3.7 and 5.4 prove modes zero and one, and Theorem 5.2 proves mode-two positivity.

Location: manuscript/main.tex:67-70. Direct keys: BercziFeher2026. Source: BercziFeher2026, Definition 3.1, Conjecture 3.3, Theorems 3.7, 5.2 and 5.4. Formal source statements have precisely the claimed modes and distinguish positivity from log-concavity.

### C05 — Verified (exact)

For every integer k>=4, rho is positive exactly on [k-2,2k-1] and all its adjacent log-concavity minors are nonnegative.

Location: manuscript/main.tex:84-91. Direct keys: none; original argument/evidence. Source: claim.json; audit/math.md, accepted assertion and reconstructed proof. Theorem 1 is the accepted all-k auxiliary theorem, without strengthening to the full second mode.

### C06 — Verified (exact)

The four-term forcing polynomial occurs in source equation (5.2); the recurrence and its k=4 zero convention follow from the product identity.

Location: manuscript/main.tex:93-106. Direct keys: BercziFeher2026. Source: BercziFeher2026, equations (5.1)-(5.2), proof of Theorem 5.2. All four forcing terms and the (x+1)A(k-1,2) term match. The source also uses A(3,2)=0; the displayed product factorization and palindromic convention justify it.

### C07 — Verified (paraphrase)

The new increment is log-concavity of the forcing sum, extending the source 17-prefix mode-one calculation to 41 prefixes; the method and recurrence are prior.

Location: manuscript/main.tex:108-114. Direct keys: BercziFeher2026. Source: BercziFeher2026, proof of Theorem 5.4 and Appendix A; audit/math.md, contribution assessment. The source explicitly has seventeen trace prefixes. The present 41-prefix forcing theorem is a specific application of the same method, as the manuscript states.

### C08 — Verified (exact)

The positive log-concave rows (1,1,1,1) and (1,2,4,8) sum to (2,3,5,9), which is not log-concave.

Location: manuscript/main.tex:110-111. Direct keys: none; original argument/evidence. Source: direct integer calculation of the three displayed rows. Both summands have equality in their interior log-concavity minors. For the sum, 3^2-2*5=-1 and 5^2-3*9=-2.

### C09 — Verified (paraphrase)

Patel claims all-index binomial positivity by support induction; no unverified all-index assertion is used in this note.

Location: manuscript/main.tex:115-118. Direct keys: Patel2026. Source: Patel2026, actual contribution headed Proof for every Schur index, equations (1)-(2) through conclusion; author line 181. The actual post claims all-index positivity by recurrence and support induction. The manuscript treats it as a reader claim and does not import its correctness.

### C10 — Verified (interpretation)

No equivalent explicit residual theorem was found in the inspected sources by 14 September 2026; source Figure 1 conflicts with the formal mode-one Theorem 5.4.

Location: manuscript/main.tex:120-126. Direct keys: BercziFeher2026. Source: BercziFeher2026, Figure 1 inline SVG S1.F1 and formal Theorem 5.4; audit/citation-search-evidence.json and audit/citation-primary-passages.json. The frozen figure actually labels the final log-concavity stage j=2; the formal theorem and proof say j=1. The recorded focused queries and inspected sources yielded no equivalent theorem for this R_k. This is bounded negative-search evidence, not worldwide priority.

### C11 — Verified (exact)

The fixed-point-free permutation defect recurrence has strict support K+1<=N<=2K for K>=1.

Location: manuscript/main.tex:130-140. Direct keys: none; original argument/evidence. Source: BercziFeher2026, Lemma 3.5; manuscript support proof; audit/math.md. Deleting a letter or its transposition gives the recurrence. The cycle-count argument gives exactly K+1<=N<=2K for K>=1, including endpoint constructions.

### C12 — Verified (paraphrase)

Zeroth and first Schur modes obey the displayed permutation-defect and rising-factorial identities; the formulas and defect basis occur in source Section 3.

Location: manuscript/main.tex:142-160. Direct keys: BercziFeher2026. Source: BercziFeher2026, Section 3.2, equations (3.1)-(3.3) and proof of Theorem 3.6. The source contains the rising-factorial expression, defect basis, zeroth coefficient expansion and first-mode formula used here.

### C13 — Verified (exact)

Newton multiplication and defect reduction give the displayed four-term first-mode coefficient formula.

Location: manuscript/main.tex:162-176. Direct keys: none; original argument/evidence. Source: BercziFeher2026, Theorem 3.6; manuscript equations (10)-(11); audit/math.md. The four multipliers and shifted D indices agree term by term with the source and accepted derivation.

### C14 — Verified (exact)

The first-mode coefficients have strict support [n-1,2n] for n>=2 and the zeroth mode has support [h,2h] for h>=1.

Location: manuscript/main.tex:177-185. Direct keys: none; original argument/evidence. Source: manuscript support calculation; audit/math.md, reconstructed support proof. The active multipliers are positive. The endpoint values and the t-substitution agree with the accepted argument, including n=2 and h=1.

### C15 — Verified (exact)

Linear multiplication gives the four listed term supports, all nonnegative, whose union proves forcing support including k=4.

Location: manuscript/main.tex:187-196. Direct keys: none; original argument/evidence. Source: BercziFeher2026, Lemma 5.1; audit/math.md; manuscript four displayed intervals. Newton multiplication yields the stated support rule. The four intervals and their union agree with the accepted proof, without cancellation.

### C16 — Verified (paraphrase)

The derivative recurrence and Rolle theorem give real nonpositive roots; the cited coefficient inequality gives log-concavity and the strong pair inequalities with zero extension.

Location: manuscript/main.tex:200-218. Direct keys: Branden2014. Source: Branden2014, Lemma 1.1, printed pp. 2-3; BercziFeher2026, proof of Theorem 3.7. The original Branden lemma assumes a finite nonnegative coefficient sequence and real roots, and explicitly implies ordinary log-concavity. The derivative recurrence supplies those hypotheses here; interval support handles zero-boundary cases.

### C17 — Verified (paraphrase)

This is the defect-sequence argument of source Lemma 5.3.

Location: manuscript/main.tex:219-220. Direct keys: BercziFeher2026. Source: BercziFeher2026, Lemma 5.3 and its proof. The strong pair inequality follows from the monotone ratios of the same defect sequence, exactly as attributed.

### C18 — Verified (exact)

The exact recursion specifies seven expansion polynomials p_i, each of total degree at most four.

Location: manuscript/main.tex:222-250. Direct keys: none; original argument/evidence. Source: audit/math.md; manuscript/certificate.py; audit/release-frozen-certificate-comparison.json. The seven recursively specified degree-at-most-four polynomials reconstruct successfully and equal the frozen expansion polynomials.

### C19 — Verified (exact)

The complete central and adjacent quadratic product pair set has exactly 41 pairs.

Location: manuscript/main.tex:252-265. Direct keys: none; original argument/evidence. Source: audit/release-table-verification.json; manuscript/certificate.py. The union of central and shifted pair sets contains exactly 41 pairs. No parameter-dependent terms have been omitted.

### C20 — Verified (exact)

Tracewise Abel summation and permutation support yield the exact identity and the nonnegative support variables with the stated inverse substitution.

Location: manuscript/main.tex:267-286. Direct keys: none; original argument/evidence. Source: audit/math.md; manuscript equations (17)-(18). Finite Abel summation gives the identity, and solving the two displayed support equations gives the stated k,r substitution. The range K=k-3>=1 agrees with k>=4.

### C21 — Verified (exact)

All 41 substituted prefixes are nonzero with 1506 positive rational coefficients; they prove every active Abel summand nonnegative, including boundary cases.

Location: manuscript/main.tex:288-302. Direct keys: none; original argument/evidence. Source: audit/release-certificate-output.txt; audit/release-frozen-certificate-comparison.json; audit/math.md. The extracted attachment verifier reconstructs all 41 identities and 1506 positive coefficients. The accepted argument turns this complete finite algebra into the infinite-range inequality, including boundaries.

### C22 — Verified (paraphrase)

Zeng Theorem 10, equations (8.25)-(8.27), uses exact positive Bernstein coefficients on a compact parameter box; basis signs and exact identities give uniform positivity, while this note uses monomials on the nonnegative support quadrant.

Location: manuscript/main.tex:304-310. Direct keys: Zeng2026Lens. Source: Zeng2026Lens, v1, Theorem 10 proof, equations (8.25)-(8.27), primary HTML lines 1408-1458. The primary proof gives a,b in [1/6,5/6], an affine map to [0,1]^2, and exact positive rational Bernstein controls for V,-W,Z. The manuscript compares that verification technique with monomial positivity on its different support quadrant, without importing spectral conclusions.

### C23 — Verified (exact)

The recurrence gives B(k,2,r+1)=g_r+rho_r; the explicit minor identity shows that g preserves nonnegative interval-supported log-concavity.

Location: manuscript/main.tex:314-330. Direct keys: none; original argument/evidence. Source: audit/math.md, mixed-inequality discussion; manuscript explicit minor identity. Expanding g verifies the three-line minor identity. Strong pair inequalities and the zero extension give the stated lower bounds. This is only the preservation step.

### C24 — Verified (exact)

The displayed unproved mixed inequality is sufficient for second-mode induction with the stated base case and support overlap; no equivalence to the original is claimed.

Location: manuscript/main.tex:332-344. Direct keys: none; original argument/evidence. Source: audit/math.md, remaining-gap discussion; manuscript equation (20). The mixed expression plus the two separate minors is the minor of g+rho. The base case and support overlap agree with the accepted analysis. The mixed inequality itself remains explicitly unproved.

### C25 — Verified (exact)

Exact checks reconstructed products for 0<=d<=90: 3690 residual entries and minors and 3690 recurrence evaluations for 4<=k<=44, plus 2000 mixed cases for 5<=k<=44; the first row is (0,0,27,212,660,1000,735,210,0).

Location: manuscript/main.tex:346-355. Direct keys: none; original argument/evidence. Source: audit/referee-verification.json and audit/referee_verify.py lines 204-301; audit/release-table-verification.json. The historical reviewer code reconstructs d=0,...,90, then has 41*90=3690 entries and recurrence evaluations. The mixed range has sum(2k+1,k=5,...,44)=2000 cases. The saved report contains the exact first row displayed. These counts are historical exact checks, not a new all-k proof.

### C26 — Verified (exact)

The PDF embeds the complete JSON and standard-library reconstruction, whose command checks seven polynomials, 41 prefixes, and 1506 positive coefficients.

Location: manuscript/main.tex:360-375. Direct keys: none; original argument/evidence. Source: audit/release-attachment-check.json; audit/release-certificate-output.txt. pdfdetach lists and extracts both named files. They match the publication sources byte for byte and the copied command verifies all specified objects.

### C27 — Verified (exact)

The initial symbolic generator used SymPy, identified by Meurer et al. (2017).

Location: manuscript/main.tex:377-377. Direct keys: Meurer2017. Source: Meurer2017, author-maintained sympy/sympy-paper README citation/BibTeX and abstract; evidence/j2_residual_symbolic.py line 11. The authors primary repository identifies SymPy and supplies the full 27-author published record. The frozen initial generator actually imports sympy. The final certificate verifier uses only the standard library.

### C28 — Verified (exact)

The two exact verification implementations use a 9-by-9 grid and sparse polynomial comparisons; degree at most eight makes 3321 grid comparisons a complete identity certificate.

Location: manuscript/main.tex:378-389. Direct keys: none; original argument/evidence. Source: evidence/verify_residual_certificate.py lines 103-164; evidence/residual-certificate-verification.json; audit/referee_verify.py; audit/math.md. The first code checks 81 exact points for each of 41 prefixes; 41*81=3321. The independent sparse-polynomial code is distinct. Degree at most eight makes repeated univariate interpolation complete; finite numerical tests are not misrepresented as the proof.

### C29 — Verified (exact)

AI assisted proof exploration, code, sources and drafting, with a separate exact-arithmetic review pass; there is no proof-assistant or journal-peer-review claim.

Location: manuscript/main.tex:427-433. Direct keys: none; original argument/evidence. Source: research/write/referee provenance in claim.json, audit/math.json, audit/math.md, audit/write.md. The disclosure agrees with the recorded AI-assisted process and separate implementation. It explicitly avoids claims of formalization or journal review.

### C30 — Verified (exact)

Table 1 inventories all 41 prefix polynomials with their trace, pair, total degree, nonzero monomial count, and exact minimum coefficient, totaling 1506 coefficients.

Location: manuscript/main.tex:391-425. Direct keys: none; original argument/evidence. Source: audit/release-table-verification.json; embedded manuscript/certificate.json; rendered page 6. All 41 trace/pair/degree/count/minimum records match the exact rational certificate. Both columns, all values and the two fractional minima were inspected in the rendered table.

## Dependency and PDF checks

The complete publication list is manuscript/main.tex, manuscript/references.bib, manuscript/certificate.py and manuscript/certificate.json. The table is now literal in main.tex. The latter two sources are actual PDF attachments installed by audit/release-build.py. The .fls recorder lists only the main source, generated build inputs and installed system TeX dependencies; the build driver supplies no additional mathematical content. The historical separate table file is unused and excluded from publication.json.

The final BibTeX key check reports five body keys, five database keys and five aux bibliography keys, with no missing, unused, or inconsistent key. All rendered references on page 7 resolve, and the body citations are visibly ordinary flow on pages 1-6. The clean compiler/BibTeX logs contain no unresolved citations, cross-references, warnings or layout errors. All seven final pages were actually viewed; see audit/visual.md. The 41 table rows were compared value by value with the attached exact JSON, and the extracted attachments replay successfully. No PDF or source change followed those final checks.
