# PDF audit

Final file: `results/order9_linegraph_signature.pdf`.

- Recompiled with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
- Final log has no undefined reference/citation, overfull/underfull box, or
  substantive package warning.
- PDF metadata title and author match the manuscript.
- 3 pages, US letter; every page rendered at 130 dpi under
  `audit/rendered_release/` and visually inspected.
- Equations, graph6 strings, tables, references, header, author address and
  email are legible; no clipping, overlap, black boxes or missing glyphs.

Verdict: PASS.

Root release review: the three rendered pages were inspected independently.
The searchable PDF text contains no prompt, model/vendor name, internal tool
disclosure, or checksum-like string.
