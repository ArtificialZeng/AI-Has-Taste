# Checkpoint

Job: `bigMac-00014-p01-release-bc265e3b209b` (release phase, 2026-09-08).

## Current state and evidence

- The accepted mathematical snapshot remains
  `64359d3012d06c12d1f42fca723c4b98cccde9ccf428bdb15ce924eab88e8b70`;
  `audit/math.json` has verdict `accept` from the separate referee job.
- The advisory citation-check workflow fixed eight external-attribution,
  disclosure, and bibliography claims in `audit/citation_claims.md`. Primary
  arXiv/author/publisher text verifies He--Huang, Li--Lin--Rodman,
  Houck--Paul, and Flajolet--Odlyzko at the manuscript's narrow scope.
- The user-designated workbook record documented in
  `literature/user_bibliography_check.md` supplies the authoritative metadata
  for Zijian Zeng (2026), DOI `10.2139/ssrn.7380519`. A fresh external refresh
  was unavailable in scope. The manuscript's unsupported attribution of a
  specific parity cancellation to that paper was removed; its remaining use is
  the genuinely relevant, title-supported comparison with the distinct-cycle-
  length probability for uniform permutations.
- A from-clean LaTeX build produced `manuscript/manuscript.pdf`, five A4 pages.
  The final `manuscript/manuscript.log` has SHA-256
  `a8b91de76e32ce641ea9d33c3d1df41b223c49ea699734ec20f2d4fd58a75c9c`
  and no warnings, undefined references/citations, or box diagnostics.
- The current manuscript digest is
  `2caba2992b8d76c289fde31228e4aaa1a1d70dcf2af83ad9ca6c2ae29f99cc16`;
  the PDF digest is
  `e25cc9967925fe8788aac0c3b7c725d6b61235469b8fc3ff0e24688073bbcb37`.
- All five pages were rendered at 160 dpi and visually inspected. Equations,
  tables, references, fonts, wrapping, margins, and page numbers are legible,
  with no clipping or overlap. Reports and provenance-bound records are in
  `audit/citations.*`, `audit/build.*`, and `audit/visual.*`.
- `release_gate.py check` passed with kind `resolution-paper`, original status
  `proved`, and five pages. The immutable `source.md` SHA-256 remains
  `948ed700a0d00a8cf0441896e9d587e341a2633660cffb0b21b8bd9f917c6140`.

## Obstacles and limitations

No mathematical, build, citation-support, or visual obstacle remains. The
Zeng resolver/full-text refresh limitation is disclosed and does not affect
the theorem, determinant reduction, asymptotic, or bounded novelty wording.

## One next test

The supervisor should run `release_gate.py publish` on this exact validated
state and verify that the active manifest's PDF digest equals
`e25cc9967925fe8788aac0c3b7c725d6b61235469b8fc3ff0e24688073bbcb37`.

