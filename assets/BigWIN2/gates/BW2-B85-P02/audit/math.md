# Fresh mathematical referee report

## Reviewed scope and integrity

I reviewed the exact `resolution-paper` claim frozen by snapshot
`5bae88dfd167abf34d7f9b6441aec165a07bb2053cafb251320da605716a69b9`:
under the definition in `source.md`, `s_1(4)=9`, with
`(1,1,1,2,2,2,10,13)` as a length-eight obstruction.  I did not replace this
with a weaker statement.

I recomputed the SHA-256 digest of every file named in the snapshot.  Every
file hash equals its recorded value, and hashing the canonical sorted compact
JSON serialization of the snapshot's `files` mapping reproduces the displayed
snapshot digest.  In particular, `source.md` still has SHA-256
`8dea57f4ed625562f4d0ff3d6ee46d2ad0a89dd86bfbc37f472166aead93d5f9`.

## Reconstruction of the decisive argument

An integer not divisible by 4 has, modulo 16, one of the twelve residues

`A={1,2,3,5,6,7,9,10,11,13,14,15}`.

Both the hypothesis and the conclusion depend only on these residues.  A sum
which is divisible by 4 but not by 16 has residue exactly in
`T={4,8,12}` modulo 16.  Thus reduction of arbitrary (including negative)
integers modulo 16 loses no information.

Permuting the nine positions does not change whether four distinct positions
work.  Each permutation orbit is represented uniquely by a vector of twelve
nonnegative multiplicities summing to 9.  Conversely, every such vector is a
valid residue multiset and expands to an ordered sequence.  Hence the complete
domain has

`C(9+12-1,12-1)=C(20,9)=167,960`

states.  Selecting distinct positions is exactly the requirement that the
selected count in each residue class not exceed that class's multiplicity;
repeated values are therefore retained correctly.

For the candidate's multiplicity-DP verifier, after the first `i` residue
classes the degree-`j` bit mask is precisely the set of residues obtainable by
selecting `j` available positions from those classes.  The update takes every
integer `q` from 0 through the smaller of the available multiplicity and the
remaining degree, then rotates the previous mask by `q*r` modulo 16.  Induction
on the processed classes proves this invariant.  Truncating degrees above four
cannot affect degree four because all degrees are nonnegative.  Thus the final
mask tests the required predicate exactly, with no floating-point arithmetic.
The weak-composition recursion chooses the first eleven coordinates and forces
the twelfth, giving one and only one path for each state.

I replayed both frozen programs.  Each exited successfully and reproduced its
recorded results.  The multiplicity-DP program tested 167,960 size-nine states,
found zero avoiders, and reproduced state/signature digest
`e1ea938b23ab49e04666a0495e15fceda29df1c204bacfeb8b4122c8943eba35`.
The direct position-quadruple program independently tested 167,960 sorted
multisets, found zero avoiders, and reproduced domain/outcome digest
`63d4154ad6439c6e92cd1af693f522ae3fc48cca7ea695b916f33538263cb7b4`.

I also wrote and ran `audit/referee_exact_check.py`, a third formulation which
imports neither frozen checker.  It generates multiplicity vectors through a
stars-and-bars separator bijection.  Separately, it generates all 274
four-term residue-multiplicity patterns summing to a member of `T`; an ordered
four-tuple enumeration verifies that pattern set.  A nine-term state works if
and only if it componentwise dominates one of those patterns.  This verifier
again tested exactly 167,960 size-nine states and found zero avoiders.  At
length eight it tested `C(19,8)=75,582` states and found 160 avoiders, agreeing
with both frozen implementations.  Its source and recorded output are in
`audit/referee_exact_check.py` and `audit/referee_exact_check.report.json`.

For the asserted lower-bound witness, all entries are allowed.  If `a,b,c,d`
copies of `1,2,10,13` are selected, respectively, then
`a+b+c+d=4`, `a,b<=3`, `c,d<=1`, and the sum is

`4+b+9c+12d (mod 16)`.

For `(c,d)=(0,0),(1,0),(0,1),(1,1)`, the exact attainable sets are respectively
`{5,6,7}`, `{13,14,15,0}`, `{0,1,2,3}`, and `{9,10,11}`.  Their union omits
`4,8,12`.  I additionally enumerated all `C(8,4)=70` four-position selections
and obtained the same support.  Thus the defining property fails at length
eight.  Monotonicity of the universal property then rules out every smaller
threshold, so `s_1(4)>=9`; the exhaustive size-nine result gives `s_1(4)<=9`.
Consequently `s_1(4)=9` in the full frozen scope.

## Scope, source comparison, and attacks

The quantifiers, exact selection length, position distinctness, repeated
values, negative inputs, and the three allowed target residues all survive the
finite reduction.  There is no division, limiting argument, compactness step,
or imported lemma.  The coverage counts are proved by explicit bijections and
checked against the corresponding binomial coefficients.  The lower bound
does not rely on a citation.

The frozen literature records identify Sun's arXiv:2606.18234v5 as defining
the same exactly-`n` invariant, proving only `9 <= s_1(4) <= 13`, and
conjecturing the value 9.  They distinguish the later Gao--Jiang--Mu invariants,
which allow a nonempty subsequence or one of length at most `n`, from the exact
four-term condition here.  Two bounded same-day primary-source searches found
no equivalent exact-case resolution.  This supports the claimed delta from
the nearest cited result, while the candidate correctly avoids claiming a
guarantee of priority.  Resolving the original `n=4` case is neither a toy
restriction substituted for the problem nor a routine corollary of the cited
bounds.

I found no unresolved mathematical gap in the frozen claim.  The new audit
verifier is corroboration rather than a change of statement or decisive frozen
evidence.

## Verdict

**ACCEPT.**  The frozen resolution claim has the correct full scope, its exact
finite proof is reproducible and independently reconstructed, the sharpness
witness is valid, and the stated contribution and literature limitations are
honest.
