# Proof dependency graph

All variables below are integers with \(1\le i<j\le n/2\).  Write

\[
A=\binom ni,\quad B=\binom nj,\quad
V_i(n)=\prod_{p\ge i}p^{v_p(A)},\quad
U_i(n)=A/V_i(n).
\]

## L1. Transport identity (proved)

\[
\binom ni\binom{n-i}{j-i}=\binom nj\binom ji.
\]

This follows by expanding factorials.  If \(d\mid A\) and \(\gcd(d,B)=1\),
Euclid's lemma applied to the identity gives \(d\mid\binom ji\).

## L2. Large-prime-part divisibility in a counterexample (proved)

In a weak-form counterexample, \(\gcd(V_i(n),B)=1\).  By L1,

\[
V_i(n)\mid\binom ji. \tag{10}
\]

No squarefreeness is assumed: the full prime powers in \(V_i(n)\) divide.

## L3. Kummer carry bound for the small-prime part (proved)

For every prime \(q<i\), Kummer's theorem gives

\[
v_q(A)\le \lfloor\log_q n\rfloor,
\qquad q^{v_q(A)}\le n.
\]

There are \(\pi(i-1)\) such primes, hence

\[
U_i(n)\le n^{\pi(i-1)},\qquad
V_i(n)\ge \frac{\binom ni}{n^{\pi(i-1)}}. \tag{11}
\]

## L4. Explicit fixed-pair bound (proved)

The product formula gives

\[
\frac{\binom ni}{\binom ji}
=\prod_{t=0}^{i-1}\frac{n-t}{j-t}
\ge\left(\frac nj\right)^i,
\]

because \((n-t)/(j-t)\ge n/j\) for \(n\ge j\).  Combining L2--L3,

\[
n^{i-\pi(i-1)}\le j^i,
\quad\text{or}\quad
n\le j^{i/(i-\pi(i-1))}. \tag{12}
\]

The exponent denominator is positive because \(\pi(i-1)<i\).  This proves
finiteness of possible \(n\) for each fixed \((i,j)\).  For \(i=1,2\),
(12) contradicts \(n\ge2j\), so those two strata satisfy the conjecture.
For \(i=3\), it yields \(n\le j^{3/2}\).

## L5. Prime-gap obstruction (proved)

If a prime \(p\in(n-i,n]\), then \(p>n/2\ge j\).  Put \(r=n-p<i\).
Since \(p>j>i\), the one-digit Lucas criterion gives

\[
p\mid\binom ni\quad\text{and}\quad p\mid\binom nj
\]

from \(r<i<j\).  Therefore a counterexample must have no prime in
\((n-i,n]\).  If \(P^-(n)\) denotes the largest prime at most \(n\), then

\[
i\le n-P^-(n). \tag{13}
\]

This proves that a row search need inspect only \(i\) up to the trailing
prime gap.

## L6. Smooth terminal interval (proved)

If a prime \(q>j\) divides one of \(n-i+1,\ldots,n\), then it divides the
numerator of \(A\), cannot divide \(i!\), and hence divides \(A\).  Writing
\(n\equiv r\pmod q\) with \(0\le r<i<j<q\), Lucas again gives \(q\mid B\),
a contradiction.  Thus in a counterexample every one of

\[
n-i+1,\ldots,n
\]

is \(j\)-smooth.  This is a necessary condition, not a sufficient one.

## L7. Accepted EEES size route (external theorem; local reconstruction active)

The 1978 EEES theorem says that, apart from twelve explicit \((n,i)\),
\(V_i(n)>\sqrt{\binom ni}\).  Combining with L2 and Vandermonde yields
the published/accepted partial range \(j\le3i/2\).  The exact treatment of
the twelve pairs and the separate \(n=2j\) case is not yet a local theorem
until the finite verifier and proof audit close.

## Endpoint dependency graph

```text
Kummer/Lucas ----> L3 carry bound ----> L4 finite bound ----> i=1,2 proved
      |                                      |
      +----------> L5 prime gap ------------+----> complete row-search domain
      |                                      |
      +----------> L6 smoothness ------------+----> structured falsification

transport identity --> L2 V_i divisibility --> L4
                                 |
EEES theorem --------------------+--> L7 accepted partial range (audit active)
```
