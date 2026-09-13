# Fresh rendered-page visual audit

## Method and binding

I rendered the current `manuscript/main.pdf` with Poppler at 180 dpi to four
1530-by-1980 RGB PNG images and inspected every image at original rendered
resolution.  The inspected PDF has SHA-256
`e93effdcef1e2bcd89eca44c15aa105cb4c459227f5744fb9cf63985d171b88a`;
`pdfinfo` reports exactly four pages.  Text extraction was used only as a
separate cross-check, not as a substitute for visual inspection.

## Page observations

1. **Page 1:** Title, degree-sequence superscripts, author block, abstract,
   Section 1 prose, displayed excess formula, Theorem 1, and the Section 2
   heading are sharp and within the margins.  Citation markers are resolved.
   There is no clipping, collision, orphaned rule, or illegible symbol.
2. **Page 2:** Lemma 2, its proof, the displayed edge count, attachment-orbit
   formulas, and the opening of Section 3 are readable.  Line breaks and the
   proof-ending square remain inside the text block.  No equation or paragraph
   overlaps another element or crosses the page boundary.
3. **Page 3:** Table 1 is centered, all seven columns and every digit are
   legible, and the top/mid/bottom rules are intact.  The proof completion,
   four-item reproducibility list, verbatim command block, and Zeng comparison
   are fully visible with no clipping or overlap.
4. **Page 4:** The limitations/assistance text and all four bibliography items
   are legible.  Long titles and journal names wrap cleanly; diacritics,
   identifiers, DOI strings, punctuation, and page ranges render correctly.
   The page has no stranded heading, collision, or cut-off reference.

Across all pages, margins are consistent, page numbers are visible, font sizes
are readable, embedded Latin Modern text and mathematical symbols are crisp,
and there are no figures requiring a separate legend or color check.  PDF
title/author/subject metadata also match the rendered manuscript.  The authored
text does not visually or verbally strengthen the accepted theorem beyond
degree sequence `(5,3^23)`.

## Verdict

**Accept.**  Pages reviewed exactly once: 1, 2, 3, and 4.  No substantive
typographic or presentation defect was found.
