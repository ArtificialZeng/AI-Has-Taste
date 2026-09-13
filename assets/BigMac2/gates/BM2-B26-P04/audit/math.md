# Fresh mathematical audit

## Scope and binding

This review concerns exactly the frozen existential claim in `source.md`: a
simple graph on exactly 13 vertices whose full local-complementation orbit has
independence number at most four.  The reviewed snapshot digest is
`413f5c03360234d737d20f93f903d94a9e4c26eeddf3b27781609cb6e3077d6d`.
Without opening the prohibited progress summary `checkpoint.md`, I checked the
snapshot hashes of `claim.json`, `source.md`, `problem.md`, and all six decisive
files under `evidence/`; they match `audit/snapshot.json`.  The release gate is
left to check the integrity of the entire frozen mapping.

The candidate has graph6 string ``LlthgsL`mEkLkL``.  Direct decoding gives order
13, and the resulting edge relation is

\[
  ij\in E \quad\Longleftrightarrow\quad
  j-i\pmod {13}\in\{1,3,4,9,10,12\}
  \qquad(i<j),
\]

so it is the stated 39-edge Paley graph (P(13)).  The graph is finite,
undirected, loopless, and represented by exactly the 78 possible adjacency
bits; there is no padding-bit ambiguity.

## Reconstruction of the decisive argument

Let (S) be the 711,440 adjacency keys serialized in
`evidence/paley13_lc_orbit.bin`.

1. The first key is exactly the graph6-decoded candidate.  All keys are distinct
   as full pairs of a 64-bit low word and 14-bit high word.  Thus hash collisions
   cannot merge states, and no isomorphism quotient is being assumed.
2. Each of the other 711,439 records names an earlier parent and a vertex in
   \(\{0,\ldots,12\}\), and its key equals the result of local complementation
   at that vertex.  Induction on record index therefore gives (S\subseteq
   [G]_{\rm LC}).
3. For every key in (S) and every one of the 13 vertices, its local complement
   is again a key in (S).  Since (S) contains (G) and is closed under all
   generators, every finite local-complementation sequence from (G) stays in
   (S), so ([G]_{\rm LC}\subseteq S).  Hence (S=[G]_{\rm LC}).
4. For each state and each of the \(\binom{13}{5}=1287\) five-subsets, the
   induced-edge mask has nonzero intersection with the state's adjacency mask.
   Therefore no orbit member has an independent five-set.  Any independent set
   of size greater than five would contain one of size five, so every member has
   independence number at most four.
5. In orbit record 834, vertices \(\{0,1,2,3\}\) induce no edge.  Thus one orbit
   member has independence number at least four.  Combining the bounds gives
   \(\beta(P(13))=4\), and in particular the frozen existential assertion is
   true.

Reachability plus closure is sufficient to certify the entire labeled orbit;
it does not depend on the claimed numerical orbit size being guessed in
advance.  The inspected generator nevertheless also satisfies the requested
BFS procedure: it uses a FIFO `std::deque`, applies all 13 moves to every
dequeued state, and exits only after the queue is empty.  Its duplicate table
uses full-key equality.

## Checks performed

- I ran the snapshot-listed Python verifier with the mandated research Python.
  It independently checked graph6 decoding, all 711,439 parent edges, all
  9,248,720 closure moves, and all 915,623,280 state/five-subset pairs, and
  returned `beta: 4`.
- I compiled and reran the snapshot-listed C++ generator into `/tmp`.  It
  processed and discovered exactly 711,440 states, drained the queue, and
  performed its own independent-five search.  The regenerated 10,671,616-byte
  certificate was byte-identical to the frozen artifact and had SHA-256
  `6ee96dec3a2e4c2dcbd4424366e3499b611024c5911b8f20c7d54dca1eb73d02`.
- I wrote a fresh verifier, `audit/referee_verify.cpp`, whose local complement
  toggles neighbor pairs directly rather than using the claimant's clique-mask
  implementation.  It separately parsed the certificate, checked graph6 and
  the Paley edge relation, full-key uniqueness, FIFO-compatible parent order,
  every tree edge, every closure move, every five-subset, and the four-set
  witness.  It returned PASS with the same exact counts.  The durable command
  and result record is `audit/referee_verification.txt`.

These checks cover degenerate local complements (degree zero or one gives the
same state), fixed vertex labels, all generators, the root/empty sequence,
serialization range, and the quantifier over every five-subset.  There are no
division, limiting, compactness, or equality-case assumptions in the argument.

## Source comparison and limitations

The frozen source reports that Bae's arXiv:2604.13434v1 proves
\(R_{\rm vm}(5)\ge 13\), leaves the relevant case unresolved, and uses the
convention under which this witness gives \(R_{\rm vm}(5)\ge14\).  The
snapshot-listed dated literature/registry check reports no explicit 13-vertex
witness in its targeted primary-source, title, notation, code, and local-registry
searches.  That search is expressly non-exhaustive and cannot prove priority.
Accordingly, the safe contribution claim is the exact resolution of the frozen
existence question and its stated lower-bound consequence, not a claim of first
discovery or exhaustive literature coverage.

No mathematical gap remains in the frozen candidate scope.  The certificate
proves an affirmative instance, so no classification of all 13-vertex graphs is
needed.  The submission is not a partial result silently promoted to a full
resolution.

## Verdict

**Accept.**  Scope, exact correctness/evidence, and contribution all pass for a
`resolution-paper`; the original frozen assertion is **proved** by the explicit
13-vertex witness.
