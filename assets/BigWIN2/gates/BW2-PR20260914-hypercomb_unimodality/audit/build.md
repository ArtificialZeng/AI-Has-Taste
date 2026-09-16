# Fresh build audit

Verdict: accept. Release job: primary-20260914-hypercomb-unimodality-release-d6e0c44087b7. Reviewed at 2026-09-14T09:06:25.761861+00:00 (UTC).

A clean build was actually executed from the project root:

    bash manuscript/build.sh > audit/release-build-command.log 2>&1

The script first calls latexmk -C and then latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex from manuscript/. The command exited 0. Final compiler log: manuscript/build/main.log. Final BibTeX log: manuscript/build/main.blg. The complete command transcript is retained separately; initial unresolved references during multi-pass compilation were resolved before the final pass.

The real final logs were scanned and inspected: no LaTeX/BibTeX errors, undefined citations or cross-references, missing database entries, duplicate entries, overfull/underfull boxes, runaway arguments, undefined control sequences, or other warnings. The installed bibliography checker reports eight cited keys, eight bibliography entries and eight resolved auxiliary keys with no discrepancies; its actual output is audit/bib-key-check.txt. The generated bibliography agrees with the primary-record checks in audit/citations.md.

The PDF has six US-letter pages, PDF version 1.5, a valid PDF header and nonempty text extraction. It is unencrypted and has no JavaScript or form content according to pdfinfo. Creator/producer metadata identify LaTeX/hyperref and pdfTeX 1.40.22. Optional Title/Author/Subject/Keywords metadata fields are empty; the correct visible title and author were inspected on page 1. The fixed creation/modification timestamp comes from the documented SOURCE_DATE_EPOCH, not the date of the citation audit. No incorrect author or institution is encoded in PDF metadata.

Source dependencies were checked against publication.json, manuscript sources and the TeX recorder. main.aux, main.out and main.bbl are generated products; plain.bst and all style/package inputs are system resources. There are no undeclared authored inputs, figures or local custom styles. The verifier, README and build script are included in the publication source list as reproducibility companions.

Fresh execution of python3 manuscript/verify.py reproduced 388 parameter pairs, 958808 all-pair minors, 60 direct combinatorial comparisons, and coefficient-stream SHA-256 c4041b7d391d5246268ec7aef6eca1e610382bf38166766b261dda3b73db23a8, equal to the referee record. This is an exact finite replay, not a further independent proof. audit/release-verification.json contains the output.

The single prose change checked -> checkable was made before this clean build. The manuscript was then refrozen. The build log digest and current snapshot/PDF bindings are in audit/build.json. All protected mathematical inputs remain unchanged. The fresh rendered-page review is recorded separately in audit/visual.md.
