# bigMac-00027-p01 — complete `n=3` overlap-Bernoulli entropy layer

## Immutable source statement

Let `u,v` be arbitrary positive integers.  For `p in [0,1]`, let
`B_1,B_2,B_3` be independent Bernoulli random variables with
`P(B_i=1)=1-p`, and put

\[
X_{u,v}(p)=1+B_1+uB_2+vB_3.
\]

Prove or disprove that the Shannon entropy

\[
h_{u,v}(p)=-\sum_x P(X_{u,v}(p)=x)\log P(X_{u,v}(p)=x),
\qquad 0\log0:=0,
\]

is concave on `[0,1]` for every pair `(u,v)`.  A proof must cover all positive
integer pairs, including every subset-sum collision and all endpoints.  A
counterexample must give an explicit `(u,v)` and a rigorous interval on which
the concavity inequality fails.

Equivalently, for every integer prefix `a_1=2<a_2<a_3`, take
`u=a_2-a_1` and `v=a_3-a_2`; the target is the complete `n=3` case of the
source's recursive overlap-Bernoulli entropy conjecture.  Do not weaken it to
one selected prefix or to sampled values of `p`.

## Source and status boundary

- Primary source: Jörg Neunhäuserer, *Recursive overlap Bernoulli
  distributions and an entropy concavity conjecture*, arXiv:2609.05546v1,
  Conjecture 3.1 and Proposition 3.1, PDF pp.3--4.
- Local primary PDF: `batches/literature/bigMac-27/2609.05546v1.pdf`, SHA-256
  `3e1709d9010041ee3060a0daba79286edabd268c782629f653e98991775314f8`.
- The source proves only the binomial sequence and the completely
  non-overlapping regime, and reports computation for several sequence
  families.  The present full `n=3` layer is not proved there.  Openness and
  novelty remain status-uncertain pending a fresh nearby-literature check.
