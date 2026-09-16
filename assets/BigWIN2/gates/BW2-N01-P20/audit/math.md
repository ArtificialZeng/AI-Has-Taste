# Mathematical referee report

**Verdict: accept the exact frozen candidate.**

Referee job: `newwin-00001-p20-referee-385d4a10a625`.
Date: 2026-09-12.
Snapshot digest: `cf7630d6bb75637ad046c973a80a87165a82712e35b2590de9570c5fd83fbf73`.
Frozen kind: `resolution-paper`. Frozen original status: `proved`.

The accepted statement is exactly `claim.json`, including the explicit
constants in the submitted proof. It resolves the user's entire fixed-window
problem in `source.md`: every fixed real A>0, every sufficiently large integer
m, and every real |x|<=A, including x depending on m and all floor jumps.
No subsidiary theorem or weaker scope is substituted.

With x_+=max(x,0), the accepted coefficients are

\[
H(x)=\frac{\sqrt\pi}{2}e^{x^2}\operatorname{erfc}(|x|),\qquad
F_0(x)=H(x)+2x_+,
\]
\[
F_1(x,\delta)=(2\delta+1)xH(x)+\delta+1-2x_+^2,
\qquad -1<\delta\le0.
\]

## Inputs and independence of this pass

The reviewed project inputs were `source.md`, `problem.md`, `claim.json`,
`audit/snapshot.json`, and the evidence files enumerated by that snapshot:
the submitted proof, verification record, checker and its output, literature
comparison, the Insko--Johnson--Sullivan PDF, and the Hiveley--Zeilberger HTML.
I did not use checkpoint/state files, owner progress summaries, earlier job
transcripts, or prior audit decisions. Assertions of correctness appearing
inside the required inputs were not treated as evidence of correctness.
This report records a fresh model review pass, not outside peer review or
statistically independent evidence.

All ten frozen file hashes agree with the snapshot. I also recomputed the
snapshot digest from its sorted-key, compact JSON file mapping. The immutable
source has SHA256
`b5dd0cb2ff5644a13c42b0b0e352a6a172be7c766f45a41ad37d89c83c4af495`.
The integrity record is `audit/referee-integrity.json`. No frozen input was
edited. The role reference and the complete release contract were read;
the four-field mathematical audit JSON follows that contract.

## Reconstruction and attacks on the argument

1. **Exact branches and endpoints.** Write h=m^(-1/2), d=k-m and y=dh.
   For p_j=2^(-(2m-1)) binom(2m-1,m+j) and
   q_j=4^(-m) binom(2m,m+j), factorial cancellation gives
   p_j=(1-j/m)q_j and p_j=p_(-j-1). The odd binomial midpoint implies
   S_(-1)=1/2. Reflection at the correct endpoint gives
   S_(-d-2)=1-S_d, rather than a tail including the atom at d. Thus

   \[
   E_{m,m+d}=\begin{cases}
   S_d/p_d,&d<0,\\
   (1-S_d)/p_d+2m(d+1)/(m+d+1),&d\ge0.
   \end{cases}
   \]

   The empty upper tail at k=2m-1 is consistent with this identity. All
   binomial denominators are positive. The final asymptotic range lies
   strictly inside the support; no endpoint convention is used to mask a
   zero denominator.

2. **Local mass estimate and its constants.** The three Wallis integrals
   in proof equation (8) have the stated factorial values. Monotonicity in
   their exponents gives
   1/sqrt(pi(m+1/2)) <= q_0 <= 1/sqrt(pi m), hence logarithmic central
   error at most 1/(4m). For r=|j|, expanding each factor of

   \[
   q_r/q_0=\prod_{\ell=1}^{r}
       \frac{1-(\ell-1)/m}{1+\ell/m}
   \]

   gives linear sum -r^2/m, quadratic sum r^2/(2m^2), and absolute
   remaining error at most r^2(r^2+1)/(3m^3). In particular, the sum of
   the two cubic powers in the proof is r^2(r^2+1)/2. These calculations
   verify equation (9), including its signs. With
   K=1/4+5B^2/6+B^4/3 and
   M=ceil(max(4,4B^2,K)), all logarithm arguments have absolute value
   at most 1/2 and the logarithmic error is at most K/m<=1.
   Multiplication by 1-j/m yields

   \[
   p_j=hf(jh)(1-jh^2+\rho_j),\quad
   |\rho_j|\le Lh^2,\quad p_j/(hf(jh))\ge1/(2e),
   \]

   where f(t)=exp(-t^2)/sqrt(pi) and L=3eK/2. Thus both the relative
   remainder and the quantitative lower bound in (7) are justified.

