# Breaker exact census audit

## Formal convention and reduction

For a finite simple connected graph `G` on exactly 9 vertices, adjacency
signature means `s(H)=n_+(A(H))-n_-(A(H))`; zero eigenvalues contribute zero.
Let `B` be the unsigned vertex-edge incidence matrix and `Q=BB^T=D+A`.
Since `A(L(G))=B^TB-2I`, if the inertia of `Q-2I` is `(a,b,d)`, then the
inertia of `A(L(G))` is exactly `(a,b,d+m-n)`.  (The zero eigenvalue of `Q`
for connected bipartite `G` is absent from the nonzero spectrum of `B^TB`,
and cancels with the corresponding extra kernel dimension.)  Thus all
inertia calculations in the census are over `Q-2I`, an integer 9 by 9 matrix.

## Enumeration and commands

The generator was the Ubuntu amd64 build of nauty 2.8.9, extracted without
installation from `nauty_2.8.9+ds-1_amd64.deb` (SHA-256
`194f56cb6123d84834b026f7ca48a5219b6d648a480e781d624341d5175912d1`),
with `libnauty-2.8.9` package SHA-256
`5ac4c57ea71b6c462ae35de84b7c8e51e3b02e2444da00577df58a577c521339`.

Generation command (the package prefixes programs with `nauty-`):

    LD_LIBRARY_PATH=... nauty-geng -cq 9 > data/connected9.g6

The file has 261080 lines and SHA-256
`fe73f2b8aad1a653b6f3bee799efff369cc486688df5aeade62ce0b3b5889eb5`.
Here `-c` means connected and `-q` suppresses auxiliary output; geng emits
one canonical representative of every unlabeled simple graph in graph6.

Census command:

    python3 src/exact_census.py --input data/connected9.g6 \
      --summary data/census_summary.json --candidates data/minimum_margin.jsonl

Python was 3.10.12, SymPy 1.14.0, NetworkX 3.4.2.  The census uses only
`fractions.Fraction` congruence elimination for inertia.  It found no negative
margin; minimum margin zero occurs for exactly six graph6 records.

## Independent checks

`verify_equality.py` explicitly constructs each equality line graph, computes
its exact characteristic polynomial in SymPy, square-free factors it, and
uses exact real-root isolation with multiplicities.  All six records verify;
the serialized output is `data/equality_direct_charpoly.json`.

`crosscheck.py` applies the same independent direct-line-graph evaluator to
105 evenly spaced records (indices divisible by 2500) in the order-9 corpus.
All 105 agree with the census evaluator; see
`data/crosscheck_stride2500.json`.

## Superseded run and detected defect

An initial run incorrectly used line-graph negative count
`d+m-n+b0`, with `b0=1` for connected bipartite graphs.  The independent
direct-line-graph cross-check caught the error on the first graph, a tree.
The correct expression is `d+m-n`: one must first remove the `b0` zero
eigenvalues of `Q` before adding the kernel eigenvalues of `B^TB`.  The old
histogram (which had margin-1 count 1 and margin-2 count 3) is superseded.
The final corrected histogram has margin-1 count 21 and margin-2 count 30.
The six equality graphs are nonbipartite, so their records did not change.

