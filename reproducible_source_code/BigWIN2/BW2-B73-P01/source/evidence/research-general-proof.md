# Proof of the exact one-atom identity for every \(N\geq 1\)

This proof uses exactly the Fourier, Laplacian, Abel, and balayage
normalizations frozen in `problem.md`.  In particular,

\[
\widehat f(\xi)=\int_{\mathbb R^3}e^{-2\pi i x\cdot\xi}f(x)\,dx,
\quad \widehat{\Delta f}(\xi)=-4\pi^2|\xi|^2\widehat f(\xi),
\]

\[
H_tf=(4\pi t)^{-3/2}e^{-|\cdot|^2/(4t)}*f,
\qquad A_s=s(s-\Delta)^{-1},
\]

and the complement of the partial-balayage domain is \(\{x:|x|\geq R\}\)
up to its null boundary, where

\[
R^3=\frac{3m}{4\pi\kappa}.
\tag{1}
\]

More explicitly, the resolvent convention implied by these formulas is

\[
(s-\Delta)^{-1}\delta_0(x)=\frac{e^{-\sqrt{s}|x|}}{4\pi|x|},
\qquad
\widehat{A_s^Nf}(\xi)=
 \left(\frac{s}{s+4\pi^2|\xi|^2}\right)^N\widehat f(\xi).
\]

The cap-\(\kappa\) partial-balayage convention is
\(m\delta_0=\kappa\mathbf1_\Omega\,dx-\Delta u\),
\(u\geq0\), \(\Omega=\{u>0\}\).  In this radial case it gives
\(\Omega=B(0,R)\) and (1), equivalently \(|\Omega|=m/\kappa\).

## 1. Abel-power kernel and its dilation derivative

For an integer \(N\geq1\), the Laplace formula for a resolvent power and the
heat kernel give, for \(r=|x|>0\),

\[
\begin{aligned}
(s-\Delta)^{-N}\delta_0(r)
&=\frac1{\Gamma(N)}\int_0^\infty
 t^{N-1}e^{-st}H_t\delta_0(r)\,dt\\
&=\frac1{(4\pi)^{3/2}\Gamma(N)}\int_0^\infty
 t^{N-5/2}e^{-st-r^2/(4t)}\,dt .
\end{aligned}
\tag{2}
\]

Put \(z=r\sqrt{s}\) and \(\nu=N-3/2\).  After \(u=st\), the standard
integral representation

\[
\int_0^\infty u^{\nu-1}e^{-u-z^2/(4u)}\,du
=2(z/2)^\nu K_\nu(z)
\]

turns (2), after multiplication by \(s^N\), into

\[
A_s^N\delta_0(r)=s^{3/2}F_N(z),
\qquad
F_N(z)=c_Nz^\nu K_\nu(z),
\quad
c_N=\frac{2^{-\nu-2}}{\pi^{3/2}\Gamma(N)}.
\tag{3}
\]

The identity

\[
\frac d{dz}\bigl(z^\nu K_\nu(z)\bigr)=-z^\nu K_{\nu-1}(z)
\tag{4}
\]

therefore shows that

\[
s\partial_s(A_s^N\delta_0)(r)=s^{3/2}G_N(z),
\quad
G_N(z)=\frac{c_N}{2}z^\nu
 \bigl(3K_\nu(z)-zK_{\nu-1}(z)\bigr).
\tag{5}
\]

For the measure \(m\delta_0\), the right side of (5) is multiplied by \(m\).
Since \(s=z^2/r^2\) and \(ds/s=2\,dz/z\), (5) yields the scale-separated
identity

\[
\int_0^\infty
 |s\partial_s(A_s^N(m\delta_0))(r)|^2\frac{ds}{s}
=\frac{2m^2}{r^6}Q_N,
\qquad
Q_N:=\int_0^\infty z^5G_N(z)^2\,dz.
\tag{6}
\]

## 2. A self-contained Bessel product integral

For real \(\alpha,\beta\) and \(\rho>|\alpha|+|\beta|\),

