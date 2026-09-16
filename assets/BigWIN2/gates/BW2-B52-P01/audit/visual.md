# Rendered-page visual audit

The current PDF (SHA-256
`c92e5991620ae4b44aec550d45c353a2611da2c90dc7b70913eb6c45a65c8d09`)
was rendered at 150 dpi with `pdftoppm` and pages 1, 2, 3, and 4 were each
inspected at original rendered resolution.

- Page 1: title, author block, abstract, definitions, theorem, and displayed
  formulae are fully visible and legible.
- Page 2: lemma/proof, group-type display, path names, and enumeration table are
  aligned, legible, and within the page boundary.
- Page 3: continued proof, certificate formulae, reproduction commands,
  disclosure, and the first bibliography entry are legible; line wrapping is
  sound.
- Page 4: the two remaining bibliography entries and DOI links are legible and
  unclipped.

No page has clipping, overlap, missing glyphs, illegible text, distorted
figures, broken tables, or margin overflow.  There are no charts, graphs,
figures, or visual data values requiring a separate value-by-value source
comparison.  Hyperlink and cross-reference annotation boxes are visible but do
not obscure any character.  All fonts reported by `pdffonts` are embedded.
