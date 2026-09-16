# Verification Report

**Mode:** Search for primary citations; doc-only scope comparison against the accepted mathematical dossier.
**Document:** `manuscript/main.tex`, `manuscript/references.bib`, their declared ancillary sources, and the final six-page PDF.
**Generated:** 2026-09-13T15:19:31.424787+00:00
**Release job:** `primary-20260913-king-odd-staircase-release-83d20eee6b85`.

| Metric | Count |
|---|---:|
| Fixed extracted claims | 33 |
| Verified at the asserted scope | 33 |
| Retained bibliography entries | 5 |
| Unsupported or misleading retained claims | 0 |
| Numerical discrepancies | 0 |

**Overall status: PASS at the stated scope.** The exact original result remains mathematically accepted as `resolution-paper` / `proved`. This release audit does not certify priority, current openness elsewhere, external peer review, or a formal proof of the entire theorem. The later SSRN full text remains uncompared; its citation supports only the existence of that posting.

## Two-stage audit and dependency scope

The complete manuscript was read and the 33 claim records were saved before checking primary support. The user required a non-interactive audit and explicitly prohibited delegation; no agents or background workers were used. Verification then followed the fixed IDs in order. Minor citation and formatting repairs preserved the set of claims and line locations; their final literal contexts and source hashes are frozen in `citation-claim-ledger.json`. `release-claim-verification.json` records each finding against that exact ledger hash. Definitions and assistance/process disclosure were excluded from factual extraction under the citation skill’s rules, but the disclosure and theorem scope were inspected.

The ledger's key union equals all five ordinary body-flow keys. Every retained entry is used directly in body prose; no comment, hidden conditional, inert macro, verbatim block, or nocite supplies coverage. `release-selection-validation.json` records successful validation with the installed hook-compatible library validator and actual UTC date. The runner-owned pre-publication hook was not invoked.

All four declared publication sources were read: `manuscript/REPRODUCE.md`, `manuscript/main.tex`, `manuscript/references.bib`, and `manuscript/reproduce.py`. The recorder and BibTeX log show no undeclared authored compile dependency; the other local inputs are generated AUX/OUT/BBL files. Styles and fonts are installed TeX packages. The reproduction guide identifies the already accepted exact scripts and excludes the incomplete historical triage holdout. No accepted mathematical input was edited.

## Citation correctness and bibliography coverage

