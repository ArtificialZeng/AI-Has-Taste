# Build audit

**Verdict: accept.** A fresh `latexmk -C` followed by a full PDF build from
`manuscript/` converged after BibTeX and produced the current three-page PDF.
The final `main.log` and `main.blg` contain no undefined citation/reference,
missing database entry, repeated entry, LaTeX error, BibTeX warning, overfull
box, or underfull box. The bibliography key checker reports matching eight-key
TeX, BibTeX, and AUX sets with no missing or unused entry.

`pdfinfo` reports a valid, unencrypted letter-size PDF with three pages and the
expected title, author, subject, and keywords. `pdffonts` reports all 28 listed
fonts embedded. The final log and PDF hashes are recorded in `audit/build.json`
and bound to the current manuscript snapshot.
