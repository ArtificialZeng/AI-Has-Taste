# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` statement frozen in `claim.json`, with
original status `proved`, against snapshot digest
`0677f750942dc6e8eaad2b20f9392b0327cb73e0fce1269a5cb0d51e3bd3ef56`.
All seven hashes in `audit/snapshot.json` were recomputed and matched.  The
snapshot digest also equals the SHA-256 hash of the compact sorted-key JSON
serialization of its `files` mapping.

The theorem under review is full-scope: for every integer `m >= 6`, it asserts
the complete identifying-edge set, its full-automorphism orbits, the total and
card-type multiplicities, and a nonisomorphic maximal-planar parent for every
remaining edge orbit.  I did not reinterpret this as a partial result.

## Reconstruction of the decisive argument

Write `e_i=r_i r_{i+1}`.  The degrees in `J_m` are

`d(p)=m+1`, `d(q)=m`, `d(w)=3`, `d(r_0)=d(r_1)=5`, and all other
rim degrees are four.  These values are valid also at the boundary `m=6`.

If a maximal-planar graph `H` has an edge card isomorphic to `C=J_m-e`, then,
after transporting the isomorphism, `H` is exactly `C+xy` for one nonedge
`xy`.  Thus one-edge completion is an exhaustive parent test, not merely a
search among a selected family of flips.

For each of `e=pw,wr_0,wr_1`, the card has `w` as its unique degree-two
vertex.  Since a maximal planar graph on these orders has minimum degree at
least three, every parent must add an edge incident with `w`.  The neighbours
of a degree-three vertex in a planar triangulation form a triangle, so the new
endpoint must be a common neighbour of the two neighbours of `w` already in
the card.  Direct intersection of the displayed neighbourhoods gives exactly

| deleted edge | exhaustive possible additions |
| --- | --- |
| `pw` | `wp`, `wq` |
| `wr_0` | `wr_0`, `wr_2` |
| `wr_1` | `wr_1`, `wr_{m-1}` |

Both completions in each row are maximal planar.  The first pair is isomorphic
under interchange of the bipyramid hubs; the second and third pairs are
isomorphic under a rim rotation.  Hence all three edges are identifying and
there is no omitted parent.

For every other edge the proof gives a legal diagonal flip.  The opposite
vertices and replacement edges are respectively

* `pr_0`: `w,r_{m-1}` and `wr_{m-1}`;
* `pr_1`: `w,r_2` and `wr_2`;
* `pr_i`, `i notin {0,1}`: `r_{i-1},r_{i+1}` and
  `r_{i-1}r_{i+1}`;
* `qr_i`: `r_{i-1},r_{i+1}` and `r_{i-1}r_{i+1}`;
* `e_0`: `w,q` and `wq`;
* `e_i`, `i != 0`: `p,q` and `pq`.

In every case the opposite vertices are nonadjacent for `m>=6`, so the flip
is a finite simple maximal-planar parent of the same card.  It is not
isomorphic to `J_m`: an `e_0` flip has two maximum-degree vertices instead of
one; an `e_i` flip for `i!=0` has maximum degree `m+2`; and every `pr_i` flip
has maximum degree at most `m`, instead of `m+1`.  For a `qr_i` flip with
`m>=7`, degree `m` is absent, whereas it occurs at `q` in `J_m`.  At `m=6`,
the stated degree multisets separate `i in {2,3,4,5}`.  For `i=0,1`, both
graphs have unique degree-seven and degree-six vertices, but these are
nonadjacent in `J_6` and adjacent in the rival.  This closes the only degree-
multiset collision and proves that every non-`w` edge is non-identifying.

## Automorphisms, counts, and card types

The degree data fix `p,q,w` and the set `{r_0,r_1}`.  The remaining action is
an automorphism of the induced rim cycle stabilizing the edge `r_0r_1`, hence
is either the identity or `r_i -> r_{1-i}`; both occur.  Therefore
`Aut(J_m)` has order two.  Burnside counting on the three indexed edge
families gives `m/2,m/2,m/2+1` orbits when `m` is even and
`(m+1)/2` in each family when `m` is odd.  Adding the two `w`-edge orbits
produces exactly `3m/2+3` and `(3m+7)/2`, respectively.

Deleting a non-`w` edge never creates a degree-two vertex, so none of those
cards is isomorphic to an identifying card.  The `pw` card has maximum degree
`m`, while the `wr_0` and `wr_1` cards have maximum degree `m+1`; the latter
two are interchanged by the reflection.  The two identifying card types are
therefore distinct and have full-deck multiplicities one and two.

## Checks actually performed

I inspected the cited primary PDF.  Proposition 5.2 and Figure 4 establish
only that the `pw` card identifies `J_m`; Proposition 2.4 states the exact
parent criterion.  They do not supply the additional `wr_0,wr_1`
classification, orbit count, multiplicities, or rival list claimed here.
Thus the submitted delta relative to the cited source is accurately stated.
The source's broader structural question also does not already state this
family classification.  The dossier appropriately describes its literature
search as bounded and makes no priority claim.

I reran `evidence/enumerate_cards.py` for `m=6,7,8,9`.  Its output was
byte-for-byte equal to the frozen census (SHA-256
`350f6e407d726e515d76c11794f43800b344ad9d4a20f7cb279f370cef698b34`).
For the four cases it found automorphism-group order two, respectively
12, 14, 15, and 17 edge orbits, and exactly `p-w,r0-w,r1-w` as identifying.
I also separately enumerated every planar one-edge addition to each of the
three proposed identifying cards for these four values; the additions were
exactly the two in the table above and every resulting parent was isomorphic
to `J_m`.

The proof dossier mentions an additional `m=10,...,20` census that is not in
the frozen snapshot.  I did not use or assess that assertion.  It is expressly
nonessential: the uniform argument above covers all `m>=6`, including parity
and the only exceptional degree comparison.

## Verdict

**Accept.**  Scope, mathematical correctness, exhaustive parent evidence, and
the stated structural contribution all pass.  I found no unresolved
mathematical gap in the frozen claim.
