# Rendered-page visual audit

## Verdict

Accept.  The final PDF was rendered at 150 dpi with `pdftoppm` and every page
was inspected at original rendered resolution (1275 by 1650 pixels).

- Page 1: title block, abstract, context, theorem, and start of the exhaustive
  reduction are fully visible; citations, subscripts, and displayed formulas
  are legible; no clipping or overlap.
- Page 2: candidate list, zero-witness table, Frobenius/Jacobi--Trudi formulas,
  determinant recurrence, and proof conclusion are fully visible; table rules
  and long partitions are legible; no clipping or collision.
- Page 3: computational verification, assistance disclosure, and all six
  bibliography entries are fully visible; line wrapping and page margins are
  sound; no missing glyphs or illegible text.

There are no figures or charts requiring data-point comparison.  All three
rendered page hashes were unchanged by the metadata-only final source repair.

