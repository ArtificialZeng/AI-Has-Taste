# Mathematical referee report

Verdict: **accept** the exact frozen `result-note` claim, with
`original_status=unresolved`.

Referee job: `primary-20260913-fgn-positivity-referee-198603e6403d`.
Snapshot digest:
`799be9016a1551bc7a18ffc8ae8337eff2d67b706742436d3c0a6efa08931289`.
Review date: 2026-09-13, Asia/Shanghai.

The accepted statement is strict positivity of every one-sided coefficient
for every real $1/2<H<1$, every integer $2\le n\le5$, and every
$2\le k\le n$, together with the analytic continuation and strict
$27/10$ lower bound for

\[
 \frac{P(t)}{(t-1)(2-t)^3},\qquad 1\le t\le2,
 \quad P(t)=16\det(T_4(t)\text{ with column 3 replaced by }b_4(t)).
\]

Both parts of the frozen statement pass. The universal statement for all
$n$ remains unresolved. No alteration of the claim, parameter interval,
coefficient indexing, or numerical lower bound was needed for acceptance.

All 16 files in the snapshot match their SHA-256 entries, and the snapshot
digest matches the canonical compact sorted-key serialization of its file
mapping. The original `source.md` retains SHA-256
`7d0cf0cdfbdab8562029335d2852daca1e2d46fb8a29a0a2f562d35d74c0df15`.
The review used the specified frozen dossier and primary sources, without
reading owner checkpoints, state, historical transcripts, or earlier audit
verdicts. No agents or other research workers were launched. This is a
fresh workflow review, not external peer review or a statistical claim of
independence.

The decisive argument was reconstructed as follows.

1. **Covariance and denominators.** For $0<t<2$, the integral defining
   $C_t=\int_0^\infty(1-\cos u)u^{-1-t}\,du$ converges and is positive.
   Taking the centered second difference of its scaling identity gives
   the asserted Fourier integral for $\rho_j$, including $j=0$.
   The resulting quadratic form is the integral of a nonzero
   trigonometric polynomial's squared modulus against a weight positive
   almost everywhere. It is strictly positive. Thus all finite covariance
   determinants and the residual variances used in the proof are positive.
   No positivity of inverse matrix entries is inferred from this fact.

2. **The conditional edge step.** The second-difference integral with
   weight (1-|u|) proves $1>\rho_1>\rho_2>\cdots>0$ for $1<t<2$.
   The singularity in the $j=1$ integral is integrable. Strict
   log-convexity of $z^{t-2}$, followed by Cauchy--Schwarz, proves
   $\rho_j^2<\rho_{j-1}\rho_{j+1}$ for $j\ge2$. The independently
   verified identity
   $\rho_2-\rho_1^2=(\rho_1-\rho_3)/2>0$ supplies $j=1$.
   Consequently $\rho_{j+1}/\rho_j$ increases strictly for $j\ge0$.

   If $g_k=\Gamma_n^k>0$ for the preceding entire row, the first new
   coefficient has numerator
   $\sum_{k=2}^n g_k(\rho_{k-2}-\rho_k)>0$. The last new coefficient
   has numerator

   \[
   \sum_{k=2}^n g_k\rho_{n-k}
   \left(\frac{\rho_n}{\rho_{n-1}}-
   \frac{\rho_{n+1-k}}{\rho_{n-k}}\right)>0.
   \]

   I checked the residualization, reversal of indices, and the two
   preceding-row equations that give these identities. Every ratio
   denominator is positive; $n-k\$ ranges from 0 to (n-2), strictly
   below the index of the first ratio. Both residual denominators are
   positive by step 1. The preceding-row positivity hypothesis is
   established before every application; there is no all-$n$ circularity.

3. **The $n=4$ middle coefficient.** Independent symbolic determinant
   computation gives $N_{43}=(1-\rho_2)q$, where
   $q=\rho_2+\rho_2^2-\rho_1^2-\rho_1\rho_3$, and verifies

   \[
   4q=F(t)=9^t-8^t-2\,6^t+4\,4^t-2\,2^t-1.
   \]

   The exponential Descartes argument in the dossier is valid: choose an
   exponent strictly between two coefficients of opposite signs, conjugate
   by its exponential, and differentiate. All coefficients to its left
   change sign, removing exactly one variation. Induction and Rolle's
   theorem bound real zeros counted with multiplicity by the number of
   variations. Here the ordered coefficients have three variations.
   Exact checks give $F(1)=F(2)=0$, $F(3)=24$,
   $F'(1)=2\log(27/16)>0$, and
   $F'(2)=18\log(243/256)<0$. A third zero lies in $(2,3)$.
   There can be no zero in $(1,2)$, where (F) is therefore positive.

