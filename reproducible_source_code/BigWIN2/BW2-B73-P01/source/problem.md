# Precise reading

## Frozen source and conventions

The immutable statement is `source.md` (SHA-256
`e687bbc592fb1cf50f153019a1455938757572d27099d1f4d58d66e68c8ff3c3`).
Interpret `R^3` as Euclidean \(\mathbb R^3\), with Lebesgue measure \(dx\), and

\[
\Delta=\partial_1^2+\partial_2^2+\partial_3^2,
\qquad
\widehat f(\xi)=\int_{\mathbb R^3}e^{-2\pi i x\cdot\xi}f(x)\,dx.
\]

Thus \(\widehat{\Delta f}(\xi)=-4\pi^2|\xi|^2\widehat f(\xi)\),

\[
H_tf=e^{t\Delta}f=h_t*f,
\qquad h_t(x)=(4\pi t)^{-3/2}e^{-|x|^2/(4t)},
\]

and, for \(s>0\),

\[
A_s=s(s-\Delta)^{-1}=\int_0^\infty se^{-st}H_t\,dt.
\]

The resolvent and Abel kernels away from the origin are

\[
(s-\Delta)^{-1}\delta_0(x)=\frac{e^{-\sqrt{s}|x|}}{4\pi|x|},
\qquad
A_s\delta_0(x)=\frac{s e^{-\sqrt{s}|x|}}{4\pi|x|}.
\]

Here \(A_s^N\) means \(N\)-fold composition at the same value of \(s\); its
Fourier multiplier is

\[
\left(\frac{s}{s+4\pi^2|\xi|^2}\right)^N.
\]

All derivatives \(\partial_s\) are classical derivatives of the smooth
off-support kernel. The spatial integral is a Lebesgue integral, so whether
the boundary of the ball is included is immaterial.

## Balayage domain

Let \(m>0\), \(\kappa>0\), and \(\nu=m\delta_0\). Use the cap-\(\kappa\)
Laplacian partial-balayage convention

\[
\nu=\kappa\mathbf 1_\Omega\,dx-\Delta u,
\qquad u\ge 0,\qquad \Omega=\{u>0\}.
\]

In the radial one-atom case,

\[
\Omega=B(0,R),\qquad R=\left(\frac{3m}{4\pi\kappa}\right)^{1/3},
\qquad |\Omega|=\frac m\kappa.
\]

One compatible odometer is zero for \(|x|\ge R\), and for \(0<r=|x|<R\),

\[
u(r)=\frac{m}{4\pi r}+\frac{\kappa r^2}{6}-\frac{\kappa R^2}{2}.
\]

## Quantified claim

For every \(m>0\), every \(\kappa>0\), and every integer \(N\ge1\), define

\[
I_N(m,\kappa)=\int_{|x|\ge R}\int_0^\infty
 \left|s\partial_s(A_s^N(m\delta_0))(x)\right|^2\,\frac{ds}{s}\,dx.
\]

The claim to prove or disprove is

\[
I_N(m,\kappa)=\kappa m\,
\frac{2\Gamma(N+\tfrac32)^2}
{3\pi(N+1)(N+2)(2N+1)\Gamma(N)^2}.
\tag{C}
\]

The phrase “normalized expression” is read as \(I_N/(\kappa m)\). The
secondary claim is therefore

\[
\lim_{N\to\infty}\frac{I_N(m,\kappa)}{\kappa m}=\frac1{3\pi}.
\tag{L}
\]

If (C) is established, (L) follows from
\(\Gamma(N+3/2)/\Gamma(N)\sim N^{3/2}\). This reading does not assert that
the cited paper states (C): `source.md` expressly identifies (C) as a
supervisor-generated candidate.

## Nearest prior result and proposed delta

Spector--Stockdale, arXiv:2609.05377v1 (submitted 2026-09-04), equations
(1.10)--(1.11) and Theorem 1.3, defines the same Abel mean and proves for
general finite positive atomic measures in dimensions \(n\ge3\) only the
upper bound \(I_N\lesssim\sqrt N\,\kappa m\). The proposed delta is the exact
one-atom, dimension-three evaluation (C), including its limiting constant.
The verification route is explicit radial resolvent-power kernels followed by
exact Gamma/Beta integration. Exact-assertion searches performed on
2026-09-08 found no primary source stating (C); this is a limited search, not
a novelty or open-status certification.
