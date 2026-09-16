# Exact proof dossier: the odd all-one family is real stable

All identities below use the variable and normalization of `source.md`.  Put

\[
q_j(x)=Q_{\mathcal C(1^j)}(x)\qquad (j\geq 1).
\]

The claim in `problem.md` is that every nonzero zero of
\(R_n=q_{2n+1}\), \(n\geq1\), is real.

## 1. Direct rational-tangle transfer

Work in the relative Q-skein of a disk with four boundary points.  Write
\(1,e,g\) for, respectively, the two vertical strings, the cup--cap, and a
single crossing.  The skein relation and invariance under a curl give

\[
g+g^{-1}=x(1+e),\qquad ge=eg=e,
\qquad e^2=\delta e,\qquad \delta=2x^{-1}-1.
\]

Indeed, applying the skein relation to a curl gives
\(Q_{L\sqcup U}=\delta Q_L\).  Multiplying the first displayed relation by
\(g\) therefore gives

\[
g^2=-1+xe+xg. \tag{1}
\]

Let \(\rho\) be a planar quarter-turn composed with mirroring.  A quarter-turn
sends a rational-tangle fraction \(f\) to \(-1/f\), while mirroring changes
its sign, so \(\rho\) sends \(f\) to \(1/f\).  On the three diagrams above it
sends \(1\leftrightarrow e\) and fixes \(g\).  Starting with \(T_1=g\), the
standard positive all-one rational-tangle construction is

\[
T_{j+1}=g\rho(T_j).
\]

At the level of fractions this is exactly
\(F_{j+1}/F_j=1+F_{j-1}/F_j\), so its closure is the family fixed in
`problem.md`.  In the ordered spanning set \((1,e,g)\), (1) makes the step
matrix

\[
A=\begin{pmatrix}
0&0&-1\\
1&0&x\\
0&1&x
\end{pmatrix}. \tag{2}
\]

The closure functional has values
\(N(1)=\delta\), \(N(e)=N(g)=1\).  Thus

\[
q_j=N(A^{j-1}g).
\]

Direct calculation gives

\[
q_1=1,\quad q_2=2x+1-2x^{-1},\quad
q_3=2x^2+2x-3. \tag{3}
\]

These smallest cases also have a diagrammatic check independent of (2):
\(\mathcal C(1)\) is the unknot; \(\mathcal C(1,1)\) is the Hopf link and
the skein relation gives \(Q_H=2x-\delta\); and at one crossing of the
trefoil \(\mathcal C(1,1,1)\), the switched diagram and the two smoothings
reduce to an unknot, a Hopf link, and an unknot, giving
\(Q_{3_1}+1=x(Q_H+1)\), which is the third value in (3).  As a convention
check, (2) also gives

\[
q_4=2x^3+4x^2-2x-3,
\]

the value forced by Shoji's even-family recurrence and initial data.

The two characteristic polynomials needed below are

\[
\begin{aligned}
\det(\lambda I-A)
 &= (\lambda+1)(\lambda^2-(x+1)\lambda+1),\\
\det(\lambda I-A^2)
 &= (\lambda-1)
    (\lambda^2-(x^2+2x-1)\lambda+1).
\end{aligned} \tag{4}
\]

Consequently the full sequence and the odd subsequence satisfy, respectively,

\[
q_{j+3}=xq_{j+2}+xq_{j+1}-q_j, \tag{5}
\]

and

\[
R_n-(x^2+2x)R_{n-1}+(x^2+2x)R_{n-2}-R_{n-3}=0. \tag{6}
\]

All initial Laurent polynomials for (6) are

\[
\begin{aligned}
R_0&=1,\\
R_1&=2x^2+2x-3,\\
R_2&=2x^4+6x^3-8x-1+2x^{-1}.
\end{aligned} \tag{7}
\]

Thus (6) is genuinely the odd subsequence with its own initial data, not a
relabeling of the even case.

## 2. Closed form

Set \(x=2\cos\theta-1\).  Factoring (4), and matching (3), gives the rational
identity

\[
q_j(2\cos\theta-1)=
\frac{(-1)^j(\cos2\theta-\cos\theta)
      +2\cos((j+1)\theta)}
     {(2\cos\theta-1)(\cos\theta+1)}. \tag{8}
\]

This can also be checked without division at the exceptional values: after
cross-multiplication both sides obey (5), and (3) supplies the initial cases.

For the odd family put \(m=2n+2\), \(c=(x+1)/2\), and

\[
H_n(x)=2\{c-T_2(c)+2T_m(c)\}, \tag{9}
\]

where \(T_r(\cos\theta)=\cos(r\theta)\).  Equation (8) is exactly

\[
x(x+3)R_n(x)=H_n(x). \tag{10}
\]

The polynomial \(H_n\) has degree exactly \(m\).

## 3. Complete real-root count

Define

\[
h_n(\theta)=\cos\theta-\cos2\theta+2\cos(m\theta),
\qquad 0\leq\theta\leq\pi.
\]

For \(\theta_k=k\pi/m\), write \(c_k=\cos\theta_k\).  Then

\[
h_n(\theta_k)=2(-1)^k+\phi(c_k),
\qquad \phi(c)=-2c^2+c+1.
\]

On \([-1,1]\),

\[
-2\leq\phi(c)\leq\frac98,
\]

and equality on the left occurs only at \(c=-1\).  Hence
\(h_n(\theta_k)>0\) for every even \(k<m\),
\(h_n(\theta_k)<0\) for every odd \(k\), and
\(h_n(\pi)=0\).  The intermediate value theorem supplies one zero in each
of the \(m-1\) intervals
\((\theta_k,\theta_{k+1})\), \(0\leq k\leq m-2\), plus the zero at
\(\theta=\pi\).  These are \(m\) distinct zeros.  Since (9) has degree
\(m\) in \(c\), and \(\cos\theta\) is injective on \([0,\pi]\), these are
all its zeros and all are simple.  In particular, every zero of \(H_n(x)\)
is simple, real, and lies in \([-3,1]\).

It remains only to track the two denominator factors in (10).  Always
\(H_n(-3)=0\).  At \(x=0\),

\[
H_n(0)=2\left(1+2\cos\frac{m\pi}{3}\right)
=\begin{cases}
0,&n\not\equiv2\pmod3,\\
6,&n\equiv2\pmod3.
\end{cases} \tag{11}
\]

All roots are simple, so every indicated cancellation is exactly once.
If \(n\not\equiv2\pmod3\), then
\(R_n=H_n/[x(x+3)]\) is an ordinary polynomial and all of its
\(m-2=2n\) zeros are real.  If \(n\equiv2\pmod3\), then

\[
xR_n(x)=\frac{H_n(x)}{x+3}
\]

is the canonical monomial-cleared polynomial and all of its
\(m-1=2n+1\) zeros are real (and nonzero by (11)).  This proves the frozen
assertion for every \(n\geq1\).  It also proves the stronger statement that
the canonical zeros are simple and contained in \([-3,1]\).

## 4. Exact computational cross-check

`evidence/verify_odd_family.py` independently constructs the Laurent
polynomials from (2), constructs (9) using exact Chebyshev polynomials over
\(\mathbb Q\), asserts their equality for \(1\leq n\leq20\), and performs
exact Sturm counts on every canonical polynomial.  The reproducible output
in `evidence/sturm_counts.txt` records degree-many distinct real roots in all
20 cases.  These finite checks audit the formulas; the universal conclusion
comes from the sign argument above, not from the computation.
