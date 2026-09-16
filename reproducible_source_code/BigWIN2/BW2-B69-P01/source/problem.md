# Precise problem reading

## Frozen source and status

The immutable statement is `source.md` (SHA-256
`8c450171f5fe6b12b21014c3e96e060d54fedb1b3e3418de1d26ada9d4921dab`).
This file only fixes its mathematical reading; it does not alter the claim.

Source status: **open-supported specialization**. Bathija--Rohatgi--Soskin,
*Bounded ratios for Lorentzian polynomials*, arXiv:2609.05341v1, states the
general assertion as Conjecture 9.2. Its text does not prove or disprove the
complete `(n,k)=(4,3)` specialization. A targeted arXiv search on 2026-09-08
found the source paper but no separate resolution of this specialization. This
is evidence about the inspected literature, not a claim of priority or an
exhaustive proof that no resolution exists.

## Objects and conventions

Let
\[
H=H(4,3)=\{\alpha=(\alpha_1,\alpha_2,\alpha_3)\in
\mathbb Z_{\ge 0}^3:\alpha_1+\alpha_2+\alpha_3=4\};
\]
thus `|H|=15`. For a formal `4 x 3` matrix
`A=(a_{ri})`, define
\[
Q_A(x_1,x_2,x_3)=\prod_{r=1}^{4}
 (a_{r1}x_1+a_{r2}x_2+a_{r3}x_3)
 =\sum_{\alpha\in H}P_\alpha(A)x^\alpha.
\]
Here `P_alpha` is the **ordinary**, not factorial-normalized, coefficient:
\[
P_\alpha(A)=\sum_{\substack{\phi:\{1,2,3,4\}\to\{1,2,3\}\\
|\phi^{-1}(i)|=\alpha_i}}
\prod_{r=1}^{4}a_{r,\phi(r)}
\in\mathbb Z_{\ge0}[a_{11},\ldots,a_{43}].
\]

The product bounded-ratio cone is read exactly as Definition 5.5:
\[
\mathrm{BR}_{\mathring Q}(4,3)=
\left\{\gamma\in\mathbb R^H:
\exists B>0\ \forall A\in\mathbb R_{>0}^{4\times3},\quad
\prod_{\alpha\in H}P_\alpha(A)^{\gamma_\alpha}\le B\right\}.
\]
In particular, the cone domain uses strictly positive `A`; the later
coefficientwise condition is an identity/inequality in the twelve formal
indeterminates and consequently also evaluates on nonnegative `A`. Every
member of the cone is balanced:
\[
\sum_{\alpha\in H}\gamma_\alpha\alpha=0.
\]
No additional factorial correction is inserted.

For an integral `gamma in Z^H`, put
\[
N_\gamma=\prod_{\gamma_\alpha>0}P_\alpha^{\gamma_\alpha},\qquad
D_\gamma=\prod_{\gamma_\alpha<0}P_\alpha^{-\gamma_\alpha}.
\]
Empty products are `1`. Both are finite polynomials with nonnegative integer
coefficients in the twelve `a_ri`.

## Quantified claim to resolve

Prove or disprove
\[
\boxed{\quad
\forall\gamma\in\mathrm{BR}_{\mathring Q}(4,3)\cap\mathbb Z^H\;
\exists C=C(\gamma)>0\;
\forall u\in\mathbb Z_{\ge0}^{12},\quad
[a^u](C D_\gamma-N_\gamma)\ge0.
\quad}
\]
The constant is allowed to depend on `gamma` and need not be `1`. The
quantifier includes `gamma=0`, all non-ray lattice points, and lattice points
whose semigroup generation may require more than the primitive extreme rays.

Because `N_gamma` and `D_gamma` have positive coefficients on their supports,
for each fixed `gamma` the displayed existential statement is equivalent to
the exact finite condition
\[
\operatorname{supp}(N_\gamma)\subseteq
\operatorname{supp}(D_\gamma).
\]
Indeed, support containment permits the finite choice
`C=max_u [a^u]N_gamma/[a^u]D_gamma` (and any positive `C` at least `1` for
`gamma=0`); a missing denominator monomial makes every `C` fail.

## Nearest result and delta

Proposition 7.4 of arXiv:2609.05341v1 proves, using exact rational cone
computations, that
\[
\mathrm{BR}_{\mathring Q}(4,3)=
\mathrm{BR}_{\mathring L}(4,3)=
\operatorname{cone}\{\rho_{\beta;i\mid jk}:
\beta\in H(2,3),\ i\in\{1,2,3\},\ \{j,k\}=\{1,2,3\}\setminus\{i\}\},
\]
with 18 distinct extreme rays, where
\[
R_{\rho_{\beta;i\mid jk}}=
\frac{P_{\beta+2e_i}P_{\beta+e_j+e_k}}
{P_{\beta+e_i+e_j}P_{\beta+e_i+e_k}}.
\]
Conjecture 9.2 records `C=1` checks only for all rays at `(3,3)` and `(3,4)`,
not `(4,3)`. The predecessor Huang--Huh--Soskin--Wang,
arXiv:2510.25030v2, Conjecture 5.5 and its following paragraph concern the
degree-two/rank-two analogue (verified there for matrix size at most six), not
the present degree-four claim.

Thus the proposed delta is the full integral semigroup statement at `(4,3)`.
Checking the 18 rays alone is only a falsification screen, not a proof of this
delta.

## Scope and decisive routes

An acceptable disproof is one explicit integral `gamma` with exact cone
membership plus an exact monomial in
`supp(N_gamma) \\ supp(D_gamma)`. An acceptable proof must cover every lattice
point, for example by computing sign-chamber Hilbert bases in the balanced
lattice and certifying support containment for each generator. Addition is
multiplicatively closed only for sign-compatible exponent vectors; cancellation
across sign chambers cannot be ignored. Real conical generation by the 18 rays
does not by itself establish integral semigroup generation.

## Sources inspected (retrieved 2026-09-08)

- <https://arxiv.org/abs/2609.05341v1> and
  <https://arxiv.org/html/2609.05341v1>: Definitions 5.1, 5.4, 5.5 and 9.1;
  Proposition 7.4 (especially the exact computation after it); Conjecture 9.2.
- <https://arxiv.org/abs/2510.25030v2> and
  <https://arxiv.org/html/2510.25030v2>: Conjecture 5.5 and the reported
  degree-two computation following it.
- Exact/equivalent arXiv searches for `subtraction-free ratio`,
  `Conjecture 9.2`, and bounded ratios of products of linear forms returned the
  source paper and the unrelated bounded-ratio neighbor arXiv:2609.03934, but
  no separate `(4,3)` resolution in the inspected results.
