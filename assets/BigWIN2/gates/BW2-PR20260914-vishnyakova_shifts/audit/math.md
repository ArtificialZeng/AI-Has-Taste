# Mathematical referee report

Verdict: **accept** the exact frozen `result-note` scope.

Referee job: `primary-20260914-vishnyakova-shifts-referee-7e4f30ec6a07`.
Snapshot: `4b6ede918fda88951d06829d6bebbc9a1f5f4df5aa8af00b5ecc89c1af992c3c`.
Review date: 2026-09-14 Asia/Shanghai (2026-09-13 UTC).

## Scope and integrity

The frozen original problem requires interval shape, positive bounded endpoint
constants, and successive even-degree nesting. The submitted theorem establishes
the first two assertions with stronger bounds and classifies the endpoint
collisions. It also includes the stated two-step operator theorem, including
equality in the coefficient constraint, and its all-odd-degree consequence on
`-3/10 <= t < 0`. All these assertions were reviewed. Successive nesting is
explicitly unresolved. Accordingly the accepted kind is `result-note` and the
original status remains `unresolved`.

I read `source.md`, `problem.md`, `claim.json`, the snapshot, the full submitted
proof and verification code, the literature comparison, and relevant statements
in all three listed primary-source HTML files. The serialized JSON inputs were
parsed in full and independently recomputed. I did not execute the proposer
script, which would replace frozen evidence. No checkpoint, scheduling state,
previous audit, transcript, or unlisted historical proof was used. Historical
status assertions in the required `problem.md` were not used as evidence.

Every listed file hash, the equality of the snapshot file set with the claim's
evidence plus `claim.json`, and the canonical snapshot digest were checked before
and after computation. No frozen input was changed. The original source hash is
`599d20eb671a5110cc3ae01b0f602ff5460c237a42052ac704e602aca2e4dda8`.

## Reconstruction of the operator argument

Write `h(z)=c product_i(z+a_i)`, with `c>0`, distinct `0<a_i<1`, and even
degree `d>=2`. Then `S=sum_i 1/a_i>d`, `delta=(1+2t)/(1+t)^2>0`, and
`Lambda=1/(S+delta)>0`. Thus every division in the submitted argument is
legitimate. With `y=Lambda/2`, the following bounds hold on the entire
claimed parameter interval, including `t=-3/10`:

    40/49 <= delta <= 1,
    0 < y < 1/[2(2+delta)] < 5/28,
    R=yS=1/2-delta*y in (0,1/2),
    r_i=y/a_i in (y,1/2),
    eta=y/(y+lambda) >= 1/3.

In particular `-y` is to the right of every negative input root and `p(-y)<0`
for `p=(z-lambda)h`. The bound on `eta` uses precisely `lambda<=Lambda`,
so it retains the equality case.

For `w_i=r_i/(1-r_i)`, `W=sum_i w_i`, `V=sum_i w_i^2`, the two estimates
that drive the proof are valid:

    W >= R/(1-y),
    W^2 <= R(W+V).

The latter is Cauchy--Schwarz applied to the two vectors with components
`sqrt(r_i)` and `sqrt(r_i)/(1-r_i)`. Rearrangement gives
`W^2-V <= W-(1-R)W^2/R`, with no reversed inequality.

Direct differentiation gives, with `a=z(1+z)`,

    T_t^2 p = a^2 p'' + a(1+4z+2t)p'
                        +[2z^2+(1+2t)z+t^2]p.

At `z=-y`, logarithmic differentiation of the factors gives
`p'/p=(W-eta)/y` and `p''/p=(W^2-V-2 eta W)/y^2`.
These reconstruct equation (2) of the submitted proof. Its coefficient of
`eta` is `(1-y)[B-2(1-y)W]`, where `B=1-4y+2t`, and is strictly negative
because

    B-2(1-y)W <= B-2R = 2t+2(delta-2)y < 0.

Replacing `eta` by `1/3` therefore gives an upper bound. After the Cauchy
estimate, the remaining quadratic in `W` is

    F(W)=(1-y)^2[W-(1-R)W^2/R]-K W,
    K=(1-y)[5/3-14y/3+2t]>0.

