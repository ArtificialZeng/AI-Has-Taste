# Clean build audit

Status: **PASS**  
Date: 2026-08-30 (Asia/Shanghai)

## Commands

```sh
cd paper
latexmk -C main.tex
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py main.tex --aux main.aux
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py main.tex references.bib --log main.log
rg -n "Citation .* undefined|There were undefined|I didn't find a database entry|Warning--|Repeated entry|LaTeX Error|Fatal error|Emergency stop|Undefined control sequence|Runaway argument|Overfull|Underfull" main.log main.blg
```

## Results

- `latexmk`: exit 0 after a full clean; target up to date.
- Citations: 8 cited keys, 8 BibTeX keys, 8 `.aux` bibcite keys.
- Missing or unused keys: 0.
- Final log scan: no match for undefined citations/references, missing
  database entries, duplicate entries, LaTeX errors, overfull boxes, or
  underfull boxes.
- `audit_latex.py`: `cited=8 bib=8 missing=0 unused=0`.
- Final `.bbl` SHA-256:
  `f02172023a4383619a1bcc5c25ec95ebbfb4369692c88412cbee27f8e476d7c6`.
