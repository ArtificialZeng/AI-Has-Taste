# Exact certificate argument for the `C_4 square C_4` fast-robber game

## Claim

Under the convention frozen in `problem.md`,
\[
c_{1,\infty}(C_4\mathbin{\square}C_4)=4.
\]

All computations use finite integer and bit-mask operations.  Vertex `(x,y)` is
encoded as `4*x+y`.  The sorted edge list has SHA-256
`dc5ff1ba83c901714eae763d51d3c87d763524cff2a1b8c4a57929254d106d5e`.
The certificate quotients only by permutations of cop labels, not by graph
automorphisms.  The independent checker expands the certificate to ordered,
labelled cop tuples and ordered simultaneous moves.

## Four-cop upper bound

List the sorted four-cop multisets lexicographically.  For every legal state
`(C,r)`, `evidence/attractor_certificate.json` records a rank in `{1,2,3,4}`
and a destination cop multiset `D`.  The verifier establishes that `D` can be
matched to the labelled cops so that each cop stays or traverses one edge.  It
then checks one of the following:

1. `r` is occupied in `D`, so capture is immediate; or
2. every vertex `r'` in the component of `r` in `G-D` has a positive rank
   strictly smaller than the rank of `(C,r)` in state `(D,r')`.

Strong induction on the rank proves capture within at most the recorded number
of cop moves.  This covers all 48,960 legal sorted-multiset states.  The rank
histogram is 32,944, 9,344, 6,496, and 176 at ranks 1, 2, 3, and 4.  The
labelled checker also covers all 65,536 ordered four-cop configurations and
810,000 legal ordered states, verifying that every selected multiset move lifts
to a legal labelled move.  Thus four cops win (indeed, from every placement).

## Three-cop lower bound

For each sorted three-cop multiset `C`, the certificate gives a nonempty mask
of robber vertices belonging to a set `L`.  For every `(C,r)` in `L` and every
distinct successor multiset `D`, it records a vertex `r'`.  The labelled checker
enumerates every ordered representative of `C` and all `5^3` ordered cop moves.
For each such move it verifies:

1. no cop in `D` occupies `r`;
2. `r'` belongs to the component of `r` in `G-D`; and
3. `(D,r')` again belongs to `L`.

Therefore the robber can choose an initial state in `L` after every three-cop
placement and can remain in `L` after every later cop move.  Induction over any
finite number of rounds gives an infinite evasion strategy.  The certificate
contains 4,576 legal sorted states in `L`; the labelled expansion contains
21,296 such states and checks 2,662,000 ordered cop moves from them.  Hence
three cops do not win.

Combining the two bounds gives the claimed exact value 4.

## Reproduction and independent checks

Run, from the project root:

```text
python3 evidence/export_attractor_certificate.py
python3 evidence/check_labelled_certificate.py
```

The first command reconstructs `evidence/attractor_certificate.json`.  The
second is separately implemented, imports no exporter/search code, and writes
`evidence/labelled_checker_report.json`.  Its report has status `pass`, compares
the graph digest and canonical counts with `evidence/triage_attractor.json`, and
records certificate SHA-256
`a544375352b451c4f703477b9ea88c3dfad6096573cb3c1b4e2cc80dbb8bc779`.

This is an exact exhaustive certificate for this 16-vertex game only.  It makes
no assertion about larger tori and no priority claim beyond the bounded source
comparison in `problem.md`.
