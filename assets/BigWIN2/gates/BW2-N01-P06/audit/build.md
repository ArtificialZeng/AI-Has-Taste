# Clean build audit

PASS. Job `newwin-00001-p06-release-8c9ea9285eb1`, 2026-09-12 UTC. Manuscript `573155d648f7899400e851cb2492608a7a72d1c380e2a00cc6be30155780826d`; PDF `1d4d5f76dedc14044b6b0960650442dd054aa87bda00cb4e903c5468c49a8610`.

Started from the new empty `audit/recovery-clean-build/` directory with only the canonical main.tex and references.bib. Ran the four commands recorded in `audit/recovery-build-commands.json`: pdflatex, bibtex main, pdflatex, pdflatex. Every exit code was zero. Generated PDF, bibliography and final logs were copied to their canonical manuscript locations. Initial unresolved-reference messages are normal before BibTeX; the final converged logs were independently scanned and contain no citation/reference errors, missing or duplicate bibliography entries, warnings, overfull or underfull boxes, or fatal diagnostics.

The final combined log is `audit/recovery-build.log` (SHA-256 `b91375a307a2d456c2da3b5de4ed9219d1ab5d198a137b7b74d16c8eea07d04c`); the complete pass transcript is `audit/recovery-build-transcript.log`. The read-only bib-reference-audit key checker ran against main.tex and main.aux and reported five bibliography/citation/auxiliary keys, with zero missing, unused or extra keys (`audit/recovery-bib-check.txt`).

The PDF has five A4 pages, correct title and author metadata, and embedded fonts (`audit/recovery-pdfinfo.txt`, `audit/recovery-fonts.txt`). It has no JavaScript or encryption. All source dependencies in publication.json were checked: canonical TeX/BibTeX, the generated bbl, tables inlined exactly from tables.tex, README and 22-file exact companion. The companion archive was unchanged and byte-checked; mathematical inputs were untouched. No mathematical conclusion follows merely from successful compilation.
