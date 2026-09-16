# Clean build audit

Release job: `primary-20260914-antiprism-total-positivity-release-0c9af236c4d2`. Date: 2026-09-14 UTC.

Verdict: **accept**. The actual clean rebuild from `manuscript/` was:

```sh
latexmk -gg -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=../build main.tex > ../build/release-build-driver.log 2>&1
```

The process exited zero. The final pdfLaTeX output is `build/main.pdf`, six pages, 285,653 bytes. The final compiler log `build/main.log` and BibTeX log `build/main.blg` were inspected for fatal errors, missing references/citations, database omissions, repeated entries, warnings and overfull/underfull boxes; none occurs. Initial-pass label messages in the driver transcript resolved on normal reruns. The final log, rather than an intermediate pass, is bound in `audit/build.json`.

The requested `check_bib_keys.py manuscript/main.tex --aux build/main.aux` reports one bibliography file, six cited keys, six entries, six AUX labels, and zero missing, unused or inconsistent keys. `pdftotext -layout` produced the readable six-page text at `audit/release-pdf.txt`; the reference list contains all six records and no unresolved markers. The actual PDF begins with the PDF header and `pdfinfo` reports an unencrypted six-page document. Title and author metadata are correct and contain no internal job identifiers.

`pdffonts` reports all 15 listed font instances embedded, subsetted, with Unicode mappings. The TeX recorder's project-local inputs are the main source and generated AUX/BBL/OUT files. System packages and system `plain.bst` account for the rest. The BibTeX database and the distributed companion program are both included in `publication.json`; no authored dependency is omitted.

After rebuilding, `release_gate.py freeze-manuscript .` succeeded. The exact current manuscript/PDF/evidence digests are copied into `audit/build.json`. No manuscript source or PDF was changed after that freeze. The clean build is a presentation and reproducibility check, not mathematical certification.
