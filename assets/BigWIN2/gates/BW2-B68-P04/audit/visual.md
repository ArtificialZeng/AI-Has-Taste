# Rendered-page visual audit

Release job `win-00068-p04-release-8022f2ea8df8`. **PASS.**

The freshly rebuilt PDF was rendered with `pdftoppm -png -r 150 manuscript/main.pdf audit/rendered/page`. Every page was then opened at original rendered resolution and inspected directly. No clipping, overlap, missing glyph, illegible expression, unresolved cross-reference, or margin overflow was seen. The paper contains no charts or data graphics requiring value-by-value visual verification.

1. Page 1: title, author, abstract, foundational citations, and measure definitions are complete and legible.
2. Page 2: curvature and flow definitions, transport imbalance, epsilon bounds, coupling, and dual potential are legible; all content clears the footer.
3. Page 3: both transport branches, the displayed curvature formula, tied-edge limit, and ordered curvature vector render correctly.
4. Page 4: ODE citation, invariant-wall calculation, Proposition 1, and log-ratio identities are complete and well spaced.
5. Page 5: equilibria, median argument, ratio argument, and all three cases of Theorem 2 are complete and legible.
6. Page 6: assistance disclosure and all seven references are readable; long names and versioned URLs wrap within the text area.

PDF SHA-256: `3a72e85bd8acb27a4286cabcacc8af315a579c87a00e80f2bee2a00b0e88f6a8`.
