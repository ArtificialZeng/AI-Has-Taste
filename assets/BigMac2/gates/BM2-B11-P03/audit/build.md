# Clean-build audit

The publication was rebuilt on 2026-09-07 from a `latexmk -C` state with the
command recorded in `publication.json`:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`latexmk` ran pdfLaTeX, BibTeX, and the required reruns to convergence and
reported that `main.pdf` was up to date.  The final nonempty compiler log is
`manuscript/main.log`, SHA-256
`920c0666b7f91f318bca177a2e39c28a715e6187b3dabd50645e5c9b561ceb30`.

The final log and `main.blg` contain no fatal/error diagnostic, undefined
citation or reference, multiply-defined label, missing character, overfull or
underfull box, or rerun request.  BibTeX used exactly two entries and emitted
zero warnings.  `pdftotext` yields nonempty text, `pdfinfo` reports three
unencrypted letter-size pages, and `pdffonts` reports every font embedded.
PDF title and author metadata match the manuscript.

Verdict: **accept**.  This was a clean successful build with resolved
citations and cross-references.
