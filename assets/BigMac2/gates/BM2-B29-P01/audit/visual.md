# Fresh rendered-page visual audit

I rendered the current five-page PDF at 180 dpi with `pdftoppm` and inspected
each PNG at original resolution.  The reviewed images are
`audit/rendered/page-1.png` through `audit/rendered/page-5.png`.

- **Page 1:** title, author block, abstract, theorem display, citations, prose,
  and opening Krawtchouk formula are sharp and within the margins.  No overlap,
  clipping, orphaned symbol, or illegible text is present.
- **Page 2:** the baseline and mixed-system displays, equation numbers, branch
  list, sums, and Hadamard matrix are aligned and fully visible.  The page break
  is semantically clean.
- **Page 3:** the joint-transform identity, theorem, both witness tables, phase
  sums, and coefficient formulas are readable.  Rules and entries in both
  tables remain inside the text block, and equation links do not obscure text.
- **Page 4:** long ancillary paths wrap cleanly without crossing margins; the
  Farkas inequalities, denominator, fraction, and contradiction chain are
  legible and correctly positioned.  No line or glyph is clipped.
- **Page 5:** scope statements, two replay commands, disclosure, and all three
  bibliography entries are readable.  DOI links fit the text block, and the
  final page has balanced whitespace with no stranded heading.

There are no figures or charts requiring data-point comparison.  Visual review
also confirms consistent fonts, equation numbering, heading hierarchy, page
numbers, link coloring, and margins.  All fonts are embedded according to
`audit/pdffonts.txt`.

**Verdict: ACCEPT.**  Pages 1--5 are clean, legible, and submission-ready.
