# Exact `n <= 32` integral-circulant perfectness census

Research job: `bigMac-00023-p06-research-d993171d8665`  
Scope: the 539 pairs in the preliminary layer of the frozen `n <= 64` task  
Status: result-note candidate; the original `n <= 64` classification remains unresolved

## Exact statement encoded by the manifest

For each `n`, write the strict divisors in increasing order as
`D_n = [d_0,...,d_{k-1}]` and encode `D` by

```text
dmask(D) = sum(2^i : d_i in D).
```

Among all 539 pairs `(n,D)` with `1 <= n <= 32`, exactly 415 give perfect
graphs and exactly 124 give imperfect graphs.  Imperfect inputs occur only for
`n` in `{12,20,24,28,30}`.  Their complete mask table is:

| `n` | increasing `D_n` | all imperfect masks |
|---:|---|---|
| 12 | `[1,2,3,4,6]` | `6,9,12,19,22,25` |
| 20 | `[1,2,4,5,10]` | `5,10,12,19,21,26` |
| 24 | `[1,2,3,4,6,8,12]` | `6,9,12,14,19,22,24,25,27,28,29,30,33,34,35,36,38,39,41,44,48,49,51,52,53,54,57,70,73,74,75,76,78,79,83,86,88,89,91,92,93,94,97,98,99,100,102,103,105,108,113,115,118,121` |
| 28 | `[1,2,4,7,14]` | `5,10,12,19,21,26` |
| 30 | `[1,2,3,5,6,10,15]` | `6,10,14,15,17,19,21,22,24,27,28,30,33,35,36,39,41,42,44,46,49,52,53,56,57,61,66,70,71,74,75,78,81,83,85,86,88,91,92,94,97,99,100,103,105,106,108,110,112,113,117,121` |

For every other `n <= 32`, every divisor mask is perfect.  Thus the table is
an unambiguous compression of all 539 Boolean values.  The full record,
including each selected divisor set, adjacency digest, certificate metadata,
and witness, is `evidence/n32_manifest.json`.  Its SHA-256 is

```text
637121fe094a6321bd5c1abf182a215a24e42931d49507cc8d405c39e7e61188
```

and the SHA-256 of its canonical `records` array is

```text
fe36f96a628851b9ef03d912c8d9ec451e48d4c7773ab12626aa36a52610357e
```

## Certificate and completeness argument

The generator `evidence/n32_census.py` constructs each adjacency relation
directly from `gcd(x-y,n) in D`, with integer arithmetic.  It searches for an
induced odd cycle separately in the graph and its complement, for every odd
target length from 5 through `n`.

The reduction to cycles through vertex 0 is complete.  Translation
`x -> x-a (mod n)` is an automorphism of every `ICG_n(D)` and of its
complement.  Hence, if an induced cycle exists, a translate of it contains 0.
For a fixed target length, the depth-first search begins with every neighbor
of 0 and maintains an induced path.  It extends by a vertex exactly when that
vertex is adjacent to the current endpoint and to no earlier
non-predecessor.  A vertex adjacent to 0 is tested only as a closing vertex,
and is accepted exactly when it has no other edge to the path.  Therefore, if
`(0,v_1,...,v_{ell-1})` is any induced cycle in cyclic order, the search has the
branch `0,v_1,...,v_{ell-1}` and accepts it.  Conversely, its acceptance test
ensures precisely the cycle edges and forbids every chord.  Iterating all odd
lengths is therefore a sound and complete odd-hole test.  Applying it also to
the complement is a sound and complete Berge test; the Strong Perfect Graph
Theorem then gives the recorded perfectness value.

The run visited 2,789,071 induced-path search states.  Every one of the 124
imperfect records contains an exact forbidden cycle, canonicalized
lexicographically under translations, multiplication by units modulo `n`,
cycle rotation, and reversal.  There are 105 graph-side and 19
complement-side witnesses: 86 have length 5, 36 length 7, and 2 length 9.

`evidence/replay_n32.py` is a separate verifier: it does not import the
generator, reconstructs all 539 adjacency matrices from the gcd definition,
checks the ordered domain with no omission or duplication, checks adjacency
digests, recalculates witness normal forms, and checks every pair of vertices
in all 124 cycles.  Its output `evidence/n32_replay.json` reports `status=pass`.

As a second implementation check, `evidence/networkx_crosscheck_n32.py` uses
NetworkX 3.4.2's independent `chordless_cycles` enumeration on both sides.  It
checked all 539 records, scanned 1,602,322 chordless cycles up to each decision,
and reported no status mismatch in
`evidence/n32_networkx_crosscheck.json`.  This is corroboration, not a
substitute for the completeness proof above.

## Positive structure screen and limitations

The exact generator also applied elementary sufficient perfectness classes.
Of the 415 positive records, 329 lie in at least one of: bipartite,
co-bipartite, complete multipartite, cluster, chordal, co-chordal, or cograph.
The remaining 86 are a residue only with respect to this short list; they are
not uncertified, because the complete two-sided odd-hole enumeration is their
replayable Berge certificate.  No structural divisor-lattice decomposition of
those 86 cases is claimed.

This result does not classify any `33 <= n <= 64`, does not imply a statement
for unbounded `n`, and does not resolve the frozen original task.  The bounded
primary-source screen in `evidence/primary-source-collision-screen.md` found no
equivalent perfectness census, but that negative search is not proof of
priority.  In particular, So's earlier enumeration of integral-circulant
symbols below 100 for spectral purposes prevents any claim that the underlying
graph inputs were first enumerated here.

