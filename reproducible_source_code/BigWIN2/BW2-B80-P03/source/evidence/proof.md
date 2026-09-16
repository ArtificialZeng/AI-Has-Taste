# Exact toughness under tetrahedral replacement

This file proves the immutable claim in `source.md` under the precise reading
in `problem.md`.  All graphs below are finite and simple.  Let

\[
B=\{a,b,c\},\qquad A=\{x,y,z,w\},\qquad H=R_v(G).
\]

Thus, `B` induces a triangle, `A` induces a `K_4`, every edge from `A` to
`V(G)-{v}` ends in `B`, each member of `B` has two neighbors in
`{x,y,z}`, and `w` has no neighbor outside `A`.

## Lemma 1 (lower-bound transfer)

If `0 <= t <= 3/2` and `G` is `t`-tough, then `H` is `t`-tough.

### Proof

Fix `S subseteq V(H)` with `d=c(H-S)>=2`, and set

\[
 S_0=S\setminus A,\qquad k=|S\cap A|,
 \qquad g=c(G-S_0),\qquad
 g'=c((G-v)-S_0).
\]

Here `S_0` is viewed as a subset of `V(G)-{v}`.  Since `B` is a clique,
all vertices of `B-S_0`, when any exist, lie in one component of
`(G-v)-S_0`.  Adding `v` therefore gives

\[
 g=\begin{cases}
 g',&B-S_0\ne\varnothing,\\
 g'+1,&B\subseteq S_0.
 \end{cases} \tag{1}
\]

We audit all five possible values of `k`.

**Cases `k=0,1`.**  The nonempty graph `H[A-S]` is connected.  Moreover,
at most one of `x,y,z` was deleted, so every vertex of `B-S_0` has a
neighbor in `A-S`.  If `B-S_0` is nonempty, both the gadget in `H-S` and
`v` in `G-S_0` attach to the component containing `B-S_0`; if it is empty,
each is one isolated component relative to the same graph
`(G-v)-S_0`.  Hence `d=g`.  In particular `g>=2`, and

\[
 |S|\ge |S_0|\ge t g=t d.
\]

**Cases `k=2,3`.**  Again `H[A-S]` is nonempty and connected.  Adding it
to `(G-v)-S_0` either joins one existing component or creates one new
component.  Thus

\[
 d\le g'+1\le g+1. \tag{2}
\]

If `g>=2`, toughness of `G`, (2), and `k>=2>=t` give

\[
 |S|=|S_0|+k\ge t g+k\ge t(g+1)\ge t d.
\]

It remains to consider `g=1`.  From `d>=2` and (2), `d=2`.  If `k=3`,
then `|S|>=3>=2t=td`.  If `k=2` and `S_0` is nonempty, the same inequality
follows from `|S|>=3`.  Finally, `k=2` and `S_0` empty cannot occur with
`d=2`: the graph `G-v` is connected because `G` is connected and the
three neighbors of `v` form a clique; the two surviving vertices of `A`
induce a connected graph, include at least one of `x,y,z`, and hence attach
to `B`.  Thus `H-S` would be connected.

**Case `k=4`.**  In this case

\[
 H-S=(G-v)-S_0=G-(S_0\cup\{v\}),
\]

so the `t`-toughness of `G` applies because the displayed graph has `d>=2`
components.  It yields `|S_0|+1>=td`, and consequently

\[
 |S|=|S_0|+4\ge td.
\]

Every admissible `S` satisfies `|S|>=t c(H-S)`, proving the lemma. `square`

## Lemma 2 (an optimum avoids the replaced vertex)

Suppose that `G` is noncomplete.  If it has a degree-three vertex `v`
whose neighborhood `B` is a clique, then some toughness-minimizing set of
`G` avoids `v`.

### Proof

Because `G` is noncomplete and finite, an admissible minimizing set `Q`
exists.  Put `d=c(G-Q)>=2`.  Suppose for a contradiction that `v in Q`,
and put `Q_0=Q-{v}`.

If `B` is not contained in `Q`, restoring `v` attaches it to the one
component containing all surviving members of the clique `B` and merges no
components.  Hence `c(G-Q_0)=d`, while `|Q_0|=|Q|-1`, contradicting the
minimality of `|Q|/d`.

If `B subseteq Q`, restoring `v` makes it an isolated component, so
`c(G-Q_0)=d+1`.  Again the resulting set is admissible, and

\[
 \frac{|Q|-1}{d+1}<\frac{|Q|}{d},
\]

another contradiction.  Thus every minimizing set in fact avoids `v`.
`square`

## Theorem

For every finite plane triangulation `G` and every degree-three vertex `v`,

\[
 \tau(R_v(G))=\min\{\tau(G),3/2\}.
\]

### Proof

First suppose `G` is not `K_4`.  It has at least five vertices: a plane
triangulation of order three has no degree-three vertex, and the unique
plane triangulation of order four is `K_4`.  Deleting
`B=N_G(v)` leaves the isolated vertex `v` and at least one other vertex.
Therefore

\[
 \tau(G)\le \frac{|B|}{c(G-B)}\le\frac32. \tag{3}
\]

In particular `G` is noncomplete.  Set `t=tau(G)`.  By (3), Lemma 1 gives
`tau(H)>=tau(G)`.

For the reverse inequality, choose by Lemma 2 a minimizing set
`Q subseteq V(G)-{v}`, and write `d=c(G-Q)>=2`.  No gadget vertex belongs
to `Q`.  If `B-Q` is nonempty, the connected gadget `A` in `H-Q` attaches
to precisely the same component of `(G-v)-Q` to which `v` attaches in
`G-Q`.  If `B subseteq Q`, `A` is one isolated component in `H-Q`, just as
`v` is in `G-Q`.  In both cases

\[
 c(H-Q)=c(G-Q)=d.
\]

Thus

\[
 \tau(H)\le\frac{|Q|}{c(H-Q)}
 =\frac{|Q|}{c(G-Q)}=\tau(G).
\]

Together with the lower bound this proves
`tau(H)=tau(G)=min{tau(G),3/2}` in the non-`K_4` case.

Now let `G=K_4`.  By convention `tau(G)=infinity`, and `K_4` is
`3/2`-tough, so Lemma 1 gives `tau(H)>=3/2`.  Conversely, deleting
`{x,y,z}` from `H` leaves exactly two components: the isolated vertex `w`
and the triangle on `B={a,b,c}`.  Hence

\[
 \tau(H)\le \frac{3}{2}.
\]

Therefore `tau(H)=3/2=min{infinity,3/2}`, as required. `square`

## Dependencies and gap list

The proof uses only the defining adjacencies of the replacement, the fact
that the neighbors of a degree-three vertex in a plane triangulation induce
a triangle, and the elementary order-four classification of plane
triangulations.  It does not assume Theorem 1.4(ii) of the source paper;
Lemma 1 is its parameterized separator proof.  Known gaps: none.
