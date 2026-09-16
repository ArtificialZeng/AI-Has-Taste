# Clean build audit

Verdict: accept. Job `newwin-00001-p05-release-df34904a6a33`; 2026-09-12T10:11:20.355939+00:00.

From `manuscript/`, executed `latexmk -C main.tex` and then `latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex`. Both succeeded. The full multipass transcript is `audit/release-build-full.log`; ordinary first-pass unresolved citations resolved after BibTeX and reruns. The accepted final-pass log is `audit/release-build.log`, with matching `audit/release-bibtex.log`. Neither contains warnings, undefined references/citations, duplicate entries, missing glyphs, overfull boxes or underfull boxes.

`check_bib_keys.py manuscript/main.tex --aux manuscript/main.aux` reports five active keys, five auxiliary keys, no missing or stale keys, and the one intentionally preserved uncited former comparison. `pdfinfo` reports a seven-page A4 PDF with the correct title and Xiaojian Zeng as author. `pdffonts` shows every font embedded and subsetted; no Type 3 fallback appears.

The unsupported listing configuration was replaced by standard footnotesize verbatim without changing the executable program. `audit/release-verification.json` verifies both its AST and all nonblank source lines against the companion file; the companion was rerun over the complete 28,800-input base. The PDF and all source inputs are frozen by `audit/manuscript-snapshot.json`. No mathematical input was modified.
