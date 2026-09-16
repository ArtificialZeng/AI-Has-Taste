# Exact first gate and source check

## The \(N=1\) calculation

For \(r=|x|>0\), the stated conventions give

\[
A_s(m\delta_0)(x)=\frac{m}{4\pi r}s e^{-r\sqrt{s}},
\qquad
s\partial_s A_s(m\delta_0)(x)
=\frac{m}{4\pi r}s e^{-r\sqrt{s}}
\left(1-\frac{r\sqrt{s}}2\right).
\]

With \(z=r\sqrt{s}\),

\[
\begin{aligned}
\int_0^\infty|s\partial_s A_s(m\delta_0)(x)|^2\frac{ds}{s}
&=\frac{m^2}{8\pi^2r^6}
  \int_0^\infty z^3e^{-2z}(1-z/2)^2\,dz\\
&=\frac{3m^2}{256\pi^2r^6},
\end{aligned}
\]

because the last scalar integral is \(3/32\). Therefore

\[
I_1=4\pi\frac{3m^2}{256\pi^2}\int_R^\infty r^{-4}\,dr
=\frac{m^2}{64\pi R^3}=\frac{\kappa m}{48},
\]

using \(R^3=3m/(4\pi\kappa)\). Substitution of \(N=1\) into the proposed
Gamma quotient also gives \(1/48\). Thus the required first falsification
gate passes exactly; this does not prove the all-\(N\) identity.

## Primary-source verification

Retrieved 2026-09-08:

- Daniel Spector and Cody B. Stockdale, *The weak-type (1,1) bound for the
  Hardy--Littlewood maximal function is \(O(\sqrt n\log n)\)*,
  arXiv:2609.05377v1, <https://arxiv.org/abs/2609.05377v1>.
- Page 2 gives \(H_t=e^{t\Delta}\) with
  \(h_t(x)=(4\pi t)^{-n/2}e^{-|x|^2/(4t)}\).
- Equations (1.10)--(1.11), on page 4 of the PDF, define
  \(A_s=s(s-\Delta)^{-1}=\int_0^\infty se^{-st}H_t\,dt\), its \(N\)-fold
  power, and the same exterior square function.
- Theorem 1.3, pages 4--5, proves only
  \(I_N\lesssim\sqrt N\,\kappa m\) for general finite positive atomic
  measures and \(n\ge3\); it does not state the displayed exact formula.

Searches for the exact title/formula language and equivalent Abel-power
square-function language returned no primary-source match beyond this nearest
paper. Search snippets were not treated as evidence, and absence of a match is
not a priority claim.
