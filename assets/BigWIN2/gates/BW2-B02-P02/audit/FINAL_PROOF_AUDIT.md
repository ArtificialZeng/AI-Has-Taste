# Terminal referee reconstruction

Date: 2026-08-29.  Scope: only the locked proposition in
`problem/formal_statement.md`, SHA-256
`83f619b909485fb9fb34eacd44c311336106003b147845ce74997236271472aa`.

## Verdict

**PASS.**  The proof in `proof/tree_conjugacy_proof.md` establishes the full
quantified statement and the least-positive-period requirement.  I found no
open mathematical dependency, hidden quotient, or numerical extrapolation.
The proof uses no proof assistant.

This terminal review was run serially from the locked rule and definitions.  I
used the earlier Builder and Breaker files only after reconstructing the
dependencies below, to compare conclusions and locate convention-sensitive
cases.

## 1. Rule, phase, and full-grid reduction

The integer rule 115 gives, in Wolfram order,
`0,1,1,1,0,0,1,1`, and hence

\[
\delta(\ell,x,r)=1+x+\ell x+\ell xr.
\]

For the all-zero initial pair the current layer is
\(\beta_t=1\) exactly at \(t\equiv1\pmod3\).  Therefore a background site
symbol \(2\beta_{t-1}+\beta_t\) cycles as \(0,1,2\).

Let \(a=-k\), \(b=k\), and \(e_t=d^t_{a-1}\).  The right receiver
\(b+1\) remains background because
\(\delta(s,0,0)=1\) and \(\delta(s,1,1)=0\), independent of the interior bit
\(s\).  On the left, simultaneous induction gives

\[
e_{3q+1}=1,\qquad e_{3q}=e_{3q-1}.
\]

Indeed, at phase zero the identity \(\delta(0,x,r)=1+x\) gives the first
formula; at phase two it gives the second formula at the next cycle.  The only
phase in which site \(a-2\) can depend on \(e_t\) is phase one, where
\(e_{3q+1}=1\) makes its neighborhood `111` and its rule output zero.
The other phases use \(\delta(0,0,r)=1\).  It follows for all times that

\[
d^t_j=\beta_t\quad(j>b\text{ or }j\le a-2).
\]

Thus the exact safe window is \(W_k=[-k-1,k]\).  Equality on the full lattice
is equivalent to equality of both layers on this window together with phase
zero.  The converse phase condition is forced by any site to the right of the
window, whose background pair is `(0,0)` only in phase zero.  This closes both
the boundary and hidden-quotient risks.

## 2. Four-symbol normalization and local toggle

For \(q=2d^{t-1}+d^t\), direct substitution gives

\[
g(L,X,R)=2(X\bmod2)+
 \bigl(\lfloor X/2\rfloor+\delta(L\bmod2,X\bmod2,R\bmod2)\bigr)\bmod2.
\]

Let \(\tau=(0\ 1\ 2)\), fixing 3.  I reconstructed the normalized map
\(h_p=\tau^{-(p+1)}g(\tau^pL,\tau^pX,\tau^pR)\) directly from the integer
115, without importing either tree implementation.  All
\(3\cdot4^3=192\) inputs agree with equation (7a): for
\((a_0,a_1,a_2)=(1,0,2)\), the only change is
\(X=a_p\leftrightarrow3\) when
\(L\in\{a_p,3\}\) and
\(R\in\{0,1,2\}\setminus\{a_p\}\).  There are exactly eight toggling inputs
in each phase and zero discrepancies.  This finite truth-table calculation
proves a local identity; it is not an all-parameter orbit search.

For an admissible padded word \(3^{N-|v|}v\), the condition occurs only at the
boundary of the leading run of 3s.  It deletes a leading \(a_p\), prepends
\(a_p\) when the result is admissible, and otherwise fixes the word.  The
empty, full-length, length-\(N-1\), terminal-zero, and ghost-cell cases match
the missing-edge convention.  Hence the one-step conjugacy is exact.

## 3. The reduced-word graph is a properly colored tree

