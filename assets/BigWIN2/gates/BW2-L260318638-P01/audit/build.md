# Build audit

Verdict: **accept**.

Release job: `lit-260318638-p01-release-5d1f71735d61`.

The final canonical manuscript was force-rebuilt from `manuscript/` with `latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex`. BibTeX ran against `references.bib`, followed by the required LaTeX passes, and `latexmk` reported that `main.pdf` was up to date.

The final log is nonempty and contains no fatal error, emergency stop, undefined citation, undefined reference, or rerun-required diagnostic. The ordinary body-flow, BibTeX database, and auxiliary citation-key sets are identical: `EldridgeEtAl2026`, `Humphreys1990`, `MalenRoldanToala2023`, and `ZengEtAl2026Finite`.

`pdfinfo` reports a valid five-page, unencrypted A4 PDF with extractable text and explicit title/author metadata. `pdffonts` reports every font embedded. The exact ancillary verifier also replayed successfully with assertions enabled; its bounded results are recorded in `audit/verifier-replay.json`.

Final digests:

- manuscript snapshot: `297be95a6b49fbc13d480f090b229c5d3b90a7a89e50cd4f401173a6ff21d50f`
- PDF: `edbcd7c26bc7bf3acf798cf17c166ce4aae16a75ee7a0ff99c9d110d5726beb6`
- build log: `0ea65d620ca4a1722a475902f6d900fe7f9c57a95d52bc1c36a90b1cf6757719`
