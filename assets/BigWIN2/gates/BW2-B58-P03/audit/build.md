# Build audit

Verdict: **accept**. A clean latexmk build from `manuscript/`, followed by the
normal convergence invocation, produced a five-page PDF. The final log digest
is `6b702859faf678fa5448098a150be565e72327bb9eef760702723c9caaa20e23`.
The required diagnostic scan is empty, and the citation-key checker reports
five cited keys, five bibliography keys, and exact AUX agreement.

`pdfinfo` reports the full title, author, subject, keywords, five letter-size
pages, no encryption, and extractable text. `pdffonts` reports every font
embedded with Unicode mapping.
