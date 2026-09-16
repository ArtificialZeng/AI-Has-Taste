# PDF audit

Audit date: 2026-08-31 (Asia/Shanghai).

- Built `paper/main.tex` with `latexmk`, BibTeX, and repeated pdfLaTeX passes.
  The final log has no unresolved citation/reference, LaTeX error,
  overfull box, or underfull box diagnostic.
- `pdfinfo` reports the expected title, author Zijian Zeng, six letter-size
  pages, no encryption, no JavaScript, and no form fields.
- Extracted text was checked for forbidden release-body material: no digest,
  internal route/role identifier, completion/confidence score, or explicit AI
  audit language is present.  The exact-open limitation is present in the
  abstract, introduction, and limitations section.
- Pages 1--6 were rendered at 140 dpi and inspected individually.  Title,
  abstract, theorem statements, two-column count table, multiline sums,
  citations, section transitions, page numbers, references, affiliation, and
  both email addresses are legible.  No clipping, overlap, broken glyph,
  black box, orphaned heading, or malformed page boundary was found.
- The final PDF in `output/pdf/` is byte-identical to the release copy.
- The LaTeX ZIP contains no generated TeX artifacts, PDFs, bytecode, absolute
  paths, or redistributed third-party paper.  It passes archive integrity,
  builds from a fresh extraction with resolved references, and its
  self-contained exact numerical verifiers pass.  Instructions identify the
  cited external PDF required only for the optional 121-entry source
  transcription check.

Status: **passed**.
