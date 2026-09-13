# Research pass 1 recovery record

Job `bigMac-00019-p02-research-df698f9daef5` reached its 25-minute
wall-clock ceiling before returning `result.json`.  The runner therefore
recorded an infrastructure failure with unreported usage.  This is not a
mathematical rejection.  The pass nevertheless produced a potentially
complete exact exclusion for one of the two first noncubic degree patterns.

## Candidate finite exclusion

Let family A consist of 24-vertex simple graphs with degree sequence
`(5,3^23)` and no cycles of lengths 4, 8, or 16.  The program
`evidence/geng_excess2_search.cpp` uses the degree-5 vertex as vertex 0.
In a C4-free graph its five neighbors induce a matching of size
`m in {0,1,2}`, and no remaining vertex can meet two of those neighbors.
Deleting vertex 0 and its five neighbors leaves an 18-vertex C4-free graph
with degrees 2 or 3, exactly `22+m` edges, and `10-2m` degree-2 attachment
ports.  The program enumerates the residual graphs with `geng`, then all port
partitions modulo only the evident symmetries of the five arms, and directly
tests every reconstructed graph for C4, C8, and C16.

The three completed logs report:

| m | residual graphs | residual C8/C16 survivors | attachments tested | C4 rejects | C8 rejects | C16 rejects | witness |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 294,693 | 29,143 | 27,540,135 | 15,062,760 | 12,477,375 | 0 | none |
| 1 | 835,745 | 13,064 | 5,486,880 | 2,331,130 | 3,155,750 | 0 | none |
| 2 | 1,087,732 | 1,020 | 45,900 | 12,131 | 33,769 | 0 | none |

The reject counts exactly sum to the attachment counts in each row.  Thus,
conditional on an audit of the reduction, enumeration coverage, port-orbit
coverage, parser, and cycle detector, the logs exclude family A.  They do not
settle the second degree-excess-two pattern `(4,4,3^22)`, much less the frozen
minimum-degree-at-least-three assertion.

## Reproducible artifacts

- `geng_excess2_search.cpp` SHA-256:
  `eb71db5101f32f56e6e5b8ab58b428c270f0336edf0171c9ca2b14bdb0666ee1`.
- `geng_A_m0.log` SHA-256:
  `c7795224f61667e0c8674d798e57b77dbc4dbacafbe2038a6f4653a79e000e4a`.
- `geng_A_m1.log` SHA-256:
  `05ed6bb5aa37b3cd1d9cfe304f741972c58ec0e920fb67a501a347661e9765e0`.
- `geng_A_m2.log` SHA-256:
  `81618730e542210943e7773d1f8548ca7417fb5ccece29d94245796ddfcafa6a`.
- Immutable `source.md` remains SHA-256
  `8c3b64806f2471c61924f4be72e1873a67a03633e8fc843b70d0916afd0aba1e`.

The earlier incremental CryptoMiniSat route remains `UNKNOWN`; its retained
cycle clauses and CNFs are resumable search state, not UNSAT certificates and
not evidence for a universal statement.

## Audit gaps and one next test

At the next clean owner boundary, officially requeue without resetting
`research_passes=1`.  First independently prove the neighborhood-matching
reduction and audit all three attachment enumerators (945, 420, and 45 choices
per surviving residual graph).  Rebuild from source and reproduce the three
counts with an independent cycle checker or a separately implemented held-out
sample.  If this audit succeeds, freeze the family-A exclusion as a candidate
subsidiary theorem and then formulate the analogous complete split for
`(4,4,3^22)`.  Any discrepancy kills the candidate and must be recorded.

