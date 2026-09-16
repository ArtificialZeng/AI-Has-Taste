# Clean build audit

The final source snapshot was built from a cleaned LaTeX state with

```text
cd manuscript
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`latexmk` converged after BibTeX and the required PDFLaTeX rerun.  The final
`manuscript/main.log` is nonempty and has SHA-256
`b114a4ec70b6cb1d6ffb7a8f172d989c5dd9ea63a07c51e0091663da61ef43ab`.
The final log and `main.blg` contain no fatal error, LaTeX error, undefined
citation, undefined cross-reference, missing BibTeX entry, repeated entry,
BibTeX warning, overfull box, or underfull box.  The bibliography checker
reports four cited keys and exact `.bib`/`.aux` agreement.

`pdfinfo` reports four unencrypted letter-size pages.  PDF title, author, and
subject metadata are populated.  `pdffonts` reports every used font embedded
and subsetted with Unicode mappings.

**Verdict: accept.**  The build is clean and reproducible from the declared
publication command.
