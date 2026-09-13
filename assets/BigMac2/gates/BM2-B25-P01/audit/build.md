# Fresh clean-build audit

## Build performed

From `manuscript/`, I ran a full `latexmk -C main.tex` cleanup followed by:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The clean build ran pdfLaTeX, BibTeX, and the required settling pdfLaTeX pass,
then reported all targets current.  The final compiler transcript is the
nonempty project-relative file `manuscript/main.log`, SHA-256
`ace0c8e41e3b63aed9ab3909be6766da64398f51c6b1fb874828cf9a2d143db8`.
The BibTeX log reports zero warnings.

## Final-log and artifact checks

- The final log has no LaTeX/package warnings, compilation errors, undefined
  citations or references, rerun request, overfull/underfull box, or fatal
  diagnostic.  First-pass transient messages are absent from the final log.
- Cross-references, theorem/table/appendix labels, and the sole bibliography
  key resolve in both the final log and extracted PDF.
- The recorder file identifies `main.tex` and `references.bib` as the complete
  project-local authored inputs; this agrees with `publication.json`.
- `manuscript/main.pdf` has a valid PDF 1.7 header, four letter-size pages,
  nonempty text extraction (7901 bytes in the audit extraction), and SHA-256
  `c75ffad4013ac083705fe012b4fe30361eebae03896bb57206471489954bb020`.
- All 23 listed fonts are embedded subsets.  PDF Info identifies pdfTeX and
  LaTeX/hyperref as producer/creator; no inaccurate title, author, subject, or
  keywords metadata are embedded.
- The immutable `source.md` still has SHA-256
  `ea3d097839f8cdfdfcd8a59c1df8afb91c7c37250f6bef314a0a0f9eda58ff4f`.

**Verdict: accept; clean build confirmed.**

