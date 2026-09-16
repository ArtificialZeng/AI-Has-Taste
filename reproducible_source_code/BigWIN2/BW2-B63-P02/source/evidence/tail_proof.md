# Exact tail proof for `J(4r+2,2r,r)`

This note proves the frozen claim directly from the Eberlein formula and the
standard multiplicities recorded in `problem.md`.  All inequalities below are
strict, so it also determines all minimizing indices.

Fix an integer \(r\geq2\), and put

\[
 v=\binom{4r+2}{2r},\qquad
 \Delta=\binom{2r}{r}\binom{2r+2}{r},\qquad
 \theta_j=E_r(j)/\Delta,
\]

and \(m_j=\binom{4r+2}{j}-\binom{4r+2}{j-1}\).  Direct substitution in the
Eberlein formula (equivalently, Proposition 12 of the attached arXiv v1 PDF
with its parameter \(t=2\)) gives

\[
 \theta_0=1,\qquad \theta_1=\frac1{2r+2},\qquad
 \theta_2=-\frac{2r^2+1}{(2r-1)(2r+2)(2r+1)},
\]

and

\[
 \theta_3-\theta_2=\frac{r-1}{2(r+1)(2r+1)}>0.
\]

Thus \(\theta_2<\theta_j\) for \(j=0,1,3\).  It remains to treat
\(4\leq j\leq2r\).

## Multiplicity bound

For \(n=4r+2\), elementary cancellation gives

\[
 \frac{m_{j+1}}{m_j}
 =\frac{(4r+1-2j)(4r+3-j)}{(j+1)(4r+3-2j)}.
\]

The sign of this ratio minus one is the sign of

\[
 g_r(j)=j^2-(4r+2)j+4r^2+3r.
\]

Since \(g_r(j+1)-g_r(j)=2j-4r-1<0\) for \(j\leq2r\), the sequence
\((m_j)_{4\leq j\leq2r}\) first increases and then decreases (either phase
may be empty).  Its minimum is therefore at an endpoint.  For \(r=2\) the
two endpoints coincide.  For \(r\geq3\), binomial unimodality and \(2r\geq6\)
give \(\binom{4r+2}{2r}\geq\binom{4r+2}{5}\), and hence

\[
 m_{2r}=\frac3{2r+3}\binom{4r+2}{2r}
 \geq\frac3{2r+3}\binom{4r+2}{5}\geq m_4.
\]

The last inequality follows after division by \(\binom{4r+2}{4}\) from

\[
 \frac{3(4r-2)}{5(2r+3)}\geq\frac{4r-5}{4r-1};
\]

after cross multiplication its numerator difference is
\(8r^2-46r+81>0\) (its discriminant is \(-476\)).  Consequently
\(m_j\geq m_4\) throughout \(4\leq j\leq2r\).

## Effective trace bound

Because the graph is \(\Delta\)-regular on \(v\) vertices,
\(\operatorname{tr}(A^2)=v\Delta\).  Dividing its spectral expansion by
\(\Delta^2\) yields

\[
 \sum_{j=0}^{2r}m_j\theta_j^2=\frac v\Delta.
\]

Define

\[
 Q(r)=\frac{v/\Delta}{m_4\theta_2^2}.
\]

Exact factorial cancellation gives \(Q(3)=330/361<1\) and

\[
 Q(r)=\frac{6(2r-1)^2\binom{4r}{2r}(r-1)!(r+2)!}
 {(4r-5)(2r^2+1)^2\binom{2r}{r}(2r)!}.
\]

Consequently,

\[
 \frac{Q(r+1)}{Q(r)}=
 \frac{r(r+3)(4r-5)(4r+1)(4r+3)(2r^2+1)^2}
 {2(r+1)(2r-1)^2(2r+1)(4r-1)(2r^2+4r+3)^2}.
\]

If \(D(r)\) denotes the positive denominator on the right, then

\[
 1-\frac{Q(r+1)}{Q(r)}=\frac{P(r)}{D(r)},
\]

where

\[
\begin{split}
P(r)={}&384r^8+2032r^7+1276r^6+76r^5-236r^4\\
      &+136r^3+439r^2+87r-18.
\end{split}
\]

For \(r\geq1\), the only negative terms are already dominated because
\(384r^8-236r^4-18\geq148r^4-18>0\).  Hence \(P(r)>0\), so \(Q\) is strictly
decreasing and \(Q(r)<1\) for every \(r\geq3\).

Suppose now that \(r\geq3\) and some \(j\geq4\) satisfied
\(\theta_j\leq\theta_2<0\).  Then \(\theta_j^2\geq\theta_2^2\), while the
trace identity and the multiplicity bound would give

\[
 \frac v\Delta\geq m_j\theta_j^2\geq m_4\theta_2^2,
\]

contradicting \(Q(r)<1\).  Therefore \(\theta_j>\theta_2\) for every
\(j\geq4\).  Together with the explicit comparisons, this proves that
\(I(r)=\{2\}\) for every \(r\geq3\).

Finally, at \(r=2\), direct evaluation of the five exact integer eigenvalues is

\[
 (E_2(0),E_2(1),E_2(2),E_2(3),E_2(4))=(90,15,-9,-6,6),
\]

so again \(I(2)=\{2\}\).  The least allowed threshold is therefore
\(r_0=2\), and the exception range \(2\leq r<r_0\) is empty.
