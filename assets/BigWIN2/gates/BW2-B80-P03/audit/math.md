# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the exact `resolution-paper` claim in `claim.json`: for every
finite simple plane triangulation `G` and every degree-three vertex `v`, the
specified tetrahedral replacement `H=R_v(G)` satisfies

\[
\tau(H)=\min\{\tau(G),3/2\},
\]

including `G=K_4`.  I independently recomputed the SHA-256 digests of
`claim.json` and every file listed in `audit/snapshot.json`; all agree with
snapshot digest
`5199d048ca07154a9087dcf01c066f76df20378152da661fda8cc17ac54c41cd`.
The statement reviewed is therefore the frozen statement, with no silent
restriction or correction.

## Reconstruction and correctness audit

Let `A={x,y,z,w}` be the replacement gadget and `B={a,b,c}=N_G(v)`.
The plane-triangulation hypothesis implies that `B` is a triangle.  I
reconstructed the proof from these adjacencies as follows.

For a candidate separator `S` of `H`, put `S_0=S\setminus A`,
`k=|S\cap A|`, `g=c(G-S_0)`, and
`g'=c((G-v)-S_0)`.  Because surviving vertices of `B` lie in one component,

\[
g=g'\quad\text{if }B-S_0\ne\varnothing,
\qquad
g=g'+1\quad\text{if }B\subseteq S_0.
\]

For every `0<=t<=3/2`, assuming `G` is `t`-tough, the five possible gadget
deletion counts give `|S|>=t c(H-S)`:

- If `k=0` or `1`, `A-S` is connected and every surviving vertex of `B`
  still has a neighbor in it.  Adding `A-S` to the common base graph has
  exactly the same component-count effect as adding `v`, so
  `c(H-S)=g>=2`, and toughness of `G` applies to `S_0`.
- If `k=2` or `3`, the surviving part of `A` is nonempty and connected, so
  `c(H-S)<=g'+1<=g+1`.  When `g>=2`, toughness gives
  `|S_0|>=tg`, while `k>=2>=t`, proving the desired bound.  When `g=1`,
  admissibility forces `c(H-S)=2`; then `|S|>=3>=2t`, except potentially
  when `k=2` and `S_0` is empty.  That exception cannot disconnect `H`:
  `G-v` is connected because `G` is connected and `B` is a clique, and the
  two surviving gadget vertices include a member of `{x,y,z}` and hence
  attach to `B`.
- If `k=4`, then `H-S=G-(S_0\cup\{v\})`.  Applying `t`-toughness to the
  latter separator gives `|S_0|+1>=t c(H-S)`, which is stronger than needed
  after all four gadget vertices have been deleted.

Thus `G` being `t`-tough implies `H` is `t`-tough for every
`t<=3/2`.  The proof does not assume the desired equality.

I also checked the reverse transfer rather than relying on the submitted
lemma as a black box.  In a finite noncomplete `G`, a toughness-minimizing
separator exists.  If such a separator `Q` contained `v`, restoring `v`
would either (i) attach it to the unique component containing the nonempty
clique `B-Q`, leaving the component count fixed while reducing the
numerator, or (ii), when `B` is wholly deleted, add one isolated component
while reducing the numerator.  Either operation strictly lowers the ratio.
Hence a minimizing `Q` avoids `v`.  Replacing `v` by the connected gadget
`A` then has exactly the same component-count effect on the common graph
`(G-v)-Q`: both attach to the component containing `B-Q` when it is
nonempty, and both form one isolated component when `B\subseteq Q`.
Consequently `c(H-Q)=c(G-Q)` and `tau(H)<=tau(G)`.

If `G` is not `K_4`, it has at least five vertices.  Deleting `B` leaves
the isolated vertex `v` and at least one other vertex, so
`tau(G)<=3/c(G-B)<=3/2`; also `G` is noncomplete.  Taking `t=tau(G)` in
the lower transfer and combining it with the preceding upper transfer gives
`tau(H)=tau(G)=min{tau(G),3/2}`.

If `G=K_4`, the convention gives `tau(G)=infinity`.  Applying the lower
transfer with `t=3/2` gives `tau(H)>=3/2`.  The graph `H` is noncomplete
because `w` has no neighbor in `B`, and deleting `{x,y,z}` leaves exactly
the isolated vertex `w` and the triangle `B`, giving the matching ratio
`3/2`.  This verifies the required boundary case.

I specifically checked admissibility (`c>=2`) before every use of
toughness, the possible empty common base graph, the `g=1` and equality
cases, the complete-graph convention, and the fact that no division by a
zero component count occurs.  I found no circular lemma, omitted gadget
case, or unproved limiting/compactness step.

## Computational and source checks

I inspected `evidence/exact_small_checks.py` and freshly executed it.  It
uses exact rational ratios and exhaustive vertex subsets, and reproduced
the recorded result: seven graph-atlas plane triangulations with a
degree-three vertex, sixteen ordered `(G,v)` inputs through seven vertices,
and the exact `K_4` replacement value `3/2` all satisfy the formula.  This
finite computation is supplementary only; the general verdict rests on the
proof above.

I inspected the supplied primary PDF, Songling Shan,
*Non-Hamiltonian 3/2-Tough Plane Triangulations*, arXiv:2609.05414v1.  Its
definition on PDF page 2 matches the frozen replacement adjacencies.
Theorem 1.4(ii) states only that a `3/2`-tough input has a `3/2`-tough
replacement, and its proof on PDF pages 5--6 uses the corresponding five
separator cases at that single threshold.  It does not state the exact
formula or the reverse transfer for inputs of toughness below `3/2`.
The candidate's precise delta is therefore accurately described relative
to this inspected source.  The evidence makes no global priority claim, and
this review does not infer one from the bounded source comparison.

## Verdict

**Accept.**  The argument proves the frozen original claim in its full
universal scope, including `G=K_4`; the exact separator transfers are valid,
and no unresolved mathematical gap remains within the claimed theorem.
