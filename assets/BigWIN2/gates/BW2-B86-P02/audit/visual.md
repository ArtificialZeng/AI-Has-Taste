# Rendered-page visual audit

The current `manuscript/main.pdf` was rendered with `pdftoppm -png -r 150`.
Pages 1, 2, and 3 were each opened and inspected at original rendered
resolution after the final rebuild.

- Page 1: title, author block, abstract, equations, citations, and section
  transition are centered or aligned correctly; no clipping or collision.
- Page 2: theorem, proof paragraphs, displayed equations (2)--(6), subscripts,
  cosets, wreath-product notation, and page number are fully visible; the last
  display remains above the footer.
- Page 3: equations (7)--(8), proof ending, disclosure, and all six reference
  entries are legible and inside the margins; DOI and arXiv text is intact.

Across all pages there are no figures, charts, or tables requiring data-point
verification.  No overlap, cutoff, missing glyph, broken symbol, unexpected
blank region, orphaned heading, illegible text, or malformed reference was
seen.  The rendered mathematical statement remains within the accepted scope.

Result: **visual audit accepted for pages 1--3**.
