# Fresh mathematical audit

**Frozen claim.**  I reviewed the snapshot with digest
`5d141b6b1ca16a35121e8276a6b73a6a96c20f2f114c8cfd125fce39b27bcf47`.
I recomputed every listed file hash and the canonical snapshot digest; all
matched `audit/snapshot.json`.  The claim is the full conjunction

1. `G_2(20,8,7)` is nonempty;
2. `M_2(20,8,7)` is empty;
3. `M_2(20,8,6)` is nonempty.

The regions are exactly the real LP systems displayed in `problem.md`; the
claim makes no assertion about existence of an LCD code.

## Reconstruction of the exact systems

For the mixed system I used the variable order consisting of 21 `A`
coordinates, 21 `B` coordinates, and the 1771 lexicographically enumerated
compositions `(a,b,c,e)` of 20.  Thus there are 1813 nonnegative variables.
For compositions `s,t`, set

\[
T_{t,s}=[x^t]\prod_{i=0}^3\left(\sum_{j=0}^3H_{ij}x_j\right)^{s_i}.
\]

The coefficient form of the joint MacWilliams identity is therefore

\[
2^{20}M_t-\sum_sT_{t,s}M_s=0
\quad(t\in I_{20}).
\]

The supplied standalone generator constructs `T` inductively: remove one
factor from the last nonzero coordinate of `s`, then multiply the already
constructed column by the corresponding row-linear form of `H`.  Induction on
the total degree proves that this recurrence gives precisely the displayed
coefficient.  Its integer arithmetic is safe: before collection, the absolute
coefficient sum of any degree-20 column is at most `4^20 = 2^40`, well within
signed 64-bit range; certificate accumulation itself uses arbitrary-precision
integers.

I checked the row construction term by term against `problem.md`: normalization,
the `A` distance zeros, all 21 Hamming MacWilliams equations, the three stated
families of mixed zeros, both axes, both scaled marginals, the binomial
marginal, and all 1771 joint-transform coefficients are present.  The resulting
counts are 3099 equalities at `d=6` and 3205 at `d=7`; the latter also has 20
packing inequalities, although the infeasibility certificate below does not
need them.

As an additional attack on the most error-prone component, I independently
expanded 19 strategically chosen columns of `T` by repeated polynomial
multiplication and compared all 1771 coefficients in each column.  Every
coefficient agreed.  I also checked `H^2=4I` and the induced full-matrix identity
`T^2=4^20 I` modulo each of 32749, 65519, and 65521.  These computational checks
support, but are not substitutes for, the inductive coefficient argument above.

## Positive Gauss claim

The sparse point in `evidence/gauss_d7_rational_point.json` is integral.  Its
nonzero primal coordinates are

\[
\begin{aligned}
&A_0=1,\quad (A_7,\ldots,A_{14})=(36,53,28,36,28,18,36,20),\\
&B_0=1,\ B_2=1,\ (B_5,\ldots,B_{16})=
(84,203,260,440,680,727,680,524,260,125,84,27),
\end{aligned}
\]

with all omitted coordinates zero.  The branch `(tau,beta,eta)=(O,0,0)` is
admissible because its dual type is `O`, `(E,E)` is irrelevant, and
`(20-0) mod 8=4` lies in `B_O(12)`.  Here `A_20=0`, and the three phase sums are
respectively

\[
1+53+18=72,\qquad 28+36=64,\qquad 36+20=56,
\]

which are exactly the branch targets.  Fresh exact replay independently
recomputed all 21 Krawtchouk rows, all 20 packing rows, normalization,
nonnegativity, six distance-zero rows, the eta row, and the three phase rows.
Every row passed.  This is a rational witness for
`G_2(20,8,7) != empty`.

## Positive mixed claim at `d=6`

The sparse point in `evidence/mixed_d6_rational_point.json` has 617 nonzero
rational coordinates among the 1813 variables.  I validated every listed
index, rational denominator, and variable label; omitted entries are zero.
After taking the exact common denominator (333-bit), fresh replay checked
nonnegativity, all 3099 equality rows, all 20 packing rows, and all 3,136,441
generated entries of the joint transform with integer arithmetic.  Every row
passed exactly.  Hence this serialized point proves
`M_2(20,8,6) != empty` over the rationals, and therefore over the reals.

## Mixed infeasibility at `d=7`

Write the 3205 equality rows as `E x=b`, with all 1813 variables constrained by
`x>=0`.  The certificate in `evidence/mixed_d7_farkas.json` supplies an exact
rational vector `y` and the vector `s=E^T y`.  Fresh reconstruction and replay
gave

\[
y^Tb=-\frac{73714918700799625629}{73786976294838206464}<0,
\]

while every coordinate of `s` is positive.  With common denominator `2^86`,
the minimum numerator of `s` is `2^52`; all 1813 coordinates were recomputed,
not inferred from a tolerance.  The replay used 1703 nonzero equality
multipliers, matched every row index and row name, and obtained exact
coefficient cancellation.  The packing multipliers are zero, so the
certificate already contradicts the larger system without packing:

\[
0\le s^Tx=(E^Ty)^Tx=y^T(Ex)=y^Tb<0.
\]

Thus `M_2(20,8,7)` is empty.

## Scope, source comparison, and verdict

The three certificates decide all three conjuncts at their frozen quantifiers;
there is no silent restriction or endpoint extrapolation.  In particular, the
`d=7` mixed conclusion is an exact Farkas argument, not a solver-status claim,
and the two nonemptiness conclusions are complete serialized rational points.

The frozen `source.md` and `problem.md` describe the nearest inspected result as
the `(20,8):7->6` floating-point screening observation in Kang--Xiong and state
that it was excluded from that paper's exact endpoint claims.  The present
delta is precisely the exact certification requested in the immutable source.
The cited PDF was not among the snapshot-listed files and, under this job's
explicit evidence restriction, I did not use it to certify bibliography or
priority; those matters remain for the later citation audit.  No priority or
broader code-existence assertion is needed for the mathematical conclusion.

**Verdict: ACCEPT.**  The `resolution-paper` scope, exact correctness evidence,
and stated contribution pass mathematical review.  The original frozen claim
has status `proved`.
