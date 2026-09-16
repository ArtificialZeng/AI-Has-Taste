# Fresh build audit

Release job `win-00070-p02-release-7fa60259311e`; checked 2026-09-08.

From `manuscript/`, I removed generated LaTeX products with
`latexmk -C main.tex` and performed a fresh non-interactive build with
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. Latexmk ran
pdfLaTeX, BibTeX, and a converging second pdfLaTeX pass, then reported all
targets up to date. The resulting PDF has four letter-size pages and SHA-256
`57c6e200d7ac574e379774f84a9e25e395949aa6891ac9580fddc2d024121785`.

The read-only bibliography consistency checker reported four cited keys, four
BibTeX keys, no missing or unused entries, and exact AUX agreement. A final
diagnostic scan of `manuscript/main.log` and `manuscript/main.blg` found no
undefined citations/references, missing database entries, BibTeX warnings,
repeated entries, LaTeX errors, fatal errors, emergency stops, undefined
control sequences, or runaway arguments.

`pdfinfo` recognized a valid four-page PDF with extractable text. Its metadata
identifies LaTeX/pdfTeX as creator/producer, contains no stale title or author,
and reports no encryption, form, JavaScript, or suspect content. All nineteen
fonts reported by `pdffonts` are embedded subsets with Unicode mappings.

Verdict: **accept**; clean build completed with no unresolved diagnostics.
