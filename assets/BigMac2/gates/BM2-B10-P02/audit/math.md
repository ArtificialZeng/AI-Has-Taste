# Fresh mathematical referee report

Referee job: `bigMac-00010-p02-referee-09e992174bab`  
Frozen snapshot: `36a1a4f0329030693dcac1a4882f04ade8a4069c4fc496cffbfd95c06e5949fb`

## Scope and verdict

I reviewed the exact `resolution-paper` claim frozen in `claim.json`: the
asynchronous with-replacement chain, the locally uniform boundary-layer limit,
the exact integral characterization of the sharp constant, and the complete
extended-half-line limit set of scaled maximizers.  I did not weaken the claim
to a pointwise asymptotic or a numerical assertion.

**Verdict: accept.**  The submitted argument proves the full frozen original
claim.  The Green-kernel normalization, limiting estimates, uniform control at
zero, tail control, and optimizer-tightness step are all valid.  I found no
unresolved mathematical gap in the accepted scope.

## Frozen-input integrity

I independently recomputed the SHA-256 digest of every file named in
`audit/snapshot.json`.  All four file hashes agree with the snapshot, and the
canonical digest of its sorted file mapping is exactly
`36a1a4f0329030693dcac1a4882f04ade8a4069c4fc496cffbfd95c06e5949fb`.
Thus this report addresses the frozen candidate rather than a changed version.

## Reconstruction of the decisive argument

Conditional on (S_t=s), the updating index and the three input indices are
independent uniform indices.  Their displayed bits are therefore independent
Bernoulli variables with parameter (p=s/N), even though index coincidences
are allowed.  This gives

\[
 \beta_s=p(1-p)(1+p-p^2),\qquad
 \delta_s=p(1-p)(1-p^2),
\]

and hence

\[
 r_s=\frac{\delta_s}{\beta_s}
 =\frac{1-p^2}{1+p-p^2}.
\]

With (q_1=1), (q_{k+1}=r_kq_k), and
(H_s=\sum_{k\le s}q_k), the increment of (H) is (q_s), so

\[
 \beta_s(H_{s+1}-H_s)+\delta_s(H_{s-1}-H_s)
 =\beta_sq_{s+1}-\delta_sq_s=0.
\]

Consequently the proposed Green column is zero at both absorbing boundaries
and harmonic away from its pole.  At (s=j), its generator is

\[
 -\frac{\beta_jH_jq_{j+1}+\delta_jQ_jq_j}
        {H_N\delta_jq_j}=-1,
\]

because (eta_jq_{j+1}=\delta_jq_j) and (H_j+Q_j=H_N).
This verifies the denominator in (6), including the effect of holding
probabilities, and summing the columns gives (7).

Writing (d_s=u_N(s)-u_N(s-1)), the Poisson equation gives

\[
 \frac{d_{s+1}}{q_{s+1}}=\frac{d_s}{q_s}-a_s,
 \qquad a_s=(\delta_sq_s)^{-1}.
\]

The boundary identity (sum_{s=1}^Nd_s=0) then yields (8).  Its
sign-controlling term
(F_N(s)=B_N(s)-A_N(s-1)) obeys the exact identity

\[
 F_N(s+1)-F_N(s)=-H_Na_s<0.
\]

Thus the finite sequence (u_N) is unimodal, allowing two adjacent tied
maximizers only.  This exact fact is what permits a complete maximizer result,
not merely convergence of values at fixed scaled states.

For (k=O(\sqrt N)), summing
(log r_k=-k/N+O(k^2/N^2)) gives

\[
 q_k=\exp\{-k(k-1)/(2N)+O(N^{-1/2})\}
\]

locally uniformly on that scale.  Globally,
(1-r(p)=p/(1+p-p^2)\ge4p/5), hence
(q_k\le\exp\{-2k(k-1)/(5N)\}).  These two estimates justify both
(H_{\lfloor x\sqrt N\rfloor}/\sqrt N\to\Phi(x)) locally uniformly and
(H_N/\sqrt N\to S).

The same local estimates give the Riemann limit for (A_N/N^{3/2}).  Near
zero, (H_j\le j), (delta_j\ge c j/N), and (q_j\ge c) on a fixed
boundary-layer window, so the omitted interval contributes (O(\varepsilon))
uniformly.  For the second Green sum, monotonicity of (r_j) gives

