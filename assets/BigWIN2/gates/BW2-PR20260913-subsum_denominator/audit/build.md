# Clean build review

Job: `primary-20260913-subsum-denominator-release-2b584cd00e77`. Reviewed 2026-09-13T01:07:03.134033+00:00.

A clean `sh manuscript/build.sh` removed the prior build, ran latexmk/pdfTeX/BibTeX and a final pdfTeX convergence pass. Exit status was zero; the final PDF has seven pages. The initial review found a cross-reference rerun warning after latexmk, which a final pass resolved. The script now includes that pass, and a new clean build was actually executed. `audit/release-build-transcript.log` preserves the full run.

The final `manuscript/build/main.log` and `main.blg` have no warnings, undefined citations/references, missing/duplicate BibTeX entries, fatal diagnostics or overfull/underfull boxes. The installed bib checker reports five body keys, five bibliography entries and five matching AUX entries, with no missing or unused entries. All referenced labels were checked against the generated AUX and printed pages.

The recorder has only main.tex as an authored TeX input, the declared canonical bibliography generates the BBL, and the five publication source files cover the README, builder, TeX, bibliography and companion program. All nineteen PDF font subsets are embedded with Unicode mappings. The title and Xiaojian Zeng author metadata now match the title page; the subject states conjecture-note scope and unresolved original status. Letter page size is consistent; no encryption or JavaScript is present.

The companion exact verifier completed successfully in 18.347 seconds and reproduced all 613137 dense coefficients and 3126 earlier cases. This rerun is a reproduction of an existing verifier, not a newly independent proof. No source/claim/checkpoint or accepted mathematical evidence changed.
