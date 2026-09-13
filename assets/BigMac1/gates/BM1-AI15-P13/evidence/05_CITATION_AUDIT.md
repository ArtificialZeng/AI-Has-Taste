# Citation audit

Audit date: 2026-08-29 (Asia/Shanghai)

Outcome: **PASS -- one citation checked, one verified, zero unresolved.**

The unique key was independently re-audited after verifier hardening. The
result was unchanged: the manuscript context is supported by the abstract,
Algorithm 2 and its fixed-precision discussion, and the conditional theorem;
the current official arXiv BibTeX remains correct.

## Per-citation result

| Key | Verification | Result |
|---|---|---|
| `hashemi2025instabilityshermanmorrisonformulastabilization` | Independent per-citation audit against arXiv:2510.01696v1, arXiv API metadata, downloaded PDF/source, and DataCite record for DOI `10.48550/arXiv.2510.01696` | Title, authors, year, arXiv identifier, subject class, URL, conjecture attribution, Algorithm 2 reuse claim, and conditional-theorem description agree. |

The manuscript uses the official arXiv-export BibTeX entry in
`paper/references.bib`. DataCite's machine-generated entry was retained as
`literature/hashemi_datacite.bib` for comparison. The internal key is the
official arXiv export key; no `\\cite{...}` rewrite was required.

## Database and build integrity

- `paper/main.tex` contains exactly one distinct citation key.
- `paper/references.bib` contains exactly one entry.
- Missing entries: zero. Unused entries: zero. Duplicate keys: zero.
- BibTeX regenerated `paper/main.bbl`; `paper/main.aux` contains the matching
  `\\bibcite` record.
- The final LaTeX/BibTeX logs contain no undefined citations, missing database
  entries, duplicate-entry warnings, or bibliography-format warnings.
- `audit_latex.py` reported `cited=1 bib=1 missing=0 unused=0`.

## Publication-status boundary

arXiv listed only version 1 during both novelty passes. The first author's
site reported August 2026 acceptance by an IMA Journal of Numerical Analysis
special issue, but no publisher article page or journal DOI was located.
Accordingly the bibliography cites the verified arXiv record and makes no
publisher-status claim. This should be revisited if an official journal record
appears.
