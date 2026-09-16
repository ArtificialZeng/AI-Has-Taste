# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim that, for the Cartesian product
`H=C_3 square C_4` on `Z_3 x Z_4`, the connectivity-code number for arbitrary
(not necessarily linear) families of edge subsets is `m(H)=16`.  The status
`proved` is appropriate only if both the universal upper bound and the explicit
16-word construction are valid at this full scope.

Before reviewing the mathematics, I recomputed SHA-256 digests for `claim.json`
and every file in `audit/snapshot.json`.  All digests agreed with snapshot
`fcab1078c67cde7833ebd4bbeb78fea82164cea4524e20d43643410a3a67d264`.

## Reconstruction of the decisive argument

For the upper bound, fix a vertex `v`.  If two codewords have the same
restriction to the four edges incident with `v`, their symmetric difference
contains no incident edge at `v`; hence `v` is isolated and that difference is
not a connected spanning subgraph.  Restriction to `delta_H(v)` is therefore
injective on every connectivity code.  Since `H` is 4-regular, there are only
`2^4=16` possible restrictions.  Thus `m(H)<=16`.  This argument applies to
arbitrary nonlinear families and uses no normalization assumption.

For the lower bound, the four masks

`470c7f, 296bf4, fb304a, 17e0e8`

generate 16 binary edge masks.  For coefficient vectors `a,b`, the symmetric
difference of the corresponding words is the word indexed by `a XOR b`.
Consequently it is enough to verify that every one of the 15 nonzero generated
words spans a connected subgraph.  The serialized certificate supplies, inside
each such word, 11 distinct edges connecting all 12 vertices.  These subsets
are spanning trees, so all nonzero words are connected.  They are also nonzero,
which makes the 16 generated words distinct.  Thus they form a 16-word
connectivity code and give `m(H)>=16`.

## Independent exact checks

I independently derived adjacency from cyclic coordinate distance, rather than
trusting the search model or its flow variables.  The resulting 24 unordered
edges agreed with the serialized edge list, were all distinct, and gave degree
4 at each of the 12 vertices.  I then reconstructed the 16 masks directly from
the four hexadecimal generators and used a separate union-find connectivity
calculation on all 120 unordered pairwise symmetric differences.  All 120 were
connected, and all 16 masks were distinct.

I also checked every serialized tree entry: its mask equals the corresponding
nonzero generated word; its 11 edge indices are distinct, in range, and present
in that word; and those edges connect all 12 vertices.  Finally, I reran the
supplied verifier, which independently reported 15 connected nonzero words, 120
connected pairwise differences, and 15 valid spanning-tree certificates.

The empty word causes no issue because connectivity is required only for
differences of distinct codewords.  The construction's linearity is likewise
not a restriction on the maximization problem: it is a permitted witness, while
the upper bound already covers all families.  No limiting, division, or hidden
nondegeneracy step occurs.

## Source comparison and contribution

The frozen Tian PDF uses the same connectivity-code definition and degree
bound.  Its page 8 concluding remarks explicitly state that determining
`m(C_m square C_n)` remains open; page 1 records the diagonal `C_3 square C_3`
and `C_4 square C_4` cases.  The candidate settles only the frozen
`C_3 square C_4` instance and does not claim a solution for all products or
absolute priority beyond the bounded screen recorded in `problem.md`.  The
proof is self-contained, and its full-scope exact construction is a substantive
resolution of the original fixed instance.  No unstated literature claim is
needed for mathematical correctness.

## Verdict

**Accept.**  The upper bound is valid for arbitrary connectivity codes, the
explicit lower-bound witness passes independent exact replay, and together they
prove the exact frozen statement `m(C_3 square C_4)=16`.  I found no scope,
correctness, or contribution gap requiring revision.
