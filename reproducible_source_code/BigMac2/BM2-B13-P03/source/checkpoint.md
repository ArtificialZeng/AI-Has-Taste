# Checkpoint

## Accepted result and frozen scope

- The fresh referee accepted the full-resolution `claim.json`; see
  `audit/math.json` and `audit/math.md`.
- For every \(L>0\),
  \[
  \operatorname{Lip}(T_L)=T_L'(0)=Z_L=2e^{L^2/2}\Phi(L),
  \]
  the continuous derivative has maximizer set \(\{0\}\), and the accepted
  logarithmic asymptotic is reproduced in the manuscript.
- The evidence snapshot remains
  `393c635435e81b9dc70256f6851164d5d45067c12ff2d04143ac46090b6303c6`.
  `source.md` remains unchanged at SHA-256
  `e3d10ece2fc71dccdf70f98eef6b53150b533f21e138b19f7310d1ec861d52b5`.

## Fresh release evidence

- Release job: `bigMac-00013-p03-release-4189b067aff7`.
- Citation audit: `audit/citations.md` and `audit/citations.json`. The requested
  citation-check skill was used in two passes. Gwóźdź v1 Remark 5.7 exactly
  supports the stated family, origin derivative, and lower-bound provenance.
  The official Zeng preprint supports only the explicitly disclosed
  restricted-model-versus-ambient methodological comparison and contains no
  optimal-transport claim. Both citations and all keys are verified.
- Clean build audit: `audit/build.md` and `audit/build.json`. A forced full
  latexmk build completed successfully. The final `manuscript/main.log` has
  SHA-256 `e1b6dcecff22e91d6164dd9254d6d8dd7d7967af0f324c1afbf2317d5d43301b`
  and no unresolved references/citations, compiler errors, box warnings, or
  rerun request.
- The rebuilt three-page `manuscript/main.pdf` has SHA-256
  `0bef46e936a25d8d0af1f3ea63a3cf60c8b5c982e46281d50a845a7ea5f88909`.
  `freeze-manuscript` succeeded with unchanged manuscript digest
  `8487aa4f23241b4179277a1ce3bdde7e416eebd1cfe23df81005e94282a62ca3`.
- Visual audit: `audit/visual.md` and `audit/visual.json`. Pages 1--3 were
  rendered at 180 dpi and each opened at original resolution. No clipping,
  overlap, illegibility, broken glyph, bad equation layout, or reference-wrap
  defect was found.

## Obstacles

No mathematical, citation, build, provenance, or visual obstacle remains. The
optional direct DOI/Crossref endpoint returned no usable audit-interface body,
but the authoritative Preprints.org record supplied matching metadata and full
text, so no citation remains unverified. The optional `qpdf` executable is not
installed; required PDF structure/text checks succeeded with `pdfinfo`,
`pdftotext`, the TeX engine, and the release gate.

## One next test

After this worker returns `ready`, let the supervisor run
`release_gate.py publish` and verify the resulting active manifest/PDF digest.
