# Fresh clean-build audit

Release job: `bigMac-00004-p01-release-4826a634131d`

## Bindings

- Research snapshot: `079e9113bb882a88ac5c2f62f841b0780dcb2f54f2d7ae330c8f4ced81548137`
- Manuscript snapshot: `9248dc0364747cfc845571c546dbc900d90f0ceaa6dd2800c697b5fa3a3325ce`
- PDF SHA-256: `ca8b94bff18967835a2ea808ccbdd1b81166f640d1c001ec0b364116a4013e27`
- Build log: `manuscript/main.log`
- Build-log SHA-256: `5ee10f19555e0fa1614e15fa1851a48f4a014cd6996f0f67a10fc278fd6a806b`

## Checks

The existing clean build log is nonempty (26,514 bytes) and records a
successful pdfTeX completion: `Output written on main.pdf (6 pages, 342239
bytes).`  Inspection found no TeX error, fatal diagnostic, emergency stop,
undefined citation/reference, multiply defined label, overfull or underfull
box, package warning, or request for another rerun.  The only occurrence of
the string `rerun` is package identification/information from
`rerunfilecheck`; its final checksum says `main.out` did not change.

The BibTeX log names `references.bib`, reports three entries used, zero missing
fields, and `warning$ -- 0`.  The rendered bibliography contains exactly those
three cited works.  Cross-references to the theorem and propositions resolve in
both extracted text and the rendered pages.

`publication.json` lists the two complete authored inputs, `main.tex` and
`references.bib`.  Source inspection and the recorder file show no local
figure, custom style, or imported subsidiary TeX dependency.  All other inputs
are system TeX packages or generated auxiliaries.

The PDF begins with `%PDF-`, is unencrypted, has six letter-size pages, has
nonempty text extraction, and embeds every listed font.  `pdfinfo` and
`pdftotext` completed successfully.  The logged output size and the current PDF
size agree exactly.

## Verdict

Accept.  The existing build and bound log are clean, complete, and consistent
with the frozen manuscript and PDF.

