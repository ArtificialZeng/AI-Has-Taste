# Verification Report

**Mode:** Primary-source search verification and exact local-evidence verification.
**Document:** manuscript/main.tex and all publication source files.
**Generated:** 2026-09-13T18:38:52.106919+00:00
**Release job:** primary-20260914-bigdescent-logconcavity-release-6798cd9eec42
**Attempt:** 1; **launch:** 161bd8b8-bc48-4760-813c-25a3fb84ee74.

| Metric | Count |
|---|---:|
| Extracted substantive claim groups | 29 |
| Verified | 29 |
| Numerical errors | 0 |
| Unsupported nearby claims | 0 |
| Hallucinations or misleading claims | 0 |
| Ordinary body citation keys | 4 |
| Selected library entries | 1 |
| Non-library body sources | 3 |

**Overall status:** PASS for the specified manuscript scope. This is a release review, not a new proof of the original conjecture, journal acceptance, or exhaustive priority determination.

## Procedure and exact scope

The requested citation-check-skill and bib-reference-audit were applied in this fresh release context. The user prohibited agents and interactive questions, so every reference was checked locally by this worker. First the entire 473-line manuscript was read and the 29 claim groups were fixed in audit/citation-claim-ledger.json and audit/citation-extraction.md. Only afterward were sources checked. Verification records retain the extraction order and claim text; subsequent ledger changes add only final snapshot bindings. No confidence percentage or audit flag substitutes for mathematical support.

All applicable academic search templates (author/year/title prefix; exact title with arXiv/Semantic Scholar scope; author/year/venue; DOI where supplied; and the accessed KN arXiv identifier) were run. Search outputs were discovery aids. Actual support comes from primary article text, the author manuscript, the textbook draft, and the exact local proof/certificate. The saved web records preserve queries, URLs, results and source locators. The report does not rely on secondary snippets.

## Citation coverage and metadata

