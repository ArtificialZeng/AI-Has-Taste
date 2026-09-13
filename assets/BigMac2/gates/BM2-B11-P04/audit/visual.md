# Fresh rendered-page visual audit

I rendered `manuscript/main.pdf` with Poppler at 150 dpi and inspected every
rendered page as an image, not merely as extracted text.  `pdfinfo` gives an
actual page count of four, so the complete reviewed set is pages 1--4.

- **Page 1:** title, author block, abstract, model notation, equations (1)--(2),
  citation markers, and footer are sharp and fully inside the page.  The long
  title and covariance display fit without collision or clipping.
- **Page 2:** Theorem 1, sign classification, Robin problem, moment equations,
  and the mixed-moment display are legible.  Line breaks, equation numbers,
  margins, and page footer are clean.
- **Page 3:** covariance reduction, series coefficient argument, zero-set
  proof, and exact-witness calculation are legible.  The infinite-series and
  rational displays do not overrun the margins or collide with text.
- **Page 4:** the witness conclusion, variance argument, literature-scope
  paragraph, assistance disclosure, and both bibliography entries render
  cleanly.  The bottom half is intentionally open whitespace; no content is
  missing or clipped.

There are no figures, charts, tables, raster artifacts, overlapping objects,
cut equations, illegible symbols, orphaned headings, or anomalous blank
pages.  Font weight and size remain readable throughout, and all four page
numbers are visible.

**Verdict: accept.**  The complete four-page PDF is visually suitable for
release.
