# Claim ledger

Frozen before the main search on 2026-08-30 (Asia/Shanghai).  “Not found” is
limited to the databases and queries recorded in `search_log.md`.

| ID | Claim | Type | Status | Primary or authoritative evidence | Location | Confidence | Consequence |
|---|---|---|---|---|---|---:|---|
| C01 | The problem asks for the maximum number of full translation orbits of 5-subsets of \(\mathbb Z_{31}\) whose developed triples have multiplicity at most one. | exact | verified | TheoremDB problem P2632 | statement, Definitions 1--2 | 100% | Fixes the target. |
| C02 | Nine displayed base blocks form a feasible packing. | exact computational | independently reproduced locally | TheoremDB record R187 plus local no-import verifier | `experiments/instance.json`; positive-verifier tests | 100% | Baseline \(M\ge9\). |
| C03 | Pair incidences and orbit divisibility imply \(M\le13\). | exact theorem | independently reconstructed locally | TheoremDB record R188; Bailey--Burgess for the general packing-bound context | `proof/structural_reduction.md`; `proof/proof_dag.md` | 100% | Baseline upper endpoint. |
| C04 | There are 145 triple translation resources. | exact finite count | verified analytically as \(\binom{31}{3}/31\) | present formal reduction | `problem/formal_statement.md` | 100% | Row count of exact set packing. |
| C05 | There are 5481 translation classes of 5-subsets, of which exactly 4761 are internally valid. | exact finite count | independently reconstructed locally from definitions | TheoremDB artifact R184 plus local enumeration | `experiments/instance.json`; `tests/test_enumeration.py` | 100% | Column count of exact set packing. |
| C06 | The packing is equivalent to a one-dimensional \((31,5,2)\) optical orthogonal code when both auto- and cross-correlation limits are 2. | paraphrase/equivalence | verified directly from the correlation definition | Chung--Salehi--Wei, DOI 10.1109/18.30982; TheoremDB R186 | OOC definition / recorded equivalence | 99% | Supplies literature vocabulary, not the optimum. |
| C07 | The foundational OOC paper has the stated journal metadata. | exact metadata | verified | Crossref DOI record 10.1109/18.30982; IEEE Xplore document 30982 | metadata record | 100% | Bibliographic integrity. |
| C08 | Bailey--Burgess is the cited general packing reference and Chu--Colbourn treats exact search for weight 4, not this weight-5 instance. | exact metadata/scope | verified | Crossref DOI 10.1016/j.disc.2011.11.039; ScienceDirect DOI 10.1016/S0012-365X(03)00266-8 | title, abstract, journal metadata | 100% | Prevents importing a neighboring result as this result. |
| C09 | No checked primary paper, arXiv record, professional-database record, or public code settles \(\Phi(31,5,2)\), gives the local twelve-block packing, or proves target 13 impossible. | bounded novelty claim | not found in both Gate 1 and the post-result Gate 2 pass | searches in TheoremDB, arXiv API, Crossref, zbMATH Open, OpenAlex, GitHub/Zenodo recorded in log | query log, including Gate 2 | 90% within the documented scope | Supports provisional novelty only; unindexed or unpublished prior work is not excluded. |
| C10 | Moura's thesis studies cyclic \(t\)-packings computationally, but its displayed small-parameter tables do not settle the present \(3-(31,5,1)\) instance. | exact scope | verified by inspection | L. Moura, *Polyhedral methods for combinatorial optimization problems*, 1999 thesis, Library and Archives Canada PDF | Chapter 4, pp. 107--122, especially Tables 4.15 and 4.19 | 98% | Historical context only. |
| C11 | TheoremDB's 2026-07-25 packet labels the exact value open and retains only the interval \(9\le M\le13\). | author/database report | verified as a database status, not as proof of global novelty | TheoremDB P2632 | Status and packet records | 100% | Starting frontier, subject to independent audit. |
| C12 | A 12-orbit cyclic packing exists. | exact computational | independently certified locally | strict serialized witness plus no-import full development | `certificates/packing12.json`; `tests/test_positive_verifier.py` | 100% | Improves the lower bound to \(M\ge12\). |
| C13 | Target-13 excess partition type `(5)` and every one of the 162 multiplier block-orbit branches are impossible. | exact negative computation | certified locally | two checked LRAT encodings plus independently replayable complete clique enumerations and the exact 4,761-variable orbit cover | `certificates/negative/target13_partition_5_manifest.json`; `certificates/negative/fixed*_finite_manifest.json`; `certificates/negative/target13_global_fixed_cover_manifest.json` | 100% | Rules out every target-13 packing. |
| C14 | The maximum number of base-block orbits is \(M=12\). | exact theorem with finite computation | certified locally | twelve-block full-development certificate plus the independently reconstructed complete 162-branch multiplier cover | `certificates/packing12.json`; `certificates/negative/target13_global_fixed_cover_manifest.json`; global and adversarial verifier tests | 100% for the local theorem claim | Closes the original problem; Gate 2 found no checked prior source for the endpoint. |

## Gate 1 verdict: `NOVELTY_LOCK`

The source boundary is internally consistent and no correction to the formal
target is needed.  TheoremDB is a 2026 research-memory record rather than an
original journal conjecture.  The original literature supplies the general
OOC/packing framework and adjacent algorithms, but the audited sources do not
settle the exact parameter.  Main computation may proceed from the certified
baseline only after the 4761 count and nine-block witness are reproduced
locally.  Any claim of a new exact value remains provisional until the required
second novelty pass and citation-by-citation audit.

## Gate 2 verdict

The second novelty pass is complete. C14 is a strict local theorem; its
priority/novelty remains a bounded literature conclusion as stated in C09.
