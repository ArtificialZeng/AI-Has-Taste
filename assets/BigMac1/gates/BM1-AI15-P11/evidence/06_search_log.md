# Search log

## NOVELTY_LOCK pass 1 — frozen claims

- Search cutoff: 2026-08-29 (Asia/Shanghai).
- Frozen claim IDs: C01--C10 in `literature/claim_ledger.md`.
- Required source classes: the live Erdős Problems record; original papers;
  publisher/DOI metadata; arXiv versions actually inspected; MathSciNet,
  zbMATH, OEIS/MathDB or comparable formal databases where accessible; the
  user-supplied SciNet record and any attached certificate/code.
- Planned query families: exact problem number and wording; `independence
  polynomial tree unimodal`; `independent set sequence tree unimodality`;
  `tree independence polynomial log-concavity counterexample`; title/author
  forward- and backward-citation searches for every decisive paper.
- Negative-result convention: “not found” will always name the databases,
  queries, and cutoff; it will not be stated as an absolute nonexistence
  theorem.

## NOVELTY_LOCK pass 2 — source audit

Search date: 2026-08-29. The following query families were run with exact
titles, author names, problem number, and date variants:

- `Erdős #993 independent sets tree unimodal`, plus the live problem URL and
  its `/latex/993` endpoint;
- `independent set sequence tree unimodal conjecture` and `independence
  polynomial tree unimodal`;
- `tree independence polynomial not log-concave counterexample 2023 2024
  2025 2026`;
- `tree unimodality conjecture proof counterexample 2026`;
- exact-title and author searches for Alavi–Malde–Schwenk–Erdős,
  Kadrawi–Levit, Galvin, Ramos–Sun, Hibi–Kara–Vien, and Reynolds;
- forward-reference inspection in the June 2026 *Graphs and Combinatorics*
  paper and the April 2026 Hibi–Kara–Vien bibliography.

Databases/endpoints inspected: Erdős Problems, the Erdős archival PDF server,
arXiv abstract and HTML records, DOI/publisher pages (Springer, Ars Mathematica
Contemporanea repository, Mathematical Theory and Applications), Zenodo,
SciNet, OEIS-linked census metadata, and GitHub artifact links attached to the
SciNet and Zenodo records. Google-style search was used only to locate primary
records; claims in the ledger cite the primary record or explicitly label an
author/SciNet report.

### Theorem frontier found in pass 2

- **Open endpoint:** no all-tree proof or counterexample was found. The latest
  live records inspected still say open.
- **False strengthening:** universal log-concavity is false. The primary
  sources now contain infinite families, examples with multiple failures, and
  2026 families with two or three consecutive failures.
- **Finite endpoint:** Reynolds' archival v3 record covers trees through order
  29; the later SciNet artifact reports trees and forests through order 30.
- **Positive subclasses:** paths/claw-free graphs, several well-covered tree
  families, some rooted products, and gamma-admissible bridge constructions.
  Galvin explicitly states that even all caterpillars were still open in the
  version inspected (arXiv:2502.10654v2, Introduction).
- **Structural work:** Reynolds reports mean bounds, a subdivision–contraction
  identity, structural reductions, and leaf-attachment asymptotics; these must
  be treated as prior art before any similar local claim is called new.

### Exact bibliographic anchors

- Y. Alavi, P. J. Malde, A. J. Schwenk, P. Erdős, *The vertex
  independence sequence of a graph is not constrained*, Congr. Numer. 58
  (1987), 15–23.
- O. Kadrawi, V. E. Levit, *Ars Mathematica Contemporanea* 25(4)
  (2025), article P4.03, DOI 10.26493/1855-3974.3207.2ad; the earlier
  manuscript is arXiv:2305.01784v2.
- D. Galvin, arXiv:2502.10654v2 (2026-01-23 revision).
- E. Ramos, S. Sun, arXiv:2510.18826v2.
- T. Hibi, S. Kara, D. Vien, arXiv:2604.18824v1.
- C. Bautista-Ramos, C. Guillén-Galván, P. Gómez-Salgado, DOI
  10.1007/s00373-026-03054-4 (published 2026-06-22).
- B. Reynolds, Zenodo DOI 10.5281/zenodo.19100781, v3 dated 2026-03-18.

### Bounded conclusion of pass 2

Within the databases and queries above, and only through the 2026-08-29
cutoff, the all-tree conjecture remains open. This lock must be repeated after
the mathematical search and before asserting novelty for any local theorem or
counterexample.

## NOVELTY_LOCK pass 3 — post-result search

Search date: 2026-08-29 (Asia/Shanghai), after both local order-31 aggregators
had returned PASS.  The candidate claims were frozen before searching:

1. all 40,330,829,030 unlabelled trees on exactly 31 vertices have unimodal
   independent-set sequences;
2. exactly 159 of those order-31 trees are non-log-concave, and every one is
   still unimodal;
3. together with the independently reviewed order-30 census, this raises the
   finite no-counterexample frontier from 30 to 31.

The following exact and variant query families were run:

- `"40330829030" independence unimodal tree`;
- `"trees on 31 vertices" "independence polynomial" unimodal`;
- `Erdős 993 tree unimodal 31 2026`;
- `site:arxiv.org "independence polynomial" tree unimodal 31`;
- `"through order 31" "tree independence" unimodality`;
- `"order 31" "Erdős #993"`;
- `"all trees" "31 vertices" unimodal independent-set`;
- `site:zenodo.org OR site:arxiv.org "40330829030" unimodal`.

Primary/live records then inspected directly were the SciNet problem and its
order-30 finding, Erdős Problems #993, OEIS A000055, the current arXiv records
found by the searches, and the Reynolds Zenodo record.  GitHub search results
were used as discovery aids and checked against their attached release or
SciNet records when they affected a claim.

### Post-result frontier conclusion

- The live SciNet problem, crawled on the search date, still lists the
  independently reproduced 2026-07-27 result through order 30 and explicitly
  calls order 31 the next rung.
- The order-30 finding certifies 14,830,871,802 order-30 trees and 149
  non-log-concave trees through order 30; it contains no order-31 census.
- OEIS A000055 gives exactly 40,330,829,030 unlabelled trees on 31 vertices,
  agreeing with both local aggregators.
- No order-31 or stronger exhaustive unimodality result was located in the
  searched arXiv, Zenodo, SciNet, Erdős Problems, OEIS-linked, DOI/publisher,
  or exact-title/exact-count records.

This is a date- and database-bounded novelty conclusion, not a proof that no
unindexed or unpublished computation exists.  On the inspected record, the
local order-31 result is a strict one-layer extension of the order-30 frontier.
