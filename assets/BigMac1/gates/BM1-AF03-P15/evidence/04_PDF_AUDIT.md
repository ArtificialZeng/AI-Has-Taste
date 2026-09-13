# PDF audit

Audit date: 2026-08-29 (Asia/Shanghai)  
Artifact: `output/pdf/d9_normalized_flow.pdf`  
Decision: **PASS**

## Build and structure

- Clean build command: `latexmk -pdf -interaction=nonstopmode
  -halt-on-error -file-line-error -outdir=../.build/latex main.tex`, run from
  `paper/` with `SOURCE_DATE_EPOCH=1788000000` and `FORCE_SOURCE_DATE=1`.
- Build result: exit 0; 6 pages; no unresolved citations or references; no
  overfull/underfull boxes; no LaTeX warnings in the final log.
- Bibliography audit: 2 cited keys, 2 BibTeX keys, 2 `.aux` keys; missing 0,
  unused 0.
- LaTeX audit: `cited=2 bib=2 missing=0 unused=0`.
- PDF metadata: title *A certified normalized flow for the absolute order of
  type D9*; author `Zijian Zeng`; letter size; PDF 1.7; unencrypted; no forms,
  JavaScript, rotation, or suspect objects.
- File size: 377,572 bytes.
- SHA-256:
  `c8741981935f22594dcc944e2981b166b1084f58cf6d59c455ecb9f02c08d184`.
- Exactly one PDF is present under `output/`.

The PDF skill's required operation-marker command was invoked exactly once
immediately before the first PDF build.  This local macOS workspace did not
contain `container_tools/mark_artifact_operation_started.mjs`, so the hook
reported `MODULE_NOT_FOUND`.  This is recorded as an environment/tooling
limitation; the subsequent LaTeX build and the mathematical checks were not
affected.

## Page-by-page visual inspection

Each page was rendered at 150 dpi with Poppler and inspected at original
render resolution.

| page | visual contents | result |
|---:|---|---|
| 1 | title, sole author, abstract, introduction, theorem, bounded novelty wording | PASS -- centered title block, readable abstract, no clipping or collision |
| 2 | finite endpoint, normalized-flow equations, automorphism action | PASS -- displayed formulas and proof ending fit the text block |
| 3 | signed-cycle classification, Carter applicability, rank vectors, cover types | PASS -- citations, equation labels, and long rank data are legible and contained |
| 4 | five multiplicity cases, edge conservation, quotient-lifting lemma | PASS -- cases display and all equations fit with clear spacing |
| 5 | frozen hashes, exact layer table, independent-verifier description | PASS -- table columns align and remain inside margins; file paths wrap safely |
| 6 | mutation audit, theorem proof, reproduction commands, limitations, references, affiliation and both emails | PASS -- no orphaned headings, truncation, or footer collision |

## Text and identity checks

Poppler text extraction confirmed the exact affiliation and both email
addresses:

- `Institute of Computer Science and Digital Innovation, UCSI University,
  Kuala Lumpur, 56000, MALAYSIA`;
- `zijianzeng@foxmail.com`;
- `1002266693@ucsiuniversity.edu.my`.

No additional author or affiliation appears.  The paper explicitly states
that no Lean, Coq, Isabelle, or other proof assistant was used and restricts
the theorem to `D_9`.

## Conclusion

The release PDF passes structural, metadata, text, citation, and every-page
visual review.  No PDF correction is required.
