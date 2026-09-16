# Rendered-page visual audit

The final four-page PDF was rendered at 150 dpi with `pdftoppm` to
`audit/rendered/page-1.png` through `page-4.png`.  I opened and inspected every
render at its original 1275 by 1651 pixel resolution.

| Page | Contents inspected | Result |
| --- | --- | --- |
| 1 | Title, author block, abstract, definition, context citations, and start of Theorem 1 | Clear; no clipping, overlap, missing glyph, or margin violation |
| 2 | Remainder of Theorem 1, Lemma 2 and proof, parent-completion table, start of rival proof | Clear; equations and table rules are aligned and legible |
| 3 | Flip-rival Table 1, exceptional degree table, automorphism/orbit argument, start of computation section | Clear; all subscripts, exponents, labels, and table cells are legible |
| 4 | Computation disclosure, literal rerun command, literature scope, and all four bibliography entries | Clear; URLs, DOI, numbering, and page footer are intact |

There are no figures or quantitative charts requiring a value-by-value visual
data comparison.  Both mathematical tables were compared to the TeX source;
their rows, labels, subscripts, and numerical entries render without omission
or distortion.  Page breaks do not hide text, all references are visible, and
the type size and line spacing remain readable.  PDF metadata is present and
all fonts are embedded.

**Verdict: accept.**  Pages 1, 2, 3, and 4 were each actually seen and have no
visual release blocker.
