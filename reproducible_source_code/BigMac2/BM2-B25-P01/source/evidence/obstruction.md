# Exact obstruction for the frozen `q=4, r=3` instance

## Claim resolved

There is no four-layer balanced directed Hamilton cycle in
\(C_4(3)=\operatorname{Cay}(\mathbb Z_{12},\{1,2,3\})\). In particular,
there cannot be one whose three translates contain
\(0\to2,2\to4,4\to6\) in three distinct cycles, so the existential question
in `source.md` has a negative answer.

## Completeness of the finite domain

For each \((j,s)\in\mathbb Z_4\times\{1,2,3\}\), balance requires exactly
one representative of the orbit whose possible tails are
\(j,j+4,j+8\). Writing the chosen tail as \(j+4t_{j,s}\), with
\(t_{j,s}\in\{0,1,2\}\), is therefore a bijection between balanced arc sets
and the \(3^{12}=531441\) twelve-digit ternary vectors
\((t_{j,s})\). No symmetry reduction or sampling is used.

Every selection has exactly twelve arcs. It can be a directed Hamilton cycle
only if all twelve tails and all twelve heads are distinct. Those two tests
make its arcs the graph of a permutation \(f\) of \(\mathbb Z_{12}\). It is
then a Hamilton cycle if and only if the orbit of 0 under \(f\) contains all
twelve vertices (and returns to 0 after twelve applications). These are
finite integer and bit-mask predicates.

As an internal count check, distinct tails require, independently in each
layer, that the three step-orbits choose the three possible tails in some
order. Hence exactly \((3!)^4=1296\) selections pass the outdegree test.

## Exhaustive result and separate replay

`enumerate_balanced.py` visits the domain with `itertools.product` in
layer-major orbit order. `enumerate_replay.py` instead visits integer codes
\(0,\ldots,3^{12}-1\), decodes them in base three, and uses step-major orbit
order. They share no enumeration routine. Both use exact integers and both
serialize every selection passing the indegree and outdegree tests, together
with its canonical directed-cycle decomposition.

The exact agreed counts are:

| predicate | count |
|---|---:|
| balanced selections visited | 531441 |
| indegree unrestricted, outdegree one | 1296 |
| indegree and outdegree one | 15 |
| one directed 12-cycle | 0 |
| also satisfying the prescribed development colours | 0 |

The fifteen permutation survivors consist of twelve decompositions of type
\(6+6\) and three of type \(4+8\); thus every survivor has two directed
cycles. After canonical sorting, the complete survivor records have SHA-256
`b36456535b5da51566823d0c7781e5d398dd6beb8a4f85ce21a347d181a6f77b`.
Both programs print those fifteen records, so the digest is not a substitute
for inspectable data. `crosscheck.py` reruns both programs and rejects unless
their counts, complete survivor records, cycle-type histogram, input hashes,
and target result agree. Its recorded output is `crosscheck.json`.

Replay from the project directory with the required research interpreter:

```sh
/Users/mac/4prove-or-disprove-math/.research-venv/bin/python evidence/enumerate_balanced.py
/Users/mac/4prove-or-disprove-math/.research-venv/bin/python evidence/enumerate_replay.py
/Users/mac/4prove-or-disprove-math/.research-venv/bin/python evidence/crosscheck.py
```

The recorded crosscheck reports `pass`, uses that exact interpreter, and binds
the frozen input hashes. In particular, it records `source.md` SHA-256
`ea3d097839f8cdfdfcd8a59c1df8afb91c7c37250f6bef314a0a0f9eda58ff4f`.

## Logical conclusion and scope

The domain bijection exhausts every balanced arc set. The degree filters are
necessary for a Hamilton cycle, and all fifteen selections passing both
filters have two components rather than one. Therefore no balanced Hamilton
cycle exists. This is stronger than merely failing the requested arc-colour
condition, but it is asserted only for the frozen \(q=4,r=3\) instance. No
claim is made here about other \(r\equiv3\pmod4\) cases or about literature
priority.
