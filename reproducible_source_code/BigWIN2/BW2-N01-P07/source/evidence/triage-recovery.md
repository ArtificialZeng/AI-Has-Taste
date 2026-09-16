# Bounded triage recovery

Job: `newwin-00001-p07-triage-47782f07ff79`; 2026-09-12.
Purpose: check the surviving structural route and decide admission, without
claiming mathematical acceptance or creating a manuscript.

## Inverse decomposition checked explicitly

Let a nonempty permutation avoiding 312 and 321 have its minimum at position
\(d\). For \(i<d<j\), an inequality \(\pi_i>\pi_j\) would make
\((\pi_i,1,\pi_j)\) a 312. Hence every entry before the minimum is smaller
than every entry after it. The first \(d\) entries therefore have value set
\([d]\). Two decreasing entries before the minimum would form a 321 with
the minimum. Consequently the prefix is exactly \((2,3,\ldots,d,1)\).
Subtracting \(d\) from the suffix gives another permutation in the same
avoidance class, so this operation recursively determines the composition
uniquely, ending at the empty permutation.

Conversely, in a cyclic block \(\epsilon_d=(2,\ldots,d,1)\), an entry
has at most one smaller entry to its right. In a direct sum, entries to
the right in later blocks are larger. Thus no entry has two smaller
entries to its right, which excludes both 312 and 321. This checks both
directions of the known composition encoding, including uniqueness and
the empty object. The inverse uses the original permutation, not its cube:
the cube cannot distinguish a part 3 from three parts 1.

## Two-inversion criterion checked

Powers preserve each direct-sum interval. On one block,
\(q_d(i)=\epsilon_d^3(i)=1+((i-1+3)\bmod d)\).
Thus \(q_1=1\), \(q_2=21\), \(q_3=123\), and
\(q_d=(4,5,\ldots,d,1,2,3)\) for \(d\ge4\).
Only sizes 1 and 3 give identity blocks. Each other block is a
concatenation of two increasing runs. Any subsequence takes entries from
the first run followed by entries from the second and has at most one
descent; hence it cannot have relative order 2143, which has two descents.

In a direct sum every inversion lies in one block. An occurrence of 2143
at positions \(a<b<c<e\) has inversions \((a,b)\) and \((c,e)\).
The inversion pairs cannot lie in the same block, since then that single
block would contain 2143. Thus they require two nonidentity blocks.
Conversely, inversions \((a,b)\), \((c,e)\) chosen from two blocks in
their block order obey
\(q(b)<q(a)<q(e)<q(c)\), giving an actual 2143 occurrence. Singleton
blocks between them cannot affect these inequalities. This supplies the
proposed exact equivalence with at most one part outside \(\{1,3\}\).

These elementary arguments support admission of the full original target.
They are triage mathematics, not an independent referee's acceptance.
The ensuing generating series is obtained from sequences of ordinary
parts with series \(A=1/(1-z-z^3)\), and either zero exceptional parts
or one exceptional part with series \(E=z^2+z^4/(1-z)\): \(A+AEA\).

## Evidence status

The prior `triage_check.py` and JSON were read. Their source/script hashes
and reported coverage totals are checked by `recovery_check.py`; the old
enumeration is not repeated as an unfinished task. Its surviving observation
covers 4096 compositions through size 12, 46234 permutations through size 8,
and individual block sizes 1 through 40.

The new script independently computes patterns by relative ranks and tests
the minimum-position inverse on all eligible permutations through size 8.
It also composes the permutation three times directly. Its exact run result
is in `recovery_check.json`: 46234 permutations examined, 256 eligible
inverse round trips, no counterexample, and counts
\(1,1,2,4,7,13,23,39,66\) for sizes 0 through 8. The run completed with
exit code zero. Finite coverage cannot prove the all-n claim.

No `literature/*handoff*.md` files were present. The recovery guidance in
`checkpoint.md` was treated as a lead, and its formerly pending finite test
was replaced by checking the inverse and structural argument above.

Next test: audit the complete restricted bijection for arbitrary block lists,
including both inverse identities and empty/singleton cases, and assemble
the all-n equivalence and formal generating series into a frozen resolution
candidate for subsequent independent review.
