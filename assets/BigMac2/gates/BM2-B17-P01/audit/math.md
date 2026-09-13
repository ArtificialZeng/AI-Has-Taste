# Fresh mathematical referee report

## Frozen scope and materials

I reviewed the exact universal statement frozen in `source.md` and interpreted
in `problem.md`: for every integer \(n\ge 496\), every admissible
\(1\le a<n/2\) has \(R_n(a)<1\).  The submitted claim is a
`resolution-paper`, not a partial result.  Its two asserted ranges are the exact
finite interval \(496\le n\le100000\) and the analytic tail
\(n\ge100001\), so accepting it requires both ranges with no weakening.

The SHA-256 values of `source.md`, `problem.md`, `claim.json`, and all five
decisive files under `evidence/` agree with `audit/snapshot.json`.  I also
recomputed the canonical digest of the snapshot file map as
`124cbe9f75d939decb620e907de84b0c167e0da00c9cfde5e2dd61d12b737b03`.
In accordance with the referee assignment, I did not use `checkpoint.md` or any
owner verdict or confidence statement.

## Reconstruction of row localization

All denominators in the target range are positive.  For
\(2\le a<n/2\), direct cancellation in the definition gives
\[
q_n(a):=\frac{R_n(a-1)}{R_n(a)}
=\frac{a(a-1)(n-2a+3)}{(n-a+1)^2(n-2a+1)}.
\]
With \(t=n-2a+1\), clearing the positive denominator gives the exact
identity
\[
a(a-1)(n-2a+3)-(n-a+1)^2(n-2a+1)
=\frac12H_n(t),
\]
where
\[
H_n(t)=n^2-n(2t^2+3t)-t-1.
\]
Furthermore \(H_n(t+2)-H_n(t)=-n(8t+14)-2<0\).  Since \(t\)
falls by two when \(a\) rises by one, the signs of \(q_n(a)-1\) pass
from negative to nonnegative exactly once.  Thus the index immediately before
the first nonnegative threshold is a genuine row maximizer.  If the threshold
is zero, the next index is the sole additional maximizer and has the same
value.

The endpoint signs used here are valid throughout the submitted range.  At
\(a=2\), one obtains
\(H_n(n-3)=-2(n^3-5n^2+5n-1)<0\).  At the last admissible index,
\(t=2\) for odd \(n\) and \(t=3\) for even \(n\), giving respectively
\(n^2-14n-3>0\) and \(n^2-27n-4>0\).  Hence no boundary maximum is omitted.

## Exact finite range

I rederived the two row-to-row identities used by the computation:
\[
\frac{R_{n+1}(a)}{R_n(a)}=
\frac{(n+1)^2(n-1)(n-2a+2)}
{2(2n-1)(n-a+1)^2(n-2a+1)},
\]
and
\[
\frac{R_{n+1}(a+1)}{R_n(a)}=
\frac{(n+1)^2(n-1)(n-2a)}
{2(2n-1)a(a+1)(n-2a+1)}.
\]
They follow by factorial cancellation from the defining formula, so exact
propagation from one localized maximum to the next does not assume an
asymptotic approximation.

I ran `evidence/resolution_check.py` afresh.  It completed successfully using
Python integers and reduced rational numbers and reproduced the frozen
certificate: all 99,505 rows from 496 through 100000 were tested; the observed
maximizing-index increments were always 0 or 1; there were no maximizing ties
and no violations; and the row-signature hash was
`9b908153a9c38afe5ae28a184267bbc69a65778c08e567eb46658b5e6344c294`.
The eight direct-formula cross-checks, including both endpoints, all agreed
with recurrence propagation.  The largest exact value in this range was at
\((n,a)=(497,241)\), and its denominator exceeded its numerator by the
positive integer serialized in `evidence/resolution_check_results.json`.

As a separate check rather than merely trusting that rerun, I implemented the
definitions directly in a transient exact-integer calculation.  It verified
both transition identities at the six rows 496, 497, 2000, 4096, 10000, and
100000; brute-forced every admissible \(a\) in rows 496, 497, 1000, and 2001;
and directly evaluated the localized peaks at nine selected rows from 496
through 123457.  The brute-force maxima agreed with the threshold localization,
and every checked peak was strictly below one.  These checks supplement, but
do not replace, the algebraic localization and exact exhaustive scan.

