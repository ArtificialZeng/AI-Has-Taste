# Rendered-page visual audit

Accept. The current `manuscript/main.pdf` was rendered to PNG with
`pdftoppm -png -r 150`. Pages 1, 2, and 3 were each inspected at original image
resolution. The later PDF-metadata-only repair was rebuilt and re-rendered; all
three final PNG digests exactly matched the already inspected page images.

- Page 1: title block, abstract, context, displayed concentration matrix, main
  theorem, citations, mathematical symbols, and footer are sharp, aligned, and
  fully within the page.
- Page 2: proof heading, equations (1)--(6), products, fractions, PSD/kernel/rank
  line, proof terminator, corollary, and footer are legible with no clipping,
  overlap, bad break, or margin collision.
- Page 3: scope and assistance prose, all four bibliography entries, accents,
  italics, identifiers, and footer are legible and unclipped.

There are no figures, charts, tables, or raster data needing value-by-value
visual verification. No page has missing glyphs, overlap, truncation, illegible
text, or a visual strengthening of the accepted mathematical scope. The PDF
metadata title, author, and subject also match the manuscript.
