# The third-position kernel and uniform third boundary inequalities

Job: `primary-20260913-binary-subsum-shape-research-9e631dc6dcdd`.
This completes the assigned kernel test. The original conjecture is unresolved.

## Statement and dependence on the previous dossier

Let K3_m(l,t) be exactly equation (10) of `research-boundary-proof.md`, with
the linear coefficient functionals in its equations (1) and (9). Then

    K3_m(l,t)>=0 for integers m>=5 and 0<=l<=t<=m.          (K1)

Consequently, for every even n>=6,

    T_3(N_n)>T_3(A_n)>0,

and the same holds at j=d(n)-3 by palindromicity. The cases n=6,8 are
checked explicitly below; (K1) proves compensation for even n>=10.
Together with the previous first- and second-position proof this gives
strict log-concavity for all n>=6 at j=1,2,3 and their reflections. Odd
indices use the prior equality N_(2m+1)=N_(2m).

The previous dossier derives coefficient identities from the prior recurrence;
its argument is a dependency, not an assumption that computation proved them.
Its old statement that the K3 assertion was unproved is superseded by this file.

## Closed tail formulas

Put q=floor(m/2), delta=m mod 2, epsilon=z mod 2, and

    S_r(z,m)=sum_(k=z)^m k^r,
    H_r(z,q)=sum_(k=z)^q k^r if z<=q, and 0 otherwise,
    E_z=(q-(z-epsilon)/2)*(q-(z-epsilon)/2+1-epsilon).

For a tail weight vector w_k=1_(k>=z), equation (9) in the previous dossier
can be summed in the other order. Its quartic terms respectively give

    sum_(k=z)^m [binom(2k,4)+z*binom(2k,2)],
    2*sum_(h=z)^q h^2*(m-2h+1),
    2*sum_(h=z)^m h^2*(m-h),
    sum_(even k<=m)(k-z)_+ = E_z.

The first expression uses k*w_k-sum_(h<k)w_h=z for k>=z and zero before.
The second counts k=2h,...,m, the third counts k=h+1,...,m, and the final
sum is an arithmetic progression starting at the first even k>z.
Writing v_r=S_r(z,m), the needed tail coefficients are therefore

    p2 = 2*v2,
    p3 = 4*v3/3-v2+(2*m+5/3)*v1-(m*m+m)*v0,
    p4 = 2*v4/3-2*v3+11*v2/6-v1/2
         +z*(2*v2-v1)+2*m*v2-2*v3
         +2*(m+1)*H2-4*H3+E_z,
    a2 = 2*m*m-m+z,
    a3 = (4*m^3+2*m)/3-2*m*(m-z),
    a4 = binom(2*m,4)+binom(2*m,2)*z+2*H2.             (K2)

These identities hold for the formal tail weights as defined, whether or not
those weights are actual binary partition counts. They are the same formal
extension as the assigned kernel. The power sums are F_r(m)-F_r(z-1), where

    F0(y)=y+1, F1(y)=y(y+1)/2, F2(y)=y(y+1)(2y+1)/6,
    F3(y)=y^2(y+1)^2/4,
    F4(y)=y(y+1)(2y+1)(3y^2+3y-1)/30.

F0(-1)=0 handles z=0. For H_r use these differences only on the active
branch z<=q, and otherwise use zero. Substitution in the assigned equation
(10) gives the exact piecewise polynomial 2*K3.

## Complete certificate domain

Use nonnegative integer gaps u,b,c and delta in {0,1}. Set m=2(u+b+c)+delta.
The following chambers cover 0<=l<=t<=m; equality overlaps cause no difficulty.

| Chamber | l | t | Additional condition | Active H terms |
|---|---|---|---|---|
| LL | u | u+b | none | both |
| HH | 2u+b+c+delta | 2u+2b+c+delta | u>=1-delta | neither |
| LH1 | u | 2u+b+2c+delta | u+c+delta>=1 | l only |
| LH2 | b+u | b+2u+c+delta | u>=1-delta | l only |

For LL, the inverse gaps are (l,t-l,q-t). For HH they are
(l-q-delta,t-l,m-t). For l<=q<t, use LH1 when t>=q+l+delta, with gaps
(l,m-t,t-q-l-delta). Otherwise use LH2 with gaps
(t-q-delta,q+l+delta-t,q-l). Thus every required pair is covered by a
nonnegative integer gap vector with the stated restrictions.