| Key | Verified primary record and location | Needed nearby use |
|---|---|---|
| `gkm2025` | [Impartial Chess on Integer Partitions](https://arxiv.org/html/2501.14640v1); Section 2.1; Definitions 2.1/3.1; Theorem 3.8; Lemmas 3.13/3.14; Conjecture 5.1. DOM IDs S2.SS1.p4, S2.Thmtheorem1, S3.SS1.p2, S3.Thmtheorem1, S3.Thmtheorem8/13/14, S5.Thmtheorem1. | Exact unit moves, nonempty destinations, original conjecture, and closest rectangle/ordinary/even-block cases. Berlekamp is explicitly an attribution by this source. |
| `sprague1935` | [Über mathematische Kampfspiele](https://www.jstage.jst.go.jp/article/tmj1911/41/0/41_0_438/_pdf); Printed pages 439–440 (PDF pages 2–3), Section 6, Satz I and its proof. Web text lines 48–72. | Ranks are assigned by the least missing nonnegative successor rank in games of bounded play length; finite partition games meet this hypothesis. |
| `gkmssrn2025` | [Impartial Chess on Integer Partitions](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5649443); Primary-host search-indexed landing record: title, authors, 31 pages, posting date, and suggested citation. | Existence of a later posting, solely to identify the exact boundary of the literature comparison. |
| `demoura2008` | [Z3: An Efficient SMT Solver](https://link.springer.com/chapter/10.1007/978-3-540-78800-3_24); Primary abstract and About this paper; independently matching authors’ Microsoft Research record, abstract. | Identifies Z3 as an SMT solver. The 14 runs and unsat results are supported by local computation evidence, not attributed to the 2008 paper. |
| `zeng2026finite` | [Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes](https://www.preprints.org/manuscript/202608.1658); Section 4, Lemma 3 and Proposition 1 certificate proof; Section 6 independent implementation; Section 7 finite-library limits. Official subject index lines 298–323 binds the title, four authors, date and DOI. | Exact integer predicates, separately implemented verifiers, and the specific finite scope supply the nearby methodological comparison. No geometric theorem is used in the King proof. |

Five entries were verified, with no key renaming and no wholesale BibTeX replacement. `references.bib` gained the primary-verified library DOI and protection of the German noun’s capitalization. `main.tex` now uses a direct selected cite, spells out “Section” in the Sprague locator, and uses standard article section numbering. These are metadata/formatting changes only. The final BBL and rendered bibliography have the five expected references and correct authors, dates, versions and identifiers. The selected paper is explicitly marked as not peer reviewed.

The Microsoft and Springer official BibTeX export links were discovered, but the web parser rejected their content type and local network downloads were denied. No export text was invented. The already supported records were retained, with only independently established field/format corrections. These export limitations leave no unsupported retained attribution; the actual original Sprague passage, GKM statements, Z3 primary abstract, and library full-text passages were received and inspected. The official Preprints.org subject index independently binds the selected title and four authors to its DOI and posting date. Direct DOI/Crossref transport failure is not used to negate that primary record. Before recording failures, all project `crossref-*.json`/`crossref-*.md` leads were enumerated: none existed.

The bibliography has one gate-bound library selection and four natural non-library sources, identified by publication identity rather than key spelling. GKM supplies both the original problem and closest relevant results; Sprague supplies the foundational mex rule; de Moura–Bjørner identifies the verification method; the later GKM posting documents the qualified literature boundary. The library comparison concerns exact predicates, separate implementations and finite scope, which directly explain the role and limits of this paper’s computations. It imports no geometric result. No fixed bibliography quota was used and no decorative source was retained. Berlekamp’s rectangle result is explicitly attributed through GKM, whose theorem and a self-contained proof are provided; no unseen video is claimed as verified.

All 49 active first-sheet records were screened by title and identifiers, with full nearest-method records for rows 9, 11, 19 and 20 examined. Row 9 is the single supported selection. Row 11 has a closer phase-dynamics theme but the bounded primary searches supplied no verifiable matching record; it was not cited. Rows 19 and 20 concern more remote SAT/LRAT reductions. Additional unrelated papers would not improve the actual claim support. The selection has the dynamic checksum/sheet/count binding and runner-issued attempt 1 and launch UUID; it is a minimum selection, not a cap on useful sources.

## Verified claims

| ID | Primary or accepted source location | Finding |
|---|---|---|
| C01 | Accepted claim.json; proof.md statement and Sections 1–6; GKM v1 Conjecture 5.1 | Universal formula and proof scope agree; later-text limitation appears in abstract and introduction. |
| C02 | GKM v1, Section 2.1 and Definitions 2.1/3.1; release-primary-extract.txt | Subpartition removes trailing nonpositive parts; exactly the three unit moves; destinations must be nonempty. |
| C03 | Sprague, printed pp. 439–440, Section 6, Satz I and proof | Bounded play length is the relevant hypothesis. The rank is the least missing nonnegative successor rank; translated from German. |
| C04 | Accepted proof.md statement/dependencies and Section 2 | Each move strictly decreases cells. At most three successors imply mex at most 3, with terminal value 0. |
| C05 | claim.json statement; proof.md conclusion | Every positive odd r and every positive k retained. All three residue cases agree. |
| C06 | GKM v1 Conjecture 5.1, Theorem 3.8, Lemmas 3.13/3.14 | All cases agree; positive-k use avoids the source’s empty-staircase endpoint. Berlekamp attribution is expressly to this source. |
| C07 | Accepted proof.md versus GKM v1 Sections 3.4/5 | Comparison is bounded to v1; universal odd-block argument and boundary/interior formulas are supplied in full. |
| C08 | SSRN official-host indexed record, 5649443; web-identifiers.json | Same title/authors, posted 23 October 2025. Metadata only: the manuscript explicitly discloses the uncompared text. |
| C09 | proof.md statement and Sections 3–6 | Five W cases agree. Substitution r=3,k=1 and k=6 gives (0,3,0) and (0,2,0). |
| C10 | proof.md Section 2 | Transposition swaps the two axial options and preserves the diagonal; finite induction gives conjugate invariance. |
| C11 | proof.md Section 2, displayed shape and edge identities | All block deletions and k>=2/k>=3 domains match; these are shape identities, not new moves. |
| C12 | proof.md Section 2, final paragraphs | Absent corner is only at k=2; descending induction is finite and every first-square cell exists. |
| C13 | proof.md Section 1, three tables and equation (1) | All twelve matrix entries and the F(L,L)=2 override match. Lemma’s nonnegative domain and both high assignments are unchanged. |
| C14 | proof.md Section 1, ordinary case table | The four triples and two diagonal cases match entry by entry, and T/C reductions have the same conditions. |
| C15 | proof.md Section 1, exceptional tables and exhaustive division | All cases, feasibility restrictions and threshold-0/1 treatment agree. |
| C16 | proof.md Section 1, ten-row seam table; final PDF page 4 | Every region condition, parity, current value and triple compared against the accepted table; no discrepant cell. |
| C17 | GKM v1 Theorem 3.8; proof.md Section 3 | The four rectangle cases and positive side-length hypothesis agree exactly. |
| C18 | proof.md Section 3, base path and six option sets | Unit-side path and all displayed finite successor sets match; this establishes the base without relying on an external proof. |
| C19 | proof.md Section 3, last paragraph | Odd r gives the 0/3 boundary by even/odd j. F is not asserted at k=1. |
| C20 | proof.md Section 4, edge formula | Threshold shifts to L+1; inequality s<=L and all four parity values agree. |
| C21 | proof.md Section 4, corner paragraphs | t>=3 gives x; t=2 gives 2 when the corner exists. The conditions are retained. |
| C22 | proof.md Section 4, k=2 paragraph | Both {0,2} and {0} have mex 1; r=1 retained and no empty position assigned a value. |
| C23 | proof.md Section 5, first two paragraphs | Wrap threshold L=r+1 and phase reversal agree; only the two endpoint values may differ. |
| C24 | proof.md Section 5, h cases | h=1 agrees directly; h=0 changes endpoints only and preserves mex of (2,2,1), also at r=1. |
| C25 | proof.md Section 6 | Full first-square formula is only at k>=2, followed by base-plus-induction for W. |
| C26 | proof.md statement and Section 6; claim.json | Root extraction t=p versus other t is exactly the frozen residue formula. |
| C27 | proof.md dependencies and Sections 1–6; verifier source functions | No computational premise occurs in the argument; the game evaluators use exact integers. |
| C28 | audit/referee-verify.py lines 200–225; saved JSON; release-computation-check.json | All coverage pairs match; counts recomputed arithmetically as 136, 27,464,908, 26,800, 245. Saved rows and no-failure record agree. |
| C29 | de Moura–Bjørner, primary abstract; referee SMT source and outputs | Z3 identification matches the primary abstract. The query count and domain come from local artifacts, not the citation. |
| C30 | audit/referee-verify.json and its 14 hashed SMT files; release-computation-check.json | All 14 saved files were freshly replayed and returned unsat. The manuscript keeps whole-proof certification outside this encoded scope. |
| C31 | Zeng et al., Sections 4 and 6; primary text | Lemma 3 gives an integer predicate; Proposition 1 and Section 6 describe a separate implementation. This is a relevant verification-method comparison. |
| C32 | Zeng et al., abstract and Section 7; accepted King proof | The cited scope is finite ternary libraries. King evaluations are explicitly finite corroboration of a separate universal proof. |
| C33 | audit/referee-verify.json python/z3_version; proof.md statement | Exact recorded versions are 3.10.12 and 4.15.3; no claim about unequal blocks or other movesets. |

## Search and access evidence

Applicable templates were run without stopping at the first hit. GKM searches included author/year/first title words; full title with the arXiv/Semantic Scholar domain template; author/year/arXiv and SSRN venue terms; `arxiv:2501.14640`; and `doi:10.2139/ssrn.5649443`. Sprague searches covered author/year/title, full-title domain template, and Tohoku venue terms. Z3 searches covered de Moura/2008/title, full-title domain template, TACAS, and its DOI. Library searches covered Zeng/2026/title, the full-title domain template, Preprints venue terms, and the exact DOI. Optional row-11 searches used the same four templates and yielded no matching primary passage. Secondary results were discovery only. Primary retrieval and search responses are preserved under `release-sources/`; no secondary summary establishes a retained claim.

The live arXiv record shows v1 dated 24 January 2025. The SSRN-host indexed record shows the later posting dated 23 October 2025, but its full text was not available for comparison. This restriction remains explicit in the abstract and introduction. No assertion of current openness or first-proof priority is made. The numerical observations are verified against their actual saved rows and specified domains; the existing fourteen query files were replayed without modifying them. That replay checks the encoded identities, not the complete written induction.

## Build and rendered output

A clean latexmk/BibTeX build converged with no final undefined citation, cross-reference, duplicate/missing bibliography entry, fatal diagnostic, overfull/underfull box, or layout warning. The installed `check_bib_keys.py` reports five source, bibliography and AUX keys with no missing or extra key. All six final pages were viewed as rendered images, including the symbolic tables and complete bibliography. See `build.md`, `visual.md`, `release-bib-key-check.txt`, and the current manuscript snapshot.
