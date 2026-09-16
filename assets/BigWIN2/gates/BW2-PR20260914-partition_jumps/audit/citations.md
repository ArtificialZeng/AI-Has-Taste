# Verification Report

**Mode:** Search verification plus frozen-dossier checks and exact finite replay. **Generated:** 2026-09-14T02:11:48.293536+00:00.
**Document:** manuscript/main.tex and manuscript/references.bib. **Job:** primary-20260914-partition-jumps-release-53b5e2a5c417.

**Overall status: PASS within the accepted result-note scope.**

| Metric | Count |
|---|---:|
| Extracted and checked claims | 42 |
| Citation-bearing claim groups | 9 |
| Direct body citation occurrences | 11 |
| Bibliography records | 7 |
| Numerical errors, unverified or unsupported claims | 0 |

Pass 1 read the entire canonical TeX and verifier, matched the old index to every current claim, and froze the resulting 42-claim extraction before source verification. Pass 2 used that fixed list in C01-C42 order. The final ledger only refreshes the PDF/snapshot binding after a clean rebuild; its claims equal the frozen extraction. Definitions and assistance acknowledgments were excluded under the extraction rules. No interactive confirmation or delegation was used because the user explicitly required a non-interactive, single-worker job.

The current research digest is `fce4053e5a3907860b747c9542daeb32f9d40fbb83dae61c32423ee9941797aa`; manuscript digest `6a77b9ab481ab6d3d7560adb2a14429616d35e351ddc1b733579ad606bd36ea0`; PDF digest `407292477df86d3d20d3536ae5001cbe99c2ba30ebd67f2214dffa3be1a8a451`. These are audit bindings, not mathematical evidence.

## Citation-to-source verification

