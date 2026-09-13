# Research pass 1 recovery record

- Job: `bigMac-00019-p03-research-99fd258a5d5f`
- Role/model: research, `gpt-5.6-sol`, `ultra`
- Start: 2026-09-08T15:57:23Z
- End condition: 25-minute infrastructure timeout; no `result.json`
- Imported usage: unknown
- Immutable `source.md`: unchanged

## Exact graph and cycle evidence

The deposited `agl_29_g14.g6` member remains SHA-256
`8b074cd755a5d1e1e6a1d09a7888173821372e6cdcd501cfd2baf1a34bfeb08e`.
`cycle_census.py` verifies the 812-vertex connected simple cubic graph and
canonicalizes 2,030 fourteen-cycles, zero fifteen-cycles, and 5,278
sixteen-cycles. The complete TSV SHA-256 is
`1aebbf14917b5d14aaed298898e5386e78f7dd4b2d322fb06118c35f4c8344a8`.

## Encodings and solver status

The direct DIMACS has 2,436 variables and 2,040,556 clauses, SHA-256
`a1670786449e453ef32755f726110d03fb095b36d586c8bf7c7a9c393ae6adbb`.
Its semantics are exactly one of three neighbour choices at each vertex and
the required outside-neighbour lower bound for every target cycle. CaDiCaL
3.0.1 reached 1,317,170 conflicts and the 300-second wall limit, returning
only `c UNKNOWN`; peak RSS was approximately 3.48 GB.

The left-scaling-order-28 and left-translation-order-29 quotient instances
returned `s UNSATISFIABLE` in under one second, but no independently checked
proof was preserved. They reject only their invariant subclasses. The
order-14 scaling quotient remained `UNKNOWN` under 90-second CaDiCaL and
Kissat runs. None of these statuses settles the full CSP.

The local fourteen-cycle incidence counts at each vertex are a permutation of
`(13,13,9)`. Choosing a local maximum produces aggregate 10,556 versus the
required 10,150, so the elementary counting test has slack 406. The unsolved
`good_edge.cnf` restricts each vertex to its two maximizing choices; it has
812 variables, 665,028 clauses, and SHA-256
`b1dbfb4a891027e796c891d41017b2bc96b18560537edb2e727e92aa80c08e0b`.

## Recovery decision

New exact evidence and a decisive next test justify one official research
requeue with counters preserved. First solve and check the good-edge
restriction. Then, if needed, replace exponential subset-cardinality clauses
by a validated compact encoding and demand either a directly checked complete
assignment or an independently checkable UNSAT proof. Do not repeat graph
decoding, literature intake, or bare symmetry-restricted solving.
