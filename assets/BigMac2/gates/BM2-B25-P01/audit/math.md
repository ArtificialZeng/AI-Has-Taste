# Fresh mathematical referee report

## Scope reviewed

I reviewed the frozen `resolution-paper` claim at snapshot digest
`aba5bfb150da45f4077b1be845ed62e60b4fd3cfad55d8fa54cdddb9f83e369e`.
The claim is exactly that no four-layer balanced directed Hamilton cycle exists
in \(\operatorname{Cay}(\mathbb Z_{12},\{1,2,3\})\), with balance interpreted
as in `problem.md`.  This is stronger than, and would therefore negatively
settle, the original request for such a cycle whose three developments contain
the three prescribed step-two arcs in distinct cycles.

## Reconstruction of the obstruction

For every pair \((j,s)\in\mathbb Z_4\times\{1,2,3\}\), balance selects one
tail from \(j,j+4,j+8\).  Writing that tail as \(j+4t_{j,s}\) gives one and
only one ternary digit for each of the twelve pairs.  Thus the candidate's
\(3^{12}=531441\) search domain is a bijective parameterization of all
balanced arc sets; it uses neither symmetry reduction nor sampling.

A directed Hamilton cycle must give every vertex one outgoing and one incoming
arc.  For a fixed layer \(j\), distinct outgoing tails force the three steps
\(1,2,3\) to choose the three tails \(j,j+4,j+8\) bijectively.  There are
therefore \((3!)^4=1296\) balanced selections satisfying the necessary
outdegree condition.  If their twelve heads are also distinct, the arcs are
the graph of a permutation of \(\mathbb Z_{12}\).  Such an arc set is a
Hamilton cycle exactly when this permutation has one cycle of length twelve.

The two frozen enumerators implement the complete ternary domain in different
orders.  I checked their tail and head predicates, their permutation-cycle
tests, and their handling of modular endpoints.  In particular, a full
twelve-bit head mask is equivalent to distinct heads because exactly twelve
arcs have been selected.  The orbit-from-zero test is sufficient for a
permutation, and the programs additionally serialize the complete cycle
decompositions of every degree survivor.

## Checks actually performed

I reran `evidence/crosscheck.py` with the required interpreter
`/Users/mac/4prove-or-disprove-math/.research-venv/bin/python`.  It completed
successfully and reproduced the frozen record: 531441 balanced selections,
1296 outdegree-one selections, 15 selections with both degrees one, and zero
Hamilton cycles.  The fifteen survivors split as twelve of cycle type
\(6+6\) and three of type \(4+8\); their canonical serialized SHA-256 was
`b36456535b5da51566823d0c7781e5d398dd6beb8a4f85ce21a347d181a6f77b`.

I also wrote and ran the fresh verifier `audit/referee_recompute.py`.  It does
not replay either \(3^{12}\) loop.  Instead it directly enumerates the
\(6^4=1296\) layerwise permutations assigning steps \(1,2,3\) to the three
tails in each layer, retains maps with twelve distinct heads, and decomposes
each resulting permutation from all components.  It independently returned
15 degree survivors, the same \(\{\text{4+8}:3,\text{6+6}:12\}\) histogram,
zero twelve-cycles, and the same complete-survivor digest.

All computations are finite exact-integer computations.  There is no
floating-point tolerance, probabilistic step, limiting argument, or omitted
degenerate case.  Allowed steps \(1,2,3\) are nonzero modulo 12, and the
finite domain is nonempty.  Decomposing every degree survivor also removes
any possible ambiguity from testing only the orbit of vertex zero.

## Scope and source comparison

The original frozen question asks for existence in the single case
\(q=4,r=3\), with an additional development-colour condition.  Since every
balanced candidate arc set has been covered and none is a Hamilton cycle, the
base object required by the original existential quantifiers does not exist;
the development-colour and deletion conditions cannot arise.  The claim does
not infer a result for any other \(r\), does not confuse failure of the cited
ABAB construction with this obstruction, and makes no literature-priority
claim.  Its mathematical conclusion depends only on the self-contained frozen
definitions and exact enumeration, not on an unverified external theorem.

## Gaps and verdict

I found no gap in the coverage, degree reduction, cycle criterion, or stated
scope.  The exact obstruction proves the frozen original existential claim
false.  Literature priority and all cases beyond \(q=4,r=3\) remain outside
the submitted claim.

**Verdict: accept.**
