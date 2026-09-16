# Fresh mathematical referee report

## Verdict

**Accept.** The frozen `resolution-paper` claim proves the original identity in
its full stated scope (all (m,κ>0) and all integers (N\geq1)), with the
specified Fourier, Laplacian, resolvent, Abel-power, and partial-balayage
normalizations. The limiting constant follows from the proved formula. I found
no mathematical gap requiring a change of scope or statement.

## Frozen scope and integrity

I reviewed the statement in `source.md`, its precise reading in `problem.md`,
`claim.json`, snapshot digest
`d45fcb7c5650dd0813cf983a7a09999aa5cb3852cd9f976ff3d0de93e478e261`,
and every file enumerated by that snapshot. I recomputed all seven file hashes;
each agrees with `audit/snapshot.json`. I also recomputed the canonical digest
of the snapshot's `files` mapping and obtained the displayed digest. In
particular, the frozen source hash remains
`e687bbc592fb1cf50f153019a1455938757572d27099d1f4d58d66e68c8ff3c3`.

The claim is equivalent to the original question, rather than a restricted or
weakened version: the exterior is the complement of the centered ball with
(R^3=3m/(4\pi\kappa)), and the asserted equality is quantified over exactly
the requested parameters. Inclusion of the null boundary is immaterial.

## Reconstruction of the decisive argument

For (r=|x|>0), the heat-kernel Laplace representation gives

\[
(s-\Delta)^{-N}\delta_0(r)=\frac{1}{(4\pi)^{3/2}\Gamma(N)}
 \int_0^\infty t^{N-5/2}e^{-st-r^2/(4t)}\,dt.
\]

With (z=r\sqrt{s}), ν=(N-3/2), and

\[
c_N=\frac{2^{-\nu-2}}{\pi^{3/2}\Gamma(N)},
\]

this yields

\[
A_s^N\delta_0(r)=s^{3/2}c_Nz^\nu K_\nu(z).
\]

Using
(\frac d{dz}(z^\nu K_\nu)=-z^\nu K_{\nu-1}) and
(s\partial_s z=z/2), I recover

\[
s\partial_s(A_s^N\delta_0)(r)=s^{3/2}G_N(z),\qquad
G_N(z)=\frac{c_N}{2}z^\nu
       \bigl(3K_\nu(z)-zK_{\nu-1}(z)\bigr).
\]

Consequently the (s)-integral separates exactly as

\[
\int_0^\infty|s\partial_s(A_s^N(m\delta_0))(r)|^2\frac{ds}{s}
=\frac{2m^2}{r^6}Q_N,
\qquad Q_N=\int_0^\infty z^5G_N(z)^2\,dz.
\]

I independently substituted the standard product integral for two modified
Bessel functions into the three terms of this square. Setting
(S_N=2^{2N-1}\Gamma(N+3/2)^2), the required moments are

\[
M_0=\frac{S_N}{N(N+1)(2N+1)},\qquad
M_1=3M_0,\qquad
M_2=\frac{6(2N+3)}{N+2}M_0.
\]

Thus

\[
9M_0-6M_1+M_2=\frac{3N}{N+2}M_0
\]

and, after inserting (c_N^2/4),

\[
Q_N=\frac{3\Gamma(N+3/2)^2}
 {16\pi^3(N+1)(N+2)(2N+1)\Gamma(N)^2}.
\]

The final radial integration is then

\[
I_N=4\pi\int_R^\infty r^2\frac{2m^2Q_N}{r^6}\,dr
=\frac{8\pi m^2Q_N}{3R^3}
=\kappa m\frac{32\pi^2}{9}Q_N,
\]

which is precisely the claimed expression. Finally,
(\Gamma(N+3/2)/\Gamma(N)\sim N^{3/2}) and the denominator polynomial is
asymptotic to (2N^3), giving (I_N/(\kappa m)\to1/(3\pi)).

## Adversarial checks performed

- **Endpoint and exceptional-index check.** The potentially delicate case is
  (N=1), where ν=(-1/2). For each of the three product moments, the
  hypothesis ρ>∣α∣+∣β∣ still holds strictly, so the proof does not
  use an invalid endpoint continuation. All Gamma arguments are positive.
  Exponential decay handles infinity. Thus the separate moment evaluations,
  not merely their combination, converge for every claimed (N).
- **Constants and quantifiers.** I rederived the factors (s^{3/2}),
  (ds/s=2\,dz/z), (2m^2/r^6),
  (\int_R^\infty r^{-4}dr=1/(3R^3)), and
  (R^{-3}=4\pi\kappa/(3m)). This rules out the most likely Fourier,
  radial-measure, mass-scaling, and balayage-radius errors. The calculation is
  pointwise only for (r>0), exactly where it is used since (R>0); no
  differentiation of the singular kernel at the atom is needed.
- **Exact finite check.** I ran the frozen rational-arithmetic verifier. Its
  independent half-integer exponential-polynomial expansion agrees with the
  claimed Gamma quotient for every (1\leq N\leq30), including the required
  gate (I_1/(\kappa m)=1/48).
- **Direct numerical check.** I separately integrated the Bessel expression at
  60-digit precision for (N=1,2,3,4,7,12). The normalized values agreed with
  the claimed values to at least 60 decimal digits (for example (1/48),
  (5/128), and (105/2048) for (N=1,2,3)). This is corroboration only;
  the verdict rests on the exact derivation above.
- **Degenerate-domain check.** The hypotheses (m,κ>0) imply a finite,
  strictly positive radius. Hence there is no empty domain, zero-radius
  singularity, or division by zero within the frozen scope.

## Source comparison and contribution

The frozen source-check evidence identifies Spector--Stockdale,
arXiv:2609.05377v1, equations (1.10)--(1.11) and Theorem 1.3, as using the
same Abel square function while proving only a general upper bound
(I_N\lesssim\sqrt N\,\kappa m) for positive atomic measures in dimensions
(n\geq3). It also explicitly records that the exact formula is
supervisor-generated and is not attributed to that paper. Thus the submitted
scope honestly presents an exact one-atom, three-dimensional resolution and
makes no unsupported priority claim. Within the frozen evidence set, this is
a concrete and nontrivial delta from the cited general estimate.

There are no unresolved mathematical gaps in the frozen resolution claim.
The bounded literature search is appropriately described as limited and is
not used as proof of novelty.
