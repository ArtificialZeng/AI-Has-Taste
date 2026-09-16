# Verification Report

**Mode:** two-stage, non-interactive primary-source verification and accepted-proof
transcription review. **Document:** `manuscript/main.tex` and its sole canonical
bibliography, `manuscript/references.bib`. **UTC date:** 2026-09-12.
**Job:** `primary-20260912-stack22-mechanism-release-bd956129f546`.
**Citation attempt:** 1. **Launch:** `1273ecce-d946-461e-aa47-fcaeaaca42d9`.

| Metric | Count |
|---|---:|
| Final extracted claims | 36 |
| Verified at the stated scope | 36 |
| Ordinary body citation instances | 8 |
| Distinct cited works | 6 |
| Selected user-library works | 1 |
| Non-library primary/method works | 5 |
| Undefined, decorative or unsupported retained citations | 0 |
| Numerical errors, misleading claims, unverifiable retained claims | 0 |

**Overall status: PASS.** This accepts citation support, bibliography coverage
and manuscript scope; mathematical acceptance remains the frozen `audit/math.json`.

## Extraction and verification order

The initial entire-paper extraction was saved before primary verification as
`audit/citation-extraction-initial.json`. Initial verification identified a missing
DOI in the selected library entry. The final extraction in
`audit/citation-claim-ledger.json` contains 36 substantive statements with unique
IDs, locations, types and direct keys; it was frozen after the scope-preserving
repairs. A separate pass checked those fixed statements, with per-ID results in
`audit/citation-verification.json`. Definitions, methodology disclosures and
acknowledgments were excluded from factual claim extraction as the skill requires;
the computational disclosure was nevertheless checked against the actual files.
No interactive confirmation was sought, as expressly instructed.

The hook-compatible parser, without invoking the hook, confirmed the exact
ordinary-flow key set and registry-bound selection. None of the eight citations
is supplied by a comment, inactive macro, hidden conditional, footnote or nocite.
The selected reference uses the direct `\cite{ZengEtAl2026}` form in Section 6.
Its context is the smallest complete citation-bearing sentence, excluding the
preceding local-verifier sentence and following comparison sentence.

The three prescribed skills were read and applied by this single worker.
No agent delegation was used because the user explicitly prohibited it.

## Claim-to-primary-source audit

| Key and claim IDs | Exact source locator | Support and limits |
|---|---|---|
| Atkinson1998; C02 | Publisher abstract; author PDF p. 1 definition and pp. 7–8, Theorem 4 | The same first-r insertion/first-s removal model and the eight-pattern characterization. The author version numbers the theorem 4; Vatter's journal locator is 4.1. Neither is silently substituted for the other. |
| Vatter2026; C03, also attribution in C05/C36 | arXiv v2, Section 5, Theorem 5.9 and the paragraph immediately before Problem 5.11; Problem 5.11 itself | The exact basis, attribution to Pantone of a basis-derived cubic using Combinatorial Exploration, and the remaining request for a mechanism derivation. Pantone's private computation was not inspected and is not represented as inspected. |
| AlbertEtAl2026; C04/C20 | Author manuscript v3, Section 3.3; Section 4.1, Definition 4.1 and Theorem 4.1; Section 5.2 | Specifications yield counting relations and, with suitable transfers, generating-function equations. Productivity is explicitly treated. The paper does not claim every arbitrary specification is productive; the present manuscript proves its own decreasing-size recurrence. |
| FlajoletSedgewick2009; C19 | Authors' book site, Chapter 1 description and Chapter I.1–I.2 contents | The authors identify construction-to-generating-function transfer as the symbolic method. The actual sum/product translation here is elementary and displayed in the present proof; it is also explicit in the inspected Albert et al. Sections 3.3 and 5.2. No deep analytic transfer theorem is imported. Full-book and lecture-PDF retrieval exceeded/accessed tool limits; no full-book passage inspection is claimed. |
| OEIS393395; C07/C27 | A393395 internal fields S/T/U, N, C, F, O and A | The original-author record gives the model, offset zero, the cubic and the displayed coefficients. It is calibration only, not evidence for the new all-size grammar or for exhaustive test coverage. |
| ZengEtAl2026; C24 | Publisher version 1, Section 4, Proposition 1, Certificate proof; Section 6 | The first exact implementation uses bitsets; a separate list-based implementation reconstructs the graph independently. This supports precisely the stated verification-method comparison. The citation does not transfer any Borsuk/kissing bound into stack sorting and is not an all-size proof dependency. |

Author/title/year/version checks used the following actual primary records:

