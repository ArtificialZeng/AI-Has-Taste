# Clean build audit

The frozen clean build was produced during citation attempt 6 after `latexmk -C`
removed generated build products.  The first canonical
`latexmk -pdf -interaction=nonstopmode -halt-on-error
main.tex` invocation stopped after its initial pdfLaTeX pass with a transient
recorder diagnostic.  Without changing any source, an immediate invocation of
the same canonical command ran BibTeX and two final pdfLaTeX passes, exited 0,
and reported all targets up to date.  The resulting clean-cycle output is a
five-page PDF.

For release job `win-00068-p02-release-ad1c2e39c442`, citation attempt 7,
launch `19e4b0d4-8102-47fd-98db-15f8d58d6f9f`, every fast-handoff source,
bibliography, publication-manifest, PDF, and snapshot digest remained exact.
Accordingly this recovery did not rebuild or refreeze.  I freshly recomputed the
converged build-log SHA-256 as
`6e816382fe13f8e3905fd1089267f175b5212336d84c859ffc895a367a2ade68`
and replayed the checks below against the unchanged clean-build artifacts.

The bibliography consistency checker reported 7 cited keys, 7 bibliography
keys, no missing or unused entries, and exact agreement with `main.aux`.
Scanning the converged `manuscript/main.log` and `manuscript/main.blg` found no
undefined citations or references, missing database entries, duplicate entries,
BibTeX warnings, LaTeX errors, fatal errors, emergency stops, undefined control
sequences, or runaway arguments.

`pdfinfo` reports the intended title and author, five letter-size unrotated
pages and no encryption.  `pdffonts` reports every listed font embedded.
Cross-references, theorem and lemma labels, mathematical symbols, graph6
strings, tables, bibliography, and metadata are present.  The converged clean
build is accepted.
