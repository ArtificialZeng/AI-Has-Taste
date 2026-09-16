# Fresh build audit

Release job `win-00077-p01-release-1b135af2eacf`; checked 2026-09-09 UTC.

From `manuscript/`, I removed generated LaTeX products with
`latexmk -C main.tex` and performed a fresh non-interactive build with
`latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error
main.tex`. Latexmk ran pdfLaTeX, BibTeX, and a converging second pdfLaTeX pass,
then reported all targets up to date. The resulting PDF has two letter-size
pages and SHA-256
`ff87e7ba25522932028403bfd37dfef39e1e7de2b7580776aa0adbbab71d72bc`.

The read-only bibliography checker reported three cited keys, three BibTeX
entries, no missing or unused entry, and exact AUX agreement. A final
diagnostic scan of `manuscript/main.log` and `manuscript/main.blg` found no
undefined citations or references, missing database entries, BibTeX warnings,
repeated entries, LaTeX errors, fatal errors, emergency stops, undefined
control sequences, or runaway arguments.

`pdfinfo` recognized a valid two-page, unencrypted PDF with extractable text,
no forms, JavaScript, or suspect content. `pdffonts` reported 23 font subsets;
all are embedded and all have Unicode mappings.

Verdict: **accept**; the clean build completed and converged without an
unresolved diagnostic.
