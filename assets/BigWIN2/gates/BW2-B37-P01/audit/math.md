# Fresh mathematical referee report

**Verdict: accept.**  The frozen candidate proves the original conjecture in
its full stated scope, including the least-period requirement and the case
\(i=0\).  I found no unresolved mathematical gap in the submitted argument.

## Scope reconstructed

I reviewed snapshot
`a467f5dfaeb8788c8fc3c18449ef09ac3839f180d9cd3ae8e8b5c93785377564`.
All hashes of `claim.json` and the enumerated evidence files agree with
`audit/snapshot.json`.  The claim uses exactly the global map and centered
family fixed in `problem.md`, and asserts the displayed formula for every
integer \(i\geq0\).  It does not replace the least period by a return time or
exclude a small index.

Write \(H=F^3\), and encode each adjacent site pair \((2r-1,2r)\) as one
base-four block.  For family parameter \(k=2i\), the initial left factor is
the length-\(i\) word \((1,\ldots,1)\), while the initial right factor is the
length-\(i+1\) word \((3,1,\ldots,1)\).  These lie in the submitted path
languages \(L_i\) and \(R_i\), respectively (with the empty left word and
right word \((3)\) when \(i=0\)).

## Decisive argument

1. Three radius-one updates give a radius-two rule on the two-site blocks.
   The exhaustive transducer certificate checks the full \(16^5\) local truth
   table, all possible interior length-five and length-six path contexts, all
   padded boundary contexts (including every overlapping short case), and all
   interface contexts.  These checks establish for arbitrary lengths that
   \(L_i\) and \(R_i\) are invariant with zero spill and that
   \(H(lr)=H(l)H(r)\).  Locality makes the finite context coverage exhaustive,
   rather than a bounded-length extrapolation.  Since
   \(F(b,c)=(c,d)\) has the inverse reconstruction
   \(b_j=d_j\mathbin\oplus\delta_{115}(c_{j-1},c_j,c_{j+1})\), each finite
   invariant factor map is a permutation.

2. With \(M\) the displayed generic-path adjacency matrix and \(e\) the
   terminal-set indicator, direct row substitution gives
   \((M^2-5M+4I)e=0\).  The resulting recurrence, with initial values
   \(5,21\) on the left and \(9,41\) on the right, yields
   \[
   |L_i|=A_i=\frac{4^{i+1}-1}{3},\qquad
   |R_i|=B_i=\frac{2\,4^{i+1}-5}{3}.
   \]
   The \(i=0\) languages both have size one.

3. The ordered lists \(O_t\) in `colex_successor_proof.md` are exactly the
   possible generic predecessors of \(t\), with \(O_0\) the terminal set in
   its chosen order.  The left and right base lists are exactly their allowed
   initial blocks.  Thus the recursive lists \(E_m^X(t)\) enumerate every
   admissible path exactly once.

4. The colex certificate summarizes every aligned adjacent-list pair by all
   factors of length at most five and its length-five boundary segments.  Its
   recurrence is exact: within a top-level group it appends the common final
   symbol to the preceding summary, and between consecutive groups it uses
   the recorded last/first pair.  Those data also determine the next extrema.
   For block radius two, the summary contains precisely all records needed to
   check the image at every interior site, both boundaries, and all four spill
   blocks.  The cyclic last-to-first relation is included.  The entire summary
   state repeats at left lengths 7 and 8 and at right lengths 8 and 9.  Since
   the update is deterministic and these lengths exceed the five-block window,
   the verified transition persists by induction at every later length.
   Therefore \(H\) is the cyclic successor on each complete list, so its least
   factor periods are exactly \(A_i\) and \(B_i\), not merely divisors or
   observed return times.

5. Because \(B_i=2A_i-1\), \(\gcd(A_i,B_i)=1\).  Exact factor independence
   therefore gives least sampled period \(A_iB_i\).  Far outside the finite
   defect, the uniform state follows the genuine three-cycle
   \((0,0)\to(0,1)\to(1,0)\to(0,0)\), so the original configuration cannot
   return at a time not divisible by three.  Consequently
   \[
   P(2i)=3A_iB_i
   =\frac{2\,4^{2i+2}-7\,4^{i+1}+5}{3}.
   \]
   At \(i=0\), this gives and directly realizes the least period \(3\).

## Checks actually performed

- Recomputed every snapshot file hash and obtained exact agreement.
- Reran all four supplied Python programs with exact integer operations.  The
  direct orbit tests, 1,048,576-row local truth table, invariance/interface
  checks, and both all-length summary certificates all passed; the transducer
  digest was
  `8daa099568b0ddd2641c338c7e006173826db9c18662d0f8330138b6be80f0d2`.
- Independently implemented rule 115 and three global updates without calling
  the submitted local-rule function.  I reconstructed the recursive ordered
  languages and checked every cyclic successor transition directly through
  left length 7 (21,845 words) and right length 8 (43,689 words), exactly the
  first members of the two certified stabilization pairs.  All checks passed.
- Independently checked the predecessor sets, the matrix identity
  \((M^2-5M+4I)e=0\), its four initial counts, the coprimality calculation,
  the formula expansion, the background three-cycle, and the \(i=0\) case.

## Source comparison and limits

The authorized frozen source record identifies Formenti--Kamilya Conjecture 3
as exactly this formula and records their nearest results as existence of the
period and divisibility by three.  The candidate supplies the missing
all-\(i\) equality and leastness argument, so it is a full resolution rather
than a subsidiary or toy-scope result.  Under the instruction to read only the
snapshot-listed evidence, I did not add an independent literature search or
inspect unlisted source files; accordingly this verdict certifies the frozen
mathematical claim and its stated source comparison, not an unrestricted
priority claim beyond that bounded record.

There is no mathematical revision needed.  The manuscript phase should retain
the exact finite-state induction details, the scope of the computer-assisted
certificate, and the leastness argument above.
