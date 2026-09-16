# Verification and exact computation scope

Job: primary-20260913-subtree-annulus-research-bac30ce160a8.
Date: 2026-09-13 +08. Researcher verification; no fresh referee has run.

The assigned next test is complete. The following statements were checked
against the argument itself, rather than accepted from the checkpoint.

1. The four-way partition of connected vertex sets gives
   Q=q+(1+z)^a+(1+z)^b+z(1+z)^q for every a,b>=1. Its degree is q+1,
   leading coefficient one, and constant coefficient q+2.
2. On the outer circle, t=|1+z| belongs to [c,c+1] and
   |z|^2=2c^2+2c+1-t^2>=c^2>0. There is no branch or denominator exception.
3. Convexity in a gives t^a+t^b<=t+t^(q-1), including the degenerate
   one-point interval at q=2. Each required f_k is convex for k>=1.
   Endpoint comparison is valid because the exact ratio is
   (c/(c+1))^(k-1), never a negative exponent in this application.
4. Substitution c^(q+1)=q+1 gives the exact positive margin
   (c-1)(q+1-c^2)/(c(c+1)(q+1)). Its sign holds for every q>=2.
   No limiting positive margin as q tends to infinity is asserted.
5. Rouche counts q+1 zeros of Q, including multiplicities, inside the
   shifted circle. The comparison zeros at 0 and -1 are strictly inside.
   Q has exactly that degree, and the separate zero of Phi at zero is simple.
6. The inner argument was strengthened to closed-disk exclusion for Q.
   The old P4 Hurwitz determinants 9,64,128 are correct, but a direct
   bound |2+2w|>=2>1>=|z w^2| removes that dependency. The q=3 equality
   possibilities at z=0,-1 were checked individually.
7. Stars and the diameter-three classification give the stated corollary;
   n=2 and the parity and uniqueness of the star outer-boundary root were
   checked directly. The star calculation is not presented as a new result.

## Reproduction

    python3 evidence/research-exact-check.py

The final run passed and wrote `evidence/research-exact-checks.json`:

- 25 connected-set coefficient checks: q=2,...,10, a=1,...,floor(q/2),
  b=q-a, n=q+2. An independently coded exhaustive subset routine counts
  edges in each induced forest; a nonempty forest is connected exactly when
  its edge count equals its vertex count minus one. This differs from the
  triage traversal implementation.
- 144 exact polynomial root checks: q=2,...,24, the same full a range,
  n=4,...,26. These are all double-star parameters in this range up to
  interchanging the centres. Each check covers every root of that polynomial.
  This is a family check, not a census of all trees.
- 288 Schur recursions: one for the inner region and one for the outer region
  for each of those 144 polynomials. All integers and rationals are exact.
- Six control polynomials check stable, unstable, unit-boundary and
  later-recursion-failure cases. Six separately constructed SymPy identities
  check both coordinate transforms, including (a,b)=(1,23) and (12,12).
- 63 exact endpoint algebra checks, q=2,...,64, by polynomial remainder
  modulo c^(q+1)-(q+1). The proof of the sign and the identity for all q is
  analytic, not inferred from this finite list.

The new computations are supplementary falsification attempts against the
completed theorem, not a fresh model review or statistically independent
confirmation. The small formulas and parameter ranges were selected after
the analytic argument existed. No numerical root approximations are used.

## Why the exact root checks certify their finite assertions

Let P(x) be real of degree d, with leading coefficient A and constant B,
and let P*(x)=x^d P(1/x). Assume |B|<|A|. Put

    G(x)=[A P(x)-B P*(x)]/x.

Then G has degree d-1 and leading coefficient A^2-B^2. If G has all its
zeros in |x|<1, then P has none on |x|=1: a zero of P there is also a zero
of P*, hence of G, a contradiction. On that circle |P*|=|P|, so
|B P*|<|A P|. Rouche shows that P has the same number of interior zeros
as xG, namely d. Recursing down to a nonzero constant therefore certifies
strict unit-disk containment. Dividing by the positive content of an integer
coefficient list, and changing its sign when necessary, preserves all roots.

For the inner check, with d=deg Q, use

    I(u)=(2u)^d Q((1-u)/(2u)).

Its constant term is one, its leading coefficient is nonzero, and its roots
are u=1/(2z+1) as z ranges over roots of Q. Thus strict unit-disk containment
of I proves |z+1/2|>1/2 for every Q root. The nonzero leading coefficient
also verifies that z=-1/2 is not an omitted root.

For the outer check, choose the largest k/10000 with
(k/10000)^(q+1)<q+1 using only integer bisection. Write c0=k/10000 and
R=c0+1/2. Transform Q to V^d Q(Rx-1/2), with an even common denominator
V for R and 1/2. Its Schur stability proves |z+1/2|<R<c+1/2. The saved
JSON gives the exact R and initial coefficient lists. Every recursion row
records a positive exact margin and a binary digest; the script recomputes
all intermediate integers, rather than trusting those labels or digests.

An initial implementation run exceeded Python's decimal-output digit limit
when trying to print large intermediate certificate coefficients. The
recording format was changed to store their bit lengths and binary hashes,
alongside the complete initial polynomials. This was an operational output
failure, not a failed inequality, and the corrected final run completed.

## Limits

No known mathematical gap remains in the stated family proof after this
pass, but correctness, novelty and value still require the fresh referee.
The original arbitrary-tree statement is unresolved. The prior rooted-disk
counterexample in `structural-test.md` concerns only its named auxiliary
invariant and is not a counterexample to any subtree-root assertion here.
