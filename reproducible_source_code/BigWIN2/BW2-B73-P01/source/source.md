# win-00073-p01 — Exact one-atom Abel-power square function in dimension three

Work on `R^3` with heat semigroup `H_t=exp(t Delta)` and Abel mean
`A_s=s(s-Delta)^{-1}`.  For `N>=1`, let `A_s^N` denote N-fold composition.
Fix `m,kappa>0`, put `nu=m delta_0`, and let `Omega` be the cap-kappa
Laplacian partial-balayage domain of `nu`; in this radial case `Omega` is the
centered ball of volume `m/kappa`.

Prove or disprove, for every integer `N>=1`,

`int_{Omega^c} int_0^infty |s partial_s(A_s^N nu)(x)|^2 ds/s dx`

`= kappa*m * 2*Gamma(N+3/2)^2 /
   (3*pi*(N+1)*(N+2)*(2*N+1)*Gamma(N)^2)`.

If true, also prove that the normalized expression tends to `1/(3*pi)`.
All Fourier-transform, Laplacian, resolvent-kernel, and partial-balayage
normalizations must be explicit.  The first falsification gate is the exact
case `N=1`, whose proposed normalized value is `1/48`.

Primary source: Daniel Spector and Cody B. Stockdale, *The weak-type (1,1)
bound for the Hardy--Littlewood maximal function is O(sqrt(n) log n)*,
arXiv:2609.05377v1, equations (1.10)--(1.11), Theorem 1.3 and surrounding
discussion: https://arxiv.org/abs/2609.05377v1 .  The displayed closed form is
a supervisor-generated candidate, not a claim made by the source.
