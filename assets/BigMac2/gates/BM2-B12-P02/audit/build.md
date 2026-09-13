# Fresh clean-build audit

Verdict: accept. Job: `bigMac-00012-p02-release-436e003549d5`; date: 2026-09-08.

I ran `latexmk -C main.tex`, then
`latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` in `manuscript`.
Both exited zero; the complete execution transcript is `audit/build-transcript.txt`.
The final compiler log `manuscript/main.log` is nonempty, SHA-256
`13d3cec7aa9d07a3c9a368ffbf8b4735497cfeb7817dbb375bd97f9288580312`. There are no final LaTeX/package warnings,
undefined citations/references, overfull/underfull boxes or fatal diagnostics.
The package-description text “info/warning/error” is not a warning.
BibTeX's `warning$ -- 0` records zero warnings and all three entries were used.
Initial clean-build passes naturally request reruns; latexmk completed them and
the final log is clean.

PDF SHA-256: `6c8a138c1527970c728b130ea1a4258c9ca9480f17c8ee8ad0e981f3f276a4ab`. `pdfinfo` reports four letter-size,
unencrypted PDF 1.7 pages, correct title and Xiaojian Zeng author metadata;
`pdftotext` extraction is nonempty. All 24 fonts are embedded and subsetted.
Evidence is in `audit/pdfinfo.txt`, `audit/pdffonts.txt`, and
`audit/manuscript-text.txt`. Final references and all mathematical displays were
checked in the extracted text and actual page renders. No build defect remains.
The manuscript was refrozen after this rebuild; no source file was changed.
