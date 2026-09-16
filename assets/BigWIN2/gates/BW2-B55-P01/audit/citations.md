# Citation and bibliography audit

## Verdict

Accept. The citation-check audit used two non-interleaved stages: the claim
surface was frozen in `audit/citation-claim-ledger.json`, then the fixed claim
IDs were checked in `audit/citation-verification.json`. All eight citation-claim
pairs and all four bibliography records passed. The user explicitly prohibited
agents, so the normally delegated per-key checks were performed serially in
this release context.

## Claim-to-source results

| Claim IDs | Key | Primary source and exact support | Result |
|---|---|---|---|
| C01 | `HojsgaardLauritzen2008` | Oxford Academic article record and Summary for volume 70(5), pp. 1005--1027, DOI `10.1111/j.1467-9868.2008.00666.x`: the authors say they introduce the colored edge/vertex-symmetry models. | Verified (paraphrase) |
| C02 | `GrossSullivant2018` | Official Bernoulli/Project Euclid PDF, abstract and first page, DOI `10.3150/16-BEJ881`: it defines and develops the graph maximum-likelihood threshold. | Verified (paraphrase) |
| C03--C07 | `HomsKuznetsovaStolz2026` | Official arXiv `2609.02382v1` PDF: Definition 2.13 (PDF p. 5), Theorem 3.4(2) (p. 7), Corollary 3.7 (p. 8), Proposition 3.26 and Conjecture 3.27 (p. 13), and Appendix Table 2 (p. 28). The hypotheses and values match every nearby claim. | Verified (exact/paraphrase as recorded) |
| C08 | `ZengLiuRatnavelu2026` | Official Preprints.org version 1, Section 7, DOI `10.20944/preprints202608.1346.v1`: analytic proofs are separated from independent exact-arithmetic finite checks using symbolic integers and rationals. | Verified (paraphrase) |

No citation was numerical, rounded, contradicted, misleading, absent, or
supported only by a secondary source. Exact source locations and individual
status decisions are preserved in `audit/citation-verification.json`.

## Bibliographic record audit

| Key | Current/official title | Authority | BibTeX replacement | Key change | Uncertainty |
|---|---|---|---|---|---|
| `HojsgaardLauritzen2008` | *Graphical Gaussian Models with Edge and Vertex Symmetries* | Oxford Academic and DOI record | No; authors, year, journal, volume, issue, pages, and DOI already match. | None | None |
| `GrossSullivant2018` | *The Maximum Likelihood Threshold of a Graph* | Project Euclid/Bernoulli and DOI record | No; authors, year, journal, volume, issue, pages, and DOI already match. | None | None |
| `HomsKuznetsovaStolz2026` | *A Computational Approach to Maximum Likelihood Thresholds for Colored Gaussian Graphical Models* | arXiv v1 record and checksum-matched local PDF | No; authors, title, year, identifier, version, and URL already match. | None | None |
| `ZengLiuRatnavelu2026` | *Sharp Self-Chollet Inequalities for Rank-Two Correlation Matrices of Order Five* | Official Preprints.org v1 and DOI record | No; authors, title, date, venue, DOI, and version already match. | None | None |

The mechanical audit found four cited keys, four unique `.bib` entries, no
missing or unused entries, and an identical four-key set in `main.aux`. There
are no custom or indirect citation macros.

## Coverage and relevance

The bibliography is not user-library-only. It includes the primary origin of
the colored edge/vertex-symmetry model, the primary paper developing graph MLT,
and the exact closest-prior/problem source that supplies all nontrivial imported
threshold results. The standard weighted-Laplacian sum-of-squares fact is proved
directly in equation (6), so it needs no external dependency. The one active
user-library work is retained only for its exact-arithmetic audit methodology;
it is cited in ordinary body flow by `\cite{ZengLiuRatnavelu2026}` and is not
used to support the theorem or novelty. Screening all 49 registry abstracts
found no honest second library match; adding one would be citation padding.

The project contains no `literature/bibliography-revision-*.md` or saved
`literature/crossref-*` files. Direct WSL DOI content negotiation was unavailable,
but the official arXiv, Oxford Academic, Project Euclid, and Preprints.org pages
were accessible and supplied the claim-level primary evidence. The online
comparison is bounded to the inspected sources on 2026-09-07 and makes no global
priority claim.

## Final consistency checks

The canonical source is `manuscript/main.tex` and the only database is
`manuscript/references.bib`. The post-build bibliography checker passed with no
missing/unused/aux-inconsistent keys. The converged `main.log` and `main.blg`
contain no undefined citation/reference, missing database entry, repeated entry,
BibTeX warning, LaTeX error, fatal error, emergency stop, undefined control
sequence, or runaway argument.
