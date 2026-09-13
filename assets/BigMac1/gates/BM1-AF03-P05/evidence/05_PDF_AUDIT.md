# PDF audit

Date: 2026-08-29 (Asia/Shanghai)  
Artifact: `paper/main.pdf`  
Status: **PASS**

## Build and metadata

- Clean build command: `latexmk -C main.tex`, followed by
  `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` in `paper/`.
- Final `main.log` and `main.blg`: no warning, undefined citation/reference,
  error, overfull-box, or underfull-box match.
- LaTeX audit: `cited=5 bib=5 missing=0 unused=0`.
- PDF metadata title matches the paper title; PDF author is `Zijian Zeng`.
- Printed author block contains exactly the authorized author, affiliation,
  Malaysian address, and both authorized email addresses.
- Pages: 5; US letter; PDF 1.7; unencrypted; no JavaScript or forms.

## Visual inspection

All five pages were rendered with Poppler at 160 dpi and inspected at original
resolution after the final meaningful edit.  Checks passed for:

- no clipping, overlap, black boxes, missing glyphs, or unreadable text;
- correct overlines and zero/nonzero mathematical notation;
- legible route table and canonical graph6 identifiers, including `^`, `_`,
  `[`, and `{` characters;
- unbroken SHA-256 digest and command block;
- balanced final pagination, with references, affiliation, and email block on
  page 5 and no nearly empty trailing page.

Final SHA-256 values at this audit point:

| File | SHA-256 |
|---|---|
| `paper/main.tex` | `ec4ff6cbd8c6b28b1248122ffc468a0f98a2039a93fe164ba14fa64b24538c01` |
| `paper/references.bib` | `d0814d13bf1d527ecd224197b70e6d63a1b7737b16cde444038a54e2336f0d4d` |
| `paper/main.pdf` | `d271645951e7d5ee0844eabc7ac7bd9227a41cfaeac05cd77f8529fdb3048688` |
