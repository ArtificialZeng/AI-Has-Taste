# Exact zero-residue lift tree

Let \(L_k=3\cdot2^k\) and

\[
Z_k=\{0\leq r<L_k:a_r\equiv0\pmod{2^k}\}.
\]

The universal modular-period theorem makes these finite sets into a rooted
binary forest.

## Lemma T1: exact parent map

If \(s\in Z_{k+1}\), then

\[
s\bmod L_k\in Z_k.
\]

Proof.  Write \(s=r+\varepsilon L_k\), where \(0\leq r<L_k\) and
\(\varepsilon\in\{0,1\}\).  The modular-period theorem at level \(k\)
gives \(a_s\equiv a_r\pmod{2^k}\).  Since \(2^{k+1}\mid a_s\), also
\(2^k\mid a_r\), so \(r\in Z_k\).

Thus a node \(r\in Z_k\) has at most two children, \(r\) and \(r+L_k\),
at level \(k+1\).  Equivalently, after fixing \(c=r\bmod3\) and writing
\(r=c+3t\), the child operation appends one binary digit to \(t\):
\(t\mapsto t\) or \(t+2^k\).

## Lemma T2: integer zeros are exactly eventually-lower infinite paths

An ordinary nonnegative integer \(n\) is a zero of the sequence if and only
if the zero-residue forest contains an infinite path whose representatives
are eventually all equal to \(n\).

Proof.  If \(a_n=0\), then \(n\in Z_k\) for every \(k\) with \(L_k>n\),
and these nodes use the lower child forever.  Conversely, an eventually
lower path stabilizes at some representative \(n\).  Membership at every
later level gives \(2^k\mid a_n\) for arbitrarily large \(k\), hence the
fixed integer \(a_n\) is zero.

## Exact unresolved kernel

The original assertion is equivalent to the statement that the only
eventually-lower infinite paths stabilize at

\[
0,6,11,23,36,42,48,54.
\]

This is narrower as a proof-search object than replaying the original
recurrence: every level and every parent/child edge is finite and exactly
checkable.  It is not itself a proof.  A uniform bound on consecutive lower
edges outside the eight known paths would suffice, but the current finite
data cannot establish such a bound.