The bracket defining `K` is greater than `7/30`. For `W>=R`,
`F'(W)<0`, since at `W=R` its value is
`(1-y)^2(2R-1)-K<0` and its slope is negative. Consequently substituting
`W=R/(1-y)` again preserves the required upper-bound direction. The result
is exactly `U_t(y)` in equation (3).

The quadratic coefficient of `U_t` is
`(delta-5/3)(delta-2)>0`. A convex function on `[0,Y]` lies below the chord
joining its endpoint values, so negativity at both endpoints is sufficient.
Here `Y=1/[2(2+delta)]`. The value at zero is at most `-3/50`, and

    U_t(Y)=N(t)/[3(2t^2+6t+3)^2],
    N(t)=12t^6+60t^5+89t^4+12t^3-60t^2-40t-7.

The denominator is strictly positive. I independently recovered the seven
Bernstein coefficients of `N((3/10)(u-1))` by solving a rational interpolation
system at `u=0,1/6,...,1`. They agree exactly with the seven strictly negative
coefficients in the proof. Nonnegative Bernstein basis functions sum to one,
including at the interval endpoints. Therefore `U_t(Y)<0` throughout the
closed parameter interval, and `q(-y)>0` follows. No numerical extrapolation
or limiting argument in `lambda` is needed.

To check the root count, order the negative roots of `p` as
`beta_1<...<beta_d`, put `g=T_t p`, and divide by `z(1+z)p`. On each of
`(-1,beta_1),...,(beta_(d-1),beta_d)`, its logarithmic expression is

    H(z)=sum_i 1/(z-beta_i)+1/(z-lambda)+t/z+(1-t)/(1+z).

For `z<beta_d`, the only positive summand in `H'` is `-t/z^2`.
It is strictly dominated by `1/(z-beta_d)^2`, since
`|z-beta_d|<|z|` and `-t<1`. Thus `H'<0`, and its one-sided pole limits
give exactly one simple root `xi_i` in each of those `d` intervals.
At these roots `sign g'(xi_i)=sign p(xi_i)=(-1)^i`, whence
`sign q(xi_i)=(-1)^(i+1)`.

The remaining signs are `q(-1)<0`, `q(0)<0`, `q(-y)>0` and positive
leading coefficient. Since `xi_d<beta_d<-y<0`, they give `d+2` distinct
roots in `(-1,0)` and one positive root in disjoint intervals. The output
degree is exactly `d+3` with positive leading coefficient. The exhibited
roots therefore exhaust the degree and are all simple. This proves the
full operator theorem in the claim, including `lambda=Lambda`.

## Odd-degree induction

The finite-difference definition gives

    Q_0=1, Q_(n+1)=T_t Q_n, partial_t Q_n=n Q_(n-1),
    Q_n(0)=t^n, Q_n(-1)=(t-1)^n, [z^n]Q_n=n!,
    [z]Q_n=(1+t)^n-t^n.

The recurrence follows from the binomial-basis multiplication identity, not
from an unproved root property. It also proves the reflection formula.
The case `m=1` is immediate. For `m=3`, I constructed `Q_3` directly from
finite differences and recomputed its discriminant and Bernstein certificate.
The discriminant is strictly positive on `[-3/10,0]`. For `t<0`, the constant
term is negative and every other coefficient is positive, so Descartes' rule
gives exactly one positive root. Reflection to parameter `1-t>1` excludes
roots at or below `-1`. The two remaining real simple roots lie in `(-1,0)`.

If the asserted configuration holds for odd `m>=3`, factor
`Q_m=(z-lambda)h`. The exact coefficient identity is

    [z]T_t^2[(z-lambda)h]
      =(1+t)^2 h(0)[1-lambda(S+delta)].

For the actual output `Q_(m+2)`, its left side is
`(1+t)^(m+2)-t^(m+2)>0`. Since `h(0)>0`, the required bound on `lambda`
follows strictly. This uses known coefficients, not the desired root count,
so the induction is not circular. The operator theorem completes all odd
degrees throughout the exact claimed strip.

## Global interval and endpoint argument

