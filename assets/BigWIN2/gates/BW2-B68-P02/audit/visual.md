# Rendered-page visual audit

For release job `win-00068-p02-release-ad1c2e39c442`, citation attempt 7,
launch `19e4b0d4-8102-47fd-98db-15f8d58d6f9f`, I freshly rendered the
unchanged refrozen `manuscript/main.pdf` (SHA-256
`1ce0b11ced22734c49a198b92d73f3652acde55382f314a00e61c8645898a671`)
with `pdftoppm -png -r 150` into a fresh temporary directory and invoked the
image-view tool at original detail on each rendered page.  Pages actually
viewed: 1, 2, 3, 4, and 5.

- Page 1: title, author block, abstract, context, theorem, and the beginning of
  the graph6 list are fully visible; no clipping, collision, or bad glyphs.
- Page 2: the complete two-column graph6 list, lemma, displayed identities,
  CNF notation, and prose are legible and remain inside the margins.
- Page 3: census method, recurrence, and eight-row census table are aligned and
  readable; no table overflow or symbol loss.
- Page 4: classification table and reproducibility discussion are clear; rules,
  numerals, math symbols, and monospaced path are intact.
- Page 5: assistance disclosure and all seven bibliography entries are legible;
  DOI/URL strings wrap without crossing margins.

There are no figures requiring value-by-value source comparison.  The PDF has
no clipped text, overlapping blocks, missing characters, illegible tables,
or distorted visuals.  The title/author metadata agrees with the rendered first
page.  The visual audit accepts all five pages.
