# Proof audit

Audit date: 2026-08-29.  Status: **PASS for `NEW_STRICT_BOUND`**.

## Claim audited

No integer \(n\) in

\[
9{,}174{,}471{,}185{,}880{,}000{,}000<n\le
9{,}180{,}628{,}549{,}092{,}000{,}000
\]

satisfies the Erdős #647 prefix inequality.  The global existence question is
not audited as solved.

## Quantifiers and reductions

For fixed \(n\), substituting \(k=n-m\) gives the exact equivalence

\[
\max_{m<n}(m+\tau(m))\le n+2
\quad\Longleftrightarrow\quad
\tau(n-k)\le k+2\quad(1\le k<n).
\]

Thus one exact violating shift is enough to reject a candidate.  The imported
Hughes chain is used only to prove that a candidate in this very large interval
has \(n=2520N\) and \(N\bmod46189\) in the elementary 96-class survivor set;
the separate dependency audit records that boundary.

## Coverage audit

The verifier reconstructs the \(96\) residues from the twelve congruence forms
and verifies that the serialized rows are exactly

\[
\mathcal R\times\{0,\ldots,528\}.
\]

With

\[
A=2520\cdot46189\cdot529=61{,}573{,}632{,}120,
\qquad n=Au+2520(46189s+r),
\]

the offset is in \([0,A)\), so the representation is unique.  Enumerating
\(149000000\le u\le149100000\) includes the left partial layer immediately
above \(Au_0\); the extra \(u=u_1\), positive-offset cells only overcover the
right endpoint.  The endpoint identities are checked from serialized integers,
not trusted text.  The exact cell count is

\[
96\cdot529\cdot100001=5{,}078{,}450{,}784.
\]

## Arithmetic audit

For a tested shift \(F=n-k\), the C replay removes exact valuations of primes
at most \(100000\).  Writing the removed part as \(Q\) and the cofactor as
\(C=F/Q\), exact division gives \(\gcd(Q,C)=1\).  Therefore the accepted lower
bound is \(\tau(Q)\) if \(C=1\), and \(2\tau(Q)\) if \(C>1\).  A cell is killed
only when this lower bound is strictly greater than \(k+2\).

This accounts for `5,078,450,763` cells.  The remaining 21 records are not
silently accepted: Python reconstructs their coordinates and \(F\), verifies
each serialized prime by deterministic 64-bit Miller--Rabin, multiplies every
prime power back to \(F\), recomputes the divisor count, and checks the strict
killing inequality.  All are killed at \(k\in\{1,2,3,4,6\}\); unresolved count
is zero.

All endpoints and reconstructed values must fit the signed 64-bit range.  An
endpoint-overflow mutation is an explicit negative test.

## Adversarial software audit

The decisive verifier and test harness contain zero AST `Assert` nodes.  The
test harness loads the verifier by an absolute `__file__`-derived path and uses
explicit fail-closed exceptions.  Normal, `-O`, outside-project `-I`, and
outside-project `-O -I` tests have byte-identical PASS logs.  The same four
modes replay all cells and produce byte-identical canonical output
`19f8f31a1d037ddae404448ba13863f10607a23f24414b57628bf13b6ecc83c3`.
Negative tests cover hash corruption, a duplicate pair, endpoint mutation,
signed-64 overflow, deletion of a required field, a modified hard factor, and
inconsistent hard coordinates.  See `audit/GATE4_AUDIT.md`.

The main independent auditor additionally reported a complete outside-project
`python3 -O -I` replay against final verifier source hash
`b75c881a95a8e0bf304f0117a3ae9c4804a0d330c456ea3440bb0ab4e4c7b43c`.

## Surviving limitations

1. The all-candidate modular implication is imported from a fixed Lean source;
   Lean was not invoked locally.
2. The earlier prefix through the left endpoint is audited as an external
   reported computation but was not fully rerun.
3. No finite endpoint controls the infinite tail.  Fatal global gaps G01 and
   G02 remain open.

These limitations preclude `PROVED` or `DISPROVED` and are compatible only
with the claimed terminal state `NEW_STRICT_BOUND`.