The source's generating-function criterion is applicable with fixed positive
leading coefficient. More explicitly, if
`Q_n(z)=n! product_i(z+a_i)` with `a_i in [0,1]`, its generating numerator is
`n! product_i[a_i+(1-a_i)x]`, which has nonnegative coefficients and only
nonpositive finite roots. A root `a_i=1` causes a degree drop in that
numerator, and a root `a_i=0` is permitted. There is no lost endpoint case.
The converse follows from the same transform and the total-positivity
criterion in the primary source.

The elementary restrictions in the proof check out. For even `n`, coefficient
nonnegativity implies `t>=-1/2`. The specified two-by-two Toeplitz minor then
implies `t>=-b` for a negative admissible `t`, where `b=1-1/sqrt(2)`.
At `t=-b`, writing `a_j=(j-b)^n>0`, one has `a_1^2=a_0 a_2`, and the
specified three-by-three determinant is

    a_1^3-2a_0 a_1 a_2+a_0^2 a_3
      =(a_0^2/a_1)(a_1 a_3-a_2^2)<0.

The strict sign follows from
`(1-b)(3-b)-(2-b)^2=-1`. All quantities divided by are positive.
Reflection thus gives `M_n subset (-b,1+b)`. The set is closed by its
definition as an intersection of nonnegative-minor conditions, hence compact.

The quadratic computation and the source's polynomial multiplication theorem
give `M_2 subset M_n` for every even `n`. Multiplication is used only in the
polynomial-interpolated class, where the theorem applies; arbitrary termwise
closure of totally positive sequences is not assumed. The interior root
induction for `0<t<1` has positive endpoint residues and proves simple roots
in `(-1,0)`. Continuity supplies membership at `t=0,1`.

Now fix even `n>=4` and a negative admissible parameter. The odd theorem
applies because `b<3/10`. Its `g=Q_(n-1)` has `n-2` simple negative roots
and one positive root. The preceding strictly decreasing `H` argument for
`Q_n=T_t g` gives `n-2` simple roots to the left of the largest negative
root of `g`. No root of `g` is a root of `Q_n`, and neither `-1` nor zero
is a root. If `Q_n` has a multiple root, its remaining two degrees force
exactly one double root `r` to the right of all its other roots. Hence

    partial_z^2 Q_n(r)=2 n! product_gamma(r-gamma)>0,
    partial_t Q_n(r)=n Q_(n-1)(r)<0.

The second sign follows directly from the one positive-root factor of `g`.
The case `n=2` was independently checked exactly, including the derivative
signs; the statement about other roots is then vacuous.

For clarity, the local collision conclusion can be made precise by factoring
off the persistent simple roots. With `s=t-t_0`, the remaining monic factor
has form `(z-r)^2+A(s)(z-r)+B(s)`, with `A(0)=B(0)=0` and
`B'(0)=2 partial_t Q_n(r)/partial_z^2 Q_n(r)<0`. Its discriminant has
strictly positive derivative at zero. It thus has two simple real roots for
small `s>0`, and a nonreal conjugate pair for small `s<0`. All persistent
roots stay in `(-1,0)`. This verifies both the splitting coefficient in the
proof and its orientation.

Consequently every negative admissible collision is a left boundary with
admissibility immediately to its right. Every negative admissible simple-root
parameter is interior. The discriminant has finitely many zeros because it
is a polynomial in `t` and is nonzero at `t=1/2`. Any extra admissible
component below zero would have a right boundary of one of these two kinds,
which is impossible. The component meeting zero is nonempty by the quadratic
inclusion. It follows that its form is `[-c_n,0]`, with
`(sqrt(2)-1)/2<=c_n<b`. Reflection and `[0,1]` complete exactly the asserted
interval equality. At the left endpoint the double-root classification applies;
reflection gives the right endpoint, with the parameter-derivative sign reversed.

## Independent computational evidence

`audit/referee-check.py` does not import or run the proposer implementation.
It reconstructs the operator symbolically, obtains the two Bernstein
certificates using rational interpolation, and uses SymPy's exact root-count
and polynomial-gcd routines instead of the saved custom Fraction/Sturm routine.
The record is `audit/referee-check.json`. All of the following passed:

