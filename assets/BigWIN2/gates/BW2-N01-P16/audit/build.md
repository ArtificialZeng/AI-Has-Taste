# Clean-build audit

Verdict: accept. Job `newwin-00001-p16-release-699cf5c87937`, 2026-09-12 UTC.
Bindings are recorded in `audit/build.json` and `audit/manuscript-snapshot.json`.

From manuscript/, the following commands both completed with exit status zero:

```sh
latexmk -C -outdir=build main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex
```

The clean and full compilation transcripts are `audit/release-clean.log` and
`audit/release-build-transcript.log`. The latter includes ordinary temporary
first-pass citation warnings before BibTeX runs. `audit/build.log` preserves the
converged final TeX and BibTeX logs: no undefined citations or references, LaTeX
warnings, BibTeX warnings, overfull/underfull boxes or fatal errors remain.

The canonical bibliography is manuscript/references.bib. The read-only key
checker passed with exactly five body/database/aux keys, with no missing or
unused entry; its output is `audit/bib-key-check.txt`. The .fls recorder's complete
local scholarly input set equals publication.json: manuscript/main.tex,
manuscript/references.bib and manuscript/build/main.bbl. Only installed standard
TeX packages, Latin Modern fonts and plain.bst are otherwise used.

The PDF has five A4 portrait pages, no encryption or JavaScript, the correct title
and author metadata, and embedded Type 1 fonts with Unicode mappings. Fresh text
extraction is `audit/release-pdf-text.txt`. The table transcription and all frozen
input hashes also passed `audit/release-check.py`; see `audit/release-checks.json`.
No dependency was installed. The build and snapshot do not constitute a proof.
