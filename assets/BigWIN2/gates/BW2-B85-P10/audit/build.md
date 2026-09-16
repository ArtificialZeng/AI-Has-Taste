# Fresh build audit

Job: win-00085-p10-release-67ea8095309a. Checked 2026-09-12 UTC.

Accepted the final clean build after the canonical-source compatibility repairs.
From `manuscript/`, ran `latexmk -C -outdir=build main.tex`, then
`latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error -outdir=build main.tex`.
Both exited zero; full output is in `release-clean.log` and
`release-build-transcript.log`. The final converged LaTeX log is copied verbatim
to `release-final-latex.log`; the BibTeX log was also checked. Neither contains
warnings, undefined references/citations, overfull or underfull boxes, duplicate
entries, or fatal diagnostics. Early first-pass cross-reference messages in the
full transcript resolve during the normal latexmk reruns.

The bibliography/aux checker reports five cited and five defined keys, with
zero missing, unused, or unmatched entries (`release-bib-key-check.txt`). PDF
metadata has the correct title and Xiaojian Zeng as author. The six A4 pages
have extractable text, and all 22 listed font instances are embedded. The PDF
is unencrypted and has no JavaScript. The table and certificate checks, and the
full accepted verifier replay, passed; its JSON equals the frozen saved output.

All publication input hashes and the PDF are bound to the final manuscript
snapshot. This compilation result is not mathematical certification.
