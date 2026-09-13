# Fresh build audit

## Binding

Release job `bigMac-00020-p01-release-80ff7c9383b6` audited evidence snapshot
`3647bf565806d5d07c7d5aaeea1ea8148576e5430042ef81a177c2acfb6b78c6`,
manuscript snapshot
`488892484bc96d7b34bbff749318870b687f20d1f27eafaeeb7f79d6da6d1515`,
and PDF
`367e110c905d90de5c2eb099cf1b67f3b2502ecd1643be94f530c6cd495f0542`.

## Compiler and log inspection

The existing nonempty compiler log is `manuscript/main.log`, SHA-256
`4282196828d1be9e7c66403c69944fa6ccef1559084a05f9d695b663b4db137d`.
It records successful production of a two-page, 268264-byte PDF. A fresh run of

```text
latexmk -cd -pdf -interaction=nonstopmode -halt-on-error manuscript/main.tex
```

reported that `main.pdf` is current and all targets are up to date, without
changing the bound PDF or log.

The full LaTeX and BibTeX logs were checked. They contain no compiler error,
fatal stop, unresolved citation or reference, rerun request, overfull or
underfull box, multiply defined label, or substantive package warning. The
`warning$ -- 0` line in `main.blg` records zero BibTeX warnings. BibTeX reads
`references.bib`, uses its one cited entry, and `main.aux` maps
`Dramburg2026` to `Dra26`.

## Output checks

- The PDF begins with `%PDF-` and ends with `%%EOF`.
- `pdfinfo` reports two unencrypted letter-sized pages and the intended title,
  author, and subject.
- `pdftotext -layout` extracts the title, theorem, proof, disclosure, and full
  bibliography as nonempty text.
- `pdffonts` reports all 18 fonts embedded, subsetted, and Unicode mapped.
- `main.fls` and `main.tex` show no undeclared authored input beyond the two
  files enumerated in `publication.json`.
- Recomputed evidence, source, PDF, and build-log hashes agree with both frozen
  snapshots and this audit's bindings.

**Verdict: accept.** The existing bound build log is clean and the PDF is a
successful build of the complete declared source set.
