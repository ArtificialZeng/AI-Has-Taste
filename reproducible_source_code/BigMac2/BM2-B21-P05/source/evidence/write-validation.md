# Manuscript validation

- Write job: `bigMac-00021-p05-write-fa1c8c702ee4`.
- Mathematical gate passed before drafting against accepted snapshot
  `9e7842d90ed58979a2ede4784ab0fc050c002d8ad19c4f615af4742d6e1ba13f`.
- Build command: `cd manuscript && latexmk -pdf -interaction=nonstopmode
  -halt-on-error article.tex`.
- The final build exited successfully. A case-insensitive scan of
  `manuscript/article.log` for warnings, overfull/underfull boxes, undefined
  references, and multiply-defined labels returned no matches.
- `manuscript/article.pdf` has three letter-size pages, descriptive PDF
  title/author/subject metadata, and embedded fonts. All three rendered pages
  were inspected at 130--150 dpi; no clipping, overlap, missing glyphs, or
  unreadable content was observed.
- A clean rerun of `evidence/verify_resolution.py` was byte-for-byte identical
  to `evidence/verify_resolution.out` (diff exit 0).
- `source.md` remained unchanged with SHA-256
  `ebbe264caf080f8158cce54870acfd5a01eddf57ddb0a704f6da2eaa51da5eab`.
- The manuscript freeze gate passed. The frozen PDF is
  `manuscript/article.pdf`; the generated freeze record is
  `audit/manuscript-snapshot.json`.

Citation-input limitation: `literature/user_bibliography_check.md` was absent.
This did not block the manuscript. The two directly relevant references and
the precise support available from the supplied primary-source PDF are recorded
in `manuscript/citation-notes.md` for the separate release audit.

The accepted `checkpoint.md` is itself a hashed file in `audit/snapshot.json`.
A trial content update caused `check-math` to report changed evidence, so the
accepted bytes were restored rather than invalidating the referee decision.
This file is the durable writing handoff instead.

Next test: a separate release reviewer should audit both citations against the
stated support, rebuild from the frozen TeX/BibTeX inputs, and repeat the
three-page visual inspection before any publication decision.
