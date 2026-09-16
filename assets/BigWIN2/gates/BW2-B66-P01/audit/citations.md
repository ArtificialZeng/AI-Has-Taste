# Citation, bibliography, build, and rendered-page audit

## Scope and method

This release audit is bound to job `win-00066-p01-release-0d8daa2815b8`, citation attempt 3, launch UUID `289e30e2-93e7-4edf-bebb-cf7584aa33b4`, and the manuscript snapshot recorded in `audit/manuscript-snapshot.json`. The review used a two-pass procedure: first the five claim/citation pairs in `audit/citation-claim-ledger.json` were extracted and frozen without verification; second, those fixed claims were checked sequentially against primary publication records and exact source passages. No subagents were used because the job explicitly prohibited them.

The ordinary body-flow citation-key set is exactly `AxenovichEtAl2019`, `BaldacchinoCaroMifsud2026`, `MaTangYu2020`, and `Zeng2026SmallRamsey`. Its equality with the union of ledger keys was checked directly. There are no citation macros, `\nocite` commands, hidden-condition citations, or commented citations. Bibliography coverage is not library-only: three of four works are natural non-library primary sources, including the problem-origin/closest-prior source and the two prior planar-Ramsey method/context papers.

## Claim verification

| Claim | Key | Primary source and exact location | Result | Why retained |
|---|---|---|---|---|
| CIT-001 | `AxenovichEtAl2019` | Electronic Journal of Combinatorics article page and PDF, abstract and p. 2 definition: planar unavoidability means that there exists a planar witness graph whose every two-edge-colouring contains the target. DOI `10.37236/8366`. | Verified, paraphrase | Defines the weak planar-witness formulation contrasted with this note. |
| CIT-002 | `MaTangYu2020` | Electronic Journal of Combinatorics article page and PDF, abstract and p. 1 introduction: the paper studies two-edge-colourings of recursively defined iterated triangulations under the same witness formulation. DOI `10.37236/9292`. | Verified, paraphrase | Natural primary follow-up on iterated triangulations. |
| CIT-003 | `Zeng2026SmallRamsey` | Preprints.org Version 1 landing page, abstract first sentence: the small Ramsey degree of the ordered edge in finite linearly ordered split graphs with induced order-preserving embeddings is exactly three. DOI `10.20944/preprints202608.2162.v1`. | Verified, paraphrase | The sole naturally relevant active-library record; distinguishes another Ramsey invariant. |
| CIT-004 | `BaldacchinoCaroMifsud2026` | Supplied arXiv v1 PDF, p. 2, Definition 1 and Section 1.1: unavoidability requires every sufficiently large graph in the class, and the paper calls this the strong condition. arXiv `2609.05268v1`. | Verified, paraphrase | Establishes the exact convention used by the problem and manuscript. |
| CIT-005 | `BaldacchinoCaroMifsud2026` | Supplied arXiv v1 PDF, p. 2, Theorem 2, and p. 21, Problem 2: the connected diagonal MP case is characterized and the disconnected diagonal case is posed. | Verified, paraphrase | Problem origin and closest prior result. |

All four sources exist. Author, title, year, venue/version, and DOI/arXiv metadata in `manuscript/references.bib` agree with their primary records. No retained reference is decorative, no bibliography key change or replacement was needed, and no source claims the new bound `21`; that theorem rests on the accepted self-contained proof. The manuscript expressly limits the comparison and makes no global priority claim.

Search verification was performed on 2026-09-07 using the prescribed author/title, exact-title/domain, author/year/venue, DOI, and (where applicable) arXiv-ID query patterns. The primary records inspected were:

- https://www.combinatorics.org/ojs/index.php/eljc/article/view/v26i4p9
- https://www.combinatorics.org/ojs/index.php/eljc/article/download/v26i4p9/pdf/
- https://www.combinatorics.org/ojs/index.php/eljc/article/view/v27i4p18
- https://www.combinatorics.org/ojs/index.php/eljc/article/download/v27i4p18/pdf/
- https://www.preprints.org/manuscript/202608.2162
- `evidence/external/2609.05268.pdf`, SHA-256 `d2c05952bb165545210571a572678338e7766162141549adbf62411e3cf881b2`

## User-library selection and coverage

The active registry and workbook were independently hashed and match the dynamic binding in `audit/user-bibliography-selection.json`. Row 27 is the only natural selection. Its title, author, DOI, Version 1 posting date, and exact abstract support were verified against Preprints.org. The final key `Zeng2026SmallRamsey` is cited directly in ordinary body flow at `manuscript/main.tex:51`. Selecting any second registry entry would add an unsupported or decorative comparison, so none was added.

## Build, references, and visual review

The canonical build command completed successfully with `latexmk`, and the BibTeX workflow converged. The mechanical key checker found four cited keys, four bibliography keys, no missing or unused entries, and no `.aux` mismatch. The final `.log` and `.blg` contain no undefined citations, missing database entries, duplicate-entry warnings, LaTeX errors, fatal errors, emergency stops, undefined control sequences, or runaway arguments. Cross-references resolve.

Every page of `manuscript/main.pdf` was rasterized at 180 dpi and visually inspected at original rendered resolution. Pages 1--3 were seen. The title/author block, abstract, theorem and proof displays, section transitions, bibliography, and assistance disclosure are legible; there is no clipping, overlap, cropped text, malformed formula, broken link text, or figure/table issue. Fonts are embedded and the PDF has no encryption or JavaScript. The PDF title/author metadata agree with the manuscript.

## Verdict

Pass. The citations are real and correctly support all five frozen nearby claims; coverage includes the natural non-library primary sources; the accepted mathematical scope was not strengthened; the bibliography and build are internally consistent; and all three rendered pages pass visual review.
