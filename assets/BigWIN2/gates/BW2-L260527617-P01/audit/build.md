# Clean-build audit

## Binding and verdict

- Release job: `lit-260527617-p01-release-4b162acd588d`
- Frozen mathematical snapshot: `95cd9fcb261ad6fe4df05945af76955e312cda7ba75fce350ac973bbca29f6cf`
- Manuscript digest: `9a63259426e3187bf462df2c2662be51389cb663c1ee497f22834586b3fec9b5`
- PDF digest: `b1523fd8749b16a0c9b2baee2c29b7251c8f6f9887af37614338aa38a6843646`
- Final log digest: `317836eefd7ad75609ef121c49eefccd55442cf687a3a5be7717a3d55c243944`

**Verdict: accept.** A clean noninteractive `latexmk` build converged and
produced the bound six-page PDF. The build used latexmk 4.76, pdfTeX 1.40.22,
and BibTeX 0.99d with canonical `references.bib`.

The final log contains no TeX error, fatal diagnostic, undefined control
sequence, undefined citation, undefined reference, or rerun request. The
BibTeX log has no missing or repeated entry and no warning. The bibliography
checker reports eight cited keys, eight entries, zero missing or unused keys,
and exact auxiliary-file agreement. `pdfinfo` recognizes an unencrypted
six-page letter-size PDF with the intended title and author; `pdffonts` reports
all fonts embedded with Unicode maps; `pdftotext` extracts nonempty text. The
regenerated PDF was refrozen before these release-audit bindings were written.
