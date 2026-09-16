# Verification report

**Mode:** Two-pass noninteractive search verification, with accepted local proof and exact computation records for original mathematical claims.
**Document:** manuscript/main.tex and its canonical bibliography.
**Generated:** 2026-09-13T14:05:45.025420+00:00. **Release job:** `primary-20260913-ascent-0120-0121-release-fadb0e167fc3`.

| Metric | Count |
|---|---:|
| Claims extracted | 27 |
| Claims supported at their stated scope | 27 |
| Retained references verified | 9 |
| Numerical errors | 0 |
| Unsupported citation claims | 0 |
| Selected library references | 1 |
| Natural non-library references | 8 |

**Overall status:** PASS for the current release scope. Full later-literature overlap and worldwide priority remain explicitly unestablished.

Pass 1 read the entire canonical manuscript and froze all 27 numbered claims and all nine ordinary citation keys in `audit/release-recovery-extraction.json` before fresh source verification. Exact excerpts were regenerated from current lines. Pass 2 used that fixed inventory; source locators and individual findings are in `audit/primary-source-locations.json` and `audit/citation-verification.json`. The clean build changed only the PDF binding; no claim was added, removed, or re-extracted during verification.

The selected library item is row 9 from the exact active 49-entry first-sheet registry. Its primary Section 6 supports the nearby comparison of reconstruction from definitions with a separate exact implementation. The compact selection context is exactly the single citation-bearing sentence at lines 343–345. The installed hook-compatible `validate_selection` passed with attempt 2 and launch UUID `71e63e1d-c09c-44e3-aa51-faa0c729295e`. The runner-owned pre-publication hook was not invoked.

The complete ordinary body key set equals the ledger key union and the nine BibTeX entries. No comment-only citation, nocite, inert macro, verbatim citation, hidden conditional, or renamed library identity supplies coverage. The eight non-library citations are identified by their actual DOI/record identities. None of the nine citations is decorative; their distinct uses follow.

