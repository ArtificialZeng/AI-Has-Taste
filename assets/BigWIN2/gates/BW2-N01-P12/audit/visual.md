# Rendered-page visual audit

Verdict: **accept**. Job: newwin-00001-p12-release-3b1ac840a39d

Final PDF SHA-256: `3127b814b3a9ba2b644ec69ad464bc100248db6d3a102006ff032851d54f9d73`. Manuscript digest: `f6967d1b82942a4db6cdf29869eddc47ab55b32366a0b4d5dce2d7eaa4e52d7d`.

Every final page was rendered at 110 dpi with pdftoppm and individually opened with view_image after the final parser-compatible rebuild. This is an actual image inspection, not an inference from pdftotext or prior writer checks. The earlier inspected build was superseded and not used to accept this PDF.

- Page 1: Title, author, abstract and exact theorem fit. The algebraic-closure overbar, subscripts, q-integer products and equation numbers are legible.
- Page 2: Prior-work citations and augmented-cell formulas are complete. The transpose convention, scalar quotient and normalization fit without overlap.
- Page 3: Unit-pivot lemma, equations, variable order and full elimination proof are readable. The bottom partition ranges are inside the page boundary.
- Page 4: Complete finite-evaluation discussion, method citations, main proof and binary-check description fit. The long factor-length formula is not clipped.
- Page 5: Binary witness matrices and nonzero minor are legible. AI/reproducibility disclosure and the start of the code listing are complete; the listing continues naturally on page 6.
- Page 6: Remaining code retains indentation, brackets, assertions and terminal print statement. Listing frame is complete and no line is truncated.
- Page 7: First 47 coefficient rows are aligned beneath all four headers. Continuation notice is visible and the final row does not touch the page number.
- Page 8: Final eight coefficient rows retain the repeated table header and end at the maximal shape. All six bibliography entries, dates and preprint status are readable; no overlap or clipped DOI.

There are no plots, empirical axes or image-derived statistics. All 55 rows of the coefficient table were checked value by value against exact reconstruction, with no rounding or omitted rows. Code was checked against the executable companion. PDF title and author are correct; all fonts are embedded. No clipping, overlaps, illegible symbols or blank pages were found. The table uses default column spacing after the scope-preserving parser repair and remains legible. Image/PDF bindings and per-page hashes are in audit/release-visual-evidence.json.
