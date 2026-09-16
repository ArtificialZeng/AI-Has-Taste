# Fresh mathematical referee report

Referee job: `win-00085-p01-referee-927423d0d0c2`  
Frozen snapshot: `ccc843aad5d52beb01f8b3bade403cf06f1d1580cfe2176e9c28de1681a70d5c`

## Scope reviewed

The frozen candidate is a `resolution-paper` asserting the negations of both
existential statements in `source.md`: product-local-unitary-plus-permutation
equivalence fails for $Q(S_A),Q(S_B)$ and separately for
$Q(S_+),Q(S_-)$.  I reviewed that exact scope; I did not replace it by a
claim about generator lists, local Clifford operations, monomial maps, or a
subclass of one-qubit unitaries.

All nine hashes in `audit/snapshot.json` were recomputed before review and
matched.  In particular, the immutable source retained SHA-256
`8bdbd0fa48aea26f73f732eaeb115a15243603a548dc4dabaca4647bf1af6990`.

## Reconstruction of the decisive argument

Let $S$ be any of the four stabilizer groups and let $n$ be its number of
qubits.  The three displayed generators commute and are independent as binary
Pauli labels.  Thus $|S|=8$, $-I\notin S$, and the orthogonal projector onto
the common $+1$ space is

\[
P_S=\frac1{8}\sum_{g\in S}g.
\]

Since $\operatorname{rank}P_S=2^{n-3}$, its trace-one normalization is

\[
\rho_S=2^{-n}\sum_{g\in S}g.
\]

For a coordinate set $A\subseteq[n]$, every Pauli term nontrivial on a
traced-out coordinate has zero partial trace.  Each term supported within
$A$ instead acquires the factor $2^{n-|A|}$.  Hence

\[
\operatorname{Tr}_{A^c}\rho_S
=2^{-|A|}\sum_{\substack{g\in S\\
\operatorname{supp}(g)\subseteq A}}g|_A.
\]

The terms in this sum form a stabilizer subgroup $H_A$ of order
$2^{d_S(A)}$.  Its group average is a projector of rank
$2^{|A|-d_S(A)}$.  Multiplying it by a nonzero scalar does not change rank,
so

\[
\operatorname{rank}(\operatorname{Tr}_{A^c}\rho_S)
=2^{|A|-d_S(A)}. \tag{1}
\]

This derivation handles the signed Pauli products: subgroup averaging uses the
actual Hermitian operators, not unsigned words.

Now suppose a product unitary and permutation mapped one frozen code subspace
onto the other.  Their normalized projectors would be related by conjugation.
After relabelling $A$ by the same permutation, partial trace cancels the
unitaries on $A^c$ and conjugates the reduced operator by the product unitary
on $A$.  Therefore its rank is unchanged.  A necessary condition for the
claimed equivalence is consequently that one coordinate permutation identify
the entire indexed rank profile (1).

For the five-qubit pair, direct multiplication gives precisely two
three-coordinate sets of marginal rank $4$:

\[
S_A:\ \{1,2,5\},\{3,4,5\},\qquad
S_B:\ \{1,3,4\},\{2,3,4\}.
\]

The two sets intersect in one coordinate on the left and two coordinates on
the right.  Coordinate permutations preserve intersection cardinality, so no
permutation can identify these rank profiles.  Thus $E_5$ is false.

For the six-qubit pair, the rank histograms over all fifteen four-coordinate
sets are

\[
S_+:\ \{8:3,16:12\},\qquad
S_-:\ \{4:1,16:14\}.
\]

Even the unlabelled histograms differ, and a permutation cannot change either
histogram.  Thus $E_6$ is false.

These are obstructions for arbitrary one-qubit unitaries, not only Clifford
unitaries.  They concern equality of code subspaces through their uniquely
defined projectors.  Rank-profile agreement would only be necessary, but the
strict mismatch used here is sufficient for non-equivalence.

## Checks actually performed

- I replayed `evidence/research_projector_audit.py`.  It exited successfully
  with `AUDIT_OK` after constructing the four signed dense Pauli sums over
  exact Gaussian integers, checking $R^2=8R$, and directly tracing and
  exactly ranking all 192 code/subsystem pairs.
- I replayed `evidence/triage_exact_check.py`; it independently returned zero
  coordinating permutations and the same two small certificates.
- I wrote and ran `audit/referee_exact_check.py` (SHA-256
  `ea2561a46aed245141d7230864d0ec493d9f6e4dc37a11abcd518a4c34a828b4`).
  This fresh binary-label implementation rebuilt every group and every
  $d_S(A)$, exhausted all $5!$ and $6!$ coordinate permutations, and
  ended in `REFEREE_CHECK_OK`.  It does not establish signs by itself; that is
  why the signed dense-projector replay above was also required.
- I independently checked the decisive support data by hand from the complete
  signed tables.  For $S_+$, the only weight-four supports are $1256$,
  $3456$, and $1234$, each contributing a one-dimensional supported
  subgroup.  For $S_-$, three distinct nonidentity elements have support
  $1234$, producing a subgroup of order four there; its other nonidentity
  elements have weight five.  This gives the two six-qubit histograms without
  relying on permutation exhaustion.
- I checked the live primary arXiv records.  Mahmoud's v1 displays exactly the
  four frozen triples in Theorem 5.3(ii),(iii) and asks exactly the two
  product-unitary-plus-permutation questions in Question 5.4:
  <https://arxiv.org/html/2607.26214v1>.  The record still showed only v1.
  Van den Nest--Dehaene--De Moor equation (14) identifies the supported binary
  stabilizer-subspace dimensions as degree-two local-unitary invariants:
  <https://arxiv.org/html/quant-ph/0404106v2>.  The candidate correctly treats
  this invariant as prior art.  Fresh exact-string searches found no separate
  primary resolution; this is only a bounded literature screen, not a priority
  proof.

## Edge cases and gaps

The empty and full subsystems, generator phases, generator independence, code
dimensions, and both permutation conventions were checked.  There is no
division by a possibly zero quantity, limiting argument, compactness claim, or
unstated Clifford restriction.  The two existential assertions are refuted
separately.  Mahmoud's broader LU--LC-style question remains unresolved, as the
candidate explicitly says.

I find no mathematical gap in the frozen scope.  The bounded literature search
cannot establish priority, but the candidate makes no priority claim and
carefully attributes the general invariant.  Resolving both concrete open
instances by explicit exact incidence certificates is a nontrivial and useful
full-scope contribution.

## Verdict

**ACCEPT.**  The frozen argument correctly disproves both $E_5$ and $E_6$,
matches the original problem without weakening, and states an honest
contribution relative to the cited prior invariant.