\[
\begin{aligned}
M(\rho;\alpha,\beta)
&:=\int_0^\infty z^{\rho-1}K_\alpha(z)K_\beta(z)\,dz\\
&=\frac{2^{\rho-3}}{\Gamma(\rho)}
 \Gamma\!\left(\frac{\rho+\alpha+\beta}{2}\right)
 \Gamma\!\left(\frac{\rho+\alpha-\beta}{2}\right)\\
&\hspace{32mm}\times
 \Gamma\!\left(\frac{\rho-\alpha+\beta}{2}\right)
 \Gamma\!\left(\frac{\rho-\alpha-\beta}{2}\right).
\end{aligned}
\tag{7}
\]

For completeness, insert twice

\[
K_\alpha(z)=\frac12(z/2)^\alpha
 \int_0^\infty a^{-\alpha-1}e^{-a-z^2/(4a)}\,da.
\]

The positive integrand permits Tonelli's theorem.  Integrating first in \(z\)
gives a factor
\(\frac12[4ab/(a+b)]^{(\rho+\alpha+\beta)/2}
\Gamma((\rho+\alpha+\beta)/2)\).  The substitution
\(w=a+b\), \(y=a/(a+b)\) separates the remaining integral into one Gamma
integral and one Beta integral, giving exactly (7).  The displayed condition
makes all four Gamma arguments positive and also guarantees convergence.

## 3. Exact evaluation of \(Q_N\)

Expanding (5) and applying (7), define

\[
\begin{aligned}
M_0&=M(2\nu+6;\nu,\nu),\\
M_1&=M(2\nu+7;\nu,\nu-1),\\
M_2&=M(2\nu+8;\nu-1,\nu-1).
\end{aligned}
\]

The convergence condition in (7) holds for every integer \(N\geq1\),
including \(\nu=-1/2\) when \(N=1\).  Direct substitution of
\(\nu=N-3/2\) in (7), followed only by
\(\Gamma(x+1)=x\Gamma(x)\), gives, with

\[
S_N:=2^{2N-1}\Gamma(N+3/2)^2,
\]

the three values

\[
M_0=\frac{S_N}{N(N+1)(2N+1)},
\qquad M_1=3M_0,
\qquad
M_2=\frac{6(2N+3)}{N+2}M_0.
\tag{8}
\]

Hence

\[
\begin{aligned}
Q_N
&=\frac{c_N^2}{4}(9M_0-6M_1+M_2)\\
&=\frac{2^{-2N-3}}{\pi^3\Gamma(N)^2}
 \frac{3S_N}{(N+1)(N+2)(2N+1)}\\
&=\frac{3\Gamma(N+3/2)^2}
 {16\pi^3(N+1)(N+2)(2N+1)\Gamma(N)^2}.
\end{aligned}
\tag{9}
\]

In the second line, the cancellation is

\[
9M_0-6M_1+M_2
=M_0\left(-9+\frac{6(2N+3)}{N+2}\right)
=\frac{3N}{N+2}M_0.
\]

This also proves convergence of every integral used in (6).

## 4. Exterior spatial integral and limit

Using (1), (6), and (9),

\[
\begin{aligned}
I_N(m,\kappa)
&=4\pi\int_R^\infty r^2\frac{2m^2Q_N}{r^6}\,dr
=\frac{8\pi m^2Q_N}{3R^3}\\
&=\kappa m\,\frac{32\pi^2}{9}Q_N\\
&=\kappa m\,
\frac{2\Gamma(N+3/2)^2}
 {3\pi(N+1)(N+2)(2N+1)\Gamma(N)^2}.
\end{aligned}
\tag{10}
\]

Thus the proposed identity holds for every integer \(N\geq1\).  Finally,
\(\Gamma(N+3/2)/\Gamma(N)\sim N^{3/2}\) and
\((N+1)(N+2)(2N+1)\sim2N^3\), so (10) also gives

\[
\lim_{N\to\infty}\frac{I_N(m,\kappa)}{\kappa m}=\frac1{3\pi}.
\]

No unproved mathematical step remains in this argument.
