# PDF audit

Audit date: 2026-08-30.

Artifact: paper/main.pdf

- SHA-256:
  d4c1cde0b8b91e97686bcf71c6f082ba099e7523179592d50222f3f2f327ebbd
- Size: 356,404 bytes
- Pages: 5
- Page size: US Letter, 612 by 792 points
- PDF version: 1.7
- Encrypted: no
- Forms/JavaScript: none
- Fonts: every listed font is embedded and subset
- Title metadata: A Certified Finite Census for Additive-Square-Free Words on
  Four-Letter Integer Alphabets of Height at Most Five
- Author metadata: Zijian Zeng

## Visual inspection

Every page was rendered at 150 dpi with Poppler and inspected at original
render resolution.

1. Page 1: title, author, abstract, displayed values, citations, date, and
   footer are aligned and legible.
2. Page 2: definitions, normalization equations, midpoint identity, proof
   symbols, and section transition are complete with no clipped glyphs.
3. Page 3: all seven table rows and all integer groupings are legible; both
   displayed witnesses wrap deliberately; theorem and proposition transitions
   are clean.
4. Page 4: morphism proof, certificate paths, 64-character SHA-256 strings,
   commands, and diagnostic section all fit inside the text block.
5. Page 5: limitations, disclosure, all nine bibliography entries,
   affiliation, and both email addresses are present and readable.

No clipping, overlap, black boxes, missing glyphs, orphaned author block,
broken table rules, or excessive final-page whitespace was found. An
intermediate six-page build that left the author block alone on page 6 was
rejected and re-typeset; it is not the audited artifact.

## Build-log checks

The final LaTeX log contains no undefined citations/references, overfull or
underfull boxes, warnings, or errors. The skill audit returned:

    cited=9 bib=9 missing=0 unused=0

Disposition: PASS.
