# Build audit

Verdict: **accept**. Job: newwin-00001-p12-release-3b1ac840a39d

Final manuscript digest: `f6967d1b82942a4db6cdf29869eddc47ab55b32366a0b4d5dce2d7eaa4e52d7d`; PDF digest: `3127b814b3a9ba2b644ec69ad464bc100248db6d3a102006ff032851d54f9d73`.

The final clean build ran `latexmk -C -outdir=build main.tex` followed by `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex` from manuscript/. Both returned zero. The complete transcript is audit/release-build-transcript.log. Unmodified final-pass logs are audit/release-build.log and audit/release-bibtex.log. Earlier first-pass bootstrap diagnostics in the transcript converged; the final logs contain no warnings, undefined references/citations, overfull/underfull boxes or errors.

`python3 /home/ailab/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py manuscript/main.tex --aux manuscript/build/main.aux` passed: six cited keys, six bibliography entries, six aux labels, no missing or extra key. Bibliographic truth was audited separately, not inferred from this mechanical result.

Recorder inputs were checked against publication.json. The final TeX now contains the exact code and all 55 table rows inline; its only local typesetting inputs beyond main.tex are generated main.bbl, main.aux and main.out. The canonical references.bib and retained companion census.py/shape-table.tex are explicitly enumerated publication sources, and the inline copies match them exactly in every code line and numerical row. Standard TeX Live packages are environment dependencies, with no package installation.

PDF metadata reports the intended title and author, eight A4 pages, no encryption and no JavaScript. Every listed font is embedded and subsetted. All eight pages contain readable extracted text. Detailed machine evidence is audit/release-build-check.json; pdfinfo and font reports are audit/release-pdfinfo.txt and audit/release-fonts.txt. These checks do not substitute for the actual visual review.