4. **The first interior coefficient at $n=5$.** Independent symbolic
   computation gives $N_{53}=qK$, with
   $K=(1-\rho_2)(1-\rho_4)-(\rho_1-\rho_3)^2$.
   The covariance matrix of $X_1-X_5,X_2-X_4$ is the stated two-by-two
   matrix and has determinant (4K). Its coefficient vectors are linearly
   independent, so strict positive definiteness proves $K>0$.
   This proves $\Gamma_5^3>0$.

5. **The full normalized cofactor bound.** SymPy's Berkowitz determinant
   was applied to the defining covariance matrix, without importing the
   proposer's algebra code. It reproduces all 30 exponential terms of
   (P). Applying
   $aL_2\partial_a+bL_3\partial_b+cL_5\partial_c$ to the polynomial
   in $a=2^t,b=3^t,c=5^t$ verifies exactly
   $P(1)=0$, $P(2)=P'(2)=P''(2)=0$, and
   $P'(1)=80L_2-48L_3$. Identically zero formal polynomials imply the
   logarithmic identities; no algebraic independence of logarithms is
   assumed. The exponential polynomial is entire, so the endpoint zeros
   give the claimed removable singularities and analytic continuation.

   With $x=2-t$ and $A_k=(-1)^kP^{(k)}(2)/k!$, absolute convergence
   and $\sum_{k\ge3}A_k=0$ give

   \[
   R(x)=-\sum_{k\ge4}A_k\sum_{j=0}^{k-4}x^j,
   \qquad 0\le x\le1.
   \]

   Thus truncation at $N=26$ has uniform error bounded by
   $\sum_{k\ge27}(k-3)|A_k|$. The estimates
   $\log b<5$ and $\sum_b|c_b|b^2=212096$ give the supplied
   geometric majorant. Its exact value is

   \[
   B=\frac{790119171142578125}{179590728782941572096}<\frac1{200}.
   \]

   The ratio of consecutive majorant terms is bounded by (5/24)
   starting at $k=27$. This also justifies uniform convergence at the
   otherwise problematic endpoint $x=1$; no division of an approximate
   zero is used.

   The fresh verifier checks the supplied prime-log intervals by a
   different calculation: degree-90 rational Taylor bounds on the
   exponential prove $e^{L_p}<p<e^{U_p}$. It does not reuse the
   proposer's logarithm series. Exact rational substitution then verifies
   all 24 $A_k$ enclosures and all 23 degree-22 Bernstein lower bounds.
   The power-to-Bernstein conversion has positive factors
   $\binom{i}{j}/\binom{22}{j}$, so the interval direction is correct.
   The Bernstein basis is nonnegative and sums to one. The smallest
   recorded lower bound is $2718387/10^6>271/100$. Therefore

   \[
   R(x)>\frac{271}{100}-\frac1{200}
         =\frac{541}{200}>\frac{27}{10}
   \]

   on the full closed interval, including both continued endpoints.
   In particular $\Gamma_5^4=P/(16\det T_4)>0$ on $1<t<2$.

6. **Assembly and endpoints.** The $n=2$ row starts with
   $\Gamma_2^2=2^{t-1}-1>0$. The edge argument gives $n=3$, then
   the edges of $n=4$; step 3 completes that row. The edge argument
   then gives the two edges at $n=5$, and steps 4--5 give its two
   interior entries. The proof makes no assertion about predictor
   existence at $H=1$, nor strict positivity at $H=1/2$.

The fresh exact verifier is `audit/referee_verify.py`; its successful
output is `audit/referee-verification.json`. These records concern the
finite algebra and arithmetic. The analytic reasoning above is also
necessary for the mathematical verdict.

