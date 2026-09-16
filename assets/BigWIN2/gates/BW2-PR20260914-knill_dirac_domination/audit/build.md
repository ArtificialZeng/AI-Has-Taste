# Fresh build audit

Release job `primary-20260914-knill-dirac-domination-release-2935067edeff`.
Date: 2026-09-14 UTC. Verdict: **accept** for the current snapshot.

The final clean build was actually executed as
`bash manuscript/build.sh > build/release-latexmk-console.log 2>&1` and exited 0.
The script first runs `latexmk -C`, then pdfLaTeX/BibTeX through latexmk with
nonstop, halt-on-error, file-line-error and recorder options. The final run
followed all source changes. The complete final compiler log is
`build/main.log`; its SHA-256 is bound in `audit/build.json`.

The fresh selection validator rejected the otherwise valid TeX controls
`square` and `begingroup`. The only source edits replaced the proof-end glyph
with amsthm's `qed` and removed redundant grouping around the final ragged-right
bibliography. Mathematical text, citation keys, references and research evidence
were unchanged. These are compatibility repairs, not changes to the validator.

The final `.log` and `.blg` contain no errors, unresolved references/citations,
database omissions, repeated entries, package/LaTeX warnings or overfull/underfull
boxes. BibTeX reports seven used entries and zero warnings. The skill's read-only
`check_bib_keys.py manuscript/main.tex --aux build/main.aux` confirms seven
matching source, bibliography and auxiliary keys, with no missing or extra keys.

`pdfinfo build/main.pdf` reports five A4 pages, PDF 1.5, correct title and author,
no encryption and no JavaScript. The PDF has a valid header and nonempty text;
`pdftotext -layout` was saved as `audit/release-pdf-text.txt`. `pdffonts` shows all
18 listed font resources embedded and subset, with Unicode maps. Equation and
reference labels are resolved in both extraction and page images.

The TeX recorder and BibTeX log establish the complete authored dependency list:
`manuscript/main.tex` and `manuscript/references.bib`. Other local recorder inputs
are generated intermediates. No local custom style, figure or imported TeX file
is missing from `publication.json`. The final `freeze-manuscript` succeeded;
its real output is in `audit/release-freeze.json`. This report and the build JSON
refer to that same current source/PDF snapshot. Final release-gate execution is
left until all reports and reviews are complete.
