# Citation audit

Audit date: 2026-08-22.

Fourteen cited records were individually checked against publisher, archival,
DOI, or arXiv records.  The manuscript cites the 2026 journal version of
Baek--Balko rather than its preliminary SoCG version, and the Springer record
of Subercaseaux--Mackey--Qian--Heule (CICM 2025 proceedings, formally
published in 2026).

| Key | Work | Authoritative record | Status |
|---|---|---|---|
| `BaekBalko2026` | The Erdős--Szekeres conjecture revisited | Elsevier/Crossref DOI `10.1016/j.jcta.2026.106195` | verified |
| `BalkoValtr2017` | A SAT attack on the Erdős--Szekeres conjecture | Elsevier DOI `10.1016/j.ejc.2017.06.010` | verified |
| `Dumitru2025` | Notes on the 33-point Erdős--Szekeres problem | arXiv `2512.24061`, v1 | verified as preprint |
| `ErdosSzekeres1935` | A combinatorial problem in geometry | NUMDAM archival record | verified |
| `ErdosSzekeres1960` | On some extremum problems in elementary geometry | Erdős archive scan/catalogue | verified; pages 53--62 |
| `FelsnerWeil2001` | Sweeps, arrangements and signotopes | Elsevier DOI `10.1016/S0166-218X(00)00232-8` | verified |
| `HeuleScheucher2024` | Happy Ending: An Empty Hexagon in Every Set of 30 Points | Springer DOI `10.1007/978-3-031-57246-3_5` | verified; normalization and 17-point timings checked in Sections 3.4 and 6 |
| `KoshelevKoshka2026` | Combinatorial geometry of Erdős--Szekeres type problems | arXiv `2604.20120`, v1 | verified; equations (13)--(16) support the endpoint/middle prior art |
| `Maric2019` | Fast formal proof ... at most 6 points | Springer DOI `10.1007/s10817-017-9423-7` | verified; print year 2019 |
| `MojarradVlachos2016` | An improved upper bound ... | Springer DOI `10.1007/s00454-016-9791-5` | verified |
| `Scheucher2023` | A SAT attack ... and the empty hexagon theorem | journal/DataCite DOI `10.57717/cgt.v2i1.12` | verified |
| `SzekeresPeters2006` | Computer solution to the 17-point problem | Cambridge DOI `10.1017/S144618110000300X` | verified |
| `SubercaseauxMackeyQianHeule2026` | Automated symmetric constructions in discrete geometry | Springer DOI `10.1007/978-3-032-07021-0_3` | verified; formal year 2026 |
| `WetzlerHeuleHunt2014` | DRAT-trim | Springer DOI `10.1007/978-3-319-09284-3_31` | verified |

The Marić citation context was corrected to describe its new Isabelle/HOL
proof rather than a check of the earlier computation.  The Subercaseaux et al.
comparison was audited against the CNF emitted by the authors' public code:
after fixing the global order, it uses one convexity variable and sixteen
five-literal full-reification clauses per four-set, with no parity auxiliary
variables.  Koshelev--Koshka's arXiv metadata and Section 4.4 were checked
separately: its two convex-quadrilateral cases have endpoint equivalence and
middle disequality, whose complement is the factorization used here.  The
final BibTeX key checker reports 14 cited keys and 14 database keys, with no
missing or unused entries.  A final post-build log check is recorded in
`PDF_AUDIT.md`.  There are no unresolved bibliographic blockers.