- [Atkinson publisher record](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/abs/generalized-stack-permutations/9BFFBAAD479417994250012D5835EE02): M. D. Atkinson, 1998, *Combinatorics, Probability and Computing* 7(3), 239–246, DOI 10.1017/S096354839800354X. The [author publication index, item 55](https://www.cs.otago.ac.nz/staffpriv/mike/HomePages/oldpublications.html) links the [author PDF](https://www.cs.otago.ac.nz/staffpriv/mike/Papers/Genstack/Genstack.pdf). Its local bytes match the handoff SHA256; physical pages 1, 7 and 8 were freshly rendered and actually viewed. Its decreasing-top-pair rule differs from the present rule: no attribution of the present normalization is made.
- [Vatter arXiv v2 record](https://arxiv.org/abs/2602.16355v2) confirms title, author and registered revision date 25 February 2026; the [inspected v2 text](https://arxiv.org/html/2602.16355v2#S5) carries a separate internal manuscript date. Neither date is replaced by the other. Its frozen HTML agrees on the relevant passages.
- [Albert et al. author manuscript](https://arxiv.org/html/2202.07715v3) and [version record](https://arxiv.org/abs/2202.07715) identify six authors and v3 dated 15 October 2024. The [University of Otago publication record](https://ourarchive.otago.ac.nz/esploro/outputs/journalArticle/Combinatorial-Exploration-An-Algorithmic-Framework-for/9926847164801891) and [ICE-TCS authors' publication list, item 5](https://icetcs.github.io/publ/) independently supply *Memoirs AMS* 317(1611), 2026, DOI 10.1090/memo/1611. The bibliography deliberately identifies the version used for section locators.
- [Flajolet's book publication page](https://algo.inria.fr/flajolet/Publications/AnaCombi/anacombi.html) confirms both authors, January 2009 and Cambridge University Press. The [authors' book site](https://ac.cs.princeton.edu/home/) and [Chapter 1 page](https://ac.cs.princeton.edu/10ogf/) support the limited method attribution above. Full PDF access failure is recorded, not turned into source content.
- [OEIS A393395 internal record](https://oeis.org/A393395/internal) identifies Vincent Vatter as original author on 17 February 2026, and lists the exact calibration data.
- [Zeng et al., publisher version 1](https://www.preprints.org/manuscript/202608.1658/v1) confirms all four author names, full title, preprint status and posting on 24 August 2026. The [publisher's Computational Mathematics listing](https://www.preprints.org/subject/browse/computer-science-and-mathematics/computational-mathematics), entry with this title and date, explicitly supplies DOI 10.20944/preprints202608.1658.v1. Following its DOI link opened the same v1 article. The direct resolver/API requests failed in this environment, but this publisher-owned DOI binding is readable and exact.

## Bibliography coverage and repairs

The six works have six necessary contextual roles: original machine, exact
problem/closest prior enumeration, that enumeration's framework, foundational
symbolic method, known coefficient calibration, and independent exact-verifier
comparison. Five are natural non-library sources. No entry was retained solely
to increase a count. The minimum user-library selection is not a ceiling on
references, and no source was renamed to conceal library membership.

All 49 active first-sheet titles were screened. No entry concerns stack sorting.
Row 9 is the relevant, inspectable comparison for separately rebuilding the finite
model in exact verification. Its relevance is narrow but substantive in Section 6.
An unrelated second item would add no support; the exact reason and dynamic
registry binding are in `audit/user-bibliography-selection.json`.
`verified_at` is the actual UTC date, 2026-09-12, rather than the local date.

Existing BibTeX records and all six citation keys were retained. No wholesale
official-export replacement was performed: export attempts did not provide a
usable block. Two source-grounded field repairs were made in `references.bib`:
the verified publisher DOI was added for ZengEtAl2026, and Atkinson1998's lengthy
publisher URL was replaced with its equivalent verified DOI URL. No invented
authors, title, venue, date or identifier was introduced. `main.tex` changed only
the selected citation's locator placement, standard URL package, title helper
and explicit PDF metadata; the mathematical content and line locations remain
unchanged. The initial URL change caused bibliography spacing diagnostics, which
were repaired by shortening the Atkinson link and then rebuilding cleanly.

## Accepted mathematics, finite numbers and scope

C01, C06, C08–C18, C21–C23 and C34–C35 were compared directly with the frozen
proof, original model and accepted report. The theorem, four transitions,
comparison forest, first-return cases, empty-interior exception, equation
elimination and uniqueness argument preserve the accepted all-size scope.
There is no unsupported strengthening to general (r,s)-stacks, no claim of a
finite global state space, and no new claim of priority for the greedy rule.

C25–C33 were checked against the actual original and referee JSON artifacts,
with the independent transcription checker `audit/release-transcription.py`.
The table has exactly 1,1,2,6,24,116,628,3636,21956,136428 for n=0 through 9.
The 46,234 inputs, 362,880 held-out inputs, 136,428 held-out words, 13,860 suffix
replays, 107,848 rejected/accepted legal-word attack cases and degree 40 bound
all match. The residual identity was freshly expanded with exact SymPy arithmetic.
The large exhaustive searches were not rerun by this release worker; no new
exhaustive coverage is claimed. The table was additionally compared visually
with the exact values after rendering.

C36 is a bounded, dated comparison, supported by the frozen search record and
fresh query captures. The prescribed author/year/title, venue, DOI and arXiv
queries were run where applicable; exact mechanism/Problem 5.11 searches were
also made. Returned secondary pages were discovery leads only. No equivalent
direct derivation was identified in the inspected primary sources; this is not
a global novelty certification. Search responses are saved in
`audit/source-search-1.json` through `audit/source-search-6.json`; source pages,
locators and access failures are saved in `audit/source-web-*.json`.

Bibliography revision leads were enumerated: none. Both supplied handoffs were
read and their relevant source/hash/version predicates checked. Crossref JSON/MD
captures were enumerated before declaring direct API access unavailable: none
were present. No valid saved authoritative response was discarded.

## Mechanical and rendered checks

The clean latexmk/BibTeX build converged with no warnings, undefined references,
undefined citations, missing records, duplicates, overfull or underfull boxes in
the final logs. `check_bib_keys.py` finds six cited keys, six bibliography keys,
six aux entries and no mismatch. All authored publication dependencies are the
two sorted `publication.source_files`; remaining inputs are standard toolchain
files or generated build products. No hidden local bibliography is used.

All seven final PDF pages were actually inspected at 1500-pixel scale. Citations
and all six references are visible, equations and tables are legible and inside
the margins, and proof continuations are intact. Detailed page observations and
PDF binding are in `audit/visual.md` and `audit/visual.json`; build evidence is
in `audit/build.md` and `audit/build.json`. `audit/citations.json` binds this
report to the current accepted evidence, manuscript and PDF snapshot.
