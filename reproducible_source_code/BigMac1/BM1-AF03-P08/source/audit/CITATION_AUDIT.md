# Citation audit

Search date: 2026-08-29.

A local `@STRING{July = "July"}` declaration precedes the entries solely to
make the official Pagliacci export's `month=July` token defined under BibTeX;
the exported article block itself is unchanged.

| Key | Intended claim/context | Official title/record | Official source | BibTeX action | Key change | Uncertainty |
|---|---|---|---|---|---|---|
| `chen2013classkazhdanlusztigrpolynomialsqfibonacci` | Exact conjecture, authors' `n<=9` report, and proved upper-endpoint formula | *A Class of Kazhdan-Lusztig R-Polynomials and q-Fibonacci Numbers*, four authors, 2013, arXiv:1312.2170v1 | `https://export.arxiv.org/bibtex/1312.2170`; arXiv abstract; DataCite `10.48550/arXiv.1312.2170` | Official arXiv export inserted verbatim | planned local key `ChenFanGuoZhong2013` -> official export key | No journal reference exists on arXiv; phrase `n<=9` as an author report. |
| `BjornerBrenti2005` | Bruhat order/subword/rank criteria and Coxeter background | *Combinatorics of Coxeter Groups*, Anders Björner and Francesco Brenti, GTM 231, 2005 | Springer book page and Crossref DOI `10.1007/3-540-27596-7` | Complete block assembled only from fields explicitly verified on Springer/Crossref; raw Crossref export omits author/title/volume | none | Official records disagree only on publication place, so `address` is omitted. |
| `CM_1993__89_1_91_0` | Primary provenance for modified (R)-polynomials, nonnegative path form, and change of variables | *Hecke algebras and shellings of Bruhat intervals*, M. J. Dyer, *Compositio Mathematica* 89(1), 91--115 (1993) | Numdam item and original journal PDF | Official Numdam BibTeX inserted verbatim | planned `Dyer1993` -> official export key | Primary records checked contain no DOI; the modern displayed two-branch recurrence is also explicitly reproduced in Chen et al. |
| `Kazhdan1979` | Original ordinary (R)-polynomials and Kazhdan--Lusztig theory | *Representations of Coxeter groups and Hecke algebras*, David Kazhdan and George Lusztig, *Inventiones mathematicae* 53(2), 165--184 (1979) | Springer article page/export, DOI `10.1007/BF01390031`, Crossref, original scan | Official Springer BibTeX inserted verbatim | `KazhdanLusztig1979` -> `Kazhdan1979` | Supports ordinary (R), not the later modified normalization. |
| `Pagliacci_2001` | Lower-endpoint formula $\mathcal R_{e,v_n}(q)=q^{2n-4}F_{n-2}(q^{-2})$ | *Explicit Formulae for Some Kazhdan–Lusztig R-Polynomials*, Michela Pagliacci, *J. Combin. Theory Ser. A* 95(1), 74--87 (2001) | DOI/ScienceDirect record, DOI `10.1006/jcta.2000.3151`; attribution cross-checked in Chen et al. before their (2.4) | Official DOI Content Negotiation BibTeX inserted verbatim | `Pagliacci2001` -> `Pagliacci_2001` | ScienceDirect abstract and Chen et al.'s primary source support the claim; the VOR theorem's exact internal printed page was not directly inspected because full-text access returned 403. |

The source's `e`-to-`v_n` formula is explicitly credited there to Pagliacci;
the manuscript cites Pagliacci directly when using that formula.  The
tilde-R recurrence is explicitly credited there to Dyer; the manuscript will
also cite Dyer's primary paper.

## Build and key audit

The final manuscript cites five keys, and the final bibliography contains
exactly those five keys.  The checks

```sh
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py paper/main.tex --aux paper/main.aux
python3 /Users/mac/.codex/skills/prove-or-disprove-math/scripts/audit_latex.py paper/main.tex paper/references.bib
```

reported `cited_keys_missing_from_bib: 0`, `bib_keys_not_cited: 0`, and
`cited_keys_missing_from_aux: 0`.  A clean `latexmk` build followed by a scan
of `paper/main.log` and `paper/main.blg` found no undefined citations or
references, missing database entries, BibTeX warnings, repeated entries,
LaTeX errors, overfull boxes, or underfull boxes.
