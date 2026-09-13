# Proof audit

Audit date: 2026-08-21.

Terminal status: **partial theorem**.  The stated endpoint passed the audit;
the unrestricted sixth-power equation was not solved.

## Audited endpoint

For a primitive positive solution of

\[
a_1^6+\cdots+a_5^6=B^6,
\]

with repetitions allowed, the manuscript proves:

1. \(\gcd(B,42)=1\);
2. exactly one left-hand occurrence is a unit at each of \(2,3,7\);
3. every repeated left-hand base is divisible by \(42\);
4. the multiplicity patterns \((5),(4,1),(3,2)\) are impossible, so at
   least three distinct left-hand bases are necessary;
5. the divisibility placement in the two exactly-three-distinct patterns
   \((3,1,1)\) and \((2,2,1)\) is as stated in Corollary 4.1.

## Dependency audit

- Sixth-power residues modulo \(8,9,7\) were exhaustively recomputed by two
  independently structured programs.  The residue-count argument correctly
  uses primitivity to rule out \(2\mid B\), \(3\mid B\), and \(7\mid B\).
- A repeated value cannot occupy a unique unit position, so divisibility by
  \(2\), \(3\), and \(7\) follows separately.  No distinctness assumption is
  introduced.
- The partitions of five into at most two positive parts are exactly
  \((5),(4,1),(3,2)\).  The first and third are excluded by the repeated-base
  lemma.
- For \((4,1)\), primitivity makes the singleton \(b\) and right-hand base
  \(B\) odd and coprime.  The positive integers
  \(r=(B^3-b^3)/2\) and \(s=(B^3+b^3)/2\) satisfy \(rs=a^6\) and
  \(\gcd(r,s)=1\).  Unique factorization makes both sixth powers, and
  \(B^3=(u^2)^3+(v^2)^3\) contradicts Fermat's theorem for exponent three.
  The only external mathematical dependency is this classical theorem.
- The exactly-three-distinct classification exhausts the relevant
  partitions and then places the unique unit occurrence; it does not claim
  those two strata are empty.

## Computational audit

`code/run_all_verifiers.py` passed.  The exact finite search indexed 499,500
unordered pair sums and tested 1,879,634 exact targets, finding no
repeated-summand solution with \(B\le 1000\).  This is recorded only as a
finite diagnostic, not as evidence for unbounded nonexistence.

## Remaining global gaps

The patterns \((3,1,1)\), \((2,2,1)\), \((2,1,1,1)\), and the all-distinct
pattern remain open.  There is no six-integer counterexample certificate and
no unrestricted nonexistence proof.  No proof assistant was used.
