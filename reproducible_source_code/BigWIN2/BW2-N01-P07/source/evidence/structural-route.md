# Triage derivation for the next proof attempt

Job: newwin-00001-p07-triage-19444324da60; 2026-09-12.
This is a preliminary mathematical argument, not an independently reviewed
resolution or a manuscript. Its role is to justify advancing the exact target.

Take the composition encoding in problem.md and set \(q_d=\epsilon_d^3\).
Since \(\epsilon_d(i)=1+(i\bmod d)\), direct calculation gives
\[
q_d(i)=1+((i-1+3)\bmod d),\qquad 1\leq i\leq d.
\]
Thus \(q_1=1\), \(q_2=21\), \(q_3=123\), and
\(q_d=(4,5,\ldots,d,1,2,3)\) for \(d\geq4\).
The identities occur exactly at \(d\in\{1,3\}\). Every other block consists
of two increasing runs and has one descent; every subsequence therefore
has at most one descent. In particular, a single block avoids 2143.
Powers preserve direct sums because each interval is invariant.

For any direct sum \(q=\bigoplus_i q_{d_i}\), an inversion has both
endpoints in one block: all entries of an earlier block are smaller than
all entries of a later block. An occurrence of 2143 at positions
\(a<b<c<e\) satisfies \(q(b)<q(a)<q(e)<q(c)\). Each of its inversion
pairs \((a,b)\) and \((c,e)\) must lie in a single block. If both pairs
lie in the same block, that block contains 2143, already excluded.
Otherwise two distinct nonidentity blocks are required. Conversely, choose
an inversion from each of two nonidentity blocks in their block order.
The direct-sum inequalities make those four entries an occurrence of 2143.

This suggests precisely the desired criterion, with no restriction on
where the exceptional part occurs. The argument extends to the empty sum.
For a fully self-contained proof, verify the composition bijection's inverse:
the position of the minimum forces the first block to be
\((2,3,\ldots,d,1)\), then recurse on the standardized suffix.
Uniqueness is essential; the lengths of blocks in the cube alone cannot
recover parts of size 1 versus 3.

The enumeration step has no additional pattern analysis:
\(A(z)=1/(1-z-z^3)\) counts ordinary parts, and
\(E(z)=z^2+z^4/(1-z)\) counts exceptional parts. The zero-exception and
one-exception cases have series \(A(z)\) and \(A(z)E(z)A(z)\).

Finite cross-check: evidence/triage_check.py directly composes permutations
three times and tests all 4-subsequences, without using the above
cross-block criterion in the avoidance detector. All 4096 compositions
of sizes 0 through 12 pass; all 46234 permutations of sizes 0 through 8
verify the encoding's image independently. Single blocks of sizes 1
through 40 also pass. This is finite evidence only.

Next decisive test: turn this route into a complete all-n equivalence,
checking the inverse decomposition and the same-block/two-block inversion
cases explicitly. If valid, the restricted bijection and formal series
resolve the frozen assertion; an independent referee is still required
before any resolution candidate can be accepted.
