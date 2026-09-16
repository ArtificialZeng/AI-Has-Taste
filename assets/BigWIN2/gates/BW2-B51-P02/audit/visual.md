# Rendered-page visual release audit

I rendered the current `manuscript/main.pdf` at 144 DPI with `pdftoppm` and visually inspected each page at its original rendered resolution (1224 by 1584 pixels).

- Page 1: title, author block, abstract, context, theorem, displayed equations, citations, and the opening upper-bound proof are legible.  Margins are intact; the Cartesian-product square and all mathematical symbols render with embedded fonts.  No clipping, collision, missing text, or overfull visual line is present.
- Page 2: the edge-numbering formulas, four hexadecimal generators, spanning-tree certificate table, proof continuation, and section transition are legible.  All 15 table rows and all edge-index lists fit inside the rules and page margins.  No overlap, truncation, or illegible reduction occurs.
- Page 3: the replay/scope text, computational-assistance disclosure, and all four bibliography entries are legible.  DOI text and the long Tian and Zeng titles wrap inside the margins.  The page has no clipped footer, stray artifact, overlap, or missing glyph.

The page sequence is complete (1, 2, 3), table and theorem references resolve, font rendering is consistent, and no figures or charts require value-by-value visual checking.

**Verdict: accept.**
