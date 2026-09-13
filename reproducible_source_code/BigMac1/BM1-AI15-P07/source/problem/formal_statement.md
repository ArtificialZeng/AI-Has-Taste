# Formal statement

## Weak Erdős--Szekeres conjecture (#699)

For every triple of integers \((n,i,j)\) satisfying

\[
n\ge 4,\qquad 1\le i<j\le \lfloor n/2\rfloor,
\]

there exists a (positive) rational prime \(p\) such that

\[
p\ge i,\qquad p\mid \binom ni,\qquad p\mid \binom nj.
\]

Equivalently, the greatest prime factor of
\(\gcd(\binom ni,\binom nj)\) is at least \(i\).  A counterexample is
therefore one integer triple in the displayed domain for which every prime
dividing that gcd is strictly smaller than \(i\).

## Conventions and endpoints

- \(\binom nk=n!/(k!(n-k)!)\), and divisibility is in \(\mathbb Z\).
- The condition written in the source as \(j\le n/2\) means
  \(2j\le n\), equivalently \(j\le\lfloor n/2\rfloor\).
- Equality \(p=i\) is allowed.  It matters only when \(i\) itself is prime.
- The stronger historical variant replaces \(p\ge i\) by \(p>i\).  It is
  not the present conjecture and has known counterexamples.
- The domain is empty for \(n<4\).  The case \(i=1\) is included; there is
  no exceptional zero binomial coefficient or undefined greatest-prime-factor
  convention in the stated domain.

## Exact divisibility formulations used in this project

For a prime \(p\), Legendre--Kummer gives

\[
v_p\binom nk=\sum_{a\ge1}\left(\left\lfloor\frac n{p^a}\right\rfloor-
\left\lfloor\frac k{p^a}\right\rfloor-
\left\lfloor\frac{n-k}{p^a}\right\rfloor\right).
\]

This is positive exactly when adding \(k\) and \(n-k\) in base \(p\)
produces a carry.  In particular, when \(p>k\),

\[
p\mid\binom nk\quad\Longleftrightarrow\quad n\bmod p<k.
\]

If \(i=p\) is prime, Lucas's theorem instead gives
\(\binom np\equiv \lfloor n/p\rfloor\pmod p\); this equality endpoint must
not be silently treated as the easier case \(p>i\).
