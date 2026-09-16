# Fresh build audit

Verdict: **accept**. Job:
`primary-20260912-stack22-mechanism-release-bd956129f546`.
UTC date: 2026-09-12.

From `manuscript`, the final sources were built with the installed toolchain:

```sh
latexmk -C -outdir=build main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
```

Both commands completed with exit status zero. Cleaning removed previous
generated inputs before the converged pdfLaTeX/BibTeX passes. The final output
is the canonical `manuscript/build/main.pdf`. Command output is preserved in
`audit/release-clean-command.log` and `audit/release-build-command.log`;
the final engine log is `manuscript/build/main.log` and the BibTeX log is
`manuscript/build/main.blg`.

The final logs contain no warnings, missing/undefined citations or references,
duplicate records, missing bibliography entries, errors, overfull or underfull
boxes. The citation-key checker reports six keys in the source, bibliography
and aux file, with no mismatch (`audit/bib-key-check.txt`). `plainurl.bst` and
all packages are installed toolchain dependencies. The two canonical source
files in `publication.json` cover the entire authored publication; the recorder
shows no additional authored TeX, figures or local style dependencies.

The supported standard `url` package replaces `xurl`, and a plain title plus
explicit metadata replaces the title's unsupported PDF-string helper. A long
Atkinson publisher link was replaced with its equivalent verified DOI URL,
which removed the initial bibliography spacing diagnostics. No mathematics was
changed. One intermediate command placed generated files in a duplicate nested
build folder; that generated folder was removed, and the final clean build used
the declared working directory and canonical output path. No superseded PDF is
among deliverables.

`pdfinfo` reports seven A4 pages, no encryption, no JavaScript, PDF version 1.5,
and the correct title and author. `pdffonts` shows all 19 fonts embedded,
subsetted and with Unicode mappings. Extracted text, citation numbers, theorem
references and all six bibliography entries are present. Evidence:
`audit/pdfinfo.txt`, `audit/pdffonts.txt`, `manuscript/build/main.txt`.

The final manuscript/PDF was refrozen before acceptance. `audit/build.json`
copies the current mathematical, manuscript and PDF digests from
`audit/manuscript-snapshot.json` and hashes the final engine log. All 14 frozen
mathematical inputs and the checkpoint remain byte-identical. This is a build
audit, not a proof or a public publication.