3. **Signed summation, including the two central cells.** For d<0,
   the signed sum in (4) excludes both endpoints of [dh,0]. Negating
   the usual trapezoidal sum on that interval and restoring its two
   endpoint half-weights gives exactly equation (10), with the same
   positive endpoint correction as for d>=0. The one-interval case
   d=-1 and the zero-length case d=0 are covered. The integrated
   interpolation error is bounded by |y|h^2 sup|g''|/12.

   There are at most B/h+1 mass terms; their O(h^3) absolute errors
   therefore sum to the stated O(h^2) bound. Applying the trapezoidal
   inequality separately to f and t f(t), and using
   integral_0^y t f(t) dt=(f(0)-f(y))/2, gives

   \[
   S_d=P(y)+hf(y)+\varepsilon_d,\qquad
   |\varepsilon_d|\le Dh^2.
   \]

   I checked every term of D in (11): the accumulated local errors,
   the f quadrature error, the t f endpoint term, and its quadrature
   error (using h<=1). This avoids an unproved approximation to a
   remote tail. The Gaussian integral establishes 0<=P<=1.

4. **Division and the upper rational term.** For
   z=1-yh+rho, the identity

   \[
   z^{-1}-1-yh=\frac{y^2h^2-\rho(1+yh)}{z}
   \]

   is exact. The lower bound for z and |yh|<=1/2 give the stated
   J=2e(B^2+3L/2). Since f(y)>=a=exp(-B^2)/sqrt(pi), the terms
   J/a, B+J, and 2eD/a account for all of Q in (13). The signs of
   the constant terms are +1 for S_d/p_d and -1 for (1-S_d)/p_d.
   There is no missing error of order one from division.

   With v=y+h>=0, exact polynomial division of 2v/[h(1+hv)] gives
   2y/h+2-2y^2 plus
   -4yh-2h^2+2h(y+h)^3/[1+h(y+h)]. Its absolute value is at most
   (4B+2+2(B+1)^3)h=Th. Combining the two branches therefore proves
   equation (17) with V(y)=yH(y)+1-2y_+^2 and error (Q+T)h.

5. **Smoothness, the floor, and quantifiers.** Although H has a corner,
   F_0'(x)=2xH(x)+1 on both sides, including at zero. Differentiating
   this expression shows F_0''(0)=sqrt(pi) and continuity of F_0''.
   Also V'(0)=sqrt(pi)/2, with V' continuous. The estimates H<=b,
   |H'|<=2Bb+1 away from zero, with b=sqrt(pi)/2, give exactly the
   U and W bounds in (18). No differentiability of H at zero is
   assumed.

   Set B=A+1, take M_A=M above, and write
   y=x+delta h for the actual delta=floor(x/h)-x/h in (-1,0].
   Then |y|<=B and |d|<=B sqrt(m)<=m/2. As m>=4,
   0<=m+d<=2m-1. Taylor's theorem on the interval between x and y
   gives an error at most Uh/2 in the leading term; the V error is
   at most Wh. Finally V(x)+delta F_0'(x) is exactly the submitted
   F_1. Thus the claimed explicit C_A=Q+T+U/2+W works for every
   allowed real x with the same M_A and C_A. This proves the full
   uniform remainder, rather than just a fixed-x assertion.

As additional central checks, direct algebra gives
E_(m,m-1)=1/(2q_0) and
E_(m,m)-E_(m,m-1)=(m-1)/(m+1). At x=0 the displayed coefficients
are F_0(0)=sqrt(pi)/2 and F_1(0,0)=1. On approaching zero from the
negative cell, delta approaches -1; the floor correction supplies the
different constant term. More generally the limiting change of F_1
across a floor reset is F_0'(x), as required by the discrete expansion.

## Independent finite verification

I wrote and ran `audit/referee-check.py`; it neither imports nor executes
the proposer checker. The output is `audit/referee-checks.json` and records
the verifier hash, the frozen input digest, environment versions, coverage,
and numerical maxima. Reproduce it from the project root with
`python3 audit/referee-check.py > audit/referee-checks.json`.

The exact checks passed:

- Directly simulated every binary arrival sequence for m=1,...,9:
  174,762 sequences and 90 fixed-red-count classes. The accumulated gap
  in each class equals the original numerator, using capacity blocking
  rather than the binomial reflection formula to perform the simulation.
