# Citation audit

Search date: 2026-08-29.

Status: **PASS** (source record, BibTeX key consistency, and clean build).

The post-timeout Gate 1/Gate 6 recovery pass reopened the arXiv v2 source and
MathDB record, then reran both the bibliography-key checker and a clean
BibTeX build.  A fresh result-specific second novelty audit subsequently
froze the exact `n=3` matrix statement, equality classification, and
equivalent binary-cubic inequality, then searched the dated sources recorded
in `literature/novelty_recheck_n3.md`.  No prior occurrence was found in
those recorded queries; this is deliberately not presented as proof of
global novelty.  The bibliography result remained one verified citation and
zero missing, unused, or `.aux`-mismatched keys.

| Current key | Context | Official title | Official source | BibTeX action | Key action | Uncertainty |
|---|---|---|---|---|---|---|
| `Marcus_2022` | Original Conjecture 10; author report that the positive-entry case is known | *A Determinantal Identity for the Permanent of a Rank 2 Matrix* | [DOI/publisher](https://doi.org/10.1080/00029890.2022.2115803); [arXiv v2](https://arxiv.org/abs/2108.02528v2) | Crossref block inserted; invalid exported `month=Sept` normalized to `month={September}` after BibTeX warned that `sept` is undefined | Draft key `Marcus2022RankTwoPermanent` changed to official Crossref key `Marcus_2022` before first build | Conjecture 10 does not repeat the real field in its own sentence; the real interpretation comes from the surrounding paper. The positive-entry proof is only an uncited author report in the source. |

Official metadata checked independently by a dedicated citation auditor:
Adam W. Marcus; *The American Mathematical Monthly* 129(10), 962--971
(2022); DOI `10.1080/00029890.2022.2115803`. Crossref records online
publication on 2022-09-26 and print publication on 2022-11-26. The arXiv
version is `2108.02528v2` (2021-08-10), category `math.CO`.

Citation count: 1. Unofficial or unverified references: 0. No borrowed theorem
beyond the source statement is used in the proof.

Final mechanical audit:

```text
python3 /Users/mac/.codex/skills/bib-reference-audit/scripts/check_bib_keys.py paper/main.tex --aux paper/main.aux
cited_keys: 1; bib_keys: 1; missing: 0; unused: 0; aux mismatches: 0
```

The final `main.log` and `main.blg` contain no undefined citation, missing
database entry, repeated entry, BibTeX warning, or rerun warning.  The one
Crossref-export defect encountered during drafting (`month=Sept`) was
normalized to `month={September}`; title, author, venue, volume, issue,
pages, year, and DOI were not altered.
