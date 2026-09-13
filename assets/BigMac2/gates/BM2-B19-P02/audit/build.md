# Fresh clean-build audit

## Bound artifact

- Publication source snapshot:
  `15aef917056e90e131d160b5fe12d26f8fd959a9dd8c87352837427634080b70`
- PDF SHA-256:
  `e93effdcef1e2bcd89eca44c15aa105cb4c459227f5744fb9cf63985d171b88a`
- Build log: `manuscript/main.log`
- Build-log SHA-256:
  `f3cdac2e83991ee886d349337f0f258810f628bcf6121e4a00b98faf7d09d708`

## Clean build performed

From `manuscript/`, I ran a full `latexmk -C main.tex` cleanup and then the
declared command

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

with TeX Live 2026, pdfTeX 1.40.29, Latexmk 4.88, and BibTeX 0.99e.  The build
started without an auxiliary file, ran pdfLaTeX, BibTeX, and the required final
pdfLaTeX pass, exited zero, and reported all targets up to date.  The final log
is nonempty and ends with a four-page PDF output.

## Diagnostic inspection

The final compiler log contains no LaTeX/package warnings, no overfull or
underfull boxes, no undefined references or citations, no multiply defined
labels, no errors, no emergency stop, and no fatal diagnostic.  The BibTeX log
uses four entries and reports zero warning calls.  The final `.aux` maps all
four citation keys and the final `.bbl` contains all four corresponding
`\bibitem` records.  Cross-references to Theorem 1, Lemma 2, and Table 1 render
as resolved numbers.

The recorder file identifies `main.tex` and `references.bib` as the authored
TeX inputs; they are both listed in `publication.json`.  The same publication
list also includes every cited supplement source, exact enumeration log,
citation note, and designated bibliography record.  Generated `.aux`, `.bbl`,
`.blg`, `.fls`, and system TeX packages are build products or system inputs,
not omitted authored sources.

## PDF checks

The output starts with `%PDF-`, `pdfinfo` reports four letter-size unrotated
pages and the intended title, author, and subject metadata, and `pdftotext`
extracts 9,571 characters of nonempty text.  `pdffonts` reports every used font
as embedded and subsetted with Unicode mappings.  No source, evidence, or
accepted mathematical statement changed during the build; `source.md` remains
at its frozen SHA-256.

## Verdict

**Accept.**  This is a clean, resolved build bound to the current PDF and
current manuscript snapshot.