For delta=0 split LH1 into u>=1 (LH1u), and u=0,c>=1 (LH1c).
Shift each compulsory lower bound, then write each free gap as its shifted
residue plus twice a nonnegative integer. The fixed u in LH1c remains zero.
This yields 68 parity roots. Finally m>=5 is the condition

    X0+X1+X2 >= max(0,ceil((3-delta-sum(gap_base))/2)).    (K3)

The fixed X0 in LH1c equals zero. It contributes nothing to the sum.

`research_kernel3.json` gives 144 leaves covering these roots. For each row,
the actual gap coordinate is

    gap_i=gap_base_i+2*(offset_i+Y_i)

when fixed_i=false, with Y_i any nonnegative integer; when fixed_i=true,
put Y_i=0. The row's `terms` are the complete coefficient list of

    1440*K3_m(l,t) = sum_(a,b,c) coefficient_(a,b,c)*Y0^a*Y1^b*Y2^c.

Every listed coefficient is a nonnegative integer; all omitted monomials
have coefficient zero. There are 12325 listed monomials altogether.
The scale is positive, so every such identity proves K3>=0 on its leaf.

For a finite, complete verification of the infinite coverage, note that every
leaf offset is at most 2. Clipping each X_i at 3 preserves every leaf's lower
bound or fixed-equality membership: fixed equalities are at 0,1,2 only.
It also preserves (K3), whose threshold is at most 2. Therefore it suffices
to check X_i in {0,1,2,3} on each of the 68 roots, respecting fixed axes.
The independent verifier checks all 4119 valid clipped vectors and finds a
covering leaf for each. It also checks each entire leaf is contained in the
stated m,l,t domain and has the prescribed parity and active branches.
This is an infinite-domain coverage argument, not extrapolation from m<=48.

The generator uses exact SymPy expansion. A separate verifier, importing
neither SymPy nor the generator, recomputes all 144 polynomial identities
using Fraction polynomial arithmetic and compares every monomial. Both scripts
are retained. The verifier additionally compares 20790 literal kernel entries
for 5<=m<=48 and checks their gap mapping. These literal checks are calibration
only; the identities and complete coverage prove (K1).

## Strictness and the comparison term

For the actual counts w_k=B(k), let e0=w0=1 and e_l=w_l-w_(l-1)>=0.
Linearity and expansion of the quadratic Turan expression give exactly

    T3(N_(2m))-T3(A_(2m)) = sum_(l,t) e_l*e_t*K3_m(l,t).

K3 is symmetric, so (K1) controls the whole double sum. For strictness,
1440*K3_m(0,0), after m=2z+6 and m=2z+5 respectively, has the following
coefficient arrays in ascending powers of z:

    even: [46638720,139543488,175898688,123122688,52593728,
           14069952,2302592,210432,8192],
    odd:  [8985600,34793280,55319456,48077056,25219648,
           8213440,1623424,177664,8192].

All are strictly positive. Thus e0^2*K3_m(0,0)>0 for m>=5.

It remains to justify T3(A)>0, rather than assuming that A is log-concave.
Let w=w_m>0, R=sum_(k<m)w_k, L=m*w-R>=0, and
Q=2*sum_(h=0)^floor(m/2) h^2*w_h. Put C_i=binom(2m,i) and
q2=2*sum_(h=0)^floor(m/2)h^2. Monotonicity gives Q<=q2*w. Since

    a2=C2*w+L, a3=C3*w+2m*L, a4=C4*w+C2*L+Q,

we obtain

    T3(A) >= alpha*w^2+beta*w*L+(4m^2-C2)*L^2,
    alpha=C3^2-C2*(C4+q2),
    beta=4m*C3-C2^2-C4-q2.                              (K4)

For m=2z+4, z>=0, the polynomials 9*alpha and 3*beta have ascending
coefficient arrays

    [8064,28632,41224,31014,12916,2832,256],
    [96,406,463,206,32].

For m=2z+5 they are

    [40500,105300,113725,65304,21028,3600,256],
    [465,1056,823,270,32].

These positive expansions, and 4m^2-C2=2m^2+m>0, prove T3(A)>0 for m>=4.
For n=6 the triples (c2,c3,c4)=(54,80,100) and (a2,a3,a4)=(32,52,62)
give T3(N)=1000>T3(A)=720>0. For n=8 the triples
(182,406,738) and (122,304,578) give 30520>21900>0.
This completes the asserted third-position theorem and its reflected version.

## Audit limits

Gap list: none known for the stated kernel and boundary arguments.
Two exact arithmetic implementations are not a fresh mathematical referee.
No remaining central-index inequality or optimal boundary width is claimed.
The growing-boundary argument in `research-growing-boundary-proof.md` is a
separate elementary argument; it does not rely on these polynomial certificates.
