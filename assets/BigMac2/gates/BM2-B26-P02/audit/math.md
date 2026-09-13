# Fresh mathematical audit

## Frozen scope and integrity

I reviewed the claim frozen by snapshot
`9d187ad65fc4f91f8917a488d7a8505255d5d1118baaed63f542cd964662a043`.
Every file named in the snapshot was present and had its recorded SHA-256
digest. In particular, `source.md` retained SHA-256
`e8d3f12668e1311cc09c0fb6df882dfb0726e649e17c394b04813b8d6b92fe1a`.

The candidate claim is exactly the universal statement in the immutable
source: for each connected non-tree simple graph on eight vertices, each
genuine nonedge, and each fixed start (including either endpoint of the new
edge), adding that edge changes the expected discrete-time cover time. It does
not assert a sign, a worst-start statement, a tree case, another order, or the
unrestricted conjecture. Thus an accepted computation must cover all marked
instances rather than an orbit-reduced or weakened subfamily.

## Reconstruction of the exact argument

For a connected graph (H), a nonempty proper set (B\subsetneq V(H)), degree
matrix (D), and adjacency matrix (A_H), put

\[
M_B=D[B,B]-A_H[B,B].
\]

For real (z\in\mathbb R^B),

\[
z^TM_Bz=\sum_{xy\in E(H[B])}(z_x-z_y)^2+
\sum_{\substack{xy\in E(H)\\x\in B,\ y\notin B}}z_x^2.
\]

Every component of (H[B]) has an edge to its complement, so the displayed
form is positive definite. Hence each (M_B) is nonsingular over
\(\mathbb Q\), and all rational systems used below have unique solutions.

In the visited-set formulation, after multiplying the one-step recurrence by
the current degree, the unknowns for a fixed visited set (B) satisfy

\[
d(x)C(x,B)-\sum_{\substack{y\in B\\y\sim x}}C(y,B)
=d(x)+\sum_{\substack{y\notin B\\y\sim x}}C(y,B\cup\{y\}).
\]

The coefficient matrix is (M_B), and strict supersets on the right are
already known when subsets are processed in decreasing cardinality. The code
implements this recurrence for every nonempty proper mask and reads
\(C(s,\{s\})\), so the starting vertex is counted as visited at time zero.

The second formulation is genuinely different at the probabilistic level.
For nonempty (S\subseteq V(H)), let (h_S(x)) be the time to hit (S).
On (U=V(H)\setminus S), its equations are (M_Uh_S=d_U). The pointwise
inclusion-exclusion identity for the maximum of the vertex hitting times gives

\[
t_{\rm cov}(H,s)=\sum_{\varnothing\ne S\subseteq V(H)}
(-1)^{|S|+1}h_S(s).
\]

This follows, for example, by applying inclusion-exclusion to the tail event
that at least one vertex has not yet been hit and then summing over time. Terms
whose target contains (s) are zero. I checked that the complement-mask sign
and the omission of the all-target term in the implementation agree with this
identity. This route uses absorbing hitting-time systems and a forward/back
solver rather than visited-set states and Gauss--Jordan elimination.

Let (p) be one of the tested primes. Whenever every encountered (M_B) is
nonsingular modulo (p), its determinant is not divisible by (p), so the
unique modular solution is the well-defined reduction of the rational
solution. Induction over the visited subsets gives the same conclusion for the
first formulation. Therefore rational equality of a base and augmented cover
time would force equality of their residues at every such good prime. A single
nonzero good-prime residue is consequently an exact certificate of rational
nonequality; no denominator bound or rational reconstruction is needed. The
program tests primality, uses row pivoting, and aborts on any missing pivot.

## Exhaustiveness and implementation checks

The stored headerless graph6 inventory contains 11,094 distinct records. A
fresh invocation of `geng` gave 11,117 connected unlabelled order-eight
graphs, of which 23 have seven edges and 11,094 have between eight and 28
edges. Since a connected graph of order eight is a tree exactly when it has
seven edges, the latter stream is precisely the required connected non-tree
inventory. The independent NetworkX codec check validates all 11,094 records,
connectivity, round trips, and edge counts. The complete graph is correctly
present but has no genuine nonedge, so its marked domain is empty.

For every inventory record the decisive loop enumerates all 28 unordered
pairs and skips exactly the existing edges, then iterates all eight starts. It
therefore covers 150,573 nonedges and 1,204,584 marked triples, without a
nonedge or start orbit reduction. The augmented adjacency matrix is formed
directly. For every base graph, both formulations are solved at both primes.
For every augmented graph, the visited-set method is solved at 1,000,003 and
the absorbing inclusion-exclusion method at 1,000,033. All principal systems
were nonsingular. The direct comparisons report zero equal residues in both
routes. Thus every one of the 1,204,584 rational differences is nonzero. The
root-canonical lookup is an additional consistency check, not a dependency of
this direct conclusion.

I inspected the graph6 decoder, pair/start loop, adjacency augmentation,
finite-field operations, both elimination routines, recurrence ordering, and
comparison counters. Array bounds and integer products are safe at the stated
order and moduli; pivot failures return failure rather than a success record.

I then ran `evidence/reproduce.sh` in a fresh temporary directory. It
regenerated the inventory and both rooted streams byte-for-byte, recompiled
the census, reran all marked instances, and reproduced every non-timing result
field with status `pass`. It also reproduced the exact rational regression.
As a further rational check at order eight, I evaluated base and augmented
graphs at inventory indices 0, 127, 5547, and 11092 (edge counts 8, 8, 14,
and 27). On each, the two exact-rational formulations agreed for every start
before and after adding the selected nonedge, and all eight differences were
nonzero. The recorded details are in `audit/referee-checks.json`.

Finally, any labelled graph in the quantified class is isomorphic to an
inventory representative. Transporting its nonedge and start gives one of the
explicitly processed marked triples, and fixed-start cover time is invariant
under such a rooted isomorphism. This transfers the finite census to the full
labelled universal quantifier.

## Source comparison, limitations, and verdict

Within the frozen source comparison, the cited prior census stops at all
graphs through order seven and at trees for orders eight and nine. The present
claim resolves exactly the omitted connected cyclic order-eight fixed-start
layer. That delta is a complete, non-routine finite classification with an
independently reproducible exact certificate. The frozen evidence did not
include the cited paper PDF, so this mathematical audit does not independently
certify literature priority or broader open status; it makes neither claim.
That limitation does not affect equivalence to the immutable problem or the
correctness and substantive value of the proved finite result, and citation
verification remains a separate release-stage task.

No mathematical gap remains in the frozen scope. **Verdict: accept.**
