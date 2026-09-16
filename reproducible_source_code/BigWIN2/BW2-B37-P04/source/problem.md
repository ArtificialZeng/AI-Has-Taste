# Precise problem reading

## Frozen input

The immutable statement is `source.md` (SHA-256
`1f096da7e19b8c1eea505c2c161c993123ba99462bac0932f4009aa3fe81ecfe`).
This file interprets it; it does not replace or amend it.

## Objects and quantifiers

Let \(p_n\) denote the \(n\)-th positive prime, indexed by \(p_1=2\).  For a
positive integer \(m\), let

\[
v_2(m)=\max\{e\in\mathbb Z_{\geq 0}:2^e\mid m\},\qquad
\operatorname{oddpart}(m)=m/2^{v_2(m)}.
\]

Define a unique integer sequence by \(a_0=0\) and, for every integer
\(n\geq1\),

\[
a_n=\operatorname{oddpart}(a_{n-1}+p_n).
\]

All sums in this recurrence are positive; hence `oddpart` is always defined,
and \(a_n\) is a positive odd integer for every \(n\geq1\).  The finite target
set is exactly

\[
I=\{78{,}493{,}253,78{,}493{,}254,\ldots,100{,}000{,}000\}.
\]

The task is to establish exactly one of the following:

1. **Positive branch:** exhibit an integer \(n\in I\) for which the exactly
   computed recurrence has \(a_n=1\).
2. **Negative branch:** certify the universal finite statement
   \(\forall n\in I,\ a_n\ne1\) by reproducible exhaustive exact computation.

Because \(a_{n-1}\) and \(p_n\) are odd for \(n\geq2\), and the equivalence is
also valid at \(n=1\),

\[
a_n=1\quad\Longleftrightarrow\quad a_{n-1}+p_n\text{ is a power of }2.
\]

This gives an exact hit test; it is not a heuristic or a weakening of the
recurrence.

## Certificate scope

All arithmetic, prime generation, index counting, and hit tests must be exact.
For a negative answer, a verifier must independently enumerate the primes with
their indices and replay recurrence segments between recorded checkpoints; it
must not merely trust a supplied list of primes or a terminal state from one
opaque run.  In the absence of a separately verified prefix certificate in the
project, the state at the lower endpoint must ultimately be anchored by replay
from \((0,a_0)=(0,0)\).  Independent implementations should compare explicit
checkpoint tuples (at least index, indexed prime, recurrence state, and an
integrity digest or equivalent exact segment record) and the complete hit list.

A positive witness still needs enough exact replay/checkpoint evidence to show
that its \(p_n\) and \(a_{n-1}\) have the claimed indices and values.  The
problem asks only about \(I\): a negative result makes no claim about any
\(n>100{,}000{,}000\), whether occurrences are finite, or whether the displayed
frontier is the last occurrence.

## Triage of prior information (retrieved 2026-09-06)

- [OEIS A114216](https://oeis.org/A114216) gives the same recurrence and records
  the exact event at \(n=33900\); its page says only that there was no other hit
  below ten million, not that the present interval has been searched.
- [OEIS A114217](https://oeis.org/A114217), the authoritative occurrence list
  for \(a_n=1\), currently displays
  \(1,2,5,12,14,20,75,33900,78493252\).  Thus it independently supports the
  stated lower frontier, but its displayed list is not a certificate excluding
  later indices through one hundred million.
- [OEIS A114218](https://oeis.org/A114218) displays the corresponding exponents
  ending in \(31\), although its prose comment still discusses \(33900\) and
  exponent \(19\).  This metadata lag is a reason to verify rather than infer
  the requested finite exclusion from the entry.
- The cited “user bibliography row 32” is not present in the project, so it was
  not inspected.  Narrow exact-assertion searches found no additional
  authoritative certificate for the interval.  This is not a priority or
  open-status claim.

The source status is therefore **new-question**: it is a newly selected finite
extension of an authoritative recorded occurrence frontier, not a literature
claim that an open theorem is being solved.  The nearest prior result is the
OEIS-recorded occurrence at \(78{,}493{,}252\).  The proposed delta is a certified
witness or certified exhaustive exclusion on the next \(21{,}506{,}748\)
indices.  The verification route is independent exact prime enumeration and
checkpointed recurrence replay.  This is suitable to advance because the
target and verifier are precise and the computation is finite; no mathematical
resolution has yet been obtained.
