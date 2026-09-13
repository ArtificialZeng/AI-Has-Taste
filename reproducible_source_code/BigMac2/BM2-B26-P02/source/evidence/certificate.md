# Exact exhaustive certificate for the order-eight fixed-start layer

## Certified statement

For every connected non-tree simple graph (G) on eight vertices, every
genuine nonedge (uv), and every start (s),

\[
t_{\rm cov}(G+uv,s)-t_{\rm cov}(G,s)\ne 0.
\]

This certificate concerns only the frozen statement in `source.md` under the
reading in `problem.md`.

## Inventory completeness

Nauty 2.9.3 was run as

```text
/opt/homebrew/bin/geng -cq 8 8:28 evidence/order8-connected-nontrees.g6
```

The stream contains 11,094 headerless graph6 records and has SHA-256
`63b2d6b5a6092d23ea899a1cf4d50305ab45d746c389562ad3dcdbcc7da97307`.
The `-c` option restricts to connected graphs, and `8:28` restricts the edge
count.  A connected graph on eight vertices is a non-tree exactly when it has
at least eight edges.  Thus this is one representative of each required
unlabelled class.  The program checked that all 11,094 records are distinct,
connected, and have 8--28 edges.  An independent NetworkX 3.6.1 decode and
round-trip checked every record and reproduced the edge distribution in
`graph6-crosscheck.json`.

Enumerating every absent unordered vertex pair of every record gives 150,573
nonedges.  Enumerating all eight starts for each gives exactly 1,204,584 marked
instances.  No nonedge or start orbit reduction was used in the decisive
direct scan.

## Why finite-field nonzero residues are exact certificates

For a graph (H), let (D) and (A_H) be its degree and adjacency matrices.
For every nonempty proper vertex subset (B), put

\[
M_B=D[B,B]-A_H[B,B].
\]

This matrix is nonsingular over the rationals.  Indeed,

\[
z^T M_Bz=
\sum_{\substack{xy\in E(H)\\x,y\in B}}(z_x-z_y)^2+
\sum_{\substack{xy\in E(H)\\x\in B,\ y\notin B}}z_x^2.
\]

Every component of the induced graph on (B) has a boundary edge because
(H) is connected and (B\ne V(H)).  Equality therefore forces (z=0).
Consequently all cover-time systems below have unique rational solutions.

Let (p) be a prime for which every encountered (M_B) remains nonsingular
over (\mathbb F_p).  Reducing the integer systems modulo (p) then commutes
with solving them.  Hence every computed finite-field cover time is exactly
the residue of the corresponding rational cover time.  In particular,

\[
t_{\rm cov}(H_1,s)=t_{\rm cov}(H_2,s)\quad\Longrightarrow\quad
t_{\rm cov}(H_1,s)\equiv t_{\rm cov}(H_2,s)\pmod p.
\]

Thus one nonzero good-prime residue proves rational nonequality.  The code
certifies primality of 1,000,003 and 1,000,033 by trial division, detects every
zero pivot with row pivoting, and aborts rather than reporting success if any
principal system is singular.  The completed run encountered no singular
system under either prime.

## Two exact formulations

Method A is the visited-set recurrence from `problem.md`.  For fixed visited
set (B), multiplying by degrees gives a system with coefficient matrix
(M_B); the right side uses already solved strict supersets.  It is solved in
decreasing subset size by Gauss--Jordan elimination.

Method B is structurally different.  For nonempty (S\subseteq V(H)), let
(h_S(x)) be the expected time to hit (S), with value zero on (S).  On
(U=V(H)\setminus S), the absorbing-chain equations are

\[
M_U h_S=d_U.
\]

The pointwise inclusion--exclusion identity for the maximum of the vertex
hitting times gives

\[
t_{\rm cov}(H,s)=
\sum_{\varnothing\ne S\subseteq V(H)}(-1)^{|S|+1}h_S(s).
\]

Method B solves these systems by unnormalised forward elimination and back
substitution.  It neither uses visited-set states nor Method A's recurrence.

Before the order-eight run, both formulations were also evaluated over
(\mathbb Q), using Python `Fraction` for Method A and SymPy exact matrices for
Method B, on three order-seven graphs and their edge augmentations.  All 42
base/augmented start values agreed as reduced rationals; the complete values
are in `exact-regression.json`.

## Exhaustive result

The decisive direct scan in `census_modular.cpp` did the following for every
inventory representative and every one of its nonedges:

1. Compute the eight base cover times with both formulations under both
   primes and compare the two formulations.
2. Construct the labelled augmented graph directly.
3. Recompute all eight augmented cover times by Method A under 1,000,003 and
   independently by Method B under 1,000,033.
4. Compare each augmented residue with the corresponding base residue.

There were 177,504 base graph/start/prime comparisons between the two methods,
all equal.  There were 150,573 directly solved augmented graphs and 1,204,584
marked comparisons per method.  The number of zero difference residues was
`[0, 0]`.  Therefore every marked rational difference is nonzero.

As an additional check, every rooted base and augmented instance was
canonicalised by `labelg` with the start in a singleton color class.  Lookup
through all 72,374 rooted isomorphism classes independently produced zero
residue counts `[0, 0]` under the two primes.

Finally, an arbitrary labelled graph in the frozen scope is isomorphic to one
inventory representative.  Its marked nonedge and start transport to a
nonedge and start explicitly processed for that representative, and cover
time is invariant under rooted graph isomorphism.  The direct census therefore
settles the entire frozen universal statement.

## Reproduction and fixed artifacts

The run command was

```text
/usr/bin/clang++ -std=c++20 -O3 -DNDEBUG -Wall -Wextra -pedantic \
  evidence/census_modular.cpp -o evidence/census_modular
evidence/census_modular evidence/order8-connected-nontrees.g6 \
  evidence/base-rooted-canonical.g6 \
  evidence/augmented-rooted-canonical.g6 \
  > evidence/census-modular-result.json
```

`reproduce.sh` regenerates the Nauty inventory and both rooted streams in a
fresh temporary directory, compares them byte-for-byte, recompiles the census,
reruns both the census and rational regression, and compares all non-timing
fields.  Its recorded run passed.  Critical hashes are recorded in
`run-metadata.json` and `reproduction-result.json`.

The computation was performed on macOS 26.5 arm64 with Apple clang 21.0.0,
Nauty 2.9.3, and the required research Python 3.12.14.  The computational
conclusion is an exact finite-field certificate, not floating-point evidence.
