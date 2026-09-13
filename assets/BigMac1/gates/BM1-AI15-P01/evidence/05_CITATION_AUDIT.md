# Citation audit

Search and audit date: 2026-08-29 (Asia/Shanghai).

## Result

**PASS for the manuscript's single citation.** The cited item exists, its
metadata agrees with the primary arXiv/DataCite record, and the source
supports each nearby attribution. Novelty language remains explicitly
database-bounded.

## Source-to-claim check

| Manuscript claim | Primary-source location | Audit result |
|---|---|---|
| Rivin studies rank-(2,2) Hadamard expressibility of invertible \(4\times4\) matrices. | arXiv:2508.14901v1, Definition 3 and §2.2 | supported |
| The displayed matrix is Rivin's Example 5 and is reported nonexpressible over \(\mathbb F_2\). | Example 5, PDF p. 3 | supported; matrix compared entrywise |
| The real conclusion in the source is numerical evidence, not a rigorous infeasibility theorem. | abstract and §4.3, pp. 1, 3--4 | supported |
| The source asks for analytic work on the real case. | §7.1(4), PDF p. 7 | supported |

The manuscript does not rely on Rivin's Theorem 6 about integer factors. The
referee identified a coverage concern in the theorem's printed proof, so the
project attributes that theorem only in the literature ledger and quarantines
it from the new proof.

## Metadata

- Author: Igor Rivin
- Title: *Computational Resolution of Hadamard Product Factorization for
  \(4\times4\) Matrices*
- arXiv: 2508.14901v1; submitted 2025-07-31
- DOI: 10.48550/arXiv.2508.14901
- Local source PDF SHA-256:
  `2e4de59df9c31feb8f8d96a3a87f239c6b1277ebb9bf5de39a0911ee6a239d34`

The arXiv history lists only v1. OpenAlex and Semantic Scholar returned no
indexed citing work in the dated checks. Full query provenance and caveats
are in `literature/search_log.md` and `literature/referee_search_log.md`.

## LaTeX/BibTeX integrity

Command:

```bash
python /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py \
  paper/main.tex paper/references.bib
```

Output: `cited=1 bib=1 missing=0 unused=0`.

The final BibTeX-rendered reference visibly contains the author, title, year,
arXiv identifier, version, and submission date.

## Novelty limitation

No audited source contained the explicit rational factorization, but finite
database searches do not prove priority. The manuscript therefore makes no
absolute “first” claim. The frozen permissible wording is recorded in
`literature/NOVELTY_LOCK.md`.
