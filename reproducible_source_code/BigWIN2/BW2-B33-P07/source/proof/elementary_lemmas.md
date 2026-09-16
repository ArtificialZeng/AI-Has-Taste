# Elementary exact lemmas

All XOR operations below use infinite-width two's-complement integers.

## Lemma E1: bounded XOR displacement

For every (x\in\mathbb Z) and (n\in\mathbb N),

\[
\left|(x\mathbin{\mathrm{XOR}}n)-x\right|\leq n.
\]

Proof. Only bit positions at which (n) has a one can change. If (b_j(x))
is the (j)-th two's-complement bit of (x), then

\[
(x\mathbin{\mathrm{XOR}}n)-x
=\sum_{j:\,b_j(n)=1}(1-2b_j(x))2^j.
\]

This is a finite sum even for negative (x), and its absolute value is at
most (sum_{j:b_j(n)=1}2^j=n).  Equivalently,
(x\mathbin{\mathrm{XOR}}n=x+n-2(x\mathbin{\mathrm{AND}}n)), with
(0\leq x\mathbin{\mathrm{AND}}n\leq n).

## Lemma E2: a global quadratic size bound

For every (n\geq0),

\[
|a_n|\leq \frac{n(n+1)}2.
\]

Proof. Put

\[
d_n=(a_{n-1}\mathbin{\mathrm{XOR}}n)-a_{n-1}.
\]

Then (|d_n|\leq n) by E1 and

\[
a_n=a_{n-1}-a_{n-2}+d_n.
\]

The homogeneous solution with initial values (0,1) is six-periodic and has
absolute value at most one.  The impulse response beginning at its forcing
index is (1,1,0,-1,-1,0,\ldots), also of absolute value at most one.
Therefore, for (n\geq2),

\[
|a_n|\leq 1+\sum_{j=2}^n|d_j|
\leq1+\sum_{j=2}^n j=\frac{n(n+1)}2.
\]

The cases (n=0,1) are direct.

## Lemma E3: parity obstruction

The parity sequence is periodic with period six:

\[
(a_n\bmod2)_{n\geq0}=(0,1,1,1,0,0)^{\infty}.
\]

Consequently a zero can occur only when

\[
n\equiv0,4,5\pmod6.
\]

Proof. Modulo two, XOR is addition, so

\[
a_n\equiv a_{n-1}+a_{n-2}+n\pmod2.
\]

Starting from (0,1) gives (0,1,1,1,0,0,0,1); at the last pair both the
state and the parity of the time index have returned, proving the period.

## Lemma E4: exact level-33 necessary condition

Let (L=3\cdot2^{33}=25{,}769{,}803{,}776), and let (Z_{33}) be the 354-entry
array saved at `sequence_period_tests[k=33].zero_residues` in
`experiments/modular-falsification-evidence.json`.  If (a_n=0), then

\[
n\bmod L\in Z_{33}.
\]

Proof. The universal modular-period theorem gives
(a_{n+L}\equiv a_n\pmod {2^{33}}).  The saved traversal, independently
recomputed by `experiments/verify_modular_falsification.py` using the AND
formula rather than direct XOR, evaluates every representative in one period.
Thus the array is an exhaustive exact list of the indices at which
(a_n\equiv0\pmod {2^{33}}), not a sample.  An integer zero must satisfy this
congruence.

The first eight entries of (Z_{33}) are
(0,6,11,23,36,42,48,54); its least further representative is
(123{,}064{,}307).  This is a strong infinite arithmetic restriction, but the
remaining 346 residue classes still contain infinitely many ordinary
integers, so E4 is not a resolution.