| Key | Actual nearby use and checked source passage | Primary source |
|---|---|---|
| BMC2010 | Origin of the objects and their poset connection. Author preprint v4: page 1 abstract/introduction, page 3 Section 2 definition; institutional publication record and its BibTeX. | [(2+2)-free posets, ascent sequences and pattern avoiding permutations](https://arxiv.org/pdf/0806.0666) |
| DS2011 | Foundational attribution of pattern avoidance in ascent sequences. Publisher PDF page 1, title/byline/publication date, abstract and Section 1; publisher landing page DOI. | [Pattern avoidance in ascent sequences](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v18i1p226/pdf/) |
| LKZ2026 | Problem origin, closest checked benchmark and the RGF restriction on its shorter-pattern reduction. Version/date/byline, Section 1 Table 1 exact-pair row (HTML line 110), Lemma 2.2 (lines 146–148), Section 6 (lines 566–568). Frozen original HTML is evidence/external/liu-kitaev-zhang-2604.06735v1.html. | [Simultaneous avoidance of length-4 patterns in ascent sequences](https://arxiv.org/html/2604.06735v1) |
| Banderier2002 | Attribution of the generating-tree framework. PDF page 1 publication note, byline, abstract and introduction; page 2 succession system (1). arXiv journal reference and related DOI. | [Generating functions for generating trees](https://arxiv.org/pdf/math/0411250) |
| Stanley2012 | Transfer-matrix method used to assemble the finite systems. Author-hosted second-edition draft, Section 4.7.1: adjacency definition, Theorems 4.7.1–4.7.2; PDF pages 573–574, web lines 36068–36138. Publisher-indexed record lists 5 June 2012 electronic and 12 December 2011 print publication. | [Enumerative Combinatorics, Volume 1](https://math.mit.edu/~rstan/ec/ec1.pdf) |
| Zeng2026 | Specific reconstruction-and-separate-exact-implementation comparison; the one selected user-library record. Primary title/byline/version/date block; Section 6, second and fourth bullets and concluding implementation paragraph (HTML lines 207–219). | [Exact Finite Certificates for the Four-Dimensional Ternary Borsuk Problem and Five-Dimensional Ternary Kissing Codes](https://www.preprints.org/manuscript/202608.1658) |
| SymPy2017 | Attribution for the symbolic software used in the recorded computation. Author-maintained paper repository README: publication citation, full official BibTeX, author list and abstract. Publisher-indexed PDF page 1 confirms metadata. | [SymPy: symbolic computing in Python](https://github.com/sympy/sympy-paper) |
| MS2025 | Comparison with the neighboring extra-021 class. Version-1 landing-page date and authors; PDF page 1 abstract, lines 15–16; introductory class definition on pages 1–2. | [On ascent sequences avoiding 021 and a pattern of length four](https://arxiv.org/pdf/2507.17947v1) |
| Mansour2026 | Honest disclosure of a potentially relevant later paper and the remaining overlap-screen limitation. Publisher-indexed title/byline/date/abstract; author publication list entry 558. Direct publisher open returned Internal Error. | [0132-Avoiding Ascent Sequences](https://www.mdpi.com/2073-8994/18/7/1174) |

Every existing author/title/year/version/venue/DOI or arXiv identity was compared with the named primary record. The SymPy author list was compared with the author-maintained official BibTeX. No `.tex` or `.bib` source was changed; no BibTeX entry was replaced and no key changed. The journal metadata for BMC2010 were available from its author institution; Banderier2002 follows the PDF author order; Stanley2012 uses the publisher’s electronic-edition year. Available official export data were checked without gratuitously reformatting correct existing entries.

Applicable author/year/title, exact-title/database, author/year/venue, DOI, and explicit arXiv queries were run for all retained records. Additional exact-pair, eligible-rank and initial-count searches were bounded checks only. Search snippets from aggregators were discovery leads, never authoritative support. One mistyped Duncan preprint URL returned an unrelated solar-flare paper; it was rejected and replaced by the correct primary publisher PDF and arXiv:1109.3641. See `audit/release-recovery-search-provenance.json`.

The nine-reference coverage is adequate for the actual paper: original objects and pattern avoidance, exact April benchmark, generating trees, transfer matrices, neighboring restricted classes, exact verification design and symbolic software. The proof itself is self-contained and does not need additional substantive theorems. The source dependency set is exactly the four sorted files in publication.json: main.tex, references.bib, coefficients.py and README.md. TeX recorder inputs and the BibTeX log show no unlisted authored TeX, local style or figure. System packages, Latin Modern fonts and plainurl.bst are standard dependencies.

All finite count and coverage assertions were traced to the accepted research and referee records. The publication program was freshly run through degree 28 and all 29 coefficients match both accepted records; all 17 table entries were also read on rendered page 5. The two short word witnesses were checked directly. This is release verification of statements and implementation, not a new all-length proof or mathematical acceptance.

The later Mansour paper is identified by the indexed primary publisher record and the author’s publication list. Direct full-text retrieval failed. Indexed passages mention additional 0120 work and therefore do not justify a nonoverlap conclusion. The changes in the 021 journal version were not compared. These limitations are printed on page 6. No source-access failure was used as evidence of novelty, falsehood or resolution. The empty Crossref-capture enumeration was checked before reporting failed access; no saved authoritative Crossref response was ignored.

No agents or parallel model reviewers were used because the user explicitly prohibited them; the citation keys were verified in this release context. The noninteractive fixed-ledger workflow follows the user’s override of the skill’s confirmation step.

The main skill, release.md, release-contract.md, both requested citation skills and AGENTS.md were actually read in full in separate top-level tool results before auditing. Their factual read record is `audit/release-instruction-reads.json`; the detailed account is `audit/release-recovery-report.md`. The prior job’s missing read is not retrospectively asserted.

The fresh clean build and all seven native-image page inspections passed; see `audit/build.md` and `audit/visual.md`. Final release consistency remains subject to the immediately following official release_gate.py check.
