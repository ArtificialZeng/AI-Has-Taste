# PDF audit

Audit date: 2026-08-29.

Status: **passed**.

- Clean build: `latexmk -C main.tex` followed by
  `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
- Build result: six pages, no undefined citations/references, no BibTeX
  warnings, and no overfull or underfull boxes in the final log.
- Metadata: title `Generic Lotka–Volterra Tree Systems Determine Their Trees`;
  author `Zijian Zeng`; letter paper; PDF 1.7; unencrypted; no JavaScript.
- Text extraction: title, theorem, certificate hash, disclosure, bibliography,
  affiliation, and both email addresses are present and readable.
- Visual inspection: every rendered page 1--6 was checked at 144 dpi.  No
  clipping, collision, missing glyph, malformed formula, table overflow,
  broken URL, or unreadable footer was found.
- Authorship check: only Zijian Zeng is listed as author.  The required UCSI
  affiliation and both required email addresses appear on page 6.
- Proof-assistant disclosure: page 6 explicitly says that no Lean, Coq,
  Isabelle, or other proof assistant was used.

Final pre-release PDF SHA-256:

```text
24959453f24bc7c50cd2578e95f52389de140fae3665af9e1d24d226bfc97e47
```