\[
 \frac{Q_j}{q_j}\le\frac{r_j}{1-r_j}=\frac{1-(j/N)^2}{j/N},
\]

and therefore

\[
 \frac{Q_j}{\delta_jq_j}
 \le \frac1{(j/N)^2(1-j/N)}
 =\frac Nj+\frac{N^2}{j^2}+\frac N{N-j}.
\]

Summation proves the stated (B_N) tail bound, whose normalized tail is
(O(1/L)+o(1)) beyond (L\sqrt N).  This supplies the uniform truncation
needed for (B_N/N^{3/2}\to B).  In (7) the second sum is (B_N(s+1)),
whereas (19) is written for (B_N(s)); on every scaled interval bounded away
from zero their difference is (Q_sa_s=O(N)=o(N^{3/2})).  The analogous
one-index shifts in (8) are also (o(N^{3/2})).  Thus this harmless shift does
not leave a gap.

At the zero endpoint, the submitted estimate (20) follows by bounding the
first Green sum by (CNs), the part of the second sum up to (sqrt N) by a
harmonic sum, and its remaining part by the global tail estimate.  Its
normalized upper bound is (Cz(1+\log(1/z))+o(1)), where
(z=s/\sqrt N), which vanishes uniformly as (z\downarrow0).  This completes
the claimed compact-uniform convergence on ([0,\infty)).

Finally, (A) is strictly increasing from zero to infinity, while (B) is
strictly decreasing from infinity to zero, so their crossing (x_*) is unique.
Differentiating the displayed formula for (U) cancels the two integral
derivative terms and gives

\[
 U'(x)=\frac{e^{-x^2/2}}S\{B(x)-A(x)\}.
\]

Hence (U) has the unique maximizer (x_*) and
(U(x_*)=A(x_*)=B(x_*)).  Local convergence of (F_N/N^{3/2}), together
with its exact strict decrease, places every finite-(N) maximizer between
((x_*-\varepsilon)\sqrt N) and
((x_*+\varepsilon)\sqrt N) for all sufficiently large (N).  This proves
optimizer tightness, convergence of every maximizing sequence, convergence of
the maxima, and exclusion of (+\infty) from the limit set.

## Independent computational checks

These checks support, but are not used as substitutes for, the proof.

- Direct finite tridiagonal Poisson solves and a separately evaluated Green
  sum agreed to numerical roundoff for (N=2,3,4,7,12); the largest absolute
  discrepancies were respectively (0), (4.44\times10^{-16}),
  (3.55\times10^{-15}), (8.35\times10^{-14}), and
  (2.78\times10^{-12}).
- Independent quadrature using the error-function forms gave
  (x_*=0.8631424109396626\) and
  (A(x_*)=B(x_*)=0.941499337310331\), agreeing with the orientation values in
  the evidence.
- Exact tridiagonal solves at (N=50{,}000,100{,}000,200{,}000) gave scaled
  maximizing locations (0.8988993,0.8886000,0.8832469) and normalized maxima
  (0.9844453,0.9738025,0.9657168), consistently approaching the stated
  limits from above.

## Scope, prior-result comparison, and edge cases

The frozen `source.md` and `problem.md` identify the nearest prior boundary as
an order estimate (M_N=\Theta(N^{3/2})).  The accepted result supplies the
strictly stronger sharp constant, a compact-uniform scaled profile, and the
full maximizer limit set.  Those are substantive rather than a toy restriction
or routine numerical refinement.  The cited primary PDF was not enumerated in
the frozen snapshot and therefore was outside the evidence this job was
permitted to inspect; accordingly this audit makes no independent literature-
priority finding.  That limitation does not affect the self-contained proof of
the frozen original statement, and the candidate itself expressly makes no
priority claim.

All denominators used in the finite formulas are positive for
(1\le s,j<N).  The proof treats (s=0) by continuous extension, permits the
only possible finite-(N) tie (two adjacent maximizers), controls both the
small-state and near-(N) tails, keeps time in asynchronous-update units, and
answers the extended-half-line question.  No division-by-zero, empty-domain,
limit/max interchange, or unaddressed equality-case defect remains.
