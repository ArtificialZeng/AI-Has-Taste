# Rendered-page visual audit

Release job `win-00077-p01-release-1b135af2eacf`; checked 2026-09-09 UTC
against PDF SHA-256
`ff87e7ba25522932028403bfd37dfef39e1e7de2b7580776aa0adbbab71d72bc`.

I rendered every PDF page at 150 dpi with `pdftoppm` and actually inspected
both PNGs at their original 1275 by 1651 pixel resolution.

| Page | Visible content inspected | Result |
|---|---|---|
| 1 | Title, author and affiliation, abstract, context and statement, all three citation callouts, fork definition, Theorem 1, and the first maximal-planarity display. | Clear; no clipping, overlap, broken glyph, margin overflow, or illegible citation. |
| 2 | Remaining maximal-planarity proof, complete red/blue avoidance proof, quantifier negation, proof-end mark, scope and assistance, and all three bibliography entries with DOI/URL wrapping. | Clear; equations, subscripts, overlines, disjoint-union symbols, page break, and references are legible and correctly aligned. |

The manuscript contains no chart, graph, table, diagram, or external bitmap
requiring value-by-value visual-source comparison. Page numbers are present
and ordered 1--2. Mathematical symbols, theorem typography, citations
`[1]`--`[3]`, headings, and whitespace are consistent. `pdffonts` confirms
that every font is embedded with a Unicode map, and text extraction confirms
searchable theorem, scope, and reference text.

Verdict: **accept**; pages 1 and 2 were each viewed at original rendered
resolution and show no visual defect that blocks release.