Deleting the first letter of any nonempty admissible word preserves all
constraints, so every nonempty vertex has one shorter parent and repeated
deletion reaches the empty word.  Every nonloop colored edge changes the
length by one.  If a cycle existed, a maximal-length vertex on it would need
two shorter neighbors, contradicting uniqueness of its parent.  Thus the
graph is connected and acyclic.

For a fixed color, a valid prepend is reversed by deletion.  A forbidden
prepend is a fixed point.  Therefore every \(s_a\) is an involution and at
most one edge of any color meets a vertex; the edge coloring is proper.

## 4. The contour map is exactly one cycle

For a one-vertex tree the phase map is a 3-cycle.  Suppose a leaf \(u\), joined
to \(v\) by color \(a_p\), is removed.  In the smaller tree the transition
\((v,p)\to(v,p+1)\) uses a missing edge.  Restoring the leaf replaces only that
transition by

\[
(v,p)\to(u,p+1)\to(u,p+2)\to(u,p)\to(v,p+1).
\]

The two intermediate colors differ from the leaf-edge color because every
color occurs once per phase cycle, so those two moves stay at the leaf.
Exactly the three new phase states are spliced into the old cycle.  Leaf
induction therefore proves that the phase-tagged contour map is one cycle on
\(V_N\times\mathbb Z/3\mathbb Z\).  This proves the least period of every
encoded state is \(3|V_N|\), excluding every smaller positive return, not only
proper divisors of a proposed exponent.

The physical encoding is injective: the uniform exterior recovers the phase;
inverse phase rotation recovers the normalized word; deleting its unique
leading run of 3s recovers \(v\).  Hence the physical orbit is not a quotient
with a shorter period.

## 5. Count and target initial state

For lengths \(1\le m<N\), there are \(2^m\) admissible words ending nonzero.
For length \(N\), start-zero/end-nonzero words number

\[
A_N=\frac{2^N+2(-1)^N}{3}.
\]

Since \(N=2k+2\) is even,

\[
|V_N|=1+\sum_{m=1}^{N-1}2^m+A_N
      =\frac{2^{N+2}-1}{3}.
\]

For odd \(k\), the phase-zero symbol word on \([-k-1,k]\) starts with 0,
ends with 1, and has unequal adjacent letters.  The current bit at site zero
is 0 while the memory spike is 1, so the central symbol is 2; this preserves
the alternating inequality.  The word is therefore a full-length vertex of
\(V_N\).  The contour result gives

\[
P(k)=3|V_N|=2^{2k+4}-1.
\]

With \(k=2i+1\), this is exactly

\[
P(2i+1)=2^{4i+6}-1=4^{2i+3}-1\qquad(i\ge0).
\]

## 6. Independent checks and adversarial conventions

The final clean suite ran all 43 tests successfully.  The system image lacked
`gcc`, so the C test used the verified Zig 0.13 `zig cc` wrapper documented in
`audit/COMPILER_ENV_NOTE.md`.  The exact certificate verifier then passed,
independently checking the primary tree model through \(N=12\),
the separate Breaker model through \(N=14\), every normalized local input,
and dense/bit-packed first returns through \(k=7\).  A malformed certificate
failed closed with exit code 1.

The Breaker mutations give immediate witnesses against omitting missing-edge
loops, changing the generator order, or reversing phase rotation.  These
checks confirm that the conventions used by the proof are substantive.  None
of the finite checks is used to infer the quantified theorem.

## Final dependency classification

| Dependency | Referee status |
|---|---|
| locked source/formal statement | PASS |
| full-grid/window equivalence | PASS |
| normalized local toggle law | PASS |
| admissible-word tree and involutions | PASS |
| one-cycle contour lemma | PASS |
| vertex count | PASS |
| odd initial membership | PASS |
| exact least-positive return | PASS |
| computational independence/labeling | PASS |

There is no remaining fatal or major mathematical gap.  Novelty, citation,
manuscript metadata, and PDF presentation are separate publication gates and
are not certified by this proof verdict.
