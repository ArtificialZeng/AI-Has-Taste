# Breaker notes

The breaker attacked the finite conclusion as follows.

- Replaced discovery's letter-layer enumeration by shape-first row-major
  filling; all counts still agree.
- Replaced row-bitset tableau encoding by a cellwise 80-bit encoding.
- Replaced bitset-row insertion by explicit-grid insertion and checked the two
  published hand examples 2.8 and 2.9.
- Generated the 148 primitive rules generically instead of using discovery's
  hard-coded loops.
- Replaced pairwise recursive interval enumeration by the independent identity
  \((\uparrow S)\cap(\downarrow S)\setminus S=\varnothing\).
- Rebuilt every endpoint \(n=0,\ldots,8\), including the empty tableau and
  degenerate singleton intervals.
- Required exact equality of the \(n=8\) primitive-test, closure-test, and merge
  counts.
- Submitted five malformed/tampered certificate variants; all were rejected.
  An intact control certificate was accepted.

No counterexample survived these tests. The breaker notes that both programs
use the published Algorithm 1, as they must to certify the same relation; the
independence is in state generation, representation, insertion evaluation, and
interval evaluation.
