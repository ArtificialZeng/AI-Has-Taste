# Fresh clean-build audit

Verdict: **accept**. Job: `primary-20260914-grid-narayana-release-a978c20a048a`.
UTC date: 2026-09-13. Output: `build/main.pdf`, six pages.

From `manuscript/`, the release worker actually ran:

```sh
latexmk -C -outdir=../build main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error -pdflatex='pdflatex -no-shell-escape -recorder %O %S' -outdir=../build main.tex
```

Both commands exited zero. `audit/release-build-transcript.log` preserves the clean removal and complete build, including ordinary initial unresolved-reference passes. The converged engine log `build/main.log` and BibTeX log `build/main.blg` were inspected; neither contains warnings, undefined references/citations, missing database entries, repeated entries, compilation failures, or overfull/underfull boxes. The build audit binds the final engine log by its SHA-256.

The requested bibliography checker was run with `manuscript/main.tex --aux build/main.aux`: five cited keys, five bibliography entries, five auxiliary bibliography labels, and no missing files, missing keys, unused entries, or auxiliary mismatches. Its final output is saved in `audit/bib-key-check.txt`.

`publication.json` lists exactly the authored compiler inputs `manuscript/main.tex` and `manuscript/references.bib`. The recorder identifies no other local authored TeX dependency; `main.aux`, `main.bbl`, and `main.out` are generated. The BibTeX log identifies `references.bib` and standard `plain.bst`. Other dependencies are installed TeX resources. No shell escape, custom style, external generated figure, or code execution enters the paper build.

`pdfinfo` confirms a valid unencrypted six-page PDF, letter page size, correct title and author, and no JavaScript. `pdffonts` lists 17 embedded, subsetted fonts with Unicode mappings; no missing font was observed. `pdftotext -layout` yields nonempty readable text, saved in `audit/release-pdf-text.txt`. Metadata/font output is saved in `audit/pdf-metadata.txt`.

The final source and PDF were frozen after the metadata and presentation repairs. `audit/manuscript-snapshot.json` supplies the digest bindings copied to `audit/build.json`. No source or PDF change followed that freeze. Every protected mathematical input and the frozen checkpoint retained its original hash. Clean compilation checks presentation and consistency; mathematical acceptance comes from the unchanged referee report.
