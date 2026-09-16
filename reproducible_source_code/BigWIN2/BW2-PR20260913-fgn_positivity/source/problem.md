# One-sided fractional Gaussian noise predictor positivity

## Frozen original and precise interpretation

The verbatim original remains in source.md. Its SHA256 is
7d0cf0cdfbdab8562029335d2852daca1e2d46fb8a29a0a2f562d35d74c0df15.
For every real H with 1/2<H<1, define rho_0(H)=1 and, for integers j>=1,

rho_j(H)=((j+1)^(2H)-2*j^(2H)+|j-1|^(2H))/2.

For every integer n>=2, let T_(n-1)(H) be the real symmetric matrix with
entries rho_|i-j|(H), 1<=i,j<=n-1, and let
b_(n-1)(H)=(rho_1(H),...,rho_(n-1)(H))^T. Define

(Gamma_n^2(H),...,Gamma_n^n(H))^T = T_(n-1)(H)^(-1) b_(n-1)(H).

The exact target is:

For all H in (1/2,1), all integers n>=2, and every k in {2,...,n},
Gamma_n^k(H)>0.

Equivalently, let B^H be centered fractional Brownian motion with covariance
E[B_s^H B_t^H]=(s^(2H)+t^(2H)-|t-s|^(2H))/2, and
Delta_j=B_j^H-B_(j-1)^H. Then Gamma are the coefficients of
E[Delta_1 | Delta_2,...,Delta_n]=sum_(k=2)^n Gamma_n^k Delta_k.
The finite increment covariance is strictly positive definite for 0<H<1,
so these coefficients exist uniquely. Time reversal gives the equivalent
finite past predictor; bilateral conditioning changes the problem.

The n=2 case is Gamma_2^2=2^(2H-1)-1>0. At H=1/2 all off-diagonal rho_j
vanish and the coefficients are zero, so strict positivity would fail there.
At H=1 all rho_j=1 and T_(n-1) is singular for n>=3. Both endpoints are
excluded uniformly. No finite-n restriction replaces the original.

## Source status and nearest prior results

Source status: open-supported under the bounded current primary-source
search in evidence/literature-check.md and evidence/research-literature.md,
not a guarantee of worldwide open
status. The original is 2022 arXiv:2209.02501v1 Conjecture (A), p.2, and
2025 Fractal Fract. 9:428 Conjecture 3, p.3.

The 2022 paper proves the n=3 case and the n=4 outer coefficient signs/order;
its Remark 2.12, p.9, supplies numerical support for the middle coefficient.
The 2025 paper already states the full n=4 inequality as Proposition 1,
pp.5–6, combining analytic subintervals and a graph for the remaining range.
That graph passage was independently checked in the actual supplied PDF.
It is not a rigorous full-interval certificate by itself.

Correction to the intake handoff: the all-n first-coefficient positivity is
stated in 2022 Proposition 2.17, pp.13–14, but its last weighted-sum sign
step requires an additional justification when previous coefficients have
unknown signs. Treat it as a stated result whose unconditional proof was
not verified here. Its conditional form is valid. The 2025 last-coefficient
positivity result also explicitly assumes positivity of the previous row;
neither argument propagates all interior signs by itself.

A 2026 primary preprint, arXiv:2605.31416v1, addresses PACF asymptotics;
its inspected main theorems do not settle all finite predictor signs.

## Research result submitted for fresh review

Nearest prior result X: full n=4 positivity is already stated, with the
remaining n=5 penultimate analytic sign explicitly discussed in 2025 Remark 4.

The self-contained argument in evidence/n5-proof.md supplies a short global
n=4 certificate using the standard exponential Descartes rule. Exact cofactor
algebra also gives

Gamma_5^3 = q*K/det(T_4),
q=rho_2+rho_2^2-rho_1^2-rho_1*rho_3,
K=(1-rho_2)(1-rho_4)-(rho_1-rho_3)^2>0.

The sign K>0 follows from strict positive definiteness for the two increment
differences Delta_1-Delta_5 and Delta_2-Delta_4. With n=4 positive, the valid
conditional edge arguments give Gamma_5^2>0 and Gamma_5^5>0. The remaining
Gamma_5^4 sign is now certified over the entire open H interval.

Exact proposed subsidiary theorem: for every H in (1/2,1), all Gamma_n^k
are strictly positive for 2<=n<=5 and 2<=k<=n. In addition, let t=2H and

P(t)=16*det(T_4 with column 3 replaced by (rho_1,...,rho_4)^T).

Then the analytic continuation of P(t)/((t-1)*(2-t)^3) is >27/10 for every
t in [1,2]. The endpoint continuation concerns this cofactor quotient, not
existence of a predictor at the excluded degenerate endpoint.

Evidence: evidence/certify_n5.py independently expands the determinant and
checks the endpoint identities with integer polynomial arithmetic. Its
standard-library rational log bounds and Taylor/Bernstein certificate,
evidence/n5-certificate.json, prove a uniform positive lower bound. A
different ball arithmetic calculation, evidence/crosscheck_n5_arb.py and
evidence/n5-arb-crosscheck.json, verifies endpoint derivative signs and 112
contiguous interior intervals. Seven held-out dyadic determinant checks,
including t=1+2^(-30) and t=2-2^(-30), are supplementary finite evidence.

The natural contribution is a rigorous full-H completion of the n=5 case
explicitly identified in 2025 Remark 4, with an inspectable finite certificate.
No novelty is claimed for n<=4, the covariance factorization, predictor
recursion, Descartes rule, or Bernstein/Taylor machinery. The contribution's
value and bounded literature comparison remain subject to fresh review.

Scope remains the original all-n question. The proposed finite theorem is
a subsidiary result; original_status remains unresolved. No fresh referee
has yet accepted it. One next test: rederive and audit the n=5 certificate
and proof at this exact scope in the runner's fresh referee context.

## Deduplication and decision

Read the sole handoff and both dedup notes. The four retained neighboring
originals have different objects and quantifiers. The fresh 652-record native
registry scan matched only this project's own registration; the handoff's
2,883-description Excel comparison was not independently rerun. Details and
limits are in evidence/literature-check.md.

Decision after research pass 1: candidate; candidate_kind=result-note;
original_status=unresolved. The claim is the complete n<=5 finite theorem
and its explicit cofactor bound. No manuscript, research PDF, mathematical
acceptance, or unconditional priority claim is made by this research job.