## Uniform tail

Let \(a_*=a_0-1\) be the left maximizer given by the first nonnegative
threshold and set \(x=n-2a_*\).  The two adjacent threshold signs are
\[
H_n(x+1)<0\le H_n(x-1).
\]
The second gives
\[
0\le n^2-n(2x^2-x-1)-x,
\]
so \(2x^2-x-1<n\).  Since \(x\ge2\), this implies the strict and uniform
localization bound \(x^2<n\).  A possible tied right maximizer has exactly the
same value, so it needs no separate estimate.

Writing \(a_*=(n-x)/2\), the row maximum is
\[
R_n(a_*)=\frac{2n(x+1)}{n+x}
\frac{\binom n{(n-x)/2}\binom{n-2}{(n-2-x)/2}}
{\binom{2n-2}{n-1}}.
\]
The stated one-sided Stirling inequalities correctly yield the two off-central
upper bounds and the central lower bound.  On multiplying them, the entropy
terms combine with coefficient
\[
A_n=\frac{n-1}{n(n-2)},
\]
and the correction terms combine as
\[
E_n=\frac1{12n}+\frac1{12(n-2)}+\frac1{6(n-1)}.
\]
After using \(n/(n+x)<1\), this gives
\[
R_n(a_*)<\frac{4\sqrt{A_n}}{\sqrt\pi}
\frac{(x+1)e^{-A_nx^2+E_n}}
{\sqrt{(1-x^2/n^2)(1-x^2/(n-2)^2)}}.
\]
The elementary maximum
\(xe^{-Ax^2}\le1/\sqrt{2eA}\), together with \(x^2<n\), therefore gives
\[
R_n(a_*)<\frac4{\sqrt\pi}
\left(\frac1{\sqrt{2e}}+\sqrt{A_n}\right)C_ne^{E_n},
\quad
C_n=\left((1-1/n)(1-n/(n-2)^2)\right)^{-1/2}.
\]
For real \(n>2\), \(A_n\) and \(E_n\) decrease.  Both factors inside
the reciprocal defining \(C_n\) increase, so \(C_n\) also decreases.
Consequently the displayed majorant is largest at the submitted tail endpoint
\(N=100001\).

I checked each endpoint rational comparison.  The bounds
\[
\frac4{\sqrt\pi}<\frac{231}{100},\quad
\frac1{\sqrt{2e}}<\frac{429}{1000},\quad
\sqrt{A_N}<\frac{3163}{10^6},\quad
C_N<\frac{1000011}{10^6},\quad
e^{E_N}<\frac{1000004}{10^6}
\]
follow with the stated positive square/cross-product margins.  For the last,
\(e^u\le(1-u)^{-1}\) for \(0\le u<1\) is used in the correct direction.
Their exact product is
\[
\frac{24957787612296876183}{25000000000000000000}<1,
\]
with positive margin
\(42212387703123817/25000000000000000000\).  Thus every row maximum is
strictly below one for every \(n\ge100001\).

## Scope attacks, comparison, and verdict

The proof preserves the integer quantifiers and strict inequality.  The
admissible sets are nonempty in the target range; all divisions and square
roots have positive arguments; odd and even terminal indices are both handled;
an adjacent maximizing tie is covered; and the finite and analytic ranges meet
without a missing row.  No floating-point estimate or limiting interchange is
used in a decisive step.

Relative to the frozen nearest result in `source.md` and `problem.md`—exact
verification only through 2000 plus the adjacent-ratio identity—the candidate
adds an exact exhaustive bridge through 100000 and a uniform proof of the
entire remaining tail.  This settles the original claim in its full stated
scope and is a substantive resolution, not a routine finite extension or toy
restriction.  The assignment restricted source inspection to the frozen
evidence, so I make no broader priority claim beyond that supplied comparison;
this limitation is not used in the proof.

**Verdict: ACCEPT.**  I found no unresolved mathematical, evidentiary, or scope
gap in the frozen resolution claim.
