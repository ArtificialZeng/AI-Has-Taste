# Immutable source — bigMac-00024-p02

## Frozen source statement

For `L>0`, let `F_L(R^d)` denote the class of differentiable convex functions `f:R^d->R` with `L`-Lipschitz gradient and nonempty proper minimizer set. For positive steps `eta_1,eta_2`, run
\[
x_1=x_0-\eta_1\nabla f(x_0),\qquad
x_2=x_1-\eta_2\nabla f(x_1),
\]
and define exactly as Jung--Cho--Yun Equation (1)
\[
R_2^L(\eta_1,\eta_2)=
\sup_{\substack{d\ge1,\ f\in F_L(\mathbb R^d),\ x_*\in\arg\min f,\\x_0\notin\arg\min f}}
\frac{f(x_2)-f(x_*)}{L\lVert x_0-x_*\rVert^2}.
\]
Prove or disprove
\[
\inf_{\eta_1,\eta_2>0}R_2^L(\eta_1,\eta_2)
=C_*:=\frac1{5+4\sqrt2+\sqrt{9+8\sqrt2}},
\]
with attainment by the ordered normalized schedule
\[
L\eta_1=\sqrt2,\qquad
L\eta_2=\frac{3+\sqrt{9+8\sqrt2}}4.
\]
Do not assert uniqueness unless it is independently proved. The statement quantifies over every finite dimension, every function in the class, and all positive ordered step pairs.

## Sources and exact proposed delta

- Minchan Jung, Hanseul Cho, and Chulhee Yun, *Stronger Lower Bounds for (Non-)Anytime Acceleration of Gradient Descent*, arXiv:2609.04032v1: Equation (1), Section 1.1, Theorem 3.3, and Appendix A rescaling.
- Benjamin Grimmer, Kevin Shu, and Alex L. Wang, *Composing Optimized Stepsize Schedules for Gradient Descent*, arXiv:2410.16249v2: Definition 1, the length-two basic f-composable table on PDF p. 10, Section 3.2.2, and Conjecture 1. Its exact composition theorem gives the candidate schedule a tight fixed-schedule bound with f-composable rate `2C_*`, hence `R_2^L=C_*` at that schedule.
- Shuvomoy Gupta et al., arXiv:2203.07305: PDF pp. 34--35, Tables 11--12, reports a BnB-PEP global numerical value `0.065946` and steps `(1.414214,1.876768)`.

Fixed local PDFs and SHA-256:

- `batches/literature/bigMac-24/2609.04032v1.pdf`: `862b892efb97c0d818f37339c4cbeeff259763bc62681ea761efd32570f6bcc0`;
- `batches/literature/bigMac-24/2410.16249v2.pdf`: `c75a6ee85b829d59ec83b28eb347fb2d05d7aad78887b50f8391cd1e49053f70`;
- `batches/literature/bigMac-24/2203.07305.pdf`: `6e660372e6874d0a65bf7de46798ddd9ce5def84b747770904b82df2ff6d263a`.

The proposed delta is the missing exact lower bound over all positive two-step schedules. Existing exact composability proves the candidate's upper bound and sharpness at that fixed schedule; the reported branch-and-bound result is numerical/certified only to its stated tolerances, not the desired symbolic theorem.

## Cheapest decisive route to audit

Normalize `L=||x_0-x_*||=1`. Form the complete smooth-convex interpolation PEP for the samples at `x_*,x_0,x_1,x_2`: a `4x4` Gram matrix, function values, the full set of directed interpolation inequalities, and the two outer variables. Numerically identify the active set only as a discovery aid. Then either:

1. exactify a primal/dual/KKT certificate in `Q(sqrt(2),sqrt(9+8sqrt(2)))` and cover the remaining positive step quadrant by an exact CAD/SOS or analytic partition; or
2. refute the target by exhibiting an exact positive ordered step pair and a rigorously valid worst-case upper bound strictly below `C_*`.

The one-dimensional quadratic and appropriate Huber function certify sharpness of the fixed candidate schedule, but they do not by themselves prove minimaxity over all schedules.

## Scope and honesty

Do not conflate the source's asymptotic schedule question with this finite `N=2` layer. Do not treat a floating-point SDP, a numerical branch-and-bound tolerance, or recognition of the displayed radical as a proof. The nearby `bigMac-00022-p01` result concerns Nesterov FGM and a queried-gradient objective; it cannot be imported as this theorem.