- Checked the exact branch reduction for all admissible k at m=1,...,64:
  4,160 cases, plus 64 exact central-jump checks.
- Checked the signed quadrature inequality in exact rational arithmetic
  for 567 cases: h=2/7,3/11,5/13; d=-13,...,13; and monomials of
  degrees 0 through 6.

At 80 decimal digits, 1,939 local-mass/CDF checks and 7,735 full
expansion checks passed. Windows were A=1/16,3/4,2,4; capacities were
the values in {M_A,M_A+1,3M_A,64,311,1024} satisfying m>=M_A.
All integer cells intersecting each window were visited at the listed
six phases, when the resulting point belonged to that window. Points
were specified as x=(d+theta)/sqrt(m) with rational theta, so window
membership and the floor index were checked exactly. The phases include
0, 10^(-30), 1/(m^2+1), 1/2, 1-1/(m^2+1), and 1-10^(-30).
The expectation numerator and denominator were computed as integers
from the original definition; H was evaluated through the upper
incomplete gamma function.

These are finite consistency checks, and the special-function evaluations
are not interval certificates. They neither exhaust real floor cells nor
prove the asymptotic theorem. Acceptance rests on the analytic inequalities
reconstructed above, not on the number of passing numerical tests.

## Primary-source comparison and contribution

The nearest prior result is Insko, Johnson and Sullivan,
*A Combinatorial Model for Lane Merging: Limited Capacity Lanes*, ECA
6:2 (2026), S2R9, DOI 10.54550/ECA2026V6S2R9. I inspected Corollary
7.2 and section 8 question 2 on printed pages 11--12 of the frozen
[primary PDF](https://ecajournal.haifa.ac.il/Volume2026/ECA2026_S2A9.pdf).
The corollary gives the exact expectation and bounds; symmetry removes
the subtracted endpoint binomial coefficient from its upper-branch sum,
giving exactly `source.md`. It also gives the exact central value.
Question 2 requests improved approximations near k=m. The accepted
delta is the explicit two-term expansion throughout every bounded
central window, with its lattice term and uniform absolute error.
It makes that published approximation request precise in the manner
frozen by the user. A live publisher-PDF fetch timed out; the actual
frozen primary PDF, not a search snippet, supplied this comparison.

I also inspected the introduction, Theorem 1, sections 6--7 and references
of the frozen and live [Hiveley--Zeilberger v1
paper](https://arxiv.org/html/2607.26334v1). Its object is multi-lane
end-state enumeration without this capacity and fixed-red-count
conditioning. The inspected statements do not give the submitted
central-window expansion. In the live [Bardenova--Insko--Johnson--Sullivan
JIS paper](https://cs.uwaterloo.ca/journals/JIS/VOL26/Insko/insko5.pdf),
Lemma 25 and Corollary 26 on printed pages 19--20 concern a fixed-ratio
unrestricted-lane limit; Open Problem 39 on page 28 separately poses
the capacity-gap expectation. Those statements do not supply this
uniform two-term result either.

Fresh search queries on 2026-09-12 were:

- `"A Combinatorial Model for Lane Merging" "Limited Capacity" approximation`
- `"lane merging" "erfc"`
- `"lane merging" "central window"`
- `"Insko" "Johnson" "Sullivan" "uniform" "gap"`
- `"limited capacity lanes" asymptotics approximation -site:researchgate.net`
- `"lane merging" "continuity correction"`

The search produced no verified equivalent result in the inspected primary
material. This is a bounded screen, not proof of priority or exhaustive
current open status. A later publisher revision was not checked successfully.
No conclusion is drawn from a fetch failure. The claim already states
these limits and does not assert a new general asymptotic method.

The contribution passes at its stated scope: a modest but concrete full
solution of the frozen approximation problem, giving both computable
coefficients and an error estimate in the central range where the nearest
paper requests improvement. It is not the already-known single central
value, a fitted curve, or an arbitrary restricted subcase. Wallis bounds,
binomial approximations and quadrature are classical; the accepted value
is this specific application. No journal-acceptance prediction is made.

## Gaps, limits, and handoff

No material mathematical gap or required scope revision was found. The
explicit constants are conservative; optimization is not part of the
frozen claim. No growing-window theorem, optimal remainder, or exhaustive
novelty claim is accepted. Those omissions do not weaken the stated target.

The decision is **accept**, with the original `resolution-paper` / `proved`
fields retained. The runner should run `check-math` against this unchanged
snapshot before dispatching the manuscript phase. This referee pass has
created no manuscript or publication PDF.
