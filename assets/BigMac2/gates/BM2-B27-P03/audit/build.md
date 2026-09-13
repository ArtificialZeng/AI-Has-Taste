# Fresh build audit

## Bound artifact

This audit is bound to evidence snapshot
`67a9ad102f9c06b2ad1eb8ba87fc50c7e8788ce28044350978f67f60278681dc`,
manuscript digest
`82323397713c1a4e2b0f6cabbf4c9f9b92e0451d318f396c0823c94fcdde45c8`,
and PDF digest
`ff88f4f1cd608d26134d5ed87844085916170e844a65e79d7fa88364cf8396f9`.

## Clean compilation

From `manuscript/`, I removed generated LaTeX intermediates with
`latexmk -C main.tex` and ran

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

to completion.  After the clean build resolved its expected first-pass
cross-references, I forced a fresh confirmation compilation with `latexmk -g`.
The complete confirmation transcript is `evidence/release_build.log`, SHA-256
`fd8083c79f65b34deb20b8ba224e8037aa19092d19d0e4a445ccc343f7af5ca4`.
It ends with all targets up to date and contains no LaTeX/package warning,
undefined citation or reference, error, emergency stop, overfull box, or
underfull box.  The final `manuscript/main.log` and `manuscript/main.blg` were
also inspected; BibTeX reports four entries and zero warnings.

All theorem, lemma, and equation cross-references resolve.  All four citation
keys in `main.tex` occur in `references.bib` and in the generated `main.bbl`.
The dependency trace contains no authored input beyond the two files listed in
`publication.json`; `main.bbl` and other auxiliary files are generated outputs.

## PDF checks

- `manuscript/main.pdf` has a valid PDF 1.7 header, is unencrypted, and has four
  US-letter pages.
- `pdftotext -layout` produced 10,152 nonempty bytes and no unresolved-marker
  pattern.
- The title, author, subject, and keywords metadata match `main.tex`.
- `pdffonts` lists only embedded, subsetted Latin Modern and AMS fonts, with
  Unicode mappings.
- The compiled size is 302,927 bytes.  The PDF SHA-256 is the bound digest
  above.

## Verdict

**Accept.** The current source has a clean, reproducible compilation with
resolved references and citations, a clean bound build log, embedded fonts,
and a structurally valid text-extractable PDF.
