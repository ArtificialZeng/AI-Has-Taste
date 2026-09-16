# Exact resolvent-power tests for \(N=2,3\)

Under the conventions frozen in `problem.md`, the heat representation gives,
for \(r=|x|>0\),

\[
(s-\Delta)^{-N}\delta _0(r)
=\frac{1}{(4\pi)^{3/2}\Gamma(N)}
 \int_0^\infty t^{N-5/2}e^{-st-r^2/(4t)}\,dt .
\tag{1}
\]

Writing \(z=r\sqrt{s}\) and multiplying (1) by \(s^N\),

\[
A_s^N\delta _0(r)=
\frac{s^{3/2}}{8\pi^{3/2}\Gamma(N)}
\int_0^\infty u^{N-5/2}e^{-u-z^2/(4u)}\,du.
\tag{2}
\]

Equivalently, the integral is
\(2(z/2)^{N-3/2}K_{N-3/2}(z)\).  The half-integer Bessel
values needed here yield

\[
A_s^2\delta _0(r)=\frac{s^{3/2}e^{-z}}{8\pi},
\qquad
A_s^3\delta _0(r)=\frac{s^{3/2}e^{-z}(1+z)}{32\pi}.
\tag{3}
\]

The input measure \(m\delta _0\) multiplies all displayed kernels and their
derivatives by \(m\).

## The case \(N=2\)

From (3),

\[
s\partial_s(A_s^2\delta _0)(r)
=\frac{s^{3/2}e^{-z}}{16\pi}(3-z).
\]

Since \(s=z^2/r^2\) and \(ds/s=2\,dz/z\),

\[
\int_0^\infty |s\partial_s(A_s^2(m\delta _0))(r)|^2\frac{ds}{s}
=\frac{m^2}{128\pi^2r^6}
 \int_0^\infty z^5e^{-2z}(3-z)^2\,dz
=\frac{45m^2}{2048\pi^2r^6},
\]

where the scalar integral is \(45/16\).  Radial integration over \(r\ge R\)
and \(R^3=3m/(4\pi\kappa)\) give

\[
I_2=4\pi\frac{45m^2}{2048\pi^2}
 \int_R^\infty r^{-4}\,dr
=\frac{5}{128}\,\kappa m.
\tag{4}
\]

Substitution of \(N=2\) into the proposed Gamma quotient also gives
\(5/128\).

## The case \(N=3\)

Again from (3),

\[
s\partial_s(A_s^3\delta _0)(r)
=\frac{s^{3/2}e^{-z}}{64\pi}(3+3z-z^2).
\]

Consequently,

\[
\int_0^\infty |s\partial_s(A_s^3(m\delta _0))(r)|^2\frac{ds}{s}
=\frac{m^2}{2048\pi^2r^6}
 \int_0^\infty z^5e^{-2z}(3+3z-z^2)^2\,dz
=\frac{945m^2}{32768\pi^2r^6},
\]

because the scalar integral is \(945/16\).  Thus

\[
I_3=4\pi\frac{945m^2}{32768\pi^2}
 \int_R^\infty r^{-4}\,dr
=\frac{105}{2048}\,\kappa m.
\tag{5}
\]

The proposed Gamma quotient at \(N=3\) is likewise \(105/2048\).

Equations (4)--(5) are exact special-case confirmations, not an all-\(N\)
proof.  Formula (2) reduces the remaining claim to an exact norm identity for
the half-integer Bessel kernel (or its finite exponential-polynomial form).
