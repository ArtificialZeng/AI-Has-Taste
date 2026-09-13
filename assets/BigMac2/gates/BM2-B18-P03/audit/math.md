# Fresh mathematical referee report

## Provenance and frozen scope

- Referee job: `bigMac-00018-p03-referee-2ef1e7649fa6`.
- Frozen snapshot digest: `541d34c4cdaca83b4396c9302a0418af32ffe4cc1fedd99b0f6b17a06c273718`.
- Candidate: `resolution-paper`; proposed original status: `disproved`.
- Exact scope reviewed: for the Gaussian truncated heat-kernel operator in
  `source.md`, with (A=\pi^2/4) and
  (R(u)=\log\lambda(u)+Au), prove two-sided signed bounds
  (c u^{3/2}\le R(u)\le C u^{3/2}) for all sufficiently small (u>0),
  and use them to rule out a finite value of
  \(\lim_{u\downarrow0}(\Phi'(u)+A)/u\).

I recomputed the four frozen hashes. They agree with `audit/snapshot.json`:

| file | SHA-256 |
|---|---|
| `source.md` | `65c11a0f7088c13b0ff6a2702bde0bc8b6b2c3c5b4626a06f291d5cedda3b646` |
| `problem.md` | `267f8577d16f6906f43a5114c2631f2c692b21c2488ab5356b4978fbbdf58ec1` |
| `claim.json` | `ef899e397049803472bf49a1f197476f53d1541a57023567506282904a376ed4` |
| `evidence/resolution_argument.md` | `d59ea47fbf7e9a75f6a27f32cc77b03f321891c0fe29a5920cf9c73fbf60238d` |

## Reconstruction of the lower bound

Let \(\kappa=\pi/2\), so (A=\kappa^2), and extend
(f_1(p)=\cos(\kappa p)) by zero outside ([-1,1]). Direct integration gives

\[
 \|f_1\|_2=1,\qquad
 \widehat f_1(\xi)=\frac{2\kappa\cos\xi}{\kappa^2-\xi^2}.
\]

The apparent singularities at \(\xi=\pm\kappa\) are removable. Because the
zero extension vanishes continuously at both endpoints, it is in
(H^1(\mathbb R)), and Plancherel gives
((2\pi)^{-1}\int\xi^2|\widehat f_1|^2=A). Thus, for
(h(s)=e^{-s}-1+s\ge0), its Rayleigh quotient satisfies

\[
 q(u)-1+Au=\int_{\mathbb R}h(u\xi^2)
 \frac{2\kappa^2}{\pi}\frac{\cos^2\xi}{(\xi^2-\kappa^2)^2}\,d\xi.
\]

I checked the tail subtraction used in the evidence. If

\[
 r(\xi)=\frac{2\kappa^2}{\pi}\cos^2\xi
 \left((\xi^2-\kappa^2)^{-2}-\xi^{-4}\right),
\]

then \(\xi^4r(\xi)\) is bounded near zero, has removable singularities at
(\pm\kappa), and is (O(\xi^{-2})) at infinity. Hence
(J=\int|\xi^4r(\xi)|d\xi<\infty). The global elementary inequality
(0\le h(s)\le s^2/2) therefore yields a genuinely uniform (O(u^2))
error, not merely a formal expansion.

For the subtracted tail, scaling and integration by parts give

\[
 \int_{\mathbb R}\frac{h(u\xi^2)}{\xi^4}\,d\xi
 =\frac{4\sqrt\pi}{3}u^{3/2}.
\]

Writing \(\cos^2\xi=(1+\cos2\xi)/2\), the oscillatory part is (O(u^2)):
after scaling, (g(t)=(e^{-t^2}-1+t^2)/t^4) has (g'\in L^1\), and one
integration by parts supplies the extra factor \(\sqrt u\). The coefficient
is consequently

\[
 q(u)=1-Au+\frac{4A}{3\sqrt\pi}u^{3/2}+O(u^2),
\]

with an all-small-(u) remainder bound. Since (q(u)=1+O(u)), the logarithm
changes only the (O(u^2)) term. The variational inequality
(\lambda(u)\ge q(u)>0) then gives, after fixing one sufficiently small
(u_1>0),

\[
 R(u)\ge \frac{2A}{3\sqrt\pi}u^{3/2}\qquad(0<u<u_1).
\]

Every inequality here is signed; there is no conversion from numerical
evidence to a lower bound.

## Reconstruction of the upper bound

For zero extensions of functions on ([-1,1]), pointwise Fourier-multiplier
domination

\[
 e^{-u\xi^2}\le(1+u\xi^2)^{-1}
\]

proves quadratic-form domination (S_u\le T_u), where

\[
 T_u(p,q)=\frac{1}{2\sqrt u}e^{-|p-q|/\sqrt u}.
\]

Thus \(\lambda(u)\le\rho(u)\), the top eigenvalue of (T_u). I independently
checked the boundary reduction. With \(\varepsilon=\sqrt u\), applying
(1-\varepsilon^2d^2/dp^2) to an eigenfunction and differentiating the
kernel at the endpoints gives

\[
 -f''=k^2f,\quad f'(-1)=\varepsilon^{-1}f(-1),\quad
 f'(1)=-\varepsilon^{-1}f(1),\quad
 \rho=(1+uk^2)^{-1}.
\]

The multiplier is strictly below one almost everywhere away from zero, so
(0<\rho<1) and (k>0). Positivity improvement makes the top eigenfunction
unique, positive, and even. It is therefore proportional to \(\cos(kp)\),
with (0<k<\kappa), and

\[
 k\tan k=\varepsilon^{-1}.
\]

This equation has exactly one root in ((0,\kappa)). Setting
(\delta=\kappa-k) gives
(\tan\delta=\varepsilon k), hence
(0<\delta\le\varepsilon k\le\kappa\varepsilon). Therefore

\[
\begin{aligned}
 R(u)&\le -\log(1+uk^2)+Au\\
 &=u(A-k^2)+\{uk^2-\log(1+uk^2)\}\\
 &\le 2A u^{3/2}+\frac{A^2}{2}u^2.
\end{aligned}
\]

For (0<u\le1), this is at most
((2A+A^2/2)u^{3/2}). Together with the trial lower bound, it proves the
exact two-sided, all-small-(u), signed scale claimed.

As a non-probative arithmetic check, I also recomputed the trial quotient
directly from its compact-support autocorrelation. The scaled logarithmic
remainders at (u=10^{-3},3\cdot10^{-4},10^{-4}) were approximately
(1.856971,1.856375,1.856199), consistent with the independently calculated
trial coefficient (4A/(3\sqrt\pi)\approx1.856109). This check was not used
as proof.

## Endpoint implication and adversarial checks

The lower bound gives
(2R(u)/u^2\ge(4A/(3\sqrt\pi))u^{-1/2}\to+\infty). If the finite classical
limit in the frozen interpretation existed, say
((\Phi'(u)+A)/u\to L\), then integration from a positive lower endpoint and
passage to zero (using (R(u)\to0), already supplied by the two-sided bound)
would give (R(u)=(L/2)u^2+o(u^2)), a contradiction. This proves precisely
nonexistence of a *finite* classical right second derivative; it does not
claim a limit for the derivative quotient in the extended reals.

I specifically checked the following possible failure points:

- no zero denominator remains untreated in the Fourier calculation;
- the trial function is normalized and its zero extension really is in
  (H^1), while no unproved (H^2) assertion is used;
- all remainder constants are independent of (u) on a fixed punctured
  interval;
- the operator comparison is in Loewner quadratic-form order, which is the
  order needed for the top eigenvalues;
- the Robin root is the positive even ground state, rather than an arbitrary
  higher root;
- logarithms are applied only to positive quantities;
- divergence of the Peano quotient is used only to exclude a finite classical
  derivative, exactly as permitted by the frozen reading;
- neither an exact optimized (u^{3/2}) coefficient nor bibliographic
  priority is inferred.

## Source boundary, contribution, and verdict

Within the frozen evidence, `source.md` and `problem.md` identify the nearest
cited result as only
(\lambda(u)=1-(\pi^2/4)u+o(u)), with higher-order analysis left unresolved
there. The candidate proves substantially more: a uniform matching scale for
the optimized principal eigenvalue's logarithm and the resulting endpoint
nonregularity. The proof is self-contained apart from standard Plancherel,
Rayleigh, and elementary Green-kernel facts, and it does not make a broader
literature-priority claim. This is a nontrivial complete resolution of the
exact frozen problem, not a toy restriction or a subsidiary result.

**Verdict: accept.** Scope, mathematical correctness/evidence, and contribution
all pass. I found no gap requiring revision and made no substantive change to
the frozen claim or decisive evidence.
