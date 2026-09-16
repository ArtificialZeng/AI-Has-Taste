# Clean-build audit

Verdict: **accept**. From `manuscript/`, the generated LaTeX state was cleaned
for release job `win-00066-p02-release-7cbcf9ae4463`.
with `latexmk -C main.tex`; the canonical publication command then ran
pdfLaTeX, BibTeX, and two convergent pdfLaTeX passes, all with
`-interaction=nonstopmode -halt-on-error`. The final PDF has four letter-size
pages.

The prescribed final `main.log`/`main.blg` scan found no undefined citation or
reference, missing database entry, BibTeX warning, repeated entry, LaTeX error,
fatal error, emergency stop, undefined control sequence, or runaway argument.
The bibliography checker found four cited keys, four BibTeX entries, and exact
AUX agreement. A 1.50 pt overfull-box diagnostic and several underfull-box
diagnostics occur in dense prose/table cells; original-resolution page review
confirmed that nothing crosses a margin, clips, overlaps, or becomes illegible.

`pdfinfo` reports the full title and author Xiaojian Zeng, no encryption, and a
text layer. `pdffonts` reports every listed font embedded and Unicode-mapped.
The final build log SHA-256 is
`5088748354a75fa6766b638951491e968c0098f906736e8a5dd54a14e31531b1`.
The canonical source, bibliography, evidence script, PDF, and publication
manifest are bound by `audit/manuscript-snapshot.json`.