| Key | Verified title and version | Source passage | Action |
|---|---|---|---|
| ERZ | [Counting Pattern-Avoiding Permutations by Big Descents](https://link.springer.com/article/10.1007/s00026-026-00805-1); Annals of Combinatorics, version of record, 2 February 2026 | Section 1.2 reverse-complement invariance and Theorem 1.2; Theorems 3.5/3.8 and Lemmas 3.6/3.9; Conjecture 4.6; Section 4.3. Preserved primary text lines 76-97, 351-410, 501-515. | Retained; no key or BibTeX changes |
| KN | [A strong log-concavity property for measures on Boolean algebras](https://arxiv.org/pdf/0907.0243); Journal of Combinatorial Theory, Series A 118(6), 1749-1760 | Author manuscript arXiv:0907.0243v1 (1 July 2009), pages 1-2, equation (1), APP/CAPP definitions, and Theorem 1; browser PDF text lines 46-59. | Retained; no key or BibTeX changes |
| StanleyEC1 | [Enumerative Combinatorics, Volume 1](https://math.mit.edu/~rstan/ec/ec1/); Cambridge University Press, second edition | Second-edition author draft, Section 4.7, Theorem 4.7.1, printed page 573 (PDF page index 572), weighted-walk matrix multiplication; PDF text lines 36098-36106. | Retained; no key or BibTeX changes |
| ZengCertificates | [Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes](https://www.preprints.org/manuscript/202608.1658/v1); Preprints.org, version 1, posted 24 August 2026 | Version 1, Section 6, Certificate Architecture and Reproducibility, HTML lines 207-218, especially the second file-description bullet at line 212; heading/author/version/date at lines 15-58. | Retained; no key or BibTeX changes |

The current titles, authors, years, editions/versions and venues agree with these primary or author-institution records. All four entries are cited; no decorative or unused entries were added. The canonical bibliography is manuscript/references.bib. Exactly one source edit removed the optional Section 6 note from the selected library citation, giving a literal direct citation; its precise Section 6 locator remains in the audit. No theorem, proof or reference identity changed.

**ERZ.** Problem origin and closest enumerative result, including the limited comparison. The source gives the binary-word statistic and univariate enumeration, the original conjecture, and the distinct permutation-set quasisymmetric construction. The third avoidance class follows by the source's reverse-complement symmetry. Online-first journal record supplies no volume or pages; none are fabricated.

**KN.** Closest antipodal-pairs criterion and exact reason its normalization does not prove this result. The binomial normalization and conditional hypothesis are explicit. In dimension two alpha_0=AD and alpha_1=BC up to a common positive factor, so (2,1,1,1) fails APP. The no-internal-zeros hypothesis is retained. Publisher fetch returned a tool error. Journal metadata agrees with the authors' institutional publication record; precise equation/theorem locators were checked in the accessible author manuscript, not claimed to be a newly accessed publisher PDF.

**StanleyEC1.** Natural primary textbook source for the transfer-matrix method. Weighted length-n walk sums are entries of the nth power of the weighted adjacency matrix. The manuscript uses this walk-count interpretation and derives its own suffix transitions and boundary vectors. The author identifies print availability in December 2011 and copyright 2012; the retained bibliography uses the latter. Content was checked in the institutional copy of the author draft.

**ZengCertificates.** Relevant active-library method comparison for certificate/domain separation. A separate verifier reconstructs the complete point/distance/clique/symmetry domain before accepting a stored color certificate. This supports the concrete verification-architecture comparison only, not any geometric result or this manuscript's positivity theorem. The live primary host identifies manuscript 202608.1658, version 1, with matching title, authors and date. The registered DOI is retained unchanged; direct DOI/Crossref/export requests were inaccessible and are recorded separately. No successful DOI resolution or fetched official export is claimed.

The bibliography covers the actual dependencies: ERZ for origin/closest enumeration, KN for the normalized comparison, Stanley for the transfer method, and the library preprint for the concrete certificate architecture. Elementary two-variable Schur and quadratic identities are explicitly derived in the paper. No further outside theorem is invoked without a source. The library minimum is therefore a supplement to three natural non-library sources, not a reference-count ceiling.

The active 49-entry first-sheet registry and manifest were read; the strongest method match is row 9. Its primary version-1 record and full Section 6 were checked independently of registry metadata. The selection binds the exact current registry/workbook hashes and runner attempt/launch. Every verified_at is the actual UTC date obtained with date -u +%F. The smallest citation-bearing sentence at manuscript lines 448-450 is the literal citation_context, excluding the following equation reference. The hook-compatible validate_selection routine passed; the runner-owned pre_publish_hook was not invoked.

No literature/bibliography-revision-*.md, literature/*handoff*.md or literature/crossref-*.json/.md files existed at enumeration. Direct DOI/Crossref and publisher transport errors are retained in the fetch evidence; they were not represented as successful fetches. The cited primary works and the exact nearby support were accessible by the primary/author/institutional URLs above. No fetched official BibTeX export is claimed; accurate existing entries were retained rather than replaced with an invented export.

## Fixed claims and independent support checks

| ID | Status | Exact source/evidence locator | Support and scope check |
|---|---|---|---|
| C01 | Verified (exact) | claim.json exact accepted statement; frozen proof; audit/release-verification.json | All four conclusions and all 695500 certificate positions agree; original problem remains unresolved by this work. |
| C02 | Verified (exact) | manuscript/main.tex event definition, lines 43-55 | Factors end in different bits (0 versus 1); exact-set counts of unattainable sets are zero. |
| C03 | Verified (paraphrase) | ERZ, Sections 1.2, 3.3-3.4; Theorem 1.2; Theorems 3.5/3.8; Lemmas 3.6/3.9 | Exact count-preserving interpretation; reverse-complement handles {123,213}. No position-preserving claim. |
| C04 | Verified (exact) | ERZ, Conjecture 4.6; source.md; claim.json | The source quantifiers agree; 6+binom(6,2)=21. The note is explicitly partial. |
| C05 | Verified (exact) | evidence/research/four-singleton-theorem.md, Exact statement; manuscript equations (1)-(4) | Complementary subsets give symmetry; subtracting adjacent symmetric coefficients in the finite Schur sums gives the displayed expansion. |
| C06 | Verified (exact) | claim.json; evidence/research/four-singleton-theorem.md, matrix theorem and consequences; audit/math.md | The free-site and adjacent-fixed-event block hypotheses are unchanged, including zero cases and unrestricted gaps. |
| C07 | Verified (exact) | evidence/research/four-singleton-theorem.md, Consequences and boundaries; audit/math.md, coefficientwise corollary | No extension to all free-site counts is asserted for the coefficientwise result. The monomial argument fixes squared positions present and unused positions absent. |
| C08 | Verified (exact) | evidence/research/four-singleton-theorem.md, sharp two-position example; audit/release-verification.json:sharp_example | The exact word counts (2,1,1,1) attain AD=2BC. |
| C09 | Verified (interpretation) | KN, arXiv:0907.0243v1 pp.1-2 equation (1), definitions, Theorem 1 | The source premise is normalized; substituting the note's verified counts yields AD=2>1=BC. The source theorem is not imported without its hypotheses. |
| C10 | Verified (paraphrase) | Stanley second-edition draft, Section 4.7, Theorem 4.7.1, p.573 | Weighted-walk interpretation supports the method; the specific matrices are derived in the note. |
| C11 | Verified (exact) | evidence/research/four-singleton-theorem.md, matrix theorem; audit/release-verification.json:structural_checks and direct_words_by_n | All suffix transitions and n=1 initialization checked in source/code and replayed exactly. |
| C12 | Verified (exact) | evidence/research/four-singleton-theorem.md, cone descriptions; manuscript Lemma 4; audit/release-verification.json:structural_checks | Ray coefficients sum to each stated vector with feasible intervals; the four maps preserve the inequalities. |
| C13 | Verified (exact) | evidence/research/four-singleton-theorem.md, matrix theorem; manuscript lines 200-216 | Splitting U_n...U_2 reverses the free-site order, without changing cardinality or complementation; u=o_3 and v=r_2. |
| C14 | Verified (exact) | evidence/research/four-singleton-theorem.md, Exhausting all gap words; audit/release-verification.json:structural_checks | P repetition is removed; a QQ creates the stated admissible cut; all other words are alternating and obey the four displayed recurrences. The separate cones are never pooled. |
| C15 | Verified (exact) | evidence/research/four-singleton-theorem.md, rank-one argument and Schur product identity; manuscript lines 251-267 | Factorization is multiplicative without division. The geometric-sum product identity and m=0,1 cases supply the induction. |
| C16 | Verified (exact) | evidence/research/four-singleton-theorem.md, finite algebraic certificate; manuscript lines 271-284 | Every count is linear separately in every group, hence each product and difference is degree two in each group. |
| C17 | Verified (exact) | manuscript equation (17); manuscript/supplement/verify_certificate.py:check_certificate; audit/release-verification.json | The convolution formula and finite-difference reconstruction have the same quadratic coefficient domain; every stored coefficient is compared, including zeros. |
| C18 | Verified (exact) | audit/release-verification.json:certificate_checks; manuscript Table 1 | Per-order counts, positive counts, zero negatives and the formula N_m match exactly. No rounding or sample extrapolation. |
| C19 | Verified (exact) | manuscript equation (19); manuscript/supplement/verify_certificate.py:polarize_axis/check_certificate; audit/release-verification.json | Mixed finite differences recover coefficients, not sampled signs, and compare all 695500 entries. |
| C20 | Verified (exact) | evidence/research/four-singleton-theorem.md, rank-one induction and consequences; manuscript proof of Theorem 1 | Each cut has fewer sites and invariant boundary cones; splitting at adjacent fixed events proves exactly the accepted larger-block assertion. |
| C21 | Verified (exact) | audit/math.md, Coefficientwise log-concavity and sharpness; manuscript proof of Corollary 2 | Exponent-two sites belong to both factors and exponent-one sites are partitioned. Their even count is at most four; r=0 is a square. |
| C22 | Verified (exact) | audit/release-verification.json:sharp_example | All five displayed words, their event sets, and their four counts match exactly. |
| C23 | Verified (exact) | audit/release-verification.json:generic_face_bound_counterexample_verified; verifier final loop | All six faces have AD=2BC; complementary rank sums are (4,3,3,4) and middle difference -1. The example is explicitly outside the word model. |
| C24 | Verified (exact) | claim.json exact scope; manuscript Theorem 1 and scope paragraph | There is no claim of an unrestricted free-site theorem or optimality of the cutoff. |
| C25 | Verified (paraphrase) | ERZ, Section 4.3, quasisymmetric definition; preserved primary text lines 503-515 | The cited source encodes permutation big-descent sets in fundamental quasisymmetric functions. The note's distinct word-event antipodal construction is explicit; no exhaustive novelty assertion. |
| C26 | Verified (exact) | manuscript/supplement/verify_certificate.py complete source; audit/release-verifier.log | Inspected all imports and calculation loops, then executed the packaged command successfully. Arrays use object dtype and Python integers. |
| C27 | Verified (paraphrase) | Zeng et al., version 1 Section 6, HTML lines 207-218, especially 212 | The exact primary passage supports reconstructing a full finite domain independently before accepting stored certificates. This is a natural method comparison, with no borrowed geometry claim. |
| C28 | Verified (exact) | audit/release-verification.json:direct_conditional_configurations, direct_Schur_positions, direct_LC_monomial_positions_n_le_10 | Fresh totals are 198399, 433405, 383073; loops cover n<=12 for word/Schur checks and n<=10 for LC monomials. Uniformity still relies on the proof. |
| C29 | Verified (exact) | frozen proof finite-certificate section; audit/math.md independent implementation; packaged verifier source; job provenance | The disclosure matches the documented convolution/tensor/finite-difference work. No formal-assistant or external-peer-review claim is made; release replay is distinguished from the accepted referee pass. |

## Mechanical and rendered checks

The clean latexmk/BibTeX build succeeded. The final LaTeX/BibTeX logs contain no undefined citations, undefined references, database omissions, duplicate entries, fatal errors, or box warnings. The independent key checker reports four source keys, four BibTeX entries and four matching aux keys, with no missing or unused keys. The active-TeX parser produces the same four-key set as the ledger union. All six declared publication source files were inspected for their role; recorder input analysis confirms local TeX dependencies, and the package lists the bibliography plus all stable supplementary inputs. Generated aux/output/run reports are not omitted publication inputs.

The packaged verifier was actually run: all 695500 coefficient positions and exact finite word totals match. Its fresh report is audit/release-verification.json. The certificate is byte-identical to the accepted frozen certificate. All seven PDF pages were rendered and actually viewed; the two tables were compared value by value with the fresh exact report. Separate build and visual reports bind the same final snapshot. The accepted mathematics, source.md, checkpoint.md, claim.json, and every mathematical-snapshot input remain unchanged.

Bindings: manuscript 3f64ca522fd169f4ca3d495053659c8d7b5d4c5f0eb4fc967511df2c6afb9e19; PDF ec4f98a71460aa42d3b61faef3e570137f0d841c82b63db1b60b60dbfad3389c; mathematical snapshot eb53a91aae391332997c181abb1a6520595e81df64ebfc2f9344d940702e1155.