- Twenty algebra, endpoint, metadata, and integrity checks.
- All 72 serialized operator inputs: exact output coefficients, evaluation
  signs, coefficient-bound equality where applicable, squarefreeness, and root
  counts in `(-infinity,-1)`, `(-1,0)`, `(0,infinity)`. There are 36 equality
  cases. Saved sign-variation counts also agree with the independent counts.
- Twenty-seven additional exact operator inputs, with widely separated negative
  roots, roots close to both endpoints, and `lambda/Lambda` equal to `1`,
  `999999/1000000`, or `1/1000000`. The tested parameters are `-3/10`,
  `-299999/1000000`, and `-1/1000000`.
- Six shifted powers built directly from finite differences: degrees 15, 17,
  and 21, each at `t=-3/10` and `t=-1/1000`. Their exact counts are
  `[0,m-1,1]` and their gcd with their derivative is constant.

These are finite checks of the proposed argument and certificates. The
quantified conclusions rest on the mathematical reconstruction above. No
floating-point root decisions, proof-assistant certification, additional agents,
or other model processes were used.

## Source comparison and contribution

The nearest source is
[Vishnyakova, arXiv:2607.06207v1](https://arxiv.org/html/2607.06207v1).
Its Example 5.7 and Conjecture 5.8 pose the same interval/nesting conjunction.
Equations (3)--(8), Statement 2.1, Example 5.3, and Theorem C supply the
transform, reflection, quadratic baseline, and multiplication closure used here.
The live [arXiv record](https://arxiv.org/abs/2607.06207) still lists only v1
at this review date. The all-even exterior connectedness argument is a
substantial delta from those statements, and reduces admissibility for each
even degree to one boundary rather than possible separated parameter components.

[Janson, Euler--Frobenius numbers and rounding](https://arxiv.org/html/1305.3512),
Remark A.2, places its simple negative-root assertion in `0<rho<=1`, with
the stated endpoint extensions. Equation (A.20) is consistent with the
parameter derivative after the coordinate change. These statements do not
provide the new exterior odd-degree induction.

[Karp--Vishnyakova, arXiv:2509.13897v1](https://arxiv.org/html/2509.13897v1),
Lemma 3, requires that every input numerator root avoid `[0,1]`, including in
its opposite-sign case. Here the positive `Q` root becomes a numerator root
`lambda/(1+lambda)` in `(0,1)`. Thus this lemma cannot be iterated directly
to supply the claimed induction. This is a specific hypothesis comparison,
not a claim that adaptation of other ideas in that paper is impossible.

I also inspected the cited comparison with
[Dubeau--Savoie, More on the roots of Euler--Frobenius polynomials](https://www.labmath.uqam.ca/~annales/volumes/22-1/PDF/031-042.pdf).
The introduction uses spline parameters in `[0,1]`; Theorems 12 and 13 apply
to recurrence (G) with positive `r_n` and nonzero `c_n`. In coordinates
`x=2z+1`, the present `2T_t` has differential expression
`(x^2-1)D+x+(2t-1)`, whereas (G) uses `(x^2-1)D+2r_n x`.
The extra constant term does not disappear in the exterior strip. Those
inspected theorems do not directly identify the submitted result as a corollary.

The bounded current search included the original title and identifier, shifted
totally positive even powers, and Euler--Frobenius roots with negative/exterior
parameters and odd degree. No equivalent theorem was found in the inspected
primary statements. Search snippets and generated conjecture registries were
not used to establish priority or mathematical status. Older literature has
not been exhausted; this is not an unconditional priority certification.

## Decision and limits

No mathematical gap was found in the exact frozen scope. The uniform sign
estimate is nontrivial and has a concrete all-degree consequence for the
source conjecture, so this is neither a finite-degree toy restriction nor just
the known multiplication corollary. The operator, odd-degree, and interval
results belong together in one result note.

Acceptance covers all clauses in `claim.json`, with no weakening of the
parameter interval, exclusion of coefficient-bound equality, or loss of
endpoint multiplicities. No sharpness of `-3/10` is asserted. Successive
nesting and the contextual limit question remain unproved here. A manuscript
may describe the interval-shape part as proved, but must retain the unresolved
status of the original conjunction and the bounded literature language. This
report is a fresh model-context mathematical review, not external peer review.
