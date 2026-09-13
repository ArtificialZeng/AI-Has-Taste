# Exact structural reductions

Write the fixed-\(n\) candidate condition as

\[
  \tau(n-k)\le k+2\qquad(1\le k<n). \tag{L}
\]

The following argument is independent of the search code.

## Lemma 1 (two last shifts)

If \(n>24\) satisfies (L), then

\[
 n=2q+2,
\]

where both \(q\) and \(2q+1\) are prime.

**Proof.**  At \(k=1\), \(\tau(n-1)\le3\), so \(n-1\) is prime or the
square of a prime.  If \(n\) were odd, then the even number \(n-1>4\) could be
neither: an even prime square with three divisors is only \(4\).  Thus \(n\) is
even.  The even number \(n-2>8\) has at most four divisors.  The complete
classification from the prime-exponent formula for \(\tau\) gives
\(n-2=2q\) with \(q\) an odd prime.  Finally \(n-1=2q+1\equiv3\pmod4\), so it
cannot be a square; it is prime. ∎

## Lemma 2 (prime-chain reduction)

Every candidate \(n>24\) lies in exactly one of the two shapes

\[
\begin{aligned}
  &n=8s+8,  &&s,\ 2s+1,\ 4s+3,\ 8s+7\text{ all prime};\tag{A}\\
  &n=16s+8, &&s,\ 4s+1,\ 8s+3,\ 16s+7\text{ all prime}.\tag{B}
\end{aligned}
\]

**Proof.**  By Lemma 1 write \(q-1=2^a r\), with \(r\) odd.  Since
\(n-4=2(q-1)\), the \(k=4\) condition is

\[
 (a+2)\tau(r)\le6. \tag{1}
\]

For \(a=1\), (1) gives \(\tau(r)\le2\); the cases \(r=1\) and \(q\le11\)
are excluded by \(n>24\), so \(r=p\) is prime.  For \(a=2,3\), (1) forces
\(r=1\), giving \(q=5,9\); for \(a=4\), it gives \(q=17\), but then
\(2q+1=35\) contradicts Lemma 1; and \(a\ge5\) is impossible.  Hence
\(q=2p+1\), with \(p,2p+1,4p+3\) prime and \(n=4p+4\).

Now write \(p-1=2^b s\), with \(s\) odd.  Since
\(n-8=4(p-1)\), the \(k=8\) condition is

\[
 (b+3)\tau(s)\le10. \tag{2}
\]

For \(b=1,2\), (2) gives \(\tau(s)\le2\); the \(s=1\) cases give
\(n\le24\), so \(s\) is prime.  For \(b=3,\ldots,7\), (2) forces
\(s=1\), giving \(p\in\{9,17,33,65,129\}\), each composite or (for
\(p=17\)) making \(q=35\) composite.  For \(b\ge8\), (2) is impossible.
Substitution gives (A) and (B).  The two shapes have different 2-adic
valuations of \(n\), so are disjoint. ∎

## Lemma 3 (finite-prefix domination certificates)

For an integer \(m\), define its kill interval

\[
 I_m=[m+1,\,m+\tau(m)-3]\cap\mathbb Z.
\]

Every \(n\in I_m\) fails (E647), because \(m<n\) and
\(m+\tau(m)\ge n+3\).  Consequently, a list of exact factorizations of
integers \(m_i\), whose intervals \(I_{m_i}\) concatenate without a gap, is a
finite exclusion certificate.  This is an exact equivalence for the excluded
points and does not imply that such intervals cover all sufficiently large
integers.

## Search-space boundary

Recent formal/computational work supplies the additional necessary condition
that every candidate \(n>84\) has \(2520\mid n\), and that for
\(n=2520N\), \(N\bmod46189\) belongs to an explicit set of 96 elementary
12-form-sieve residues.  The later full-value analysis closes 55 of these and
leaves 41 open, but the present replay deliberately enumerates all 96 and does
not depend on that later split or its axiom boundary.  This project treats the
imported 2520-divisibility and 96-residue reduction as a separately audited
dependency and reconstructs the finite residue arithmetic rather than silently
trusting a copied list.

The prime-chain lemma shows why an unrestricted linear prefix sieve is the wrong
post-frontier search class.  It also shows why finite-window constructions under
prime-tuple hypotheses do not settle the full problem: the necessary window
length grows with the largest possible divisor count below \(n\).
