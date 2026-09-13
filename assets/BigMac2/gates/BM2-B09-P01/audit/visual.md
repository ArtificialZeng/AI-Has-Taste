# Fresh rendered-page visual audit

Audit date: 2026-09-07 (Asia/Shanghai)  
Release job: `bigMac-00009-p01-release-0c119e668365`

This report is bound to evidence snapshot
`f9c68aabbc292cf2fd8e90b5635b9baef672e7c87ad17d46d177e0d4d622b153`,
manuscript digest
`e492c66ba6b9df7334af2f520131d3a5d6f0676fe4ab45df1ddab17a80709752`,
and PDF digest
`fdcdba76cfab26dd9d05844b0c1a9cc033a655303cd090e0ee0b1a92f8110d84`.

I obtained the actual page count (4) with `pdfinfo`, rendered the current PDF at
150 dpi with `pdftoppm`, and visually inspected the original-resolution PNG for
every page. The reviewed images are `audit/render-release/page-1.png` through
`page-4.png`.

## Page-by-page observations

1. Page 1: title, author block, abstract, keywords, definitions, source-question
   attribution, theorem, and graph6 string are sharp and fully inside the page.
   The two-line title and abstract wrapping are balanced; no character or line
   is clipped.
2. Page 2: both color tables, captions, displayed spanning-tree edge list,
   class-size vector, and section transition are legible. Rules and columns are
   aligned, table entries do not collide, and mathematical primes/subscripts are
   distinguishable.
3. Page 3: the CNF clauses, recurrence, reified-connective display, Lemma 2,
   numerical certificate counts, and RUP argument are all readable. Equation
   number (1) stays inside the margin; no display overlaps surrounding prose.
4. Page 4: the reproducibility command, scope/disclosure prose, and all three
   references are legible. Long arXiv/DOI URLs wrap without entering the margin,
   reference labels align, and no bibliography line is clipped.

All four pages use consistent margins, baseline spacing, headings, and page
numbers. There are no figures or charts requiring value-by-value visual-data
comparison. The tables have no truncated axes, 3-D effects, or other visual
distortion. No page shows overlap, crop loss, missing glyphs, unreadably small
text, unintended blank content, or broken hyperlink text.

## Verdict

**Accept.** Pages 1, 2, 3, and 4 were each actually seen and are readable and
submission-ready at the audited scope.
