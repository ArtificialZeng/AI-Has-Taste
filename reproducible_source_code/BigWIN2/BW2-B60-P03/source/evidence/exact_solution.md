# Exact solution dossier

Let \(\alpha\) be the unique real root in
\((-1/24,-1/25)\) of

\[
32\alpha^3+48\alpha^2+26\alpha+1=0.
\]

The exact optimum of the frozen conic program is

\[
v_*=-t,
\qquad
t=\frac{32\alpha^2+16\alpha+1}{36}
=0.0108411477500751\ldots .
\]

Equivalently, \(v_*\) is the negative root near \(-0.01084\) of
\(576v^3-16v^2+92v+1=0\).

## Exact primal point and complete face

In the binary-string indexing fixed in `problem.md`, all probabilities not
listed below are zero, and

\[
\begin{array}{c|c}
z&p_z\\ \hline
0000,1111&4(5144\alpha^2+3256\alpha+1711)/35073\\
0001,0111&-2(7552\alpha^2+3362\alpha-2779)/35073\\
0011&-8(1046\alpha^2+1153\alpha-1193)/35073\\
1010&-(2576\alpha^2+3376\alpha-725)/35073.
\end{array}
\]

These six numbers (counting repeated rows separately) are strictly positive
and sum to one.  Define \(x_i=\sum_zp_zz_i\) and
\(X_{ij}=\sum_zp_zz_iz_j\) for \(i<j\).  The diagonal is

\[
\begin{aligned}
X_{11}&=(8368\alpha^2+9224\alpha+2147)/11691,\\
X_{22}&=-4(1204\alpha^2+53\alpha-2245)/35073,\\
X_{33}&=-(15760\alpha^2+12812\alpha-19249)/35073,\\
X_{44}&=-8(454\alpha^2-349\alpha-1099)/11691.
\end{aligned}
\]

Numerically, the six ordered weights on
\((0000,0001,0011,0111,1010,1111)\) are

\[
(0.1807155517,0.1656936580,0.2826366501,
  0.1656936580,0.02454493068,0.1807155517),
\]

and the diagonal is approximately
\((0.1520900498,0.2560514338,0.5632330146,0.7415690851)\).

This point is the **entire** optimal face, including the representing
probability vector.  Thus quotienting by the reverse-complement involution
does nothing further: the unique point is fixed by that involution.

## Exact dual certificate

After eliminating \(x\) and the six off-diagonal entries of \(X\), write

\[
Y=E_{00}+\sum_zp_zF_z+\sum_{i=1}^4X_{ii}E_{ii},
\]

where \(F_z\) has top row/column \(z\), lower off-diagonal entries
\(z_iz_j\), and zero lower diagonal.  Put

\[
v=(8\alpha^2+8\alpha+1)/2,\qquad w=-2\alpha-1
\]

and

\[
S=\begin{pmatrix}
t&\frac14-\alpha-v&-\frac12-v-w&\alpha&0\\
\frac14-\alpha-v&\frac14&-\frac12-\alpha&v&2\alpha\\
-\frac12-v-w&-\frac12-\alpha&1&w&v\\
\alpha&v&w&1&-\frac12-\alpha\\
0&2\alpha&v&-\frac12-\alpha&\frac14
\end{pmatrix}.
\]

Then \(S\succeq0\), \(S_{ii}=Q_{ii}\) for \(i=1,\ldots,4\), and with
dual scalar \(\tau=0\),

\[
h_z-\langle S,F_z\rangle-\tau\geq0
\quad(z\in\{0,1\}^4),
\]

where \(h_z=2\sum_{i<j}Q_{ij}z_iz_j+c^\top z\).  Equality holds exactly
at

\[
0000,0001,0011,0111,1010,1111.
\]

For any primal feasible point,

\[
L=\langle S,Y\rangle-S_{00}
 +\sum_zp_z(h_z-\langle S,F_z\rangle)
\geq -t.
\]

At the displayed primal point, exact arithmetic gives \(SY=0\) and
\(L=-t\), proving global optimality.

For an inspectable PSD check, reverse-coordinate even/odd decomposition of
the lower \(4\times4\) block of \(S\) gives two rank-one PSD matrices.
The top-row vector lies in their ranges and its Schur complement is zero, so
\(S\) is PSD of rank two.  For the primal lifted matrix, every principal
minor of order four is zero, while the principal \(3\times3\) block on
indices \(\{0,1,2\}\) is positive definite.  Hence it is PSD of rank three.
All identities and signs are reproduced exactly by
`evidence/exact_certificate.py` using rational polynomial reduction and
rational interval arithmetic.

Finally, strict positivity of the ten unused atom slacks forces any optimal
distribution to use only the six displayed atoms.  PSD complementarity then
gives \(SY=0\).  Exact row reduction over
\(\mathbb Q[\alpha]/(32\alpha^3+48\alpha^2+26\alpha+1)\) has rank ten in
the six remaining probabilities and four diagonal variables and returns the
displayed point uniquely.  This proves the asserted complete-face
classification rather than only uniqueness inside the symmetric subspace.
