# Build audit

The canonical manuscript was forcibly rebuilt from `manuscript/` with

```text
latexmk -g -pdf -interaction=nonstopmode -halt-on-error main.tex
```

BibTeX and pdfLaTeX converged after the expected intermediate pass caused by the citation-key change.  The final pass reports all targets up to date and writes a three-page PDF.  The retained final `manuscript/main.log` has SHA-256 `79fd1d3b4d81afebb3c1ca82f8c5c7efd55cf7c8c2bc2ecd4610276073413ab9` and contains no unresolved citation/reference warning, missing BibTeX entry, repeated entry, LaTeX error, fatal error, emergency stop, undefined control sequence, or runaway argument.

The final BibTeX/AUX audit found exactly three cited keys, all present in the canonical bibliography and AUX, with no unused entries.  `pdfinfo` identifies a valid unencrypted PDF 1.5 with three letter-sized pages.  `pdffonts` reports all fonts embedded and subsetted; text extraction is nonempty and contains no unresolved citation marker.
