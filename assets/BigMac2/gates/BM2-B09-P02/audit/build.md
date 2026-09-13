# Clean build audit

**Verdict:** accept  
**Checked:** 2026-09-07 (Asia/Shanghai)

A full cleanup was performed with
`latexmk -cd -C manuscript/main.tex`, followed by the command recorded in
`publication.json`:

`latexmk -cd -pdf -interaction=nonstopmode -halt-on-error manuscript/main.tex`

The clean build completed with exit status zero. Its initial LaTeX pass had
the expected unresolved citations and cross-references before BibTeX; BibTeX
and the required rerun resolved all of them. The final compiler transcript is
`manuscript/main.log`, SHA-256
`a2d7f8f600bade887aef940700f3132f8b4783b780a6160245e21c14ac9f9bb7`.
Inspection of that final log found no LaTeX warning, undefined citation or
reference, overfull/underfull box, fatal error, or emergency stop. The BibTeX
log reports two used entries and zero calls to `warning$`; the displayed
`missing$ -- 1` is BibTeX's built-in function-call counter, not a
missing-field diagnostic.

The final output is a 3-page A4 PDF with a valid PDF 1.7 header, nonempty text
extraction, and SHA-256
`ad60333710de1e83be0695f607468ff9441c2c4464072e5f595af695bf5d3852`.
All fonts reported by `pdffonts` are embedded, subsetted, and carry Unicode
maps. `pdfinfo` reports blank document-level Title and Author fields; the
visible title and author block are complete, and no target metadata policy was
specified, so this is recorded as a non-substantive metadata omission rather
than a build or identification defect.

The recorder file confirms that the only project-local authored inputs are
`manuscript/main.tex` and `manuscript/references.bib`, exactly as listed in
`publication.json`. The refreshed manuscript snapshot binds the current PDF
and these inputs.

