# Rendered-page visual audit

Verdict: accept

The final `manuscript/main.pdf` (SHA-256
`420b7184611029b90132c057147606feb5825a15b2e02ab5de029d1da07ca5c4`)
was rendered with `pdftoppm -png -r 144` and pages 1, 2, 3, 4, and 5 were each
inspected at original rendered resolution.

- Page 1: title, author block, abstract, contextual citations, and opening
  displayed formulae are centered and legible; no clipping or collision.
- Page 2: theorem statement and top-layer lemma are complete; long formulae,
  equation numbers, indices, and page footer fit within the margins.
- Page 3: proof displays and the off-diagonal lemma are legible; no overlap,
  missing glyph, or clipped proof symbol.
- Page 4: alternating-path proof and both remarks fit cleanly; the bottom line
  and footer are visible and not clipped.
- Page 5: assistance disclosure and all four bibliography entries are legible;
  line wrapping, DOI/arXiv text, and Unicode-derived title typography render
  without missing glyphs.

Across all pages, margins are consistent, fonts are embedded/rendered, equation
numbers are aligned, hyperlinks do not obscure text, and there are no figures,
tables, color encodings, truncated axes, or other visual data requiring a
value-by-value integrity audit.

