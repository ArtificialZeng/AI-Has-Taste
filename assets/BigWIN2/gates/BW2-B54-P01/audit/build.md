# Clean build audit

## Result

**PASS.**  A clean build was performed in `manuscript/` by removing generated
LaTeX artifacts with `latexmk -C main.tex`, compiling with the publication
command, and then recording a forced converged run in `audit/build.log`:

```text
latexmk -g -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The final run executed BibTeX and pdfLaTeX successfully and produced a four-page
PDF.  The final `main.log` and `main.blg` contain none of the following:
undefined citations or references, missing database entries, BibTeX warnings,
repeated entries, LaTeX errors, fatal errors, emergency stops, undefined control
sequences, runaway arguments, or overfull/underfull boxes.

The bibliography consistency checker reports eight cited keys, eight database
keys, eight `.aux` keys, no missing key, no unused entry, and no `.aux` mismatch.
All references and equation/theorem cross-references are resolved.  `pdfinfo`,
`pdftotext`, `pdffonts`, and `pdftoppm` all parse the output, and `pdffonts`
reports that every one of the 19 Latin Modern or AMS font subsets is embedded;
no bitmap image dependency occurs.  `qpdf` is not installed, so no `qpdf` result
is claimed or used by this audit.

PDF metadata was inspected with `pdfinfo`: the producer is pdfTeX 1.40.22, the
creator is LaTeX with hyperref, the page size is US letter, the file is unencrypted,
and it has four pages.  Title, subject, and author metadata fields are blank; the
corresponding information is visibly present on page 1, so this is not a content,
identification, accessibility, or build blocker.

Snapshot bindings:

- accepted mathematics: `49a052feaeae6b3876006ac5ed12f5a9351fab520a15b89424a8ee069a18676b`
- manuscript sources: `3ef31c061e0471a2b07338f2d30037c1e06e5d50164a003622a7edf21d4ed241`
- final PDF: `69c7f8c4e0f06f3b9d9d3d029144fb2327a61dbae6dd5cf4a2b102c561954568`
- recorded build log: `d6a9231c8ef2c38f059e79bd27e4fe8397e4737191e2e625de08243a83c24ec6`