The supplementary ball evidence was checked separately. A read-only
execution of the frozen Taylor function reproduces the two endpoint
derivative signs and all 112 contiguous interior cells, using python-flint
0.9.0 at 192 bits. The left and right endpoint arguments are valid:
$P(1)=0,P'>0$ give positivity on the left, and the triple zero at 2
with $P'''<0$ gives positivity to its left. This reproduction reuses
the supplied algorithm and is not described as an independent sign proof.
Six newly selected rational parameters, including $1+2^{-45}$ and
$2-2^{-45}$, were also checked by direct linear solves at 320 bits for
every row $2\le n\le5$; all 60 coefficient enclosures were positive.
Those six parameters are finite supplementary checks, not domain coverage.
The script and output are `audit/referee_arb.py` and
`audit/referee-arb-verification.json`.

There is one nondecisive serialization limitation. The stored `str(arb)`
displays for cells $j=246,247$ in `evidence/n5-arb-crosscheck.json` are
`[+/- 0.0102]` and `[+/- 7.58e-3]`; each displayed enclosure contains
zero. Therefore the saved strings alone do not certify all 112 signs.
Recomputation from the frozen code proves both underlying intervals
strictly positive, with lower endpoints greater than 0.00746 and 0.00535,
respectively. The audit output records their exact dyadic endpoints, as
well as those of all other cells. This is a display precision issue, not
a failed sign check or a change to the submitted theorem. The independent
rational certificate proves the stronger frozen bound without this
supplement. If the ball output is presented in a manuscript, use lossless
endpoints or explain the display limitation; do not describe those two
rounded strings as standalone positive certificates. No frozen file was
modified to address it.

The nearest prior results and contribution were checked in the actual
primary PDFs. Fresh `pdftotext` extraction matches all four submitted
source extracts byte-for-byte; this is recorded in
`audit/referee-source-extraction-checks.json`. The 2022 paper proves the
small $n=3$ case and gives partial $n=4$ analysis. Its Remark 2.12
on page 9 describes the missing middle sign numerically. I also checked
the weighted-sum inference on pages 13--14: monotonicity of $\rho_j$
alone does not justify it with unknown signs of the weights. The present
proof uses the valid conditional version with positive weights already
established. This dependency observation does not disprove that paper's
stated first-coefficient theorem.
Source: [Mishura, Ralchenko and Schilling (2022)](https://arxiv.org/abs/2209.02501).

The 2025 paper's Conjecture 3 is the original all-$n$ target.
Proposition 1 states the $n=4$ inequality and its proof supplements
analytic subintervals with a graph. Proposition 2 proves the conditional
last-coefficient step. Remark 4 on page 8 explicitly discusses the
$n=5$ penultimate sign through numerical evidence. Thus the exact
delta is a rigorous certificate over the entire Hurst interval for that
named finite case, including all four coefficients and a quantitative
normalized-cofactor margin. The claim properly excludes priority for
$n\le4$, the recursion, covariance factorization, and approximation
tools.
Source: [Bodnarchuk, Mishura and Ralchenko (2025), primary university copy](https://osuva.uwasa.fi/bitstreams/ba17e604-877b-4de0-b940-2ac4cae74a92/download).

A fresh bounded web search used combinations of “fractional Gaussian
noise”, “positivity”, “n = 5”/“n=5”, “positive coefficients”, “proof”,
“2026”, “penultimate”, and “certificate”. No equivalent rigorous
full-interval $n=5$ result was found in the primary material inspected.
The opened 2026 preprint's Theorems 2.1--2.3 concern a FARIMA formula
and fGn PACF asymptotics; their statements do not supply the finite
interior-coefficient claim reviewed here. Its proofs were not audited.
Source: [Cai, arXiv:2605.31416v1](https://arxiv.org/html/2605.31416v1).
The metadata and abstract of
[Chigansky and Kleptsyna, arXiv:2504.01562](https://arxiv.org/abs/2504.01562)
were also inspected; that limited inspection is not a full-paper audit.
The direct 2025 journal-page open failed, while the complete frozen
primary PDF remained available. None of these access or search limits
is treated as mathematical evidence. The novelty finding is bounded to
the sources and searches inspected on this date, not worldwide priority.

This is a nontrivial finite-case contribution rather than an arbitrary
restriction: it completes the next case explicitly singled out in the
primary literature, and the missing sign requires control of a
30-term exponential sum with endpoint cancellations. Its credible use is
as a rigorous finite-prediction benchmark, a base case for further
recurrence arguments, and a reproducible certificate for a previously
graph-supported sign. The quantitative margin makes the computational
claim inspectable. It is suitable in scope for one coherent result note;
the $n=4$ proof should remain supporting material in the same note.
This assessment makes no promise of journal acceptance or exhaustive
priority verification.

No unresolved mathematical gap remains in the frozen candidate scope.
Acceptance does not extend to $n\ge6$, any bilateral conditioning
claim, an optimal lower bound, or publication build/citation/visual
checks. The next workflow step is the runner's `check-math` gate,
followed by writing at exactly the accepted finite-case scope.
