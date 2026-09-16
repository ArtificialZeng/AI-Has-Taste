# Rendered-page visual audit

The final PDF with SHA-256
`e81fb2000a28b9979af53203dbcaed986aaac0e1cce7502021de82baced0cec7`
was rendered with `pdftoppm -png -r 150`.  Every rendered page was opened and
inspected at original image resolution after the final metadata and bibliography
edits.

- Page 1: title, author block, abstract, source comparison, theorem, and opening
  notation are fully visible with intact margins and readable superscripts.
- Page 2: vertex-ray argument and equations (1)--(8) are aligned and legible;
  there is no clipping, collision, or orphaned display.
- Page 3: the full 8-by-8 Gram matrix, model normals, and Lorentz-isometry argument
  fit within the text block; matrix delimiters, equation numbers, and subscripts
  are clear.
- Page 4: Klein conclusion, exact-check disclosure, and all three bibliography
  entries are legible; DOI and URL text stays inside the page boundary.

No figures, charts, or tables require data-value verification.  Across pages
1--4 there is no overlap, cutoff, blank page, malformed glyph, illegible text,
unexpected color, or inconsistent page geometry.  All fonts reported by
`pdffonts` are embedded.  The rendered-page review therefore passes.
