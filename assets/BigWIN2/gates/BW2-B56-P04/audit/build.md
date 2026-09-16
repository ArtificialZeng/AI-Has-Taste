# Fresh build audit

- Job: `win-00056-p04-release-abe5976d40e2`.
- Command: `latexmk -gg -pdf -interaction=nonstopmode -halt-on-error main.tex`
  from `manuscript/`.
- Result: success after the normal BibTeX and converging LaTeX passes.
- Output: `manuscript/main.pdf`, five pages, SHA-256
  `0fa9bf6381c47f17b4ce7fc472f9ca5b4070beac99e2ad8bc8d8d9683836f1cf`.
- Final log: `manuscript/main.log`, SHA-256
  `25e9c68f759a8fb742cfa509a85d2b525a1f88a6df9a04bde603eb8eda12c49c`.
- Log scan: no undefined references/citations, missing database entries,
  repeated entries, BibTeX warnings, LaTeX/package warnings, errors, fatal
  stops, overfull boxes, or underfull boxes.
- `check_bib_keys.py` found four cited keys, four bibliography entries, and
  exact agreement among source, bibliography, and final auxiliary file.
- `pdfinfo` and `pdftotext` both succeeded; the PDF has a valid header and
  extractable text.

Verdict: **accept**.
