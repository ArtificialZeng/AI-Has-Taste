# Fresh build audit

Release job: `bigMac-00015-p01-release-3bca604ddec1`  
Inspected build log: `manuscript/main.log`  
Build-log SHA-256: `0bba46c439ceefeb4a95678821996e5f0e07e7bcc3c7554038ffba1fb8ac3e5b`

The existing compiler log is a complete successful pdfLaTeX run for the
frozen sources.  It ends with `Output written on main.pdf (4 pages, 310309
bytes).`  Re-running the recorded `latexmk -pdf -interaction=nonstopmode
-halt-on-error main.tex` command reported that the current target is up to date
and did not change the source, PDF, or log digests.

## Diagnostics

- Fatal TeX errors: 0.
- LaTeX/package warnings: 0.
- Undefined citations or references: 0.
- Overfull boxes: 0.
- Underfull boxes: 0.
- BibTeX warnings: 0; `main.blg` records two entries used.
- `main.aux` contains the two expected `\citation` keys, corresponding
  `\bibcite` records, and a resolved `thm:main` label.
- The PDF begins with a valid PDF header, `pdfinfo` reports four unencrypted
  letter-size pages, and `pdftotext` extracts the complete article and both
  references.
- `pdffonts` lists 19 font subsets; every one is embedded and subsetted, with
  Unicode mapping present.

The `.fls` dependency trace confirms that the only authored project inputs are
`main.tex` and the bibliography that generated `main.bbl`; no local figure,
style, or imported TeX source is omitted from `publication.json`.

PDF document-info title and author fields are blank, while the visible title,
author, affiliation, email, and references are present and legible.  The blank
optional metadata fields do not affect compilation, identification of the
article, text extraction, or submission readiness; this is recorded as an
informational observation rather than a build defect.

## Verdict

**Accept.**  The existing bound build log is clean and corresponds to the
current frozen four-page PDF.

