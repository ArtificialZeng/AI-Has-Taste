# Certified short-factor bound

## Claim

Let (w=h^\omega(0)) be the word in `source.md`.  For every (s\geq0) and
positive (m,n) with (m+n\leq2745), the adjacent factors

\[
x=w_s\cdots w_{s+m-1},\qquad
y=w_{s+m}\cdots w_{s+m+n-1}
\]

have different normalized Parikh vectors.  Consequently, if the frozen claim
is false, every counterexample has total length (m+n\geq2746).

## Proof

Write (B=14^3=2744).  The base word

\[
b=01213101314310
\]

has no equal adjacent letters, and its first and last letters are both (0).
It follows inductively that every (h^k(0)), and hence (w), has no equal
adjacent letters: internal image adjacencies are translates of those in (b),
while the boundary between (h(a)) and (h(c)) is the pair (ac).

Use the canonical level-3 decomposition

\[
w=h^3(w_0)h^3(w_1)h^3(w_2)\cdots .
\]

Every factor of length at most (B+1=2745) meets at most two consecutive
level-3 blocks.  If it meets two, those blocks are (h^3(a)h^3(c)) with
(a\ne c).  Put (d=c-a\pmod 5).  The base word contains an adjacent pair
with each possible nonzero difference:

\[
01\ (d=1),\qquad 13\ (d=2),\qquad
14\ (d=3),\qquad 21\ (d=4).
\]

The morphism is equivariant under cyclic letter translation:
(h^3(a+t)=h^3(a)+t\pmod5).  Therefore (h^3(a)h^3(c)), after one common
cyclic translation of all its letters, is one of the four corresponding block
pairs occurring literally inside

\[
h^4(0)=h^3(b).
\]

The same is immediate for a factor meeting only one block.  Thus every factor
of (w) of length at most (2745) is, up to a cyclic permutation of the
alphabet, a factor of (h^4(0)).  A cyclic permutation merely permutes Parikh
coordinates, so it preserves equality of normalized Parikh vectors and also
preserves the location of an internal split.

The exact sweep in `exhaustive_h4.cpp`, recorded in
`h4_collinearity.json`, found no violating split in (h^4(0)).  It processed
all

\[
\frac{38416\cdot38415}{2}=737875320
\]

left factors and the same number of right factors.  At each split it compared
primitive five-coordinate Parikh signatures in an exact collision-resolving
hash table; equality of these signatures is equivalent to equality of
normalized Parikh vectors.  Applying this finite result to the factor copy
above proves the claim.

## Reproduction and limits

The executable was built and run from the project root with

```text
clang++ -std=c++20 -O3 -DNDEBUG -march=native evidence/exhaustive_h4.cpp -o /tmp/bigmac_exhaustive_h4
/tmp/bigmac_exhaustive_h4
```

The run first reproduced the independent Python (h^3) result and digest.
`verify_h4_certificate.py`, run with the prescribed research interpreter,
independently regenerates both words, checks the digests and loop totals, and
checks every cyclic-difference block representative.  The computation does
not settle factors of total length at least (2746), so it does not resolve
the frozen infinite claim.
