# Fresh build audit

The current compiled artifact is `manuscript/article.pdf`, bound to PDF digest
`a4d13aa84c9372f466abb5f6b0d4a4127e11b4f3499b010b68708784c29f59d9`
and manuscript digest
`eb00feeb1d21ef170e521b805881d769bca7fc11dd6ea8211719eadb6a32d36b`.

I inspected the nonempty compiler log `manuscript/article.log` byte-for-byte
at SHA-256
`72a47380e34e1b829c7795803ff3eb095c397d510de4f69b93ed4b7fe6b7951c`.
It records a successful pdfTeX run, reads the resolved `article.bbl`, completes
all five pages, and ends with `Output written on article.pdf (5 pages, 348184
bytes).`

Targeted checks of `article.log`, `article.blg`, `article.aux` and
`article.bbl` found:

- no LaTeX, pdfTeX or BibTeX error or fatal diagnostic;
- no undefined or multiply-defined citation, reference or label;
- no rerun-needed warning;
- no overfull or underfull box warning;
- BibTeX reports `warning$ -- 0` and resolves all three cited keys;
- the PDF metadata title, author and subject agree with the manuscript, and
  `pdftotext` returns nonempty text from all pages;
- `pdffonts` reports every listed font as embedded and subsetted.

The package-name occurrences `infwarerr`, `refcount` and `rerunfilecheck` are
ordinary package information, not warnings.  The build is clean.

**Verdict: accept.**
