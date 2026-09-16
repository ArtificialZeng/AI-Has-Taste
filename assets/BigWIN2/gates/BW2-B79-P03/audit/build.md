# Clean build audit

## Verdict

**Accept.** The final canonical source was built from a clean state with:

```text
cd manuscript && latexmk -C && latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The converged build ran pdfLaTeX and BibTeX successfully and produced a
seven-page PDF. The final `manuscript/main.log` SHA-256 digest is
`2d5193425472f8589d6ce1b0986a5322f64bfd54e9ebc48999565f448a98f705`.

## Diagnostics checked

The final log and BibTeX log contain no LaTeX error, emergency stop, fatal error,
undefined citation, undefined reference, missing database entry, repeated-entry
diagnostic, or request for another rerun. A mechanical key comparison found eight
active TeX citation keys, eight bibliography entries, and eight resolved `.aux`
keys, with no missing or unused entry.

`pdfinfo` identifies the intended title and author, seven Letter-sized pages, and
an unencrypted PDF. `pdffonts` reports every listed font as embedded. Extracted
text is nonempty and contains the bibliography. Layout and legibility were
checked separately by rendering and viewing every page.

## Digest binding

- Accepted evidence snapshot: `71cb4c86fc33451424485a0b8d9495aa4e425cf029d346856d6018b998017a51`
- Manuscript digest: `da0af80f46244a58e7f156ed985226969c50873f465c1898f1590ed387903cea`
- PDF digest: `fa326ed2d297a3d497d3b1b01cd16d611b0104eda8adba40d916b4ea8bfc5dca`
- TeX digest: `ebf39cb363bd7858699116a08e48e686ba7f7bab7842f5b250fbf22714b36923`
- Bibliography digest: `bc8d2334e8eaa156c7b357837ea7512ce510072df3a97ed6febb2f17b11cf8fc`
