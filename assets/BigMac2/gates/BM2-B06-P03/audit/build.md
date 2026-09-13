# Fresh build audit

Job: `bigMac-00006-p03-release-45c673bd9503`. Date: 2026-09-08.
Verdict: **accept**.

I inspected the actual existing clean build, not just its file presence or a
success flag. The complete TeX source, BBL/BibTeX inputs, final compiler log
`manuscript/main.log`, Biber log `manuscript/main.blg`, four-command transcript
`evidence/write-build-transcript.txt`, and command/return-code record
`evidence/write-build-commands.json` were checked. All frozen manuscript/PDF
hashes still match; no recompilation or refreeze was necessary in this review.

The clean sequence in `manuscript` was pdflatex, Biber, pdflatex, pdflatex.
All four recorded commands returned zero. The first pass, before Biber and
cross-reference convergence, contains expected temporary undefined references
and a box warning caused by a raw citation key. The penultimate pass requests
another LaTeX pass. These were resolved: the final transcript segment and the
actual final `main.log` contain no undefined citations/references, rerun
requests, fatal errors, missing glyphs, overfull or underfull boxes, or package
warnings. The Biber log reports two citekeys, loads `references.bib`, writes
`main.bbl`, and has no warning or error. The build audit binds the actual
**final compiler log**, rather than the multipass transcript with transient
first-pass diagnostics.

The final compiler output reports three pages and 345504 bytes, matching the
current `manuscript/main.pdf`. The PDF header, text extraction, page count,
unresolved-marker absence, exact citation key/database/BBL agreement, and
accepted-evidence/manuscript/PDF hashes were freshly checked by
`audit/release-validation.py`; its output is
`evidence/release-validation.json`. The real compiler log's SHA-256 is bound
in `audit/build.json`.

`pdfinfo` reports a readable unencrypted PDF 1.7, three upright US-letter pages,
with no JavaScript or form. The creator and producer are LaTeX with hyperref
and pdfTeX 1.40.29. Title/author metadata fields are empty rather than
incorrect; the visible title, byline, affiliation, and email are correct.
The file is not tagged for accessibility, which was not a requested release
requirement. `pdffonts` shows all 25 fonts embedded and subset, with Unicode
mapping and no Type 3 fonts. Full evidence is in
`evidence/release-pdfinfo.txt` and `evidence/release-fonts.txt`.

The build checker's initial transcript scan briefly matched `error -` inside
the command option `-halt-on-error -file-line-error`. That was a scanner false
positive, not a compiler diagnostic: the scanner now excludes the shell
command header and checks the actual compiler output. No manuscript, log,
or PDF content was changed to satisfy this check.

All three pages were separately rendered and visually inspected; see
`audit/visual.md`. A clean compiler log is not used as evidence of visual or
mathematical correctness.
