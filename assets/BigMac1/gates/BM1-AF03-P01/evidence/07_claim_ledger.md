# Claim ledger

| ID | Claim | Status | Source | Location | Confidence | Consequence |
|---|---|---|---|---|---|---|
| C01 | Huang--Zhang Conjecture 4.1 states \(\delta_d(\mathcal F)\le\binom{n-d-1}{k-d-1}\) for all \(k>d\ge0\), \(n\ge2k+1\), and intersecting \(\mathcal F\subseteq\binom{[n]}k\). | verified exact | arXiv:2407.14091v1 | Conjecture 4.1, PDF p. 8; HTML lines 206--210 | 100% | Determines the intended mother conjecture. |
| C02 | The cited work proves the conjectured bound for \(d\ge2\) when \(n\ge2k+2d-3\). | verified exact | arXiv:2407.14091v1; publisher abstract | Theorem 1.1, PDF p. 2; HTML lines 42--46 | 100% | Covers \((4,3)\) for every \(n\ge11\). |
| C03 | The mother conjecture is already known for \(d=0,1,2\). | verified exact with primary chains | EKR (1961); Huang--Zhao arXiv:1605.07535; Huang--Zhang Theorem 1.1 at \(d=2\) | EKR bound; Huang--Zhao Theorem 1.1; direct substitution \(d=2\) | 100% | Background cases are correctly stated. |
| C04 | The paper is formally published as Hao Huang and Yi Zhang, *On a d-degree Erdős--Ko--Rado theorem*, JCTA 221 (2026), article 106163, DOI 10.1016/j.jcta.2026.106163. | verified exact | Elsevier/ScienceDirect; Crossref REST singleton | publisher record; Crossref metadata fields | 100% | Bibliographic accuracy. |
| C05 | arXiv:2407.14091 is the correct record; its latest version as of 2026-08-29 has no correction changing C01/C02. | verified exact | arXiv abstract/version history | only v1, 19 Jul 2024 07:56:57 UTC | 100% | Source-version lock. |
| C06 | No later primary-source paper publicly resolves the two endpoints \(n=9,10\) or the full \((4,3)\) family as of 2026-08-29. | two bounded negative passes completed; no prior resolution found | arXiv/full-text forward search; Crossref; OpenAlex; Semantic Scholar; publisher/author pages; exact web queries | `search_log.md`, Gate 1 and second-pass entries | 95% (necessarily non-absolute) | Exact research and qualified release wording permitted; no categorical priority claim. |
| C07 | No public code/certificate already establishes the proposed \(n=9,10\) SAT instances. | two bounded negative passes completed; no public artifact found | arXiv source/ancillary; Crossref relations; GitHub code/repository/issues; GitLab projects; Zenodo; author page | `search_log.md`, public-code audit and second pass | 95% (necessarily non-absolute) | New certificates may be released with a bounded-search qualification. |
| C08 | Substitution \((k,d)=(4,3)\) gives RHS \(1\), threshold \(n\ge11\), and mother-conjecture domain \(n\ge9\). | verified exact inference | arithmetic plus C01/C02 | direct substitution | 100% | Reduces the unresolved range to \(n=9,10\). |
| C09 | The Boolean formulation in `problem/formal_statement.md` is logically equivalent to a counterexample at each fixed \(n\). | verified exact by independent reconstruction and truth-table audit | definitions; no-import CNF verifier; certificate referee | `problem/formal_statement.md`; `audit/PROOF_AUDIT.md` | 100% | Basis for SAT/UNSAT certification. |

Claim list frozen before web searching on 2026-08-29 (Asia/Shanghai).  “Not
found” will mean only “not found by the explicitly recorded queries and
databases.”
