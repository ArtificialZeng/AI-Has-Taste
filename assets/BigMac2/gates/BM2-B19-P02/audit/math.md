# Fresh mathematical referee report

## Frozen scope

The submitted `result-note` claim is the following strict subsidiary of the
original problem: every simple undirected graph with degree sequence
\((5,3^{23})\) has a simple cycle of length 4, 8, or 16.  It does **not** claim
the original minimum-degree-at-least-three assertion, whose status remains
unresolved.  I reconstructed the argument from `source.md`, `problem.md`, the
frozen claim, and the listed proof/code/log evidence.  In accordance with the
referee brief, I did not consult `checkpoint.md`; it is not needed for the
argument below.

## Reconstruction of the reduction

Assume for contradiction that a graph \(G\) of degree sequence
\((5,3^{23})\) avoids all three target cycle lengths, and let \(v\) be its
unique vertex of degree 5.

1. The graph induced by the five vertices of \(N(v)\) has maximum degree at
   most one.  Indeed, if one neighbour of \(v\) were adjacent to two other
   neighbours, those three vertices together with \(v\) would give a simple
   4-cycle.  Thus `G[N(v)]` is a matching of some size
   \(m\in\{0,1,2\}\).
2. No vertex outside \(\{v\}\cup N(v)\) can meet two vertices of \(N(v)\),
   since the two incidences and the two edges to \(v\) would again give a
   4-cycle.
3. Delete \(v\) and its five neighbours.  The remaining graph \(H\) has 18
   vertices.  A matched arm has one edge into \(H\), while an unmatched arm
   has two.  By step 2, the resulting \(10-2m\) endpoints in \(H\) are all
   distinct.  They have degree 2 in \(H\), and all other vertices of \(H\)
   have degree 3.  Consequently
   \[
     |E(H)|=\frac{2(10-2m)+3(8+2m)}2=22+m.
   \]
   Moreover, \(H\) is itself free of 4-, 8-, and 16-cycles.
4. Conversely, take any simple 18-vertex graph with minimum degree 2,
   maximum degree 3, and \(22+m\) edges.  The degree sum forces exactly
   \(10-2m\) vertices of degree 2.  Attaching these distinct ports to the
   five-arm matching gadget, with load one on each matched arm and load two
   on each unmatched arm, produces every possible \(G\) in case \(m\).
   Quotienting by automorphisms of only the five-arm gadget cannot omit an
   attachment (automorphisms of \(H\) may only cause repetitions).

This establishes that the three enumerated cases are exhaustive.  There is
no hidden connectedness assumption: `geng` was invoked without `-c`, so its
ordinary simple-graph enumeration includes disconnected residual graphs.

## Code and exhaustive-computation checks

I checked the frozen SHA-256 values of the claim, original and interpreted
statements, proof record, all three logs, and all four C++ sources against
`audit/snapshot.json`; they match.  The installed `geng` hash also matches the
one recorded in the proof record.  Its own help identifies `-f` as
4-cycle-free, `-d2` as minimum degree at least 2, and `-D3` as maximum degree
at most 3.  A small independent semantic check gave 8 unlabeled 4-vertex
graphs under `geng -f`, versus 11 without `-f`, correctly excluding the
three graphs that contain a (not necessarily induced) 4-cycle.

I rebuilt the frozen search source with Apple clang and reran, from scratch,
all three complete streams

```
geng -q -f -d2 -D3 18 22:22
geng -q -f -d2 -D3 18 23:23
geng -q -f -d2 -D3 18 24:24
```

through the rebuilt verifier.  All runs returned the documented exhaustion
code 20, created no witness, and reproduced the frozen counts exactly:

| \(m\) | residual graphs | residual C8/C16 survivors | attachments | C4 rejects | C8 rejects | C16 rejects |
|---:|---:|---:|---:|---:|---:|---:|
| 0 | 294,693 | 29,143 | 27,540,135 | 15,062,760 | 12,477,375 | 0 |
| 1 | 835,745 | 13,064 | 5,486,880 | 2,331,130 | 3,155,750 | 0 |
| 2 | 1,087,732 | 1,020 | 45,900 | 12,131 | 33,769 | 0 |

For each row, the reject counts sum to the number of attachments.  The
attachment totals also equal the survivor count times, respectively, 945,
420, and 45 gadget-orbit representatives.

I separately rebuilt and ran the supplied component checks.  Exhaustive
permutation canonicalization agreed with the production attachment generator
at exactly 945, 420, and 45 representatives.  The independently written
unpruned cycle DFS agreed with the production detector on all 32,768 labeled
graphs on six vertices for C4, on cycle boundary fixtures of orders 3 through
24, and on the fixed-seed random suite (57,234 comparisons total).  In an
additional fresh parser check, the production graph6 parser's adjacency
matrices agreed byte-for-byte with nauty `showg -a` on an entire deterministic
35,063-graph `geng` shard.  Direct source inspection also confirms that the
cycle routine searches simple paths, chooses the least vertex on a cycle,
and removes only the two orientation duplicates; the 24-bit adjacency masks
and all shifts stay within their 32-bit type.

The construction itself preserves simplicity and gives degree 5 to \(v\)
and degree 3 to every other vertex: every degree-2 residual port receives
exactly one new edge, every degree-3 residual vertex receives none, and the
five arm loads are exactly those forced by the matching case.  Thus every
candidate graph in the frozen scope occurs in the search, and every such
candidate was rejected for containing a target cycle.  This proves the
submitted statement.

## Contribution and source comparison

The supplied frozen source comparison says that Garcia's cited result covers
all general graphs through 23 vertices and the 24-vertex cubic subclass, but
does not decide the full 24-vertex problem.  The present theorem treats one
of the two natural degree-excess-two sequences immediately beyond the cubic
boundary; the other is \((4,4,3^{22})\).  It required a complete three-case
reduction and tens of millions of exact attachment checks, so it is neither a
restatement of the cubic case nor an arbitrary order restriction.  It gives a
usable reduction of the smallest non-cubic boundary and can naturally be
merged with a later treatment of the other excess-two sequence.

The cited Garcia PDF was not part of the frozen evidence list available to
this referee, so this review certifies the mathematical delta relative to the
precise source characterization frozen in `source.md` and `problem.md`, not a
global priority claim.  No cited theorem is used as a premise of the proof
above.

## Verdict

**Accept the exact frozen `result-note` scope.**  Correctness/evidence, scope,
and the nontrivial subsidiary contribution all pass.  The original assertion
must remain marked `unresolved`; this acceptance supplies no UNSAT certificate
and says nothing about \((4,4,3^{22})\) or higher degree excess.
