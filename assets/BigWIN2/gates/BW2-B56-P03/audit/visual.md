# Rendered-page visual audit

**Accept.** The final PDF was rendered with `pdftoppm -png -r 150` and every
page was inspected at original rendered resolution.

| Page | Content inspected | Result |
|---:|---|---|
| 1 | title, author, abstract, context, theorem opening | legible; no clipping, overlap, or bad glyphs |
| 2 | four equality ideals, encoding proof, Taylor display | legible; page-break placement is clear and no formula is clipped |
| 3 | tangent proof, histogram table, scope, references 1--4 | table aligned; no overlap, clipping, or margin overflow |
| 4 | references 5--6 | legible; intentionally sparse final bibliography page |

All mathematical symbols, superscripts, subscripts, inequalities, generator
lists, citation numbers, and page numbers render correctly. The table has no
distorted axis or graphical encoding; it is a direct two-row exact-value
table. The authored text preserves the accepted Borel-only scope and does not
strengthen the frozen theorem. Title and author PDF metadata are present.
