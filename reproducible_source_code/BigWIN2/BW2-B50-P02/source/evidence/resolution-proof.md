# Exact finite resolution argument

## Theorem submitted for audit

Use the definitions and the two-item cyclic-Gray-code convention fixed in
`problem.md`. For every connected unlabelled loopless simple graph $G$ with
$2\leq |V(G)|\leq6$,

\[
 AO(G)\text{ has a Hamilton cycle}\quad\Longleftrightarrow\quad\sigma(G)=0.
\]

There are 142 graph classes. Exactly 125 have signature zero and are
Hamiltonian; the other 17 have nonzero signature and are non-Hamiltonian.
Hence there is no counterexample to signature-zero sufficiency in this domain.

## Completeness of the graph and orientation domains

For each $n=2,\ldots,6$, `atlas-enumerate.py` examines all
$2^{\binom n2}$ labelled simple graphs, tests connectedness, and takes the
lexicographically least graph6 encoding over all $n!$ vertex permutations.
Orbit deduplication gives respectively $1,2,6,21,112$ representatives. The
resulting 142-identifier set equals the independently canonicalized connected
portion of `networkx.graph_atlas_g()`. `atlas-verify.py` also rejects every
same-order pair as nonisomorphic. Thus the list has both coverage and uniqueness.

For a representative with $m$ lexicographically ordered edges, the generator
examines all $2^m$ bit vectors and retains exactly those passing an integer
Kahn acyclicity test. It checks that this set equals the orientations induced by
all $n!$ vertex orders: every order induces an acyclic orientation, while every
acyclic orientation has a topological order. Flip edges are then exactly pairs
of retained vectors at Hamming distance one. `atlas-verify.py` reconstructs the
same orientation and flip sets using NetworkX digraph acyclicity routines. The
atlas therefore exactly represents every $AO(G)$ in the claimed domain.

## The 17 negative cases

Color an orientation bit vector by the parity of its Hamming weight. Reversing
one edge changes that parity, so every $AO(G)$ is bipartite with these two
color classes. A Hamilton cycle, including under the fixed two-vertex boundary
convention, alternates colors and therefore contains equally many vertices of
each color. Their cardinality difference is

\[
 \sum_{A\in AO(G)}(-1)^{\operatorname{rk}_{D_0}(A)},
\]

whose absolute value is $\sigma(G)$. Consequently $\sigma(G)\ne0$ proves
non-Hamiltonicity. Exact enumeration finds 17 such
graphs, with canonical graph6 identifiers

```
C] DFw DLs D]{ E?~o E@vg E@vo EBj? EBjW EBjg EBz_ EBzw EB~o
EJeg EJnW ELvg E]~o
```

`hamilton-verify.py` independently reconstructs their orientations from the
edge lists, recomputes both parity-class sizes, and checks their unequal
difference against every recorded nonzero signature.

## The 125 positive cases

`hamilton-cycles.json` gives, for each of the other 125 representatives, a
cyclic list of orientation bit vectors. The lists were discovered by the
single-worker deterministic `AddCircuit` feasibility search in
`hamilton-search.py`; solver status is not used as proof. Instead,
`hamilton-verify.py`, which does not import the solver, reconstructs the full
acyclic-orientation set directly from each graph's edge list and verifies:

1. the cyclic list has no repetition and its set equals the full reconstructed
   acyclic-orientation set;
2. every consecutive pair, including the closing pair, has Hamming distance
   one; and
3. the exceptional two-item list occurs only for $K_2$ and its two entries
   differ in the unique edge.

The verifier reports 125 valid cycles in order counts $1,2,5,18,99$, covering
17,130 orientation vertices. Thus all signature-zero cases are Hamiltonian.
Together with the parity argument, this proves the theorem and supplies the
requested complete classification.

## Dependencies, limitations, and gap list

The mathematical dependence is only on exhaustive finite enumeration, the
elementary topological-order characterization of acyclic digraphs, and the
bipartite alternation argument above. All decisive calculations use finite
integers and explicit lists; neither a timeout nor an infeasibility response is
used. The primary-source PDF is included to bind definitions and the nearest
reported census, not to replace the proof above. The claim is only for the
frozen order-at-most-six domain and makes no unrestricted classification or
priority assertion. Known proof gaps for that finite scope: none. Independent
referee review remains required before acceptance.
