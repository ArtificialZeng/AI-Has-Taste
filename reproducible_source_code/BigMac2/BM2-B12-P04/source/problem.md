# Precise reading of the problem

## Probability model and conventions

Fix one probability space carrying the following variables for every integer
`d >= 2`.

- `Ber(p)` means the `{0,1}`-valued law with probability `p` at `1`.
- `S^(d-1) = {u in R^d : ||u||_2 = 1}`, equipped with normalized Haar
  (rotation-invariant) surface measure.
- `X_d ~ Ber(d^(-1/2))`, and `U_1^(d), U_2^(d)` are independent and each
  uniform on `S^(d-1)`.
- The phrase "in the source's notation" is read as importing Hypothesis
  5.1(3) of the cited paper: `X_d` (equivalently, the length vector below) is
  independent of `(U_1^(d), U_2^(d))`. Thus the joint law of each triple is
  the product of its three displayed marginal laws.
- The triples `(X_d,U_1^(d),U_2^(d))`, `d >= 2`, are mutually independent.

The within-`d` independence in the fourth bullet is essential. It is supported
by the source notation, but it is not explicit if the immutable statement is
read in isolation; without it, the coupling of `X_d` to the directions can
change the answer. This bullet records the interpretation and does not alter
`source.md`.

Throughout, `log` is the natural logarithm. For each fixed real parameter
`alpha`, define the nonnegative step lengths

`L_1^(d) = 1`,

`L_2^(d) = sqrt(d) (log d)^(-alpha) X_d`,

the two-step isotropic Pearson walk

`S_(d,2) = L_1^(d) U_1^(d) + L_2^(d) U_2^(d) in R^d`,

and the squared coefficient norm

`|L^(d)|_2^2 = (L_1^(d))^2 + (L_2^(d))^2`.

Consequently, the exact algebraic identity to be studied is

`Y_d = |S_(d,2)|_2^2 - |L^(d)|_2^2`

`    = 2 sqrt(d) (log d)^(-alpha) X_d <U_1^(d),U_2^(d)>`.

Here `Y_d` is signed. The assertion `Y_d -> 0 almost surely` means

`P({omega : lim_(d->infinity) Y_d(omega) = 0}) = 1`,

equivalently, for every `epsilon > 0`, only finitely many events
`{|Y_d| > epsilon}` occur almost surely.

## Quantified target

Determine the set

`A = {alpha in R : P(lim_(d->infinity) Y_d = 0) = 1}`.

The probability-one assertion is interpreted separately for each fixed
`alpha`; no uniform null set over the uncountable parameter set is requested.
The classification must explicitly decide whether `alpha = 1/2` belongs to
`A`.

## Scope and nearest stated result

The frozen claim is unresolved at intake. The designated primary source is
Bignamini--Casini--Martinelli, *Asymptotic Behaviour for Isotropic Pearson
Random Walks*, arXiv:2609.05195v1 (4 September 2026). Hypothesis 5.1 defines
the walk and imposes independence between lengths and directions; Proposition
3.3 identifies the inner-product law with one spherical coordinate; and
Example 6.5, pp. 10--11, treats `L_2^(d)=d^beta X_d`. It gives the sufficient
range `beta < 1/2` through Theorem 5.6 and proves failure at `beta = 1/2` under
cross-dimensional independence. It does not state the logarithmically damped
critical classification above.

Intake status is `new-question`: this is a precise logarithmic refinement of
the cited boundary, not a question that the cited source itself labels open.
No claim of novelty or exhaustive literature coverage is made. The permitted
target is an if-and-only-if classification in `alpha`, including the endpoint,
or a rigorously scoped partial result that closes a nontrivial side together
with the endpoint. Almost-sure conclusions require summable/divergent tail
bounds and the appropriate Borel--Cantelli direction; convergence in
probability or simulation is outside that evidentiary threshold.