| Key | Nearby claim and exact primary location | Decision |
|---|---|---|
| LyudogovskiyMorphology | C01, C04, C08: Graph convention and original local-dimension formula. [Local Morphology of the Partition Graph](https://arxiv.org/html/2603.18696v1), Section 2, HTML lines 66-112; Lemma 3.1, lines 180-223; Theorem 7.1, lines 518-576; Proposition 3.7, lines 304-320 | Verified; metadata and support match; no BibTeX replacement or key change. |
| LyudogovskiyJumps | C02: Immediate problem origin and exact residual scope. [Jump and Gradient Invariants in the Partition Graph](https://arxiv.org/html/2605.28981v1), Section 8.6, Problems 8.1 and 8.2, HTML lines 2239-2258 | Verified; metadata and support match; no BibTeX replacement or key change. |
| LyudogovskiyStratification | C03: Earlier origin of the uniform-bound question. [Simplex Stratification and Phase Boundaries in the Partition Graph](https://arxiv.org/html/2603.23228v1), Problem 6.4(iii), HTML lines 642-664 | Verified; metadata and support match; no BibTeX replacement or key change. |
| LyudogovskiyDegree | C04, C06, C07: Imported degree formula and closest-prior-result comparison. [Degree theory of the partition graph: exact maxima, profiles, and fibres](https://arxiv.org/html/2603.27248v1), Section 2, HTML lines 115-133; Theorem 2.2, lines 190-224; Abstract and introduction: maximum vertex degree and maximizing profiles | Verified; metadata and support match; no BibTeX replacement or key change. |
| LyudogovskiySupport | C05: Attribution of known support-change facts. [Support and Support Jumps in the Partition Graph](https://arxiv.org/html/2604.11837v1), Theorem 3.4 and Corollary 3.5, HTML lines 253-270; transfer conventions, lines 218-250 | Verified; metadata and support match; no BibTeX replacement or key change. |
| LyudogovskiySynthesis | C08: The reproduced capacity formulation and boundary conventions used in the proof. No global topology theorem is borrowed. [Local Complexity, Overlap Control, and Global Simplicity in Partition Graphs: A Conceptual Synthesis for G_n and K_n = Cl(G_n)](https://arxiv.org/html/2606.20773v1), Background Proposition 3.1, HTML lines 389-413 | Verified; metadata and support match; no BibTeX replacement or key change. |
| ZengFiniteCertificates | C09: A directly relevant exact-clique verification comparison, selected from active library row 9. [Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes](https://www.preprints.org/manuscript/202608.1658/v1), Publisher version 1 title/authors/posting block, HTML lines 15-58; Section 4, Lemma 3, HTML lines 169-184; Proposition 1 certificate proof, lines 187-195; Publisher Computational Mathematics listing, lines 298-323: exact title, authors, posted date, DOI | Verified; metadata and support match; no BibTeX replacement or key change. |

Every retained entry has a substantive nearby use. Six non-library primary papers cover the graph convention, the two problem origins, degree maxima/formula, original dimension capacities, support accounting, and the later boundary-convention reproduction. The synthesis is cited explicitly as a reproduction alongside the original theorem, not as its origin. The elementary support arguments and complete literal-subset verifier are supplied and justified in the paper; they do not depend on an uncited specialized clique algorithm. No extra general references were added for a count.

The sole gate-bound library selection is active first-sheet row 9. All 49 titles were screened, with the related exact-certification candidates inspected in the registry. Row 9 provides the natural integer-compatibility/two-clique-implementation comparison, limited expressly to its finite ternary library. Its title, four authors, version and 24 August 2026 posting date match the publisher article; its DOI matches the publisher Computational Mathematics listing, lines 298-323. Registry metadata was only a selection lead.

The selection uses attempt 2 and launch UUID `7bdc96b2-2f52-44fc-b888-9c7d813aad81`, a freshly generated dynamic registry binding, and the actual UTC date from `date -u +%F`. The smallest active citation-bearing sentence at main.tex:355-358 is literal and excludes unrelated TeX commands. The installed hook-compatible validator passed; see `audit/selection-validation.json`. The configured pre-publication hook was not invoked.

All applicable academic templates were run for each retained source: author/year/title opening; full title with the specified discovery domains; author/year/venue; and each present DOI or arXiv identifier. Search responses and exact original article passages are saved under `audit/release-53b5e2a5c417/`. Final authority comes from arXiv and the publisher, never secondary snippets. No Crossref captures exist under literature/crossref-*.json or literature/crossref-*.md; no source was declared unavailable. Existing BibTeX was verified field by field and retained rather than represented as a newly downloaded export.

## Mathematical and numerical scope

The main statements, boundary cases, witnesses, proof steps and exclusions were compared with claim.json, the frozen proof and accepted math report. The report in `audit/citation-verification.json` checks each extracted claim individually, with a source locator and evidence path. Original claims are assessed against the accepted proof, not passed merely because a citation exists. No theorem or source was strengthened. The original qualitative localization question, exact all-n degree function and optimal additive constants remain outside the conclusion.

The complete printed verifier was executed and matched all 12 table rows, covering 371 vertices and 1,084 edges. Each rendered table integer was also read on page 4. The appendix listing is byte-identical to the executed script. The referee code/results through n=24 support the manuscript account of the earlier separate computation; this release did not rerun that larger range. Finite evidence is not an infinite proof.

The limited novelty sentence remains limited: the cited preprints and frozen comparison were checked, and four additional targeted live queries returned no results. This supplies no worldwide priority guarantee and does not exhaust Gray-code, dominance-lattice or nonindexed literature. The alternative first-layer staircase lead in the supervisor handoff is a different target and is not used as a new result or an established theorem.

## Bibliography, build and dependency coverage

All seven ordinary body keys equal exactly the union in the ledger and the canonical bibliography; the final AUX has exactly the same seven resolved entries. The installed bibliography checker passed with no missing, unused or extra keys. Comments, verbatim code and inert macros supplied no evidence keys. No .tex or .bib edit or key mapping was needed.

The publication dependency list was checked against the complete source and the compiler .fls inputs: main.tex, references.bib, generated main.bbl (explicitly frozen), build.py and verify_small.py. AUX/OUT files are clean-build outputs; all style/font dependencies are installed system packages. There are no omitted imported TeX files, local custom styles or figures. `sources_checked` is the sorted exact publication source_files list.

The clean project build ran pdflatex, BibTeX and two final pdflatex passes successfully; final logs have no fatal, undefined-citation/reference, duplicate-entry, overfull/underfull or LaTeX-warning diagnostics. All seven references were read in the rendered final page and agree with the canonical entries. Separate build and seven-page visual reports bind the same snapshot. Publication activation and the runner hook remain runner-owned.
