# Proof dependency graph

## Certified endpoint N3

**N3.** For every real `3 x 3` matrix `T` of rank at most two,

`per([[T,T],[T,T]]) <= 20 per(T)^2`.

Dependencies:

1. **L1 (exact permanent expansion).**  If
   `A_ij=c_j+a_i d_j`, then direct permutation expansion gives both normal
   form identities stored in `certificates/n3_sos_certificate.json`.
2. **L2 (three row-line strata).**  A rank-two factorisation `T=UV^T` has,
   after excluding zero rows, either three distinct row projective lines or
   one repeated line.  Three equal lines would force rank at most one.
3. **L3 (projective normalisation).**  A real `GL_2` change in the factor
   space sends the two strata to `a=(-1,0,1)` and `a=(0,0,1)`, respectively;
   row scalings multiply the target gap by a square.
4. **L4 (SOS nonnegativity).**  Each identity in L1 is a sum of squares with
   nonnegative quadratic weights over the reals.
5. **L5 (zero and rank-one strata).**  A zero row/column makes both
   permanents zero.  For rank at most one the two sides are equal by direct
   factorial evaluation.
6. **N3** follows from L1--L5 without division by `per(T)`.

Status: proved.  L1 has two exact independent implementations, including a
pure-standard-library reconstruction from all `3!` and `6!` permutations.
L2--L5 and every boundary/equality stratum were independently reconstructed
in `audit/agents/builder.md` and `audit/agents/referee.md`.

## Certified equality classification

For rank at most one, equality always holds.  For rank two, the certified
classification is: equality holds exactly when `T` has a zero row or zero
column, or after row/column permutations it contains a `2 x 2` all-zero
submatrix.  This follows from the vanishing conditions of the two homogeneous
SOS normal forms and passed the independent referee and symbolic family
checks.
