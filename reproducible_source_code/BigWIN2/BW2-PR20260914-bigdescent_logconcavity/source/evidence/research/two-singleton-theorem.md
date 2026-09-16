# A sharp conditional two-position inequality

Job: primary-20260914-bigdescent-logconcavity-research-6ff0786c2423.
Status: proved by the reduction and finite exact polynomial certificate below;
same-worker verification only. No fresh referee, novelty certification, or
qualified publication candidate is claimed.

## Statement and interpretation

For a binary word w of length n ending in 1, let E(w) contain the ending
positions of its 10 and 011 factors. Put a_n(S)=#{w:E(w)=S}, including zero
for unattainable sets. For every n>=3, distinct i,j in {2,...,n}, and
S contained in {2,...,n}\{i,j},

    a_n(S) a_n(S union {i,j})
        <= 2 a_n(S union {i}) a_n(S union {j}).                 (1)

All indicators outside i,j are fixed, including their absences. The inequality
is stated for counts and includes zero-count cases; no conditional probability
with a zero denominator is used. Factor 2 is optimal: n=4, i=2, j=4, S=empty
gives the four counts (a00,a10,a01,a11)=(2,1,1,1). The respective words are
{0001,1111}, {1001}, {0011}, {1011}. Thus ordinary conditional negative
correlation (the same inequality with factor 1) is false.

In the pair-profile notation of profile-reduction.md, a profile with m entries
equal to 2, two entries equal to 1, and any number of zeros has

    H_e=(xy)^m [a00 a11 (x^2+y^2)+2 a10 a01 xy]
       = a00 a11 s_(m+2,m)
          +(2 a10 a01-a00 a11) s_(m+1,m+1).

Consequently all such profiles are Schur-positive, with no bound on degree,
length, spacing, or number of common events. Profiles with zero or one entry
equal to 1 are Schur-positive directly. This proves an infinite special case
of the stronger assertion under investigation. It does not establish the
full weighted assertion or the frozen 21-family original.

## Matrix theorem

Use P,Q,v,u from profile-reduction.md. Define the output row cone and input
column cone by their nonnegative generators:

    O: (1,0,0), (0,1,0), (1,0,1), (0,1,1);
    I: (1,0,0), (1,1,0), (1,0,1), (1,1,1).

For every l in O, r in I, and every product M of P and Q, including the
empty product, define

    A=l P M P r, B=l Q M P r, C=l P M Q r, D=l Q M Q r.

Then AD<=2BC. This includes nonnegative real combinations of the generators.

The cones are preserved respectively by right and left multiplication by
P,Q. For the four generators in their displayed orders, their images are:

| operation | images in the same cone's generator basis |
|---|---|
| output times P | o0, o0, o2, o2 |
| output times Q | o3, 0, o1+o3, o1 |
| P times input | i1, i1, i3, i3 |
| Q times input | 0, i2, i0, i0+i2 |

Since u^T=o3 and v=i2, the transfer factors outside the two selected
positions give l in O and r in I. The intervening factors give M. The four
counts are exactly A,B,C,D, possibly exchanging B,C according to position
order, which does not affect their product. Thus the matrix theorem implies
(1).

## Complete reduction of the intervening word

P^2=P, so delete repeated P's in its matrix word. Q^2 has rank one, so any
word containing QQ has rank at most one. If M=ab^T (including the zero case),
direct multiplication gives AD=BC. Such words satisfy the theorem.

Every remaining nonempty word is alternating. Direct matrix multiplication
gives

    P Q P Q P = P Q P + P,
    Q P Q P Q = Q P Q + Q,
    (P Q)^3 = (P Q)^2 + P Q,
    (Q P)^3 = (Q P)^2 + Q P.

Multiplying these identities by the appropriate alternating suffixes proves
that every alternating word belongs to one of the following four cones:

    cone(P,PQP), cone(Q,QPQ),
    cone(PQ,(PQ)^2), cone(QP,(QP)^2).

The coefficients follow the nonnegative Fibonacci recurrence; the first two
words in each parity/starting-letter family are the displayed generators.
Include cone(Id) for the empty word. This exhausts every possible M.

## Finite polynomial proof for the five families

In each family write l=sum L_a o_a, r=sum R_b i_b, and M=sum Z_c M_c,
with all parameters nonnegative. The polynomial 2BC-AD is homogeneous of
degree two separately in L, R, and Z. It therefore has exactly 100 possible
coefficient positions for the one-generator family and 300 for each of the
four two-generator families, including positions with coefficient zero.

The certificate two_singleton_certificate.json lists all 1,300 coefficients,
their matrices, and the unambiguous index order. Every coefficient is a
nonnegative integer. The accompanying script obtains a coefficient by
polarizing the integer table

    (o_a P M_c P i_b, o_a Q M_c P i_b,
     o_a P M_c Q i_b, o_a Q M_c Q i_b).

For an unordered pair in each parameter group, sum 2 B_first C_second
- A_first D_second over the two assignments for distinct indices and one
assignment for equal indices. This is exactly polynomial multiplication,
so the table is a finite algebraic positivity certificate, not an empirical
parameter sample. A separate SymPy expansion checks every coefficient,
including zeros, and checks that no extra nonzero monomials occur. The
script also verifies every matrix identity and cone-generator image above.
This completes the proof of the matrix theorem and (1).

The direct-word audit in pass2_audit.json checks the count interpretation
without a suffix recurrence. These deterministic cross-checks do not
constitute a fresh mathematical referee.

## Limitation of a tempting enlargement

One must keep the four alternating families separate. The theorem fails
if M is allowed to be an arbitrary nonnegative combination of all P,Q
products: take l=(1,0,0), r=(2,1,0), M=Id+2 Q^2. These give
(A,B,C,D)=(6,2,1,1), hence 2BC-AD=-2. All boundary hypotheses still hold,
but this M is not a permitted single word. Thus replacing the semigroup
by its whole positive hull would invalidate this proof premise.

## One next test

Extend the polynomial certificate to four singly occupied positions. Their
three intervening common-event blocks are each rank at most one or belong
to one of the five alternating families above. Test both Schur differences
of the resulting degree-four scalar as polynomials in nonnegative boundary
and gap parameters. A negative parameter coefficient rejects this proposed
positive-coefficient proof premise; it is not automatically a counterexample
for actual matrix words. A successful certificate would give another
unbounded-degree special case, beyond merely increasing a length cutoff.
