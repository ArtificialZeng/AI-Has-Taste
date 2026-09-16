# Rendered-page visual audit

Release job `win-00070-p02-release-7fa60259311e`; checked 2026-09-08 against
PDF SHA-256
`57c6e200d7ac574e379774f84a9e25e395949aa6891ac9580fddc2d024121785`.

I rendered every page at 150 dpi with `pdftoppm` and inspected the four PNGs
at their original 1275 by 1651 pixel resolution.

| Page | Visible content inspected | Result |
|---|---|---|
| 1 | Title, author/affiliation, abstract, Statement and context, displayed definitions and functional equation, Theorem 1, Corollary 2, and bounded-scope warning. | Clear; no clipping, overlap, broken glyph, or margin overflow. |
| 2 | Analytic enclosures, derivative recurrence, Arb citation, quotient definition, interpolation bound, and Lemma 3. | Equations and subscripts/superscripts are legible and aligned; no collision or cutoff. |
| 3 | Leaf proof, monotonicity formula, exact partition, certificate census and margins, theorem/corollary proofs, and start of reproducibility file list. | Clear page break and full lines; proof-end marks, bars, conjugation, intervals, and scientific notation render correctly. |
| 4 | Remaining artifact list, replay command, trust boundary, library-method comparison, limitations, assistance disclosure, and all four references. | Monospace commands and bibliography wrap cleanly; all entries fit and remain legible. |

The document contains no charts, figures, or tables requiring value-by-value
visual-source comparison. Page numbers are present and ordered 1--4. Font
weight, mathematical symbols, citations [1]--[4], headings, and whitespace are
consistent. `pdffonts` confirms every font is embedded, and `pdftotext`
confirms searchable text for the theorem, corollary, lemma, limitations, and
all references.

Verdict: **accept**; pages 1, 2, 3, and 4 were each actually viewed once and
show no rendered-page defect that blocks release.
