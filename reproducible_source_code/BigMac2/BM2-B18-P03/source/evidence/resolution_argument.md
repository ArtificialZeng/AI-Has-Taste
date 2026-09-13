# Resolution argument: the endpoint remainder has order \(u^{3/2}\)

## Claim and conventions

Let \(S_u,\lambda(u),\Phi(u)\) be exactly as frozen in `source.md` and
interpreted in `problem.md`.  Put

\[
  \kappa:=\frac{\pi}{2},\qquad A:=\kappa^2=\frac{\pi^2}{4},\qquad
  R(u):=\Phi(u)+Au.
\]

There are constants \(c,C,u_0>0\), independent of \(u\), such that

\[
             c u^{3/2}\le R(u)\le C u^{3/2}
             \qquad(0<u<u_0).                              \tag{1}
\]

Consequently

\[
 \frac{2[\Phi(u)+Au]}{u^2}\longrightarrow +\infty,         \tag{2}
\]

so the finite classical right second derivative specified in `(Q)` of
`problem.md` does not exist.  The correct pure-power scale of the signed
first-order remainder is \(u^{3/2}\).  No exact leading coefficient for the
*optimized* eigenvalue is asserted.

The proof below uses the Fourier transform
\(\widehat f(\xi)=\int_{\mathbb R}e^{-ip\xi}f(p)\,dp\), so that Plancherel has
the factor \(1/(2\pi)\).

## 1. A trial quotient with a uniform remainder

Extend

\[
 f_1(p)=\cos(\kappa p),\qquad -1\le p\le1,
\]

by zero to \(\mathbb R\).  It has norm one, belongs to
\(H^1(\mathbb R)\), and

\[
 \widehat f_1(\xi)
 =\frac{2\kappa\cos\xi}{\kappa^2-\xi^2},                  \tag{3}
\]

with the values at \(\xi=\pm\kappa\) understood by continuity.  Hence its
Rayleigh quotient is

\[
 q(u):=\langle f_1,S_uf_1\rangle
 =\frac1{2\pi}\int_{\mathbb R}e^{-u\xi^2}
       |\widehat f_1(\xi)|^2\,d\xi .                       \tag{4}
\]

Moreover,

\[
 \frac1{2\pi}\int_{\mathbb R}\xi^2|\widehat f_1(\xi)|^2d\xi
 =\|f_1'\|_2^2=\kappa^2=A.                                \tag{5}
\]

Define \(h(s)=e^{-s}-1+s\).  Equations (4)--(5) give

\[
 q(u)-1+Au=\int_{\mathbb R}h(u\xi^2)w(\xi)\,d\xi,
 \quad
 w(\xi)=\frac{2\kappa^2}{\pi}
         \frac{\cos^2\xi}{(\xi^2-\kappa^2)^2}.            \tag{6}
\]

The following calculation includes the required uniform error estimate.  Put
\(B=2\kappa^2/\pi\) and

\[
 r(\xi):=B\cos^2\xi
 \left(\frac1{(\xi^2-\kappa^2)^2}-\frac1{\xi^4}\right).
\]

Although \(r\) itself has a fourth-order singularity at zero, the function
\(\xi^4r(\xi)\) has removable singularities at
\(0,\pm\kappa\), is bounded on compact sets, and is \(O(\xi^{-2})\) at
infinity.  Thus

\[
 J:=\int_{\mathbb R}|\xi^4r(\xi)|\,d\xi<\infty.            \tag{7}
\]

Since \(0\le h(s)\le s^2/2\) for \(s\ge0\), (7) yields the all-\(u\) bound

\[
 \left|\int_{\mathbb R}h(u\xi^2)r(\xi)d\xi\right|
 \le \frac J2u^2.                                         \tag{8}
\]

For the leading tail, split \(\cos^2\xi=(1+\cos2\xi)/2\).  Direct scaling
and two elementary integrations by parts give

\[
 \begin{aligned}
 \int_{\mathbb R}\frac{h(u\xi^2)}{\xi^4}d\xi
 &=u^{3/2}\int_{\mathbb R}
       \frac{e^{-t^2}-1+t^2}{t^4}dt,\\
 \int_{\mathbb R}\frac{e^{-t^2}-1+t^2}{t^4}dt
 &=\frac{4\sqrt\pi}{3}.                                   \tag{9}
 \end{aligned}
\]

For completeness, on \((0,\infty)\) the first integration by parts reduces
the last integral to
\((2/3)\int_0^\infty(1-e^{-t^2})t^{-2}dt\), and the second integral equals
\(\sqrt\pi\); doubling gives (9).  All boundary terms vanish by the
expansions at zero and infinity.

The oscillatory half is uniformly smaller.  Set

\[
 g(t)=\begin{cases}
 (e^{-t^2}-1+t^2)/t^4,&t\ne0,\\[2mm]
 1/2,&t=0.
 \end{cases}
\]

