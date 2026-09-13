# PDF and LaTeX audit

Status: **PASS**.  Final audit date: 2026-08-29.

## Clean build

The PDF artifact operation was marked once before creation, as required by the
PDF workflow.  The release candidate was then built from an entirely fresh
output directory:

```bash
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir=../tmp/clean-build-20260829-final1 main.tex
```

`latexmk` ran BibTeX and the required LaTeX passes to convergence.  The final
`main.log` contains no LaTeX/package warnings, undefined citations or
references, duplicate labels, overfull/underfull boxes, or rerun request.
`main.blg` reports `warning$ -- 0`.  The generated `paper/main.bbl` is
byte-identical to the clean-build `.bbl`, with SHA-256
`50fe9eece9d223ac55a4e9fc5a2843a74359fb99776a46847d692c084d299c46`.

The citation-key gate reports 3 cited keys, 3 BibTeX keys, 3 `.aux` keys, zero
missing keys, and zero unused keys.  The theorem-workflow LaTeX audit reports:

```text
cited=3 bib=3 missing=0 unused=0
```

## PDF checks

- Final path: `output/pdf/d_degree_ekr_k4d3.pdf`.
- SHA-256:
  `f5ffc1c942f5a246278a40c1e8b81739704f369effe42f0339b3793e36cc5f1c`.
- Four US-letter pages, PDF 1.7, unencrypted, no forms or JavaScript.
- PDF metadata title matches the article title and author is exactly
  `Zijian Zeng`.
- All fonts reported by `pdffonts` are embedded and subsetted.
- Rasterized every page at 144 dpi (1224 by 1584 pixels) and inspected all
  four pages at original detail.  No clipping, overlap, missing glyph,
  truncated equation, table collision, broken reference, or bad page break was
  found.  The bibliography and both email lines are fully visible.

## Authorship check

The PDF and LaTeX contain exactly the authorized author and affiliation:

```text
Zijian Zeng
Institute of Computer Science and Digital Innovation,
UCSI University, Kuala Lumpur, 56000, MALAYSIA
zijianzeng@foxmail.com
1002266693@ucsiuniversity.edu.my
```

No additional author or affiliation appears.  The disclosure accurately says
that no Lean, Coq, Isabelle, or other proof assistant was used.
