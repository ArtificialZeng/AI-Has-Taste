# Fresh build audit

Verdict: accept. Job primary-20260914-vishnyakova-shifts-release-6f4d0d4e6d7f.

Final sources were built from a clean latexmk state. The actual commands and zero return codes are in release-build-execution.json; the complete transcript is release-clean-build.log. Normal transient first-pass references resolved in subsequent passes. The bound final compiler and BibTeX logs are release-final-build.log.

The final logs contain no fatal errors, undefined commands, unresolved citations/references, duplicate/missing BibTeX entries, or overfull/underfull/layout diagnostics. The final AUX passes the independent bibliography-key checker.

pdfinfo reports eight letter-size pages, correct title/author metadata, no encryption and no JavaScript. All 22 fonts are embedded Type 1 subsets. Text extraction is substantive. The recorder confirms all authored local TeX dependencies are declared in publication.json. See release-local-verification.json, release-pdfinfo.txt and release-pdffonts.txt.

The mathematical snapshot and original source are byte-identical. The only edits expanded section locators and removed redundant bibliography grouping for the selection parser. Final build and PDF digests are bound in build.json.
