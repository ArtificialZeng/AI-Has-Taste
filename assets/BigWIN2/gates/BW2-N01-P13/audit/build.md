# Clean-build audit

**Verdict: accept.** Job `newwin-00001-p13-release-e80ab705955d`; UTC 2026-09-12T10:22:27.030551+00:00.

From `manuscript/`, the commands `latexmk -C -outdir=build main.tex` and `latexmk -pdf -outdir=build -interaction=nonstopmode -halt-on-error -file-line-error main.tex` both returned zero. The final converged log is `audit/release-build.log`; the complete clean/build transcript and command record are retained. No source or PDF was changed afterward.

The final LOG and BLG contain no undefined citation/reference, missing database entry, duplicate entry, LaTeX error, fatal error, warning, or overfull/underfull box. The supplied BibTeX checker, run on canonical main.tex and build/main.aux, found six cited keys, six bibliography entries and six AUX bindings, with no missing or unused keys. No citation keys were renamed.

The PDF has nine letter-sized pages. Its title and author metadata match the article. All 20 font records are embedded Type 1 fonts, with Unicode mappings and no missing-glyph warning. PDF extraction includes all six numbered bibliography entries. The manuscript includes its orbit table literally; the retained authoring companion is byte-identical to that block. The publication source inventory includes both, the canonical bibliography and generated BBL, so dependency scope is complete.

The current PDF was rendered at 110 dpi and every page actually inspected in this worker; visual findings are in `audit/visual.md`. Protected inputs and supplement hashes pass `audit/release-artifact-checks.json`.

Manuscript digest: `69f0c0877e7662597fc452e956d04ade99877f4da48524144a92a7980f33837e`. PDF digest: `03aafbb8438b545795ef0dce60b93227c846381a78d5f070d1a283b09eb6644d`. Build-log SHA-256: `4e342f4bd90c83c3d3e0174916e9fb9147c3402e18c7f19b682a6c4c829d1050`.
