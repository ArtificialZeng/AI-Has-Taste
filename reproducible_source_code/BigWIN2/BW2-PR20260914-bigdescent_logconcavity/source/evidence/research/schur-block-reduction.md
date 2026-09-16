# Schur-positive reduction of runs of singleton entries

Job: primary-20260914-bigdescent-logconcavity-research-6ff0786c2423.
The notation and transfer interpretation are those of profile-reduction.md.
This is a proved reduction, not a solution of arbitrary profiles.

Write q=xy, s=x+y, h2=x^2+xy+y^2. The last two polynomials are the
two-variable Schur functions s_(1) and s_(2); q=s_(1,1). Direct multiplication
of the 9 by 9 pair-transfer matrix R=R1 gives the exact identity

    R^8 = q R^6 + q s R^5 + 5 q^2 R^4 + 2 q^2 s R^3
          + q^2 h2 R^2 + q^3 s R.                         (1)

The script schur_blocks.py verifies all 81 polynomial entries. It records
the other identities R0^2=R0, R2^3=0, and R2 R1 R2=0. Thus a profile
containing 222 or 212 has zero scalar, irrespective of the surrounding
profile. Every run of at least eight consecutive 1s can be replaced by a
positive Schur-linear combination of shorter runs, in arbitrary context.

To justify positivity propagation, the product of two two-variable Schur
polynomials is Schur-positive. Explicitly, if a>=b and c>=d, write r=a-b,
t=c-d. Then

    s_(a,b) s_(c,d)
      = sum_{j=0}^{min(r,t)} s_(a+c-j,b+d+j).

This follows by multiplying the two finite geometric sums defining the
Schur polynomials and comparing coefficients. Therefore (1) is a valid
positivity reduction. Iteration terminates since every replacement decreases
the run length by at least two. Combined with zero compression, arbitrary
profile Schur positivity is equivalent to the assertion restricted to
profiles with no 00, no 222, no 212, and no run of eight 1s. The restricted
language is still infinite: this is not a finite all-degree test.

For a profile 0^a 1^r 0^b with a,b each 0 or 1, the eight base values
r=0,...,7 are Schur-positive. All 32 exact Schur coefficient rows are in
schur_blocks.json. Equation (1), multiplied by R^(r-8), proves positivity
for every r>=8, for each boundary choice. Longer boundary zero runs have
the same scalar. This supplies an unbounded-degree special case.

For no boundary zeros, an additional scalar identity is

    sum_{r>=0} H_(1^r) z^r = N(z)/D(z),
    N=1+q z^2+2q s z^3+3q^2 z^4+2q^2 s z^5+q^2 h2 z^6,
    D=1-q z^2-q s z^3-5q^2 z^4-2q^2 s z^5-q^2 h2 z^6-q^3 s z^7.

The coefficient recurrence (1), together with eight initial coefficients,
verifies this formal identity; the denominator has constant term 1.
Expansion of 1/D as a formal geometric series is another positivity proof
for this family. No analytic convergence assertion is involved.

Two stronger proof premises fail on the actual profile (1,0,1). Its CC
tensor-state component is x^2+y^2=s_(2)-s_(1,1), while its accepted scalar
is 2(x^2+xy+y^2)=2s_(2). Thus requiring every diagonal state to be
Schur-positive is invalid. Also the accepted scalar has gamma expansion
2(x+y)^2-2xy, so nonnegative gamma coefficients cannot replace Schur
positivity here. Neither failure disproves the accepted-scalar assertion.

The exhaustive pass-two test schur_profiles.json checks every compressed
profile of total degree 0..14, including odd degrees: 3,211,434 profiles,
21,122,732 nontrivial Schur inequalities, no failures. Its independent
profile-count formula is sum_{l=ceil(d/2)}^d binom(l,d-l) 2^(l+1) for d>0;
d=0 has the empty and one-zero profiles. This proves coverage of the finite
degree domain. Together with zero compression it covers those degrees at
every length. These are finite exact results and explicit structural special
cases; no proof for arbitrary reduced profiles, fresh referee, or novelty
certification is claimed.
