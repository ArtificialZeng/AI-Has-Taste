# Fresh rendered-page visual audit

Date: 2026-09-09  
Release job: `bigMac-00023-p06-release-71cb8b727e7d`

The freshly built PDF was rendered with Poppler at 150 dpi:

```text
pdftoppm -png -r 150 manuscript/main.pdf page
```

All four resulting page images were opened and visually inspected at original
rendered resolution. Observations:

- Page 1: title, author block, abstract, displayed definitions, citations, and
  opening context are sharp and within margins; no overlap or clipping.
- Page 2: Theorem 1, the complete five-row mask table, complement equation,
  bullets, and Lemma 2 are legible. Long rows wrap inside the table without
  collision or truncation; rules and labels are aligned.
- Page 3: both proofs, displayed sum, proposition statistics, example cycle,
  section heading, and independent-check prose are readable. QED symbols,
  subscripts, and mathematical glyphs render correctly; no content is cut off.
- Page 4: limitations, reproduction commands, assistance disclosure, and all
  four bibliography entries are readable. DOI/arXiv URLs wrap across lines
  without clipping or overwriting adjacent text.

Page numbers are present and ordered 1--4. There are no figures or charts
requiring separate legend/axis review. Whitespace and page breaks are
reasonable, and no equation, table cell, reference, or footer is illegible.

**Verdict: accept; pages reviewed exactly `[1,2,3,4]`.**

