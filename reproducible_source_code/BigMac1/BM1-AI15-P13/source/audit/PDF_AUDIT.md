# PDF audit

Audit date: 2026-08-29 (Asia/Shanghai)

Outcome: **PASS.**

- A full `latexmk -C` followed by a clean `latexmk -pdf` build completed.
- The final log is preserved as `logs/clean_build.log`.
- `audit_latex.py` passed; the final log scan found no undefined references or
  citations, multiply-defined labels, package warnings, overfull boxes, or
  underfull boxes.
- The final PDF has 6 letter-size pages, is unencrypted, and contains no forms,
  JavaScript, or suspect objects according to `pdfinfo`.
- `pdftotext` recovered the theorem, verifier commands, disclosure, reference,
  affiliation, and email from the final file.
- All six pages were rendered at 150 dpi with Poppler and inspected
  individually. No clipping, overlap, missing glyph, broken equation,
  truncated command, or anomalous blank page was observed.
- `paper/main.pdf` and
  `output/pdf/sm_ir_fixed_point_counterexample.pdf` are byte-identical.
- Final PDF SHA-256:
  `24dabee471d37e8995e58ec9010f6873a131d7bd587a7a5e54fca0a4823e931e`.

The visual inspection was repeated after the fail-closed verifier, source
operation-order, tamper-suite, and guarded-variant scope text was frozen. It
covered the title/abstract, operation graph, both counterexamples, structural
lemmas, recurrence, reproducibility block, bibliography, and author block.
