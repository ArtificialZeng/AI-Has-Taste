# Precise problem reading

Provenance: `bigMac-00024-p02-triage-4125f9c11f6c`. The immutable statement is `source.md`; this file records its mathematical interpretation and does not replace or modify it.

## Definitions and quantifiers

Fix an arbitrary real number `L>0`. For each positive integer `d`, let
\[
\mathcal F_L(\mathbb R^d)=\{f:\mathbb R^d\to\mathbb R:
 f\text{ is differentiable and convex},\ 
 \|\nabla f(x)-\nabla f(y)\|\le L\|x-y\|\ \forall x,y,
\ \varnothing\ne\arg\min f\subsetneq\mathbb R^d\}.
\]
Thus “`L`-Lipschitz gradient” means Lipschitz constant at most `L`, and “proper minimizer set” means a strict subset of the ambient space. All norms and inner products are Euclidean. Dimensions are finite but unbounded: `d` ranges over all positive integers.

For an **ordered**, instance-independent pair `(eta_1,eta_2) in (0,infinity)^2`, and for every admissible tuple `(d,f,x_*,x_0)` with `x_* in argmin f` and `x_0 notin argmin f`, define
\[
x_1=x_0-\eta_1\nabla f(x_0),\qquad
x_2=x_1-\eta_2\nabla f(x_1).
\]
Then
\[
R_2^L(\eta_1,\eta_2)=
\sup_{d,f,x_*,x_0}
\frac{f(x_2)-f(x_*)}{L\|x_0-x_*\|^2}.
\]
The denominator is strictly positive because `x_0` is not a minimizer. The chosen minimizer `x_*` is itself part of the supremum; no closest-minimizer convention is imposed. The steps are fixed before the instance is chosen, with no adaptivity, randomness, momentum, or line search. Swapping the two steps produces a different ordered schedule.

The frozen claim is the following universal statement: for every `L>0`,
\[
\inf_{(\eta_1,\eta_2)\in(0,\infty)^2}R_2^L(\eta_1,\eta_2)
=C_*:=\frac1{5+4\sqrt2+\sqrt{9+8\sqrt2}},
\]
and this infimum is attained at
\[
(L\eta_1,L\eta_2)=
\left(\sqrt2,\frac{3+\sqrt{9+8\sqrt2}}4\right).
\]
Numerically, the proposed normalized schedule is approximately `(1.4142135624,1.8767682908)` and `C_* approximately 0.06594597645`. Attainment is claimed; uniqueness is not.

## Exact normalization

Put `h_i=L eta_i` and `g=f/L`. Then `g` is 1-smooth and the same iterates satisfy `x_i=x_{i-1}-h_i nabla g(x_{i-1})`, while
\[
\frac{f(x_2)-f(x_*)}{L\|x_0-x_*\|^2}
=\frac{g(x_2)-g(x_*)}{\|x_0-x_*\|^2}.
\]
Hence `R_2^L(eta_1,eta_2)=R_2^1(h_1,h_2)`. Translation of the chosen `x_*`, subtraction of the minimum value, and the spatial/value rescaling
\[
z=(x-x_*)/D,\qquad \phi(z)=\frac{g(x_*+Dz)-g(x_*)}{D^2},
\quad D=\|x_0-x_*\|>0,
\]
further reduce exactly to `L=1`, `x_*=0`, `f_*=0`, and `||x_0||=1`. The target is therefore a global minimization over the entire open quadrant `(h_1,h_2)>0`, not merely over a bounded box or the class of basic/composable schedules.

## Nearest inspected results and exact delta

The following fixed local primary sources were inspected on 2026-09-09; their SHA-256 hashes agree with `source.md`.

- Jung--Cho--Yun, arXiv:2609.04032v1, <https://arxiv.org/abs/2609.04032>: Equation (1) on PDF p. 1 gives the same dimension-free performance measure, Appendix A gives the `L=1` rescaling, and Theorem 3.3 on PDF p. 7 gives a general schedule lower bound. At `N=2` that theorem yields only about `0.02003175`, so it does not prove the proposed exact constant.
- Grimmer--Shu--Wang, arXiv:2410.16249v2, <https://arxiv.org/abs/2410.16249>: Definition 1 (PDF p. 4) makes an f-composable rate `rho` mean the tight bound `f(x_n)-f_* <= (rho/2)||x_0-x_*||^2`. The length-two table on PDF p. 10 contains the proposed schedule with `rho=2C_*`, proving the exact fixed-schedule identity `R_2^1=C_*` by matching quadratic and Huber instances. Section 3.2.2 and Conjecture 1 (PDF pp. 12--13) conjecture minimax optimality of basic f-composable schedules but do not prove minimaxity over all positive schedules.
- Das Gupta--Van Parys--Ryu, arXiv:2203.07305v5, <https://arxiv.org/abs/2203.07305>: Tables 11--12 on PDF pp. 34--35 report the value `0.065946` and steps `(1.414214,1.876768)` from BnB-PEP. This is numerical/global certification only to the computation's stated tolerances, not a symbolic proof of the radical formula.

Accordingly, the source status is **open-supported within the inspected sources, with broader current-literature novelty still unverified**. The exact proposed delta is solely the lower bound
\[
R_2^1(h_1,h_2)\ge C_*\qquad\text{for every }(h_1,h_2)\in(0,\infty)^2.
\]
The reverse inequality and sharpness for the displayed fixed schedule are already supplied by exact composability. A proof must cover every positive ordered pair. A disproof would require an exact pair together with a rigorous dimension-free upper bound strictly below `C_*`; a favorable quadratic or Huber value alone would not suffice.

## Verification scope and first research test

For fixed `(h_1,h_2)`, use the exact smooth-convex interpolation inequalities for the four samples `*,0,1,2`:
\[
f_i\ge f_j+\langle g_j,x_i-x_j\rangle+\tfrac12\|g_i-g_j\|^2
\quad(i,j\in\{*,0,1,2\}),
\]
with `g_*=0`, `x_*=0`, `||x_0||=1`, `x_1=x_0-h_1g_0`, and `x_2=x_1-h_2g_1`. A `4 x 4` Gram matrix for `(x_0,g_0,g_1,g_2)` gives an exact dimension-free fixed-schedule PEP. The outer dependence on the two steps is nonconvex.

The first bounded research test is to implement this complete directed-interpolation PEP, solve it at high precision near the proposed schedule to identify (not prove) the active constraints and dual multipliers, and then exactify the candidate fixed-schedule primal/dual certificate in `Q(sqrt(2),sqrt(9+8sqrt(2)))`. The resulting active set is the input for a later exact global partition of the positive step quadrant.
