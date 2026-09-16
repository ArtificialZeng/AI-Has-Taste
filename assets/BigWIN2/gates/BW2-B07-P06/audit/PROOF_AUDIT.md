# Proof audit

Status: **PASS for the claims in `paper/main.tex`; FAIL for a full resolution
of Conjecture 9.1/63.**  The manuscript explicitly presents a partial theorem
and leaves the unrestricted conjecture open.

Audit date: 2026-08-30.

## Degree transform

- Reconstructed from Stanley's all-subsets formula independently of the
  Builder derivation.
- Checked the double count over isolated vertices and the sign
  \((-1)^{n-b}\).
- Checked cycle vertices, off-cycle vertices, the full-cycle correction,
  the cancellation of the constant kernel term, and the separate \(b=n\)
  endpoint.
- Exact integer tests compare the power-sum transform with the claimed
  graph polynomial on 14 boundary examples.
- Exhaustive exact regression passed on every connected unicyclic graph of
  orders 3 through 10 (1,040 isomorphism classes).

## Divisibility and structural theorem

- Equality of cycle length is imported only from the cited source.
- The factors at \(z=0\) and \(z=1\) were checked separately; equal leaves
  supply the second factor of \(z\), not an extra factor at \(z=1\).
- The maximum-degree implication uses only degree comparison with the divisor.
- The range \(n\le2c-1\) uses the published hook dichotomy, feasibility of
  \(r=c\), the identity \(k=n-L\), and \(\Delta\le n-c+2\).
- At \(n=2c\), the ordinary branch was checked separately for \(c=4\) and
  \(c\ge5\).  The exceptional branch was classified; its actual degree
  difference agrees with the required finite difference only at \(c=3\),
  which is outside the theorem.
- The theorem makes no assertion for the general \(n>2c\) quotient.

## Edge transform

- The first proposed formula failed on a cycle.  That formula is not used.
- A from-definitions reconstruction gives the forest factor
  \((1+x)(-x)^M\), hence \(z^d(1-z)\), and the full-cycle correction
  \(-z^d(1-z)^c\).
- The top coefficient \(b=n\), cycle edges, root edges, and edges entirely
  off the cycle were checked.
- Exact integer tests passed on 20 examples and exhaustively on the same
  1,040 small-order graphs.
- The arbitrary-girth equal-CSF family at \(c=4,5\) passes both transforms
  and two full integer CSF implementations.

## Computational proposition

- Equal CSFs must agree at every exact modular specialization; only this
  necessary direction is used.
- At order 17 all 880,840 primary signatures are distinct.
- At order 18 the one full evaluation-signature match has the same structural
  triple.  The paper does not claim this pair has equal CSF.
- The candidate logic was checked for multi-record buckets: a first
  different-data record with the same refined signature is always emitted.

## Remaining fatal gaps for the original problem

1. A nonzero quotient can remain in the degree divisibility relation when
   degrees exceed the cycle length.
2. The exceptional \(r=1\) versus \(r=c\) hook branch is unresolved for
   general \(n>2c\).
3. Absence of a counterexample through order 18 is finite evidence only.

These gaps are disclosed in the abstract, introduction, and final section.
