# PDF audit

Date: 2026-08-29 (Asia/Shanghai)  
Artifact: `output/pdf/Stability_of_3-Packed_Words.pdf`  
Status: **PASS**

The PDF was produced only after the full-DAG hash-bound post-repair PASS,
second novelty pass, independent citation checks, static LaTeX audit, and a
clean converged build.  It is byte-for-byte identical to the clean working
build `paper/main.pdf`.

## Structural checks

```text
SHA-256: 1d634d4f8dadcafbb491e2a05e8dfaf612c609999cced9b3d6ec188db9fb0f17
Bytes: 397656
Pages: 10
Page size: 612 x 792 pt (US Letter)
PDF version: 1.7
Title: Stability of 3-Packed Words in the Plactic Monoid
Author: Zijian Zeng
Encrypted: no
JavaScript: no
Forms: none
Suspects: no
```

`pdffonts` lists every font with `emb=yes`; all listed fonts also have Unicode
maps.  `pdfinfo` parsed the file without error.  The clean-build log contains
no warnings, overfull boxes, underfull boxes, unresolved references, or
unresolved citations.

## Pagewise visual inspection

Every page was rendered at 144 dpi with Poppler and inspected at original
rendered resolution.

| Page | Material checked | Verdict |
|---|---|---|
| 1 | title, author, abstract, introduction, theorem statement, date, footer | PASS |
| 2 | restriction wording, cited preliminaries, tail-isolation statement, complete-column display | PASS |
| 3 | tail-isolation endpoint/cancellation, tropical representation, citations and maps | PASS |
| 4 | cone inequalities, matrix theorem hypotheses, tropical power formula | PASS |
| 5 | adjacent criteria and complete thirteen-weak-order table | PASS |
| 6 | full max-freezing inequalities I.3--I.11 analogue and proof close | PASS |
| 7 | empty-word separation, main theorem proof, six-coordinate feasibility | PASS |
| 8 | row-word induction and first stages of all-coordinate product induction | PASS |
| 9 | remaining G02 insertion batches, empty-factor endpoint, finite-verification table | PASS |
| 10 | diagnostic disclaimer, proof-assistant disclosure, references, affiliation, both emails | PASS |

No page has clipped or overlapping text, broken formulas or tables, black
boxes, missing glyphs, unreadable links, inconsistent headers/footers, or an
incorrect page transition.  Final-page whitespace is intentional and the
references and author block are fully visible.

Verdict: **PASS; the pagewise PDF gate is closed.**
