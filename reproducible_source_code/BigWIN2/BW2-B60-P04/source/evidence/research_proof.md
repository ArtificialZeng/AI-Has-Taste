# Symbolic generic resolution of win-00060-p04

Work over
\[
 R=\mathbb Q[a_{11},a_{12},a_{21},a_{22},b_1,b_2,c_1,c_2,p_1,p_2,q],
 \qquad F=\operatorname{Frac}(R),
\]
with zero derivation on the coefficient indeterminates. Put
\[
 x'=Ax+bu+c,\qquad y=p^Tx+q,
\]
as in `problem.md`, and write
\[
 \tau=\operatorname{tr}(A),\quad \delta=\det(A),\quad
 \Omega=\det\!\begin{pmatrix}p^T\\p^TA\end{pmatrix}.
\]

## Theorem

For the coefficient-generic system above, the generic order is two and the
eliminant, normalized to be monic in \(y''\), is
\[
 E=y''-\tau y'+\delta y
   +p^T(\tau I-A)b\,u-p^Tb\,u'
   +p^T(\tau I-A)c-\delta q.                 \tag{1}
\]
All six coefficients of the monomials
\(1,u,u',y,y',y''\) are nonzero coefficient polynomials. Hence the exact
generic support is
\[
 \{1,u,u',y,y',y''\}.
\]
The seven candidates supplied by Theorem 3.7 in the cited paper are
\(1,u,u',u'',y,y',y''\), so the missing monomial is \(u''\). Equivalently,
every support exponent satisfies the additional exact equality \(\ell_2=0\).

## Proof

The first two output derivatives, after substituting the state equation, are
\[
 y'=p^TAx+p^Tb\,u+p^Tc,
\]
and
\[
 y''=p^TA^2x+p^TAb\,u+p^TAc+p^Tb\,u'.        \tag{2}
\]
The Cayley--Hamilton identity \(A^2-\tau A+\delta I=0\), inserted in (2),
gives (1) identically in \(R[x_1,x_2,u,u']\).

It remains to show that this identity is the eliminant rather than a
nonminimal relation. Its observability determinant is
\[
 \Omega=p_1^2a_{12}+p_1p_2(a_{22}-a_{11})-p_2^2a_{21},
\]
which is a nonzero element of \(R\) (for example, set
\(p_1=a_{12}=1,p_2=0\)). Let \(L=\operatorname{Frac}(F\{u\})\). In the
evaluation quotient of the differential system,
\[
 \binom{y-q}{y'-p^Tb\,u-p^Tc}
 =\begin{pmatrix}p^T\\p^TA\end{pmatrix}x.    \tag{3}
\]
Because \(\Omega\ne0\) in \(F\), (3) is an invertible affine change of
coordinates over \(L\). Thus \(y,y'\) are algebraically independent over
\(L\). Identity (1) makes \(y,y',y''\) dependent, proving that the least
order \(\nu\) is exactly two.

For completeness, the defining-ideal assertion can be seen directly. Let
\(B=F[u_0,u_1,u_2]\), and consider the coordinate-ring map associated with
the order-two input-output morphism,
\[
 \psi:B[Y_0,Y_1,Y_2]\longrightarrow B[x_1,x_2].
\]
It fixes the \(u_i\) and sends \(Y_i\) to the evaluated \(i\)-th output
derivative. By (3), its restriction
\(B[Y_0,Y_1]\to B[x_1,x_2]\) is an isomorphism. If
\[
 \alpha=p^T(\tau I-A)b,\quad \beta=p^Tb,\quad
 \gamma=p^T(\tau I-A)c,
\]
then (1) says that \(Y_2\) maps, under this isomorphism, to
\[
 \tau Y_1-\delta Y_0-\alpha u_0+\beta u_1-\gamma+\delta q.
\]
Division by the monic polynomial
\[
 Y_2-\tau Y_1+\delta Y_0+\alpha u_0-\beta u_1+\gamma-\delta q
\]
therefore proves \(\ker(\psi)=(E)\). In particular the image is already the
closed graph cut out by \(E\). The polynomial is primitive because its
\(Y_2\)-coefficient is one, and it is irreducible because it is monic of
degree one in \(Y_2\). Consequently it is precisely the primitive
irreducible defining equation in Definition 3.3 of the cited paper.

The six coefficient polynomials, ordered as
\(y'',y',y,u',u,1\), are
\[
 1,\quad-\tau,\quad\delta,\quad-p^Tb,\quad
 p^T(\tau I-A)b,\quad p^T(\tau I-A)c-\delta q.       \tag{4}
\]
They are simultaneously nonzero at the exact specialization
\[
 A=\begin{pmatrix}1&1\\1&2\end{pmatrix},\quad
 p^T=(1,0),\quad b=(1,1)^T,\quad c=(1,0)^T,\quad q=0,
\]
where \((\Omega,\tau,\delta,p^Tb,p^T(\tau I-A)b,
p^T(\tau I-A)c-\delta q)=(1,3,1,1,1,2)\). Hence their product is a nonzero
coefficient polynomial and their common nonvanishing locus is a nonempty
Zariski-open set. On that locus, every monomial in the displayed support
occurs.

Finally, the first specialized inequality of Theorem 3.7 bounds total degree
by one, so its candidates can only be the constant and the six individual
variables \(u,u',u'',y,y',y''\); direct substitution shows that all seven
satisfy the remaining inequalities. Formula (1) contains the other six and
is independent of \(u''\). This proves both the missing-monomial assertion
and the exact additional equality \(\ell_2=0\). \(\square\)

The symbolic identities, candidate enumeration, inverse-coordinate check,
and exact open-set witness are reproduced by
`evidence/research_symbolic_certificate.py`.