Here \(g'(t)=O(t)\) at zero and \(g'(t)=O(t^{-3})\) at infinity, so
\(g'\in L^1(\mathbb R)\).  After scaling and one integration by parts,

\[
 \begin{aligned}
 \left|\int_{\mathbb R}\frac{h(u\xi^2)}{\xi^4}
          \cos(2\xi)d\xi\right|
 &=u^{3/2}\left|\int_{\mathbb R}g(t)
          \cos(2t/\sqrt u)dt\right|\\
 &\le \frac12\|g'\|_1u^2.                                \tag{10}
 \end{aligned}
\]

Combining (6)--(10), with constants that do not depend on \(u\), proves

\[
 q(u)=1-Au+\frac{4A}{3\sqrt\pi}u^{3/2}+E_q(u),
 \qquad |E_q(u)|\le M u^2.                                \tag{11}
\]

In particular, after decreasing a fixed \(u_1>0\) if necessary, the standard
uniform estimate for \(\log(1+z)-z\) turns (11) into

\[
 \log q(u)=-Au+\frac{4A}{3\sqrt\pi}u^{3/2}+E_{\log}(u),
 \qquad |E_{\log}(u)|\le M_1u^2
 \quad(0<u<u_1).                                          \tag{12}
\]

Because \(\lambda(u)\ge q(u)\) and logarithm is increasing, (12) implies,
for all sufficiently small \(u\),

\[
 R(u)\ge \frac{2A}{3\sqrt\pi}u^{3/2}.                    \tag{13}
\]

## 2. A matching upper bound from a solvable comparison operator

For every \(x\ge0\),

\[
                 e^{-x}\le\frac1{1+x},                    \tag{14}
\]

because \(e^x\ge1+x\).  Fourier quadratic forms therefore give

\[
                 S_u\le T_u,                              \tag{15}
\]

where \(T_u\) is the integral operator on \([-1,1]\) with kernel

\[
 T_u(p,q)=\frac{e^{-|p-q|/\sqrt u}}{2\sqrt u};             \tag{16}
\]

indeed (16) is the whole-line convolution kernel of the multiplier
\((1+u\xi^2)^{-1}\).  Thus \(\lambda(u)\le\rho(u)\), where \(\rho(u)\)
is the top eigenvalue of \(T_u\).

This comparison eigenvalue is explicit.  Write \(\varepsilon=\sqrt u\).
If \(T_uf=\rho f\), applying \(1-\varepsilon^2d^2/dp^2\) in the open
interval and differentiating (16) at the endpoints gives

\[
 -f''=k^2f,\qquad
 f'(-1)=\frac1\varepsilon f(-1),\quad
 f'(1)=-\frac1\varepsilon f(1),
 \qquad
 k^2=\frac{1-\rho}{\varepsilon^2\rho}.                    \tag{17}
\]

The strictly positive top eigenfunction is even (reflection commutes with
the positivity-improving operator), hence is proportional to \(\cos(kp)\).
Positivity forces \(0<k<\kappa\), and (17) becomes

\[
 k\tan k=\frac1\varepsilon,
 \qquad
 \rho(u)=\frac1{1+uk^2}.                                  \tag{18}
\]

The left side of the first equation in (18) is strictly increasing from zero
to infinity on \((0,\kappa)\), so this root is unique and does give the top
eigenvalue.

Let \(\delta=\kappa-k\).  Equation (18) is equivalently

\[
 \tan\delta=\varepsilon(\kappa-\delta)=\varepsilon k,
\]

and therefore

\[
 0<\delta\le\varepsilon k\le\kappa\varepsilon.            \tag{19}
\]

Using \(0\le x-\log(1+x)\le x^2/2\) for \(x\ge0\), (18)--(19) imply, for
\(0<u\le1\),

\[
\begin{aligned}
 R(u)&\le \log\rho(u)+Au\\
 &=u(A-k^2)+\{uk^2-\log(1+uk^2)\}\\
 &\le 2A u^{3/2}+\frac{A^2}{2}u^2\\
 &\le\left(2A+\frac{A^2}{2}\right)u^{3/2}.                \tag{20}
\end{aligned}
\]

Equations (13) and (20) prove (1).

## 3. Endpoint consequence and scope

Equation (13) implies (2) directly.  If the finite classical limit

\[
 \lim_{u\downarrow0}\frac{\Phi'(u)+A}{u}=L
\]

existed, integration of \(\Phi'(u)+A=Lu+o(u)\) from the endpoint would give
\(R(u)=(L/2)u^2+o(u^2)\), contradicting (2).  Hence that finite limit does
not exist.

The result settles the frozen decision problem and proves the requested
matching scale bounds.  It does **not** identify a limit of
\(R(u)/u^{3/2}\), nor does it assert bibliographic priority or a complete
literature classification.  The proof dependencies are only Plancherel's
theorem, the Rayleigh variational principle, elementary Fourier calculus, and
the explicitly solved Robin problem above.  Known proof gaps: none.

