# Formal statement

## Definitions and quantifiers

Let \(\mathbb N_{>0}=\{1,2,3,\ldots\}\).  For \(m\in\mathbb
N_{>0}\), define

\[
\tau(m)=\#\{d\in\mathbb N_{>0}:d\mid m\}.
\]

The decision problem is the existential statement

\[
\exists n\in\mathbb N_{>0}\quad
n>24\quad\text{and}\quad
\max_{1\le m<n}\bigl(m+\tau(m)\bigr)\le n+2. \tag{E647}
\]

All inequalities and divisor counts are exact integer statements.  Since
\(n>24\), the maximum is over a nonempty finite set; there is no limiting or
empty-set convention.

## Equivalent local form

Putting \(k=n-m\), (E647) for a fixed \(n\) is equivalent to

\[
\tau(n-k)\le k+2\qquad(1\le k<n). \tag{L}
\]

This change of variables is bijective between \(1\le m<n\) and
\(1\le k<n\); no terms are discarded.  It is useful for discovery, but the
final certificate must verify the original prefix maximum as well.

## Baseline and edge cases

For \(n=24\), direct exact evaluation gives
\[
\max_{1\le m<24}(m+\tau(m))=26=24+2,
\]
with maximizers \(m=20,22\).  This is a baseline outside the requested domain
\(n>24\), not a solution of (E647).

For every \(n>24\), the right side \(n+2\) is the smallest possible uniform
upper threshold: if \(n-1\) is composite then \(\tau(n-1)\ge3\); if \(n-1\)
is prime then \(n\) is even and \(n-2>2\) is an even composite, so
\(\tau(n-2)\ge4\).  Thus the maximum is always at least \(n+2\).  Hence every
solution in the requested domain necessarily has equality.

## Terminal meanings

- **PROVED** means a proof that at least one such integer \(n>24\) exists,
  together with an exact witness and verifier.
- **DISPROVED** means a proof that no such integer exists.
- A finite exhaustive exclusion, regardless of its size, is only a
  **CERTIFIED_FINITE_RESULT** unless coupled to a theorem covering all larger
  integers.
