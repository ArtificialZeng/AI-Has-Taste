# A proved subregion of the three-direction stratum

This note gives a rigorous partial result for Assertion 1.  It does not settle
the remaining parameter range.

## Lemma (three direction-class energy identities)

Suppose the atoms have exactly three distinct directions
\(\tau_1,\tau_2,\tau_3\).  For direction class \(G_g\), define
\[
 P_g=\sum_{i\in G_g}p_i,\qquad
 m_g=P_g^{-1}\sum_{i\in G_g}p_i z_i,
\]
and its conditional variance
\[
 V_g=P_g^{-1}\sum_{i\in G_g}p_i|z_i-m_g|^2.
\]
Put \(E_m=\sum_gP_g|m_g|^2\).  Then
\[
 E=E_m+\sum_gP_gV_g,
 \qquad P_g|m_g|^2=(1-2P_g)E_m\quad(g=1,2,3).
\]

### Proof

The class totals obey \(\sum_gP_g=1\) and
\(\sum_gP_g\tau_g=0\).  Hence the vectors
\((\sqrt{P_g})_g\) and \((\sqrt{P_g}\tau_g)_g\) are orthonormal in
\(\mathbb C^3\).  The aggregate moment conditions say that
\((\sqrt{P_g}m_g)_g\) lies in their one-dimensional orthogonal complement.
The orthogonal projection onto that complement has diagonal
\(1-P_g-P_g|\tau_g|^2=1-2P_g\).  A vector in the range of a rank-one
projection has coordinate-energy proportions equal to its diagonal entries,
which proves the second identity.  The first is the within/between-class
variance decomposition.

## Proposition (a certified part of the \(3+1+1\) stratum)

Assume the three direction classes have sizes \(3,1,1\), with \(G_1\) the
three-label class.  Let
\[
 d_*^2=\min_{i\in G_1}|z_i-m_1|^2.
\]
There is an explicitly attained, admissible three-label selection satisfying
\[
 C(q)=2P_1^2d_*^2\le 2P_1^2V_1.
\]
Consequently Assertion 1 holds throughout the exact parameter region
\[
 2P_1^2d_*^2\le \frac58(E_m+P_1V_1).
\]
In particular, the coarser condition \(P_1\le5/16\) is sufficient.

### Proof

Choose a label \(i\in G_1\) attaining \(d_*\), take the two singleton
labels, and put on these three labels the direction-class weights
\(P_1,P_2,P_3\).  Their direction mean is zero, so this \(q\) is admissible
and the defining matrix is the identity.  Relative to the aggregate
three-direction system, whose two response moments vanish, replacing \(m_1\)
by \(z_i\) gives
\[
 \nu=P_1(z_i-m_1),\qquad
 \lambda=P_1\overline{\tau_1}(z_i-m_1).
\]
Thus \(C(q)=|\nu|^2+|\lambda|^2=2P_1^2d_*^2\).  Since \(m_1\) is the
conditional weighted mean, \(d_*^2\le V_1\).  Also
\(E=E_m+P_1V_1\) because the singleton classes have zero conditional
variance.  If \(P_1\le5/16\), then
\(2P_1^2V_1\le(5/8)P_1V_1\le(5/8)E\).

## Remaining kernel in this stratum

The only part not covered by this certificate has
\[
 P_1>5/16,\qquad
 2P_1^2d_*^2>\frac58(E_m+P_1V_1).
\]
Here one must exploit a selection using two labels from \(G_1\) and one
singleton direction (or prove a sharper bound on \(d_*\)); repeating the
one-from-each-class certificate cannot decide this region.
