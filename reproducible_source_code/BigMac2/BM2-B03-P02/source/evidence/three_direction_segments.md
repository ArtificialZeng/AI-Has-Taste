# Exact segment reduction for the remaining `3+1+1` kernel

This note sharpens `three_direction_reduction.md`.  It computes, without a
triangle-inequality relaxation, every certificate using two labels in the
three-label direction class and either singleton.  It does **not** prove the
final (5E/8) comparison.

## Setup

Retain the notation of the earlier note.  Write (G_1=\{1,2,3\}), put

\[
 r_i=p_i/P_1,\qquad w_i=z_i-m_1 \quad (i\in G_1),
\]

so that

\[
 r_i>0,\quad \sum_i r_i=1,\quad \sum_i r_iw_i=0,\quad
 V_1=\sum_i r_i|w_i|^2.
\]

For (g\in\{2,3\}), let (h) denote the other singleton class and set
(d_{1g}=|\tau_1-\tau_g|^2).  For a complex segment, `dist` below is ordinary
Euclidean distance in \(\mathbb C\simeq\mathbb R^2\).

## Proposition (exact singleton-segment formula)

For (g\in\{2,3\}), the least value supplied by all selections supported on
the singleton in class (g) and at most two labels of (G_1) is

\[
 S_g=\frac{|m_g|^2}{2}+\frac{2}{d_{1g}}\,
 \min_{1\le i<j\le3}
 \operatorname {dist}^2\!\left(-\frac{m_1}{2P_g},[w_i,w_j]\right).
 \tag{1}
\]

Using the three-direction identities, this is equivalently

\[
 S_g=\frac{1-2P_g}{2P_g}E_m+
 \frac{2P_1P_g}{1-2P_h}\,\delta_g^2,
 \qquad
 \delta_g^2:=\min_{i<j}\operatorname {dist}^2
 \!\left(-\frac{m_1}{2P_g},[w_i,w_j]\right).
 \tag{2}
\]

Every value in (1), including an endpoint minimum, is attained by an
admissible selection of at most three labels.  Consequently the whole
`3+1+1` stratum has the attained certificate

\[
 \min\left\{2P_1^2d_*^2,S_2,S_3\right\},
 \qquad d_*^2=\min_i|w_i|^2.                         \tag{3}
\]

### Proof

For aggregate class means, let (A_g\in\mathbb C^2) be the two-point
interpolating coefficient between \((\tau_1,m_1)\) and
\((\tau_g,m_g)\).  Replacing (m_1) by (m_1+w) changes it by

\[
 v_gw,\qquad
 v_g=\frac{(-\tau_g,1)}{\tau_1-\tau_g},\qquad
 \|v_g\|^2=\frac2{d_{1g}}.
\]

Eliminating the third class from the two aggregate response-moment equations,
and then using \(\sum_kP_k\tau_k=0\), gives the exact identity

\[
 (1+\overline{\tau_g}\tau_1)m_g
   =-\frac{1-2P_g}{P_g}m_1.                         \tag{4}
\]

The Hermitian projection coefficient of (A_g) on the complex line spanned
by (v_g) is therefore

\[
 \frac{\langle v_g,A_g\rangle}{\|v_g\|^2}
 =m_1-\frac{1+\overline{\tau_g}\tau_1}{2}m_g
 =\frac{m_1}{2P_g}.
\]

Moreover

\[
 \frac{|\det(v_g,A_g)|^2}{\|v_g\|^2}=\frac{|m_g|^2}{2}.
\]

The two orthogonal components hence give

\[
 \|A_g+v_gw\|^2
 =\frac{|m_g|^2}{2}+\frac2{d_{1g}}
   \left|w+\frac{m_1}{2P_g}\right|^2.              \tag{5}
\]

Splitting the selected mass in direction (\tau_1) between labels (i,j)
allows every (w=(1-\theta)w_i+\theta w_j), (0\le\theta\le1).  Giving the
singleton any positive remaining mass makes \(|\mu|<1\), while the fitted
coefficient remains the two-direction interpolant.  Thus (5) proves (1) and
attainment.  Finally

\[
 |m_g|^2=\frac{1-2P_g}{P_g}E_m,qquad
 P_1P_gd_{1g}=1-2P_h
\]

prove (2); (3) combines (2) with the one-from-each-class certificate already
proved in `three_direction_reduction.md`.

For reproducibility, the segment minimizer used in (1) is

\[
 \theta_{ij,g}=\operatorname{clip}_{[0,1]}
 \frac{-\operatorname{Re}\!\left(
 \overline{w_i+m_1/(2P_g)}(w_j-w_i)\right)}{|w_j-w_i|^2},               \tag{6}
\]

with the coincident-endpoint case interpreted directly.

## Two proved but insufficient relaxations

The class barycentre puts

\[
 y_i=-\frac{r_i}{1-r_i}w_i\in[w_j,w_k]
 \quad(\{i,j,k\}=\{1,2,3\}).
\]

Two elementary estimates are useful for checking future arguments:

\[
 \min_i|y_i|^2\le \frac{V_1}{4},                    \tag{7}
\]

because otherwise

\[
 V_1=\sum_i r_i|w_i|^2>
 \frac{V_1}{4}\sum_i\frac{(1-r_i)^2}{r_i}\ge V_1,
\]

where \(\sum_i1/r_i\ge9\).  Also, with
(s_i=(1-r_i)/2), one has \(\sum_i s_iy_i=0\) and

\[
 \sum_i s_i|y_i|^2
 =\frac12\sum_i\frac{r_i^2}{1-r_i}|w_i|^2\le\frac{V_1}{2}.             \tag{8}
\]

The last inequality is the diagonal quadratic-form inequality

\[
 \sum_i\frac{r_i^2}{1-r_i}|w_i|^2\le\sum_i r_i|w_i|^2
 \quad\text{on }\sum_i r_iw_i=0;
\]

if all (r_i\le1/2) it is termwise, and if (say) (r_1>1/2), substituting
(r_1w_1=-r_2w_2-r_3w_3) and weighted Cauchy--Schwarz proves it.
Thus, for either target (u=-m_1/(2P_g)),

\[
 \delta_g^2\le
 \min\left\{(|u|+\sqrt{V_1}/2)^2,\ |u|^2+V_1/2\right\}.               \tag{9}
\]

These bounds discard the direction of the exact segment projection and do
not close (5E/8).  For example, take (P_1=P_2=P_3=1/3), (E_m=1), equal
conditional weights, and an equilateral deviation triangle with (V_1=48).
The right side of (9), inserted in (2), exceeds (5E/8=85/8), although the
exact edge facing the target makes (2) far smaller.  Hence this failure is an
obstruction only to the norm/averaging relaxation, not to Assertion 1.

## Remaining scalar kernel

It is now enough (and remains unproved) to establish, for all

\[
 P_k\in(0,1/2),\quad \sum_kP_k=1,\quad r_i>0,\quad
 \sum_i r_i=1,\quad \sum_i r_iw_i=0,
\]

and all compatible (m_1,E_m\), that the minimum in (3) is at most

\[
 \frac58\left(E_m+P_1V_1\right).                    \tag{10}
\]

All complex regression variables and all direction phases have disappeared
from (10): the two targets are collinear, at
(-m_1/(2P_2)) and (-m_1/(2P_3)), and each \(\delta_g\) is given by the
clipped quadratic formula (6).  This is a finite semialgebraic case split
(three edges times endpoint/interior status for each target), rather than the
original selection problem.
