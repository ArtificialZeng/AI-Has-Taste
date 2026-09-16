# Fresh mathematical referee report

## Frozen scope and integrity

I reviewed the `resolution-paper` claim frozen by snapshot digest
`ad2f266c7970465782973c8017af141444778465ff0a729aaefe20efddca0329`.
Before reviewing the argument, I recomputed SHA-256 hashes for `claim.json` and
every listed evidence file; all matched `audit/snapshot.json`.  The submitted
claim proves the original assertion for every odd length `m=2k+1 >= 3` and
also asserts the stronger conclusion for every integer `m >= 2`.  Thus the
candidate has not replaced the original quantifier by a finite test or a
weaker family.

## Reconstruction of the decisive proof

For an integer `q >= 3`, a proper coloring of the three vertices in the last
column has exactly one of two equality types: `A=(a,b,a)`, with `a != b`, or
`B=(a,b,c)`, with all three colors distinct.  Consequently the first-column
row vector is

\[
v_1=(q(q-1),q(q-1)(q-2)).
\]

Fixing representatives `(0,1,0)` and `(0,1,2)` for the old types, I recounted
the extensions to a new column.  The resulting old-type-by-new-type matrix is

\[
M(q)=\begin{pmatrix}
q^2-3q+3 &(q-2)(q^2-4q+5)\\
q^2-4q+5&q^3-6q^2+14q-13
\end{pmatrix}.
\]

For a new `A` column `(x,y,x)`, the two entries follow by separating `x=1`
from the other allowed endpoint colors.  For `A -> B`, separating `y=0` from
`y` different from both old colors gives
`(q-1)(q-2)+(q-2)^2(q-3)`.  For `B -> B`, inclusion-exclusion on the forbidden
horizontal equalities in an ordered distinct triple gives

\[
q(q-1)(q-2)-3(q-1)(q-2)+3(q-2)-1.
\]

These calculations agree with all four displayed entries.  Symmetry makes
the extension count depend only on the old type, so
`v_{m+1}=v_m M(q)` and the sum of the two coordinates is the chromatic
polynomial.  The identities hold for infinitely many integers `q >= 3` and
therefore are polynomial identities; specialization to `q=-1` is legitimate
and does not treat a negative number as a literal color count.

At `q=-1`,

\[
M(-1)\equiv\begin{pmatrix}3&2\\2&2\end{pmatrix}\pmod4,
\qquad v_1(-1)\equiv(2,2)\pmod4.
\]

The next state is `(2,0)` modulo four, and
`(2,0)M(-1)=(2,0)` modulo four.  Induction therefore gives

\[
\chi_{P_3\square P_m}(-1)\equiv 2\pmod4
\quad\text{for every }m\ge 2.
\]

Stanley's evaluation
`psi(G)=(-1)^{|V(G)|} chi_G(-1)` changes at most the sign, and `-2` and `2`
have the same residue modulo four.  Hence
`psi(P_3 square P_m) = 2 (mod 4)` for every `m >= 2`, in particular at every
`m=2k+1` with `k >= 1`.  There is no division, limiting argument, or omitted
nonempty-domain condition.  The excluded case `m=1` has four acyclic
orientations and would not satisfy the conclusion, so the claimed lower
endpoint is both correct and necessary for the stronger statement.

## Checks actually performed

I reran `evidence/width3_transfer_certificate.py`.  Direct enumeration of
column transitions agreed with the four polynomials for each `q=3,...,12`;
the two-state transfer polynomial agreed with the full FK connectivity
calculation for each `m=1,...,9`; and the modulo-four fixed-orbit assertion
passed.

I separately reran both exact `m=9` programs and byte-compared their standard
output with the frozen output files.  There was no difference.  The
deletion-contraction program and the FK chromatic-polynomial program both give

\[
\psi(P_3\square P_9)=514302841174\equiv2\pmod4.
\]

As an additional check not using either counting recurrence, I exhaustively
enumerated all edge orientations and tested acyclicity by topological sorting
for `m=1,2,3`.  This gave respectively `4`, `98`, and `2398`, agreeing with
the transfer certificate.  These finite computations corroborate but are not
used to turn the finite orbit into the proof; the polynomial identity and
fixed-state induction establish the universal statement.

## Source comparison and contribution

Within the frozen source record, Muehlherr--Poullot's 2026 paper reports only
the finite width-three cases `m=3,5,7` as experiments and states the containing
odd-by-odd assertion as Conjecture 1(1).  The candidate supplies an all-length
width-three proof and hence settles the frozen subfamily, rather than merely
deriving its non-Hamiltonicity consequence.  The problem record also identifies
Salas--Sokal transfer-matrix work as a technical antecedent but does not claim
that its inspected material contains this modulo-four theorem.  The candidate
appropriately limits its resolution claim to the cited-source comparison and
does not assert an audited global priority claim.  Resolving the complete
width-three subfamily of the stated conjecture, with a short exact invariant,
is a substantive contribution at the frozen `resolution-paper` scope.

## Verdict

**Accept.**  The two-state classification is exhaustive, every transition is
correct, the polynomial specialization is justified, and the fixed residue
proves the original claim in full scope (indeed, the submitted stronger
`m >= 2` statement).  I found no unresolved mathematical gap requiring a
claim revision.
