# Fresh clean-build audit

Date: 2026-09-08. Job: bigMac-00014-p04-release-05b975bda9df.
Verdict: accept.

Ran from manuscript/: `latexmk -C main.tex`, then `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`. This removed old generated output and rebuilt from the declared source. The build completed with exit code 0, two pdfLaTeX passes, and a four-page 285719-byte PDF. The complete run is retained in audit/release-build-transcript.log; the bound final compiler log is manuscript/main.log.

Inspected the final compiler log and recorder. There are no LaTeX errors, fatal errors, missing characters, undefined references/citations, overfull boxes, underfull boxes, or pending rerun warnings in the final log. Initial-pass unresolved references in the full transcript are expected after cleanup and are all resolved on the final pass. Both bibliography keys and all theorem/lemma/equation references are resolved in the extracted and rendered PDF.

The sole authored source is manuscript/main.tex. main.aux and main.out are generated inputs; all other recorder inputs are system TeX files. No external bibliography build is needed because the bibliography is inline.

`pdfinfo` reports four letter-size pages, a nonencrypted PDF 1.7, the intended title and Xiaojian Zeng author/affiliation metadata, no form and no JavaScript. `pdffonts` shows 18 font subsets, all embedded with Unicode mappings. pdftotext extracted text from all four pages. Metadata and font inventory are retained in audit/pdfinfo.txt and audit/pdffonts.txt; text is audit/rendered/manuscript.txt.

The accepted proof and manuscript source were not changed. The rebuild changed the PDF digest, so freeze-manuscript was rerun before generating all three fresh audits. The final build log's SHA-256 is recorded in audit/build.json. Exact certificate replay was also run to a separate audit output and matches the frozen verification bytes; it did not modify accepted evidence.
