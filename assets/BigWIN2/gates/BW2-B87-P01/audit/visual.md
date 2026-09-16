# Rendered-page visual audit

I rendered `manuscript/main.pdf` at 150 dpi with `pdftoppm -png` and actually
viewed every page.  The durable render files are
`audit/rendered/page-1.png`, `audit/rendered/page-2.png`, and
`audit/rendered/page-3.png`.

- Page 1: title, author block, abstract, context, displayed definition, and
  theorem are fully inside the page; citations and mathematical symbols are
  legible; no collision, missing glyph, or truncated line is present.
- Page 2: the auxiliary-graph lemma and lower-bound proof are fully legible;
  display equations (2) and (3), the quadratic inequality, proof marks, and
  page footer do not overlap or clip.
- Page 3: the construction proof, computational/AI disclosure, and all five
  bibliography entries are fully visible; accents, inequality symbols,
  subscripts, and line wraps render correctly, with adequate bottom margin.

The three durable renders are byte-identical to the files inspected in the
viewer.  `pdfinfo`, text extraction, and embedded-font inspection were used as
supplementary checks, not substitutes for the page views.  The authored text
does not visually or verbally strengthen the accepted theorem or claim
publication priority.

**Verdict: accept.**  All pages 1--3 pass for clipping, overlap, legibility,
glyph integrity, and layout.
